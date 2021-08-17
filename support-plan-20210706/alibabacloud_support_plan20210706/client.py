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

    def list_enterprise_dingtalk_group_customer_members_with_options(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
            self.do_rpcrequest('ListEnterpriseDingtalkGroupCustomerMembers', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_enterprise_dingtalk_group_customer_members_with_options_async(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse(),
            await self.do_rpcrequest_async('ListEnterpriseDingtalkGroupCustomerMembers', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_enterprise_dingtalk_group_customer_members(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_enterprise_dingtalk_group_customer_members_with_options(request, runtime)

    async def list_enterprise_dingtalk_group_customer_members_async(
        self,
        request: support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersRequest,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupCustomerMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_enterprise_dingtalk_group_customer_members_with_options_async(request, runtime)

    def list_enterprise_dingtalk_groups_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
            self.do_rpcrequest('ListEnterpriseDingtalkGroups', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_enterprise_dingtalk_groups_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse(),
            await self.do_rpcrequest_async('ListEnterpriseDingtalkGroups', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_enterprise_dingtalk_groups(self) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_enterprise_dingtalk_groups_with_options(runtime)

    async def list_enterprise_dingtalk_groups_async(self) -> support_plan_20210706_models.ListEnterpriseDingtalkGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_enterprise_dingtalk_groups_with_options_async(runtime)

    def delete_enterprise_dingtalk_group_customer_member_with_options(
        self,
        tmp_req: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse(),
            self.do_rpcrequest('DeleteEnterpriseDingtalkGroupCustomerMember', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_enterprise_dingtalk_group_customer_member_with_options_async(
        self,
        tmp_req: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        UtilClient.validate_model(tmp_req)
        request = support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.mobiles):
            request.mobiles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mobiles, 'Mobiles', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse(),
            await self.do_rpcrequest_async('DeleteEnterpriseDingtalkGroupCustomerMember', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_enterprise_dingtalk_group_customer_member(
        self,
        request: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_enterprise_dingtalk_group_customer_member_with_options(request, runtime)

    async def delete_enterprise_dingtalk_group_customer_member_async(
        self,
        request: support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.DeleteEnterpriseDingtalkGroupCustomerMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_enterprise_dingtalk_group_customer_member_with_options_async(request, runtime)

    def get_enterprise_dingtalk_group_customer_member_with_options(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse(),
            self.do_rpcrequest('GetEnterpriseDingtalkGroupCustomerMember', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_enterprise_dingtalk_group_customer_member_with_options_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse(),
            await self.do_rpcrequest_async('GetEnterpriseDingtalkGroupCustomerMember', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_enterprise_dingtalk_group_customer_member(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_dingtalk_group_customer_member_with_options(request, runtime)

    async def get_enterprise_dingtalk_group_customer_member_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupCustomerMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_dingtalk_group_customer_member_with_options_async(request, runtime)

    def get_enterprise_dingtalk_group_with_options(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse(),
            self.do_rpcrequest('GetEnterpriseDingtalkGroup', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_enterprise_dingtalk_group_with_options_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse(),
            await self.do_rpcrequest_async('GetEnterpriseDingtalkGroup', '2021-07-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_enterprise_dingtalk_group(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_enterprise_dingtalk_group_with_options(request, runtime)

    async def get_enterprise_dingtalk_group_async(
        self,
        request: support_plan_20210706_models.GetEnterpriseDingtalkGroupRequest,
    ) -> support_plan_20210706_models.GetEnterpriseDingtalkGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_enterprise_dingtalk_group_with_options_async(request, runtime)
