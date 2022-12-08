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
        query = {}
        if not UtilClient.is_unset(request.address_list):
            query['AddressList'] = request.address_list
        if not UtilClient.is_unset(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.AddAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddAddressBookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_list):
            query['AddressList'] = request.address_list
        if not UtilClient.is_unset(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.AddControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.members):
            query['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddInstanceMembers',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddInstanceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_instance_members_with_options_async(
        self,
        request: cloudfw_20171207_models.AddInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddInstanceMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.members):
            query['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddInstanceMembers',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.AddInstanceMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def batch_copy_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_vpc_firewall_id):
            query['SourceVpcFirewallId'] = request.source_vpc_firewall_id
        if not UtilClient.is_unset(request.target_vpc_firewall_id):
            query['TargetVpcFirewallId'] = request.target_vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCopyVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_copy_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_vpc_firewall_id):
            query['SourceVpcFirewallId'] = request.source_vpc_firewall_id
        if not UtilClient.is_unset(request.target_vpc_firewall_id):
            query['TargetVpcFirewallId'] = request.target_vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCopyVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_copy_vpc_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_copy_vpc_firewall_control_policy_with_options(request, runtime)

    async def batch_copy_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_copy_vpc_firewall_control_policy_with_options_async(request, runtime)

    def create_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not UtilClient.is_unset(request.vpc_region):
            query['VpcRegion'] = request.vpc_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcFirewallCenConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_cen_configure_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not UtilClient.is_unset(request.vpc_region):
            query['VpcRegion'] = request.vpc_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcFirewallCenConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_cen_configure(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_firewall_cen_configure_with_options(request, runtime)

    async def create_vpc_firewall_cen_configure_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def create_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteAddressBookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.member_uids):
            query['MemberUids'] = request.member_uids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceMembers',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteInstanceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_members_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_uids):
            query['MemberUids'] = request.member_uids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstanceMembers',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteInstanceMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcFirewallCenConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_firewall_cen_configure_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcFirewallCenConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_firewall_cen_configure(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_firewall_cen_configure_with_options(request, runtime)

    async def delete_vpc_firewall_cen_configure_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def delete_vpc_firewall_configure_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcFirewallConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_firewall_configure_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcFirewallConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_firewall_configure(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_firewall_configure_with_options(request, runtime)

    async def delete_vpc_firewall_configure_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_firewall_configure_with_options_async(request, runtime)

    def delete_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.contain_port):
            query['ContainPort'] = request.contain_port
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contain_port):
            query['ContainPort'] = request.contain_port
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.sg_status):
            query['SgStatus'] = request.sg_status
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAssetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.sg_status):
            query['SgStatus'] = request.sg_status
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAssetList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeAssetListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolve',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeDomainResolveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resolve_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolve',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeDomainResolveResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.member_desc):
            query['MemberDesc'] = request.member_desc
        if not UtilClient.is_unset(request.member_display_name):
            query['MemberDisplayName'] = request.member_display_name
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceMembers',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeInstanceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_members_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.member_desc):
            query['MemberDesc'] = request.member_desc
        if not UtilClient.is_unset(request.member_display_name):
            query['MemberDisplayName'] = request.member_display_name
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceMembers',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeInstanceMembersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_invade_event_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInvadeEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInvadeEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assets_ip):
            query['AssetsIP'] = request.assets_ip
        if not UtilClient.is_unset(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not UtilClient.is_unset(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_key):
            query['EventKey'] = request.event_key
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not UtilClient.is_unset(request.is_ignore):
            query['IsIgnore'] = request.is_ignore
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_status_list):
            query['ProcessStatusList'] = request.process_status_list
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvadeEventList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeInvadeEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invade_event_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeInvadeEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInvadeEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assets_ip):
            query['AssetsIP'] = request.assets_ip
        if not UtilClient.is_unset(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not UtilClient.is_unset(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_key):
            query['EventKey'] = request.event_key
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not UtilClient.is_unset(request.is_ignore):
            query['IsIgnore'] = request.is_ignore
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.process_status_list):
            query['ProcessStatusList'] = request.process_status_list
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvadeEventList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeInvadeEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invade_event_list(
        self,
        request: cloudfw_20171207_models.DescribeInvadeEventListRequest,
    ) -> cloudfw_20171207_models.DescribeInvadeEventListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invade_event_list_with_options(request, runtime)

    async def describe_invade_event_list_async(
        self,
        request: cloudfw_20171207_models.DescribeInvadeEventListRequest,
    ) -> cloudfw_20171207_models.DescribeInvadeEventListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invade_event_list_with_options_async(request, runtime)

    def describe_outgoing_destination_ipwith_options(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDestinationIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOutgoingDestinationIP',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_destination_ipwith_options_async(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDestinationIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOutgoingDestinationIP',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_destination_ip(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDestinationIPRequest,
    ) -> cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_outgoing_destination_ipwith_options(request, runtime)

    async def describe_outgoing_destination_ip_async(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDestinationIPRequest,
    ) -> cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_outgoing_destination_ipwith_options_async(request, runtime)

    def describe_outgoing_domain_with_options(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeOutgoingDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOutgoingDomain',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeOutgoingDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_domain_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeOutgoingDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOutgoingDomain',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeOutgoingDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_domain(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDomainRequest,
    ) -> cloudfw_20171207_models.DescribeOutgoingDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_outgoing_domain_with_options(request, runtime)

    async def describe_outgoing_domain_async(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDomainRequest,
    ) -> cloudfw_20171207_models.DescribeOutgoingDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_outgoing_domain_with_options_async(request, runtime)

    def describe_policy_advanced_config_with_options(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyAdvancedConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_advanced_config_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyAdvancedConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyPriorUsed',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyPriorUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_prior_used_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyPriorUsedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyPriorUsed',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribePolicyPriorUsedResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_network_instance_id):
            query['DstNetworkInstanceId'] = request.dst_network_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.no_location):
            query['NoLocation'] = request.no_location
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not UtilClient.is_unset(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.src_network_instance_id):
            query['SrcNetworkInstanceId'] = request.src_network_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vul_level):
            query['VulLevel'] = request.vul_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventGroup',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeRiskEventGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_group_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_network_instance_id):
            query['DstNetworkInstanceId'] = request.dst_network_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.no_location):
            query['NoLocation'] = request.no_location
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not UtilClient.is_unset(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.src_network_instance_id):
            query['SrcNetworkInstanceId'] = request.src_network_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.vul_level):
            query['VulLevel'] = request.vul_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventGroup',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeRiskEventGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_user_asset_iptraffic_info_with_options(
        self,
        request: cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserAssetIPTrafficInfo',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_asset_iptraffic_info_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserAssetIPTrafficInfo',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_asset_iptraffic_info(
        self,
        request: cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoRequest,
    ) -> cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_asset_iptraffic_info_with_options(request, runtime)

    async def describe_user_asset_iptraffic_info_async(
        self,
        request: cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoRequest,
    ) -> cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_asset_iptraffic_info_with_options_async(request, runtime)

    def describe_vpc_firewall_acl_group_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_configure_status):
            query['FirewallConfigureStatus'] = request.firewall_configure_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallAclGroupList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_acl_group_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_configure_status):
            query['FirewallConfigureStatus'] = request.firewall_configure_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallAclGroupList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_vpc_firewall_cen_detail_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallCenDetail',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_cen_detail_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallCenDetail',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_cen_detail(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenDetailRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_cen_detail_with_options(request, runtime)

    async def describe_vpc_firewall_cen_detail_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenDetailRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_cen_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_cen_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not UtilClient.is_unset(request.transit_router_type):
            query['TransitRouterType'] = request.transit_router_type
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallCenList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallCenListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_cen_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not UtilClient.is_unset(request.transit_router_type):
            query['TransitRouterType'] = request.transit_router_type
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallCenList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallCenListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_cen_list(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_cen_list_with_options(request, runtime)

    async def describe_vpc_firewall_cen_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_cen_list_with_options_async(request, runtime)

    def describe_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_vpc_firewall_default_ipsconfig_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallDefaultIPSConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_default_ipsconfig_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallDefaultIPSConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_default_ipsconfig(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_default_ipsconfig_with_options(request, runtime)

    async def describe_vpc_firewall_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_default_ipsconfig_with_options_async(request, runtime)

    def describe_vpc_firewall_detail_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not UtilClient.is_unset(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallDetail',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_detail_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not UtilClient.is_unset(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallDetail',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_detail(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDetailRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_detail_with_options(request, runtime)

    async def describe_vpc_firewall_detail_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDetailRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_sub_type):
            query['ConnectSubType'] = request.connect_sub_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.peer_uid):
            query['PeerUid'] = request.peer_uid
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_sub_type):
            query['ConnectSubType'] = request.connect_sub_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.peer_uid):
            query['PeerUid'] = request.peer_uid
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallList',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_list(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_list_with_options(request, runtime)

    async def describe_vpc_firewall_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_list_with_options_async(request, runtime)

    def describe_vpc_firewall_policy_prior_used_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallPolicyPriorUsed',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_policy_prior_used_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcFirewallPolicyPriorUsed',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.address_list):
            query['AddressList'] = request.address_list
        if not UtilClient.is_unset(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_address_book_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_list):
            query['AddressList'] = request.address_list
        if not UtilClient.is_unset(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.tag_list):
            query['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAddressBook',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.old_order):
            query['OldOrder'] = request.old_order
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyControlPolicyPosition',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyPositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_control_policy_position_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.old_order):
            query['OldOrder'] = request.old_order
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyControlPolicyPosition',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyControlPolicyPositionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.members):
            query['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMemberAttributes',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_member_attributes_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.members):
            query['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceMemberAttributes',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.internet_switch):
            query['InternetSwitch'] = request.internet_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicyAdvancedConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_advanced_config_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_switch):
            query['InternetSwitch'] = request.internet_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicyAdvancedConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallCenConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_cen_configure_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallCenConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_cen_configure(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_cen_configure_with_options(request, runtime)

    async def modify_vpc_firewall_cen_configure_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def modify_vpc_firewall_cen_switch_status_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallCenSwitchStatus',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_cen_switch_status_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallCenSwitchStatus',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_cen_switch_status(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_cen_switch_status_with_options(request, runtime)

    async def modify_vpc_firewall_cen_switch_status_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_cen_switch_status_with_options_async(request, runtime)

    def modify_vpc_firewall_configure_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_configure_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallConfigure',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_configure(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_configure_with_options(request, runtime)

    async def modify_vpc_firewall_configure_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_configure_with_options_async(request, runtime)

    def modify_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dest_port):
            query['DestPort'] = request.dest_port
        if not UtilClient.is_unset(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not UtilClient.is_unset(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not UtilClient.is_unset(request.destination):
            query['Destination'] = request.destination
        if not UtilClient.is_unset(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallControlPolicy',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.old_order):
            query['OldOrder'] = request.old_order
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallControlPolicyPosition',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_control_policy_position_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.old_order):
            query['OldOrder'] = request.old_order
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallControlPolicyPosition',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_vpc_firewall_default_ipsconfig_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not UtilClient.is_unset(request.enable_all_patch):
            query['EnableAllPatch'] = request.enable_all_patch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallDefaultIPSConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_default_ipsconfig_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not UtilClient.is_unset(request.enable_all_patch):
            query['EnableAllPatch'] = request.enable_all_patch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallDefaultIPSConfig',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_default_ipsconfig(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_default_ipsconfig_with_options(request, runtime)

    async def modify_vpc_firewall_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_default_ipsconfig_with_options_async(request, runtime)

    def modify_vpc_firewall_switch_status_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallSwitchStatus',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_switch_status_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallSwitchStatus',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_switch_status(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_switch_status_with_options(request, runtime)

    async def modify_vpc_firewall_switch_status_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_switch_status_with_options_async(request, runtime)

    def put_disable_all_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDisableAllFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableAllFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_disable_all_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDisableAllFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableAllFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_list):
            query['RegionList'] = request.region_list
        if not UtilClient.is_unset(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDisableFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_disable_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutDisableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableFwSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_list):
            query['RegionList'] = request.region_list
        if not UtilClient.is_unset(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDisableFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutDisableFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEnableAllFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableAllFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_enable_all_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutEnableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableAllFwSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEnableAllFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableAllFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_list):
            query['RegionList'] = request.region_list
        if not UtilClient.is_unset(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEnableFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_enable_fw_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.PutEnableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableFwSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_list):
            query['RegionList'] = request.region_list
        if not UtilClient.is_unset(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutEnableFwSwitch',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.PutEnableFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetVpcFirewallRuleHitCount',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_vpc_firewall_rule_hit_count_with_options_async(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetVpcFirewallRuleHitCount',
            version='2017-12-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse(),
            await self.call_api_async(params, req, runtime)
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
