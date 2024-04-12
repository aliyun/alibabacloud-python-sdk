# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_bastionhost20191209 import models as yundun_bastionhost_20191209_models
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

    def accept_approve_command_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AcceptApproveCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AcceptApproveCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptApproveCommand',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AcceptApproveCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_approve_command_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AcceptApproveCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AcceptApproveCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptApproveCommand',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AcceptApproveCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_approve_command(
        self,
        request: yundun_bastionhost_20191209_models.AcceptApproveCommandRequest,
    ) -> yundun_bastionhost_20191209_models.AcceptApproveCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_approve_command_with_options(request, runtime)

    async def accept_approve_command_async(
        self,
        request: yundun_bastionhost_20191209_models.AcceptApproveCommandRequest,
    ) -> yundun_bastionhost_20191209_models.AcceptApproveCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_approve_command_with_options_async(request, runtime)

    def accept_operation_ticket_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AcceptOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AcceptOperationTicketResponse:
        """
        You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effect_count):
            query['EffectCount'] = request.effect_count
        if not UtilClient.is_unset(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not UtilClient.is_unset(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptOperationTicket',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AcceptOperationTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_operation_ticket_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AcceptOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AcceptOperationTicketResponse:
        """
        You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effect_count):
            query['EffectCount'] = request.effect_count
        if not UtilClient.is_unset(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not UtilClient.is_unset(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptOperationTicket',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AcceptOperationTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_operation_ticket(
        self,
        request: yundun_bastionhost_20191209_models.AcceptOperationTicketRequest,
    ) -> yundun_bastionhost_20191209_models.AcceptOperationTicketResponse:
        """
        You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptOperationTicketRequest
        @return: AcceptOperationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_operation_ticket_with_options(request, runtime)

    async def accept_operation_ticket_async(
        self,
        request: yundun_bastionhost_20191209_models.AcceptOperationTicketRequest,
    ) -> yundun_bastionhost_20191209_models.AcceptOperationTicketResponse:
        """
        You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptOperationTicketRequest
        @return: AcceptOperationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.accept_operation_ticket_with_options_async(request, runtime)

    def add_databases_to_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AddDatabasesToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddDatabasesToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDatabasesToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddDatabasesToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_databases_to_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AddDatabasesToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddDatabasesToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDatabasesToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddDatabasesToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_databases_to_group(
        self,
        request: yundun_bastionhost_20191209_models.AddDatabasesToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddDatabasesToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_databases_to_group_with_options(request, runtime)

    async def add_databases_to_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AddDatabasesToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddDatabasesToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_databases_to_group_with_options_async(request, runtime)

    def add_hosts_to_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        """
        You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: AddHostsToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddHostsToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddHostsToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddHostsToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_hosts_to_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        """
        You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: AddHostsToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddHostsToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddHostsToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddHostsToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_hosts_to_group(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        """
        You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: AddHostsToGroupRequest
        @return: AddHostsToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_hosts_to_group_with_options(request, runtime)

    async def add_hosts_to_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        """
        You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: AddHostsToGroupRequest
        @return: AddHostsToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_hosts_to_group_with_options_async(request, runtime)

    def add_users_to_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        """
        #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](~~204596~~) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
        # Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddUsersToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddUsersToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_to_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        """
        #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](~~204596~~) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
        # Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddUsersToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddUsersToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users_to_group(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        """
        #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](~~204596~~) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
        # Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddUsersToGroupRequest
        @return: AddUsersToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_group_with_options(request, runtime)

    async def add_users_to_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        """
        #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](~~204596~~) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
        # Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddUsersToGroupRequest
        @return: AddUsersToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_users_to_group_with_options_async(request, runtime)

    def attach_database_accounts_to_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDatabaseAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_database_accounts_to_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDatabaseAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_database_accounts_to_user(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_database_accounts_to_user_with_options(request, runtime)

    async def attach_database_accounts_to_user_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_database_accounts_to_user_with_options_async(request, runtime)

    def attach_database_accounts_to_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDatabaseAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_database_accounts_to_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDatabaseAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_database_accounts_to_user_group(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_database_accounts_to_user_group_with_options(request, runtime)

    async def attach_database_accounts_to_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_database_accounts_to_user_group_with_options_async(request, runtime)

    def attach_host_accounts_to_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_accounts_to_host_share_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_host_accounts_to_host_share_key(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_host_share_key_with_options(request, runtime)

    async def attach_host_accounts_to_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_accounts_to_host_share_key_with_options_async(request, runtime)

    def attach_host_accounts_to_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_accounts_to_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
        @param request: AttachHostAccountsToUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostAccountsToUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_accounts_to_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        """
        After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
        @param request: AttachHostAccountsToUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostAccountsToUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_host_accounts_to_user_group(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        """
        After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
        @param request: AttachHostAccountsToUserGroupRequest
        @return: AttachHostAccountsToUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_user_group_with_options(request, runtime)

    async def attach_host_accounts_to_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        """
        After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
        @param request: AttachHostAccountsToUserGroupRequest
        @return: AttachHostAccountsToUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_accounts_to_user_group_with_options_async(request, runtime)

    def attach_host_group_accounts_to_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostGroupAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_group_accounts_to_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostGroupAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostGroupAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_host_group_accounts_to_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostGroupAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.authorized_security_groups):
            query['AuthorizedSecurityGroups'] = request.authorized_security_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigInstanceSecurityGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_security_groups_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_security_groups):
            query['AuthorizedSecurityGroups'] = request.authorized_security_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigInstanceSecurityGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        ## Usage notes
        You can call this operation to configure a whitelist of public IP addresses for a bastion host. By default, a bastion host is accessible from all public IP addresses. If you want to allow the requests from specific public IP addresses, you can call this operation to add trusted IP addresses to the whitelist of the bastion host.
        ## Limits
        You can call this operation up to 30 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigInstanceWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigInstanceWhiteList',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_white_list_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        """
        ## Usage notes
        You can call this operation to configure a whitelist of public IP addresses for a bastion host. By default, a bastion host is accessible from all public IP addresses. If you want to allow the requests from specific public IP addresses, you can call this operation to add trusted IP addresses to the whitelist of the bastion host.
        ## Limits
        You can call this operation up to 30 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigInstanceWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigInstanceWhiteList',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_instance_white_list(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        """
        ## Usage notes
        You can call this operation to configure a whitelist of public IP addresses for a bastion host. By default, a bastion host is accessible from all public IP addresses. If you want to allow the requests from specific public IP addresses, you can call this operation to add trusted IP addresses to the whitelist of the bastion host.
        ## Limits
        You can call this operation up to 30 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigInstanceWhiteListRequest
        @return: ConfigInstanceWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_instance_white_list_with_options(request, runtime)

    async def config_instance_white_list_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        """
        ## Usage notes
        You can call this operation to configure a whitelist of public IP addresses for a bastion host. By default, a bastion host is accessible from all public IP addresses. If you want to allow the requests from specific public IP addresses, you can call this operation to add trusted IP addresses to the whitelist of the bastion host.
        ## Limits
        You can call this operation up to 30 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ConfigInstanceWhiteListRequest
        @return: ConfigInstanceWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_white_list_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_port):
            query['DatabasePort'] = request.database_port
        if not UtilClient.is_unset(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not UtilClient.is_unset(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.polar_dbendpoint_type):
            query['PolarDBEndpointType'] = request.polar_dbendpoint_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_region_id):
            query['SourceInstanceRegionId'] = request.source_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_port):
            query['DatabasePort'] = request.database_port
        if not UtilClient.is_unset(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not UtilClient.is_unset(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.polar_dbendpoint_type):
            query['PolarDBEndpointType'] = request.polar_dbendpoint_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_region_id):
            query['SourceInstanceRegionId'] = request.source_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database_account(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_account_with_options(request, runtime)

    async def create_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_account_with_options_async(request, runtime)

    def create_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not UtilClient.is_unset(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not UtilClient.is_unset(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_share_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_share_key(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_host_share_key_with_options(request, runtime)

    async def create_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_host_share_key_with_options_async(request, runtime)

    def create_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not UtilClient.is_unset(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not UtilClient.is_unset(request.proxies):
            query['Proxies'] = request.proxies
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_domain_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not UtilClient.is_unset(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not UtilClient.is_unset(request.proxies):
            query['Proxies'] = request.proxies
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_domain(
        self,
        request: yundun_bastionhost_20191209_models.CreateNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.CreateNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_domain_with_options(request, runtime)

    async def create_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.CreateNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_domain_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: yundun_bastionhost_20191209_models.CreatePolicyRequest,
    ) -> yundun_bastionhost_20191209_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.CreatePolicyRequest,
    ) -> yundun_bastionhost_20191209_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: yundun_bastionhost_20191209_models.CreateRuleRequest,
    ) -> yundun_bastionhost_20191209_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateRuleRequest,
    ) -> yundun_bastionhost_20191209_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        """
        ## Usage notes
        You can call this operation to add a user to a bastion host. You can add local users and Resource Access Management (RAM) users. After a Bastionhost administrator adds a user to a bastion host, the O&M personnel can log on to the bastion host as the user to perform O&M operations on the host on which they have permissions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not UtilClient.is_unset(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not UtilClient.is_unset(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        """
        ## Usage notes
        You can call this operation to add a user to a bastion host. You can add local users and Resource Access Management (RAM) users. After a Bastionhost administrator adds a user to a bastion host, the O&M personnel can log on to the bastion host as the user to perform O&M operations on the host on which they have permissions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not UtilClient.is_unset(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not UtilClient.is_unset(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        """
        ## Usage notes
        You can call this operation to add a user to a bastion host. You can add local users and Resource Access Management (RAM) users. After a Bastionhost administrator adds a user to a bastion host, the O&M personnel can log on to the bastion host as the user to perform O&M operations on the host on which they have permissions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        """
        ## Usage notes
        You can call this operation to add a user to a bastion host. You can add local users and Resource Access Management (RAM) users. After a Bastionhost administrator adds a user to a bastion host, the O&M personnel can log on to the bastion host as the user to perform O&M operations on the host on which they have permissions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        """
        You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](~~204600~~) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        """
        You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](~~204600~~) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_group(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        """
        You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](~~204600~~) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        """
        You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](~~204600~~) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def create_user_public_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserPublicKeyResponse:
        """
        You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
        @param request: CreateUserPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserPublicKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_public_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserPublicKeyResponse:
        """
        You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
        @param request: CreateUserPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserPublicKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_public_key(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserPublicKeyRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserPublicKeyResponse:
        """
        You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
        @param request: CreateUserPublicKeyRequest
        @return: CreateUserPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_public_key_with_options(request, runtime)

    async def create_user_public_key_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserPublicKeyRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserPublicKeyResponse:
        """
        You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
        @param request: CreateUserPublicKeyRequest
        @return: CreateUserPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_public_key_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database_account(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_account_with_options(request, runtime)

    async def delete_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_account_with_options_async(request, runtime)

    def delete_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        ## Usage notes
        This interface is used to delete individual host accounts. If a host account is no longer in use, you can invoke this interface to delete the host account for that host that has been configured on the bastion.
        >  After you remove the host account, you must enter the username and password of the host when you log on to the host in Bastionhost.
        ## QPS Limit
        The single-user QPS limit of this interface is 10 times/second. If the limit is exceeded, the API call will be stream-limited, which may affect your business, please call reasonably.
        
        @param request: DeleteHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        """
        ## Usage notes
        This interface is used to delete individual host accounts. If a host account is no longer in use, you can invoke this interface to delete the host account for that host that has been configured on the bastion.
        >  After you remove the host account, you must enter the username and password of the host when you log on to the host in Bastionhost.
        ## QPS Limit
        The single-user QPS limit of this interface is 10 times/second. If the limit is exceeded, the API call will be stream-limited, which may affect your business, please call reasonably.
        
        @param request: DeleteHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_account(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        """
        ## Usage notes
        This interface is used to delete individual host accounts. If a host account is no longer in use, you can invoke this interface to delete the host account for that host that has been configured on the bastion.
        >  After you remove the host account, you must enter the username and password of the host when you log on to the host in Bastionhost.
        ## QPS Limit
        The single-user QPS limit of this interface is 10 times/second. If the limit is exceeded, the API call will be stream-limited, which may affect your business, please call reasonably.
        
        @param request: DeleteHostAccountRequest
        @return: DeleteHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_host_account_with_options(request, runtime)

    async def delete_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        """
        ## Usage notes
        This interface is used to delete individual host accounts. If a host account is no longer in use, you can invoke this interface to delete the host account for that host that has been configured on the bastion.
        >  After you remove the host account, you must enter the username and password of the host when you log on to the host in Bastionhost.
        ## QPS Limit
        The single-user QPS limit of this interface is 10 times/second. If the limit is exceeded, the API call will be stream-limited, which may affect your business, please call reasonably.
        
        @param request: DeleteHostAccountRequest
        @return: DeleteHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_account_with_options_async(request, runtime)

    def delete_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        """
        You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        """
        You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_group(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        """
        You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteHostGroupRequest
        @return: DeleteHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_host_group_with_options(request, runtime)

    async def delete_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        """
        You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteHostGroupRequest
        @return: DeleteHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_group_with_options_async(request, runtime)

    def delete_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_share_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_share_key(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_host_share_key_with_options(request, runtime)

    async def delete_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_share_key_with_options_async(request, runtime)

    def delete_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_domain_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_domain(
        self,
        request: yundun_bastionhost_20191209_models.DeleteNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_domain_with_options(request, runtime)

    async def delete_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_domain_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: yundun_bastionhost_20191209_models.DeletePolicyRequest,
    ) -> yundun_bastionhost_20191209_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.DeletePolicyRequest,
    ) -> yundun_bastionhost_20191209_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: yundun_bastionhost_20191209_models.DeleteRuleRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteRuleRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_user_public_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserPublicKeyResponse:
        """
        You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
        @param request: DeleteUserPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserPublicKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_public_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserPublicKeyResponse:
        """
        You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
        @param request: DeleteUserPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserPublicKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_public_key(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserPublicKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserPublicKeyResponse:
        """
        You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
        @param request: DeleteUserPublicKeyRequest
        @return: DeleteUserPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_public_key_with_options(request, runtime)

    async def delete_user_public_key_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserPublicKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserPublicKeyResponse:
        """
        You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
        @param request: DeleteUserPublicKeyRequest
        @return: DeleteUserPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_public_key_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAttribute',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAttribute',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def detach_database_accounts_from_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDatabaseAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_database_accounts_from_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDatabaseAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_database_accounts_from_user(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_database_accounts_from_user_with_options(request, runtime)

    async def detach_database_accounts_from_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_database_accounts_from_user_with_options_async(request, runtime)

    def detach_database_accounts_from_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDatabaseAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_database_accounts_from_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDatabaseAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_database_accounts_from_user_group(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_database_accounts_from_user_group_with_options(request, runtime)

    async def detach_database_accounts_from_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_database_accounts_from_user_group_with_options_async(request, runtime)

    def detach_host_accounts_from_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_accounts_from_host_share_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_host_accounts_from_host_share_key(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_host_share_key_with_options(request, runtime)

    async def detach_host_accounts_from_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_accounts_from_host_share_key_with_options_async(request, runtime)

    def detach_host_accounts_from_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_accounts_from_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_accounts_from_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostGroupAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_group_accounts_from_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostGroupAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        ***\
        
        @param request: DetachHostGroupAccountsFromUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostGroupAccountsFromUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostGroupAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_host_group_accounts_from_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        """
        ***\
        
        @param request: DetachHostGroupAccountsFromUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostGroupAccountsFromUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostGroupAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_host_group_accounts_from_user_group(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        """
        ***\
        
        @param request: DetachHostGroupAccountsFromUserGroupRequest
        @return: DetachHostGroupAccountsFromUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_host_group_accounts_from_user_group_with_options(request, runtime)

    async def detach_host_group_accounts_from_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        """
        ***\
        
        @param request: DetachHostGroupAccountsFromUserGroupRequest
        @return: DetachHostGroupAccountsFromUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_group_accounts_from_user_group_with_options_async(request, runtime)

    def disable_instance_public_access_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstancePublicAccess',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_instance_public_access_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstancePublicAccess',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse(),
            await self.call_api_async(params, req, runtime)
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

    def disable_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DisableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DisableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_rule_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DisableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_rule(
        self,
        request: yundun_bastionhost_20191209_models.DisableRuleRequest,
    ) -> yundun_bastionhost_20191209_models.DisableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_rule_with_options(request, runtime)

    async def disable_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableRuleRequest,
    ) -> yundun_bastionhost_20191209_models.DisableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_rule_with_options_async(request, runtime)

    def enable_instance_public_access_with_options(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstancePublicAccess',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_instance_public_access_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstancePublicAccess',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse(),
            await self.call_api_async(params, req, runtime)
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

    def enable_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.EnableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.EnableRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_rule_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.EnableRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_rule(
        self,
        request: yundun_bastionhost_20191209_models.EnableRuleRequest,
    ) -> yundun_bastionhost_20191209_models.EnableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_rule_with_options(request, runtime)

    async def enable_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableRuleRequest,
    ) -> yundun_bastionhost_20191209_models.EnableRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_rule_with_options_async(request, runtime)

    def generate_asset_operation_token_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GenerateAssetOperationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_account_id):
            query['AssetAccountId'] = request.asset_account_id
        if not UtilClient.is_unset(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not UtilClient.is_unset(request.asset_account_password):
            query['AssetAccountPassword'] = request.asset_account_password
        if not UtilClient.is_unset(request.asset_account_protocol_name):
            query['AssetAccountProtocolName'] = request.asset_account_protocol_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAssetOperationToken',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_asset_operation_token_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GenerateAssetOperationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_account_id):
            query['AssetAccountId'] = request.asset_account_id
        if not UtilClient.is_unset(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not UtilClient.is_unset(request.asset_account_password):
            query['AssetAccountPassword'] = request.asset_account_password
        if not UtilClient.is_unset(request.asset_account_protocol_name):
            query['AssetAccountProtocolName'] = request.asset_account_protocol_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.asset_type):
            query['AssetType'] = request.asset_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateAssetOperationToken',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_asset_operation_token(
        self,
        request: yundun_bastionhost_20191209_models.GenerateAssetOperationTokenRequest,
    ) -> yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_asset_operation_token_with_options(request, runtime)

    async def generate_asset_operation_token_async(
        self,
        request: yundun_bastionhost_20191209_models.GenerateAssetOperationTokenRequest,
    ) -> yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_asset_operation_token_with_options_async(request, runtime)

    def get_database_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_database_with_options(request, runtime)

    async def get_database_async(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_database_with_options_async(request, runtime)

    def get_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database_account(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_database_account_with_options(request, runtime)

    async def get_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_database_account_with_options_async(request, runtime)

    def get_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_host_share_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_host_share_key(
        self,
        request: yundun_bastionhost_20191209_models.GetHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_host_share_key_with_options(request, runtime)

    async def get_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_host_share_key_with_options_async(request, runtime)

    def get_instance_adauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse:
        """
        ###
        You can call this operation to query the settings of AD authentication on a bastion host. After you configure AD authentication on a bastion host, you can import AD-authenticated users into the bastion host. After the AD-authenticated users are imported into the bastion host, the AD-authenticated users can log on to the bastion host to perform O\\&M operations on servers.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceADAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceADAuthServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_adauth_server_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse:
        """
        ###
        You can call this operation to query the settings of AD authentication on a bastion host. After you configure AD authentication on a bastion host, you can import AD-authenticated users into the bastion host. After the AD-authenticated users are imported into the bastion host, the AD-authenticated users can log on to the bastion host to perform O\\&M operations on servers.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceADAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceADAuthServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_adauth_server(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse:
        """
        ###
        You can call this operation to query the settings of AD authentication on a bastion host. After you configure AD authentication on a bastion host, you can import AD-authenticated users into the bastion host. After the AD-authenticated users are imported into the bastion host, the AD-authenticated users can log on to the bastion host to perform O\\&M operations on servers.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceADAuthServerRequest
        @return: GetInstanceADAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_adauth_server_with_options(request, runtime)

    async def get_instance_adauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse:
        """
        ###
        You can call this operation to query the settings of AD authentication on a bastion host. After you configure AD authentication on a bastion host, you can import AD-authenticated users into the bastion host. After the AD-authenticated users are imported into the bastion host, the AD-authenticated users can log on to the bastion host to perform O\\&M operations on servers.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceADAuthServerRequest
        @return: GetInstanceADAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_adauth_server_with_options_async(request, runtime)

    def get_instance_ldapauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_ldapauth_server_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_ldapauth_server(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_ldapauth_server_with_options(request, runtime)

    async def get_instance_ldapauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_ldapauth_server_with_options_async(request, runtime)

    def get_instance_two_factor_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceTwoFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse:
        """
        You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceTwoFactorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceTwoFactorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceTwoFactor',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_two_factor_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceTwoFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse:
        """
        You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceTwoFactorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceTwoFactorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceTwoFactor',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_two_factor(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceTwoFactorRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse:
        """
        You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceTwoFactorRequest
        @return: GetInstanceTwoFactorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_two_factor_with_options(request, runtime)

    async def get_instance_two_factor_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceTwoFactorRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse:
        """
        You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
        ### Limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetInstanceTwoFactorRequest
        @return: GetInstanceTwoFactorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_two_factor_with_options_async(request, runtime)

    def get_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_domain_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_domain(
        self,
        request: yundun_bastionhost_20191209_models.GetNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.GetNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_network_domain_with_options(request, runtime)

    async def get_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.GetNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.GetNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_network_domain_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_asset_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyAssetScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyAssetScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_asset_scope_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyAssetScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyAssetScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_asset_scope(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyAssetScopeRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_asset_scope_with_options(request, runtime)

    async def get_policy_asset_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyAssetScopeRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_asset_scope_with_options_async(request, runtime)

    def get_policy_user_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyUserScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyUserScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_user_scope_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyUserScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyUserScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_user_scope(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyUserScopeRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_user_scope_with_options(request, runtime)

    async def get_policy_user_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyUserScopeRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_user_scope_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule(
        self,
        request: yundun_bastionhost_20191209_models.GetRuleRequest,
    ) -> yundun_bastionhost_20191209_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.GetRuleRequest,
    ) -> yundun_bastionhost_20191209_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_approve_commands_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListApproveCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListApproveCommandsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApproveCommands',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListApproveCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_approve_commands_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListApproveCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListApproveCommandsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApproveCommands',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListApproveCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_approve_commands(
        self,
        request: yundun_bastionhost_20191209_models.ListApproveCommandsRequest,
    ) -> yundun_bastionhost_20191209_models.ListApproveCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_approve_commands_with_options(request, runtime)

    async def list_approve_commands_async(
        self,
        request: yundun_bastionhost_20191209_models.ListApproveCommandsRequest,
    ) -> yundun_bastionhost_20191209_models.ListApproveCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_approve_commands_with_options_async(request, runtime)

    def list_database_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_accounts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_accounts(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_database_accounts_with_options(request, runtime)

    async def list_database_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_database_accounts_with_options_async(request, runtime)

    def list_database_accounts_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccountsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_accounts_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccountsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_accounts_for_user(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_database_accounts_for_user_with_options(request, runtime)

    async def list_database_accounts_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_database_accounts_for_user_with_options_async(request, runtime)

    def list_database_accounts_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccountsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_accounts_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseAccountsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_accounts_for_user_group(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_database_accounts_for_user_group_with_options(request, runtime)

    async def list_database_accounts_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_database_accounts_for_user_group_with_options_async(request, runtime)

    def list_databases_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_databases_with_options(request, runtime)

    async def list_databases_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_databases_with_options_async(request, runtime)

    def list_databases_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabasesForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabasesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabasesForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabasesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases_for_user(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_databases_for_user_with_options(request, runtime)

    async def list_databases_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_databases_for_user_with_options_async(request, runtime)

    def list_databases_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabasesForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabasesForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases_for_user_group(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_databases_for_user_group_with_options(request, runtime)

    async def list_databases_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_databases_for_user_group_with_options_async(request, runtime)

    def list_host_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_host_accounts_for_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_for_host_share_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_accounts_for_host_share_key(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_host_share_key_with_options(request, runtime)

    async def list_host_accounts_for_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_for_host_share_key_with_options_async(request, runtime)

    def list_host_accounts_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_accounts_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupAccountNamesForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_group_account_names_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupAccountNamesForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupAccountNamesForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_group_account_names_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupAccountNamesForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_groups_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_host_share_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostShareKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostShareKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostShareKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostShareKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_host_share_keys_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostShareKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostShareKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostShareKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostShareKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_host_share_keys(
        self,
        request: yundun_bastionhost_20191209_models.ListHostShareKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostShareKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_share_keys_with_options(request, runtime)

    async def list_host_share_keys_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostShareKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostShareKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_share_keys_with_options_async(request, runtime)

    def list_hosts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHosts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hosts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHosts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hosts_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsForUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hosts_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_network_domains_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListNetworkDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListNetworkDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not UtilClient.is_unset(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkDomains',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListNetworkDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_domains_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListNetworkDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListNetworkDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not UtilClient.is_unset(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkDomains',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListNetworkDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_domains(
        self,
        request: yundun_bastionhost_20191209_models.ListNetworkDomainsRequest,
    ) -> yundun_bastionhost_20191209_models.ListNetworkDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_network_domains_with_options(request, runtime)

    async def list_network_domains_async(
        self,
        request: yundun_bastionhost_20191209_models.ListNetworkDomainsRequest,
    ) -> yundun_bastionhost_20191209_models.ListNetworkDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_network_domains_with_options_async(request, runtime)

    def list_operation_database_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationDatabaseAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_database_accounts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationDatabaseAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_database_accounts(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_operation_database_accounts_with_options(request, runtime)

    async def list_operation_database_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_database_accounts_with_options_async(request, runtime)

    def list_operation_databases_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationDatabases',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_databases_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_address):
            query['DatabaseAddress'] = request.database_address
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationDatabases',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_databases(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabasesRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_operation_databases_with_options(request, runtime)

    async def list_operation_databases_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabasesRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_databases_with_options_async(request, runtime)

    def list_operation_host_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationHostAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_host_accounts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationHostAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_host_accounts(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_operation_host_accounts_with_options(request, runtime)

    async def list_operation_host_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_host_accounts_with_options_async(request, runtime)

    def list_operation_hosts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationHosts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_hosts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationHosts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_hosts(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_operation_hosts_with_options(request, runtime)

    async def list_operation_hosts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_hosts_with_options_async(request, runtime)

    def list_operation_tickets_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationTicketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_address):
            query['AssetAddress'] = request.asset_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationTickets',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_tickets_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationTicketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asset_address):
            query['AssetAddress'] = request.asset_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationTickets',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListOperationTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_tickets(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationTicketsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_operation_tickets_with_options(request, runtime)

    async def list_operation_tickets_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationTicketsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_tickets_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: yundun_bastionhost_20191209_models.ListPoliciesRequest,
    ) -> yundun_bastionhost_20191209_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: yundun_bastionhost_20191209_models.ListPoliciesRequest,
    ) -> yundun_bastionhost_20191209_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_state):
            query['RuleState'] = request.rule_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_state):
            query['RuleState'] = request.rule_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: yundun_bastionhost_20191209_models.ListRulesRequest,
    ) -> yundun_bastionhost_20191209_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: yundun_bastionhost_20191209_models.ListRulesRequest,
    ) -> yundun_bastionhost_20191209_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUserGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_user_public_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListUserPublicKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUserPublicKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPublicKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUserPublicKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_public_keys_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUserPublicKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUserPublicKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPublicKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUserPublicKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_public_keys(
        self,
        request: yundun_bastionhost_20191209_models.ListUserPublicKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListUserPublicKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_public_keys_with_options(request, runtime)

    async def list_user_public_keys_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUserPublicKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListUserPublicKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_public_keys_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_state):
            query['UserState'] = request.user_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_state):
            query['UserState'] = request.user_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](~~204590~~) operation.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.LockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_users_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        """
        # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](~~204590~~) operation.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.LockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_users(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        """
        # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](~~204590~~) operation.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockUsersRequest
        @return: LockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_users_with_options(request, runtime)

    async def lock_users_async(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        """
        # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](~~204590~~) operation.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: LockUsersRequest
        @return: LockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lock_users_with_options_async(request, runtime)

    def modify_database_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_port):
            query['DatabasePort'] = request.database_port
        if not UtilClient.is_unset(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not UtilClient.is_unset(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.database_port):
            query['DatabasePort'] = request.database_port
        if not UtilClient.is_unset(request.database_private_address):
            query['DatabasePrivateAddress'] = request.database_private_address
        if not UtilClient.is_unset(request.database_public_address):
            query['DatabasePublicAddress'] = request.database_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabase',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_with_options(request, runtime)

    async def modify_database_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_with_options_async(request, runtime)

    def modify_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_account_id):
            query['DatabaseAccountId'] = request.database_account_id
        if not UtilClient.is_unset(request.database_account_name):
            query['DatabaseAccountName'] = request.database_account_name
        if not UtilClient.is_unset(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDatabaseAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_account(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_account_with_options(request, runtime)

    async def modify_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_account_with_options_async(request, runtime)

    def modify_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        """
        You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
        > The basic information about ECS instances and hosts in ApsaraDB MyBase dedicated clusters within your Alibaba Cloud account is synchronized to Bastionhost on a regular basis. After you modify the basic information about an ECS instance or a host in an ApsaraDB MyBase dedicated cluster, the modification result may be overwritten by the synchronized information.
        
        @param request: ModifyHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not UtilClient.is_unset(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        """
        You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
        > The basic information about ECS instances and hosts in ApsaraDB MyBase dedicated clusters within your Alibaba Cloud account is synchronized to Bastionhost on a regular basis. After you modify the basic information about an ECS instance or a host in an ApsaraDB MyBase dedicated cluster, the modification result may be overwritten by the synchronized information.
        
        @param request: ModifyHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not UtilClient.is_unset(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        """
        You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
        > The basic information about ECS instances and hosts in ApsaraDB MyBase dedicated clusters within your Alibaba Cloud account is synchronized to Bastionhost on a regular basis. After you modify the basic information about an ECS instance or a host in an ApsaraDB MyBase dedicated cluster, the modification result may be overwritten by the synchronized information.
        
        @param request: ModifyHostRequest
        @return: ModifyHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_with_options(request, runtime)

    async def modify_host_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        """
        You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
        > The basic information about ECS instances and hosts in ApsaraDB MyBase dedicated clusters within your Alibaba Cloud account is synchronized to Bastionhost on a regular basis. After you modify the basic information about an ECS instance or a host in an ApsaraDB MyBase dedicated cluster, the modification result may be overwritten by the synchronized information.
        
        @param request: ModifyHostRequest
        @return: ModifyHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_with_options_async(request, runtime)

    def modify_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostAccountResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_share_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_share_key(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_host_share_key_with_options(request, runtime)

    async def modify_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_share_key_with_options_async(request, runtime)

    def modify_hosts_active_address_type_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostsActiveAddressType',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hosts_active_address_type_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostsActiveAddressType',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        ## Usage notes
        You can call this operation to change the port for the O&M protocol on one or more hosts. If the standard port for the O&M protocol on your host is vulnerable to attacks, you can call this operation to specify a custom port. For example, the standard port for SSH is port 22.
        >  Ports 0 to 1024 are reserved for Bastionhost. Do not change the port for the O&M protocol to a reserved port.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyHostsPortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostsPortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostsPort',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostsPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hosts_port_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        """
        ## Usage notes
        You can call this operation to change the port for the O&M protocol on one or more hosts. If the standard port for the O&M protocol on your host is vulnerable to attacks, you can call this operation to specify a custom port. For example, the standard port for SSH is port 22.
        >  Ports 0 to 1024 are reserved for Bastionhost. Do not change the port for the O&M protocol to a reserved port.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyHostsPortRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostsPortResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostsPort',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostsPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hosts_port(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        """
        ## Usage notes
        You can call this operation to change the port for the O&M protocol on one or more hosts. If the standard port for the O&M protocol on your host is vulnerable to attacks, you can call this operation to specify a custom port. For example, the standard port for SSH is port 22.
        >  Ports 0 to 1024 are reserved for Bastionhost. Do not change the port for the O&M protocol to a reserved port.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyHostsPortRequest
        @return: ModifyHostsPortResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hosts_port_with_options(request, runtime)

    async def modify_hosts_port_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        """
        ## Usage notes
        You can call this operation to change the port for the O&M protocol on one or more hosts. If the standard port for the O&M protocol on your host is vulnerable to attacks, you can call this operation to specify a custom port. For example, the standard port for SSH is port 22.
        >  Ports 0 to 1024 are reserved for Bastionhost. Do not change the port for the O&M protocol to a reserved port.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyHostsPortRequest
        @return: ModifyHostsPortResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hosts_port_with_options_async(request, runtime)

    def modify_instance_adauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not UtilClient.is_unset(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_adauth_server_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not UtilClient.is_unset(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_adauth_server(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_adauth_server_with_options(request, runtime)

    async def modify_instance_adauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_adauth_server_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_instance_ldapauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.login_name_mapping):
            query['LoginNameMapping'] = request.login_name_mapping
        if not UtilClient.is_unset(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not UtilClient.is_unset(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ldapauth_server_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.login_name_mapping):
            query['LoginNameMapping'] = request.login_name_mapping
        if not UtilClient.is_unset(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not UtilClient.is_unset(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ldapauth_server(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_ldapauth_server_with_options(request, runtime)

    async def modify_instance_ldapauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_ldapauth_server_with_options_async(request, runtime)

    def modify_instance_two_factor_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_two_factor):
            query['EnableTwoFactor'] = request.enable_two_factor
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_two_factor_time):
            query['SkipTwoFactorTime'] = request.skip_two_factor_time
        if not UtilClient.is_unset(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTwoFactor',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_two_factor_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_two_factor):
            query['EnableTwoFactor'] = request.enable_two_factor
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_two_factor_time):
            query['SkipTwoFactorTime'] = request.skip_two_factor_time
        if not UtilClient.is_unset(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTwoFactor',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_two_factor(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_two_factor_with_options(request, runtime)

    async def modify_instance_two_factor_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_two_factor_with_options_async(request, runtime)

    def modify_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not UtilClient.is_unset(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not UtilClient.is_unset(request.proxies):
            query['Proxies'] = request.proxies
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_network_domain_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.network_domain_name):
            query['NetworkDomainName'] = request.network_domain_name
        if not UtilClient.is_unset(request.network_domain_type):
            query['NetworkDomainType'] = request.network_domain_type
        if not UtilClient.is_unset(request.proxies):
            query['Proxies'] = request.proxies
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_network_domain(
        self,
        request: yundun_bastionhost_20191209_models.ModifyNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_domain_with_options(request, runtime)

    async def modify_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_domain_with_options_async(request, runtime)

    def modify_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicy',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy(
        self,
        request: yundun_bastionhost_20191209_models.ModifyPolicyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyPolicyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def modify_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rule(
        self,
        request: yundun_bastionhost_20191209_models.ModifyRuleRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_with_options(request, runtime)

    async def modify_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyRuleRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rule_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not UtilClient.is_unset(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not UtilClient.is_unset(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not UtilClient.is_unset(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.language_status):
            query['LanguageStatus'] = request.language_status
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not UtilClient.is_unset(request.need_reset_password):
            query['NeedResetPassword'] = request.need_reset_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        if not UtilClient.is_unset(request.two_factor_status):
            query['TwoFactorStatus'] = request.two_factor_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_user_public_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not UtilClient.is_unset(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPublicKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_public_key_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        if not UtilClient.is_unset(request.public_key_id):
            query['PublicKeyId'] = request.public_key_id
        if not UtilClient.is_unset(request.public_key_name):
            query['PublicKeyName'] = request.public_key_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPublicKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_public_key(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserPublicKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_public_key_with_options(request, runtime)

    async def modify_user_public_key_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserPublicKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_public_key_with_options_async(request, runtime)

    def move_databases_to_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveDatabasesToNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_databases_to_network_domain_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveDatabasesToNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_databases_to_network_domain(
        self,
        request: yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_databases_to_network_domain_with_options(request, runtime)

    async def move_databases_to_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_databases_to_network_domain_with_options_async(request, runtime)

    def move_hosts_to_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveHostsToNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_hosts_to_network_domain_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_domain_id):
            query['NetworkDomainId'] = request.network_domain_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveHostsToNetworkDomain',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_hosts_to_network_domain(
        self,
        request: yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_hosts_to_network_domain_with_options(request, runtime)

    async def move_hosts_to_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_hosts_to_network_domain_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def reject_approve_command_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RejectApproveCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RejectApproveCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectApproveCommand',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RejectApproveCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_approve_command_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RejectApproveCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RejectApproveCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_id):
            query['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectApproveCommand',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RejectApproveCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_approve_command(
        self,
        request: yundun_bastionhost_20191209_models.RejectApproveCommandRequest,
    ) -> yundun_bastionhost_20191209_models.RejectApproveCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.reject_approve_command_with_options(request, runtime)

    async def reject_approve_command_async(
        self,
        request: yundun_bastionhost_20191209_models.RejectApproveCommandRequest,
    ) -> yundun_bastionhost_20191209_models.RejectApproveCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reject_approve_command_with_options_async(request, runtime)

    def reject_operation_ticket_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RejectOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RejectOperationTicketResponse:
        """
        You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectOperationTicket',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RejectOperationTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_operation_ticket_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RejectOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RejectOperationTicketResponse:
        """
        You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.operation_ticket_id):
            query['OperationTicketId'] = request.operation_ticket_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectOperationTicket',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RejectOperationTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_operation_ticket(
        self,
        request: yundun_bastionhost_20191209_models.RejectOperationTicketRequest,
    ) -> yundun_bastionhost_20191209_models.RejectOperationTicketResponse:
        """
        You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectOperationTicketRequest
        @return: RejectOperationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reject_operation_ticket_with_options(request, runtime)

    async def reject_operation_ticket_async(
        self,
        request: yundun_bastionhost_20191209_models.RejectOperationTicketRequest,
    ) -> yundun_bastionhost_20191209_models.RejectOperationTicketResponse:
        """
        You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectOperationTicketRequest
        @return: RejectOperationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reject_operation_ticket_with_options_async(request, runtime)

    def remove_databases_from_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDatabasesFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_databases_from_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_ids):
            query['DatabaseIds'] = request.database_ids
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveDatabasesFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_databases_from_group(
        self,
        request: yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_databases_from_group_with_options(request, runtime)

    async def remove_databases_from_group_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_databases_from_group_with_options_async(request, runtime)

    def remove_hosts_from_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveHostsFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_hosts_from_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveHostsFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RemoveUsersFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_from_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        """
        You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RemoveUsersFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users_from_group(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        """
        You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RemoveUsersFromGroupRequest
        @return: RemoveUsersFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_group_with_options(request, runtime)

    async def remove_users_from_group_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        """
        You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
        ## QPS limit
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RemoveUsersFromGroupRequest
        @return: RemoveUsersFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_from_group_with_options_async(request, runtime)

    def renew_asset_operation_token_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RenewAssetOperationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RenewAssetOperationTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAssetOperationToken',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RenewAssetOperationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_asset_operation_token_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RenewAssetOperationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RenewAssetOperationTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.token_id):
            query['TokenId'] = request.token_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewAssetOperationToken',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RenewAssetOperationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_asset_operation_token(
        self,
        request: yundun_bastionhost_20191209_models.RenewAssetOperationTokenRequest,
    ) -> yundun_bastionhost_20191209_models.RenewAssetOperationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_asset_operation_token_with_options(request, runtime)

    async def renew_asset_operation_token_async(
        self,
        request: yundun_bastionhost_20191209_models.RenewAssetOperationTokenRequest,
    ) -> yundun_bastionhost_20191209_models.RenewAssetOperationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_asset_operation_token_with_options_async(request, runtime)

    def reset_host_account_credential_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetHostAccountCredential',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_host_account_credential_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetHostAccountCredential',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse(),
            await self.call_api_async(params, req, runtime)
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

    def set_policy_access_time_range_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.access_time_range_config):
            request.access_time_range_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.access_time_range_config, 'AccessTimeRangeConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_time_range_config_shrink):
            query['AccessTimeRangeConfig'] = request.access_time_range_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyAccessTimeRangeConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_access_time_range_config_with_options_async(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.access_time_range_config):
            request.access_time_range_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.access_time_range_config, 'AccessTimeRangeConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_time_range_config_shrink):
            query['AccessTimeRangeConfig'] = request.access_time_range_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyAccessTimeRangeConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_access_time_range_config(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_policy_access_time_range_config_with_options(request, runtime)

    async def set_policy_access_time_range_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_access_time_range_config_with_options_async(request, runtime)

    def set_policy_approval_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyApprovalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyApprovalConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approval_config):
            request.approval_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approval_config, 'ApprovalConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.approval_config_shrink):
            query['ApprovalConfig'] = request.approval_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyApprovalConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_approval_config_with_options_async(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyApprovalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyApprovalConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.approval_config):
            request.approval_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.approval_config, 'ApprovalConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.approval_config_shrink):
            query['ApprovalConfig'] = request.approval_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyApprovalConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_approval_config(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyApprovalConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_policy_approval_config_with_options(request, runtime)

    async def set_policy_approval_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyApprovalConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_approval_config_with_options_async(request, runtime)

    def set_policy_asset_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAssetScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyAssetScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_asset_scope_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAssetScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.databases):
            query['Databases'] = request.databases
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyAssetScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_asset_scope(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAssetScopeRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_policy_asset_scope_with_options(request, runtime)

    async def set_policy_asset_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAssetScopeRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_asset_scope_with_options_async(request, runtime)

    def set_policy_command_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyCommandConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyCommandConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.command_config):
            request.command_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.command_config, 'CommandConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_config_shrink):
            query['CommandConfig'] = request.command_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyCommandConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_command_config_with_options_async(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyCommandConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyCommandConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.command_config):
            request.command_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.command_config, 'CommandConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.command_config_shrink):
            query['CommandConfig'] = request.command_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyCommandConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_command_config(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyCommandConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_policy_command_config_with_options(request, runtime)

    async def set_policy_command_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyCommandConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_command_config_with_options_async(request, runtime)

    def set_policy_ipacl_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyIPAclConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyIPAclConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ipacl_config):
            request.ipacl_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ipacl_config, 'IPAclConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.ipacl_config_shrink):
            query['IPAclConfig'] = request.ipacl_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyIPAclConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_ipacl_config_with_options_async(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyIPAclConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyIPAclConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ipacl_config):
            request.ipacl_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ipacl_config, 'IPAclConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.ipacl_config_shrink):
            query['IPAclConfig'] = request.ipacl_config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyIPAclConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_ipacl_config(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyIPAclConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_policy_ipacl_config_with_options(request, runtime)

    async def set_policy_ipacl_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyIPAclConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_ipacl_config_with_options_async(request, runtime)

    def set_policy_protocol_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyProtocolConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyProtocolConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.protocol_config):
            request.protocol_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.protocol_config, 'ProtocolConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.protocol_config_shrink):
            query['ProtocolConfig'] = request.protocol_config_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyProtocolConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_protocol_config_with_options_async(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyProtocolConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = yundun_bastionhost_20191209_models.SetPolicyProtocolConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.protocol_config):
            request.protocol_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.protocol_config, 'ProtocolConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.protocol_config_shrink):
            query['ProtocolConfig'] = request.protocol_config_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyProtocolConfig',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_protocol_config(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyProtocolConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_policy_protocol_config_with_options(request, runtime)

    async def set_policy_protocol_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyProtocolConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_protocol_config_with_options_async(request, runtime)

    def set_policy_user_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyUserScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyUserScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_policy_user_scope_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyUserScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.user_group_ids):
            query['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPolicyUserScope',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_policy_user_scope(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyUserScopeRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_policy_user_scope_with_options(request, runtime)

    async def set_policy_user_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyUserScopeRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_user_scope_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        """
        After you call the [LockUsers](~~204591~~) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.UnlockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_users_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        """
        After you call the [LockUsers](~~204591~~) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.UnlockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_users(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        """
        After you call the [LockUsers](~~204591~~) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockUsersRequest
        @return: UnlockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_users_with_options(request, runtime)

    async def unlock_users_async(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        """
        After you call the [LockUsers](~~204591~~) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
        # Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UnlockUsersRequest
        @return: UnlockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_users_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def verify_instance_adauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_instance_adauth_server_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_instance_adauth_server(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_instance_adauth_server_with_options(request, runtime)

    async def verify_instance_adauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_instance_adauth_server_with_options_async(request, runtime)

    def verify_instance_ldapauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_instance_ldapauth_server_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_instance_ldapauth_server(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_instance_ldapauth_server_with_options(request, runtime)

    async def verify_instance_ldapauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_instance_ldapauth_server_with_options_async(request, runtime)
