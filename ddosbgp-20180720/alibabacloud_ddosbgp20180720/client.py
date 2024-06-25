# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddosbgp20180720 import models as ddosbgp_20180720_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'ddosbgp.aliyuncs.com',
            'cn-beijing': 'ddosbgp.aliyuncs.com',
            'cn-zhangjiakou': 'ddosbgp.aliyuncs.com',
            'cn-huhehaote': 'ddosbgp.aliyuncs.com',
            'cn-hangzhou': 'ddosbgp.aliyuncs.com',
            'cn-shanghai': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen': 'ddosbgp.aliyuncs.com',
            'ap-northeast-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'ddosbgp.aliyuncs.com',
            'eu-central-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'ddosbgp.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'ddosbgp.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-shanghai-finance-1': 'ddosbgp.aliyuncs.com',
            'cn-north-2-gov-1': 'ddosbgp.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddosbgp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_ip_with_options(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        """
        @summary Adds IP addresses to an Anti-DDoS Origin Enterprise instance.
        
        @param request: AddIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIp',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AddIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ip_with_options_async(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        """
        @summary Adds IP addresses to an Anti-DDoS Origin Enterprise instance.
        
        @param request: AddIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIp',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AddIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ip(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        """
        @summary Adds IP addresses to an Anti-DDoS Origin Enterprise instance.
        
        @param request: AddIpRequest
        @return: AddIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_ip_with_options(request, runtime)

    async def add_ip_async(
        self,
        request: ddosbgp_20180720_models.AddIpRequest,
    ) -> ddosbgp_20180720_models.AddIpResponse:
        """
        @summary Adds IP addresses to an Anti-DDoS Origin Enterprise instance.
        
        @param request: AddIpRequest
        @return: AddIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_ip_with_options_async(request, runtime)

    def add_rd_member_list_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.AddRdMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AddRdMemberListResponse:
        """
        @summary 添加资源目录成员账号列表
        
        @param tmp_req: AddRdMemberListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRdMemberListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.AddRdMemberListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_list):
            request.member_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRdMemberList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AddRdMemberListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_rd_member_list_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.AddRdMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AddRdMemberListResponse:
        """
        @summary 添加资源目录成员账号列表
        
        @param tmp_req: AddRdMemberListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRdMemberListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.AddRdMemberListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_list):
            request.member_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRdMemberList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AddRdMemberListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rd_member_list(
        self,
        request: ddosbgp_20180720_models.AddRdMemberListRequest,
    ) -> ddosbgp_20180720_models.AddRdMemberListResponse:
        """
        @summary 添加资源目录成员账号列表
        
        @param request: AddRdMemberListRequest
        @return: AddRdMemberListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_rd_member_list_with_options(request, runtime)

    async def add_rd_member_list_async(
        self,
        request: ddosbgp_20180720_models.AddRdMemberListRequest,
    ) -> ddosbgp_20180720_models.AddRdMemberListResponse:
        """
        @summary 添加资源目录成员账号列表
        
        @param request: AddRdMemberListRequest
        @return: AddRdMemberListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_rd_member_list_with_options_async(request, runtime)

    def attach_asset_group_to_instance_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.AttachAssetGroupToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AttachAssetGroupToInstanceResponse:
        """
        @summary Associates an asset with an Anti-DDoS Origin instance of a paid edition.
        
        @param tmp_req: AttachAssetGroupToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAssetGroupToInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.AttachAssetGroupToInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.asset_group_list):
            request.asset_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not UtilClient.is_unset(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAssetGroupToInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AttachAssetGroupToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_asset_group_to_instance_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.AttachAssetGroupToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AttachAssetGroupToInstanceResponse:
        """
        @summary Associates an asset with an Anti-DDoS Origin instance of a paid edition.
        
        @param tmp_req: AttachAssetGroupToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAssetGroupToInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.AttachAssetGroupToInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.asset_group_list):
            request.asset_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not UtilClient.is_unset(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAssetGroupToInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AttachAssetGroupToInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_asset_group_to_instance(
        self,
        request: ddosbgp_20180720_models.AttachAssetGroupToInstanceRequest,
    ) -> ddosbgp_20180720_models.AttachAssetGroupToInstanceResponse:
        """
        @summary Associates an asset with an Anti-DDoS Origin instance of a paid edition.
        
        @param request: AttachAssetGroupToInstanceRequest
        @return: AttachAssetGroupToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_asset_group_to_instance_with_options(request, runtime)

    async def attach_asset_group_to_instance_async(
        self,
        request: ddosbgp_20180720_models.AttachAssetGroupToInstanceRequest,
    ) -> ddosbgp_20180720_models.AttachAssetGroupToInstanceResponse:
        """
        @summary Associates an asset with an Anti-DDoS Origin instance of a paid edition.
        
        @param request: AttachAssetGroupToInstanceRequest
        @return: AttachAssetGroupToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_asset_group_to_instance_with_options_async(request, runtime)

    def attach_to_policy_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.AttachToPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AttachToPolicyResponse:
        """
        @summary 策略绑定
        
        @param tmp_req: AttachToPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachToPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.AttachToPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachToPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AttachToPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_to_policy_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.AttachToPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.AttachToPolicyResponse:
        """
        @summary 策略绑定
        
        @param tmp_req: AttachToPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachToPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.AttachToPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachToPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.AttachToPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_to_policy(
        self,
        request: ddosbgp_20180720_models.AttachToPolicyRequest,
    ) -> ddosbgp_20180720_models.AttachToPolicyResponse:
        """
        @summary 策略绑定
        
        @param request: AttachToPolicyRequest
        @return: AttachToPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_to_policy_with_options(request, runtime)

    async def attach_to_policy_async(
        self,
        request: ddosbgp_20180720_models.AttachToPolicyRequest,
    ) -> ddosbgp_20180720_models.AttachToPolicyResponse:
        """
        @summary 策略绑定
        
        @param request: AttachToPolicyRequest
        @return: AttachToPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_to_policy_with_options_async(request, runtime)

    def check_access_log_auth_with_options(
        self,
        request: ddosbgp_20180720_models.CheckAccessLogAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CheckAccessLogAuthResponse:
        """
        @summary Checks whether Anti-DDoS Origin is authorized to access Log Service.
        
        @param request: CheckAccessLogAuthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccessLogAuthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccessLogAuth',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CheckAccessLogAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_access_log_auth_with_options_async(
        self,
        request: ddosbgp_20180720_models.CheckAccessLogAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CheckAccessLogAuthResponse:
        """
        @summary Checks whether Anti-DDoS Origin is authorized to access Log Service.
        
        @param request: CheckAccessLogAuthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccessLogAuthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccessLogAuth',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CheckAccessLogAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_access_log_auth(
        self,
        request: ddosbgp_20180720_models.CheckAccessLogAuthRequest,
    ) -> ddosbgp_20180720_models.CheckAccessLogAuthResponse:
        """
        @summary Checks whether Anti-DDoS Origin is authorized to access Log Service.
        
        @param request: CheckAccessLogAuthRequest
        @return: CheckAccessLogAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_access_log_auth_with_options(request, runtime)

    async def check_access_log_auth_async(
        self,
        request: ddosbgp_20180720_models.CheckAccessLogAuthRequest,
    ) -> ddosbgp_20180720_models.CheckAccessLogAuthResponse:
        """
        @summary Checks whether Anti-DDoS Origin is authorized to access Log Service.
        
        @param request: CheckAccessLogAuthRequest
        @return: CheckAccessLogAuthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_access_log_auth_with_options_async(request, runtime)

    def check_grant_with_options(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        """
        @summary Queries whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        
        @description You can call the CheckGrant operation to query whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckGrantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckGrantResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckGrant',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CheckGrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_grant_with_options_async(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        """
        @summary Queries whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        
        @description You can call the CheckGrant operation to query whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckGrantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckGrantResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckGrant',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CheckGrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_grant(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        """
        @summary Queries whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        
        @description You can call the CheckGrant operation to query whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckGrantRequest
        @return: CheckGrantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_grant_with_options(request, runtime)

    async def check_grant_async(
        self,
        request: ddosbgp_20180720_models.CheckGrantRequest,
    ) -> ddosbgp_20180720_models.CheckGrantResponse:
        """
        @summary Queries whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        
        @description You can call the CheckGrant operation to query whether Anti-DDoS Origin is authorized to obtain information about the assets within the current Alibaba Cloud account.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CheckGrantRequest
        @return: CheckGrantResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_grant_with_options_async(request, runtime)

    def config_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        """
        @param request: ConfigSchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSchedruleOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not UtilClient.is_unset(request.rule_condition_cnt):
            query['RuleConditionCnt'] = request.rule_condition_cnt
        if not UtilClient.is_unset(request.rule_condition_kpps):
            query['RuleConditionKpps'] = request.rule_condition_kpps
        if not UtilClient.is_unset(request.rule_condition_mbps):
            query['RuleConditionMbps'] = request.rule_condition_mbps
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.rule_undo_begin_time):
            query['RuleUndoBeginTime'] = request.rule_undo_begin_time
        if not UtilClient.is_unset(request.rule_undo_end_time):
            query['RuleUndoEndTime'] = request.rule_undo_end_time
        if not UtilClient.is_unset(request.rule_undo_mode):
            query['RuleUndoMode'] = request.rule_undo_mode
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        """
        @param request: ConfigSchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigSchedruleOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not UtilClient.is_unset(request.rule_condition_cnt):
            query['RuleConditionCnt'] = request.rule_condition_cnt
        if not UtilClient.is_unset(request.rule_condition_kpps):
            query['RuleConditionKpps'] = request.rule_condition_kpps
        if not UtilClient.is_unset(request.rule_condition_mbps):
            query['RuleConditionMbps'] = request.rule_condition_mbps
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.rule_undo_begin_time):
            query['RuleUndoBeginTime'] = request.rule_undo_begin_time
        if not UtilClient.is_unset(request.rule_undo_end_time):
            query['RuleUndoEndTime'] = request.rule_undo_end_time
        if not UtilClient.is_unset(request.rule_undo_mode):
            query['RuleUndoMode'] = request.rule_undo_mode
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        """
        @param request: ConfigSchedruleOnDemandRequest
        @return: ConfigSchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_schedrule_on_demand_with_options(request, runtime)

    async def config_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.ConfigSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.ConfigSchedruleOnDemandResponse:
        """
        @param request: ConfigSchedruleOnDemandRequest
        @return: ConfigSchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_schedrule_on_demand_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: ddosbgp_20180720_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CreatePolicyResponse:
        """
        @summary 创建策略
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: ddosbgp_20180720_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CreatePolicyResponse:
        """
        @summary 创建策略
        
        @param request: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: ddosbgp_20180720_models.CreatePolicyRequest,
    ) -> ddosbgp_20180720_models.CreatePolicyResponse:
        """
        @summary 创建策略
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: ddosbgp_20180720_models.CreatePolicyRequest,
    ) -> ddosbgp_20180720_models.CreatePolicyResponse:
        """
        @summary 创建策略
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        """
        @summary Creates a scheduling rule for an on-demand instance.
        
        @param request: CreateSchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchedruleOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not UtilClient.is_unset(request.rule_condition_cnt):
            query['RuleConditionCnt'] = request.rule_condition_cnt
        if not UtilClient.is_unset(request.rule_condition_kpps):
            query['RuleConditionKpps'] = request.rule_condition_kpps
        if not UtilClient.is_unset(request.rule_condition_mbps):
            query['RuleConditionMbps'] = request.rule_condition_mbps
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.rule_undo_begin_time):
            query['RuleUndoBeginTime'] = request.rule_undo_begin_time
        if not UtilClient.is_unset(request.rule_undo_end_time):
            query['RuleUndoEndTime'] = request.rule_undo_end_time
        if not UtilClient.is_unset(request.rule_undo_mode):
            query['RuleUndoMode'] = request.rule_undo_mode
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CreateSchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        """
        @summary Creates a scheduling rule for an on-demand instance.
        
        @param request: CreateSchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchedruleOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not UtilClient.is_unset(request.rule_condition_cnt):
            query['RuleConditionCnt'] = request.rule_condition_cnt
        if not UtilClient.is_unset(request.rule_condition_kpps):
            query['RuleConditionKpps'] = request.rule_condition_kpps
        if not UtilClient.is_unset(request.rule_condition_mbps):
            query['RuleConditionMbps'] = request.rule_condition_mbps
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.rule_switch):
            query['RuleSwitch'] = request.rule_switch
        if not UtilClient.is_unset(request.rule_undo_begin_time):
            query['RuleUndoBeginTime'] = request.rule_undo_begin_time
        if not UtilClient.is_unset(request.rule_undo_end_time):
            query['RuleUndoEndTime'] = request.rule_undo_end_time
        if not UtilClient.is_unset(request.rule_undo_mode):
            query['RuleUndoMode'] = request.rule_undo_mode
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.CreateSchedruleOnDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        """
        @summary Creates a scheduling rule for an on-demand instance.
        
        @param request: CreateSchedruleOnDemandRequest
        @return: CreateSchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_schedrule_on_demand_with_options(request, runtime)

    async def create_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.CreateSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.CreateSchedruleOnDemandResponse:
        """
        @summary Creates a scheduling rule for an on-demand instance.
        
        @param request: CreateSchedruleOnDemandRequest
        @return: CreateSchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_schedrule_on_demand_with_options_async(request, runtime)

    def delete_blackhole_with_options(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        """
        @summary Deactivates blackhole filtering for a protected IP address.
        
        @description You can call the DeleteBlackhole operation to deactivate blackhole filtering for a protected IP address.
        Before you call this operation, you can call the [DescribePackIpList](https://help.aliyun.com/document_detail/118701.html) operation to query the protection status of the IP addresses that are protected by your Anti-DDoS Origin instance. For example, you can query whether blackhole filtering is triggered for an IP address.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteBlackholeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBlackholeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBlackhole',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteBlackholeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_blackhole_with_options_async(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        """
        @summary Deactivates blackhole filtering for a protected IP address.
        
        @description You can call the DeleteBlackhole operation to deactivate blackhole filtering for a protected IP address.
        Before you call this operation, you can call the [DescribePackIpList](https://help.aliyun.com/document_detail/118701.html) operation to query the protection status of the IP addresses that are protected by your Anti-DDoS Origin instance. For example, you can query whether blackhole filtering is triggered for an IP address.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteBlackholeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBlackholeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBlackhole',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteBlackholeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_blackhole(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        """
        @summary Deactivates blackhole filtering for a protected IP address.
        
        @description You can call the DeleteBlackhole operation to deactivate blackhole filtering for a protected IP address.
        Before you call this operation, you can call the [DescribePackIpList](https://help.aliyun.com/document_detail/118701.html) operation to query the protection status of the IP addresses that are protected by your Anti-DDoS Origin instance. For example, you can query whether blackhole filtering is triggered for an IP address.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteBlackholeRequest
        @return: DeleteBlackholeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_blackhole_with_options(request, runtime)

    async def delete_blackhole_async(
        self,
        request: ddosbgp_20180720_models.DeleteBlackholeRequest,
    ) -> ddosbgp_20180720_models.DeleteBlackholeResponse:
        """
        @summary Deactivates blackhole filtering for a protected IP address.
        
        @description You can call the DeleteBlackhole operation to deactivate blackhole filtering for a protected IP address.
        Before you call this operation, you can call the [DescribePackIpList](https://help.aliyun.com/document_detail/118701.html) operation to query the protection status of the IP addresses that are protected by your Anti-DDoS Origin instance. For example, you can query whether blackhole filtering is triggered for an IP address.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteBlackholeRequest
        @return: DeleteBlackholeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_blackhole_with_options_async(request, runtime)

    def delete_ip_with_options(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        """
        @summary Removes specific IP addresses from an Anti-DDoS Origin Enterprise instance.
        
        @description The Anti-DDoS Origin Enterprise instance no longer protects the IP addresses that are removed.
        
        @param request: DeleteIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIp',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_with_options_async(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        """
        @summary Removes specific IP addresses from an Anti-DDoS Origin Enterprise instance.
        
        @description The Anti-DDoS Origin Enterprise instance no longer protects the IP addresses that are removed.
        
        @param request: DeleteIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_list):
            query['IpList'] = request.ip_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIp',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        """
        @summary Removes specific IP addresses from an Anti-DDoS Origin Enterprise instance.
        
        @description The Anti-DDoS Origin Enterprise instance no longer protects the IP addresses that are removed.
        
        @param request: DeleteIpRequest
        @return: DeleteIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ip_with_options(request, runtime)

    async def delete_ip_async(
        self,
        request: ddosbgp_20180720_models.DeleteIpRequest,
    ) -> ddosbgp_20180720_models.DeleteIpResponse:
        """
        @summary Removes specific IP addresses from an Anti-DDoS Origin Enterprise instance.
        
        @description The Anti-DDoS Origin Enterprise instance no longer protects the IP addresses that are removed.
        
        @param request: DeleteIpRequest
        @return: DeleteIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ip_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: ddosbgp_20180720_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: ddosbgp_20180720_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @param request: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: ddosbgp_20180720_models.DeletePolicyRequest,
    ) -> ddosbgp_20180720_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: ddosbgp_20180720_models.DeletePolicyRequest,
    ) -> ddosbgp_20180720_models.DeletePolicyResponse:
        """
        @summary 删除策略
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_rd_member_list_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.DeleteRdMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteRdMemberListResponse:
        """
        @summary 删除资源目录成员账号列表
        
        @param tmp_req: DeleteRdMemberListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRdMemberListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.DeleteRdMemberListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_list):
            request.member_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRdMemberList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteRdMemberListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rd_member_list_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.DeleteRdMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteRdMemberListResponse:
        """
        @summary 删除资源目录成员账号列表
        
        @param tmp_req: DeleteRdMemberListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRdMemberListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.DeleteRdMemberListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_list):
            request.member_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_list, 'MemberList', 'json')
        query = {}
        if not UtilClient.is_unset(request.member_list_shrink):
            query['MemberList'] = request.member_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRdMemberList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteRdMemberListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rd_member_list(
        self,
        request: ddosbgp_20180720_models.DeleteRdMemberListRequest,
    ) -> ddosbgp_20180720_models.DeleteRdMemberListResponse:
        """
        @summary 删除资源目录成员账号列表
        
        @param request: DeleteRdMemberListRequest
        @return: DeleteRdMemberListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rd_member_list_with_options(request, runtime)

    async def delete_rd_member_list_async(
        self,
        request: ddosbgp_20180720_models.DeleteRdMemberListRequest,
    ) -> ddosbgp_20180720_models.DeleteRdMemberListResponse:
        """
        @summary 删除资源目录成员账号列表
        
        @param request: DeleteRdMemberListRequest
        @return: DeleteRdMemberListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rd_member_list_with_options_async(request, runtime)

    def delete_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        """
        @param request: DeleteSchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchedruleOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        """
        @param request: DeleteSchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchedruleOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        """
        @param request: DeleteSchedruleOnDemandRequest
        @return: DeleteSchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_schedrule_on_demand_with_options(request, runtime)

    async def delete_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.DeleteSchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.DeleteSchedruleOnDemandResponse:
        """
        @param request: DeleteSchedruleOnDemandRequest
        @return: DeleteSchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_schedrule_on_demand_with_options_async(request, runtime)

    def describe_asset_group_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeAssetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_group_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetGroup',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeAssetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_group(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupRequest,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupRequest
        @return: DescribeAssetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_group_with_options(request, runtime)

    async def describe_asset_group_async(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupRequest,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupRequest
        @return: DescribeAssetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_group_with_options_async(request, runtime)

    def describe_asset_group_to_instance_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupToInstanceResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetGroupToInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetGroupToInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeAssetGroupToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_group_to_instance_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupToInstanceResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetGroupToInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetGroupToInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeAssetGroupToInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_group_to_instance(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupToInstanceRequest,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupToInstanceResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupToInstanceRequest
        @return: DescribeAssetGroupToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_group_to_instance_with_options(request, runtime)

    async def describe_asset_group_to_instance_async(
        self,
        request: ddosbgp_20180720_models.DescribeAssetGroupToInstanceRequest,
    ) -> ddosbgp_20180720_models.DescribeAssetGroupToInstanceResponse:
        """
        @summary Queries the association between an asset and an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DescribeAssetGroupToInstanceRequest
        @return: DescribeAssetGroupToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_group_to_instance_with_options_async(request, runtime)

    def describe_ddos_event_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        """
        @summary Queries the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribeDdosEvent operation to query the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance by page. The details include the start time, end time, attacked IP address, and status of each event.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosEvent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeDdosEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_event_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        """
        @summary Queries the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribeDdosEvent operation to query the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance by page. The details include the start time, end time, attacked IP address, and status of each event.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosEvent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeDdosEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_event(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        """
        @summary Queries the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribeDdosEvent operation to query the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance by page. The details include the start time, end time, attacked IP address, and status of each event.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventRequest
        @return: DescribeDdosEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_event_with_options(request, runtime)

    async def describe_ddos_event_async(
        self,
        request: ddosbgp_20180720_models.DescribeDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeDdosEventResponse:
        """
        @summary Queries the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribeDdosEvent operation to query the details about the DDoS attack events that occurred on a specific Anti-DDoS Origin instance by page. The details include the start time, end time, attacked IP address, and status of each event.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDdosEventRequest
        @return: DescribeDdosEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_event_with_options_async(request, runtime)

    def describe_ddos_origin_instance_bill_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeDdosOriginInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeDdosOriginInstanceBillResponse:
        """
        @summary 查询账单
        
        @param request: DescribeDdosOriginInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosOriginInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_show_list):
            query['IsShowList'] = request.is_show_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosOriginInstanceBill',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeDdosOriginInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddos_origin_instance_bill_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeDdosOriginInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeDdosOriginInstanceBillResponse:
        """
        @summary 查询账单
        
        @param request: DescribeDdosOriginInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDdosOriginInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_show_list):
            query['IsShowList'] = request.is_show_list
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDdosOriginInstanceBill',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeDdosOriginInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddos_origin_instance_bill(
        self,
        request: ddosbgp_20180720_models.DescribeDdosOriginInstanceBillRequest,
    ) -> ddosbgp_20180720_models.DescribeDdosOriginInstanceBillResponse:
        """
        @summary 查询账单
        
        @param request: DescribeDdosOriginInstanceBillRequest
        @return: DescribeDdosOriginInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddos_origin_instance_bill_with_options(request, runtime)

    async def describe_ddos_origin_instance_bill_async(
        self,
        request: ddosbgp_20180720_models.DescribeDdosOriginInstanceBillRequest,
    ) -> ddosbgp_20180720_models.DescribeDdosOriginInstanceBillResponse:
        """
        @summary 查询账单
        
        @param request: DescribeDdosOriginInstanceBillRequest
        @return: DescribeDdosOriginInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddos_origin_instance_bill_with_options_async(request, runtime)

    def describe_excpetion_count_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        """
        @summary Queries the number of assets that are in an abnormal state and the number of Anti-DDoS
        Origin instances that are about to expire in a specific region. The assets can be
        elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS)
        instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description ## Usage notes
        You can call the DescribeExcpetionCount operation to query the number of assets that are in an abnormal state and the number of Anti-DDoS Origin instances that are about to expire in a specific region. For example, if blackhole filtering is triggered for an IP address, the IP address is in an abnormal state. An instance whose remaining validity period is less than seven days is considered as an instance that is about to expire.
        
        @param request: DescribeExcpetionCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExcpetionCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExcpetionCount',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeExcpetionCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_excpetion_count_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        """
        @summary Queries the number of assets that are in an abnormal state and the number of Anti-DDoS
        Origin instances that are about to expire in a specific region. The assets can be
        elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS)
        instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description ## Usage notes
        You can call the DescribeExcpetionCount operation to query the number of assets that are in an abnormal state and the number of Anti-DDoS Origin instances that are about to expire in a specific region. For example, if blackhole filtering is triggered for an IP address, the IP address is in an abnormal state. An instance whose remaining validity period is less than seven days is considered as an instance that is about to expire.
        
        @param request: DescribeExcpetionCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExcpetionCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExcpetionCount',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeExcpetionCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_excpetion_count(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        """
        @summary Queries the number of assets that are in an abnormal state and the number of Anti-DDoS
        Origin instances that are about to expire in a specific region. The assets can be
        elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS)
        instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description ## Usage notes
        You can call the DescribeExcpetionCount operation to query the number of assets that are in an abnormal state and the number of Anti-DDoS Origin instances that are about to expire in a specific region. For example, if blackhole filtering is triggered for an IP address, the IP address is in an abnormal state. An instance whose remaining validity period is less than seven days is considered as an instance that is about to expire.
        
        @param request: DescribeExcpetionCountRequest
        @return: DescribeExcpetionCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_excpetion_count_with_options(request, runtime)

    async def describe_excpetion_count_async(
        self,
        request: ddosbgp_20180720_models.DescribeExcpetionCountRequest,
    ) -> ddosbgp_20180720_models.DescribeExcpetionCountResponse:
        """
        @summary Queries the number of assets that are in an abnormal state and the number of Anti-DDoS
        Origin instances that are about to expire in a specific region. The assets can be
        elastic IP addresses (EIPs). The assets can also be Elastic Compute Service (ECS)
        instances or Server Load Balancer (SLB) instances that are assigned public IP addresses.
        
        @description ## Usage notes
        You can call the DescribeExcpetionCount operation to query the number of assets that are in an abnormal state and the number of Anti-DDoS Origin instances that are about to expire in a specific region. For example, if blackhole filtering is triggered for an IP address, the IP address is in an abnormal state. An instance whose remaining validity period is less than seven days is considered as an instance that is about to expire.
        
        @param request: DescribeExcpetionCountRequest
        @return: DescribeExcpetionCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_excpetion_count_with_options_async(request, runtime)

    def describe_instance_list_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        """
        @summary Queries the details of all Anti-DDoS Origin instances.
        
        @description You can call the DescribeInstanceList operation to query the details of all Anti-DDoS Origin instances within your Alibaba Cloud account by page. The details include the ID, validity period, and status of each instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.orderdire):
            query['Orderdire'] = request.orderdire
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_list_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        """
        @summary Queries the details of all Anti-DDoS Origin instances.
        
        @description You can call the DescribeInstanceList operation to query the details of all Anti-DDoS Origin instances within your Alibaba Cloud account by page. The details include the ID, validity period, and status of each instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.orderby):
            query['Orderby'] = request.orderby
        if not UtilClient.is_unset(request.orderdire):
            query['Orderdire'] = request.orderdire
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_list(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        """
        @summary Queries the details of all Anti-DDoS Origin instances.
        
        @description You can call the DescribeInstanceList operation to query the details of all Anti-DDoS Origin instances within your Alibaba Cloud account by page. The details include the ID, validity period, and status of each instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceListRequest
        @return: DescribeInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_list_with_options(request, runtime)

    async def describe_instance_list_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceListRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceListResponse:
        """
        @summary Queries the details of all Anti-DDoS Origin instances.
        
        @description You can call the DescribeInstanceList operation to query the details of all Anti-DDoS Origin instances within your Alibaba Cloud account by page. The details include the ID, validity period, and status of each instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceListRequest
        @return: DescribeInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_list_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecs',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeInstanceSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_specs(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @return: DescribeInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: ddosbgp_20180720_models.DescribeInstanceSpecsRequest,
    ) -> ddosbgp_20180720_models.DescribeInstanceSpecsResponse:
        """
        @param request: DescribeInstanceSpecsRequest
        @return: DescribeInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_on_demand_ddos_event_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        """
        @summary Call the DescribeOnDemandDdosEvent operation to query the DDoS events recorded for the IP address of the Anti-DDoS on-demand instance.
        
        @description >  Anti-DDoS Origin API operations are available for only Anti-DDoS Origin Enterprise users.
        
        @param request: DescribeOnDemandDdosEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOnDemandDdosEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnDemandDdosEvent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_on_demand_ddos_event_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        """
        @summary Call the DescribeOnDemandDdosEvent operation to query the DDoS events recorded for the IP address of the Anti-DDoS on-demand instance.
        
        @description >  Anti-DDoS Origin API operations are available for only Anti-DDoS Origin Enterprise users.
        
        @param request: DescribeOnDemandDdosEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOnDemandDdosEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnDemandDdosEvent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_on_demand_ddos_event(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        """
        @summary Call the DescribeOnDemandDdosEvent operation to query the DDoS events recorded for the IP address of the Anti-DDoS on-demand instance.
        
        @description >  Anti-DDoS Origin API operations are available for only Anti-DDoS Origin Enterprise users.
        
        @param request: DescribeOnDemandDdosEventRequest
        @return: DescribeOnDemandDdosEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_ddos_event_with_options(request, runtime)

    async def describe_on_demand_ddos_event_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandDdosEventRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandDdosEventResponse:
        """
        @summary Call the DescribeOnDemandDdosEvent operation to query the DDoS events recorded for the IP address of the Anti-DDoS on-demand instance.
        
        @description >  Anti-DDoS Origin API operations are available for only Anti-DDoS Origin Enterprise users.
        
        @param request: DescribeOnDemandDdosEventRequest
        @return: DescribeOnDemandDdosEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_on_demand_ddos_event_with_options_async(request, runtime)

    def describe_on_demand_instance_status_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        """
        @param request: DescribeOnDemandInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOnDemandInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnDemandInstanceStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_on_demand_instance_status_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        """
        @param request: DescribeOnDemandInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOnDemandInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOnDemandInstanceStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_on_demand_instance_status(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        """
        @param request: DescribeOnDemandInstanceStatusRequest
        @return: DescribeOnDemandInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_on_demand_instance_status_with_options(request, runtime)

    async def describe_on_demand_instance_status_async(
        self,
        request: ddosbgp_20180720_models.DescribeOnDemandInstanceStatusRequest,
    ) -> ddosbgp_20180720_models.DescribeOnDemandInstanceStatusResponse:
        """
        @param request: DescribeOnDemandInstanceStatusRequest
        @return: DescribeOnDemandInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_on_demand_instance_status_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        """
        @summary The number of entries to return on each page.
        
        @description The start time. Operation logs that were generated after this time are queried.*** This value is a UNIX timestamp. Unit: milliseconds.
        
        @param request: DescribeOpEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_dir):
            query['OrderDir'] = request.order_dir
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOpEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        """
        @summary The number of entries to return on each page.
        
        @description The start time. Operation logs that were generated after this time are queried.*** This value is a UNIX timestamp. Unit: milliseconds.
        
        @param request: DescribeOpEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOpEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_dir):
            query['OrderDir'] = request.order_dir
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOpEntities',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeOpEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_op_entities(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        """
        @summary The number of entries to return on each page.
        
        @description The start time. Operation logs that were generated after this time are queried.*** This value is a UNIX timestamp. Unit: milliseconds.
        
        @param request: DescribeOpEntitiesRequest
        @return: DescribeOpEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddosbgp_20180720_models.DescribeOpEntitiesRequest,
    ) -> ddosbgp_20180720_models.DescribeOpEntitiesResponse:
        """
        @summary The number of entries to return on each page.
        
        @description The start time. Operation logs that were generated after this time are queried.*** This value is a UNIX timestamp. Unit: milliseconds.
        
        @param request: DescribeOpEntitiesRequest
        @return: DescribeOpEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_pack_ip_list_with_options(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        """
        @summary Queries the IP addresses that are protected by a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribePackIpList operation to query the details about each IP address that is protected by a specific Anti-DDoS Origin instance by page. The details include the IP address and the type of the cloud asset to which the IP address belongs. The details also include the status of the IP address, such as whether blackhole filtering is triggered for the IP address.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePackIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackIpList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribePackIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pack_ip_list_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        """
        @summary Queries the IP addresses that are protected by a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribePackIpList operation to query the details about each IP address that is protected by a specific Anti-DDoS Origin instance by page. The details include the IP address and the type of the cloud asset to which the IP address belongs. The details also include the status of the IP address, such as whether blackhole filtering is triggered for the IP address.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePackIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackIpListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackIpList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribePackIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pack_ip_list(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        """
        @summary Queries the IP addresses that are protected by a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribePackIpList operation to query the details about each IP address that is protected by a specific Anti-DDoS Origin instance by page. The details include the IP address and the type of the cloud asset to which the IP address belongs. The details also include the status of the IP address, such as whether blackhole filtering is triggered for the IP address.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePackIpListRequest
        @return: DescribePackIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pack_ip_list_with_options(request, runtime)

    async def describe_pack_ip_list_async(
        self,
        request: ddosbgp_20180720_models.DescribePackIpListRequest,
    ) -> ddosbgp_20180720_models.DescribePackIpListResponse:
        """
        @summary Queries the IP addresses that are protected by a specific Anti-DDoS Origin instance.
        
        @description You can call the DescribePackIpList operation to query the details about each IP address that is protected by a specific Anti-DDoS Origin instance by page. The details include the IP address and the type of the cloud asset to which the IP address belongs. The details also include the status of the IP address, such as whether blackhole filtering is triggered for the IP address.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePackIpListRequest
        @return: DescribePackIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pack_ip_list_with_options_async(request, runtime)

    def describe_rd_member_list_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeRdMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRdMemberListResponse:
        """
        @summary 查询资源目录成员账号列表
        
        @param request: DescribeRdMemberListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdMemberListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_directory_id):
            query['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdMemberList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeRdMemberListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rd_member_list_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeRdMemberListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRdMemberListResponse:
        """
        @summary 查询资源目录成员账号列表
        
        @param request: DescribeRdMemberListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdMemberListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_directory_id):
            query['ResourceDirectoryId'] = request.resource_directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdMemberList',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeRdMemberListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rd_member_list(
        self,
        request: ddosbgp_20180720_models.DescribeRdMemberListRequest,
    ) -> ddosbgp_20180720_models.DescribeRdMemberListResponse:
        """
        @summary 查询资源目录成员账号列表
        
        @param request: DescribeRdMemberListRequest
        @return: DescribeRdMemberListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rd_member_list_with_options(request, runtime)

    async def describe_rd_member_list_async(
        self,
        request: ddosbgp_20180720_models.DescribeRdMemberListRequest,
    ) -> ddosbgp_20180720_models.DescribeRdMemberListResponse:
        """
        @summary 查询资源目录成员账号列表
        
        @param request: DescribeRdMemberListRequest
        @return: DescribeRdMemberListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rd_member_list_with_options_async(request, runtime)

    def describe_rd_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRdStatusResponse:
        """
        @summary 查询RD状态
        
        @param request: DescribeRdStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRdStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeRdStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rd_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRdStatusResponse:
        """
        @summary 查询RD状态
        
        @param request: DescribeRdStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRdStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRdStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeRdStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rd_status(self) -> ddosbgp_20180720_models.DescribeRdStatusResponse:
        """
        @summary 查询RD状态
        
        @return: DescribeRdStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rd_status_with_options(runtime)

    async def describe_rd_status_async(self) -> ddosbgp_20180720_models.DescribeRdStatusResponse:
        """
        @summary 查询RD状态
        
        @return: DescribeRdStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rd_status_with_options_async(runtime)

    def describe_regions_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        """
        @summary Queries the regions of cloud assets that are supported by an Anti-DDoS Origin instance.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        """
        @summary Queries the regions of cloud assets that are supported by an Anti-DDoS Origin instance.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        """
        @summary Queries the regions of cloud assets that are supported by an Anti-DDoS Origin instance.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ddosbgp_20180720_models.DescribeRegionsRequest,
    ) -> ddosbgp_20180720_models.DescribeRegionsResponse:
        """
        @summary Queries the regions of cloud assets that are supported by an Anti-DDoS Origin instance.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_traffic_with_options(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        """
        @summary Queries traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        
        @description You can call the DescribeTraffic operation to query traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        >  When you call this operation, you must configure the *InstanceId** parameter to specify the Anti-DDoS Origin instance whose traffic statistics you want to query.
        ## Limits
        You can call this operation once per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTrafficRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.flow_type):
            query['FlowType'] = request.flow_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ipnet):
            query['Ipnet'] = request.ipnet
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraffic',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_with_options_async(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        """
        @summary Queries traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        
        @description You can call the DescribeTraffic operation to query traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        >  When you call this operation, you must configure the *InstanceId** parameter to specify the Anti-DDoS Origin instance whose traffic statistics you want to query.
        ## Limits
        You can call this operation once per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTrafficRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrafficResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.flow_type):
            query['FlowType'] = request.flow_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ipnet):
            query['Ipnet'] = request.ipnet
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraffic',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DescribeTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        """
        @summary Queries traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        
        @description You can call the DescribeTraffic operation to query traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        >  When you call this operation, you must configure the *InstanceId** parameter to specify the Anti-DDoS Origin instance whose traffic statistics you want to query.
        ## Limits
        You can call this operation once per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTrafficRequest
        @return: DescribeTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_with_options(request, runtime)

    async def describe_traffic_async(
        self,
        request: ddosbgp_20180720_models.DescribeTrafficRequest,
    ) -> ddosbgp_20180720_models.DescribeTrafficResponse:
        """
        @summary Queries traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        
        @description You can call the DescribeTraffic operation to query traffic statistics of an Anti-DDoS Origin instance within a specific time period.
        >  When you call this operation, you must configure the *InstanceId** parameter to specify the Anti-DDoS Origin instance whose traffic statistics you want to query.
        ## Limits
        You can call this operation once per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeTrafficRequest
        @return: DescribeTrafficResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_with_options_async(request, runtime)

    def detach_from_policy_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.DetachFromPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DetachFromPolicyResponse:
        """
        @summary 策略解绑
        
        @param tmp_req: DetachFromPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachFromPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.DetachFromPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachFromPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DetachFromPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_from_policy_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.DetachFromPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DetachFromPolicyResponse:
        """
        @summary 策略解绑
        
        @param tmp_req: DetachFromPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachFromPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.DetachFromPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachFromPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DetachFromPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_from_policy(
        self,
        request: ddosbgp_20180720_models.DetachFromPolicyRequest,
    ) -> ddosbgp_20180720_models.DetachFromPolicyResponse:
        """
        @summary 策略解绑
        
        @param request: DetachFromPolicyRequest
        @return: DetachFromPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_from_policy_with_options(request, runtime)

    async def detach_from_policy_async(
        self,
        request: ddosbgp_20180720_models.DetachFromPolicyRequest,
    ) -> ddosbgp_20180720_models.DetachFromPolicyResponse:
        """
        @summary 策略解绑
        
        @param request: DetachFromPolicyRequest
        @return: DetachFromPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_from_policy_with_options_async(request, runtime)

    def dettach_asset_group_to_instance_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.DettachAssetGroupToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DettachAssetGroupToInstanceResponse:
        """
        @summary Dissociates an asset from an Anti-DDoS Origin instance of a paid edition.
        
        @param tmp_req: DettachAssetGroupToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DettachAssetGroupToInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.DettachAssetGroupToInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.asset_group_list):
            request.asset_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not UtilClient.is_unset(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DettachAssetGroupToInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DettachAssetGroupToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def dettach_asset_group_to_instance_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.DettachAssetGroupToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.DettachAssetGroupToInstanceResponse:
        """
        @summary Dissociates an asset from an Anti-DDoS Origin instance of a paid edition.
        
        @param tmp_req: DettachAssetGroupToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DettachAssetGroupToInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.DettachAssetGroupToInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.asset_group_list):
            request.asset_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.asset_group_list, 'AssetGroupList', 'json')
        query = {}
        if not UtilClient.is_unset(request.asset_group_list_shrink):
            query['AssetGroupList'] = request.asset_group_list_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DettachAssetGroupToInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.DettachAssetGroupToInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dettach_asset_group_to_instance(
        self,
        request: ddosbgp_20180720_models.DettachAssetGroupToInstanceRequest,
    ) -> ddosbgp_20180720_models.DettachAssetGroupToInstanceResponse:
        """
        @summary Dissociates an asset from an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DettachAssetGroupToInstanceRequest
        @return: DettachAssetGroupToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.dettach_asset_group_to_instance_with_options(request, runtime)

    async def dettach_asset_group_to_instance_async(
        self,
        request: ddosbgp_20180720_models.DettachAssetGroupToInstanceRequest,
    ) -> ddosbgp_20180720_models.DettachAssetGroupToInstanceResponse:
        """
        @summary Dissociates an asset from an Anti-DDoS Origin instance of a paid edition.
        
        @param request: DettachAssetGroupToInstanceRequest
        @return: DettachAssetGroupToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.dettach_asset_group_to_instance_with_options_async(request, runtime)

    def get_sls_open_status_with_options(
        self,
        request: ddosbgp_20180720_models.GetSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.GetSlsOpenStatusResponse:
        """
        @summary Checks whether Log Service is activated.
        
        @param request: GetSlsOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSlsOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSlsOpenStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.GetSlsOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sls_open_status_with_options_async(
        self,
        request: ddosbgp_20180720_models.GetSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.GetSlsOpenStatusResponse:
        """
        @summary Checks whether Log Service is activated.
        
        @param request: GetSlsOpenStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSlsOpenStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSlsOpenStatus',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.GetSlsOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sls_open_status(
        self,
        request: ddosbgp_20180720_models.GetSlsOpenStatusRequest,
    ) -> ddosbgp_20180720_models.GetSlsOpenStatusResponse:
        """
        @summary Checks whether Log Service is activated.
        
        @param request: GetSlsOpenStatusRequest
        @return: GetSlsOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sls_open_status_with_options(request, runtime)

    async def get_sls_open_status_async(
        self,
        request: ddosbgp_20180720_models.GetSlsOpenStatusRequest,
    ) -> ddosbgp_20180720_models.GetSlsOpenStatusResponse:
        """
        @summary Checks whether Log Service is activated.
        
        @param request: GetSlsOpenStatusRequest
        @return: GetSlsOpenStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sls_open_status_with_options_async(request, runtime)

    def list_opened_access_log_instances_with_options(
        self,
        request: ddosbgp_20180720_models.ListOpenedAccessLogInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListOpenedAccessLogInstancesResponse:
        """
        @summary Queries the Anti-DDoS Origin instances for which log analysis is enabled.
        
        @param request: ListOpenedAccessLogInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOpenedAccessLogInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOpenedAccessLogInstances',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListOpenedAccessLogInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_opened_access_log_instances_with_options_async(
        self,
        request: ddosbgp_20180720_models.ListOpenedAccessLogInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListOpenedAccessLogInstancesResponse:
        """
        @summary Queries the Anti-DDoS Origin instances for which log analysis is enabled.
        
        @param request: ListOpenedAccessLogInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOpenedAccessLogInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOpenedAccessLogInstances',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListOpenedAccessLogInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_opened_access_log_instances(
        self,
        request: ddosbgp_20180720_models.ListOpenedAccessLogInstancesRequest,
    ) -> ddosbgp_20180720_models.ListOpenedAccessLogInstancesResponse:
        """
        @summary Queries the Anti-DDoS Origin instances for which log analysis is enabled.
        
        @param request: ListOpenedAccessLogInstancesRequest
        @return: ListOpenedAccessLogInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_opened_access_log_instances_with_options(request, runtime)

    async def list_opened_access_log_instances_async(
        self,
        request: ddosbgp_20180720_models.ListOpenedAccessLogInstancesRequest,
    ) -> ddosbgp_20180720_models.ListOpenedAccessLogInstancesResponse:
        """
        @summary Queries the Anti-DDoS Origin instances for which log analysis is enabled.
        
        @param request: ListOpenedAccessLogInstancesRequest
        @return: ListOpenedAccessLogInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_opened_access_log_instances_with_options_async(request, runtime)

    def list_policy_with_options(
        self,
        request: ddosbgp_20180720_models.ListPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListPolicyResponse:
        """
        @summary 查询策略
        
        @param request: ListPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_with_options_async(
        self,
        request: ddosbgp_20180720_models.ListPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListPolicyResponse:
        """
        @summary 查询策略
        
        @param request: ListPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy(
        self,
        request: ddosbgp_20180720_models.ListPolicyRequest,
    ) -> ddosbgp_20180720_models.ListPolicyResponse:
        """
        @summary 查询策略
        
        @param request: ListPolicyRequest
        @return: ListPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policy_with_options(request, runtime)

    async def list_policy_async(
        self,
        request: ddosbgp_20180720_models.ListPolicyRequest,
    ) -> ddosbgp_20180720_models.ListPolicyResponse:
        """
        @summary 查询策略
        
        @param request: ListPolicyRequest
        @return: ListPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_with_options_async(request, runtime)

    def list_policy_attachment_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.ListPolicyAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListPolicyAttachmentResponse:
        """
        @summary 查询策略绑定
        
        @param tmp_req: ListPolicyAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyAttachmentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.ListPolicyAttachmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyAttachment',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListPolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_attachment_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.ListPolicyAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListPolicyAttachmentResponse:
        """
        @summary 查询策略绑定
        
        @param tmp_req: ListPolicyAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyAttachmentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.ListPolicyAttachmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_port_protocol_list):
            request.ip_port_protocol_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_port_protocol_list, 'IpPortProtocolList', 'json')
        query = {}
        if not UtilClient.is_unset(request.ip_port_protocol_list_shrink):
            query['IpPortProtocolList'] = request.ip_port_protocol_list_shrink
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyAttachment',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListPolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_attachment(
        self,
        request: ddosbgp_20180720_models.ListPolicyAttachmentRequest,
    ) -> ddosbgp_20180720_models.ListPolicyAttachmentResponse:
        """
        @summary 查询策略绑定
        
        @param request: ListPolicyAttachmentRequest
        @return: ListPolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policy_attachment_with_options(request, runtime)

    async def list_policy_attachment_async(
        self,
        request: ddosbgp_20180720_models.ListPolicyAttachmentRequest,
    ) -> ddosbgp_20180720_models.ListPolicyAttachmentResponse:
        """
        @summary 查询策略绑定
        
        @param request: ListPolicyAttachmentRequest
        @return: ListPolicyAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_attachment_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        """
        @summary Queries all tags.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
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
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        """
        @summary Queries all tags.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
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
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        """
        @summary Queries all tags.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ddosbgp_20180720_models.ListTagKeysRequest,
    ) -> ddosbgp_20180720_models.ListTagKeysResponse:
        """
        @summary Queries all tags.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        """
        @description You can call the ListTagResources operation to query the tags that are added to Anti-DDoS Origin instances at a time.
        
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
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        """
        @description You can call the ListTagResources operation to query the tags that are added to Anti-DDoS Origin instances at a time.
        
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
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        """
        @description You can call the ListTagResources operation to query the tags that are added to Anti-DDoS Origin instances at a time.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ddosbgp_20180720_models.ListTagResourcesRequest,
    ) -> ddosbgp_20180720_models.ListTagResourcesResponse:
        """
        @description You can call the ListTagResources operation to query the tags that are added to Anti-DDoS Origin instances at a time.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_policy_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @param tmp_req: ModifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.ModifyPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ModifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.ModifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @param tmp_req: ModifyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.ModifyPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicy',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ModifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy(
        self,
        request: ddosbgp_20180720_models.ModifyPolicyRequest,
    ) -> ddosbgp_20180720_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @param request: ModifyPolicyRequest
        @return: ModifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_with_options(request, runtime)

    async def modify_policy_async(
        self,
        request: ddosbgp_20180720_models.ModifyPolicyRequest,
    ) -> ddosbgp_20180720_models.ModifyPolicyResponse:
        """
        @summary 修改策略
        
        @param request: ModifyPolicyRequest
        @return: ModifyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_with_options_async(request, runtime)

    def modify_policy_content_with_options(
        self,
        tmp_req: ddosbgp_20180720_models.ModifyPolicyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyPolicyContentResponse:
        """
        @summary 修改策略
        
        @param tmp_req: ModifyPolicyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyContentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.ModifyPolicyContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicyContent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ModifyPolicyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_content_with_options_async(
        self,
        tmp_req: ddosbgp_20180720_models.ModifyPolicyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyPolicyContentResponse:
        """
        @summary 修改策略
        
        @param tmp_req: ModifyPolicyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyContentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ddosbgp_20180720_models.ModifyPolicyContentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicyContent',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ModifyPolicyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_content(
        self,
        request: ddosbgp_20180720_models.ModifyPolicyContentRequest,
    ) -> ddosbgp_20180720_models.ModifyPolicyContentResponse:
        """
        @summary 修改策略
        
        @param request: ModifyPolicyContentRequest
        @return: ModifyPolicyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_content_with_options(request, runtime)

    async def modify_policy_content_async(
        self,
        request: ddosbgp_20180720_models.ModifyPolicyContentRequest,
    ) -> ddosbgp_20180720_models.ModifyPolicyContentResponse:
        """
        @summary 修改策略
        
        @param request: ModifyPolicyContentRequest
        @return: ModifyPolicyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_content_with_options_async(request, runtime)

    def modify_remark_with_options(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        """
        @summary Adds remarks for a specific Anti-DDoS Origin instance.
        
        @description You can call the ModifyRemark operation to add remarks for a single Anti-DDoS Origin instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRemark',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ModifyRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_remark_with_options_async(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        """
        @summary Adds remarks for a specific Anti-DDoS Origin instance.
        
        @description You can call the ModifyRemark operation to add remarks for a single Anti-DDoS Origin instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyRemarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRemarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRemark',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ModifyRemarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_remark(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        """
        @summary Adds remarks for a specific Anti-DDoS Origin instance.
        
        @description You can call the ModifyRemark operation to add remarks for a single Anti-DDoS Origin instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyRemarkRequest
        @return: ModifyRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_remark_with_options(request, runtime)

    async def modify_remark_async(
        self,
        request: ddosbgp_20180720_models.ModifyRemarkRequest,
    ) -> ddosbgp_20180720_models.ModifyRemarkResponse:
        """
        @summary Adds remarks for a specific Anti-DDoS Origin instance.
        
        @description You can call the ModifyRemark operation to add remarks for a single Anti-DDoS Origin instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyRemarkRequest
        @return: ModifyRemarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_remark_with_options_async(request, runtime)

    def query_schedrule_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        """
        @summary Queries the scheduling rule of an on-demand instance.
        
        @param request: QuerySchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySchedruleOnDemandResponse
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
            action='QuerySchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.QuerySchedruleOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_schedrule_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        """
        @summary Queries the scheduling rule of an on-demand instance.
        
        @param request: QuerySchedruleOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySchedruleOnDemandResponse
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
            action='QuerySchedruleOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.QuerySchedruleOnDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_schedrule_on_demand(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        """
        @summary Queries the scheduling rule of an on-demand instance.
        
        @param request: QuerySchedruleOnDemandRequest
        @return: QuerySchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_schedrule_on_demand_with_options(request, runtime)

    async def query_schedrule_on_demand_async(
        self,
        request: ddosbgp_20180720_models.QuerySchedruleOnDemandRequest,
    ) -> ddosbgp_20180720_models.QuerySchedruleOnDemandResponse:
        """
        @summary Queries the scheduling rule of an on-demand instance.
        
        @param request: QuerySchedruleOnDemandRequest
        @return: QuerySchedruleOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_schedrule_on_demand_with_options_async(request, runtime)

    def release_ddos_origin_instance_with_options(
        self,
        request: ddosbgp_20180720_models.ReleaseDdosOriginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ReleaseDdosOriginInstanceResponse:
        """
        @summary 释放原生防护全局实例
        
        @param request: ReleaseDdosOriginInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseDdosOriginInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseDdosOriginInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ReleaseDdosOriginInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_ddos_origin_instance_with_options_async(
        self,
        request: ddosbgp_20180720_models.ReleaseDdosOriginInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.ReleaseDdosOriginInstanceResponse:
        """
        @summary 释放原生防护全局实例
        
        @param request: ReleaseDdosOriginInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseDdosOriginInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseDdosOriginInstance',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.ReleaseDdosOriginInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_ddos_origin_instance(
        self,
        request: ddosbgp_20180720_models.ReleaseDdosOriginInstanceRequest,
    ) -> ddosbgp_20180720_models.ReleaseDdosOriginInstanceResponse:
        """
        @summary 释放原生防护全局实例
        
        @param request: ReleaseDdosOriginInstanceRequest
        @return: ReleaseDdosOriginInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_ddos_origin_instance_with_options(request, runtime)

    async def release_ddos_origin_instance_async(
        self,
        request: ddosbgp_20180720_models.ReleaseDdosOriginInstanceRequest,
    ) -> ddosbgp_20180720_models.ReleaseDdosOriginInstanceResponse:
        """
        @summary 释放原生防护全局实例
        
        @param request: ReleaseDdosOriginInstanceRequest
        @return: ReleaseDdosOriginInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_ddos_origin_instance_with_options_async(request, runtime)

    def set_instance_mode_on_demand_with_options(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        """
        @param request: SetInstanceModeOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstanceModeOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceModeOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.SetInstanceModeOnDemandResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instance_mode_on_demand_with_options_async(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        """
        @param request: SetInstanceModeOnDemandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstanceModeOnDemandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceModeOnDemand',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.SetInstanceModeOnDemandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instance_mode_on_demand(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        """
        @param request: SetInstanceModeOnDemandRequest
        @return: SetInstanceModeOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_instance_mode_on_demand_with_options(request, runtime)

    async def set_instance_mode_on_demand_async(
        self,
        request: ddosbgp_20180720_models.SetInstanceModeOnDemandRequest,
    ) -> ddosbgp_20180720_models.SetInstanceModeOnDemandResponse:
        """
        @param request: SetInstanceModeOnDemandRequest
        @return: SetInstanceModeOnDemandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_mode_on_demand_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        """
        @summary Adds tags to Anti-DDoS Origin instances.
        
        @description You can call the TagResources operation to add tags to Anti-DDoS Origin instances.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        """
        @summary Adds tags to Anti-DDoS Origin instances.
        
        @description You can call the TagResources operation to add tags to Anti-DDoS Origin instances.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        """
        @summary Adds tags to Anti-DDoS Origin instances.
        
        @description You can call the TagResources operation to add tags to Anti-DDoS Origin instances.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ddosbgp_20180720_models.TagResourcesRequest,
    ) -> ddosbgp_20180720_models.TagResourcesResponse:
        """
        @summary Adds tags to Anti-DDoS Origin instances.
        
        @description You can call the TagResources operation to add tags to Anti-DDoS Origin instances.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anti-DDoS Origin Enterprise instances.
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anti-DDoS Origin Enterprise instances.
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version='2018-07-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddosbgp_20180720_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anti-DDoS Origin Enterprise instances.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ddosbgp_20180720_models.UntagResourcesRequest,
    ) -> ddosbgp_20180720_models.UntagResourcesResponse:
        """
        @summary Removes tags from Anti-DDoS Origin Enterprise instances.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
