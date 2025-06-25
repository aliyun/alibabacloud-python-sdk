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
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval field on the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to approve the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptApproveCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptApproveCommandResponse
        """
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
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval field on the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to approve the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptApproveCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptApproveCommandResponse
        """
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
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval field on the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to approve the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptApproveCommandRequest
        @return: AcceptApproveCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_approve_command_with_options(request, runtime)

    async def accept_approve_command_async(
        self,
        request: yundun_bastionhost_20191209_models.AcceptApproveCommandRequest,
    ) -> yundun_bastionhost_20191209_models.AcceptApproveCommandResponse:
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval field on the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to approve the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptApproveCommandRequest
        @return: AcceptApproveCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.accept_approve_command_with_options_async(request, runtime)

    def accept_operation_ticket_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AcceptOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AcceptOperationTicketResponse:
        """
        @summary Approves an O\\\\\\\\\\\\&M application.
        
        @description You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
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
        @summary Approves an O\\\\\\\\\\\\&M application.
        
        @description You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AcceptOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AcceptOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
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
        @summary Approves an O\\\\\\\\\\\\&M application.
        
        @description You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
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
        @summary Approves an O\\\\\\\\\\\\&M application.
        
        @description You can call this operation as a Bastionhost administrator to approve an O\\&M application of an O\\&M engineer.
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
        """
        @summary Adds multiple databases to a specified asset group.
        
        @param request: AddDatabasesToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatabasesToGroupResponse
        """
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
        """
        @summary Adds multiple databases to a specified asset group.
        
        @param request: AddDatabasesToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddDatabasesToGroupResponse
        """
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
        """
        @summary Adds multiple databases to a specified asset group.
        
        @param request: AddDatabasesToGroupRequest
        @return: AddDatabasesToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_databases_to_group_with_options(request, runtime)

    async def add_databases_to_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AddDatabasesToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddDatabasesToGroupResponse:
        """
        @summary Adds multiple databases to a specified asset group.
        
        @param request: AddDatabasesToGroupRequest
        @return: AddDatabasesToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_databases_to_group_with_options_async(request, runtime)

    def add_hosts_to_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        """
        @summary Adds one or more hosts to the specified host group.
        
        @description You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
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
        @summary Adds one or more hosts to the specified host group.
        
        @description You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
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
        @summary Adds one or more hosts to the specified host group.
        
        @description You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
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
        @summary Adds one or more hosts to the specified host group.
        
        @description You can call this operation to add one or more hosts to a host group. You can add multiple hosts to a host group to manage and grant permissions on the hosts in a centralized manner.
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
        @summary Add one or more users to a user group.
        
        @description #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](https://help.aliyun.com/document_detail/204596.html) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
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
        @summary Add one or more users to a user group.
        
        @description #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](https://help.aliyun.com/document_detail/204596.html) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
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
        @summary Add one or more users to a user group.
        
        @description #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](https://help.aliyun.com/document_detail/204596.html) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
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
        @summary Add one or more users to a user group.
        
        @description #
        You can call this operation to add one or more users to a user group. After you call the [CreateUserGroup](https://help.aliyun.com/document_detail/204596.html) operation to create a user group, you can call the AddUsersToGroup operation to add multiple users to the user group. Then, you can manage and grant permissions to the users at a time.
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
        """
        @summary Authorizes a user to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDatabaseAccountsToUserResponse
        """
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
        """
        @summary Authorizes a user to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDatabaseAccountsToUserResponse
        """
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
        """
        @summary Authorizes a user to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserRequest
        @return: AttachDatabaseAccountsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_database_accounts_to_user_with_options(request, runtime)

    async def attach_database_accounts_to_user_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserResponse:
        """
        @summary Authorizes a user to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserRequest
        @return: AttachDatabaseAccountsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_database_accounts_to_user_with_options_async(request, runtime)

    def attach_database_accounts_to_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse:
        """
        @summary Authorizes a user group to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDatabaseAccountsToUserGroupResponse
        """
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
        """
        @summary Authorizes a user group to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDatabaseAccountsToUserGroupResponse
        """
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
        """
        @summary Authorizes a user group to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserGroupRequest
        @return: AttachDatabaseAccountsToUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_database_accounts_to_user_group_with_options(request, runtime)

    async def attach_database_accounts_to_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachDatabaseAccountsToUserGroupResponse:
        """
        @summary Authorizes a user group to manage databases and database accounts.
        
        @param request: AttachDatabaseAccountsToUserGroupRequest
        @return: AttachDatabaseAccountsToUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_database_accounts_to_user_group_with_options_async(request, runtime)

    def attach_host_accounts_to_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse:
        """
        @summary Associates host accounts with a shared key.
        
        @param request: AttachHostAccountsToHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostAccountsToHostShareKeyResponse
        """
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
        """
        @summary Associates host accounts with a shared key.
        
        @param request: AttachHostAccountsToHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostAccountsToHostShareKeyResponse
        """
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
        """
        @summary Associates host accounts with a shared key.
        
        @param request: AttachHostAccountsToHostShareKeyRequest
        @return: AttachHostAccountsToHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_host_share_key_with_options(request, runtime)

    async def attach_host_accounts_to_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse:
        """
        @summary Associates host accounts with a shared key.
        
        @param request: AttachHostAccountsToHostShareKeyRequest
        @return: AttachHostAccountsToHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_accounts_to_host_share_key_with_options_async(request, runtime)

    def attach_host_accounts_to_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        """
        @summary Authorizes a user to manage the hosts and host accounts.
        
        @param request: AttachHostAccountsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostAccountsToUserResponse
        """
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
        """
        @summary Authorizes a user to manage the hosts and host accounts.
        
        @param request: AttachHostAccountsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostAccountsToUserResponse
        """
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
        """
        @summary Authorizes a user to manage the hosts and host accounts.
        
        @param request: AttachHostAccountsToUserRequest
        @return: AttachHostAccountsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_user_with_options(request, runtime)

    async def attach_host_accounts_to_user_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        """
        @summary Authorizes a user to manage the hosts and host accounts.
        
        @param request: AttachHostAccountsToUserRequest
        @return: AttachHostAccountsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_accounts_to_user_with_options_async(request, runtime)

    def attach_host_accounts_to_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        """
        @summary Authorizes a user group to manage one or more hosts and host accounts.
        
        @description After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
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
        @summary Authorizes a user group to manage one or more hosts and host accounts.
        
        @description After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
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
        @summary Authorizes a user group to manage one or more hosts and host accounts.
        
        @description After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
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
        @summary Authorizes a user group to manage one or more hosts and host accounts.
        
        @description After you authorize a user group to manage specific hosts and host accounts, all the users in the user group have access to the authorized hosts and host accounts.
        
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
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostGroupAccountsToUserResponse
        """
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
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostGroupAccountsToUserResponse
        """
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
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserRequest
        @return: AttachHostGroupAccountsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_host_group_accounts_to_user_with_options(request, runtime)

    async def attach_host_group_accounts_to_user_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse:
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserRequest
        @return: AttachHostGroupAccountsToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_group_accounts_to_user_with_options_async(request, runtime)

    def attach_host_group_accounts_to_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse:
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostGroupAccountsToUserGroupResponse
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
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachHostGroupAccountsToUserGroupResponse
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
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserGroupRequest
        @return: AttachHostGroupAccountsToUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_host_group_accounts_to_user_group_with_options(request, runtime)

    async def attach_host_group_accounts_to_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse:
        """
        @summary Authorizes a user to manage one or more host groups and host accounts.
        
        @param request: AttachHostGroupAccountsToUserGroupRequest
        @return: AttachHostGroupAccountsToUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_group_accounts_to_user_group_with_options_async(request, runtime)

    def config_instance_security_groups_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        """
        @summary Configures security groups for a bastion host.
        
        @param request: ConfigInstanceSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceSecurityGroupsResponse
        """
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
        """
        @summary Configures security groups for a bastion host.
        
        @param request: ConfigInstanceSecurityGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigInstanceSecurityGroupsResponse
        """
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
        """
        @summary Configures security groups for a bastion host.
        
        @param request: ConfigInstanceSecurityGroupsRequest
        @return: ConfigInstanceSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_instance_security_groups_with_options(request, runtime)

    async def config_instance_security_groups_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        """
        @summary Configures security groups for a bastion host.
        
        @param request: ConfigInstanceSecurityGroupsRequest
        @return: ConfigInstanceSecurityGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_security_groups_with_options_async(request, runtime)

    def config_instance_white_list_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        """
        @summary Configures a whitelist of public IP addresses for a bastion host.
        
        @description ## Usage notes
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
        if not UtilClient.is_unset(request.white_list_policies):
            query['WhiteListPolicies'] = request.white_list_policies
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
        @summary Configures a whitelist of public IP addresses for a bastion host.
        
        @description ## Usage notes
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
        if not UtilClient.is_unset(request.white_list_policies):
            query['WhiteListPolicies'] = request.white_list_policies
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
        @summary Configures a whitelist of public IP addresses for a bastion host.
        
        @description ## Usage notes
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
        @summary Configures a whitelist of public IP addresses for a bastion host.
        
        @description ## Usage notes
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
        """
        @summary Imports an ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQL Server instance, ApsaraDB RDS for PostgreSQL instance, PolarDB for MySQL cluster, PolarDB for PostgreSQL cluster, PolarDB for PostgreSQL (Compatible with Oracle) cluster, self-managed MySQL database, self-managed SQL Server database, self-managed PostgreSQL database, or self-managed Oracle database to a bastion host.
        
        @param request: CreateDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseResponse
        """
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
        """
        @summary Imports an ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQL Server instance, ApsaraDB RDS for PostgreSQL instance, PolarDB for MySQL cluster, PolarDB for PostgreSQL cluster, PolarDB for PostgreSQL (Compatible with Oracle) cluster, self-managed MySQL database, self-managed SQL Server database, self-managed PostgreSQL database, or self-managed Oracle database to a bastion host.
        
        @param request: CreateDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseResponse
        """
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
        """
        @summary Imports an ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQL Server instance, ApsaraDB RDS for PostgreSQL instance, PolarDB for MySQL cluster, PolarDB for PostgreSQL cluster, PolarDB for PostgreSQL (Compatible with Oracle) cluster, self-managed MySQL database, self-managed SQL Server database, self-managed PostgreSQL database, or self-managed Oracle database to a bastion host.
        
        @param request: CreateDatabaseRequest
        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseResponse:
        """
        @summary Imports an ApsaraDB RDS for MySQL instance, ApsaraDB RDS for SQL Server instance, ApsaraDB RDS for PostgreSQL instance, PolarDB for MySQL cluster, PolarDB for PostgreSQL cluster, PolarDB for PostgreSQL (Compatible with Oracle) cluster, self-managed MySQL database, self-managed SQL Server database, self-managed PostgreSQL database, or self-managed Oracle database to a bastion host.
        
        @param request: CreateDatabaseRequest
        @return: CreateDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse:
        """
        @summary After a database is created, you can create a database account for the database. After the account is created, O\\&M engineers can use the account to log on to and perform O\\&M operations on the database.
        
        @param request: CreateDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseAccountResponse
        """
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
        """
        @summary After a database is created, you can create a database account for the database. After the account is created, O\\&M engineers can use the account to log on to and perform O\\&M operations on the database.
        
        @param request: CreateDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatabaseAccountResponse
        """
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
        """
        @summary After a database is created, you can create a database account for the database. After the account is created, O\\&M engineers can use the account to log on to and perform O\\&M operations on the database.
        
        @param request: CreateDatabaseAccountRequest
        @return: CreateDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_database_account_with_options(request, runtime)

    async def create_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.CreateDatabaseAccountResponse:
        """
        @summary After a database is created, you can create a database account for the database. After the account is created, O\\&M engineers can use the account to log on to and perform O\\&M operations on the database.
        
        @param request: CreateDatabaseAccountRequest
        @return: CreateDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_database_account_with_options_async(request, runtime)

    def create_export_config_job_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateExportConfigJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateExportConfigJobResponse:
        """
        @param request: CreateExportConfigJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExportConfigJobResponse
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
            action='CreateExportConfigJob',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateExportConfigJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_export_config_job_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateExportConfigJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateExportConfigJobResponse:
        """
        @param request: CreateExportConfigJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExportConfigJobResponse
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
            action='CreateExportConfigJob',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateExportConfigJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_export_config_job(
        self,
        request: yundun_bastionhost_20191209_models.CreateExportConfigJobRequest,
    ) -> yundun_bastionhost_20191209_models.CreateExportConfigJobResponse:
        """
        @param request: CreateExportConfigJobRequest
        @return: CreateExportConfigJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_export_config_job_with_options(request, runtime)

    async def create_export_config_job_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateExportConfigJobRequest,
    ) -> yundun_bastionhost_20191209_models.CreateExportConfigJobResponse:
        """
        @param request: CreateExportConfigJobRequest
        @return: CreateExportConfigJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_export_config_job_with_options_async(request, runtime)

    def create_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        """
        @summary Bastionhost allows you to perform O\\&M operations on hosts from different sources, such as Alibaba Cloud Elastic Compute Service (ECS) instances, servers in on-premises data centers, and servers on other cloud platforms. Before you perform O\\&M operations on hosts by using a bastion host, you must import the hosts to the bastion host. You can call this operation to import a host to a bastion host.
        
        @param request: CreateHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostResponse
        """
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
        """
        @summary Bastionhost allows you to perform O\\&M operations on hosts from different sources, such as Alibaba Cloud Elastic Compute Service (ECS) instances, servers in on-premises data centers, and servers on other cloud platforms. Before you perform O\\&M operations on hosts by using a bastion host, you must import the hosts to the bastion host. You can call this operation to import a host to a bastion host.
        
        @param request: CreateHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostResponse
        """
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
        """
        @summary Bastionhost allows you to perform O\\&M operations on hosts from different sources, such as Alibaba Cloud Elastic Compute Service (ECS) instances, servers in on-premises data centers, and servers on other cloud platforms. Before you perform O\\&M operations on hosts by using a bastion host, you must import the hosts to the bastion host. You can call this operation to import a host to a bastion host.
        
        @param request: CreateHostRequest
        @return: CreateHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_host_with_options(request, runtime)

    async def create_host_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        """
        @summary Bastionhost allows you to perform O\\&M operations on hosts from different sources, such as Alibaba Cloud Elastic Compute Service (ECS) instances, servers in on-premises data centers, and servers on other cloud platforms. Before you perform O\\&M operations on hosts by using a bastion host, you must import the hosts to the bastion host. You can call this operation to import a host to a bastion host.
        
        @param request: CreateHostRequest
        @return: CreateHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_host_with_options_async(request, runtime)

    def create_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostAccountResponse:
        """
        @summary After you import a host to a bastion host, you must add an account of the host to the bastion host. This way, O\\&M engineers can use the account to log on to and perform O\\&M operations on the host by using the bastion host.
        
        @param request: CreateHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostAccountResponse
        """
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
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
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
        """
        @summary After you import a host to a bastion host, you must add an account of the host to the bastion host. This way, O\\&M engineers can use the account to log on to and perform O\\&M operations on the host by using the bastion host.
        
        @param request: CreateHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostAccountResponse
        """
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
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
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
        """
        @summary After you import a host to a bastion host, you must add an account of the host to the bastion host. This way, O\\&M engineers can use the account to log on to and perform O\\&M operations on the host by using the bastion host.
        
        @param request: CreateHostAccountRequest
        @return: CreateHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_host_account_with_options(request, runtime)

    async def create_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostAccountResponse:
        """
        @summary After you import a host to a bastion host, you must add an account of the host to the bastion host. This way, O\\&M engineers can use the account to log on to and perform O\\&M operations on the host by using the bastion host.
        
        @param request: CreateHostAccountRequest
        @return: CreateHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_host_account_with_options_async(request, runtime)

    def create_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostGroupResponse:
        """
        @summary You can create asset groups based on your business requirements and add assets of the same type to an asset group. This allows you to classify assets and manage multiple assets at a time.
        
        @param request: CreateHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostGroupResponse
        """
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
        """
        @summary You can create asset groups based on your business requirements and add assets of the same type to an asset group. This allows you to classify assets and manage multiple assets at a time.
        
        @param request: CreateHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostGroupResponse
        """
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
        """
        @summary You can create asset groups based on your business requirements and add assets of the same type to an asset group. This allows you to classify assets and manage multiple assets at a time.
        
        @param request: CreateHostGroupRequest
        @return: CreateHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_host_group_with_options(request, runtime)

    async def create_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostGroupResponse:
        """
        @summary You can create asset groups based on your business requirements and add assets of the same type to an asset group. This allows you to classify assets and manage multiple assets at a time.
        
        @param request: CreateHostGroupRequest
        @return: CreateHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_host_group_with_options_async(request, runtime)

    def create_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostShareKeyResponse:
        """
        @summary Bastionhost provides the shared key feature. This feature allows you to manage the private key that is used to log on to a host in a bastion host. This way, you can associate the private key with multiple accounts of the host to make host account management more efficient.
        
        @param request: CreateHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostShareKeyResponse
        """
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
        """
        @summary Bastionhost provides the shared key feature. This feature allows you to manage the private key that is used to log on to a host in a bastion host. This way, you can associate the private key with multiple accounts of the host to make host account management more efficient.
        
        @param request: CreateHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHostShareKeyResponse
        """
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
        """
        @summary Bastionhost provides the shared key feature. This feature allows you to manage the private key that is used to log on to a host in a bastion host. This way, you can associate the private key with multiple accounts of the host to make host account management more efficient.
        
        @param request: CreateHostShareKeyRequest
        @return: CreateHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_host_share_key_with_options(request, runtime)

    async def create_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostShareKeyResponse:
        """
        @summary Bastionhost provides the shared key feature. This feature allows you to manage the private key that is used to log on to a host in a bastion host. This way, you can associate the private key with multiple accounts of the host to make host account management more efficient.
        
        @param request: CreateHostShareKeyRequest
        @return: CreateHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_host_share_key_with_options_async(request, runtime)

    def create_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateNetworkDomainResponse:
        """
        @summary Creates a network domain.
        
        @param request: CreateNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkDomainResponse
        """
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
        """
        @summary Creates a network domain.
        
        @param request: CreateNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkDomainResponse
        """
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
        """
        @summary Creates a network domain.
        
        @param request: CreateNetworkDomainRequest
        @return: CreateNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_domain_with_options(request, runtime)

    async def create_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.CreateNetworkDomainResponse:
        """
        @summary Creates a network domain.
        
        @param request: CreateNetworkDomainRequest
        @return: CreateNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_domain_with_options_async(request, runtime)

    def create_operation_ticket_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateOperationTicketResponse:
        """
        @param request: CreateOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approve_comment):
            query['ApproveComment'] = request.approve_comment
        if not UtilClient.is_unset(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not UtilClient.is_unset(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_one_time_effect):
            query['IsOneTimeEffect'] = request.is_one_time_effect
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOperationTicket',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateOperationTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_operation_ticket_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateOperationTicketResponse:
        """
        @param request: CreateOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approve_comment):
            query['ApproveComment'] = request.approve_comment
        if not UtilClient.is_unset(request.asset_account_name):
            query['AssetAccountName'] = request.asset_account_name
        if not UtilClient.is_unset(request.asset_id):
            query['AssetId'] = request.asset_id
        if not UtilClient.is_unset(request.effect_end_time):
            query['EffectEndTime'] = request.effect_end_time
        if not UtilClient.is_unset(request.effect_start_time):
            query['EffectStartTime'] = request.effect_start_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_one_time_effect):
            query['IsOneTimeEffect'] = request.is_one_time_effect
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOperationTicket',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateOperationTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_operation_ticket(
        self,
        request: yundun_bastionhost_20191209_models.CreateOperationTicketRequest,
    ) -> yundun_bastionhost_20191209_models.CreateOperationTicketResponse:
        """
        @param request: CreateOperationTicketRequest
        @return: CreateOperationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_operation_ticket_with_options(request, runtime)

    async def create_operation_ticket_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateOperationTicketRequest,
    ) -> yundun_bastionhost_20191209_models.CreateOperationTicketResponse:
        """
        @param request: CreateOperationTicketRequest
        @return: CreateOperationTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_operation_ticket_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreatePolicyResponse:
        """
        @summary Configures a command control, command approval, protocol control, or access control policy to manage O\\&M operations. This effectively prevents users from performing high-risk operations or accidental operations to ensure O\\&M security.
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
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
        """
        @summary Configures a command control, command approval, protocol control, or access control policy to manage O\\&M operations. This effectively prevents users from performing high-risk operations or accidental operations to ensure O\\&M security.
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
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
        """
        @summary Configures a command control, command approval, protocol control, or access control policy to manage O\\&M operations. This effectively prevents users from performing high-risk operations or accidental operations to ensure O\\&M security.
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.CreatePolicyRequest,
    ) -> yundun_bastionhost_20191209_models.CreatePolicyResponse:
        """
        @summary Configures a command control, command approval, protocol control, or access control policy to manage O\\&M operations. This effectively prevents users from performing high-risk operations or accidental operations to ensure O\\&M security.
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateRuleResponse:
        """
        @summary You can create authorization rules to authorize multiple users to manage assets. You can also specify a validity period for an authorization rule. This way, you can manage users and assets in a more efficient manner and limit the time periods during which users can access assets.
        
        @param request: CreateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
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
        """
        @summary You can create authorization rules to authorize multiple users to manage assets. You can also specify a validity period for an authorization rule. This way, you can manage users and assets in a more efficient manner and limit the time periods during which users can access assets.
        
        @param request: CreateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRuleResponse
        """
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
        """
        @summary You can create authorization rules to authorize multiple users to manage assets. You can also specify a validity period for an authorization rule. This way, you can manage users and assets in a more efficient manner and limit the time periods during which users can access assets.
        
        @param request: CreateRuleRequest
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateRuleRequest,
    ) -> yundun_bastionhost_20191209_models.CreateRuleResponse:
        """
        @summary You can create authorization rules to authorize multiple users to manage assets. You can also specify a validity period for an authorization rule. This way, you can manage users and assets in a more efficient manner and limit the time periods during which users can access assets.
        
        @param request: CreateRuleRequest
        @return: CreateRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        """
        @summary Adds a user to a bastion host.
        
        @description You can call the CreateUser operation to add local users, Resource Access Management (RAM) users, Active Directory (AD)-authenticated users, or Lightweight Directory Access Protocol (LDAP)-authenticated users to a bastion host. After a Bastionhost administrator adds a user to a bastion host, O\\&M engineers can log on to the bastion host as the user to perform O\\&M operations on the hosts that the user is authorized to manage.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
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
        @summary Adds a user to a bastion host.
        
        @description You can call the CreateUser operation to add local users, Resource Access Management (RAM) users, Active Directory (AD)-authenticated users, or Lightweight Directory Access Protocol (LDAP)-authenticated users to a bastion host. After a Bastionhost administrator adds a user to a bastion host, O\\&M engineers can log on to the bastion host as the user to perform O\\&M operations on the hosts that the user is authorized to manage.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
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
        @summary Adds a user to a bastion host.
        
        @description You can call the CreateUser operation to add local users, Resource Access Management (RAM) users, Active Directory (AD)-authenticated users, or Lightweight Directory Access Protocol (LDAP)-authenticated users to a bastion host. After a Bastionhost administrator adds a user to a bastion host, O\\&M engineers can log on to the bastion host as the user to perform O\\&M operations on the hosts that the user is authorized to manage.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
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
        @summary Adds a user to a bastion host.
        
        @description You can call the CreateUser operation to add local users, Resource Access Management (RAM) users, Active Directory (AD)-authenticated users, or Lightweight Directory Access Protocol (LDAP)-authenticated users to a bastion host. After a Bastionhost administrator adds a user to a bastion host, O\\&M engineers can log on to the bastion host as the user to perform O\\&M operations on the hosts that the user is authorized to manage.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
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
        @summary Creates a user group for the specified bastion host.
        
        @description You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](https://help.aliyun.com/document_detail/204600.html) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
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
        @summary Creates a user group for the specified bastion host.
        
        @description You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](https://help.aliyun.com/document_detail/204600.html) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
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
        @summary Creates a user group for the specified bastion host.
        
        @description You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](https://help.aliyun.com/document_detail/204600.html) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
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
        @summary Creates a user group for the specified bastion host.
        
        @description You can call this operation to create a user group for a bastion host as an administrator. Then, you can call the [AddUsersToGroup](https://help.aliyun.com/document_detail/204600.html) operation to add users to the user group at a time. After you add the users to the user group, you can authorize and manage the users in a centralized manner.
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
        @summary Creates a public key for a bastion host user and hosts the public key in the bastion host. This way, O\\&M engineers can use the private key that corresponds to the public key to log on to the bastion host from an O\\&M client.
        
        @description You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
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
        @summary Creates a public key for a bastion host user and hosts the public key in the bastion host. This way, O\\&M engineers can use the private key that corresponds to the public key to log on to the bastion host from an O\\&M client.
        
        @description You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
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
        @summary Creates a public key for a bastion host user and hosts the public key in the bastion host. This way, O\\&M engineers can use the private key that corresponds to the public key to log on to the bastion host from an O\\&M client.
        
        @description You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
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
        @summary Creates a public key for a bastion host user and hosts the public key in the bastion host. This way, O\\&M engineers can use the private key that corresponds to the public key to log on to the bastion host from an O\\&M client.
        
        @description You can call the CreateUserPublicKey operation to create a public key for the specified user of a bastion host.
        
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
        """
        @summary Deletes a database.
        
        @param request: DeleteDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseResponse
        """
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
        """
        @summary Deletes a database.
        
        @param request: DeleteDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseResponse
        """
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
        """
        @summary Deletes a database.
        
        @param request: DeleteDatabaseRequest
        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseResponse:
        """
        @summary Deletes a database.
        
        @param request: DeleteDatabaseRequest
        @return: DeleteDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse:
        """
        @summary Deletes a database account.
        
        @param request: DeleteDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseAccountResponse
        """
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
        """
        @summary Deletes a database account.
        
        @param request: DeleteDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatabaseAccountResponse
        """
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
        """
        @summary Deletes a database account.
        
        @param request: DeleteDatabaseAccountRequest
        @return: DeleteDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_database_account_with_options(request, runtime)

    async def delete_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteDatabaseAccountResponse:
        """
        @summary Deletes a database account.
        
        @param request: DeleteDatabaseAccountRequest
        @return: DeleteDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_account_with_options_async(request, runtime)

    def delete_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        """
        @summary Deletes the specified host.
        
        @param request: DeleteHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostResponse
        """
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
        """
        @summary Deletes the specified host.
        
        @param request: DeleteHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostResponse
        """
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
        """
        @summary Deletes the specified host.
        
        @param request: DeleteHostRequest
        @return: DeleteHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_host_with_options(request, runtime)

    async def delete_host_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        """
        @summary Deletes the specified host.
        
        @param request: DeleteHostRequest
        @return: DeleteHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_with_options_async(request, runtime)

    def delete_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        """
        @summary Removes a host account.
        
        @description ## Usage notes
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
        @summary Removes a host account.
        
        @description ## Usage notes
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
        @summary Removes a host account.
        
        @description ## Usage notes
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
        @summary Removes a host account.
        
        @description ## Usage notes
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
        @summary Deletes a host group.
        
        @description You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
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
        @summary Deletes a host group.
        
        @description You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
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
        @summary Deletes a host group.
        
        @description You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
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
        @summary Deletes a host group.
        
        @description You can call this operation to delete a single host group. If you no longer need to perform O\\&M operations on all hosts in a host group, you can call this operation to delete the host group.
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
        """
        @summary Deletes a shared key.
        
        @param request: DeleteHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostShareKeyResponse
        """
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
        """
        @summary Deletes a shared key.
        
        @param request: DeleteHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHostShareKeyResponse
        """
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
        """
        @summary Deletes a shared key.
        
        @param request: DeleteHostShareKeyRequest
        @return: DeleteHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_host_share_key_with_options(request, runtime)

    async def delete_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse:
        """
        @summary Deletes a shared key.
        
        @param request: DeleteHostShareKeyRequest
        @return: DeleteHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_share_key_with_options_async(request, runtime)

    def delete_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse:
        """
        @summary Deletes a network domain.
        
        @param request: DeleteNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkDomainResponse
        """
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
        """
        @summary Deletes a network domain.
        
        @param request: DeleteNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkDomainResponse
        """
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
        """
        @summary Deletes a network domain.
        
        @param request: DeleteNetworkDomainRequest
        @return: DeleteNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_domain_with_options(request, runtime)

    async def delete_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteNetworkDomainResponse:
        """
        @summary Deletes a network domain.
        
        @param request: DeleteNetworkDomainRequest
        @return: DeleteNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_domain_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeletePolicyResponse:
        """
        @summary Deletes a control policy.
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
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
        """
        @summary Deletes a control policy.
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
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
        """
        @summary Deletes a control policy.
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.DeletePolicyRequest,
    ) -> yundun_bastionhost_20191209_models.DeletePolicyResponse:
        """
        @summary Deletes a control policy.
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteRuleResponse:
        """
        @summary Deletes an authorization rule.
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        """
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
        """
        @summary Deletes an authorization rule.
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        """
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
        """
        @summary Deletes an authorization rule.
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteRuleRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteRuleResponse:
        """
        @summary Deletes an authorization rule.
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        """
        @summary Deletes a bastion host user.
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
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
        """
        @summary Deletes a bastion host user.
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
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
        """
        @summary Deletes a bastion host user.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        """
        @summary Deletes a bastion host user.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserGroupResponse:
        """
        @summary Deletes a specified user group from a specified bastion host.
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
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
        """
        @summary Deletes a specified user group from a specified bastion host.
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
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
        """
        @summary Deletes a specified user group from a specified bastion host.
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserGroupResponse:
        """
        @summary Deletes a specified user group from a specified bastion host.
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def delete_user_public_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserPublicKeyResponse:
        """
        @summary Deletes a public key from the specified user.
        
        @description You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
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
        @summary Deletes a public key from the specified user.
        
        @description You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
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
        @summary Deletes a public key from the specified user.
        
        @description You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
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
        @summary Deletes a public key from the specified user.
        
        @description You can call the DeleteUserPublicKey operation to delete a public key from the specified user of a bastion host.
        
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
        """
        @summary Queries the attribute information about the specified bastion host. The information includes the ID and remarks of the bastion host.
        
        @description ***\
        
        @param request: DescribeInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAttributeResponse
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
        """
        @summary Queries the attribute information about the specified bastion host. The information includes the ID and remarks of the bastion host.
        
        @description ***\
        
        @param request: DescribeInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAttributeResponse
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
        """
        @summary Queries the attribute information about the specified bastion host. The information includes the ID and remarks of the bastion host.
        
        @description ***\
        
        @param request: DescribeInstanceAttributeRequest
        @return: DescribeInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        """
        @summary Queries the attribute information about the specified bastion host. The information includes the ID and remarks of the bastion host.
        
        @description ***\
        
        @param request: DescribeInstanceAttributeRequest
        @return: DescribeInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        """
        @summary 堡垒机实例列表
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
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
        """
        @summary 堡垒机实例列表
        
        @param request: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
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
        """
        @summary 堡垒机实例列表
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        """
        @summary 堡垒机实例列表
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        """
        @summary Queries available regions where you can create bastion hosts.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        """
        @summary Queries available regions where you can create bastion hosts.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
        """
        @summary Queries available regions where you can create bastion hosts.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        """
        @summary Queries available regions where you can create bastion hosts.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detach_database_accounts_from_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse:
        """
        @summary Revokes permissions on databases and database accounts from a user.
        
        @param request: DetachDatabaseAccountsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachDatabaseAccountsFromUserResponse
        """
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
        """
        @summary Revokes permissions on databases and database accounts from a user.
        
        @param request: DetachDatabaseAccountsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachDatabaseAccountsFromUserResponse
        """
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
        """
        @summary Revokes permissions on databases and database accounts from a user.
        
        @param request: DetachDatabaseAccountsFromUserRequest
        @return: DetachDatabaseAccountsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_database_accounts_from_user_with_options(request, runtime)

    async def detach_database_accounts_from_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserResponse:
        """
        @summary Revokes permissions on databases and database accounts from a user.
        
        @param request: DetachDatabaseAccountsFromUserRequest
        @return: DetachDatabaseAccountsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_database_accounts_from_user_with_options_async(request, runtime)

    def detach_database_accounts_from_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse:
        """
        @summary Revokes permissions on databases and database accounts from a user group.
        
        @param request: DetachDatabaseAccountsFromUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachDatabaseAccountsFromUserGroupResponse
        """
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
        """
        @summary Revokes permissions on databases and database accounts from a user group.
        
        @param request: DetachDatabaseAccountsFromUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachDatabaseAccountsFromUserGroupResponse
        """
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
        """
        @summary Revokes permissions on databases and database accounts from a user group.
        
        @param request: DetachDatabaseAccountsFromUserGroupRequest
        @return: DetachDatabaseAccountsFromUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_database_accounts_from_user_group_with_options(request, runtime)

    async def detach_database_accounts_from_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachDatabaseAccountsFromUserGroupResponse:
        """
        @summary Revokes permissions on databases and database accounts from a user group.
        
        @param request: DetachDatabaseAccountsFromUserGroupRequest
        @return: DetachDatabaseAccountsFromUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_database_accounts_from_user_group_with_options_async(request, runtime)

    def detach_host_accounts_from_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse:
        """
        @summary Disassociate host accounts from a shared key.
        
        @param request: DetachHostAccountsFromHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostAccountsFromHostShareKeyResponse
        """
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
        """
        @summary Disassociate host accounts from a shared key.
        
        @param request: DetachHostAccountsFromHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostAccountsFromHostShareKeyResponse
        """
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
        """
        @summary Disassociate host accounts from a shared key.
        
        @param request: DetachHostAccountsFromHostShareKeyRequest
        @return: DetachHostAccountsFromHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_host_share_key_with_options(request, runtime)

    async def detach_host_accounts_from_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse:
        """
        @summary Disassociate host accounts from a shared key.
        
        @param request: DetachHostAccountsFromHostShareKeyRequest
        @return: DetachHostAccountsFromHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_accounts_from_host_share_key_with_options_async(request, runtime)

    def detach_host_accounts_from_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        """
        @summary Revokes permissions on hosts and host accounts from a user.
        
        @param request: DetachHostAccountsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostAccountsFromUserResponse
        """
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
        """
        @summary Revokes permissions on hosts and host accounts from a user.
        
        @param request: DetachHostAccountsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostAccountsFromUserResponse
        """
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
        """
        @summary Revokes permissions on hosts and host accounts from a user.
        
        @param request: DetachHostAccountsFromUserRequest
        @return: DetachHostAccountsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_user_with_options(request, runtime)

    async def detach_host_accounts_from_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        """
        @summary Revokes permissions on hosts and host accounts from a user.
        
        @param request: DetachHostAccountsFromUserRequest
        @return: DetachHostAccountsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_accounts_from_user_with_options_async(request, runtime)

    def detach_host_accounts_from_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse:
        """
        @summary Revokes the permissions on one or more hosts and host accounts from a user group.
        
        @param request: DetachHostAccountsFromUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostAccountsFromUserGroupResponse
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
        """
        @summary Revokes the permissions on one or more hosts and host accounts from a user group.
        
        @param request: DetachHostAccountsFromUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostAccountsFromUserGroupResponse
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
        """
        @summary Revokes the permissions on one or more hosts and host accounts from a user group.
        
        @param request: DetachHostAccountsFromUserGroupRequest
        @return: DetachHostAccountsFromUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_user_group_with_options(request, runtime)

    async def detach_host_accounts_from_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse:
        """
        @summary Revokes the permissions on one or more hosts and host accounts from a user group.
        
        @param request: DetachHostAccountsFromUserGroupRequest
        @return: DetachHostAccountsFromUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_accounts_from_user_group_with_options_async(request, runtime)

    def detach_host_group_accounts_from_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse:
        """
        @summary Removes host groups and host accounts from the list of host groups and host accounts that a user is authorized to manage.
        
        @param request: DetachHostGroupAccountsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostGroupAccountsFromUserResponse
        """
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
        """
        @summary Removes host groups and host accounts from the list of host groups and host accounts that a user is authorized to manage.
        
        @param request: DetachHostGroupAccountsFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachHostGroupAccountsFromUserResponse
        """
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
        """
        @summary Removes host groups and host accounts from the list of host groups and host accounts that a user is authorized to manage.
        
        @param request: DetachHostGroupAccountsFromUserRequest
        @return: DetachHostGroupAccountsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_host_group_accounts_from_user_with_options(request, runtime)

    async def detach_host_group_accounts_from_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse:
        """
        @summary Removes host groups and host accounts from the list of host groups and host accounts that a user is authorized to manage.
        
        @param request: DetachHostGroupAccountsFromUserRequest
        @return: DetachHostGroupAccountsFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_group_accounts_from_user_with_options_async(request, runtime)

    def detach_host_group_accounts_from_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        """
        @summary Revokes permissions on one or more host groups and host accounts from a user group.
        
        @description ***\
        
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
        @summary Revokes permissions on one or more host groups and host accounts from a user group.
        
        @description ***\
        
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
        @summary Revokes permissions on one or more host groups and host accounts from a user group.
        
        @description ***\
        
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
        @summary Revokes permissions on one or more host groups and host accounts from a user group.
        
        @description ***\
        
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
        """
        @summary Disables Internet access for a bastion host.
        
        @param request: DisableInstancePublicAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInstancePublicAccessResponse
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
        """
        @summary Disables Internet access for a bastion host.
        
        @param request: DisableInstancePublicAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInstancePublicAccessResponse
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
        """
        @summary Disables Internet access for a bastion host.
        
        @param request: DisableInstancePublicAccessRequest
        @return: DisableInstancePublicAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_public_access_with_options(request, runtime)

    async def disable_instance_public_access_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        """
        @summary Disables Internet access for a bastion host.
        
        @param request: DisableInstancePublicAccessRequest
        @return: DisableInstancePublicAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_public_access_with_options_async(request, runtime)

    def disable_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DisableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableRuleResponse:
        """
        @summary Disables an authorization rule.
        
        @param request: DisableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRuleResponse
        """
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
        """
        @summary Disables an authorization rule.
        
        @param request: DisableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableRuleResponse
        """
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
        """
        @summary Disables an authorization rule.
        
        @param request: DisableRuleRequest
        @return: DisableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_rule_with_options(request, runtime)

    async def disable_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableRuleRequest,
    ) -> yundun_bastionhost_20191209_models.DisableRuleResponse:
        """
        @summary Disables an authorization rule.
        
        @param request: DisableRuleRequest
        @return: DisableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_rule_with_options_async(request, runtime)

    def enable_instance_public_access_with_options(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        """
        @summary Enables Internet access for a bastion host.
        
        @param request: EnableInstancePublicAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInstancePublicAccessResponse
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
        """
        @summary Enables Internet access for a bastion host.
        
        @param request: EnableInstancePublicAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInstancePublicAccessResponse
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
        """
        @summary Enables Internet access for a bastion host.
        
        @param request: EnableInstancePublicAccessRequest
        @return: EnableInstancePublicAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_public_access_with_options(request, runtime)

    async def enable_instance_public_access_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        """
        @summary Enables Internet access for a bastion host.
        
        @param request: EnableInstancePublicAccessRequest
        @return: EnableInstancePublicAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_public_access_with_options_async(request, runtime)

    def enable_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.EnableRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableRuleResponse:
        """
        @summary Enables an authorization rule.
        
        @param request: EnableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRuleResponse
        """
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
        """
        @summary Enables an authorization rule.
        
        @param request: EnableRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRuleResponse
        """
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
        """
        @summary Enables an authorization rule.
        
        @param request: EnableRuleRequest
        @return: EnableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_rule_with_options(request, runtime)

    async def enable_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableRuleRequest,
    ) -> yundun_bastionhost_20191209_models.EnableRuleResponse:
        """
        @summary Enables an authorization rule.
        
        @param request: EnableRuleRequest
        @return: EnableRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_rule_with_options_async(request, runtime)

    def generate_asset_operation_token_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GenerateAssetOperationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse:
        """
        @summary Applies for an O\\&M token.
        
        @param request: GenerateAssetOperationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAssetOperationTokenResponse
        """
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
        if not UtilClient.is_unset(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not UtilClient.is_unset(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not UtilClient.is_unset(request.operation_note):
            query['OperationNote'] = request.operation_note
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sso_client):
            query['SsoClient'] = request.sso_client
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
        """
        @summary Applies for an O\\&M token.
        
        @param request: GenerateAssetOperationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateAssetOperationTokenResponse
        """
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
        if not UtilClient.is_unset(request.database_schema):
            query['DatabaseSchema'] = request.database_schema
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.login_attribute):
            query['LoginAttribute'] = request.login_attribute
        if not UtilClient.is_unset(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not UtilClient.is_unset(request.operation_note):
            query['OperationNote'] = request.operation_note
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sso_client):
            query['SsoClient'] = request.sso_client
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
        """
        @summary Applies for an O\\&M token.
        
        @param request: GenerateAssetOperationTokenRequest
        @return: GenerateAssetOperationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_asset_operation_token_with_options(request, runtime)

    async def generate_asset_operation_token_async(
        self,
        request: yundun_bastionhost_20191209_models.GenerateAssetOperationTokenRequest,
    ) -> yundun_bastionhost_20191209_models.GenerateAssetOperationTokenResponse:
        """
        @summary Applies for an O\\&M token.
        
        @param request: GenerateAssetOperationTokenRequest
        @return: GenerateAssetOperationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_asset_operation_token_with_options_async(request, runtime)

    def get_database_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseResponse:
        """
        @summary Queries the detailed information about a database.
        
        @param request: GetDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseResponse
        """
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
        """
        @summary Queries the detailed information about a database.
        
        @param request: GetDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseResponse
        """
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
        """
        @summary Queries the detailed information about a database.
        
        @param request: GetDatabaseRequest
        @return: GetDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_database_with_options(request, runtime)

    async def get_database_async(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseResponse:
        """
        @summary Queries the detailed information about a database.
        
        @param request: GetDatabaseRequest
        @return: GetDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_database_with_options_async(request, runtime)

    def get_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseAccountResponse:
        """
        @summary Queries the detailed information about a database account.
        
        @param request: GetDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseAccountResponse
        """
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
        """
        @summary Queries the detailed information about a database account.
        
        @param request: GetDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseAccountResponse
        """
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
        """
        @summary Queries the detailed information about a database account.
        
        @param request: GetDatabaseAccountRequest
        @return: GetDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_database_account_with_options(request, runtime)

    async def get_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.GetDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.GetDatabaseAccountResponse:
        """
        @summary Queries the detailed information about a database account.
        
        @param request: GetDatabaseAccountRequest
        @return: GetDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_database_account_with_options_async(request, runtime)

    def get_export_config_job_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetExportConfigJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetExportConfigJobResponse:
        """
        @param request: GetExportConfigJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExportConfigJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExportConfigJob',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetExportConfigJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_export_config_job_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetExportConfigJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetExportConfigJobResponse:
        """
        @param request: GetExportConfigJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExportConfigJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExportConfigJob',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetExportConfigJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_export_config_job(
        self,
        request: yundun_bastionhost_20191209_models.GetExportConfigJobRequest,
    ) -> yundun_bastionhost_20191209_models.GetExportConfigJobResponse:
        """
        @param request: GetExportConfigJobRequest
        @return: GetExportConfigJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_export_config_job_with_options(request, runtime)

    async def get_export_config_job_async(
        self,
        request: yundun_bastionhost_20191209_models.GetExportConfigJobRequest,
    ) -> yundun_bastionhost_20191209_models.GetExportConfigJobResponse:
        """
        @param request: GetExportConfigJobRequest
        @return: GetExportConfigJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_export_config_job_with_options_async(request, runtime)

    def get_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        """
        @summary Queries the details of a host, such as the name, source, address, protocol, and service port of the host.
        
        @param request: GetHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostResponse
        """
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
        """
        @summary Queries the details of a host, such as the name, source, address, protocol, and service port of the host.
        
        @param request: GetHostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostResponse
        """
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
        """
        @summary Queries the details of a host, such as the name, source, address, protocol, and service port of the host.
        
        @param request: GetHostRequest
        @return: GetHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_host_with_options(request, runtime)

    async def get_host_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        """
        @summary Queries the details of a host, such as the name, source, address, protocol, and service port of the host.
        
        @param request: GetHostRequest
        @return: GetHostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_host_with_options_async(request, runtime)

    def get_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostAccountResponse:
        """
        @summary Queries the details of a specified host account.
        
        @param request: GetHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostAccountResponse
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
        """
        @summary Queries the details of a specified host account.
        
        @param request: GetHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostAccountResponse
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
        """
        @summary Queries the details of a specified host account.
        
        @param request: GetHostAccountRequest
        @return: GetHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_host_account_with_options(request, runtime)

    async def get_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostAccountResponse:
        """
        @summary Queries the details of a specified host account.
        
        @param request: GetHostAccountRequest
        @return: GetHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_host_account_with_options_async(request, runtime)

    def get_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostGroupResponse:
        """
        @summary Queries the details of a specified host group.
        
        @param request: GetHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostGroupResponse
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
        """
        @summary Queries the details of a specified host group.
        
        @param request: GetHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostGroupResponse
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
        """
        @summary Queries the details of a specified host group.
        
        @param request: GetHostGroupRequest
        @return: GetHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_host_group_with_options(request, runtime)

    async def get_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostGroupResponse:
        """
        @summary Queries the details of a specified host group.
        
        @param request: GetHostGroupRequest
        @return: GetHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_host_group_with_options_async(request, runtime)

    def get_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostShareKeyResponse:
        """
        @summary Queries the information about a shared key.
        
        @param request: GetHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostShareKeyResponse
        """
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
        """
        @summary Queries the information about a shared key.
        
        @param request: GetHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHostShareKeyResponse
        """
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
        """
        @summary Queries the information about a shared key.
        
        @param request: GetHostShareKeyRequest
        @return: GetHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_host_share_key_with_options(request, runtime)

    async def get_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostShareKeyResponse:
        """
        @summary Queries the information about a shared key.
        
        @param request: GetHostShareKeyRequest
        @return: GetHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_host_share_key_with_options_async(request, runtime)

    def get_instance_adauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse:
        """
        @summary Queries the settings of Active Directory (AD) authentication on a bastion host.
        
        @description ###
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
        @summary Queries the settings of Active Directory (AD) authentication on a bastion host.
        
        @description ###
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
        @summary Queries the settings of Active Directory (AD) authentication on a bastion host.
        
        @description ###
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
        @summary Queries the settings of Active Directory (AD) authentication on a bastion host.
        
        @description ###
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
        """
        @summary Queries the settings of Lightweight Directory Access Protocol (LDAP) authentication on a bastion host.
        
        @param request: GetInstanceLDAPAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceLDAPAuthServerResponse
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
        """
        @summary Queries the settings of Lightweight Directory Access Protocol (LDAP) authentication on a bastion host.
        
        @param request: GetInstanceLDAPAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceLDAPAuthServerResponse
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
        """
        @summary Queries the settings of Lightweight Directory Access Protocol (LDAP) authentication on a bastion host.
        
        @param request: GetInstanceLDAPAuthServerRequest
        @return: GetInstanceLDAPAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_ldapauth_server_with_options(request, runtime)

    async def get_instance_ldapauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse:
        """
        @summary Queries the settings of Lightweight Directory Access Protocol (LDAP) authentication on a bastion host.
        
        @param request: GetInstanceLDAPAuthServerRequest
        @return: GetInstanceLDAPAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_ldapauth_server_with_options_async(request, runtime)

    def get_instance_store_info_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceStoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceStoreInfoResponse:
        """
        @param request: GetInstanceStoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceStoreInfoResponse
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
            action='GetInstanceStoreInfo',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceStoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_store_info_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceStoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceStoreInfoResponse:
        """
        @param request: GetInstanceStoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceStoreInfoResponse
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
            action='GetInstanceStoreInfo',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceStoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_store_info(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceStoreInfoRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceStoreInfoResponse:
        """
        @param request: GetInstanceStoreInfoRequest
        @return: GetInstanceStoreInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_store_info_with_options(request, runtime)

    async def get_instance_store_info_async(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceStoreInfoRequest,
    ) -> yundun_bastionhost_20191209_models.GetInstanceStoreInfoResponse:
        """
        @param request: GetInstanceStoreInfoRequest
        @return: GetInstanceStoreInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_store_info_with_options_async(request, runtime)

    def get_instance_two_factor_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetInstanceTwoFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse:
        """
        @summary Queries the settings of two-factor authentication on a bastion host.
        
        @description You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
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
        @summary Queries the settings of two-factor authentication on a bastion host.
        
        @description You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
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
        @summary Queries the settings of two-factor authentication on a bastion host.
        
        @description You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
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
        @summary Queries the settings of two-factor authentication on a bastion host.
        
        @description You can call this operation to query the settings of two-factor authentication on a bastion host. After you enable two-factor authentication, Bastionhost sends a verification code to a local user when the local user logs on to a bastion host. A local user can log on to the bastion host only when the local user enters the valid username and password and the verification code. This reduces the security risks caused by account information leaks.
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
        """
        @summary Queries the detailed information about a network domain.
        
        @param request: GetNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkDomainResponse
        """
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
        """
        @summary Queries the detailed information about a network domain.
        
        @param request: GetNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkDomainResponse
        """
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
        """
        @summary Queries the detailed information about a network domain.
        
        @param request: GetNetworkDomainRequest
        @return: GetNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_network_domain_with_options(request, runtime)

    async def get_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.GetNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.GetNetworkDomainResponse:
        """
        @summary Queries the detailed information about a network domain.
        
        @param request: GetNetworkDomainRequest
        @return: GetNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_network_domain_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyResponse:
        """
        @summary Queries the detailed information about a control policy.
        
        @param request: GetPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
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
        """
        @summary Queries the detailed information about a control policy.
        
        @param request: GetPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyResponse
        """
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
        """
        @summary Queries the detailed information about a control policy.
        
        @param request: GetPolicyRequest
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyResponse:
        """
        @summary Queries the detailed information about a control policy.
        
        @param request: GetPolicyRequest
        @return: GetPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_asset_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyAssetScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse:
        """
        @summary Queries the assets to which a control policy applies.
        
        @param request: GetPolicyAssetScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyAssetScopeResponse
        """
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
        """
        @summary Queries the assets to which a control policy applies.
        
        @param request: GetPolicyAssetScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyAssetScopeResponse
        """
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
        """
        @summary Queries the assets to which a control policy applies.
        
        @param request: GetPolicyAssetScopeRequest
        @return: GetPolicyAssetScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_asset_scope_with_options(request, runtime)

    async def get_policy_asset_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyAssetScopeRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyAssetScopeResponse:
        """
        @summary Queries the assets to which a control policy applies.
        
        @param request: GetPolicyAssetScopeRequest
        @return: GetPolicyAssetScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_asset_scope_with_options_async(request, runtime)

    def get_policy_user_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyUserScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse:
        """
        @summary Queries the scope of users to whom a control policy applies.
        
        @param request: GetPolicyUserScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyUserScopeResponse
        """
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
        """
        @summary Queries the scope of users to whom a control policy applies.
        
        @param request: GetPolicyUserScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyUserScopeResponse
        """
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
        """
        @summary Queries the scope of users to whom a control policy applies.
        
        @param request: GetPolicyUserScopeRequest
        @return: GetPolicyUserScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_user_scope_with_options(request, runtime)

    async def get_policy_user_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.GetPolicyUserScopeRequest,
    ) -> yundun_bastionhost_20191209_models.GetPolicyUserScopeResponse:
        """
        @summary Queries the scope of users to whom a control policy applies.
        
        @param request: GetPolicyUserScopeRequest
        @return: GetPolicyUserScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_user_scope_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetRuleResponse:
        """
        @summary Queries the detailed information about an authorization rule.
        
        @param request: GetRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleResponse
        """
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
        """
        @summary Queries the detailed information about an authorization rule.
        
        @param request: GetRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleResponse
        """
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
        """
        @summary Queries the detailed information about an authorization rule.
        
        @param request: GetRuleRequest
        @return: GetRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.GetRuleRequest,
    ) -> yundun_bastionhost_20191209_models.GetRuleResponse:
        """
        @summary Queries the detailed information about an authorization rule.
        
        @param request: GetRuleRequest
        @return: GetRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        """
        @summary Queries the details of a user of the specified bastion host.
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
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
        """
        @summary Queries the details of a user of the specified bastion host.
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
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
        """
        @summary Queries the details of a user of the specified bastion host.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        """
        @summary Queries the details of a user of the specified bastion host.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserGroupResponse:
        """
        @summary Queries the details of a user group in a bastion host.
        
        @param request: GetUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupResponse
        """
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
        """
        @summary Queries the details of a user group in a bastion host.
        
        @param request: GetUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupResponse
        """
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
        """
        @summary Queries the details of a user group in a bastion host.
        
        @param request: GetUserGroupRequest
        @return: GetUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    async def get_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.GetUserGroupResponse:
        """
        @summary Queries the details of a user group in a bastion host.
        
        @param request: GetUserGroupRequest
        @return: GetUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_group_with_options_async(request, runtime)

    def list_approve_commands_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListApproveCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListApproveCommandsResponse:
        """
        @summary Queries commands to be reviewed.
        
        @description You can call this operation to query commands to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListApproveCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApproveCommandsResponse
        """
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
        """
        @summary Queries commands to be reviewed.
        
        @description You can call this operation to query commands to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListApproveCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApproveCommandsResponse
        """
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
        """
        @summary Queries commands to be reviewed.
        
        @description You can call this operation to query commands to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListApproveCommandsRequest
        @return: ListApproveCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_approve_commands_with_options(request, runtime)

    async def list_approve_commands_async(
        self,
        request: yundun_bastionhost_20191209_models.ListApproveCommandsRequest,
    ) -> yundun_bastionhost_20191209_models.ListApproveCommandsResponse:
        """
        @summary Queries commands to be reviewed.
        
        @description You can call this operation to query commands to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListApproveCommandsRequest
        @return: ListApproveCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_approve_commands_with_options_async(request, runtime)

    def list_database_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse:
        """
        @summary Queries the database accounts of a database.
        
        @param request: ListDatabaseAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccountsResponse
        """
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
        """
        @summary Queries the database accounts of a database.
        
        @param request: ListDatabaseAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccountsResponse
        """
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
        """
        @summary Queries the database accounts of a database.
        
        @param request: ListDatabaseAccountsRequest
        @return: ListDatabaseAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_database_accounts_with_options(request, runtime)

    async def list_database_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsResponse:
        """
        @summary Queries the database accounts of a database.
        
        @param request: ListDatabaseAccountsRequest
        @return: ListDatabaseAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_database_accounts_with_options_async(request, runtime)

    def list_database_accounts_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse:
        """
        @summary Queries the database accounts of a database and whether a user is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccountsForUserResponse
        """
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
        """
        @summary Queries the database accounts of a database and whether a user is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccountsForUserResponse
        """
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
        """
        @summary Queries the database accounts of a database and whether a user is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserRequest
        @return: ListDatabaseAccountsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_database_accounts_for_user_with_options(request, runtime)

    async def list_database_accounts_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserResponse:
        """
        @summary Queries the database accounts of a database and whether a user is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserRequest
        @return: ListDatabaseAccountsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_database_accounts_for_user_with_options_async(request, runtime)

    def list_database_accounts_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse:
        """
        @summary Queries the database accounts of a database and whether a user group is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccountsForUserGroupResponse
        """
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
        """
        @summary Queries the database accounts of a database and whether a user group is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabaseAccountsForUserGroupResponse
        """
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
        """
        @summary Queries the database accounts of a database and whether a user group is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserGroupRequest
        @return: ListDatabaseAccountsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_database_accounts_for_user_group_with_options(request, runtime)

    async def list_database_accounts_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabaseAccountsForUserGroupResponse:
        """
        @summary Queries the database accounts of a database and whether a user group is authorized to manage each database account.
        
        @param request: ListDatabaseAccountsForUserGroupRequest
        @return: ListDatabaseAccountsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_database_accounts_for_user_group_with_options_async(request, runtime)

    def list_databases_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesResponse:
        """
        @summary Queries the databases that are managed by a bastion host.
        
        @param request: ListDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesResponse
        """
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
        """
        @summary Queries the databases that are managed by a bastion host.
        
        @param request: ListDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesResponse
        """
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
        """
        @summary Queries the databases that are managed by a bastion host.
        
        @param request: ListDatabasesRequest
        @return: ListDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_databases_with_options(request, runtime)

    async def list_databases_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesResponse:
        """
        @summary Queries the databases that are managed by a bastion host.
        
        @param request: ListDatabasesRequest
        @return: ListDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_databases_with_options_async(request, runtime)

    def list_databases_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserResponse:
        """
        @summary Queries the databases that a user is authorized to manage.
        
        @param request: ListDatabasesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesForUserResponse
        """
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
        """
        @summary Queries the databases that a user is authorized to manage.
        
        @param request: ListDatabasesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesForUserResponse
        """
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
        """
        @summary Queries the databases that a user is authorized to manage.
        
        @param request: ListDatabasesForUserRequest
        @return: ListDatabasesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_databases_for_user_with_options(request, runtime)

    async def list_databases_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserResponse:
        """
        @summary Queries the databases that a user is authorized to manage.
        
        @param request: ListDatabasesForUserRequest
        @return: ListDatabasesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_databases_for_user_with_options_async(request, runtime)

    def list_databases_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse:
        """
        @summary Queries the databases that a user group is authorized to manage.
        
        @param request: ListDatabasesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesForUserGroupResponse
        """
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
        """
        @summary Queries the databases that a user group is authorized to manage.
        
        @param request: ListDatabasesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesForUserGroupResponse
        """
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
        """
        @summary Queries the databases that a user group is authorized to manage.
        
        @param request: ListDatabasesForUserGroupRequest
        @return: ListDatabasesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_databases_for_user_group_with_options(request, runtime)

    async def list_databases_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListDatabasesForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListDatabasesForUserGroupResponse:
        """
        @summary Queries the databases that a user group is authorized to manage.
        
        @param request: ListDatabasesForUserGroupRequest
        @return: ListDatabasesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_databases_for_user_group_with_options_async(request, runtime)

    def list_host_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        """
        @summary Queries accounts of a specified host.
        
        @param request: ListHostAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
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
        """
        @summary Queries accounts of a specified host.
        
        @param request: ListHostAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
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
        """
        @summary Queries accounts of a specified host.
        
        @param request: ListHostAccountsRequest
        @return: ListHostAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_with_options(request, runtime)

    async def list_host_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        """
        @summary Queries accounts of a specified host.
        
        @param request: ListHostAccountsRequest
        @return: ListHostAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_with_options_async(request, runtime)

    def list_host_accounts_for_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse:
        """
        @summary Queries the host accounts that are associated with a shared key.
        
        @param request: ListHostAccountsForHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsForHostShareKeyResponse
        """
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
        """
        @summary Queries the host accounts that are associated with a shared key.
        
        @param request: ListHostAccountsForHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsForHostShareKeyResponse
        """
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
        """
        @summary Queries the host accounts that are associated with a shared key.
        
        @param request: ListHostAccountsForHostShareKeyRequest
        @return: ListHostAccountsForHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_host_share_key_with_options(request, runtime)

    async def list_host_accounts_for_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse:
        """
        @summary Queries the host accounts that are associated with a shared key.
        
        @param request: ListHostAccountsForHostShareKeyRequest
        @return: ListHostAccountsForHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_for_host_share_key_with_options_async(request, runtime)

    def list_host_accounts_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        """
        @summary Queries the host accounts that the specified user is authorized to manage on the specified host.
        
        @param request: ListHostAccountsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsForUserResponse
        """
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
        """
        @summary Queries the host accounts that the specified user is authorized to manage on the specified host.
        
        @param request: ListHostAccountsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsForUserResponse
        """
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
        """
        @summary Queries the host accounts that the specified user is authorized to manage on the specified host.
        
        @param request: ListHostAccountsForUserRequest
        @return: ListHostAccountsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_user_with_options(request, runtime)

    async def list_host_accounts_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        """
        @summary Queries the host accounts that the specified user is authorized to manage on the specified host.
        
        @param request: ListHostAccountsForUserRequest
        @return: ListHostAccountsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_for_user_with_options_async(request, runtime)

    def list_host_accounts_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse:
        """
        @summary Queries the host accounts of the specified host that the specified user group is authorized to manage.
        
        @param request: ListHostAccountsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsForUserGroupResponse
        """
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
        """
        @summary Queries the host accounts of the specified host that the specified user group is authorized to manage.
        
        @param request: ListHostAccountsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostAccountsForUserGroupResponse
        """
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
        """
        @summary Queries the host accounts of the specified host that the specified user group is authorized to manage.
        
        @param request: ListHostAccountsForUserGroupRequest
        @return: ListHostAccountsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_user_group_with_options(request, runtime)

    async def list_host_accounts_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse:
        """
        @summary Queries the host accounts of the specified host that the specified user group is authorized to manage.
        
        @param request: ListHostAccountsForUserGroupRequest
        @return: ListHostAccountsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_for_user_group_with_options_async(request, runtime)

    def list_host_group_account_names_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse:
        """
        @summary Queries the names of the host accounts that a specified user is authorized to manage in a specified host group.
        
        @param request: ListHostGroupAccountNamesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupAccountNamesForUserResponse
        """
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
        """
        @summary Queries the names of the host accounts that a specified user is authorized to manage in a specified host group.
        
        @param request: ListHostGroupAccountNamesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupAccountNamesForUserResponse
        """
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
        """
        @summary Queries the names of the host accounts that a specified user is authorized to manage in a specified host group.
        
        @param request: ListHostGroupAccountNamesForUserRequest
        @return: ListHostGroupAccountNamesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_group_account_names_for_user_with_options(request, runtime)

    async def list_host_group_account_names_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse:
        """
        @summary Queries the names of the host accounts that a specified user is authorized to manage in a specified host group.
        
        @param request: ListHostGroupAccountNamesForUserRequest
        @return: ListHostGroupAccountNamesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_group_account_names_for_user_with_options_async(request, runtime)

    def list_host_group_account_names_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse:
        """
        @summary Queries the names of the host accounts that a user group is authorized to manage in a host group.
        
        @param request: ListHostGroupAccountNamesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupAccountNamesForUserGroupResponse
        """
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
        """
        @summary Queries the names of the host accounts that a user group is authorized to manage in a host group.
        
        @param request: ListHostGroupAccountNamesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupAccountNamesForUserGroupResponse
        """
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
        """
        @summary Queries the names of the host accounts that a user group is authorized to manage in a host group.
        
        @param request: ListHostGroupAccountNamesForUserGroupRequest
        @return: ListHostGroupAccountNamesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_group_account_names_for_user_group_with_options(request, runtime)

    async def list_host_group_account_names_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse:
        """
        @summary Queries the names of the host accounts that a user group is authorized to manage in a host group.
        
        @param request: ListHostGroupAccountNamesForUserGroupRequest
        @return: ListHostGroupAccountNamesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_group_account_names_for_user_group_with_options_async(request, runtime)

    def list_host_groups_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsResponse:
        """
        @summary Queries a list of asset groups that are managed by a bastion host.
        
        @param request: ListHostGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupsResponse
        """
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
        """
        @summary Queries a list of asset groups that are managed by a bastion host.
        
        @param request: ListHostGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupsResponse
        """
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
        """
        @summary Queries a list of asset groups that are managed by a bastion host.
        
        @param request: ListHostGroupsRequest
        @return: ListHostGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_with_options(request, runtime)

    async def list_host_groups_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsResponse:
        """
        @summary Queries a list of asset groups that are managed by a bastion host.
        
        @param request: ListHostGroupsRequest
        @return: ListHostGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_groups_with_options_async(request, runtime)

    def list_host_groups_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse:
        """
        @summary Queries a list of host groups that a bastion host user is authorized or is not authorized to manage.
        
        @param request: ListHostGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupsForUserResponse
        """
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
        """
        @summary Queries a list of host groups that a bastion host user is authorized or is not authorized to manage.
        
        @param request: ListHostGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupsForUserResponse
        """
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
        """
        @summary Queries a list of host groups that a bastion host user is authorized or is not authorized to manage.
        
        @param request: ListHostGroupsForUserRequest
        @return: ListHostGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_for_user_with_options(request, runtime)

    async def list_host_groups_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse:
        """
        @summary Queries a list of host groups that a bastion host user is authorized or is not authorized to manage.
        
        @param request: ListHostGroupsForUserRequest
        @return: ListHostGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_groups_for_user_with_options_async(request, runtime)

    def list_host_groups_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse:
        """
        @summary Queries the hosts that a specified user group is authorized or not authorized to manage.
        
        @param request: ListHostGroupsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupsForUserGroupResponse
        """
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
        """
        @summary Queries the hosts that a specified user group is authorized or not authorized to manage.
        
        @param request: ListHostGroupsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostGroupsForUserGroupResponse
        """
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
        """
        @summary Queries the hosts that a specified user group is authorized or not authorized to manage.
        
        @param request: ListHostGroupsForUserGroupRequest
        @return: ListHostGroupsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_for_user_group_with_options(request, runtime)

    async def list_host_groups_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse:
        """
        @summary Queries the hosts that a specified user group is authorized or not authorized to manage.
        
        @param request: ListHostGroupsForUserGroupRequest
        @return: ListHostGroupsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_groups_for_user_group_with_options_async(request, runtime)

    def list_host_share_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostShareKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostShareKeysResponse:
        """
        @summary Queries the shared keys that are associated with a host.
        
        @param request: ListHostShareKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostShareKeysResponse
        """
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
        """
        @summary Queries the shared keys that are associated with a host.
        
        @param request: ListHostShareKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostShareKeysResponse
        """
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
        """
        @summary Queries the shared keys that are associated with a host.
        
        @param request: ListHostShareKeysRequest
        @return: ListHostShareKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_host_share_keys_with_options(request, runtime)

    async def list_host_share_keys_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostShareKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostShareKeysResponse:
        """
        @summary Queries the shared keys that are associated with a host.
        
        @param request: ListHostShareKeysRequest
        @return: ListHostShareKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_host_share_keys_with_options_async(request, runtime)

    def list_hosts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        """
        @summary Queries the hosts in a bastion host.
        
        @param request: ListHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostsResponse
        """
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
        """
        @summary Queries the hosts in a bastion host.
        
        @param request: ListHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostsResponse
        """
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
        """
        @summary Queries the hosts in a bastion host.
        
        @param request: ListHostsRequest
        @return: ListHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_with_options(request, runtime)

    async def list_hosts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        """
        @summary Queries the hosts in a bastion host.
        
        @param request: ListHostsRequest
        @return: ListHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hosts_with_options_async(request, runtime)

    def list_hosts_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserResponse:
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostsForUserResponse
        """
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
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostsForUserResponse
        """
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
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserRequest
        @return: ListHostsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_for_user_with_options(request, runtime)

    async def list_hosts_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserResponse:
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserRequest
        @return: ListHostsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hosts_for_user_with_options_async(request, runtime)

    def list_hosts_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse:
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostsForUserGroupResponse
        """
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
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHostsForUserGroupResponse
        """
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
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserGroupRequest
        @return: ListHostsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_for_user_group_with_options(request, runtime)

    async def list_hosts_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse:
        """
        @summary Queries the hosts that a user group is authorized or not authorized to manage.
        
        @param request: ListHostsForUserGroupRequest
        @return: ListHostsForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_hosts_for_user_group_with_options_async(request, runtime)

    def list_network_domains_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListNetworkDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListNetworkDomainsResponse:
        """
        @summary Queries the network domains created in a bastion host.
        
        @param request: ListNetworkDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkDomainsResponse
        """
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
        """
        @summary Queries the network domains created in a bastion host.
        
        @param request: ListNetworkDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkDomainsResponse
        """
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
        """
        @summary Queries the network domains created in a bastion host.
        
        @param request: ListNetworkDomainsRequest
        @return: ListNetworkDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_domains_with_options(request, runtime)

    async def list_network_domains_async(
        self,
        request: yundun_bastionhost_20191209_models.ListNetworkDomainsRequest,
    ) -> yundun_bastionhost_20191209_models.ListNetworkDomainsResponse:
        """
        @summary Queries the network domains created in a bastion host.
        
        @param request: ListNetworkDomainsRequest
        @return: ListNetworkDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_domains_with_options_async(request, runtime)

    def list_operation_database_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse:
        """
        @summary Queries a list of database accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabaseAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationDatabaseAccountsResponse
        """
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
        """
        @summary Queries a list of database accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabaseAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationDatabaseAccountsResponse
        """
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
        """
        @summary Queries a list of database accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabaseAccountsRequest
        @return: ListOperationDatabaseAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_operation_database_accounts_with_options(request, runtime)

    async def list_operation_database_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabaseAccountsResponse:
        """
        @summary Queries a list of database accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabaseAccountsRequest
        @return: ListOperationDatabaseAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_database_accounts_with_options_async(request, runtime)

    def list_operation_databases_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabasesResponse:
        """
        @summary Queries a list of databases that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationDatabasesResponse
        """
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
        """
        @summary Queries a list of databases that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationDatabasesResponse
        """
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
        """
        @summary Queries a list of databases that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabasesRequest
        @return: ListOperationDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_operation_databases_with_options(request, runtime)

    async def list_operation_databases_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationDatabasesRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationDatabasesResponse:
        """
        @summary Queries a list of databases that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationDatabasesRequest
        @return: ListOperationDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_databases_with_options_async(request, runtime)

    def list_operation_host_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse:
        """
        @summary Queries a list of host accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationHostAccountsResponse
        """
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
        """
        @summary Queries a list of host accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationHostAccountsResponse
        """
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
        """
        @summary Queries a list of host accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostAccountsRequest
        @return: ListOperationHostAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_operation_host_accounts_with_options(request, runtime)

    async def list_operation_host_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostAccountsResponse:
        """
        @summary Queries a list of host accounts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostAccountsRequest
        @return: ListOperationHostAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_host_accounts_with_options_async(request, runtime)

    def list_operation_hosts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostsResponse:
        """
        @summary Queries a list of hosts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationHostsResponse
        """
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
        """
        @summary Queries a list of hosts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationHostsResponse
        """
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
        """
        @summary Queries a list of hosts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostsRequest
        @return: ListOperationHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_operation_hosts_with_options(request, runtime)

    async def list_operation_hosts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationHostsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationHostsResponse:
        """
        @summary Queries a list of hosts that the current Resource Access Management (RAM) user is authorized to manage.
        
        @param request: ListOperationHostsRequest
        @return: ListOperationHostsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_hosts_with_options_async(request, runtime)

    def list_operation_tickets_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListOperationTicketsResponse:
        """
        @summary Queries O\\\\\\\\\\\\&M applications to be reviewed.
        
        @description You can call this operation to query the O\\&M applications to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListOperationTicketsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationTicketsResponse
        """
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
        """
        @summary Queries O\\\\\\\\\\\\&M applications to be reviewed.
        
        @description You can call this operation to query the O\\&M applications to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListOperationTicketsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOperationTicketsResponse
        """
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
        """
        @summary Queries O\\\\\\\\\\\\&M applications to be reviewed.
        
        @description You can call this operation to query the O\\&M applications to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListOperationTicketsRequest
        @return: ListOperationTicketsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_operation_tickets_with_options(request, runtime)

    async def list_operation_tickets_async(
        self,
        request: yundun_bastionhost_20191209_models.ListOperationTicketsRequest,
    ) -> yundun_bastionhost_20191209_models.ListOperationTicketsResponse:
        """
        @summary Queries O\\\\\\\\\\\\&M applications to be reviewed.
        
        @description You can call this operation to query the O\\&M applications to be reviewed by a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListOperationTicketsRequest
        @return: ListOperationTicketsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_operation_tickets_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListPoliciesResponse:
        """
        @summary Queries a list of control policies.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
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
        """
        @summary Queries a list of control policies.
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
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
        """
        @summary Queries a list of control policies.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: yundun_bastionhost_20191209_models.ListPoliciesRequest,
    ) -> yundun_bastionhost_20191209_models.ListPoliciesResponse:
        """
        @summary Queries a list of control policies.
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListRulesResponse:
        """
        @summary Queries a list of authorization rules of a bastion host.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
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
        """
        @summary Queries a list of authorization rules of a bastion host.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        """
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
        """
        @summary Queries a list of authorization rules of a bastion host.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: yundun_bastionhost_20191209_models.ListRulesRequest,
    ) -> yundun_bastionhost_20191209_models.ListRulesResponse:
        """
        @summary Queries a list of authorization rules of a bastion host.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        """
        @summary Queries the tags that are added to a resource.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        """
        @summary Queries the tags bound to one or more Bastionhost instances.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Queries the tags bound to one or more Bastionhost instances.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Queries the tags bound to one or more Bastionhost instances.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        """
        @summary Queries the tags bound to one or more Bastionhost instances.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUserGroupsResponse:
        """
        @summary Queries a list of user groups on a bastion host.
        
        @param request: ListUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsResponse
        """
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
        """
        @summary Queries a list of user groups on a bastion host.
        
        @param request: ListUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsResponse
        """
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
        """
        @summary Queries a list of user groups on a bastion host.
        
        @param request: ListUserGroupsRequest
        @return: ListUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUserGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ListUserGroupsResponse:
        """
        @summary Queries a list of user groups on a bastion host.
        
        @param request: ListUserGroupsRequest
        @return: ListUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def list_user_public_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListUserPublicKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUserPublicKeysResponse:
        """
        @summary Queries all public keys of the specified user.
        
        @param request: ListUserPublicKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserPublicKeysResponse
        """
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
        """
        @summary Queries all public keys of the specified user.
        
        @param request: ListUserPublicKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserPublicKeysResponse
        """
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
        """
        @summary Queries all public keys of the specified user.
        
        @param request: ListUserPublicKeysRequest
        @return: ListUserPublicKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_public_keys_with_options(request, runtime)

    async def list_user_public_keys_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUserPublicKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListUserPublicKeysResponse:
        """
        @summary Queries all public keys of the specified user.
        
        @param request: ListUserPublicKeysRequest
        @return: ListUserPublicKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_public_keys_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        """
        @summary Queries a list of users of a bastion host.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
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
        """
        @summary Queries a list of users of a bastion host.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
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
        """
        @summary Queries a list of users of a bastion host.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        """
        @summary Queries a list of users of a bastion host.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def lock_users_with_options(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        """
        @summary Locks one or more users of a bastion host.
        
        @description # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](https://help.aliyun.com/document_detail/204590.html) operation.
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
        @summary Locks one or more users of a bastion host.
        
        @description # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](https://help.aliyun.com/document_detail/204590.html) operation.
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
        @summary Locks one or more users of a bastion host.
        
        @description # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](https://help.aliyun.com/document_detail/204590.html) operation.
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
        @summary Locks one or more users of a bastion host.
        
        @description # Description
        You can call this operation to lock one or more users of a bastion host. If a user does not need to use a bastion host to perform O\\&M operations within a specific period of time, you can lock the user. The locked user can no longer log on to or perform O\\&M operations on the hosts on which the user is granted permissions. If you want to unlock the user later, you can call the [UnlockUsers](https://help.aliyun.com/document_detail/204590.html) operation.
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
        """
        @summary Modifies the basic information about a database.
        
        @param request: ModifyDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseResponse
        """
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
        """
        @summary Modifies the basic information about a database.
        
        @param request: ModifyDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseResponse
        """
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
        """
        @summary Modifies the basic information about a database.
        
        @param request: ModifyDatabaseRequest
        @return: ModifyDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_with_options(request, runtime)

    async def modify_database_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseResponse:
        """
        @summary Modifies the basic information about a database.
        
        @param request: ModifyDatabaseRequest
        @return: ModifyDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_with_options_async(request, runtime)

    def modify_database_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse:
        """
        @summary Modifies the basic information about a database account.
        
        @param request: ModifyDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseAccountResponse
        """
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
        """
        @summary Modifies the basic information about a database account.
        
        @param request: ModifyDatabaseAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDatabaseAccountResponse
        """
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
        """
        @summary Modifies the basic information about a database account.
        
        @param request: ModifyDatabaseAccountRequest
        @return: ModifyDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_database_account_with_options(request, runtime)

    async def modify_database_account_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyDatabaseAccountRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyDatabaseAccountResponse:
        """
        @summary Modifies the basic information about a database account.
        
        @param request: ModifyDatabaseAccountRequest
        @return: ModifyDatabaseAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_account_with_options_async(request, runtime)

    def modify_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        """
        @summary Modifies information about a host. The information includes the address, name, and description of the host and the operating system that the host runs.
        
        @description You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
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
        if not UtilClient.is_unset(request.pref_kex):
            query['PrefKex'] = request.pref_kex
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
        @summary Modifies information about a host. The information includes the address, name, and description of the host and the operating system that the host runs.
        
        @description You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
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
        if not UtilClient.is_unset(request.pref_kex):
            query['PrefKex'] = request.pref_kex
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
        @summary Modifies information about a host. The information includes the address, name, and description of the host and the operating system that the host runs.
        
        @description You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
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
        @summary Modifies information about a host. The information includes the address, name, and description of the host and the operating system that the host runs.
        
        @description You can call the ModifyHost operation to modify the basic information about a host in a data center, an Elastic Compute Service (ECS) instance, or a host in an ApsaraDB MyBase dedicated cluster.
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
        """
        @summary Modifies the information about a host account, such as the username, password, and private key of the host account.
        
        @param request: ModifyHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostAccountResponse
        """
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
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
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
        """
        @summary Modifies the information about a host account, such as the username, password, and private key of the host account.
        
        @param request: ModifyHostAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostAccountResponse
        """
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
        if not UtilClient.is_unset(request.privilege_type):
            query['PrivilegeType'] = request.privilege_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rotation_mode):
            query['RotationMode'] = request.rotation_mode
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
        """
        @summary Modifies the information about a host account, such as the username, password, and private key of the host account.
        
        @param request: ModifyHostAccountRequest
        @return: ModifyHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_account_with_options(request, runtime)

    async def modify_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostAccountResponse:
        """
        @summary Modifies the information about a host account, such as the username, password, and private key of the host account.
        
        @param request: ModifyHostAccountRequest
        @return: ModifyHostAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_account_with_options_async(request, runtime)

    def modify_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostGroupResponse:
        """
        @summary Modifies the name or description of the specified host group.
        
        @param request: ModifyHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostGroupResponse
        """
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
        """
        @summary Modifies the name or description of the specified host group.
        
        @param request: ModifyHostGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostGroupResponse
        """
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
        """
        @summary Modifies the name or description of the specified host group.
        
        @param request: ModifyHostGroupRequest
        @return: ModifyHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_group_with_options(request, runtime)

    async def modify_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostGroupResponse:
        """
        @summary Modifies the name or description of the specified host group.
        
        @param request: ModifyHostGroupRequest
        @return: ModifyHostGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_group_with_options_async(request, runtime)

    def modify_host_share_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostShareKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse:
        """
        @summary Modifies a shared key.
        
        @param request: ModifyHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostShareKeyResponse
        """
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
        """
        @summary Modifies a shared key.
        
        @param request: ModifyHostShareKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostShareKeyResponse
        """
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
        """
        @summary Modifies a shared key.
        
        @param request: ModifyHostShareKeyRequest
        @return: ModifyHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_host_share_key_with_options(request, runtime)

    async def modify_host_share_key_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostShareKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse:
        """
        @summary Modifies a shared key.
        
        @param request: ModifyHostShareKeyRequest
        @return: ModifyHostShareKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_share_key_with_options_async(request, runtime)

    def modify_hosts_active_address_type_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        """
        @summary Changes the portal type of one or more hosts for O\\&M.
        
        @param request: ModifyHostsActiveAddressTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostsActiveAddressTypeResponse
        """
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
        """
        @summary Changes the portal type of one or more hosts for O\\&M.
        
        @param request: ModifyHostsActiveAddressTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHostsActiveAddressTypeResponse
        """
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
        """
        @summary Changes the portal type of one or more hosts for O\\&M.
        
        @param request: ModifyHostsActiveAddressTypeRequest
        @return: ModifyHostsActiveAddressTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hosts_active_address_type_with_options(request, runtime)

    async def modify_hosts_active_address_type_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        """
        @summary Changes the portal type of one or more hosts for O\\&M.
        
        @param request: ModifyHostsActiveAddressTypeRequest
        @return: ModifyHostsActiveAddressTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hosts_active_address_type_with_options_async(request, runtime)

    def modify_hosts_port_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        """
        @summary Changes the port for the O\\\\\\\\\\\\&M protocol on one or more hosts.
        
        @description ## Usage notes
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
        @summary Changes the port for the O\\\\\\\\\\\\&M protocol on one or more hosts.
        
        @description ## Usage notes
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
        @summary Changes the port for the O\\\\\\\\\\\\&M protocol on one or more hosts.
        
        @description ## Usage notes
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
        @summary Changes the port for the O\\\\\\\\\\\\&M protocol on one or more hosts.
        
        @description ## Usage notes
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
        """
        @summary Modifies the settings of the Active Directory (AD) authentication server of a bastion host.
        
        @param request: ModifyInstanceADAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceADAuthServerResponse
        """
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
        """
        @summary Modifies the settings of the Active Directory (AD) authentication server of a bastion host.
        
        @param request: ModifyInstanceADAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceADAuthServerResponse
        """
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
        """
        @summary Modifies the settings of the Active Directory (AD) authentication server of a bastion host.
        
        @param request: ModifyInstanceADAuthServerRequest
        @return: ModifyInstanceADAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_adauth_server_with_options(request, runtime)

    async def modify_instance_adauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse:
        """
        @summary Modifies the settings of the Active Directory (AD) authentication server of a bastion host.
        
        @param request: ModifyInstanceADAuthServerRequest
        @return: ModifyInstanceADAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_adauth_server_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        """
        @summary Modifies the information about a bastion host.
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
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
        """
        @summary Modifies the information about a bastion host.
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
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
        """
        @summary Modifies the information about a bastion host.
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        """
        @summary Modifies the information about a bastion host.
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_ldapauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse:
        """
        @summary Modifies the settings of the Lightweight Directory Access Protocol (LDAP) authentication server of a bastion host.
        
        @param request: ModifyInstanceLDAPAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceLDAPAuthServerResponse
        """
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
        """
        @summary Modifies the settings of the Lightweight Directory Access Protocol (LDAP) authentication server of a bastion host.
        
        @param request: ModifyInstanceLDAPAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceLDAPAuthServerResponse
        """
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
        """
        @summary Modifies the settings of the Lightweight Directory Access Protocol (LDAP) authentication server of a bastion host.
        
        @param request: ModifyInstanceLDAPAuthServerRequest
        @return: ModifyInstanceLDAPAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_ldapauth_server_with_options(request, runtime)

    async def modify_instance_ldapauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse:
        """
        @summary Modifies the settings of the Lightweight Directory Access Protocol (LDAP) authentication server of a bastion host.
        
        @param request: ModifyInstanceLDAPAuthServerRequest
        @return: ModifyInstanceLDAPAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_ldapauth_server_with_options_async(request, runtime)

    def modify_instance_two_factor_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse:
        """
        @summary Modifies the two-factor authentication settings of a bastion host.
        
        @param request: ModifyInstanceTwoFactorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTwoFactorResponse
        """
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
        """
        @summary Modifies the two-factor authentication settings of a bastion host.
        
        @param request: ModifyInstanceTwoFactorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceTwoFactorResponse
        """
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
        """
        @summary Modifies the two-factor authentication settings of a bastion host.
        
        @param request: ModifyInstanceTwoFactorRequest
        @return: ModifyInstanceTwoFactorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_two_factor_with_options(request, runtime)

    async def modify_instance_two_factor_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse:
        """
        @summary Modifies the two-factor authentication settings of a bastion host.
        
        @param request: ModifyInstanceTwoFactorRequest
        @return: ModifyInstanceTwoFactorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_two_factor_with_options_async(request, runtime)

    def modify_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse:
        """
        @summary Modifies the basic information about a network domain.
        
        @param request: ModifyNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNetworkDomainResponse
        """
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
        """
        @summary Modifies the basic information about a network domain.
        
        @param request: ModifyNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNetworkDomainResponse
        """
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
        """
        @summary Modifies the basic information about a network domain.
        
        @param request: ModifyNetworkDomainRequest
        @return: ModifyNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_network_domain_with_options(request, runtime)

    async def modify_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyNetworkDomainResponse:
        """
        @summary Modifies the basic information about a network domain.
        
        @param request: ModifyNetworkDomainRequest
        @return: ModifyNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_domain_with_options_async(request, runtime)

    def modify_policy_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyPolicyResponse:
        """
        @summary Modifies the basic information about a control policy.
        
        @param request: ModifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyResponse
        """
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
        """
        @summary Modifies the basic information about a control policy.
        
        @param request: ModifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyResponse
        """
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
        """
        @summary Modifies the basic information about a control policy.
        
        @param request: ModifyPolicyRequest
        @return: ModifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyPolicyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyPolicyResponse:
        """
        @summary Modifies the basic information about a control policy.
        
        @param request: ModifyPolicyRequest
        @return: ModifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def modify_rule_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyRuleResponse:
        """
        @summary Modifies the basic information of an authorization rule.
        
        @param request: ModifyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRuleResponse
        """
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
        """
        @summary Modifies the basic information of an authorization rule.
        
        @param request: ModifyRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRuleResponse
        """
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
        """
        @summary Modifies the basic information of an authorization rule.
        
        @param request: ModifyRuleRequest
        @return: ModifyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_with_options(request, runtime)

    async def modify_rule_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyRuleRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyRuleResponse:
        """
        @summary Modifies the basic information of an authorization rule.
        
        @param request: ModifyRuleRequest
        @return: ModifyRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_rule_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        """
        @summary Modifies the information about a user of a bastion host.
        
        @param request: ModifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserResponse
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
        """
        @summary Modifies the information about a user of a bastion host.
        
        @param request: ModifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserResponse
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
        """
        @summary Modifies the information about a user of a bastion host.
        
        @param request: ModifyUserRequest
        @return: ModifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        """
        @summary Modifies the information about a user of a bastion host.
        
        @param request: ModifyUserRequest
        @return: ModifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def modify_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserGroupResponse:
        """
        @summary Modifies the information about the specified user group.
        
        @param request: ModifyUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserGroupResponse
        """
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
        """
        @summary Modifies the information about the specified user group.
        
        @param request: ModifyUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserGroupResponse
        """
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
        """
        @summary Modifies the information about the specified user group.
        
        @param request: ModifyUserGroupRequest
        @return: ModifyUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_group_with_options(request, runtime)

    async def modify_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserGroupResponse:
        """
        @summary Modifies the information about the specified user group.
        
        @param request: ModifyUserGroupRequest
        @return: ModifyUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_group_with_options_async(request, runtime)

    def modify_user_public_key_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse:
        """
        @summary Modifies the public key of the user.
        
        @param request: ModifyUserPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserPublicKeyResponse
        """
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
        """
        @summary Modifies the public key of the user.
        
        @param request: ModifyUserPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserPublicKeyResponse
        """
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
        """
        @summary Modifies the public key of the user.
        
        @param request: ModifyUserPublicKeyRequest
        @return: ModifyUserPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_public_key_with_options(request, runtime)

    async def modify_user_public_key_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserPublicKeyRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserPublicKeyResponse:
        """
        @summary Modifies the public key of the user.
        
        @param request: ModifyUserPublicKeyRequest
        @return: ModifyUserPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_public_key_with_options_async(request, runtime)

    def move_databases_to_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse:
        """
        @summary Adds multiple databases to a network domain at a time.
        
        @param request: MoveDatabasesToNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveDatabasesToNetworkDomainResponse
        """
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
        """
        @summary Adds multiple databases to a network domain at a time.
        
        @param request: MoveDatabasesToNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveDatabasesToNetworkDomainResponse
        """
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
        """
        @summary Adds multiple databases to a network domain at a time.
        
        @param request: MoveDatabasesToNetworkDomainRequest
        @return: MoveDatabasesToNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_databases_to_network_domain_with_options(request, runtime)

    async def move_databases_to_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.MoveDatabasesToNetworkDomainResponse:
        """
        @summary Adds multiple databases to a network domain at a time.
        
        @param request: MoveDatabasesToNetworkDomainRequest
        @return: MoveDatabasesToNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_databases_to_network_domain_with_options_async(request, runtime)

    def move_hosts_to_network_domain_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse:
        """
        @summary Adds multiple hosts to a network domain at a time.
        
        @param request: MoveHostsToNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveHostsToNetworkDomainResponse
        """
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
        """
        @summary Adds multiple hosts to a network domain at a time.
        
        @param request: MoveHostsToNetworkDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveHostsToNetworkDomainResponse
        """
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
        """
        @summary Adds multiple hosts to a network domain at a time.
        
        @param request: MoveHostsToNetworkDomainRequest
        @return: MoveHostsToNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_hosts_to_network_domain_with_options(request, runtime)

    async def move_hosts_to_network_domain_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainRequest,
    ) -> yundun_bastionhost_20191209_models.MoveHostsToNetworkDomainResponse:
        """
        @summary Adds multiple hosts to a network domain at a time.
        
        @param request: MoveHostsToNetworkDomainRequest
        @return: MoveHostsToNetworkDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_hosts_to_network_domain_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        """
        @summary Moves a bastion host from one resource group to another resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
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
        """
        @summary Moves a bastion host from one resource group to another resource group.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
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
        """
        @summary Moves a bastion host from one resource group to another resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        """
        @summary Moves a bastion host from one resource group to another resource group.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def reject_approve_command_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RejectApproveCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RejectApproveCommandResponse:
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval section of the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to reject the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectApproveCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectApproveCommandResponse
        """
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
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval section of the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to reject the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectApproveCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectApproveCommandResponse
        """
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
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval section of the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to reject the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectApproveCommandRequest
        @return: RejectApproveCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reject_approve_command_with_options(request, runtime)

    async def reject_approve_command_async(
        self,
        request: yundun_bastionhost_20191209_models.RejectApproveCommandRequest,
    ) -> yundun_bastionhost_20191209_models.RejectApproveCommandResponse:
        """
        @summary If an O\\&M engineer attempts to run a command specified in the Command Approval section of the Create Control Policy page, the administrator is notified to review the command in the Bastionhost console. The command can be run only after it is approved by the administrator.
        
        @description You can call this operation as a Bastionhost administrator to reject the request to run a command of an O\\&M engineer.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectApproveCommandRequest
        @return: RejectApproveCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reject_approve_command_with_options_async(request, runtime)

    def reject_operation_ticket_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RejectOperationTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RejectOperationTicketResponse:
        """
        @summary If a Bastionhost administrator enables O\\\\\\&M Approval on the Create Control Policy page, O\\\\\\&M engineers can log on to assets to perform O\\\\\\&M operations only after the administrator approves their O\\\\\\&M applications.
        
        @description You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
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
        @summary If a Bastionhost administrator enables O\\\\\\&M Approval on the Create Control Policy page, O\\\\\\&M engineers can log on to assets to perform O\\\\\\&M operations only after the administrator approves their O\\\\\\&M applications.
        
        @description You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: RejectOperationTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectOperationTicketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
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
        @summary If a Bastionhost administrator enables O\\\\\\&M Approval on the Create Control Policy page, O\\\\\\&M engineers can log on to assets to perform O\\\\\\&M operations only after the administrator approves their O\\\\\\&M applications.
        
        @description You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
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
        @summary If a Bastionhost administrator enables O\\\\\\&M Approval on the Create Control Policy page, O\\\\\\&M engineers can log on to assets to perform O\\\\\\&M operations only after the administrator approves their O\\\\\\&M applications.
        
        @description You can call this operation to reject an O\\&M application of an O\\&M engineer as a Bastionhost administrator.
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
        """
        @summary Removes multiple databases from an asset group at a time.
        
        @param request: RemoveDatabasesFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDatabasesFromGroupResponse
        """
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
        """
        @summary Removes multiple databases from an asset group at a time.
        
        @param request: RemoveDatabasesFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveDatabasesFromGroupResponse
        """
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
        """
        @summary Removes multiple databases from an asset group at a time.
        
        @param request: RemoveDatabasesFromGroupRequest
        @return: RemoveDatabasesFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_databases_from_group_with_options(request, runtime)

    async def remove_databases_from_group_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveDatabasesFromGroupResponse:
        """
        @summary Removes multiple databases from an asset group at a time.
        
        @param request: RemoveDatabasesFromGroupRequest
        @return: RemoveDatabasesFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_databases_from_group_with_options_async(request, runtime)

    def remove_hosts_from_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        """
        @summary Removes multiple hosts from an asset group at a time.
        
        @description You can call the RemoveHostsFromGroup operation to remove multiple hosts from an asset group at a time. If you no longer need to manage some hosts in an asset group, you can call this operation to remove the hosts from the asset group.
        # [](#qps-)QPS limit
        You can call this API operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: RemoveHostsFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveHostsFromGroupResponse
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
        """
        @summary Removes multiple hosts from an asset group at a time.
        
        @description You can call the RemoveHostsFromGroup operation to remove multiple hosts from an asset group at a time. If you no longer need to manage some hosts in an asset group, you can call this operation to remove the hosts from the asset group.
        # [](#qps-)QPS limit
        You can call this API operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: RemoveHostsFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveHostsFromGroupResponse
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
        """
        @summary Removes multiple hosts from an asset group at a time.
        
        @description You can call the RemoveHostsFromGroup operation to remove multiple hosts from an asset group at a time. If you no longer need to manage some hosts in an asset group, you can call this operation to remove the hosts from the asset group.
        # [](#qps-)QPS limit
        You can call this API operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: RemoveHostsFromGroupRequest
        @return: RemoveHostsFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_hosts_from_group_with_options(request, runtime)

    async def remove_hosts_from_group_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        """
        @summary Removes multiple hosts from an asset group at a time.
        
        @description You can call the RemoveHostsFromGroup operation to remove multiple hosts from an asset group at a time. If you no longer need to manage some hosts in an asset group, you can call this operation to remove the hosts from the asset group.
        # [](#qps-)QPS limit
        You can call this API operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: RemoveHostsFromGroupRequest
        @return: RemoveHostsFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_hosts_from_group_with_options_async(request, runtime)

    def remove_users_from_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes one or more users from a user group.
        
        @description You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
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
        @summary Removes one or more users from a user group.
        
        @description You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
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
        @summary Removes one or more users from a user group.
        
        @description You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
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
        @summary Removes one or more users from a user group.
        
        @description You can call this operation to remove one or more users from a user group. When users in a user group are transferred to a new position, resign, or are switched to another user group, you can call this operation to remove the users from the current user group at a time.
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
        """
        @summary Renews an O\\&M token for one hour.
        
        @param request: RenewAssetOperationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAssetOperationTokenResponse
        """
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
        """
        @summary Renews an O\\&M token for one hour.
        
        @param request: RenewAssetOperationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewAssetOperationTokenResponse
        """
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
        """
        @summary Renews an O\\&M token for one hour.
        
        @param request: RenewAssetOperationTokenRequest
        @return: RenewAssetOperationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_asset_operation_token_with_options(request, runtime)

    async def renew_asset_operation_token_async(
        self,
        request: yundun_bastionhost_20191209_models.RenewAssetOperationTokenRequest,
    ) -> yundun_bastionhost_20191209_models.RenewAssetOperationTokenResponse:
        """
        @summary Renews an O\\&M token for one hour.
        
        @param request: RenewAssetOperationTokenRequest
        @return: RenewAssetOperationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_asset_operation_token_with_options_async(request, runtime)

    def reset_host_account_credential_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        """
        @summary Deletes the logon credential of a specified host account. The logon credential can be the password or Secure Shell (SSH) private key.
        
        @param request: ResetHostAccountCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetHostAccountCredentialResponse
        """
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
        """
        @summary Deletes the logon credential of a specified host account. The logon credential can be the password or Secure Shell (SSH) private key.
        
        @param request: ResetHostAccountCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetHostAccountCredentialResponse
        """
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
        """
        @summary Deletes the logon credential of a specified host account. The logon credential can be the password or Secure Shell (SSH) private key.
        
        @param request: ResetHostAccountCredentialRequest
        @return: ResetHostAccountCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_host_account_credential_with_options(request, runtime)

    async def reset_host_account_credential_async(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        """
        @summary Deletes the logon credential of a specified host account. The logon credential can be the password or Secure Shell (SSH) private key.
        
        @param request: ResetHostAccountCredentialRequest
        @return: ResetHostAccountCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_host_account_credential_with_options_async(request, runtime)

    def set_policy_access_time_range_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse:
        """
        @summary Configures the logon period limits in a control policy.
        
        @param tmp_req: SetPolicyAccessTimeRangeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyAccessTimeRangeConfigResponse
        """
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
        """
        @summary Configures the logon period limits in a control policy.
        
        @param tmp_req: SetPolicyAccessTimeRangeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyAccessTimeRangeConfigResponse
        """
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
        """
        @summary Configures the logon period limits in a control policy.
        
        @param request: SetPolicyAccessTimeRangeConfigRequest
        @return: SetPolicyAccessTimeRangeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_policy_access_time_range_config_with_options(request, runtime)

    async def set_policy_access_time_range_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAccessTimeRangeConfigResponse:
        """
        @summary Configures the logon period limits in a control policy.
        
        @param request: SetPolicyAccessTimeRangeConfigRequest
        @return: SetPolicyAccessTimeRangeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_access_time_range_config_with_options_async(request, runtime)

    def set_policy_approval_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyApprovalConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse:
        """
        @summary Configures the O&M approval setting in a control policy.
        
        @param tmp_req: SetPolicyApprovalConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyApprovalConfigResponse
        """
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
        """
        @summary Configures the O&M approval setting in a control policy.
        
        @param tmp_req: SetPolicyApprovalConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyApprovalConfigResponse
        """
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
        """
        @summary Configures the O&M approval setting in a control policy.
        
        @param request: SetPolicyApprovalConfigRequest
        @return: SetPolicyApprovalConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_policy_approval_config_with_options(request, runtime)

    async def set_policy_approval_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyApprovalConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyApprovalConfigResponse:
        """
        @summary Configures the O&M approval setting in a control policy.
        
        @param request: SetPolicyApprovalConfigRequest
        @return: SetPolicyApprovalConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_approval_config_with_options_async(request, runtime)

    def set_policy_asset_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAssetScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse:
        """
        @summary Specifies the assets to which a control policy applies.
        
        @param request: SetPolicyAssetScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyAssetScopeResponse
        """
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
        """
        @summary Specifies the assets to which a control policy applies.
        
        @param request: SetPolicyAssetScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyAssetScopeResponse
        """
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
        """
        @summary Specifies the assets to which a control policy applies.
        
        @param request: SetPolicyAssetScopeRequest
        @return: SetPolicyAssetScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_policy_asset_scope_with_options(request, runtime)

    async def set_policy_asset_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyAssetScopeRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyAssetScopeResponse:
        """
        @summary Specifies the assets to which a control policy applies.
        
        @param request: SetPolicyAssetScopeRequest
        @return: SetPolicyAssetScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_asset_scope_with_options_async(request, runtime)

    def set_policy_command_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyCommandConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse:
        """
        @summary Specifies the commands that can or cannot be run by the users or on the assets associated with the policy and the commands that must be reviewed.
        
        @param tmp_req: SetPolicyCommandConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyCommandConfigResponse
        """
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
        """
        @summary Specifies the commands that can or cannot be run by the users or on the assets associated with the policy and the commands that must be reviewed.
        
        @param tmp_req: SetPolicyCommandConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyCommandConfigResponse
        """
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
        """
        @summary Specifies the commands that can or cannot be run by the users or on the assets associated with the policy and the commands that must be reviewed.
        
        @param request: SetPolicyCommandConfigRequest
        @return: SetPolicyCommandConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_policy_command_config_with_options(request, runtime)

    async def set_policy_command_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyCommandConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyCommandConfigResponse:
        """
        @summary Specifies the commands that can or cannot be run by the users or on the assets associated with the policy and the commands that must be reviewed.
        
        @param request: SetPolicyCommandConfigRequest
        @return: SetPolicyCommandConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_command_config_with_options_async(request, runtime)

    def set_policy_ipacl_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyIPAclConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse:
        """
        @summary Configures access control settings in a control policy.
        
        @param tmp_req: SetPolicyIPAclConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyIPAclConfigResponse
        """
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
        """
        @summary Configures access control settings in a control policy.
        
        @param tmp_req: SetPolicyIPAclConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyIPAclConfigResponse
        """
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
        """
        @summary Configures access control settings in a control policy.
        
        @param request: SetPolicyIPAclConfigRequest
        @return: SetPolicyIPAclConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_policy_ipacl_config_with_options(request, runtime)

    async def set_policy_ipacl_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyIPAclConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyIPAclConfigResponse:
        """
        @summary Configures access control settings in a control policy.
        
        @param request: SetPolicyIPAclConfigRequest
        @return: SetPolicyIPAclConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_ipacl_config_with_options_async(request, runtime)

    def set_policy_protocol_config_with_options(
        self,
        tmp_req: yundun_bastionhost_20191209_models.SetPolicyProtocolConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse:
        """
        @summary Modify the protocol control settings in a control policy.
        
        @param tmp_req: SetPolicyProtocolConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyProtocolConfigResponse
        """
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
        """
        @summary Modify the protocol control settings in a control policy.
        
        @param tmp_req: SetPolicyProtocolConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyProtocolConfigResponse
        """
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
        """
        @summary Modify the protocol control settings in a control policy.
        
        @param request: SetPolicyProtocolConfigRequest
        @return: SetPolicyProtocolConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_policy_protocol_config_with_options(request, runtime)

    async def set_policy_protocol_config_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyProtocolConfigRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyProtocolConfigResponse:
        """
        @summary Modify the protocol control settings in a control policy.
        
        @param request: SetPolicyProtocolConfigRequest
        @return: SetPolicyProtocolConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_protocol_config_with_options_async(request, runtime)

    def set_policy_user_scope_with_options(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyUserScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse:
        """
        @summary Specifies the users to whom a control policy applies.
        
        @param request: SetPolicyUserScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyUserScopeResponse
        """
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
        """
        @summary Specifies the users to whom a control policy applies.
        
        @param request: SetPolicyUserScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPolicyUserScopeResponse
        """
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
        """
        @summary Specifies the users to whom a control policy applies.
        
        @param request: SetPolicyUserScopeRequest
        @return: SetPolicyUserScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_policy_user_scope_with_options(request, runtime)

    async def set_policy_user_scope_async(
        self,
        request: yundun_bastionhost_20191209_models.SetPolicyUserScopeRequest,
    ) -> yundun_bastionhost_20191209_models.SetPolicyUserScopeResponse:
        """
        @summary Specifies the users to whom a control policy applies.
        
        @param request: SetPolicyUserScopeRequest
        @return: SetPolicyUserScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_policy_user_scope_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        """
        @summary Enables the specified bastion host.
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_security_group_ids):
            query['ClientSecurityGroupIds'] = request.client_security_group_ids
        if not UtilClient.is_unset(request.enable_portal_private_access):
            query['EnablePortalPrivateAccess'] = request.enable_portal_private_access
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.slave_vswitch_id):
            query['SlaveVswitchId'] = request.slave_vswitch_id
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
        """
        @summary Enables the specified bastion host.
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_security_group_ids):
            query['ClientSecurityGroupIds'] = request.client_security_group_ids
        if not UtilClient.is_unset(request.enable_portal_private_access):
            query['EnablePortalPrivateAccess'] = request.enable_portal_private_access
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.slave_vswitch_id):
            query['SlaveVswitchId'] = request.slave_vswitch_id
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
        """
        @summary Enables the specified bastion host.
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        """
        @summary Enables the specified bastion host.
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to specified bastion hosts.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        """
        @summary Creates and adds tags to specified bastion hosts.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
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
        """
        @summary Creates and adds tags to specified bastion hosts.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        """
        @summary Creates and adds tags to specified bastion hosts.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unlock_users_with_options(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        """
        @summary Unlocks one or more users of a bastion host.
        
        @description After you call the [LockUsers](https://help.aliyun.com/document_detail/204591.html) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
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
        @summary Unlocks one or more users of a bastion host.
        
        @description After you call the [LockUsers](https://help.aliyun.com/document_detail/204591.html) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
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
        @summary Unlocks one or more users of a bastion host.
        
        @description After you call the [LockUsers](https://help.aliyun.com/document_detail/204591.html) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
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
        @summary Unlocks one or more users of a bastion host.
        
        @description After you call the [LockUsers](https://help.aliyun.com/document_detail/204591.html) operation to lock one or more users of a bastion host, you can call this operation to unlock the users. After the users are unlocked, the users can perform O\\&M operations by using the bastion host.
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
        """
        @summary Removes tags from the specified bastion host and deletes the tags at a time.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        """
        @summary Removes tags from the specified bastion host and deletes the tags at a time.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
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
        """
        @summary Removes tags from the specified bastion host and deletes the tags at a time.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        """
        @summary Removes tags from the specified bastion host and deletes the tags at a time.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def verify_instance_adauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse:
        """
        @summary 验证实例AD服务配置
        
        @param request: VerifyInstanceADAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyInstanceADAuthServerResponse
        """
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
        """
        @summary 验证实例AD服务配置
        
        @param request: VerifyInstanceADAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyInstanceADAuthServerResponse
        """
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
        """
        @summary 验证实例AD服务配置
        
        @param request: VerifyInstanceADAuthServerRequest
        @return: VerifyInstanceADAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_instance_adauth_server_with_options(request, runtime)

    async def verify_instance_adauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse:
        """
        @summary 验证实例AD服务配置
        
        @param request: VerifyInstanceADAuthServerRequest
        @return: VerifyInstanceADAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_instance_adauth_server_with_options_async(request, runtime)

    def verify_instance_ldapauth_server_with_options(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse:
        """
        @summary 验证实例LDAP服务配置
        
        @param request: VerifyInstanceLDAPAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyInstanceLDAPAuthServerResponse
        """
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
        """
        @summary 验证实例LDAP服务配置
        
        @param request: VerifyInstanceLDAPAuthServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyInstanceLDAPAuthServerResponse
        """
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
        """
        @summary 验证实例LDAP服务配置
        
        @param request: VerifyInstanceLDAPAuthServerRequest
        @return: VerifyInstanceLDAPAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_instance_ldapauth_server_with_options(request, runtime)

    async def verify_instance_ldapauth_server_async(
        self,
        request: yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerRequest,
    ) -> yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse:
        """
        @summary 验证实例LDAP服务配置
        
        @param request: VerifyInstanceLDAPAuthServerRequest
        @return: VerifyInstanceLDAPAuthServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_instance_ldapauth_server_with_options_async(request, runtime)
