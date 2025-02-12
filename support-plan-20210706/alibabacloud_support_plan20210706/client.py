# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_support_plan20210706 import models as support_plan_20210706_models
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
        self._endpoint = self.get_endpoint('support-plan', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_enterprise_group_member_to_task_group_with_options(
        self,
        request: support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse:
        """
        @summary 添加客户服务主群人员进子群
        
        @param request: AddEnterpriseGroupMemberToTaskGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddEnterpriseGroupMemberToTaskGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_order_id):
            query['TaskOrderId'] = request.task_order_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEnterpriseGroupMemberToTaskGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def add_enterprise_group_member_to_task_group_with_options_async(
        self,
        request: support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse:
        """
        @summary 添加客户服务主群人员进子群
        
        @param request: AddEnterpriseGroupMemberToTaskGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddEnterpriseGroupMemberToTaskGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_order_id):
            query['TaskOrderId'] = request.task_order_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEnterpriseGroupMemberToTaskGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_enterprise_group_member_to_task_group(
        self,
        request: support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupRequest,
    ) -> support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse:
        """
        @summary 添加客户服务主群人员进子群
        
        @param request: AddEnterpriseGroupMemberToTaskGroupRequest
        @return: AddEnterpriseGroupMemberToTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_enterprise_group_member_to_task_group_with_options(request, runtime)

    async def add_enterprise_group_member_to_task_group_async(
        self,
        request: support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupRequest,
    ) -> support_plan_20210706_models.AddEnterpriseGroupMemberToTaskGroupResponse:
        """
        @summary 添加客户服务主群人员进子群
        
        @param request: AddEnterpriseGroupMemberToTaskGroupRequest
        @return: AddEnterpriseGroupMemberToTaskGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_enterprise_group_member_to_task_group_with_options_async(request, runtime)

    def create_task_order_with_options(
        self,
        request: support_plan_20210706_models.CreateTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.CreateTaskOrderResponse:
        """
        @summary 创建工单
        
        @param request: CreateTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.is_urgent):
            query['IsUrgent'] = request.is_urgent
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.overview):
            query['Overview'] = request.overview
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.urgent_description):
            query['UrgentDescription'] = request.urgent_description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.CreateTaskOrderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.CreateTaskOrderResponse(),
                self.execute(params, req, runtime)
            )

    async def create_task_order_with_options_async(
        self,
        request: support_plan_20210706_models.CreateTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.CreateTaskOrderResponse:
        """
        @summary 创建工单
        
        @param request: CreateTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.is_urgent):
            query['IsUrgent'] = request.is_urgent
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.overview):
            query['Overview'] = request.overview
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.urgent_description):
            query['UrgentDescription'] = request.urgent_description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.CreateTaskOrderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.CreateTaskOrderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_task_order(
        self,
        request: support_plan_20210706_models.CreateTaskOrderRequest,
    ) -> support_plan_20210706_models.CreateTaskOrderResponse:
        """
        @summary 创建工单
        
        @param request: CreateTaskOrderRequest
        @return: CreateTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_task_order_with_options(request, runtime)

    async def create_task_order_async(
        self,
        request: support_plan_20210706_models.CreateTaskOrderRequest,
    ) -> support_plan_20210706_models.CreateTaskOrderResponse:
        """
        @summary 创建工单
        
        @param request: CreateTaskOrderRequest
        @return: CreateTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_task_order_with_options_async(request, runtime)

    def list_dd_task_order_with_options(
        self,
        request: support_plan_20210706_models.ListDdTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListDdTaskOrderResponse:
        """
        @summary ListDdTaskOrder
        
        @param request: ListDdTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDdTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_real_name):
            query['CreateRealName'] = request.create_real_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_urgent):
            query['IsUrgent'] = request.is_urgent
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDdTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListDdTaskOrderResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListDdTaskOrderResponse(),
                self.execute(params, req, runtime)
            )

    async def list_dd_task_order_with_options_async(
        self,
        request: support_plan_20210706_models.ListDdTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListDdTaskOrderResponse:
        """
        @summary ListDdTaskOrder
        
        @param request: ListDdTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDdTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_real_name):
            query['CreateRealName'] = request.create_real_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_urgent):
            query['IsUrgent'] = request.is_urgent
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDdTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListDdTaskOrderResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListDdTaskOrderResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_dd_task_order(
        self,
        request: support_plan_20210706_models.ListDdTaskOrderRequest,
    ) -> support_plan_20210706_models.ListDdTaskOrderResponse:
        """
        @summary ListDdTaskOrder
        
        @param request: ListDdTaskOrderRequest
        @return: ListDdTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dd_task_order_with_options(request, runtime)

    async def list_dd_task_order_async(
        self,
        request: support_plan_20210706_models.ListDdTaskOrderRequest,
    ) -> support_plan_20210706_models.ListDdTaskOrderResponse:
        """
        @summary ListDdTaskOrder
        
        @param request: ListDdTaskOrderRequest
        @return: ListDdTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dd_task_order_with_options_async(request, runtime)

    def list_enterprise_dingtalk_group_customer_members_with_options(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        """
        @summary 获取钉群中所有客户侧人员信息
        
        @param request: ListEnterpriseDingtalkGroupCustomerMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnterpriseDingtalkGroupCustomerMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnterpriseDingtalkGroupCustomerMembers',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
                self.execute(params, req, runtime)
            )

    async def list_enterprise_dingtalk_group_customer_members_with_options_async(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        """
        @summary 获取钉群中所有客户侧人员信息
        
        @param request: ListEnterpriseDingtalkGroupCustomerMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnterpriseDingtalkGroupCustomerMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnterpriseDingtalkGroupCustomerMembers',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_enterprise_dingtalk_group_customer_members(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        """
        @summary 获取钉群中所有客户侧人员信息
        
        @param request: ListEnterpriseDingtalkGroupCustomerMembersRequest
        @return: ListEnterpriseDingtalkGroupCustomerMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_enterprise_dingtalk_group_customer_members_with_options(request, runtime)

    async def list_enterprise_dingtalk_group_customer_members_async(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        """
        @summary 获取钉群中所有客户侧人员信息
        
        @param request: ListEnterpriseDingtalkGroupCustomerMembersRequest
        @return: ListEnterpriseDingtalkGroupCustomerMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_enterprise_dingtalk_group_customer_members_with_options_async(request, runtime)

    def list_enterprise_dingtalk_groups_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        """
        @summary 查询所有企业钉群成员
        
        @param request: ListEnterpriseDingtalkGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnterpriseDingtalkGroupsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEnterpriseDingtalkGroups',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_enterprise_dingtalk_groups_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        """
        @summary 查询所有企业钉群成员
        
        @param request: ListEnterpriseDingtalkGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnterpriseDingtalkGroupsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEnterpriseDingtalkGroups',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_enterprise_dingtalk_groups(self) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        """
        @summary 查询所有企业钉群成员
        
        @return: ListEnterpriseDingtalkGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_enterprise_dingtalk_groups_with_options(runtime)

    async def list_enterprise_dingtalk_groups_async(self) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        """
        @summary 查询所有企业钉群成员
        
        @return: ListEnterpriseDingtalkGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_enterprise_dingtalk_groups_with_options_async(runtime)

    def list_product_by_group_with_options(
        self,
        request: support_plan_20210706_models.ListProductByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListProductByGroupResponse:
        """
        @summary 获取问题分类
        
        @param request: ListProductByGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductByGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductByGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListProductByGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListProductByGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def list_product_by_group_with_options_async(
        self,
        request: support_plan_20210706_models.ListProductByGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListProductByGroupResponse:
        """
        @summary 获取问题分类
        
        @param request: ListProductByGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductByGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductByGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                support_plan_20210706_models.ListProductByGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                support_plan_20210706_models.ListProductByGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_product_by_group(
        self,
        request: support_plan_20210706_models.ListProductByGroupRequest,
    ) -> support_plan_20210706_models.ListProductByGroupResponse:
        """
        @summary 获取问题分类
        
        @param request: ListProductByGroupRequest
        @return: ListProductByGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_by_group_with_options(request, runtime)

    async def list_product_by_group_async(
        self,
        request: support_plan_20210706_models.ListProductByGroupRequest,
    ) -> support_plan_20210706_models.ListProductByGroupResponse:
        """
        @summary 获取问题分类
        
        @param request: ListProductByGroupRequest
        @return: ListProductByGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_product_by_group_with_options_async(request, runtime)
