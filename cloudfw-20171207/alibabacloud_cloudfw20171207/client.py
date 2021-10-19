# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudfw20171207 import models as cloudfw_20171207_models
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
        self._endpoint_map = {
            'ap-southeast-1': 'cloudfw.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou': 'cloudfw.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudfw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_address_book_with_options(
        self,
        request: cloudfw_20171207_models.AddAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddAddressBookResponse(),
            self.do_rpcrequest('AddAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.AddAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddAddressBookResponse(),
            await self.do_rpcrequest_async('AddAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_address_book(
        self,
        request: cloudfw_20171207_models.AddAddressBookRequest,
    ) -> cloudfw_20171207_models.AddAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_address_book_with_options(request, runtime)

    async def add_address_book_async(
        self,
        request: cloudfw_20171207_models.AddAddressBookRequest,
    ) -> cloudfw_20171207_models.AddAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_address_book_with_options_async(request, runtime)

    def add_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.AddControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddControlPolicyResponse(),
            self.do_rpcrequest('AddControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.AddControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddControlPolicyResponse(),
            await self.do_rpcrequest_async('AddControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_control_policy(
        self,
        request: cloudfw_20171207_models.AddControlPolicyRequest,
    ) -> cloudfw_20171207_models.AddControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_control_policy_with_options(request, runtime)

    async def add_control_policy_async(
        self,
        request: cloudfw_20171207_models.AddControlPolicyRequest,
    ) -> cloudfw_20171207_models.AddControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_control_policy_with_options_async(request, runtime)

    def add_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.AddInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddInstanceMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddInstanceMembersResponse(),
            self.do_rpcrequest('AddInstanceMembers', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_instance_members_with_options_async(
        self,
        request: cloudfw_20171207_models.AddInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddInstanceMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddInstanceMembersResponse(),
            await self.do_rpcrequest_async('AddInstanceMembers', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_instance_members(
        self,
        request: cloudfw_20171207_models.AddInstanceMembersRequest,
    ) -> cloudfw_20171207_models.AddInstanceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_instance_members_with_options(request, runtime)

    async def add_instance_members_async(
        self,
        request: cloudfw_20171207_models.AddInstanceMembersRequest,
    ) -> cloudfw_20171207_models.AddInstanceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_instance_members_with_options_async(request, runtime)

    def create_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse(),
            self.do_rpcrequest('CreateVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse(),
            await self.do_rpcrequest_async('CreateVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpc_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_firewall_control_policy_with_options(request, runtime)

    async def create_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_firewall_control_policy_with_options_async(request, runtime)

    def delete_address_book_with_options(
        self,
        request: cloudfw_20171207_models.DeleteAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteAddressBookResponse(),
            self.do_rpcrequest('DeleteAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteAddressBookResponse(),
            await self.do_rpcrequest_async('DeleteAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_address_book(
        self,
        request: cloudfw_20171207_models.DeleteAddressBookRequest,
    ) -> cloudfw_20171207_models.DeleteAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_address_book_with_options(request, runtime)

    async def delete_address_book_async(
        self,
        request: cloudfw_20171207_models.DeleteAddressBookRequest,
    ) -> cloudfw_20171207_models.DeleteAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_address_book_with_options_async(request, runtime)

    def delete_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteControlPolicyResponse(),
            self.do_rpcrequest('DeleteControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteControlPolicyResponse(),
            await self.do_rpcrequest_async('DeleteControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_control_policy(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    async def delete_control_policy_async(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteInstanceMembersResponse(),
            self.do_rpcrequest('DeleteInstanceMembers', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_members_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteInstanceMembersResponse(),
            await self.do_rpcrequest_async('DeleteInstanceMembers', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance_members(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_members_with_options(request, runtime)

    async def delete_instance_members_async(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_members_with_options_async(request, runtime)

    def delete_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse(),
            self.do_rpcrequest('DeleteVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse(),
            await self.do_rpcrequest_async('DeleteVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpc_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_firewall_control_policy_with_options(request, runtime)

    async def delete_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_firewall_control_policy_with_options_async(request, runtime)

    def describe_address_book_with_options(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAddressBookResponse(),
            self.do_rpcrequest('DescribeAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAddressBookResponse(),
            await self.do_rpcrequest_async('DescribeAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_address_book(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_address_book_with_options(request, runtime)

    async def describe_address_book_async(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_address_book_with_options_async(request, runtime)

    def describe_asset_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeAssetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAssetListResponse(),
            self.do_rpcrequest('DescribeAssetList', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_asset_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAssetListResponse(),
            await self.do_rpcrequest_async('DescribeAssetList', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_asset_list(
        self,
        request: cloudfw_20171207_models.DescribeAssetListRequest,
    ) -> cloudfw_20171207_models.DescribeAssetListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_list_with_options(request, runtime)

    async def describe_asset_list_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetListRequest,
    ) -> cloudfw_20171207_models.DescribeAssetListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_list_with_options_async(request, runtime)

    def describe_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeControlPolicyResponse(),
            self.do_rpcrequest('DescribeControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeControlPolicyResponse(),
            await self.do_rpcrequest_async('DescribeControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_control_policy(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_control_policy_with_options(request, runtime)

    async def describe_control_policy_async(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_control_policy_with_options_async(request, runtime)

    def describe_domain_resolve_with_options(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeDomainResolveResponse(),
            self.do_rpcrequest('DescribeDomainResolve', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_resolve_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeDomainResolveResponse(),
            await self.do_rpcrequest_async('DescribeDomainResolve', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_resolve(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resolve_with_options(request, runtime)

    async def describe_domain_resolve_async(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_resolve_with_options_async(request, runtime)

    def describe_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeInstanceMembersResponse(),
            self.do_rpcrequest('DescribeInstanceMembers', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_members_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeInstanceMembersResponse(),
            await self.do_rpcrequest_async('DescribeInstanceMembers', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_members(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_members_with_options(request, runtime)

    async def describe_instance_members_async(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_members_with_options_async(request, runtime)

    def describe_policy_advanced_config_with_options(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse(),
            self.do_rpcrequest('DescribePolicyAdvancedConfig', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_policy_advanced_config_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse(),
            await self.do_rpcrequest_async('DescribePolicyAdvancedConfig', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_policy_advanced_config(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_advanced_config_with_options(request, runtime)

    async def describe_policy_advanced_config_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_advanced_config_with_options_async(request, runtime)

    def describe_policy_prior_used_with_options(
        self,
        request: cloudfw_20171207_models.DescribePolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyPriorUsedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyPriorUsedResponse(),
            self.do_rpcrequest('DescribePolicyPriorUsed', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_policy_prior_used_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyPriorUsedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyPriorUsedResponse(),
            await self.do_rpcrequest_async('DescribePolicyPriorUsed', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_policy_prior_used(
        self,
        request: cloudfw_20171207_models.DescribePolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribePolicyPriorUsedResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_prior_used_with_options(request, runtime)

    async def describe_policy_prior_used_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribePolicyPriorUsedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_prior_used_with_options_async(request, runtime)

    def describe_risk_event_group_with_options(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeRiskEventGroupResponse(),
            self.do_rpcrequest('DescribeRiskEventGroup', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_risk_event_group_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeRiskEventGroupResponse(),
            await self.do_rpcrequest_async('DescribeRiskEventGroup', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_risk_event_group(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_group_with_options(request, runtime)

    async def describe_risk_event_group_async(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_event_group_with_options_async(request, runtime)

    def describe_vpc_firewall_acl_group_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse(),
            self.do_rpcrequest('DescribeVpcFirewallAclGroupList', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpc_firewall_acl_group_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse(),
            await self.do_rpcrequest_async('DescribeVpcFirewallAclGroupList', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_firewall_acl_group_list(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_acl_group_list_with_options(request, runtime)

    async def describe_vpc_firewall_acl_group_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_acl_group_list_with_options_async(request, runtime)

    def describe_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse(),
            self.do_rpcrequest('DescribeVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse(),
            await self.do_rpcrequest_async('DescribeVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_control_policy_with_options(request, runtime)

    async def describe_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_control_policy_with_options_async(request, runtime)

    def describe_vpc_firewall_policy_prior_used_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse(),
            self.do_rpcrequest('DescribeVpcFirewallPolicyPriorUsed', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpc_firewall_policy_prior_used_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse(),
            await self.do_rpcrequest_async('DescribeVpcFirewallPolicyPriorUsed', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_firewall_policy_prior_used(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_policy_prior_used_with_options(request, runtime)

    async def describe_vpc_firewall_policy_prior_used_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_policy_prior_used_with_options_async(request, runtime)

    def modify_address_book_with_options(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyAddressBookResponse(),
            self.do_rpcrequest('ModifyAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyAddressBookResponse(),
            await self.do_rpcrequest_async('ModifyAddressBook', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_address_book(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_address_book_with_options(request, runtime)

    async def modify_address_book_async(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_address_book_with_options_async(request, runtime)

    def modify_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyResponse(),
            self.do_rpcrequest('ModifyControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyResponse(),
            await self.do_rpcrequest_async('ModifyControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_control_policy(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_control_policy_with_options(request, runtime)

    async def modify_control_policy_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_control_policy_with_options_async(request, runtime)

    def modify_control_policy_position_with_options(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyPositionResponse(),
            self.do_rpcrequest('ModifyControlPolicyPosition', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_control_policy_position_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyPositionResponse(),
            await self.do_rpcrequest_async('ModifyControlPolicyPosition', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_control_policy_position(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyControlPolicyPositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_control_policy_position_with_options(request, runtime)

    async def modify_control_policy_position_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyControlPolicyPositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_control_policy_position_with_options_async(request, runtime)

    def modify_instance_member_attributes_with_options(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse(),
            self.do_rpcrequest('ModifyInstanceMemberAttributes', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_member_attributes_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse(),
            await self.do_rpcrequest_async('ModifyInstanceMemberAttributes', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_member_attributes(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_member_attributes_with_options(request, runtime)

    async def modify_instance_member_attributes_async(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_member_attributes_with_options_async(request, runtime)

    def modify_policy_advanced_config_with_options(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse(),
            self.do_rpcrequest('ModifyPolicyAdvancedConfig', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_policy_advanced_config_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse(),
            await self.do_rpcrequest_async('ModifyPolicyAdvancedConfig', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_policy_advanced_config(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_advanced_config_with_options(request, runtime)

    async def modify_policy_advanced_config_async(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_advanced_config_with_options_async(request, runtime)

    def modify_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse(),
            self.do_rpcrequest('ModifyVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse(),
            await self.do_rpcrequest_async('ModifyVpcFirewallControlPolicy', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpc_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_control_policy_with_options(request, runtime)

    async def modify_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_control_policy_with_options_async(request, runtime)

    def modify_vpc_firewall_control_policy_position_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse(),
            self.do_rpcrequest('ModifyVpcFirewallControlPolicyPosition', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpc_firewall_control_policy_position_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse(),
            await self.do_rpcrequest_async('ModifyVpcFirewallControlPolicyPosition', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpc_firewall_control_policy_position(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_control_policy_position_with_options(request, runtime)

    async def modify_vpc_firewall_control_policy_position_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_control_policy_position_with_options_async(request, runtime)

    def put_disable_all_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableAllFwSwitchResponse(),
            self.do_rpcrequest('PutDisableAllFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_disable_all_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableAllFwSwitchResponse(),
            await self.do_rpcrequest_async('PutDisableAllFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_disable_all_fw_switch(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_disable_all_fw_switch_with_options(request, runtime)

    async def put_disable_all_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_disable_all_fw_switch_with_options_async(request, runtime)

    def put_disable_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutDisableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableFwSwitchResponse(),
            self.do_rpcrequest('PutDisableFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_disable_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutDisableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableFwSwitchResponse(),
            await self.do_rpcrequest_async('PutDisableFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_disable_fw_switch(
        self,
        request: cloudfw_20171207_models.PutDisableFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutDisableFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_disable_fw_switch_with_options(request, runtime)

    async def put_disable_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutDisableFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutDisableFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_disable_fw_switch_with_options_async(request, runtime)

    def put_enable_all_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutEnableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableAllFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableAllFwSwitchResponse(),
            self.do_rpcrequest('PutEnableAllFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_enable_all_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutEnableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableAllFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableAllFwSwitchResponse(),
            await self.do_rpcrequest_async('PutEnableAllFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_enable_all_fw_switch(
        self,
        request: cloudfw_20171207_models.PutEnableAllFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutEnableAllFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_enable_all_fw_switch_with_options(request, runtime)

    async def put_enable_all_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutEnableAllFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutEnableAllFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_enable_all_fw_switch_with_options_async(request, runtime)

    def put_enable_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutEnableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableFwSwitchResponse(),
            self.do_rpcrequest('PutEnableFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_enable_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutEnableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableFwSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableFwSwitchResponse(),
            await self.do_rpcrequest_async('PutEnableFwSwitch', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_enable_fw_switch(
        self,
        request: cloudfw_20171207_models.PutEnableFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutEnableFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_enable_fw_switch_with_options(request, runtime)

    async def put_enable_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutEnableFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutEnableFwSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_enable_fw_switch_with_options_async(request, runtime)

    def reset_vpc_firewall_rule_hit_count_with_options(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse(),
            self.do_rpcrequest('ResetVpcFirewallRuleHitCount', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_vpc_firewall_rule_hit_count_with_options_async(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse(),
            await self.do_rpcrequest_async('ResetVpcFirewallRuleHitCount', '2017-12-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_vpc_firewall_rule_hit_count(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_vpc_firewall_rule_hit_count_with_options(request, runtime)

    async def reset_vpc_firewall_rule_hit_count_async(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_vpc_firewall_rule_hit_count_with_options_async(request, runtime)
