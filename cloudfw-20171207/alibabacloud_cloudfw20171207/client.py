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
        """
        You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAddressBookResponse
        """
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
        """
        You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAddressBookResponse
        """
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
        """
        You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAddressBookRequest
        @return: AddAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_address_book_with_options(request, runtime)

    async def add_address_book_async(
        self,
        request: cloudfw_20171207_models.AddAddressBookRequest,
    ) -> cloudfw_20171207_models.AddAddressBookResponse:
        """
        You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddAddressBookRequest
        @return: AddAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_address_book_with_options_async(request, runtime)

    def add_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.AddControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddControlPolicyResponse:
        """
        You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddControlPolicyRequest
        @return: AddControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_control_policy_with_options(request, runtime)

    async def add_control_policy_async(
        self,
        request: cloudfw_20171207_models.AddControlPolicyRequest,
    ) -> cloudfw_20171207_models.AddControlPolicyResponse:
        """
        You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddControlPolicyRequest
        @return: AddControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_control_policy_with_options_async(request, runtime)

    def add_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.AddInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.AddInstanceMembersResponse:
        """
        You can call the AddInstanceMembers operation to add members to Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddInstanceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddInstanceMembersResponse
        """
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
        """
        You can call the AddInstanceMembers operation to add members to Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddInstanceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddInstanceMembersResponse
        """
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
        """
        You can call the AddInstanceMembers operation to add members to Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddInstanceMembersRequest
        @return: AddInstanceMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_instance_members_with_options(request, runtime)

    async def add_instance_members_async(
        self,
        request: cloudfw_20171207_models.AddInstanceMembersRequest,
    ) -> cloudfw_20171207_models.AddInstanceMembersResponse:
        """
        You can call the AddInstanceMembers operation to add members to Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: AddInstanceMembersRequest
        @return: AddInstanceMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_instance_members_with_options_async(request, runtime)

    def batch_copy_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse:
        """
        You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
        Before you call this operation, we recommend that you back up access control policies. For more information about how to back up an access control policy, see [Back up an access control policy](https://www.alibabacloud.com/help/en/cloud-firewall/latest/back-up-and-roll-back-an-access-control-policy).
        After you call this operation, all the access control policies in the policy group of the destination VPC firewall are replaced.
        The policy groups of the source VPC firewall and the destination VPC firewall must belong to the same Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. When the number of calls to this operation per second exceeds the limit, throttling is triggered. Throttling may affect your business. We recommend that you take note of the limit on this operation.
        
        @param request: BatchCopyVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCopyVpcFirewallControlPolicyResponse
        """
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
        """
        You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
        Before you call this operation, we recommend that you back up access control policies. For more information about how to back up an access control policy, see [Back up an access control policy](https://www.alibabacloud.com/help/en/cloud-firewall/latest/back-up-and-roll-back-an-access-control-policy).
        After you call this operation, all the access control policies in the policy group of the destination VPC firewall are replaced.
        The policy groups of the source VPC firewall and the destination VPC firewall must belong to the same Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. When the number of calls to this operation per second exceeds the limit, throttling is triggered. Throttling may affect your business. We recommend that you take note of the limit on this operation.
        
        @param request: BatchCopyVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCopyVpcFirewallControlPolicyResponse
        """
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
        """
        You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
        Before you call this operation, we recommend that you back up access control policies. For more information about how to back up an access control policy, see [Back up an access control policy](https://www.alibabacloud.com/help/en/cloud-firewall/latest/back-up-and-roll-back-an-access-control-policy).
        After you call this operation, all the access control policies in the policy group of the destination VPC firewall are replaced.
        The policy groups of the source VPC firewall and the destination VPC firewall must belong to the same Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. When the number of calls to this operation per second exceeds the limit, throttling is triggered. Throttling may affect your business. We recommend that you take note of the limit on this operation.
        
        @param request: BatchCopyVpcFirewallControlPolicyRequest
        @return: BatchCopyVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_copy_vpc_firewall_control_policy_with_options(request, runtime)

    async def batch_copy_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.BatchCopyVpcFirewallControlPolicyResponse:
        """
        You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
        Before you call this operation, we recommend that you back up access control policies. For more information about how to back up an access control policy, see [Back up an access control policy](https://www.alibabacloud.com/help/en/cloud-firewall/latest/back-up-and-roll-back-an-access-control-policy).
        After you call this operation, all the access control policies in the policy group of the destination VPC firewall are replaced.
        The policy groups of the source VPC firewall and the destination VPC firewall must belong to the same Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. When the number of calls to this operation per second exceeds the limit, throttling is triggered. Throttling may affect your business. We recommend that you take note of the limit on this operation.
        
        @param request: BatchCopyVpcFirewallControlPolicyRequest
        @return: BatchCopyVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_copy_vpc_firewall_control_policy_with_options_async(request, runtime)

    def create_nat_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.CreateNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateNatFirewallControlPolicyResponse:
        """
        You can use this operation to create an access control policy to allow, deny, or monitor traffic that passes through a NAT firewall.
        
        @param request: CreateNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNatFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNatFirewallControlPolicy',
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
            cloudfw_20171207_models.CreateNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nat_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateNatFirewallControlPolicyResponse:
        """
        You can use this operation to create an access control policy to allow, deny, or monitor traffic that passes through a NAT firewall.
        
        @param request: CreateNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNatFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNatFirewallControlPolicy',
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
            cloudfw_20171207_models.CreateNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nat_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.CreateNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.CreateNatFirewallControlPolicyResponse:
        """
        You can use this operation to create an access control policy to allow, deny, or monitor traffic that passes through a NAT firewall.
        
        @param request: CreateNatFirewallControlPolicyRequest
        @return: CreateNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_nat_firewall_control_policy_with_options(request, runtime)

    async def create_nat_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.CreateNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.CreateNatFirewallControlPolicyResponse:
        """
        You can use this operation to create an access control policy to allow, deny, or monitor traffic that passes through a NAT firewall.
        
        @param request: CreateNatFirewallControlPolicyRequest
        @return: CreateNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_nat_firewall_control_policy_with_options_async(request, runtime)

    def create_tr_firewall_v2with_options(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.firewall_description):
            query['FirewallDescription'] = request.firewall_description
        if not UtilClient.is_unset(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not UtilClient.is_unset(request.firewall_subnet_cidr):
            query['FirewallSubnetCidr'] = request.firewall_subnet_cidr
        if not UtilClient.is_unset(request.firewall_vpc_cidr):
            query['FirewallVpcCidr'] = request.firewall_vpc_cidr
        if not UtilClient.is_unset(request.firewall_vpc_id):
            query['FirewallVpcId'] = request.firewall_vpc_id
        if not UtilClient.is_unset(request.firewall_vswitch_id):
            query['FirewallVswitchId'] = request.firewall_vswitch_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not UtilClient.is_unset(request.tr_attachment_master_cidr):
            query['TrAttachmentMasterCidr'] = request.tr_attachment_master_cidr
        if not UtilClient.is_unset(request.tr_attachment_slave_cidr):
            query['TrAttachmentSlaveCidr'] = request.tr_attachment_slave_cidr
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrFirewallV2',
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
            cloudfw_20171207_models.CreateTrFirewallV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_tr_firewall_v2with_options_async(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.firewall_description):
            query['FirewallDescription'] = request.firewall_description
        if not UtilClient.is_unset(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not UtilClient.is_unset(request.firewall_subnet_cidr):
            query['FirewallSubnetCidr'] = request.firewall_subnet_cidr
        if not UtilClient.is_unset(request.firewall_vpc_cidr):
            query['FirewallVpcCidr'] = request.firewall_vpc_cidr
        if not UtilClient.is_unset(request.firewall_vpc_id):
            query['FirewallVpcId'] = request.firewall_vpc_id
        if not UtilClient.is_unset(request.firewall_vswitch_id):
            query['FirewallVswitchId'] = request.firewall_vswitch_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not UtilClient.is_unset(request.tr_attachment_master_cidr):
            query['TrAttachmentMasterCidr'] = request.tr_attachment_master_cidr
        if not UtilClient.is_unset(request.tr_attachment_slave_cidr):
            query['TrAttachmentSlaveCidr'] = request.tr_attachment_slave_cidr
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrFirewallV2',
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
            cloudfw_20171207_models.CreateTrFirewallV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tr_firewall_v2(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2Request,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2Response:
        runtime = util_models.RuntimeOptions()
        return self.create_tr_firewall_v2with_options(request, runtime)

    async def create_tr_firewall_v2_async(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2Request,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.create_tr_firewall_v2with_options_async(request, runtime)

    def create_tr_firewall_v2route_policy_with_options(
        self,
        tmp_req: cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not UtilClient.is_unset(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not UtilClient.is_unset(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.policy_description):
            query['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrFirewallV2RoutePolicy',
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
            cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tr_firewall_v2route_policy_with_options_async(
        self,
        tmp_req: cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not UtilClient.is_unset(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not UtilClient.is_unset(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.policy_description):
            query['PolicyDescription'] = request.policy_description
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrFirewallV2RoutePolicy',
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
            cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tr_firewall_v2route_policy(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyRequest,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tr_firewall_v2route_policy_with_options(request, runtime)

    async def create_tr_firewall_v2route_policy_async(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyRequest,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tr_firewall_v2route_policy_with_options_async(request, runtime)

    def create_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse:
        """
        You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](~~172295~~).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallCenConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcFirewallCenConfigureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.firewall_vswitch_cidr_block):
            query['FirewallVSwitchCidrBlock'] = request.firewall_vswitch_cidr_block
        if not UtilClient.is_unset(request.firewall_vpc_cidr_block):
            query['FirewallVpcCidrBlock'] = request.firewall_vpc_cidr_block
        if not UtilClient.is_unset(request.firewall_vpc_zone_id):
            query['FirewallVpcZoneId'] = request.firewall_vpc_zone_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
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
        """
        You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](~~172295~~).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallCenConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcFirewallCenConfigureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.firewall_vswitch_cidr_block):
            query['FirewallVSwitchCidrBlock'] = request.firewall_vswitch_cidr_block
        if not UtilClient.is_unset(request.firewall_vpc_cidr_block):
            query['FirewallVpcCidrBlock'] = request.firewall_vpc_cidr_block
        if not UtilClient.is_unset(request.firewall_vpc_zone_id):
            query['FirewallVpcZoneId'] = request.firewall_vpc_zone_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
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
        """
        You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](~~172295~~).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallCenConfigureRequest
        @return: CreateVpcFirewallCenConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_firewall_cen_configure_with_options(request, runtime)

    async def create_vpc_firewall_cen_configure_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse:
        """
        You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](~~172295~~).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallCenConfigureRequest
        @return: CreateVpcFirewallCenConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def create_vpc_firewall_configure_with_options(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallConfigureResponse:
        """
        You can call the CreateVpcFirewallConfigure operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [Limits on VPC firewalls](https://www.alibabacloud.com/help/en/cloud-firewall/latest/vpc-firewall-limits).
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcFirewallConfigureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not UtilClient.is_unset(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not UtilClient.is_unset(request.local_vpc_region):
            query['LocalVpcRegion'] = request.local_vpc_region
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not UtilClient.is_unset(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not UtilClient.is_unset(request.peer_vpc_region):
            query['PeerVpcRegion'] = request.peer_vpc_region
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcFirewallConfigure',
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
            cloudfw_20171207_models.CreateVpcFirewallConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_configure_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallConfigureResponse:
        """
        You can call the CreateVpcFirewallConfigure operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [Limits on VPC firewalls](https://www.alibabacloud.com/help/en/cloud-firewall/latest/vpc-firewall-limits).
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcFirewallConfigureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not UtilClient.is_unset(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not UtilClient.is_unset(request.local_vpc_region):
            query['LocalVpcRegion'] = request.local_vpc_region
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not UtilClient.is_unset(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not UtilClient.is_unset(request.peer_vpc_region):
            query['PeerVpcRegion'] = request.peer_vpc_region
        if not UtilClient.is_unset(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVpcFirewallConfigure',
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
            cloudfw_20171207_models.CreateVpcFirewallConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_configure(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallConfigureResponse:
        """
        You can call the CreateVpcFirewallConfigure operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [Limits on VPC firewalls](https://www.alibabacloud.com/help/en/cloud-firewall/latest/vpc-firewall-limits).
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallConfigureRequest
        @return: CreateVpcFirewallConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_firewall_configure_with_options(request, runtime)

    async def create_vpc_firewall_configure_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallConfigureResponse:
        """
        You can call the CreateVpcFirewallConfigure operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [Limits on VPC firewalls](https://www.alibabacloud.com/help/en/cloud-firewall/latest/vpc-firewall-limits).
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallConfigureRequest
        @return: CreateVpcFirewallConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_firewall_configure_with_options_async(request, runtime)

    def create_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        """
        You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpcFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallControlPolicyRequest
        @return: CreateVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_firewall_control_policy_with_options(request, runtime)

    async def create_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.CreateVpcFirewallControlPolicyResponse:
        """
        You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateVpcFirewallControlPolicyRequest
        @return: CreateVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_firewall_control_policy_with_options_async(request, runtime)

    def delete_address_book_with_options(
        self,
        request: cloudfw_20171207_models.DeleteAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteAddressBookResponse:
        """
        You can call the DeleteAddressBook operation to delete an address book for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAddressBookResponse
        """
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
        """
        You can call the DeleteAddressBook operation to delete an address book for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAddressBookResponse
        """
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
        """
        You can call the DeleteAddressBook operation to delete an address book for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteAddressBookRequest
        @return: DeleteAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_address_book_with_options(request, runtime)

    async def delete_address_book_async(
        self,
        request: cloudfw_20171207_models.DeleteAddressBookRequest,
    ) -> cloudfw_20171207_models.DeleteAddressBookResponse:
        """
        You can call the DeleteAddressBook operation to delete an address book for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteAddressBookRequest
        @return: DeleteAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_address_book_with_options_async(request, runtime)

    def delete_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteControlPolicyResponse:
        """
        You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteControlPolicyResponse
        """
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
        """
        You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteControlPolicyResponse
        """
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
        """
        You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteControlPolicyRequest
        @return: DeleteControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    async def delete_control_policy_async(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteControlPolicyResponse:
        """
        You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteControlPolicyRequest
        @return: DeleteControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_firewall_v2route_policies_with_options(
        self,
        request: cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallV2RoutePolicies',
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
            cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_v2route_policies_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFirewallV2RoutePolicies',
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
            cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_v2route_policies(
        self,
        request: cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesRequest,
    ) -> cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_v2route_policies_with_options(request, runtime)

    async def delete_firewall_v2route_policies_async(
        self,
        request: cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesRequest,
    ) -> cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_v2route_policies_with_options_async(request, runtime)

    def delete_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        """
        You can call the DeleteInstanceMembers operation to remove members from Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteInstanceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceMembersResponse
        """
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
        """
        You can call the DeleteInstanceMembers operation to remove members from Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteInstanceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceMembersResponse
        """
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
        """
        You can call the DeleteInstanceMembers operation to remove members from Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteInstanceMembersRequest
        @return: DeleteInstanceMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_members_with_options(request, runtime)

    async def delete_instance_members_async(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        """
        You can call the DeleteInstanceMembers operation to remove members from Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteInstanceMembersRequest
        @return: DeleteInstanceMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_members_with_options_async(request, runtime)

    def delete_nat_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyResponse:
        """
        You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
        @param request: DeleteNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNatFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNatFirewallControlPolicy',
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
            cloudfw_20171207_models.DeleteNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nat_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyResponse:
        """
        You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
        @param request: DeleteNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNatFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNatFirewallControlPolicy',
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
            cloudfw_20171207_models.DeleteNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nat_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyResponse:
        """
        You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
        @param request: DeleteNatFirewallControlPolicyRequest
        @return: DeleteNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_firewall_control_policy_with_options(request, runtime)

    async def delete_nat_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyResponse:
        """
        You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
        @param request: DeleteNatFirewallControlPolicyRequest
        @return: DeleteNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_firewall_control_policy_with_options_async(request, runtime)

    def delete_tr_firewall_v2with_options(
        self,
        request: cloudfw_20171207_models.DeleteTrFirewallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteTrFirewallV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrFirewallV2',
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
            cloudfw_20171207_models.DeleteTrFirewallV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_tr_firewall_v2with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteTrFirewallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteTrFirewallV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrFirewallV2',
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
            cloudfw_20171207_models.DeleteTrFirewallV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tr_firewall_v2(
        self,
        request: cloudfw_20171207_models.DeleteTrFirewallV2Request,
    ) -> cloudfw_20171207_models.DeleteTrFirewallV2Response:
        runtime = util_models.RuntimeOptions()
        return self.delete_tr_firewall_v2with_options(request, runtime)

    async def delete_tr_firewall_v2_async(
        self,
        request: cloudfw_20171207_models.DeleteTrFirewallV2Request,
    ) -> cloudfw_20171207_models.DeleteTrFirewallV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tr_firewall_v2with_options_async(request, runtime)

    def delete_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse:
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallCenConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcFirewallCenConfigureResponse
        """
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
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallCenConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcFirewallCenConfigureResponse
        """
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
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallCenConfigureRequest
        @return: DeleteVpcFirewallCenConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_firewall_cen_configure_with_options(request, runtime)

    async def delete_vpc_firewall_cen_configure_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse:
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallCenConfigureRequest
        @return: DeleteVpcFirewallCenConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def delete_vpc_firewall_configure_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse:
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcFirewallConfigureResponse
        """
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
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcFirewallConfigureResponse
        """
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
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallConfigureRequest
        @return: DeleteVpcFirewallConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_firewall_configure_with_options(request, runtime)

    async def delete_vpc_firewall_configure_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallConfigureResponse:
        """
        You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallConfigureRequest
        @return: DeleteVpcFirewallConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_firewall_configure_with_options_async(request, runtime)

    def delete_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        """
        You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcFirewallControlPolicyResponse
        """
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
        """
        You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpcFirewallControlPolicyResponse
        """
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
        """
        You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallControlPolicyRequest
        @return: DeleteVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_firewall_control_policy_with_options(request, runtime)

    async def delete_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallControlPolicyResponse:
        """
        You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallControlPolicyRequest
        @return: DeleteVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_firewall_control_policy_with_options_async(request, runtime)

    def describe_address_book_with_options(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        """
        You can call the DescribeAddressBook operation to query the details about an address book for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddressBookResponse
        """
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
        """
        You can call the DescribeAddressBook operation to query the details about an address book for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddressBookResponse
        """
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
        """
        You can call the DescribeAddressBook operation to query the details about an address book for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAddressBookRequest
        @return: DescribeAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_address_book_with_options(request, runtime)

    async def describe_address_book_async(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        """
        You can call the DescribeAddressBook operation to query the details about an address book for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAddressBookRequest
        @return: DescribeAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_address_book_with_options_async(request, runtime)

    def describe_asset_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeAssetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetListResponse:
        """
        You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAssetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetListResponse
        """
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
        if not UtilClient.is_unset(request.new_resource_tag):
            query['NewResourceTag'] = request.new_resource_tag
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
        """
        You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAssetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetListResponse
        """
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
        if not UtilClient.is_unset(request.new_resource_tag):
            query['NewResourceTag'] = request.new_resource_tag
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
        """
        You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAssetListRequest
        @return: DescribeAssetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_list_with_options(request, runtime)

    async def describe_asset_list_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetListRequest,
    ) -> cloudfw_20171207_models.DescribeAssetListResponse:
        """
        You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAssetListRequest
        @return: DescribeAssetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_list_with_options_async(request, runtime)

    def describe_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        """
        You can call the DescribeControlPolicy operation to query the details about access control policies by page.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
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
        """
        You can call the DescribeControlPolicy operation to query the details about access control policies by page.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
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
        """
        You can call the DescribeControlPolicy operation to query the details about access control policies by page.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeControlPolicyRequest
        @return: DescribeControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_control_policy_with_options(request, runtime)

    async def describe_control_policy_async(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        """
        You can call the DescribeControlPolicy operation to query the details about access control policies by page.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeControlPolicyRequest
        @return: DescribeControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_control_policy_with_options_async(request, runtime)

    def describe_default_ipsconfig_with_options(
        self,
        request: cloudfw_20171207_models.DescribeDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefaultIPSConfig',
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
            cloudfw_20171207_models.DescribeDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_default_ipsconfig_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDefaultIPSConfig',
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
            cloudfw_20171207_models.DescribeDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_default_ipsconfig(
        self,
        request: cloudfw_20171207_models.DescribeDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.DescribeDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_default_ipsconfig_with_options(request, runtime)

    async def describe_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.DescribeDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.DescribeDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_default_ipsconfig_with_options_async(request, runtime)

    def describe_domain_resolve_with_options(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        """
        You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResolveResponse
        """
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
        """
        You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResolveResponse
        """
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
        """
        You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @return: DescribeDomainResolveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resolve_with_options(request, runtime)

    async def describe_domain_resolve_async(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        """
        You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @return: DescribeDomainResolveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_resolve_with_options_async(request, runtime)

    def describe_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        """
        You can use this operation to query the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceMembersResponse
        """
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
        """
        You can use this operation to query the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceMembersResponse
        """
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
        """
        You can use this operation to query the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceMembersRequest
        @return: DescribeInstanceMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_members_with_options(request, runtime)

    async def describe_instance_members_async(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        """
        You can use this operation to query the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceMembersRequest
        @return: DescribeInstanceMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_members_with_options_async(request, runtime)

    def describe_internet_open_ip_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInternetOpenIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInternetOpenIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not UtilClient.is_unset(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not UtilClient.is_unset(request.assets_type):
            query['AssetsType'] = request.assets_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInternetOpenIp',
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
            cloudfw_20171207_models.DescribeInternetOpenIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_open_ip_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeInternetOpenIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInternetOpenIpResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not UtilClient.is_unset(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not UtilClient.is_unset(request.assets_type):
            query['AssetsType'] = request.assets_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInternetOpenIp',
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
            cloudfw_20171207_models.DescribeInternetOpenIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_open_ip(
        self,
        request: cloudfw_20171207_models.DescribeInternetOpenIpRequest,
    ) -> cloudfw_20171207_models.DescribeInternetOpenIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_internet_open_ip_with_options(request, runtime)

    async def describe_internet_open_ip_async(
        self,
        request: cloudfw_20171207_models.DescribeInternetOpenIpRequest,
    ) -> cloudfw_20171207_models.DescribeInternetOpenIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_internet_open_ip_with_options_async(request, runtime)

    def describe_internet_traffic_trend_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInternetTrafficTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInternetTrafficTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_private_ip):
            query['SrcPrivateIP'] = request.src_private_ip
        if not UtilClient.is_unset(request.src_public_ip):
            query['SrcPublicIP'] = request.src_public_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInternetTrafficTrend',
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
            cloudfw_20171207_models.DescribeInternetTrafficTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_traffic_trend_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeInternetTrafficTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInternetTrafficTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_code):
            query['SourceCode'] = request.source_code
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.src_private_ip):
            query['SrcPrivateIP'] = request.src_private_ip
        if not UtilClient.is_unset(request.src_public_ip):
            query['SrcPublicIP'] = request.src_public_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInternetTrafficTrend',
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
            cloudfw_20171207_models.DescribeInternetTrafficTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_traffic_trend(
        self,
        request: cloudfw_20171207_models.DescribeInternetTrafficTrendRequest,
    ) -> cloudfw_20171207_models.DescribeInternetTrafficTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_internet_traffic_trend_with_options(request, runtime)

    async def describe_internet_traffic_trend_async(
        self,
        request: cloudfw_20171207_models.DescribeInternetTrafficTrendRequest,
    ) -> cloudfw_20171207_models.DescribeInternetTrafficTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_internet_traffic_trend_with_options_async(request, runtime)

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

    def describe_nat_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallControlPolicyResponse:
        """
        You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
        @param request: DescribeNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatFirewallControlPolicy',
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
            cloudfw_20171207_models.DescribeNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallControlPolicyResponse:
        """
        You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
        @param request: DescribeNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatFirewallControlPolicy',
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
            cloudfw_20171207_models.DescribeNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeNatFirewallControlPolicyResponse:
        """
        You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
        @param request: DescribeNatFirewallControlPolicyRequest
        @return: DescribeNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_firewall_control_policy_with_options(request, runtime)

    async def describe_nat_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeNatFirewallControlPolicyResponse:
        """
        You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
        @param request: DescribeNatFirewallControlPolicyRequest
        @return: DescribeNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_firewall_control_policy_with_options_async(request, runtime)

    def describe_nat_firewall_policy_prior_used_with_options(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedResponse:
        """
        You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
        @param request: DescribeNatFirewallPolicyPriorUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatFirewallPolicyPriorUsedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatFirewallPolicyPriorUsed',
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
            cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_policy_prior_used_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedResponse:
        """
        You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
        @param request: DescribeNatFirewallPolicyPriorUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatFirewallPolicyPriorUsedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatFirewallPolicyPriorUsed',
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
            cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_policy_prior_used(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedResponse:
        """
        You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
        @param request: DescribeNatFirewallPolicyPriorUsedRequest
        @return: DescribeNatFirewallPolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_firewall_policy_prior_used_with_options(request, runtime)

    async def describe_nat_firewall_policy_prior_used_async(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedResponse:
        """
        You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
        @param request: DescribeNatFirewallPolicyPriorUsedRequest
        @return: DescribeNatFirewallPolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_firewall_policy_prior_used_with_options_async(request, runtime)

    def describe_outgoing_destination_ipwith_options(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDestinationIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
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
        if not UtilClient.is_unset(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
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
        if not UtilClient.is_unset(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
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
        if not UtilClient.is_unset(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
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
        if not UtilClient.is_unset(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
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
        """
        You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyAdvancedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyAdvancedConfigResponse
        """
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
        """
        You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyAdvancedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyAdvancedConfigResponse
        """
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
        """
        You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyAdvancedConfigRequest
        @return: DescribePolicyAdvancedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_advanced_config_with_options(request, runtime)

    async def describe_policy_advanced_config_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        """
        You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyAdvancedConfigRequest
        @return: DescribePolicyAdvancedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_advanced_config_with_options_async(request, runtime)

    def describe_policy_prior_used_with_options(
        self,
        request: cloudfw_20171207_models.DescribePolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyPriorUsedResponse:
        """
        You can call the DescribePolicyPriorUsed operation to query the priority range of the access control policies that match specific query conditions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyPriorUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyPriorUsedResponse
        """
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
        """
        You can call the DescribePolicyPriorUsed operation to query the priority range of the access control policies that match specific query conditions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyPriorUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyPriorUsedResponse
        """
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
        """
        You can call the DescribePolicyPriorUsed operation to query the priority range of the access control policies that match specific query conditions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyPriorUsedRequest
        @return: DescribePolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_prior_used_with_options(request, runtime)

    async def describe_policy_prior_used_async(
        self,
        request: cloudfw_20171207_models.DescribePolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribePolicyPriorUsedResponse:
        """
        You can call the DescribePolicyPriorUsed operation to query the priority range of the access control policies that match specific query conditions.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyPriorUsedRequest
        @return: DescribePolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_prior_used_with_options_async(request, runtime)

    def describe_risk_event_group_with_options(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        """
        You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRiskEventGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRiskEventGroupResponse
        """
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
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
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
        """
        You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRiskEventGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRiskEventGroupResponse
        """
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
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
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
        """
        You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRiskEventGroupRequest
        @return: DescribeRiskEventGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_group_with_options(request, runtime)

    async def describe_risk_event_group_async(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        """
        You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeRiskEventGroupRequest
        @return: DescribeRiskEventGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_event_group_with_options_async(request, runtime)

    def describe_risk_event_payload_with_options(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventPayloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeRiskEventPayloadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventPayload',
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
            cloudfw_20171207_models.DescribeRiskEventPayloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_payload_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventPayloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeRiskEventPayloadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not UtilClient.is_unset(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not UtilClient.is_unset(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not UtilClient.is_unset(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not UtilClient.is_unset(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskEventPayload',
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
            cloudfw_20171207_models.DescribeRiskEventPayloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_payload(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventPayloadRequest,
    ) -> cloudfw_20171207_models.DescribeRiskEventPayloadResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_payload_with_options(request, runtime)

    async def describe_risk_event_payload_async(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventPayloadRequest,
    ) -> cloudfw_20171207_models.DescribeRiskEventPayloadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_event_payload_with_options_async(request, runtime)

    def describe_tr_firewall_policy_back_up_association_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallPolicyBackUpAssociationList',
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
            cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewall_policy_back_up_association_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallPolicyBackUpAssociationList',
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
            cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewall_policy_back_up_association_list(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewall_policy_back_up_association_list_with_options(request, runtime)

    async def describe_tr_firewall_policy_back_up_association_list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewall_policy_back_up_association_list_with_options_async(request, runtime)

    def describe_tr_firewall_v2route_policy_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallV2RoutePolicyList',
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
            cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewall_v2route_policy_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallV2RoutePolicyList',
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
            cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewall_v2route_policy_list(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewall_v2route_policy_list_with_options(request, runtime)

    async def describe_tr_firewall_v2route_policy_list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewall_v2route_policy_list_with_options_async(request, runtime)

    def describe_tr_firewalls_v2detail_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2DetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallsV2Detail',
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
            cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewalls_v2detail_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2DetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallsV2Detail',
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
            cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewalls_v2detail(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2DetailRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewalls_v2detail_with_options(request, runtime)

    async def describe_tr_firewalls_v2detail_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2DetailRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewalls_v2detail_with_options_async(request, runtime)

    def describe_tr_firewalls_v2list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2ListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not UtilClient.is_unset(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallsV2List',
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
            cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewalls_v2list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2ListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not UtilClient.is_unset(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not UtilClient.is_unset(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallsV2List',
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
            cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewalls_v2list(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2ListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewalls_v2list_with_options(request, runtime)

    async def describe_tr_firewalls_v2list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2ListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewalls_v2list_with_options_async(request, runtime)

    def describe_tr_firewalls_v2route_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2RouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallsV2RouteList',
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
            cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewalls_v2route_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2RouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrFirewallsV2RouteList',
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
            cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewalls_v2route_list(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2RouteListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewalls_v2route_list_with_options(request, runtime)

    async def describe_tr_firewalls_v2route_list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2RouteListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewalls_v2route_list_with_options_async(request, runtime)

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

    def describe_user_ipswhitelist_with_options(
        self,
        request: cloudfw_20171207_models.DescribeUserIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserIPSWhitelistResponse:
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
            action='DescribeUserIPSWhitelist',
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
            cloudfw_20171207_models.DescribeUserIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_ipswhitelist_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeUserIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserIPSWhitelistResponse:
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
            action='DescribeUserIPSWhitelist',
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
            cloudfw_20171207_models.DescribeUserIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_ipswhitelist(
        self,
        request: cloudfw_20171207_models.DescribeUserIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.DescribeUserIPSWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_ipswhitelist_with_options(request, runtime)

    async def describe_user_ipswhitelist_async(
        self,
        request: cloudfw_20171207_models.DescribeUserIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.DescribeUserIPSWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_ipswhitelist_with_options_async(request, runtime)

    def describe_vpc_firewall_acl_group_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        """
        You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallAclGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallAclGroupListResponse
        """
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
        """
        You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallAclGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallAclGroupListResponse
        """
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
        """
        You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallAclGroupListRequest
        @return: DescribeVpcFirewallAclGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_acl_group_list_with_options(request, runtime)

    async def describe_vpc_firewall_acl_group_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        """
        You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallAclGroupListRequest
        @return: DescribeVpcFirewallAclGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_acl_group_list_with_options_async(request, runtime)

    def describe_vpc_firewall_cen_detail_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse:
        """
        You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallCenDetailResponse
        """
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
        """
        You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallCenDetailResponse
        """
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
        """
        You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenDetailRequest
        @return: DescribeVpcFirewallCenDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_cen_detail_with_options(request, runtime)

    async def describe_vpc_firewall_cen_detail_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenDetailRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenDetailResponse:
        """
        You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenDetailRequest
        @return: DescribeVpcFirewallCenDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_cen_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_cen_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenListResponse:
        """
        You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallCenListResponse
        """
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
        """
        You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallCenListResponse
        """
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
        """
        You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenListRequest
        @return: DescribeVpcFirewallCenListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_cen_list_with_options(request, runtime)

    async def describe_vpc_firewall_cen_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallCenListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallCenListResponse:
        """
        You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallCenListRequest
        @return: DescribeVpcFirewallCenListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_cen_list_with_options_async(request, runtime)

    def describe_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        """
        You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
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
        """
        You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
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
        """
        You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallControlPolicyRequest
        @return: DescribeVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_control_policy_with_options(request, runtime)

    async def describe_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallControlPolicyResponse:
        """
        You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallControlPolicyRequest
        @return: DescribeVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_control_policy_with_options_async(request, runtime)

    def describe_vpc_firewall_default_ipsconfig_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        """
        You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallDefaultIPSConfigResponse
        """
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
        """
        You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallDefaultIPSConfigResponse
        """
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
        """
        You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDefaultIPSConfigRequest
        @return: DescribeVpcFirewallDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_default_ipsconfig_with_options(request, runtime)

    async def describe_vpc_firewall_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        """
        You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDefaultIPSConfigRequest
        @return: DescribeVpcFirewallDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_default_ipsconfig_with_options_async(request, runtime)

    def describe_vpc_firewall_detail_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDetailResponse:
        """
        You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://www.alibabacloud.com/help/en/cloud-firewall/latest/createvpcfirewallconfigure) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallDetailResponse
        """
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
        """
        You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://www.alibabacloud.com/help/en/cloud-firewall/latest/createvpcfirewallconfigure) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallDetailResponse
        """
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
        """
        You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://www.alibabacloud.com/help/en/cloud-firewall/latest/createvpcfirewallconfigure) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDetailRequest
        @return: DescribeVpcFirewallDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_detail_with_options(request, runtime)

    async def describe_vpc_firewall_detail_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallDetailRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallDetailResponse:
        """
        You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://www.alibabacloud.com/help/en/cloud-firewall/latest/createvpcfirewallconfigure) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDetailRequest
        @return: DescribeVpcFirewallDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallListResponse:
        """
        You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallListResponse
        """
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
        """
        You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallListResponse
        """
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
        """
        You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallListRequest
        @return: DescribeVpcFirewallListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_list_with_options(request, runtime)

    async def describe_vpc_firewall_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallListRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallListResponse:
        """
        You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        ### Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallListRequest
        @return: DescribeVpcFirewallListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_list_with_options_async(request, runtime)

    def describe_vpc_firewall_policy_prior_used_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        """
        You can call the DescribeVpcFirewallPolicyPriorUsed operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallPolicyPriorUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallPolicyPriorUsedResponse
        """
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
        """
        You can call the DescribeVpcFirewallPolicyPriorUsed operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallPolicyPriorUsedRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallPolicyPriorUsedResponse
        """
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
        """
        You can call the DescribeVpcFirewallPolicyPriorUsed operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallPolicyPriorUsedRequest
        @return: DescribeVpcFirewallPolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_policy_prior_used_with_options(request, runtime)

    async def describe_vpc_firewall_policy_prior_used_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        """
        You can call the DescribeVpcFirewallPolicyPriorUsed operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallPolicyPriorUsedRequest
        @return: DescribeVpcFirewallPolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_policy_prior_used_with_options_async(request, runtime)

    def describe_vulnerability_protected_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVulnerabilityProtectedListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.vuln_cve_name):
            query['VulnCveName'] = request.vuln_cve_name
        if not UtilClient.is_unset(request.vuln_level):
            query['VulnLevel'] = request.vuln_level
        if not UtilClient.is_unset(request.vuln_resource):
            query['VulnResource'] = request.vuln_resource
        if not UtilClient.is_unset(request.vuln_status):
            query['VulnStatus'] = request.vuln_status
        if not UtilClient.is_unset(request.vuln_type):
            query['VulnType'] = request.vuln_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulnerabilityProtectedList',
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
            cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vulnerability_protected_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVulnerabilityProtectedListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_key):
            query['SortKey'] = request.sort_key
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        if not UtilClient.is_unset(request.vuln_cve_name):
            query['VulnCveName'] = request.vuln_cve_name
        if not UtilClient.is_unset(request.vuln_level):
            query['VulnLevel'] = request.vuln_level
        if not UtilClient.is_unset(request.vuln_resource):
            query['VulnResource'] = request.vuln_resource
        if not UtilClient.is_unset(request.vuln_status):
            query['VulnStatus'] = request.vuln_status
        if not UtilClient.is_unset(request.vuln_type):
            query['VulnType'] = request.vuln_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulnerabilityProtectedList',
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
            cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vulnerability_protected_list(
        self,
        request: cloudfw_20171207_models.DescribeVulnerabilityProtectedListRequest,
    ) -> cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vulnerability_protected_list_with_options(request, runtime)

    async def describe_vulnerability_protected_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVulnerabilityProtectedListRequest,
    ) -> cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vulnerability_protected_list_with_options_async(request, runtime)

    def modify_address_book_with_options(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        """
        You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAddressBookResponse
        """
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
        """
        You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyAddressBookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAddressBookResponse
        """
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
        """
        You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyAddressBookRequest
        @return: ModifyAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_address_book_with_options(request, runtime)

    async def modify_address_book_async(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        """
        You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyAddressBookRequest
        @return: ModifyAddressBookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_address_book_with_options_async(request, runtime)

    def modify_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyResponse:
        """
        You can call the ModifyControlPolicy operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the ModifyControlPolicy operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the ModifyControlPolicy operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyRequest
        @return: ModifyControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_control_policy_with_options(request, runtime)

    async def modify_control_policy_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyControlPolicyResponse:
        """
        You can call the ModifyControlPolicy operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyRequest
        @return: ModifyControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_control_policy_with_options_async(request, runtime)

    def modify_control_policy_position_with_options(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyControlPolicyPositionResponse:
        """
        You can call the ModifyControlPolicyPosition operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyPositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyControlPolicyPositionResponse
        """
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
        """
        You can call the ModifyControlPolicyPosition operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyPositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyControlPolicyPositionResponse
        """
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
        """
        You can call the ModifyControlPolicyPosition operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyPositionRequest
        @return: ModifyControlPolicyPositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_control_policy_position_with_options(request, runtime)

    async def modify_control_policy_position_async(
        self,
        request: cloudfw_20171207_models.ModifyControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyControlPolicyPositionResponse:
        """
        You can call the ModifyControlPolicyPosition operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyControlPolicyPositionRequest
        @return: ModifyControlPolicyPositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_control_policy_position_with_options_async(request, runtime)

    def modify_default_ipsconfig_with_options(
        self,
        request: cloudfw_20171207_models.ModifyDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ai_rules):
            query['AiRules'] = request.ai_rules
        if not UtilClient.is_unset(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not UtilClient.is_unset(request.cti_rules):
            query['CtiRules'] = request.cti_rules
        if not UtilClient.is_unset(request.enable_all_patch):
            query['EnableAllPatch'] = request.enable_all_patch
        if not UtilClient.is_unset(request.enable_default):
            query['EnableDefault'] = request.enable_default
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.patch_rules):
            query['PatchRules'] = request.patch_rules
        if not UtilClient.is_unset(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefaultIPSConfig',
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
            cloudfw_20171207_models.ModifyDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_default_ipsconfig_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyDefaultIPSConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ai_rules):
            query['AiRules'] = request.ai_rules
        if not UtilClient.is_unset(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not UtilClient.is_unset(request.cti_rules):
            query['CtiRules'] = request.cti_rules
        if not UtilClient.is_unset(request.enable_all_patch):
            query['EnableAllPatch'] = request.enable_all_patch
        if not UtilClient.is_unset(request.enable_default):
            query['EnableDefault'] = request.enable_default
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.patch_rules):
            query['PatchRules'] = request.patch_rules
        if not UtilClient.is_unset(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDefaultIPSConfig',
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
            cloudfw_20171207_models.ModifyDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_default_ipsconfig(
        self,
        request: cloudfw_20171207_models.ModifyDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.ModifyDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_default_ipsconfig_with_options(request, runtime)

    async def modify_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.ModifyDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.ModifyDefaultIPSConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_default_ipsconfig_with_options_async(request, runtime)

    def modify_firewall_v2route_policy_switch_with_options(
        self,
        request: cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.should_recover):
            query['ShouldRecover'] = request.should_recover
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        if not UtilClient.is_unset(request.tr_firewall_route_policy_switch_status):
            query['TrFirewallRoutePolicySwitchStatus'] = request.tr_firewall_route_policy_switch_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFirewallV2RoutePolicySwitch',
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
            cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_firewall_v2route_policy_switch_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.should_recover):
            query['ShouldRecover'] = request.should_recover
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        if not UtilClient.is_unset(request.tr_firewall_route_policy_switch_status):
            query['TrFirewallRoutePolicySwitchStatus'] = request.tr_firewall_route_policy_switch_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFirewallV2RoutePolicySwitch',
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
            cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_firewall_v2route_policy_switch(
        self,
        request: cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchRequest,
    ) -> cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_firewall_v2route_policy_switch_with_options(request, runtime)

    async def modify_firewall_v2route_policy_switch_async(
        self,
        request: cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchRequest,
    ) -> cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_firewall_v2route_policy_switch_with_options_async(request, runtime)

    def modify_instance_member_attributes_with_options(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        """
        You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second for each account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyInstanceMemberAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMemberAttributesResponse
        """
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
        """
        You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second for each account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyInstanceMemberAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceMemberAttributesResponse
        """
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
        """
        You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second for each account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyInstanceMemberAttributesRequest
        @return: ModifyInstanceMemberAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_member_attributes_with_options(request, runtime)

    async def modify_instance_member_attributes_async(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        """
        You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second for each account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyInstanceMemberAttributesRequest
        @return: ModifyInstanceMemberAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_member_attributes_with_options_async(request, runtime)

    def modify_nat_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyResponse:
        """
        You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNatFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNatFirewallControlPolicy',
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
            cloudfw_20171207_models.ModifyNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_nat_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyResponse:
        """
        You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNatFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_action):
            query['AclAction'] = request.acl_action
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNatFirewallControlPolicy',
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
            cloudfw_20171207_models.ModifyNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_nat_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyResponse:
        """
        You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyRequest
        @return: ModifyNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_nat_firewall_control_policy_with_options(request, runtime)

    async def modify_nat_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyResponse:
        """
        You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyRequest
        @return: ModifyNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_nat_firewall_control_policy_with_options_async(request, runtime)

    def modify_nat_firewall_control_policy_position_with_options(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNatFirewallControlPolicyPosition',
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
            cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_nat_firewall_control_policy_position_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.new_order):
            query['NewOrder'] = request.new_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNatFirewallControlPolicyPosition',
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
            cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_nat_firewall_control_policy_position(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_nat_firewall_control_policy_position_with_options(request, runtime)

    async def modify_nat_firewall_control_policy_position_async(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_nat_firewall_control_policy_position_with_options_async(request, runtime)

    def modify_policy_advanced_config_with_options(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        """
        You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyPolicyAdvancedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyAdvancedConfigResponse
        """
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
        """
        You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyPolicyAdvancedConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPolicyAdvancedConfigResponse
        """
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
        """
        You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyPolicyAdvancedConfigRequest
        @return: ModifyPolicyAdvancedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_advanced_config_with_options(request, runtime)

    async def modify_policy_advanced_config_async(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        """
        You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyPolicyAdvancedConfigRequest
        @return: ModifyPolicyAdvancedConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_advanced_config_with_options_async(request, runtime)

    def modify_tr_firewall_v2configuration_with_options(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrFirewallV2Configuration',
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
            cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tr_firewall_v2configuration_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrFirewallV2Configuration',
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
            cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tr_firewall_v2configuration(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationRequest,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tr_firewall_v2configuration_with_options(request, runtime)

    async def modify_tr_firewall_v2configuration_async(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationRequest,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tr_firewall_v2configuration_with_options_async(request, runtime)

    def modify_tr_firewall_v2route_policy_scope_with_options(
        self,
        tmp_req: cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not UtilClient.is_unset(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not UtilClient.is_unset(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrFirewallV2RoutePolicyScope',
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
            cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tr_firewall_v2route_policy_scope_with_options_async(
        self,
        tmp_req: cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        UtilClient.validate_model(tmp_req)
        request = cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not UtilClient.is_unset(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not UtilClient.is_unset(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not UtilClient.is_unset(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        if not UtilClient.is_unset(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrFirewallV2RoutePolicyScope',
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
            cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tr_firewall_v2route_policy_scope(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_tr_firewall_v2route_policy_scope_with_options(request, runtime)

    async def modify_tr_firewall_v2route_policy_scope_async(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_tr_firewall_v2route_policy_scope_with_options_async(request, runtime)

    def modify_user_ipswhitelist_with_options(
        self,
        request: cloudfw_20171207_models.ModifyUserIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyUserIPSWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.list_type):
            query['ListType'] = request.list_type
        if not UtilClient.is_unset(request.list_value):
            query['ListValue'] = request.list_value
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserIPSWhitelist',
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
            cloudfw_20171207_models.ModifyUserIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_ipswhitelist_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyUserIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyUserIPSWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.list_type):
            query['ListType'] = request.list_type
        if not UtilClient.is_unset(request.list_value):
            query['ListValue'] = request.list_value
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserIPSWhitelist',
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
            cloudfw_20171207_models.ModifyUserIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_ipswhitelist(
        self,
        request: cloudfw_20171207_models.ModifyUserIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.ModifyUserIPSWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_ipswhitelist_with_options(request, runtime)

    async def modify_user_ipswhitelist_async(
        self,
        request: cloudfw_20171207_models.ModifyUserIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.ModifyUserIPSWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_ipswhitelist_with_options_async(request, runtime)

    def modify_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse:
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallCenConfigureResponse
        """
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
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallCenConfigureResponse
        """
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
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenConfigureRequest
        @return: ModifyVpcFirewallCenConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_cen_configure_with_options(request, runtime)

    async def modify_vpc_firewall_cen_configure_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenConfigureRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse:
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenConfigureRequest
        @return: ModifyVpcFirewallCenConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def modify_vpc_firewall_cen_switch_status_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse:
        """
        You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protect mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenSwitchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallCenSwitchStatusResponse
        """
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
        """
        You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protect mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenSwitchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallCenSwitchStatusResponse
        """
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
        """
        You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protect mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenSwitchStatusRequest
        @return: ModifyVpcFirewallCenSwitchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_cen_switch_status_with_options(request, runtime)

    async def modify_vpc_firewall_cen_switch_status_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenSwitchStatusResponse:
        """
        You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protect mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](~~345772~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallCenSwitchStatusRequest
        @return: ModifyVpcFirewallCenSwitchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_cen_switch_status_with_options_async(request, runtime)

    def modify_vpc_firewall_configure_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse:
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallConfigureResponse
        """
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
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallConfigureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallConfigureResponse
        """
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
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallConfigureRequest
        @return: ModifyVpcFirewallConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_configure_with_options(request, runtime)

    async def modify_vpc_firewall_configure_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallConfigureRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallConfigureResponse:
        """
        You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallConfigureRequest
        @return: ModifyVpcFirewallConfigureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_configure_with_options_async(request, runtime)

    def modify_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        """
        You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallControlPolicyResponse
        """
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proto):
            query['Proto'] = request.proto
        if not UtilClient.is_unset(request.release):
            query['Release'] = request.release
        if not UtilClient.is_unset(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not UtilClient.is_unset(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not UtilClient.is_unset(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not UtilClient.is_unset(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        """
        You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyRequest
        @return: ModifyVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_control_policy_with_options(request, runtime)

    async def modify_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyResponse:
        """
        You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyRequest
        @return: ModifyVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_control_policy_with_options_async(request, runtime)

    def modify_vpc_firewall_control_policy_position_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse:
        """
        You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyPositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallControlPolicyPositionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
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
        """
        You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyPositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallControlPolicyPositionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
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
        """
        You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyPositionRequest
        @return: ModifyVpcFirewallControlPolicyPositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_control_policy_position_with_options(request, runtime)

    async def modify_vpc_firewall_control_policy_position_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallControlPolicyPositionResponse:
        """
        You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallControlPolicyPositionRequest
        @return: ModifyVpcFirewallControlPolicyPositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_control_policy_position_with_options_async(request, runtime)

    def modify_vpc_firewall_default_ipsconfig_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        """
        You can call the ModifyVpcFirewallDefaultIPSConfig operation to modify the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallDefaultIPSConfigResponse
        """
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
        """
        You can call the ModifyVpcFirewallDefaultIPSConfig operation to modify the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallDefaultIPSConfigResponse
        """
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
        """
        You can call the ModifyVpcFirewallDefaultIPSConfig operation to modify the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallDefaultIPSConfigRequest
        @return: ModifyVpcFirewallDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_default_ipsconfig_with_options(request, runtime)

    async def modify_vpc_firewall_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        """
        You can call the ModifyVpcFirewallDefaultIPSConfig operation to modify the intrusion prevention configurations of a VPC firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallDefaultIPSConfigRequest
        @return: ModifyVpcFirewallDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_default_ipsconfig_with_options_async(request, runtime)

    def modify_vpc_firewall_switch_status_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse:
        """
        You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallSwitchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallSwitchStatusResponse
        """
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
        """
        You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallSwitchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallSwitchStatusResponse
        """
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
        """
        You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallSwitchStatusRequest
        @return: ModifyVpcFirewallSwitchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_switch_status_with_options(request, runtime)

    async def modify_vpc_firewall_switch_status_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse:
        """
        You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](~~342893~~) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallSwitchStatusRequest
        @return: ModifyVpcFirewallSwitchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_switch_status_with_options_async(request, runtime)

    def put_disable_all_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        """
        You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableAllFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutDisableAllFwSwitchResponse
        """
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
        """
        You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableAllFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutDisableAllFwSwitchResponse
        """
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
        """
        You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableAllFwSwitchRequest
        @return: PutDisableAllFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_disable_all_fw_switch_with_options(request, runtime)

    async def put_disable_all_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutDisableAllFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutDisableAllFwSwitchResponse:
        """
        You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableAllFwSwitchRequest
        @return: PutDisableAllFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_disable_all_fw_switch_with_options_async(request, runtime)

    def put_disable_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutDisableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutDisableFwSwitchResponse:
        """
        You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutDisableFwSwitchResponse
        """
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
        """
        You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutDisableFwSwitchResponse
        """
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
        """
        You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableFwSwitchRequest
        @return: PutDisableFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_disable_fw_switch_with_options(request, runtime)

    async def put_disable_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutDisableFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutDisableFwSwitchResponse:
        """
        You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutDisableFwSwitchRequest
        @return: PutDisableFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_disable_fw_switch_with_options_async(request, runtime)

    def put_enable_all_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutEnableAllFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableAllFwSwitchResponse:
        """
        You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutEnableAllFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEnableAllFwSwitchResponse
        """
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
        """
        You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutEnableAllFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEnableAllFwSwitchResponse
        """
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
        """
        You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutEnableAllFwSwitchRequest
        @return: PutEnableAllFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_enable_all_fw_switch_with_options(request, runtime)

    async def put_enable_all_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutEnableAllFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutEnableAllFwSwitchResponse:
        """
        You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
        ## Limits
        You can call this operation up to 10 times per second per account. You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutEnableAllFwSwitchRequest
        @return: PutEnableAllFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_enable_all_fw_switch_with_options_async(request, runtime)

    def put_enable_fw_switch_with_options(
        self,
        request: cloudfw_20171207_models.PutEnableFwSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.PutEnableFwSwitchResponse:
        """
        You can call the PutEnableFwSwitch operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: PutEnableFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEnableFwSwitchResponse
        """
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
        """
        You can call the PutEnableFwSwitch operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: PutEnableFwSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutEnableFwSwitchResponse
        """
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
        """
        You can call the PutEnableFwSwitch operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: PutEnableFwSwitchRequest
        @return: PutEnableFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_enable_fw_switch_with_options(request, runtime)

    async def put_enable_fw_switch_async(
        self,
        request: cloudfw_20171207_models.PutEnableFwSwitchRequest,
    ) -> cloudfw_20171207_models.PutEnableFwSwitchResponse:
        """
        You can call the PutEnableFwSwitch operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: PutEnableFwSwitchRequest
        @return: PutEnableFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_enable_fw_switch_with_options_async(request, runtime)

    def reset_vpc_firewall_rule_hit_count_with_options(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        """
        You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResetVpcFirewallRuleHitCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetVpcFirewallRuleHitCountResponse
        """
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
        """
        You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResetVpcFirewallRuleHitCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetVpcFirewallRuleHitCountResponse
        """
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
        """
        You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResetVpcFirewallRuleHitCountRequest
        @return: ResetVpcFirewallRuleHitCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_vpc_firewall_rule_hit_count_with_options(request, runtime)

    async def reset_vpc_firewall_rule_hit_count_async(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        """
        You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResetVpcFirewallRuleHitCountRequest
        @return: ResetVpcFirewallRuleHitCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_vpc_firewall_rule_hit_count_with_options_async(request, runtime)
