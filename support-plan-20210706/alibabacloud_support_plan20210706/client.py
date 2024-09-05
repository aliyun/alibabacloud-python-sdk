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

    def close_task_order_with_options(
        self,
        request: support_plan_20210706_models.CloseTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.CloseTaskOrderResponse:
        """
        @summary 关闭任务单
        
        @param request: CloseTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.CloseTaskOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_task_order_with_options_async(
        self,
        request: support_plan_20210706_models.CloseTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.CloseTaskOrderResponse:
        """
        @summary 关闭任务单
        
        @param request: CloseTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.CloseTaskOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_task_order(
        self,
        request: support_plan_20210706_models.CloseTaskOrderRequest,
    ) -> support_plan_20210706_models.CloseTaskOrderResponse:
        """
        @summary 关闭任务单
        
        @param request: CloseTaskOrderRequest
        @return: CloseTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_task_order_with_options(request, runtime)

    async def close_task_order_async(
        self,
        request: support_plan_20210706_models.CloseTaskOrderRequest,
    ) -> support_plan_20210706_models.CloseTaskOrderResponse:
        """
        @summary 关闭任务单
        
        @param request: CloseTaskOrderRequest
        @return: CloseTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_task_order_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.customer_real_name):
            query['CustomerRealName'] = request.customer_real_name
        if not UtilClient.is_unset(request.customer_user_id):
            query['CustomerUserId'] = request.customer_user_id
        if not UtilClient.is_unset(request.important_description):
            query['ImportantDescription'] = request.important_description
        if not UtilClient.is_unset(request.is_important):
            query['IsImportant'] = request.is_important
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.product_type_name):
            query['ProductTypeName'] = request.product_type_name
        if not UtilClient.is_unset(request.task_title):
            query['TaskTitle'] = request.task_title
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
        return TeaCore.from_map(
            support_plan_20210706_models.CreateTaskOrderResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.customer_real_name):
            query['CustomerRealName'] = request.customer_real_name
        if not UtilClient.is_unset(request.customer_user_id):
            query['CustomerUserId'] = request.customer_user_id
        if not UtilClient.is_unset(request.important_description):
            query['ImportantDescription'] = request.important_description
        if not UtilClient.is_unset(request.is_important):
            query['IsImportant'] = request.is_important
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.product_type_name):
            query['ProductTypeName'] = request.product_type_name
        if not UtilClient.is_unset(request.task_title):
            query['TaskTitle'] = request.task_title
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
        return TeaCore.from_map(
            support_plan_20210706_models.CreateTaskOrderResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_task_order_by_event_report_with_options(
        self,
        tmp_req: support_plan_20210706_models.CreateTaskOrderByEventReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.CreateTaskOrderByEventReportResponse:
        """
        @summary 告警建单
        
        @param tmp_req: CreateTaskOrderByEventReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskOrderByEventReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.CreateTaskOrderByEventReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.event_body):
            request.event_body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_body, 'EventBody', 'json')
        if not UtilClient.is_unset(tmp_req.extinfo):
            request.extinfo_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extinfo, 'Extinfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.business):
            query['Business'] = request.business
        if not UtilClient.is_unset(request.create_real_name):
            query['CreateRealName'] = request.create_real_name
        if not UtilClient.is_unset(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.event_body_shrink):
            query['EventBody'] = request.event_body_shrink
        if not UtilClient.is_unset(request.extinfo_shrink):
            query['Extinfo'] = request.extinfo_shrink
        if not UtilClient.is_unset(request.important_desc):
            query['ImportantDesc'] = request.important_desc
        if not UtilClient.is_unset(request.join_child_group_user_ids):
            query['JoinChildGroupUserIds'] = request.join_child_group_user_ids
        if not UtilClient.is_unset(request.monitor_congregation):
            query['MonitorCongregation'] = request.monitor_congregation
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskOrderByEventReport',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.CreateTaskOrderByEventReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_order_by_event_report_with_options_async(
        self,
        tmp_req: support_plan_20210706_models.CreateTaskOrderByEventReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.CreateTaskOrderByEventReportResponse:
        """
        @summary 告警建单
        
        @param tmp_req: CreateTaskOrderByEventReportRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskOrderByEventReportResponse
        """
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.CreateTaskOrderByEventReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.event_body):
            request.event_body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_body, 'EventBody', 'json')
        if not UtilClient.is_unset(tmp_req.extinfo):
            request.extinfo_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extinfo, 'Extinfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.business):
            query['Business'] = request.business
        if not UtilClient.is_unset(request.create_real_name):
            query['CreateRealName'] = request.create_real_name
        if not UtilClient.is_unset(request.create_user_id):
            query['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.event_body_shrink):
            query['EventBody'] = request.event_body_shrink
        if not UtilClient.is_unset(request.extinfo_shrink):
            query['Extinfo'] = request.extinfo_shrink
        if not UtilClient.is_unset(request.important_desc):
            query['ImportantDesc'] = request.important_desc
        if not UtilClient.is_unset(request.join_child_group_user_ids):
            query['JoinChildGroupUserIds'] = request.join_child_group_user_ids
        if not UtilClient.is_unset(request.monitor_congregation):
            query['MonitorCongregation'] = request.monitor_congregation
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskOrderByEventReport',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.CreateTaskOrderByEventReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_order_by_event_report(
        self,
        request: support_plan_20210706_models.CreateTaskOrderByEventReportRequest,
    ) -> support_plan_20210706_models.CreateTaskOrderByEventReportResponse:
        """
        @summary 告警建单
        
        @param request: CreateTaskOrderByEventReportRequest
        @return: CreateTaskOrderByEventReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_task_order_by_event_report_with_options(request, runtime)

    async def create_task_order_by_event_report_async(
        self,
        request: support_plan_20210706_models.CreateTaskOrderByEventReportRequest,
    ) -> support_plan_20210706_models.CreateTaskOrderByEventReportResponse:
        """
        @summary 告警建单
        
        @param request: CreateTaskOrderByEventReportRequest
        @return: CreateTaskOrderByEventReportResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_task_order_by_event_report_with_options_async(request, runtime)

    def delete_enterprise_dingtalk_group_customer_member_with_options(
        self,
        tmp_req: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 删除企业钉群客户侧成员
        
        @param tmp_req: DeleteEnterpriseDingtalkGroupCustomerMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnterpriseDingtalkGroupCustomerMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        body = {}
        if not UtilClient.is_unset(request.mobiles_shrink):
            body['Mobiles'] = request.mobiles_shrink
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseDingtalkGroupCustomerMember',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_dingtalk_group_customer_member_with_options_async(
        self,
        tmp_req: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 删除企业钉群客户侧成员
        
        @param tmp_req: DeleteEnterpriseDingtalkGroupCustomerMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEnterpriseDingtalkGroupCustomerMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        body = {}
        if not UtilClient.is_unset(request.mobiles_shrink):
            body['Mobiles'] = request.mobiles_shrink
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEnterpriseDingtalkGroupCustomerMember',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise_dingtalk_group_customer_member(
        self,
        request: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 删除企业钉群客户侧成员
        
        @param request: DeleteEnterpriseDingtalkGroupCustomerMemberRequest
        @return: DeleteEnterpriseDingtalkGroupCustomerMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_enterprise_dingtalk_group_customer_member_with_options(request, runtime)

    async def delete_enterprise_dingtalk_group_customer_member_async(
        self,
        request: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 删除企业钉群客户侧成员
        
        @param request: DeleteEnterpriseDingtalkGroupCustomerMemberRequest
        @return: DeleteEnterpriseDingtalkGroupCustomerMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_enterprise_dingtalk_group_customer_member_with_options_async(request, runtime)

    def get_enterprise_dingtalk_group_with_options(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        """
        @summary 查询企业钉群
        
        @param request: GetEnterpriseDingtalkGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseDingtalkGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDingtalkGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_dingtalk_group_with_options_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        """
        @summary 查询企业钉群
        
        @param request: GetEnterpriseDingtalkGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseDingtalkGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDingtalkGroup',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_dingtalk_group(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        """
        @summary 查询企业钉群
        
        @param request: GetEnterpriseDingtalkGroupRequest
        @return: GetEnterpriseDingtalkGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_dingtalk_group_with_options(request, runtime)

    async def get_enterprise_dingtalk_group_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        """
        @summary 查询企业钉群
        
        @param request: GetEnterpriseDingtalkGroupRequest
        @return: GetEnterpriseDingtalkGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_dingtalk_group_with_options_async(request, runtime)

    def get_enterprise_dingtalk_group_customer_member_with_options(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 获取企业钉群客户侧成员
        
        @param request: GetEnterpriseDingtalkGroupCustomerMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseDingtalkGroupCustomerMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDingtalkGroupCustomerMember',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_dingtalk_group_customer_member_with_options_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 获取企业钉群客户侧成员
        
        @param request: GetEnterpriseDingtalkGroupCustomerMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnterpriseDingtalkGroupCustomerMemberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEnterpriseDingtalkGroupCustomerMember',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_dingtalk_group_customer_member(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 获取企业钉群客户侧成员
        
        @param request: GetEnterpriseDingtalkGroupCustomerMemberRequest
        @return: GetEnterpriseDingtalkGroupCustomerMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_dingtalk_group_customer_member_with_options(request, runtime)

    async def get_enterprise_dingtalk_group_customer_member_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        """
        @summary 获取企业钉群客户侧成员
        
        @param request: GetEnterpriseDingtalkGroupCustomerMemberRequest
        @return: GetEnterpriseDingtalkGroupCustomerMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_dingtalk_group_customer_member_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            query['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            query['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.create_real_name):
            query['CreateRealName'] = request.create_real_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListDdTaskOrderResponse(),
            self.call_api(params, req, runtime)
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
        if not UtilClient.is_unset(request.caller_parent_id):
            query['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            query['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            query['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.create_real_name):
            query['CreateRealName'] = request.create_real_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListDdTaskOrderResponse(),
            await self.call_api_async(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
            self.call_api(params, req, runtime)
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
        body = {}
        if not UtilClient.is_unset(request.open_group_id):
            body['OpenGroupId'] = request.open_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
            await self.call_api_async(params, req, runtime)
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
            self.call_api(params, req, runtime)
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListProductByGroupResponse(),
            self.call_api(params, req, runtime)
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
        return TeaCore.from_map(
            support_plan_20210706_models.ListProductByGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_task_info_with_options(
        self,
        request: support_plan_20210706_models.QueryTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.QueryTaskInfoResponse:
        """
        @summary 获取工单状态
        
        @param request: QueryTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskInfo',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.QueryTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_info_with_options_async(
        self,
        request: support_plan_20210706_models.QueryTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.QueryTaskInfoResponse:
        """
        @summary 获取工单状态
        
        @param request: QueryTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTaskInfo',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.QueryTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_info(
        self,
        request: support_plan_20210706_models.QueryTaskInfoRequest,
    ) -> support_plan_20210706_models.QueryTaskInfoResponse:
        """
        @summary 获取工单状态
        
        @param request: QueryTaskInfoRequest
        @return: QueryTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_task_info_with_options(request, runtime)

    async def query_task_info_async(
        self,
        request: support_plan_20210706_models.QueryTaskInfoRequest,
    ) -> support_plan_20210706_models.QueryTaskInfoResponse:
        """
        @summary 获取工单状态
        
        @param request: QueryTaskInfoRequest
        @return: QueryTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_task_info_with_options_async(request, runtime)

    def reply_message_api_with_options(
        self,
        request: support_plan_20210706_models.ReplyMessageApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ReplyMessageApiResponse:
        """
        @summary 客户回复消息
        
        @param request: ReplyMessageApiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplyMessageApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.msg_content):
            query['MsgContent'] = request.msg_content
        if not UtilClient.is_unset(request.msg_type):
            query['MsgType'] = request.msg_type
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplyMessageApi',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ReplyMessageApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def reply_message_api_with_options_async(
        self,
        request: support_plan_20210706_models.ReplyMessageApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ReplyMessageApiResponse:
        """
        @summary 客户回复消息
        
        @param request: ReplyMessageApiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReplyMessageApiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.msg_content):
            query['MsgContent'] = request.msg_content
        if not UtilClient.is_unset(request.msg_type):
            query['MsgType'] = request.msg_type
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplyMessageApi',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ReplyMessageApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reply_message_api(
        self,
        request: support_plan_20210706_models.ReplyMessageApiRequest,
    ) -> support_plan_20210706_models.ReplyMessageApiResponse:
        """
        @summary 客户回复消息
        
        @param request: ReplyMessageApiRequest
        @return: ReplyMessageApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reply_message_api_with_options(request, runtime)

    async def reply_message_api_async(
        self,
        request: support_plan_20210706_models.ReplyMessageApiRequest,
    ) -> support_plan_20210706_models.ReplyMessageApiResponse:
        """
        @summary 客户回复消息
        
        @param request: ReplyMessageApiRequest
        @return: ReplyMessageApiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reply_message_api_with_options_async(request, runtime)

    def rest_open_task_order_with_options(
        self,
        request: support_plan_20210706_models.RestOpenTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.RestOpenTaskOrderResponse:
        """
        @summary 重开任务单(待客户确认状态)
        
        @param request: RestOpenTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestOpenTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.reset_content):
            query['ResetContent'] = request.reset_content
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestOpenTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.RestOpenTaskOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def rest_open_task_order_with_options_async(
        self,
        request: support_plan_20210706_models.RestOpenTaskOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.RestOpenTaskOrderResponse:
        """
        @summary 重开任务单(待客户确认状态)
        
        @param request: RestOpenTaskOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestOpenTaskOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.open_group_id):
            query['OpenGroupId'] = request.open_group_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.reset_content):
            query['ResetContent'] = request.reset_content
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestOpenTaskOrder',
            version='2021-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            support_plan_20210706_models.RestOpenTaskOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rest_open_task_order(
        self,
        request: support_plan_20210706_models.RestOpenTaskOrderRequest,
    ) -> support_plan_20210706_models.RestOpenTaskOrderResponse:
        """
        @summary 重开任务单(待客户确认状态)
        
        @param request: RestOpenTaskOrderRequest
        @return: RestOpenTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rest_open_task_order_with_options(request, runtime)

    async def rest_open_task_order_async(
        self,
        request: support_plan_20210706_models.RestOpenTaskOrderRequest,
    ) -> support_plan_20210706_models.RestOpenTaskOrderResponse:
        """
        @summary 重开任务单(待客户确认状态)
        
        @param request: RestOpenTaskOrderRequest
        @return: RestOpenTaskOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rest_open_task_order_with_options_async(request, runtime)
