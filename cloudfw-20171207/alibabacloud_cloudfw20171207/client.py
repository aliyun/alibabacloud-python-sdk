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
        @summary Creates an address book for access control. Supported address book types are IP address books, Elastic Compute Service (ECS) tag-based address books, port address books, and domain address books. An ECS tag-based address book includes the public IP addresses of the ECS instances that have specific tags.
        
        @description You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## [](#qps)Limits
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
        @summary Creates an address book for access control. Supported address book types are IP address books, Elastic Compute Service (ECS) tag-based address books, port address books, and domain address books. An ECS tag-based address book includes the public IP addresses of the ECS instances that have specific tags.
        
        @description You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## [](#qps)Limits
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
        @summary Creates an address book for access control. Supported address book types are IP address books, Elastic Compute Service (ECS) tag-based address books, port address books, and domain address books. An ECS tag-based address book includes the public IP addresses of the ECS instances that have specific tags.
        
        @description You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## [](#qps)Limits
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
        @summary Creates an address book for access control. Supported address book types are IP address books, Elastic Compute Service (ECS) tag-based address books, port address books, and domain address books. An ECS tag-based address book includes the public IP addresses of the ECS instances that have specific tags.
        
        @description You can call the AddAddressBook operation to create an address book for access control. The address book can be an IP address book, an ECS tag-based address book, a port address book, or a domain address book.
        ## [](#qps)Limits
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
        @summary Creates an access control policy.
        
        @description You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Creates an access control policy.
        
        @description You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Creates an access control policy.
        
        @description You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
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
        @summary Creates an access control policy.
        
        @description You can call the AddControlPolicy operation to create an access control policy to allow, block, or monitor traffic that reaches Cloud Firewall.
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
        @summary Adds members to Cloud Firewall.
        
        @description You can call this operation to add members to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Adds members to Cloud Firewall.
        
        @description You can call this operation to add members to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Adds members to Cloud Firewall.
        
        @description You can call this operation to add members to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Adds members to Cloud Firewall.
        
        @description You can call this operation to add members to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Copies all access control policies from a policy group of a source virtual private cloud (VPC) firewall to a policy group of a destination VPC firewall.
        
        @description You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
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
        @summary Copies all access control policies from a policy group of a source virtual private cloud (VPC) firewall to a policy group of a destination VPC firewall.
        
        @description You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
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
        @summary Copies all access control policies from a policy group of a source virtual private cloud (VPC) firewall to a policy group of a destination VPC firewall.
        
        @description You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
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
        @summary Copies all access control policies from a policy group of a source virtual private cloud (VPC) firewall to a policy group of a destination VPC firewall.
        
        @description You can call the BatchCopyVpcFirewallControlPolicy operation to copy all access control policies from a policy group of a source VPC firewall to a policy group of a destination VPC firewall.
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

    def batch_delete_vpc_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyResponse:
        """
        @summary Deletes multiple access control policies for a virtual private cloud (VPC) firewall at a time.
        
        @param request: BatchDeleteVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteVpcFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteVpcFirewallControlPolicy',
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
            cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_vpc_firewall_control_policy_with_options_async(
        self,
        request: cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyResponse:
        """
        @summary Deletes multiple access control policies for a virtual private cloud (VPC) firewall at a time.
        
        @param request: BatchDeleteVpcFirewallControlPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteVpcFirewallControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteVpcFirewallControlPolicy',
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
            cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_vpc_firewall_control_policy(
        self,
        request: cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyResponse:
        """
        @summary Deletes multiple access control policies for a virtual private cloud (VPC) firewall at a time.
        
        @param request: BatchDeleteVpcFirewallControlPolicyRequest
        @return: BatchDeleteVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_vpc_firewall_control_policy_with_options(request, runtime)

    async def batch_delete_vpc_firewall_control_policy_async(
        self,
        request: cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyRequest,
    ) -> cloudfw_20171207_models.BatchDeleteVpcFirewallControlPolicyResponse:
        """
        @summary Deletes multiple access control policies for a virtual private cloud (VPC) firewall at a time.
        
        @param request: BatchDeleteVpcFirewallControlPolicyRequest
        @return: BatchDeleteVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_vpc_firewall_control_policy_with_options_async(request, runtime)

    def create_download_task_with_options(
        self,
        request: cloudfw_20171207_models.CreateDownloadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateDownloadTaskResponse:
        """
        @summary Creates a file download task.
        
        @param request: CreateDownloadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDownloadTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_data):
            query['TaskData'] = request.task_data
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownloadTask',
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
            cloudfw_20171207_models.CreateDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_download_task_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateDownloadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateDownloadTaskResponse:
        """
        @summary Creates a file download task.
        
        @param request: CreateDownloadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDownloadTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_data):
            query['TaskData'] = request.task_data
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownloadTask',
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
            cloudfw_20171207_models.CreateDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_download_task(
        self,
        request: cloudfw_20171207_models.CreateDownloadTaskRequest,
    ) -> cloudfw_20171207_models.CreateDownloadTaskResponse:
        """
        @summary Creates a file download task.
        
        @param request: CreateDownloadTaskRequest
        @return: CreateDownloadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_download_task_with_options(request, runtime)

    async def create_download_task_async(
        self,
        request: cloudfw_20171207_models.CreateDownloadTaskRequest,
    ) -> cloudfw_20171207_models.CreateDownloadTaskResponse:
        """
        @summary Creates a file download task.
        
        @param request: CreateDownloadTaskRequest
        @return: CreateDownloadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_download_task_with_options_async(request, runtime)

    def create_nat_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.CreateNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateNatFirewallControlPolicyResponse:
        """
        @summary Creates an access control policy for a NAT firewall.
        
        @description You can call this operation to create a policy that allows, denies, or monitors the traffic that passes through the NAT firewall.
        
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
        @summary Creates an access control policy for a NAT firewall.
        
        @description You can call this operation to create a policy that allows, denies, or monitors the traffic that passes through the NAT firewall.
        
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
        @summary Creates an access control policy for a NAT firewall.
        
        @description You can call this operation to create a policy that allows, denies, or monitors the traffic that passes through the NAT firewall.
        
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
        @summary Creates an access control policy for a NAT firewall.
        
        @description You can call this operation to create a policy that allows, denies, or monitors the traffic that passes through the NAT firewall.
        
        @param request: CreateNatFirewallControlPolicyRequest
        @return: CreateNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_nat_firewall_control_policy_with_options_async(request, runtime)

    def create_security_proxy_with_options(
        self,
        request: cloudfw_20171207_models.CreateSecurityProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateSecurityProxyResponse:
        """
        @summary Creates a NAT firewall.
        
        @param request: CreateSecurityProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.nat_route_entry_list):
            query['NatRouteEntryList'] = request.nat_route_entry_list
        if not UtilClient.is_unset(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_auto):
            query['VswitchAuto'] = request.vswitch_auto
        if not UtilClient.is_unset(request.vswitch_cidr):
            query['VswitchCidr'] = request.vswitch_cidr
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityProxy',
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
            cloudfw_20171207_models.CreateSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_proxy_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateSecurityProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateSecurityProxyResponse:
        """
        @summary Creates a NAT firewall.
        
        @param request: CreateSecurityProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSecurityProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.nat_route_entry_list):
            query['NatRouteEntryList'] = request.nat_route_entry_list
        if not UtilClient.is_unset(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_auto):
            query['VswitchAuto'] = request.vswitch_auto
        if not UtilClient.is_unset(request.vswitch_cidr):
            query['VswitchCidr'] = request.vswitch_cidr
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityProxy',
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
            cloudfw_20171207_models.CreateSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_proxy(
        self,
        request: cloudfw_20171207_models.CreateSecurityProxyRequest,
    ) -> cloudfw_20171207_models.CreateSecurityProxyResponse:
        """
        @summary Creates a NAT firewall.
        
        @param request: CreateSecurityProxyRequest
        @return: CreateSecurityProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_security_proxy_with_options(request, runtime)

    async def create_security_proxy_async(
        self,
        request: cloudfw_20171207_models.CreateSecurityProxyRequest,
    ) -> cloudfw_20171207_models.CreateSecurityProxyResponse:
        """
        @summary Creates a NAT firewall.
        
        @param request: CreateSecurityProxyRequest
        @return: CreateSecurityProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_security_proxy_with_options_async(request, runtime)

    def create_sls_log_dispatch_with_options(
        self,
        request: cloudfw_20171207_models.CreateSlsLogDispatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateSlsLogDispatchResponse:
        """
        @summary 创建云防火墙SLS日志投递
        
        @param request: CreateSlsLogDispatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSlsLogDispatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sls_region_id):
            body['SlsRegionId'] = request.sls_region_id
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlsLogDispatch',
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
            cloudfw_20171207_models.CreateSlsLogDispatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sls_log_dispatch_with_options_async(
        self,
        request: cloudfw_20171207_models.CreateSlsLogDispatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateSlsLogDispatchResponse:
        """
        @summary 创建云防火墙SLS日志投递
        
        @param request: CreateSlsLogDispatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSlsLogDispatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sls_region_id):
            body['SlsRegionId'] = request.sls_region_id
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSlsLogDispatch',
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
            cloudfw_20171207_models.CreateSlsLogDispatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sls_log_dispatch(
        self,
        request: cloudfw_20171207_models.CreateSlsLogDispatchRequest,
    ) -> cloudfw_20171207_models.CreateSlsLogDispatchResponse:
        """
        @summary 创建云防火墙SLS日志投递
        
        @param request: CreateSlsLogDispatchRequest
        @return: CreateSlsLogDispatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sls_log_dispatch_with_options(request, runtime)

    async def create_sls_log_dispatch_async(
        self,
        request: cloudfw_20171207_models.CreateSlsLogDispatchRequest,
    ) -> cloudfw_20171207_models.CreateSlsLogDispatchResponse:
        """
        @summary 创建云防火墙SLS日志投递
        
        @param request: CreateSlsLogDispatchRequest
        @return: CreateSlsLogDispatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sls_log_dispatch_with_options_async(request, runtime)

    def create_tr_firewall_v2with_options(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2Response:
        """
        @summary Creates a virtual private cloud (VPC) firewall for a transit router.
        
        @param request: CreateTrFirewallV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrFirewallV2Response
        """
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
        if not UtilClient.is_unset(request.tr_attachment_master_zone):
            query['TrAttachmentMasterZone'] = request.tr_attachment_master_zone
        if not UtilClient.is_unset(request.tr_attachment_slave_cidr):
            query['TrAttachmentSlaveCidr'] = request.tr_attachment_slave_cidr
        if not UtilClient.is_unset(request.tr_attachment_slave_zone):
            query['TrAttachmentSlaveZone'] = request.tr_attachment_slave_zone
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
        """
        @summary Creates a virtual private cloud (VPC) firewall for a transit router.
        
        @param request: CreateTrFirewallV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrFirewallV2Response
        """
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
        if not UtilClient.is_unset(request.tr_attachment_master_zone):
            query['TrAttachmentMasterZone'] = request.tr_attachment_master_zone
        if not UtilClient.is_unset(request.tr_attachment_slave_cidr):
            query['TrAttachmentSlaveCidr'] = request.tr_attachment_slave_cidr
        if not UtilClient.is_unset(request.tr_attachment_slave_zone):
            query['TrAttachmentSlaveZone'] = request.tr_attachment_slave_zone
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
        """
        @summary Creates a virtual private cloud (VPC) firewall for a transit router.
        
        @param request: CreateTrFirewallV2Request
        @return: CreateTrFirewallV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tr_firewall_v2with_options(request, runtime)

    async def create_tr_firewall_v2_async(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2Request,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2Response:
        """
        @summary Creates a virtual private cloud (VPC) firewall for a transit router.
        
        @param request: CreateTrFirewallV2Request
        @return: CreateTrFirewallV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tr_firewall_v2with_options_async(request, runtime)

    def create_tr_firewall_v2route_policy_with_options(
        self,
        tmp_req: cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse:
        """
        @summary Creates a routing policy for a VPC firewall of a transit router.
        
        @param tmp_req: CreateTrFirewallV2RoutePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrFirewallV2RoutePolicyResponse
        """
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
        """
        @summary Creates a routing policy for a VPC firewall of a transit router.
        
        @param tmp_req: CreateTrFirewallV2RoutePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrFirewallV2RoutePolicyResponse
        """
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
        """
        @summary Creates a routing policy for a VPC firewall of a transit router.
        
        @param request: CreateTrFirewallV2RoutePolicyRequest
        @return: CreateTrFirewallV2RoutePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_tr_firewall_v2route_policy_with_options(request, runtime)

    async def create_tr_firewall_v2route_policy_async(
        self,
        request: cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyRequest,
    ) -> cloudfw_20171207_models.CreateTrFirewallV2RoutePolicyResponse:
        """
        @summary Creates a routing policy for a VPC firewall of a transit router.
        
        @param request: CreateTrFirewallV2RoutePolicyRequest
        @return: CreateTrFirewallV2RoutePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_tr_firewall_v2route_policy_with_options_async(request, runtime)

    def create_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.CreateVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.CreateVpcFirewallCenConfigureResponse:
        """
        @summary Creates a virtual private cloud (VPC) firewall to protect traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
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
        @summary Creates a virtual private cloud (VPC) firewall to protect traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
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
        @summary Creates a virtual private cloud (VPC) firewall to protect traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
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
        @summary Creates a virtual private cloud (VPC) firewall to protect traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the CreateVpcFirewallCenConfigure operation to create a VPC firewall. The VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. The VPC firewall cannot protect mutual access traffic between VBRs, between CCN instances, or between VBRs and CCN instances. For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
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
        @summary Creates a Virtual Private Cloud (VPC) firewall to protect traffic between two VPCs that are connected by using an Express Connect.
        
        @description You can call this operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
        ### [](#qps)QPS limit
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
        @summary Creates a Virtual Private Cloud (VPC) firewall to protect traffic between two VPCs that are connected by using an Express Connect.
        
        @description You can call this operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
        ### [](#qps)QPS limit
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
        @summary Creates a Virtual Private Cloud (VPC) firewall to protect traffic between two VPCs that are connected by using an Express Connect.
        
        @description You can call this operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
        ### [](#qps)QPS limit
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
        @summary Creates a Virtual Private Cloud (VPC) firewall to protect traffic between two VPCs that are connected by using an Express Connect.
        
        @description You can call this operation to create a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. The VPC firewall does not control the mutual access traffic between VPCs that reside in different regions or belong to different Alibaba Cloud accounts. The firewall also does not control the mutual access traffic between VPCs and virtual border routers (VBRs). For more information, see [VPC firewall limits](https://help.aliyun.com/document_detail/172295.html).
        ### [](#qps)QPS limit
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
        @summary Creates an access control policy in a specified policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Creates an access control policy in a specified policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Creates an access control policy in a specified policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        @summary Creates an access control policy in a specified policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the CreateVpcFirewallControlPolicy operation to create an access control policy in a specified policy group for a VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        @summary Deletes an address book for access control.
        
        @description You can call the DeleteAddressBook operation to delete an address book for access control.
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
        @summary Deletes an address book for access control.
        
        @description You can call the DeleteAddressBook operation to delete an address book for access control.
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
        @summary Deletes an address book for access control.
        
        @description You can call the DeleteAddressBook operation to delete an address book for access control.
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
        @summary Deletes an address book for access control.
        
        @description You can call the DeleteAddressBook operation to delete an address book for access control.
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
        @summary Deletes an access control policy.
        
        @description You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## [](#qps-)Limits
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
        @summary Deletes an access control policy.
        
        @description You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## [](#qps-)Limits
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
        @summary Deletes an access control policy.
        
        @description You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## [](#qps-)Limits
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
        @summary Deletes an access control policy.
        
        @description You can call the DeleteControlPolicy operation to delete an access control policy that applies to inbound or outbound traffic.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteControlPolicyRequest
        @return: DeleteControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_control_policy_template_with_options(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteControlPolicyTemplateResponse:
        """
        @summary Deletes an access control policy template.
        
        @param request: DeleteControlPolicyTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteControlPolicyTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicyTemplate',
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
            cloudfw_20171207_models.DeleteControlPolicyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_policy_template_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteControlPolicyTemplateResponse:
        """
        @summary Deletes an access control policy template.
        
        @param request: DeleteControlPolicyTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteControlPolicyTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicyTemplate',
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
            cloudfw_20171207_models.DeleteControlPolicyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_control_policy_template(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyTemplateRequest,
    ) -> cloudfw_20171207_models.DeleteControlPolicyTemplateResponse:
        """
        @summary Deletes an access control policy template.
        
        @param request: DeleteControlPolicyTemplateRequest
        @return: DeleteControlPolicyTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_template_with_options(request, runtime)

    async def delete_control_policy_template_async(
        self,
        request: cloudfw_20171207_models.DeleteControlPolicyTemplateRequest,
    ) -> cloudfw_20171207_models.DeleteControlPolicyTemplateResponse:
        """
        @summary Deletes an access control policy template.
        
        @param request: DeleteControlPolicyTemplateRequest
        @return: DeleteControlPolicyTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_control_policy_template_with_options_async(request, runtime)

    def delete_download_task_with_options(
        self,
        request: cloudfw_20171207_models.DeleteDownloadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteDownloadTaskResponse:
        """
        @summary Deletes file download tasks.
        
        @description You can call this operation to delete file download tasks and delete the files.
        *\
        *Warning** Both tasks and involved files are deleted. You can no longer download the involved files by using the download links. This operation is irreversible. Proceed with caution.
        
        @param request: DeleteDownloadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDownloadTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDownloadTask',
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
            cloudfw_20171207_models.DeleteDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_download_task_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteDownloadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteDownloadTaskResponse:
        """
        @summary Deletes file download tasks.
        
        @description You can call this operation to delete file download tasks and delete the files.
        *\
        *Warning** Both tasks and involved files are deleted. You can no longer download the involved files by using the download links. This operation is irreversible. Proceed with caution.
        
        @param request: DeleteDownloadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDownloadTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDownloadTask',
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
            cloudfw_20171207_models.DeleteDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_download_task(
        self,
        request: cloudfw_20171207_models.DeleteDownloadTaskRequest,
    ) -> cloudfw_20171207_models.DeleteDownloadTaskResponse:
        """
        @summary Deletes file download tasks.
        
        @description You can call this operation to delete file download tasks and delete the files.
        *\
        *Warning** Both tasks and involved files are deleted. You can no longer download the involved files by using the download links. This operation is irreversible. Proceed with caution.
        
        @param request: DeleteDownloadTaskRequest
        @return: DeleteDownloadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_download_task_with_options(request, runtime)

    async def delete_download_task_async(
        self,
        request: cloudfw_20171207_models.DeleteDownloadTaskRequest,
    ) -> cloudfw_20171207_models.DeleteDownloadTaskResponse:
        """
        @summary Deletes file download tasks.
        
        @description You can call this operation to delete file download tasks and delete the files.
        *\
        *Warning** Both tasks and involved files are deleted. You can no longer download the involved files by using the download links. This operation is irreversible. Proceed with caution.
        
        @param request: DeleteDownloadTaskRequest
        @return: DeleteDownloadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_download_task_with_options_async(request, runtime)

    def delete_firewall_v2route_policies_with_options(
        self,
        request: cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse:
        """
        @summary Deletes routing policies for a virtual private cloud (VPC) firewall of a transit router.
        
        @param request: DeleteFirewallV2RoutePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallV2RoutePoliciesResponse
        """
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
        """
        @summary Deletes routing policies for a virtual private cloud (VPC) firewall of a transit router.
        
        @param request: DeleteFirewallV2RoutePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFirewallV2RoutePoliciesResponse
        """
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
        """
        @summary Deletes routing policies for a virtual private cloud (VPC) firewall of a transit router.
        
        @param request: DeleteFirewallV2RoutePoliciesRequest
        @return: DeleteFirewallV2RoutePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_firewall_v2route_policies_with_options(request, runtime)

    async def delete_firewall_v2route_policies_async(
        self,
        request: cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesRequest,
    ) -> cloudfw_20171207_models.DeleteFirewallV2RoutePoliciesResponse:
        """
        @summary Deletes routing policies for a virtual private cloud (VPC) firewall of a transit router.
        
        @param request: DeleteFirewallV2RoutePoliciesRequest
        @return: DeleteFirewallV2RoutePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_firewall_v2route_policies_with_options_async(request, runtime)

    def delete_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.DeleteInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteInstanceMembersResponse:
        """
        @summary Removes members from Cloud Firewall.
        
        @description You can call this operation to remove up to 20 members from Cloud Firewall at a time. Separate multiple members with commas (,). After a member is removed, Cloud Firewall can no longer access the cloud resources of the member. Proceed with caution. Before you call this operation, call the [DescribeInstanceMembers](https://help.aliyun.com/document_detail/271704.html) operation to obtain the information about the members that are added to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Removes members from Cloud Firewall.
        
        @description You can call this operation to remove up to 20 members from Cloud Firewall at a time. Separate multiple members with commas (,). After a member is removed, Cloud Firewall can no longer access the cloud resources of the member. Proceed with caution. Before you call this operation, call the [DescribeInstanceMembers](https://help.aliyun.com/document_detail/271704.html) operation to obtain the information about the members that are added to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Removes members from Cloud Firewall.
        
        @description You can call this operation to remove up to 20 members from Cloud Firewall at a time. Separate multiple members with commas (,). After a member is removed, Cloud Firewall can no longer access the cloud resources of the member. Proceed with caution. Before you call this operation, call the [DescribeInstanceMembers](https://help.aliyun.com/document_detail/271704.html) operation to obtain the information about the members that are added to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Removes members from Cloud Firewall.
        
        @description You can call this operation to remove up to 20 members from Cloud Firewall at a time. Separate multiple members with commas (,). After a member is removed, Cloud Firewall can no longer access the cloud resources of the member. Proceed with caution. Before you call this operation, call the [DescribeInstanceMembers](https://help.aliyun.com/document_detail/271704.html) operation to obtain the information about the members that are added to Cloud Firewall.
        ## [](#qps-)Limits
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
        @summary Deletes an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
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
        @summary Deletes an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
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
        @summary Deletes an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
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
        @summary Deletes an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to delete an outbound access control policy that is created for a NAT firewall.
        
        @param request: DeleteNatFirewallControlPolicyRequest
        @return: DeleteNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_firewall_control_policy_with_options_async(request, runtime)

    def delete_nat_firewall_control_policy_batch_with_options(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchResponse:
        """
        @summary Deletes access control policies that are created for a NAT firewall at a time.
        
        @param request: DeleteNatFirewallControlPolicyBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNatFirewallControlPolicyBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
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
            action='DeleteNatFirewallControlPolicyBatch',
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
            cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nat_firewall_control_policy_batch_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchResponse:
        """
        @summary Deletes access control policies that are created for a NAT firewall at a time.
        
        @param request: DeleteNatFirewallControlPolicyBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNatFirewallControlPolicyBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
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
            action='DeleteNatFirewallControlPolicyBatch',
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
            cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nat_firewall_control_policy_batch(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchRequest,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchResponse:
        """
        @summary Deletes access control policies that are created for a NAT firewall at a time.
        
        @param request: DeleteNatFirewallControlPolicyBatchRequest
        @return: DeleteNatFirewallControlPolicyBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_firewall_control_policy_batch_with_options(request, runtime)

    async def delete_nat_firewall_control_policy_batch_async(
        self,
        request: cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchRequest,
    ) -> cloudfw_20171207_models.DeleteNatFirewallControlPolicyBatchResponse:
        """
        @summary Deletes access control policies that are created for a NAT firewall at a time.
        
        @param request: DeleteNatFirewallControlPolicyBatchRequest
        @return: DeleteNatFirewallControlPolicyBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_firewall_control_policy_batch_with_options_async(request, runtime)

    def delete_security_proxy_with_options(
        self,
        request: cloudfw_20171207_models.DeleteSecurityProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteSecurityProxyResponse:
        """
        @summary Deletes a NAT firewall.
        
        @param request: DeleteSecurityProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityProxy',
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
            cloudfw_20171207_models.DeleteSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_proxy_with_options_async(
        self,
        request: cloudfw_20171207_models.DeleteSecurityProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteSecurityProxyResponse:
        """
        @summary Deletes a NAT firewall.
        
        @param request: DeleteSecurityProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityProxy',
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
            cloudfw_20171207_models.DeleteSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_proxy(
        self,
        request: cloudfw_20171207_models.DeleteSecurityProxyRequest,
    ) -> cloudfw_20171207_models.DeleteSecurityProxyResponse:
        """
        @summary Deletes a NAT firewall.
        
        @param request: DeleteSecurityProxyRequest
        @return: DeleteSecurityProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_security_proxy_with_options(request, runtime)

    async def delete_security_proxy_async(
        self,
        request: cloudfw_20171207_models.DeleteSecurityProxyRequest,
    ) -> cloudfw_20171207_models.DeleteSecurityProxyResponse:
        """
        @summary Deletes a NAT firewall.
        
        @param request: DeleteSecurityProxyRequest
        @return: DeleteSecurityProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_proxy_with_options_async(request, runtime)

    def delete_tr_firewall_v2with_options(
        self,
        request: cloudfw_20171207_models.DeleteTrFirewallV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteTrFirewallV2Response:
        """
        @summary Deletes a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DeleteTrFirewallV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrFirewallV2Response
        """
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
        """
        @summary Deletes a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DeleteTrFirewallV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrFirewallV2Response
        """
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
        """
        @summary Deletes a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DeleteTrFirewallV2Request
        @return: DeleteTrFirewallV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tr_firewall_v2with_options(request, runtime)

    async def delete_tr_firewall_v2_async(
        self,
        request: cloudfw_20171207_models.DeleteTrFirewallV2Request,
    ) -> cloudfw_20171207_models.DeleteTrFirewallV2Response:
        """
        @summary Deletes a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DeleteTrFirewallV2Request
        @return: DeleteTrFirewallV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_tr_firewall_v2with_options_async(request, runtime)

    def delete_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.DeleteVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DeleteVpcFirewallCenConfigureResponse:
        """
        @summary Deletes a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Deletes a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Deletes a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Deletes a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DeleteVpcFirewallCenConfigure operation to delete a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Deletes a virtual private cloud (VPC) firewall that controls traffic between two VPCs. The VPCs are connected by using an Express Connect circuit.
        
        @description You can call the DeleteVpcFirewallConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Deletes a virtual private cloud (VPC) firewall that controls traffic between two VPCs. The VPCs are connected by using an Express Connect circuit.
        
        @description You can call the DeleteVpcFirewallConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Deletes a virtual private cloud (VPC) firewall that controls traffic between two VPCs. The VPCs are connected by using an Express Connect circuit.
        
        @description You can call the DeleteVpcFirewallConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Deletes a virtual private cloud (VPC) firewall that controls traffic between two VPCs. The VPCs are connected by using an Express Connect circuit.
        
        @description You can call the DeleteVpcFirewallConfigure operation to delete a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Deletes an access control policy from a specific policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
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
        @summary Deletes an access control policy from a specific policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
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
        @summary Deletes an access control policy from a specific policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
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
        @summary Deletes an access control policy from a specific policy group for a virtual private cloud (VPC) firewall.
        
        @description You can call the DeleteVpcFirewallControlPolicy operation to delete an access control policy from a specific policy group for a VPC firewall. Different access control policies are used for the VPC firewall that is used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewall that is used to protect each Express Connect circuit.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteVpcFirewallControlPolicyRequest
        @return: DeleteVpcFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_firewall_control_policy_with_options_async(request, runtime)

    def describe_aclprotect_trend_with_options(
        self,
        request: cloudfw_20171207_models.DescribeACLProtectTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeACLProtectTrendResponse:
        """
        @summary Queries the statistics on the requests that are blocked by the access control list (ACL) feature.
        
        @param request: DescribeACLProtectTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeACLProtectTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeACLProtectTrend',
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
            cloudfw_20171207_models.DescribeACLProtectTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aclprotect_trend_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeACLProtectTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeACLProtectTrendResponse:
        """
        @summary Queries the statistics on the requests that are blocked by the access control list (ACL) feature.
        
        @param request: DescribeACLProtectTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeACLProtectTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeACLProtectTrend',
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
            cloudfw_20171207_models.DescribeACLProtectTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aclprotect_trend(
        self,
        request: cloudfw_20171207_models.DescribeACLProtectTrendRequest,
    ) -> cloudfw_20171207_models.DescribeACLProtectTrendResponse:
        """
        @summary Queries the statistics on the requests that are blocked by the access control list (ACL) feature.
        
        @param request: DescribeACLProtectTrendRequest
        @return: DescribeACLProtectTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_aclprotect_trend_with_options(request, runtime)

    async def describe_aclprotect_trend_async(
        self,
        request: cloudfw_20171207_models.DescribeACLProtectTrendRequest,
    ) -> cloudfw_20171207_models.DescribeACLProtectTrendResponse:
        """
        @summary Queries the statistics on the requests that are blocked by the access control list (ACL) feature.
        
        @param request: DescribeACLProtectTrendRequest
        @return: DescribeACLProtectTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_aclprotect_trend_with_options_async(request, runtime)

    def describe_address_book_with_options(
        self,
        request: cloudfw_20171207_models.DescribeAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAddressBookResponse:
        """
        @summary Queries the details about an address book for an access control policy.
        
        @description You can call this operation to query the details about an address book for an access control policy.
        ## [](#qps)Limits
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
        @summary Queries the details about an address book for an access control policy.
        
        @description You can call this operation to query the details about an address book for an access control policy.
        ## [](#qps)Limits
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
        @summary Queries the details about an address book for an access control policy.
        
        @description You can call this operation to query the details about an address book for an access control policy.
        ## [](#qps)Limits
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
        @summary Queries the details about an address book for an access control policy.
        
        @description You can call this operation to query the details about an address book for an access control policy.
        ## [](#qps)Limits
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
        @summary Queries the assets that are protected by Cloud Firewall.
        
        @description You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
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
        if not UtilClient.is_unset(request.out_statistic):
            query['OutStatistic'] = request.out_statistic
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.sensitive_status):
            query['SensitiveStatus'] = request.sensitive_status
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
        @summary Queries the assets that are protected by Cloud Firewall.
        
        @description You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
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
        if not UtilClient.is_unset(request.out_statistic):
            query['OutStatistic'] = request.out_statistic
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.sensitive_status):
            query['SensitiveStatus'] = request.sensitive_status
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
        @summary Queries the assets that are protected by Cloud Firewall.
        
        @description You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
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
        @summary Queries the assets that are protected by Cloud Firewall.
        
        @description You can call the DescribeAssetList operation to query the assets that are protected by Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeAssetListRequest
        @return: DescribeAssetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_list_with_options_async(request, runtime)

    def describe_asset_risk_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeAssetRiskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetRiskListResponse:
        """
        @summary Queries the risk levels of assets.
        
        @param request: DescribeAssetRiskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetRiskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
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
            action='DescribeAssetRiskList',
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
            cloudfw_20171207_models.DescribeAssetRiskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_risk_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetRiskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetRiskListResponse:
        """
        @summary Queries the risk levels of assets.
        
        @param request: DescribeAssetRiskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetRiskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
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
            action='DescribeAssetRiskList',
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
            cloudfw_20171207_models.DescribeAssetRiskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_risk_list(
        self,
        request: cloudfw_20171207_models.DescribeAssetRiskListRequest,
    ) -> cloudfw_20171207_models.DescribeAssetRiskListResponse:
        """
        @summary Queries the risk levels of assets.
        
        @param request: DescribeAssetRiskListRequest
        @return: DescribeAssetRiskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_risk_list_with_options(request, runtime)

    async def describe_asset_risk_list_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetRiskListRequest,
    ) -> cloudfw_20171207_models.DescribeAssetRiskListResponse:
        """
        @summary Queries the risk levels of assets.
        
        @param request: DescribeAssetRiskListRequest
        @return: DescribeAssetRiskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_risk_list_with_options_async(request, runtime)

    def describe_asset_statistic_with_options(
        self,
        request: cloudfw_20171207_models.DescribeAssetStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetStatisticResponse:
        """
        @summary Queries statistics on the assets that are protected by Cloud Firewall.
        
        @param request: DescribeAssetStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetStatisticResponse
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
            action='DescribeAssetStatistic',
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
            cloudfw_20171207_models.DescribeAssetStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_statistic_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeAssetStatisticResponse:
        """
        @summary Queries statistics on the assets that are protected by Cloud Firewall.
        
        @param request: DescribeAssetStatisticRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAssetStatisticResponse
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
            action='DescribeAssetStatistic',
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
            cloudfw_20171207_models.DescribeAssetStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_statistic(
        self,
        request: cloudfw_20171207_models.DescribeAssetStatisticRequest,
    ) -> cloudfw_20171207_models.DescribeAssetStatisticResponse:
        """
        @summary Queries statistics on the assets that are protected by Cloud Firewall.
        
        @param request: DescribeAssetStatisticRequest
        @return: DescribeAssetStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_asset_statistic_with_options(request, runtime)

    async def describe_asset_statistic_async(
        self,
        request: cloudfw_20171207_models.DescribeAssetStatisticRequest,
    ) -> cloudfw_20171207_models.DescribeAssetStatisticResponse:
        """
        @summary Queries statistics on the assets that are protected by Cloud Firewall.
        
        @param request: DescribeAssetStatisticRequest
        @return: DescribeAssetStatisticResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_asset_statistic_with_options_async(request, runtime)

    def describe_cfw_risk_level_summary_with_options(
        self,
        request: cloudfw_20171207_models.DescribeCfwRiskLevelSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeCfwRiskLevelSummaryResponse:
        """
        @summary Queries the firewall risk level.
        
        @param request: DescribeCfwRiskLevelSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCfwRiskLevelSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCfwRiskLevelSummary',
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
            cloudfw_20171207_models.DescribeCfwRiskLevelSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cfw_risk_level_summary_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeCfwRiskLevelSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeCfwRiskLevelSummaryResponse:
        """
        @summary Queries the firewall risk level.
        
        @param request: DescribeCfwRiskLevelSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCfwRiskLevelSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCfwRiskLevelSummary',
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
            cloudfw_20171207_models.DescribeCfwRiskLevelSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cfw_risk_level_summary(
        self,
        request: cloudfw_20171207_models.DescribeCfwRiskLevelSummaryRequest,
    ) -> cloudfw_20171207_models.DescribeCfwRiskLevelSummaryResponse:
        """
        @summary Queries the firewall risk level.
        
        @param request: DescribeCfwRiskLevelSummaryRequest
        @return: DescribeCfwRiskLevelSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cfw_risk_level_summary_with_options(request, runtime)

    async def describe_cfw_risk_level_summary_async(
        self,
        request: cloudfw_20171207_models.DescribeCfwRiskLevelSummaryRequest,
    ) -> cloudfw_20171207_models.DescribeCfwRiskLevelSummaryResponse:
        """
        @summary Queries the firewall risk level.
        
        @param request: DescribeCfwRiskLevelSummaryRequest
        @return: DescribeCfwRiskLevelSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cfw_risk_level_summary_with_options_async(request, runtime)

    def describe_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeControlPolicyResponse:
        """
        @summary Queries the details about all access control policies.
        
        @description You can call the DescribeControlPolicy operation to query the details about access control policies by page.
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
        @summary Queries the details about all access control policies.
        
        @description You can call the DescribeControlPolicy operation to query the details about access control policies by page.
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
        @summary Queries the details about all access control policies.
        
        @description You can call the DescribeControlPolicy operation to query the details about access control policies by page.
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
        @summary Queries the details about all access control policies.
        
        @description You can call the DescribeControlPolicy operation to query the details about access control policies by page.
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
        """
        @summary Queries the default configurations of the intrusion prevention system (IPS).
        
        @param request: DescribeDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefaultIPSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        """
        @summary Queries the default configurations of the intrusion prevention system (IPS).
        
        @param request: DescribeDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDefaultIPSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
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
        """
        @summary Queries the default configurations of the intrusion prevention system (IPS).
        
        @param request: DescribeDefaultIPSConfigRequest
        @return: DescribeDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_default_ipsconfig_with_options(request, runtime)

    async def describe_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.DescribeDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.DescribeDefaultIPSConfigResponse:
        """
        @summary Queries the default configurations of the intrusion prevention system (IPS).
        
        @param request: DescribeDefaultIPSConfigRequest
        @return: DescribeDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_default_ipsconfig_with_options_async(request, runtime)

    def describe_domain_resolve_with_options(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        """
        @deprecated OpenAPI DescribeDomainResolve is deprecated
        
        @summary Queries Domain Name System (DNS) records.
        
        @description You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResolveResponse
        Deprecated
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
        @deprecated OpenAPI DescribeDomainResolve is deprecated
        
        @summary Queries Domain Name System (DNS) records.
        
        @description You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResolveResponse
        Deprecated
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
        @deprecated OpenAPI DescribeDomainResolve is deprecated
        
        @summary Queries Domain Name System (DNS) records.
        
        @description You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @return: DescribeDomainResolveResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resolve_with_options(request, runtime)

    async def describe_domain_resolve_async(
        self,
        request: cloudfw_20171207_models.DescribeDomainResolveRequest,
    ) -> cloudfw_20171207_models.DescribeDomainResolveResponse:
        """
        @deprecated OpenAPI DescribeDomainResolve is deprecated
        
        @summary Queries Domain Name System (DNS) records.
        
        @description You can use this operation to query the DNS record of a domain name. This operation can retrieve DNS records only from Alibaba Cloud DNS. Before you can call this operation, make sure that your domain name is hosted on Alibaba Cloud DNS.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeDomainResolveRequest
        @return: DescribeDomainResolveResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_resolve_with_options_async(request, runtime)

    def describe_download_task_with_options(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskResponse:
        """
        @summary Queries file download tasks, including the task information and download URLs.
        
        @param request: DescribeDownloadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadTask',
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
            cloudfw_20171207_models.DescribeDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_task_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskResponse:
        """
        @summary Queries file download tasks, including the task information and download URLs.
        
        @param request: DescribeDownloadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadTask',
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
            cloudfw_20171207_models.DescribeDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_task(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskRequest,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskResponse:
        """
        @summary Queries file download tasks, including the task information and download URLs.
        
        @param request: DescribeDownloadTaskRequest
        @return: DescribeDownloadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_task_with_options(request, runtime)

    async def describe_download_task_async(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskRequest,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskResponse:
        """
        @summary Queries file download tasks, including the task information and download URLs.
        
        @param request: DescribeDownloadTaskRequest
        @return: DescribeDownloadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_task_with_options_async(request, runtime)

    def describe_download_task_type_with_options(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskTypeResponse:
        """
        @summary Queries the types of download tasks. The type corresponds to the TaskType fields in the download task-related operations.
        
        @param request: DescribeDownloadTaskTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadTaskTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadTaskType',
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
            cloudfw_20171207_models.DescribeDownloadTaskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_task_type_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskTypeResponse:
        """
        @summary Queries the types of download tasks. The type corresponds to the TaskType fields in the download task-related operations.
        
        @param request: DescribeDownloadTaskTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDownloadTaskTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadTaskType',
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
            cloudfw_20171207_models.DescribeDownloadTaskTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_task_type(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskTypeRequest,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskTypeResponse:
        """
        @summary Queries the types of download tasks. The type corresponds to the TaskType fields in the download task-related operations.
        
        @param request: DescribeDownloadTaskTypeRequest
        @return: DescribeDownloadTaskTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_download_task_type_with_options(request, runtime)

    async def describe_download_task_type_async(
        self,
        request: cloudfw_20171207_models.DescribeDownloadTaskTypeRequest,
    ) -> cloudfw_20171207_models.DescribeDownloadTaskTypeResponse:
        """
        @summary Queries the types of download tasks. The type corresponds to the TaskType fields in the download task-related operations.
        
        @param request: DescribeDownloadTaskTypeRequest
        @return: DescribeDownloadTaskTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_task_type_with_options_async(request, runtime)

    def describe_instance_members_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInstanceMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInstanceMembersResponse:
        """
        @summary Queries the information about members in Cloud Firewall.
        
        @description You can use this operation to query the information about members in Cloud Firewall.
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
        @summary Queries the information about members in Cloud Firewall.
        
        @description You can use this operation to query the information about members in Cloud Firewall.
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
        @summary Queries the information about members in Cloud Firewall.
        
        @description You can use this operation to query the information about members in Cloud Firewall.
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
        @summary Queries the information about members in Cloud Firewall.
        
        @description You can use this operation to query the information about members in Cloud Firewall.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeInstanceMembersRequest
        @return: DescribeInstanceMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_members_with_options_async(request, runtime)

    def describe_instance_risk_levels_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInstanceRiskLevelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInstanceRiskLevelsResponse:
        """
        @summary Queries the risk levels of instances.
        
        @param request: DescribeInstanceRiskLevelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRiskLevelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRiskLevels',
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
            cloudfw_20171207_models.DescribeInstanceRiskLevelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_risk_levels_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeInstanceRiskLevelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInstanceRiskLevelsResponse:
        """
        @summary Queries the risk levels of instances.
        
        @param request: DescribeInstanceRiskLevelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRiskLevelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRiskLevels',
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
            cloudfw_20171207_models.DescribeInstanceRiskLevelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_risk_levels(
        self,
        request: cloudfw_20171207_models.DescribeInstanceRiskLevelsRequest,
    ) -> cloudfw_20171207_models.DescribeInstanceRiskLevelsResponse:
        """
        @summary Queries the risk levels of instances.
        
        @param request: DescribeInstanceRiskLevelsRequest
        @return: DescribeInstanceRiskLevelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_risk_levels_with_options(request, runtime)

    async def describe_instance_risk_levels_async(
        self,
        request: cloudfw_20171207_models.DescribeInstanceRiskLevelsRequest,
    ) -> cloudfw_20171207_models.DescribeInstanceRiskLevelsResponse:
        """
        @summary Queries the risk levels of instances.
        
        @param request: DescribeInstanceRiskLevelsRequest
        @return: DescribeInstanceRiskLevelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_risk_levels_with_options_async(request, runtime)

    def describe_internet_open_ip_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInternetOpenIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInternetOpenIpResponse:
        """
        @summary Queries the IP addresses that are open to the Internet.
        
        @param request: DescribeInternetOpenIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInternetOpenIpResponse
        """
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
        """
        @summary Queries the IP addresses that are open to the Internet.
        
        @param request: DescribeInternetOpenIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInternetOpenIpResponse
        """
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
        """
        @summary Queries the IP addresses that are open to the Internet.
        
        @param request: DescribeInternetOpenIpRequest
        @return: DescribeInternetOpenIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_internet_open_ip_with_options(request, runtime)

    async def describe_internet_open_ip_async(
        self,
        request: cloudfw_20171207_models.DescribeInternetOpenIpRequest,
    ) -> cloudfw_20171207_models.DescribeInternetOpenIpResponse:
        """
        @summary Queries the IP addresses that are open to the Internet.
        
        @param request: DescribeInternetOpenIpRequest
        @return: DescribeInternetOpenIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_internet_open_ip_with_options_async(request, runtime)

    def describe_internet_traffic_trend_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInternetTrafficTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInternetTrafficTrendResponse:
        """
        @summary Queries the trends of Internet traffic.
        
        @param request: DescribeInternetTrafficTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInternetTrafficTrendResponse
        """
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
        """
        @summary Queries the trends of Internet traffic.
        
        @param request: DescribeInternetTrafficTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInternetTrafficTrendResponse
        """
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
        """
        @summary Queries the trends of Internet traffic.
        
        @param request: DescribeInternetTrafficTrendRequest
        @return: DescribeInternetTrafficTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_internet_traffic_trend_with_options(request, runtime)

    async def describe_internet_traffic_trend_async(
        self,
        request: cloudfw_20171207_models.DescribeInternetTrafficTrendRequest,
    ) -> cloudfw_20171207_models.DescribeInternetTrafficTrendResponse:
        """
        @summary Queries the trends of Internet traffic.
        
        @param request: DescribeInternetTrafficTrendRequest
        @return: DescribeInternetTrafficTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_internet_traffic_trend_with_options_async(request, runtime)

    def describe_invade_event_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeInvadeEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeInvadeEventListResponse:
        """
        @summary Queries the information about the breach awareness events of a firewall.
        
        @param request: DescribeInvadeEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvadeEventListResponse
        """
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
        """
        @summary Queries the information about the breach awareness events of a firewall.
        
        @param request: DescribeInvadeEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvadeEventListResponse
        """
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
        """
        @summary Queries the information about the breach awareness events of a firewall.
        
        @param request: DescribeInvadeEventListRequest
        @return: DescribeInvadeEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_invade_event_list_with_options(request, runtime)

    async def describe_invade_event_list_async(
        self,
        request: cloudfw_20171207_models.DescribeInvadeEventListRequest,
    ) -> cloudfw_20171207_models.DescribeInvadeEventListResponse:
        """
        @summary Queries the information about the breach awareness events of a firewall.
        
        @param request: DescribeInvadeEventListRequest
        @return: DescribeInvadeEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_invade_event_list_with_options_async(request, runtime)

    def describe_nat_acl_page_status_with_options(
        self,
        request: cloudfw_20171207_models.DescribeNatAclPageStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatAclPageStatusResponse:
        """
        @summary Queries the pagination status of NAT firewalls.
        
        @param request: DescribeNatAclPageStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatAclPageStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatAclPageStatus',
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
            cloudfw_20171207_models.DescribeNatAclPageStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_acl_page_status_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeNatAclPageStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatAclPageStatusResponse:
        """
        @summary Queries the pagination status of NAT firewalls.
        
        @param request: DescribeNatAclPageStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatAclPageStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatAclPageStatus',
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
            cloudfw_20171207_models.DescribeNatAclPageStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_acl_page_status(
        self,
        request: cloudfw_20171207_models.DescribeNatAclPageStatusRequest,
    ) -> cloudfw_20171207_models.DescribeNatAclPageStatusResponse:
        """
        @summary Queries the pagination status of NAT firewalls.
        
        @param request: DescribeNatAclPageStatusRequest
        @return: DescribeNatAclPageStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_acl_page_status_with_options(request, runtime)

    async def describe_nat_acl_page_status_async(
        self,
        request: cloudfw_20171207_models.DescribeNatAclPageStatusRequest,
    ) -> cloudfw_20171207_models.DescribeNatAclPageStatusResponse:
        """
        @summary Queries the pagination status of NAT firewalls.
        
        @param request: DescribeNatAclPageStatusRequest
        @return: DescribeNatAclPageStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_acl_page_status_with_options_async(request, runtime)

    def describe_nat_firewall_control_policy_with_options(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallControlPolicyResponse:
        """
        @summary Queries the information about all access control policies that are created for NAT firewalls.
        
        @description You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
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
        @summary Queries the information about all access control policies that are created for NAT firewalls.
        
        @description You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
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
        @summary Queries the information about all access control policies that are created for NAT firewalls.
        
        @description You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
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
        @summary Queries the information about all access control policies that are created for NAT firewalls.
        
        @description You can use this operation to query the information about all access control policies that are created for NAT firewalls by page.
        
        @param request: DescribeNatFirewallControlPolicyRequest
        @return: DescribeNatFirewallControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_firewall_control_policy_with_options_async(request, runtime)

    def describe_nat_firewall_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallListResponse:
        """
        @summary Queries details of NAT firewalls.
        
        @param request: DescribeNatFirewallListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatFirewallListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatFirewallList',
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
            cloudfw_20171207_models.DescribeNatFirewallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_list_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallListResponse:
        """
        @summary Queries details of NAT firewalls.
        
        @param request: DescribeNatFirewallListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNatFirewallListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatFirewallList',
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
            cloudfw_20171207_models.DescribeNatFirewallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_list(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallListRequest,
    ) -> cloudfw_20171207_models.DescribeNatFirewallListResponse:
        """
        @summary Queries details of NAT firewalls.
        
        @param request: DescribeNatFirewallListRequest
        @return: DescribeNatFirewallListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_firewall_list_with_options(request, runtime)

    async def describe_nat_firewall_list_async(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallListRequest,
    ) -> cloudfw_20171207_models.DescribeNatFirewallListResponse:
        """
        @summary Queries details of NAT firewalls.
        
        @param request: DescribeNatFirewallListRequest
        @return: DescribeNatFirewallListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_firewall_list_with_options_async(request, runtime)

    def describe_nat_firewall_policy_prior_used_with_options(
        self,
        request: cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeNatFirewallPolicyPriorUsedResponse:
        """
        @summary Queries the priority range of access control policies that are created for a NAT firewall.
        
        @description You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
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
        @summary Queries the priority range of access control policies that are created for a NAT firewall.
        
        @description You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
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
        @summary Queries the priority range of access control policies that are created for a NAT firewall.
        
        @description You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
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
        @summary Queries the priority range of access control policies that are created for a NAT firewall.
        
        @description You can use this operation to query the priority range of access control policies that are created for a NAT firewall.
        
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
        """
        @summary Queries the information about the destination IP addresses in outbound connections.
        
        @param request: DescribeOutgoingDestinationIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOutgoingDestinationIPResponse
        """
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
        """
        @summary Queries the information about the destination IP addresses in outbound connections.
        
        @param request: DescribeOutgoingDestinationIPRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOutgoingDestinationIPResponse
        """
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
        """
        @summary Queries the information about the destination IP addresses in outbound connections.
        
        @param request: DescribeOutgoingDestinationIPRequest
        @return: DescribeOutgoingDestinationIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_outgoing_destination_ipwith_options(request, runtime)

    async def describe_outgoing_destination_ip_async(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDestinationIPRequest,
    ) -> cloudfw_20171207_models.DescribeOutgoingDestinationIPResponse:
        """
        @summary Queries the information about the destination IP addresses in outbound connections.
        
        @param request: DescribeOutgoingDestinationIPRequest
        @return: DescribeOutgoingDestinationIPResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_outgoing_destination_ipwith_options_async(request, runtime)

    def describe_outgoing_domain_with_options(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeOutgoingDomainResponse:
        """
        @summary Queries the information about the domain names in outbound connections.
        
        @param request: DescribeOutgoingDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOutgoingDomainResponse
        """
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
        """
        @summary Queries the information about the domain names in outbound connections.
        
        @param request: DescribeOutgoingDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOutgoingDomainResponse
        """
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
        """
        @summary Queries the information about the domain names in outbound connections.
        
        @param request: DescribeOutgoingDomainRequest
        @return: DescribeOutgoingDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_outgoing_domain_with_options(request, runtime)

    async def describe_outgoing_domain_async(
        self,
        request: cloudfw_20171207_models.DescribeOutgoingDomainRequest,
    ) -> cloudfw_20171207_models.DescribeOutgoingDomainResponse:
        """
        @summary Queries the information about the domain names in outbound connections.
        
        @param request: DescribeOutgoingDomainRequest
        @return: DescribeOutgoingDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_outgoing_domain_with_options_async(request, runtime)

    def describe_policy_advanced_config_with_options(
        self,
        request: cloudfw_20171207_models.DescribePolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePolicyAdvancedConfigResponse:
        """
        @summary Queries whether the strict mode is enabled for an access control policy.
        
        @description You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
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
        @summary Queries whether the strict mode is enabled for an access control policy.
        
        @description You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
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
        @summary Queries whether the strict mode is enabled for an access control policy.
        
        @description You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
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
        @summary Queries whether the strict mode is enabled for an access control policy.
        
        @description You can call the DescribePolicyAdvancedConfig operation to query whether the strict mode is enabled for an access control policy.
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
        @summary Queries the priority range of access control policies.
        
        @description You can call this operation to query the priority range of the access control policies that match specific query conditions.
        ## [](#qps-)Limits
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
        @summary Queries the priority range of access control policies.
        
        @description You can call this operation to query the priority range of the access control policies that match specific query conditions.
        ## [](#qps-)Limits
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
        @summary Queries the priority range of access control policies.
        
        @description You can call this operation to query the priority range of the access control policies that match specific query conditions.
        ## [](#qps-)Limits
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
        @summary Queries the priority range of access control policies.
        
        @description You can call this operation to query the priority range of the access control policies that match specific query conditions.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribePolicyPriorUsedRequest
        @return: DescribePolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_prior_used_with_options_async(request, runtime)

    def describe_postpay_traffic_detail_with_options(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficDetailResponse:
        """
        @summary Queries the details of traffic billed based on the pay-as-you-go billing method.
        
        @description If you use Cloud Firewall that uses the pay-as-you-go billing method, you can call this operation to query traffic details accurate to the granularity of specific resource instances. If you use Cloud Firewall that uses the subscription billing method, you can call this operation to query the overall traffic details.
        
        @param request: DescribePostpayTrafficDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePostpayTrafficDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePostpayTrafficDetail',
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
            cloudfw_20171207_models.DescribePostpayTrafficDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_traffic_detail_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficDetailResponse:
        """
        @summary Queries the details of traffic billed based on the pay-as-you-go billing method.
        
        @description If you use Cloud Firewall that uses the pay-as-you-go billing method, you can call this operation to query traffic details accurate to the granularity of specific resource instances. If you use Cloud Firewall that uses the subscription billing method, you can call this operation to query the overall traffic details.
        
        @param request: DescribePostpayTrafficDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePostpayTrafficDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.search_item):
            query['SearchItem'] = request.search_item
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePostpayTrafficDetail',
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
            cloudfw_20171207_models.DescribePostpayTrafficDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_traffic_detail(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficDetailRequest,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficDetailResponse:
        """
        @summary Queries the details of traffic billed based on the pay-as-you-go billing method.
        
        @description If you use Cloud Firewall that uses the pay-as-you-go billing method, you can call this operation to query traffic details accurate to the granularity of specific resource instances. If you use Cloud Firewall that uses the subscription billing method, you can call this operation to query the overall traffic details.
        
        @param request: DescribePostpayTrafficDetailRequest
        @return: DescribePostpayTrafficDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_postpay_traffic_detail_with_options(request, runtime)

    async def describe_postpay_traffic_detail_async(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficDetailRequest,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficDetailResponse:
        """
        @summary Queries the details of traffic billed based on the pay-as-you-go billing method.
        
        @description If you use Cloud Firewall that uses the pay-as-you-go billing method, you can call this operation to query traffic details accurate to the granularity of specific resource instances. If you use Cloud Firewall that uses the subscription billing method, you can call this operation to query the overall traffic details.
        
        @param request: DescribePostpayTrafficDetailRequest
        @return: DescribePostpayTrafficDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_postpay_traffic_detail_with_options_async(request, runtime)

    def describe_postpay_traffic_total_with_options(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficTotalResponse:
        """
        @summary Queries the total volume of traffic that is billed based on the pay-as-you-go billing method, including all firewalls within the current account.
        
        @description You can call this operation to query statistics of the current Cloud Firewall from the date of purchase.
        
        @param request: DescribePostpayTrafficTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePostpayTrafficTotalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePostpayTrafficTotal',
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
            cloudfw_20171207_models.DescribePostpayTrafficTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_traffic_total_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficTotalResponse:
        """
        @summary Queries the total volume of traffic that is billed based on the pay-as-you-go billing method, including all firewalls within the current account.
        
        @description You can call this operation to query statistics of the current Cloud Firewall from the date of purchase.
        
        @param request: DescribePostpayTrafficTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePostpayTrafficTotalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePostpayTrafficTotal',
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
            cloudfw_20171207_models.DescribePostpayTrafficTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_traffic_total(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficTotalRequest,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficTotalResponse:
        """
        @summary Queries the total volume of traffic that is billed based on the pay-as-you-go billing method, including all firewalls within the current account.
        
        @description You can call this operation to query statistics of the current Cloud Firewall from the date of purchase.
        
        @param request: DescribePostpayTrafficTotalRequest
        @return: DescribePostpayTrafficTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_postpay_traffic_total_with_options(request, runtime)

    async def describe_postpay_traffic_total_async(
        self,
        request: cloudfw_20171207_models.DescribePostpayTrafficTotalRequest,
    ) -> cloudfw_20171207_models.DescribePostpayTrafficTotalResponse:
        """
        @summary Queries the total volume of traffic that is billed based on the pay-as-you-go billing method, including all firewalls within the current account.
        
        @description You can call this operation to query statistics of the current Cloud Firewall from the date of purchase.
        
        @param request: DescribePostpayTrafficTotalRequest
        @return: DescribePostpayTrafficTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_postpay_traffic_total_with_options_async(request, runtime)

    def describe_prefix_lists_with_options(
        self,
        request: cloudfw_20171207_models.DescribePrefixListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePrefixListsResponse:
        """
        @summary Queries prefix lists.
        
        @param request: DescribePrefixListsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrefixListsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrefixLists',
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
            cloudfw_20171207_models.DescribePrefixListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prefix_lists_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribePrefixListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribePrefixListsResponse:
        """
        @summary Queries prefix lists.
        
        @param request: DescribePrefixListsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePrefixListsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrefixLists',
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
            cloudfw_20171207_models.DescribePrefixListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prefix_lists(
        self,
        request: cloudfw_20171207_models.DescribePrefixListsRequest,
    ) -> cloudfw_20171207_models.DescribePrefixListsResponse:
        """
        @summary Queries prefix lists.
        
        @param request: DescribePrefixListsRequest
        @return: DescribePrefixListsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_prefix_lists_with_options(request, runtime)

    async def describe_prefix_lists_async(
        self,
        request: cloudfw_20171207_models.DescribePrefixListsRequest,
    ) -> cloudfw_20171207_models.DescribePrefixListsResponse:
        """
        @summary Queries prefix lists.
        
        @param request: DescribePrefixListsRequest
        @return: DescribePrefixListsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_prefix_lists_with_options_async(request, runtime)

    def describe_risk_event_group_with_options(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeRiskEventGroupResponse:
        """
        @summary Queries the details of intrusion events.
        
        @description You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
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
        if not UtilClient.is_unset(request.is_only_private_assoc):
            query['IsOnlyPrivateAssoc'] = request.is_only_private_assoc
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
        @summary Queries the details of intrusion events.
        
        @description You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
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
        if not UtilClient.is_unset(request.is_only_private_assoc):
            query['IsOnlyPrivateAssoc'] = request.is_only_private_assoc
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
        @summary Queries the details of intrusion events.
        
        @description You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
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
        @summary Queries the details of intrusion events.
        
        @description You can call the DescribeRiskEventGroup operation to query and download the details of intrusion events. We recommend that you query the details of 5 to 10 intrusion events at a time. If you do not need to query the geographical information about IP addresses, you can set the NoLocation parameter to true to prevent query timeout.
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
        """
        @summary Queries the attack payloads of intrusion events.
        
        @param request: DescribeRiskEventPayloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRiskEventPayloadResponse
        """
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
        """
        @summary Queries the attack payloads of intrusion events.
        
        @param request: DescribeRiskEventPayloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRiskEventPayloadResponse
        """
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
        """
        @summary Queries the attack payloads of intrusion events.
        
        @param request: DescribeRiskEventPayloadRequest
        @return: DescribeRiskEventPayloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_event_payload_with_options(request, runtime)

    async def describe_risk_event_payload_async(
        self,
        request: cloudfw_20171207_models.DescribeRiskEventPayloadRequest,
    ) -> cloudfw_20171207_models.DescribeRiskEventPayloadResponse:
        """
        @summary Queries the attack payloads of intrusion events.
        
        @param request: DescribeRiskEventPayloadRequest
        @return: DescribeRiskEventPayloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_event_payload_with_options_async(request, runtime)

    def describe_signature_lib_version_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeSignatureLibVersionResponse:
        """
        @summary Queries the information about signature library versions.
        
        @param request: DescribeSignatureLibVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSignatureLibVersionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSignatureLibVersion',
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
            cloudfw_20171207_models.DescribeSignatureLibVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_signature_lib_version_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeSignatureLibVersionResponse:
        """
        @summary Queries the information about signature library versions.
        
        @param request: DescribeSignatureLibVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSignatureLibVersionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSignatureLibVersion',
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
            cloudfw_20171207_models.DescribeSignatureLibVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_signature_lib_version(self) -> cloudfw_20171207_models.DescribeSignatureLibVersionResponse:
        """
        @summary Queries the information about signature library versions.
        
        @return: DescribeSignatureLibVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_signature_lib_version_with_options(runtime)

    async def describe_signature_lib_version_async(self) -> cloudfw_20171207_models.DescribeSignatureLibVersionResponse:
        """
        @summary Queries the information about signature library versions.
        
        @return: DescribeSignatureLibVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_signature_lib_version_with_options_async(runtime)

    def describe_tr_firewall_policy_back_up_association_list_with_options(
        self,
        tmp_req: cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        """
        @summary Queries information about the transit routers that are associated with a virtual private cloud (VPC) firewall created for a transit router.
        
        @param tmp_req: DescribeTrFirewallPolicyBackUpAssociationListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallPolicyBackUpAssociationListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.candidate_list):
            request.candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.candidate_list, 'CandidateList', 'json')
        query = {}
        if not UtilClient.is_unset(request.candidate_list_shrink):
            query['CandidateList'] = request.candidate_list_shrink
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
        tmp_req: cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        """
        @summary Queries information about the transit routers that are associated with a virtual private cloud (VPC) firewall created for a transit router.
        
        @param tmp_req: DescribeTrFirewallPolicyBackUpAssociationListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallPolicyBackUpAssociationListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.candidate_list):
            request.candidate_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.candidate_list, 'CandidateList', 'json')
        query = {}
        if not UtilClient.is_unset(request.candidate_list_shrink):
            query['CandidateList'] = request.candidate_list_shrink
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
        """
        @summary Queries information about the transit routers that are associated with a virtual private cloud (VPC) firewall created for a transit router.
        
        @param request: DescribeTrFirewallPolicyBackUpAssociationListRequest
        @return: DescribeTrFirewallPolicyBackUpAssociationListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewall_policy_back_up_association_list_with_options(request, runtime)

    async def describe_tr_firewall_policy_back_up_association_list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        """
        @summary Queries information about the transit routers that are associated with a virtual private cloud (VPC) firewall created for a transit router.
        
        @param request: DescribeTrFirewallPolicyBackUpAssociationListRequest
        @return: DescribeTrFirewallPolicyBackUpAssociationListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewall_policy_back_up_association_list_with_options_async(request, runtime)

    def describe_tr_firewall_v2route_policy_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse:
        """
        @summary Queries the routing policies of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DescribeTrFirewallV2RoutePolicyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallV2RoutePolicyListResponse
        """
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
        """
        @summary Queries the routing policies of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DescribeTrFirewallV2RoutePolicyListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallV2RoutePolicyListResponse
        """
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
        """
        @summary Queries the routing policies of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DescribeTrFirewallV2RoutePolicyListRequest
        @return: DescribeTrFirewallV2RoutePolicyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewall_v2route_policy_list_with_options(request, runtime)

    async def describe_tr_firewall_v2route_policy_list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallV2RoutePolicyListResponse:
        """
        @summary Queries the routing policies of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: DescribeTrFirewallV2RoutePolicyListRequest
        @return: DescribeTrFirewallV2RoutePolicyListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewall_v2route_policy_list_with_options_async(request, runtime)

    def describe_tr_firewalls_v2detail_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2DetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse:
        """
        @summary Queries the details of the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2DetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallsV2DetailResponse
        """
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
        """
        @summary Queries the details of the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2DetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallsV2DetailResponse
        """
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
        """
        @summary Queries the details of the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2DetailRequest
        @return: DescribeTrFirewallsV2DetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewalls_v2detail_with_options(request, runtime)

    async def describe_tr_firewalls_v2detail_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2DetailRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2DetailResponse:
        """
        @summary Queries the details of the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2DetailRequest
        @return: DescribeTrFirewallsV2DetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewalls_v2detail_with_options_async(request, runtime)

    def describe_tr_firewalls_v2list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2ListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse:
        """
        @summary Queries the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2ListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallsV2ListResponse
        """
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
        """
        @summary Queries the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2ListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallsV2ListResponse
        """
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
        """
        @summary Queries the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2ListRequest
        @return: DescribeTrFirewallsV2ListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewalls_v2list_with_options(request, runtime)

    async def describe_tr_firewalls_v2list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2ListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2ListResponse:
        """
        @summary Queries the virtual private cloud (VPC) firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2ListRequest
        @return: DescribeTrFirewallsV2ListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewalls_v2list_with_options_async(request, runtime)

    def describe_tr_firewalls_v2route_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2RouteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse:
        """
        @summary Queries the route tables of the VPC firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2RouteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallsV2RouteListResponse
        """
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
        """
        @summary Queries the route tables of the VPC firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2RouteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrFirewallsV2RouteListResponse
        """
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
        """
        @summary Queries the route tables of the VPC firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2RouteListRequest
        @return: DescribeTrFirewallsV2RouteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tr_firewalls_v2route_list_with_options(request, runtime)

    async def describe_tr_firewalls_v2route_list_async(
        self,
        request: cloudfw_20171207_models.DescribeTrFirewallsV2RouteListRequest,
    ) -> cloudfw_20171207_models.DescribeTrFirewallsV2RouteListResponse:
        """
        @summary Queries the route tables of the VPC firewalls that are created for transit routers.
        
        @param request: DescribeTrFirewallsV2RouteListRequest
        @return: DescribeTrFirewallsV2RouteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_tr_firewalls_v2route_list_with_options_async(request, runtime)

    def describe_user_asset_iptraffic_info_with_options(
        self,
        request: cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse:
        """
        @summary Queries the information about the traffic of a specified asset that belongs to your Alibaba Cloud account.
        
        @param request: DescribeUserAssetIPTrafficInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserAssetIPTrafficInfoResponse
        """
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
        """
        @summary Queries the information about the traffic of a specified asset that belongs to your Alibaba Cloud account.
        
        @param request: DescribeUserAssetIPTrafficInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserAssetIPTrafficInfoResponse
        """
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
        """
        @summary Queries the information about the traffic of a specified asset that belongs to your Alibaba Cloud account.
        
        @param request: DescribeUserAssetIPTrafficInfoRequest
        @return: DescribeUserAssetIPTrafficInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_asset_iptraffic_info_with_options(request, runtime)

    async def describe_user_asset_iptraffic_info_async(
        self,
        request: cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoRequest,
    ) -> cloudfw_20171207_models.DescribeUserAssetIPTrafficInfoResponse:
        """
        @summary Queries the information about the traffic of a specified asset that belongs to your Alibaba Cloud account.
        
        @param request: DescribeUserAssetIPTrafficInfoRequest
        @return: DescribeUserAssetIPTrafficInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_asset_iptraffic_info_with_options_async(request, runtime)

    def describe_user_buy_version_with_options(
        self,
        request: cloudfw_20171207_models.DescribeUserBuyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserBuyVersionResponse:
        """
        @summary Queries the edition information about Cloud Firewall.
        
        @description You can call this operation to query the edition information about Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeUserBuyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserBuyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBuyVersion',
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
            cloudfw_20171207_models.DescribeUserBuyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_buy_version_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeUserBuyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserBuyVersionResponse:
        """
        @summary Queries the edition information about Cloud Firewall.
        
        @description You can call this operation to query the edition information about Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeUserBuyVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserBuyVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBuyVersion',
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
            cloudfw_20171207_models.DescribeUserBuyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_buy_version(
        self,
        request: cloudfw_20171207_models.DescribeUserBuyVersionRequest,
    ) -> cloudfw_20171207_models.DescribeUserBuyVersionResponse:
        """
        @summary Queries the edition information about Cloud Firewall.
        
        @description You can call this operation to query the edition information about Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeUserBuyVersionRequest
        @return: DescribeUserBuyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_buy_version_with_options(request, runtime)

    async def describe_user_buy_version_async(
        self,
        request: cloudfw_20171207_models.DescribeUserBuyVersionRequest,
    ) -> cloudfw_20171207_models.DescribeUserBuyVersionResponse:
        """
        @summary Queries the edition information about Cloud Firewall.
        
        @description You can call this operation to query the edition information about Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeUserBuyVersionRequest
        @return: DescribeUserBuyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_buy_version_with_options_async(request, runtime)

    def describe_user_ipswhitelist_with_options(
        self,
        request: cloudfw_20171207_models.DescribeUserIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeUserIPSWhitelistResponse:
        """
        @summary 获取用户IPS白名单
        
        @param request: DescribeUserIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserIPSWhitelistResponse
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
        """
        @summary 获取用户IPS白名单
        
        @param request: DescribeUserIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserIPSWhitelistResponse
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
        """
        @summary 获取用户IPS白名单
        
        @param request: DescribeUserIPSWhitelistRequest
        @return: DescribeUserIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_ipswhitelist_with_options(request, runtime)

    async def describe_user_ipswhitelist_async(
        self,
        request: cloudfw_20171207_models.DescribeUserIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.DescribeUserIPSWhitelistResponse:
        """
        @summary 获取用户IPS白名单
        
        @param request: DescribeUserIPSWhitelistRequest
        @return: DescribeUserIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_ipswhitelist_with_options_async(request, runtime)

    def describe_vpc_firewall_acl_group_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallAclGroupListResponse:
        """
        @summary Queries the information about all policy groups of access control policies that are created for virtual private cloud (VPC) firewalls.
        
        @description You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
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
        @summary Queries the information about all policy groups of access control policies that are created for virtual private cloud (VPC) firewalls.
        
        @description You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
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
        @summary Queries the information about all policy groups of access control policies that are created for virtual private cloud (VPC) firewalls.
        
        @description You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
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
        @summary Queries the information about all policy groups of access control policies that are created for virtual private cloud (VPC) firewalls.
        
        @description You can call the DescribeVpcFirewallAclGroupList operation to query the information about all policy groups of access control policies that are created for VPC firewalls.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall protects access traffic between a VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall protects access traffic between a VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall protects access traffic between a VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall protects access traffic between a VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenDetail operation to query the details about a VPC firewall. The VPC firewall protects access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries virtual private cloud (VPC) firewalls. Each VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries virtual private cloud (VPC) firewalls. Each VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries virtual private cloud (VPC) firewalls. Each VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries virtual private cloud (VPC) firewalls. Each VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the DescribeVpcFirewallCenList operation to query VPC firewalls. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance.
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
        @summary Queries the information about the access control policies for a specified virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        @summary Queries the information about the access control policies for a specified virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        @summary Queries the information about the access control policies for a specified virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        @summary Queries the information about the access control policies for a specified virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallControlPolicy operation to query the information about all access control policies that are created for a specified VPC firewall. Different access control policies are used when a VPC firewall is used to protect traffic between two VPCs that are connected by using a Cloud Enterprise Network (CEN) instance or an Express Connect circuit.
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
        @summary Queries the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
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
        @summary Queries the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
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
        @summary Queries the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
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
        @summary Queries the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call the DescribeVpcFirewallDefaultIPSConfig operation to query the intrusion prevention configurations of a VPC firewall.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
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
        @summary Queries the details about a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallDetail operation to query the details about a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://www.alibabacloud.com/help/en/cloud-firewall/latest/createvpcfirewallconfigure) operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallDetailRequest
        @return: DescribeVpcFirewallDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_ipswhitelist_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistResponse:
        """
        @summary Queries the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: DescribeVpcFirewallIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallIPSWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeVpcFirewallIPSWhitelist',
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
            cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_ipswhitelist_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistResponse:
        """
        @summary Queries the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: DescribeVpcFirewallIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcFirewallIPSWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='DescribeVpcFirewallIPSWhitelist',
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
            cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_ipswhitelist(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistResponse:
        """
        @summary Queries the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: DescribeVpcFirewallIPSWhitelistRequest
        @return: DescribeVpcFirewallIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_firewall_ipswhitelist_with_options(request, runtime)

    async def describe_vpc_firewall_ipswhitelist_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallIPSWhitelistResponse:
        """
        @summary Queries the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: DescribeVpcFirewallIPSWhitelistRequest
        @return: DescribeVpcFirewallIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_ipswhitelist_with_options_async(request, runtime)

    def describe_vpc_firewall_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcFirewallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcFirewallListResponse:
        """
        @summary Queries the details about virtual private cloud (VPC) firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
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
        @summary Queries the details about virtual private cloud (VPC) firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
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
        @summary Queries the details about virtual private cloud (VPC) firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
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
        @summary Queries the details about virtual private cloud (VPC) firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the DescribeVpcFirewallList operation to query the details about VPC firewalls by page. Each VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
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
        @summary Queries the priority range of access control policies that are created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call this operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## [](#qps-)Limits
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
        @summary Queries the priority range of access control policies that are created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call this operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## [](#qps-)Limits
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
        @summary Queries the priority range of access control policies that are created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call this operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## [](#qps-)Limits
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
        @summary Queries the priority range of access control policies that are created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call this operation to query the priority range of access control policies that are created for a VPC firewall in a specific policy group.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeVpcFirewallPolicyPriorUsedRequest
        @return: DescribeVpcFirewallPolicyPriorUsedResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_firewall_policy_prior_used_with_options_async(request, runtime)

    def describe_vpc_list_lite_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcListLiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcListLiteResponse:
        """
        @summary Queries virtual private clouds (VPCs).
        
        @param request: DescribeVpcListLiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcListLiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcListLite',
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
            cloudfw_20171207_models.DescribeVpcListLiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_list_lite_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcListLiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcListLiteResponse:
        """
        @summary Queries virtual private clouds (VPCs).
        
        @param request: DescribeVpcListLiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcListLiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcListLite',
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
            cloudfw_20171207_models.DescribeVpcListLiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_list_lite(
        self,
        request: cloudfw_20171207_models.DescribeVpcListLiteRequest,
    ) -> cloudfw_20171207_models.DescribeVpcListLiteResponse:
        """
        @summary Queries virtual private clouds (VPCs).
        
        @param request: DescribeVpcListLiteRequest
        @return: DescribeVpcListLiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_list_lite_with_options(request, runtime)

    async def describe_vpc_list_lite_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcListLiteRequest,
    ) -> cloudfw_20171207_models.DescribeVpcListLiteResponse:
        """
        @summary Queries virtual private clouds (VPCs).
        
        @param request: DescribeVpcListLiteRequest
        @return: DescribeVpcListLiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_list_lite_with_options_async(request, runtime)

    def describe_vpc_zone_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVpcZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcZoneResponse:
        """
        @summary Queries virtual private cloud (VPC) zones.
        
        @param request: DescribeVpcZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcZone',
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
            cloudfw_20171207_models.DescribeVpcZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_zone_with_options_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVpcZoneResponse:
        """
        @summary Queries virtual private cloud (VPC) zones.
        
        @param request: DescribeVpcZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['Environment'] = request.environment
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVpcZone',
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
            cloudfw_20171207_models.DescribeVpcZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_zone(
        self,
        request: cloudfw_20171207_models.DescribeVpcZoneRequest,
    ) -> cloudfw_20171207_models.DescribeVpcZoneResponse:
        """
        @summary Queries virtual private cloud (VPC) zones.
        
        @param request: DescribeVpcZoneRequest
        @return: DescribeVpcZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_zone_with_options(request, runtime)

    async def describe_vpc_zone_async(
        self,
        request: cloudfw_20171207_models.DescribeVpcZoneRequest,
    ) -> cloudfw_20171207_models.DescribeVpcZoneResponse:
        """
        @summary Queries virtual private cloud (VPC) zones.
        
        @param request: DescribeVpcZoneRequest
        @return: DescribeVpcZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_zone_with_options_async(request, runtime)

    def describe_vulnerability_protected_list_with_options(
        self,
        request: cloudfw_20171207_models.DescribeVulnerabilityProtectedListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse:
        """
        @summary Queries the vulnerabilities that are supported by Cloud Firewall.
        
        @param request: DescribeVulnerabilityProtectedListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVulnerabilityProtectedListResponse
        """
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
        """
        @summary Queries the vulnerabilities that are supported by Cloud Firewall.
        
        @param request: DescribeVulnerabilityProtectedListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVulnerabilityProtectedListResponse
        """
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
        """
        @summary Queries the vulnerabilities that are supported by Cloud Firewall.
        
        @param request: DescribeVulnerabilityProtectedListRequest
        @return: DescribeVulnerabilityProtectedListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vulnerability_protected_list_with_options(request, runtime)

    async def describe_vulnerability_protected_list_async(
        self,
        request: cloudfw_20171207_models.DescribeVulnerabilityProtectedListRequest,
    ) -> cloudfw_20171207_models.DescribeVulnerabilityProtectedListResponse:
        """
        @summary Queries the vulnerabilities that are supported by Cloud Firewall.
        
        @param request: DescribeVulnerabilityProtectedListRequest
        @return: DescribeVulnerabilityProtectedListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vulnerability_protected_list_with_options_async(request, runtime)

    def modify_address_book_with_options(
        self,
        request: cloudfw_20171207_models.ModifyAddressBookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyAddressBookResponse:
        """
        @summary Modifies the address book that is specified in an access control policy.
        
        @description You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
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
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
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
        @summary Modifies the address book that is specified in an access control policy.
        
        @description You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
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
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
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
        @summary Modifies the address book that is specified in an access control policy.
        
        @description You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
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
        @summary Modifies the address book that is specified in an access control policy.
        
        @description You can call the ModifyAddressBook operation to modify the address book that is configured for access control.
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
        @summary Modifies the configurations of an access control policy.
        
        @description You can call this operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## [](#qps)Limit
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Modifies the configurations of an access control policy.
        
        @description You can call this operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## [](#qps)Limit
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Modifies the configurations of an access control policy.
        
        @description You can call this operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## [](#qps)Limit
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
        @summary Modifies the configurations of an access control policy.
        
        @description You can call this operation to modify the configurations of an access control policy. The policy allows Cloud Firewall to allow, deny, or monitor the traffic that passes through Cloud Firewall.
        ## [](#qps)Limit
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
        @summary Modifies the priority of an IPv4 access control policy for the Internet firewall. An IPv4 access control policy refers to a policy whose source IP address and destination IP address are IPv4 addresses.
        
        @description You can use this operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## [](#qps)Limits
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
        @summary Modifies the priority of an IPv4 access control policy for the Internet firewall. An IPv4 access control policy refers to a policy whose source IP address and destination IP address are IPv4 addresses.
        
        @description You can use this operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## [](#qps)Limits
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
        @summary Modifies the priority of an IPv4 access control policy for the Internet firewall. An IPv4 access control policy refers to a policy whose source IP address and destination IP address are IPv4 addresses.
        
        @description You can use this operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## [](#qps)Limits
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
        @summary Modifies the priority of an IPv4 access control policy for the Internet firewall. An IPv4 access control policy refers to a policy whose source IP address and destination IP address are IPv4 addresses.
        
        @description You can use this operation to modify the priority of an IPv4 access control policy for the Internet firewall. No API operations are provided for you to modify the priority of an IPv6 access control policy for the Internet firewall.
        ## [](#qps)Limits
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
        """
        @summary Modifies the default configuration of the intrusion prevention system (IPS).
        
        @param request: ModifyDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefaultIPSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not UtilClient.is_unset(request.cti_rules):
            query['CtiRules'] = request.cti_rules
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_sdl):
            query['MaxSdl'] = request.max_sdl
        if not UtilClient.is_unset(request.patch_rules):
            query['PatchRules'] = request.patch_rules
        if not UtilClient.is_unset(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
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
        """
        @summary Modifies the default configuration of the intrusion prevention system (IPS).
        
        @param request: ModifyDefaultIPSConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDefaultIPSConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not UtilClient.is_unset(request.cti_rules):
            query['CtiRules'] = request.cti_rules
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_sdl):
            query['MaxSdl'] = request.max_sdl
        if not UtilClient.is_unset(request.patch_rules):
            query['PatchRules'] = request.patch_rules
        if not UtilClient.is_unset(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not UtilClient.is_unset(request.run_mode):
            query['RunMode'] = request.run_mode
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
        """
        @summary Modifies the default configuration of the intrusion prevention system (IPS).
        
        @param request: ModifyDefaultIPSConfigRequest
        @return: ModifyDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_default_ipsconfig_with_options(request, runtime)

    async def modify_default_ipsconfig_async(
        self,
        request: cloudfw_20171207_models.ModifyDefaultIPSConfigRequest,
    ) -> cloudfw_20171207_models.ModifyDefaultIPSConfigResponse:
        """
        @summary Modifies the default configuration of the intrusion prevention system (IPS).
        
        @param request: ModifyDefaultIPSConfigRequest
        @return: ModifyDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_default_ipsconfig_with_options_async(request, runtime)

    def modify_firewall_v2route_policy_switch_with_options(
        self,
        request: cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse:
        """
        @summary Modifies the status of a routing policy.
        
        @param request: ModifyFirewallV2RoutePolicySwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirewallV2RoutePolicySwitchResponse
        """
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
        """
        @summary Modifies the status of a routing policy.
        
        @param request: ModifyFirewallV2RoutePolicySwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFirewallV2RoutePolicySwitchResponse
        """
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
        """
        @summary Modifies the status of a routing policy.
        
        @param request: ModifyFirewallV2RoutePolicySwitchRequest
        @return: ModifyFirewallV2RoutePolicySwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_firewall_v2route_policy_switch_with_options(request, runtime)

    async def modify_firewall_v2route_policy_switch_async(
        self,
        request: cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchRequest,
    ) -> cloudfw_20171207_models.ModifyFirewallV2RoutePolicySwitchResponse:
        """
        @summary Modifies the status of a routing policy.
        
        @param request: ModifyFirewallV2RoutePolicySwitchRequest
        @return: ModifyFirewallV2RoutePolicySwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_firewall_v2route_policy_switch_with_options_async(request, runtime)

    def modify_instance_member_attributes_with_options(
        self,
        request: cloudfw_20171207_models.ModifyInstanceMemberAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyInstanceMemberAttributesResponse:
        """
        @summary Updates the information about members in Cloud Firewall.
        
        @description You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
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
        @summary Updates the information about members in Cloud Firewall.
        
        @description You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
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
        @summary Updates the information about members in Cloud Firewall.
        
        @description You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
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
        @summary Updates the information about members in Cloud Firewall.
        
        @description You can call the ModifyInstanceMemberAttributes operation to update the information about members in Cloud Firewall.
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
        @summary Modifies the configurations of an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
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
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
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
        @summary Modifies the configurations of an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
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
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
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
        @summary Modifies the configurations of an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
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
        @summary Modifies the configurations of an access control policy that is created for a NAT firewall.
        
        @description You can use this operation to modify the configurations of an access control policy. The policy is used to allow, deny, or monitor traffic that reaches a NAT firewall.
        
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
        """
        @summary Modifies the priority of an access control policy that is created for a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyPositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNatFirewallControlPolicyPositionResponse
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
        """
        @summary Modifies the priority of an access control policy that is created for a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyPositionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNatFirewallControlPolicyPositionResponse
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
        """
        @summary Modifies the priority of an access control policy that is created for a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyPositionRequest
        @return: ModifyNatFirewallControlPolicyPositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_nat_firewall_control_policy_position_with_options(request, runtime)

    async def modify_nat_firewall_control_policy_position_async(
        self,
        request: cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionRequest,
    ) -> cloudfw_20171207_models.ModifyNatFirewallControlPolicyPositionResponse:
        """
        @summary Modifies the priority of an access control policy that is created for a NAT firewall.
        
        @param request: ModifyNatFirewallControlPolicyPositionRequest
        @return: ModifyNatFirewallControlPolicyPositionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_nat_firewall_control_policy_position_with_options_async(request, runtime)

    def modify_object_group_operation_with_options(
        self,
        request: cloudfw_20171207_models.ModifyObjectGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyObjectGroupOperationResponse:
        """
        @summary Modifies information about an operation on an object group.
        
        @param request: ModifyObjectGroupOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyObjectGroupOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.object_list):
            query['ObjectList'] = request.object_list
        if not UtilClient.is_unset(request.object_operation):
            query['ObjectOperation'] = request.object_operation
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyObjectGroupOperation',
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
            cloudfw_20171207_models.ModifyObjectGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_object_group_operation_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyObjectGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyObjectGroupOperationResponse:
        """
        @summary Modifies information about an operation on an object group.
        
        @param request: ModifyObjectGroupOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyObjectGroupOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.object_list):
            query['ObjectList'] = request.object_list
        if not UtilClient.is_unset(request.object_operation):
            query['ObjectOperation'] = request.object_operation
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyObjectGroupOperation',
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
            cloudfw_20171207_models.ModifyObjectGroupOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_object_group_operation(
        self,
        request: cloudfw_20171207_models.ModifyObjectGroupOperationRequest,
    ) -> cloudfw_20171207_models.ModifyObjectGroupOperationResponse:
        """
        @summary Modifies information about an operation on an object group.
        
        @param request: ModifyObjectGroupOperationRequest
        @return: ModifyObjectGroupOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_object_group_operation_with_options(request, runtime)

    async def modify_object_group_operation_async(
        self,
        request: cloudfw_20171207_models.ModifyObjectGroupOperationRequest,
    ) -> cloudfw_20171207_models.ModifyObjectGroupOperationResponse:
        """
        @summary Modifies information about an operation on an object group.
        
        @param request: ModifyObjectGroupOperationRequest
        @return: ModifyObjectGroupOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_object_group_operation_with_options_async(request, runtime)

    def modify_policy_advanced_config_with_options(
        self,
        request: cloudfw_20171207_models.ModifyPolicyAdvancedConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyPolicyAdvancedConfigResponse:
        """
        @summary Enables or disables the strict mode for an access control policy.
        
        @description You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
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
        @summary Enables or disables the strict mode for an access control policy.
        
        @description You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
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
        @summary Enables or disables the strict mode for an access control policy.
        
        @description You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
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
        @summary Enables or disables the strict mode for an access control policy.
        
        @description You can call the ModifyPolicyAdvancedConfig operation to enable or disable the strict mode for an access control policy.
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
        """
        @summary Modifies the configuration of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: ModifyTrFirewallV2ConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTrFirewallV2ConfigurationResponse
        """
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
        """
        @summary Modifies the configuration of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: ModifyTrFirewallV2ConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTrFirewallV2ConfigurationResponse
        """
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
        """
        @summary Modifies the configuration of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: ModifyTrFirewallV2ConfigurationRequest
        @return: ModifyTrFirewallV2ConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tr_firewall_v2configuration_with_options(request, runtime)

    async def modify_tr_firewall_v2configuration_async(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationRequest,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2ConfigurationResponse:
        """
        @summary Modifies the configuration of a virtual private cloud (VPC) firewall that is created for a transit router.
        
        @param request: ModifyTrFirewallV2ConfigurationRequest
        @return: ModifyTrFirewallV2ConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tr_firewall_v2configuration_with_options_async(request, runtime)

    def modify_tr_firewall_v2route_policy_scope_with_options(
        self,
        tmp_req: cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        """
        @summary Modifies the effective scope of the routing policy created for the VPC firewall for a transit router.
        
        @param tmp_req: ModifyTrFirewallV2RoutePolicyScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTrFirewallV2RoutePolicyScopeResponse
        """
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
        if not UtilClient.is_unset(request.should_recover):
            query['ShouldRecover'] = request.should_recover
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
        """
        @summary Modifies the effective scope of the routing policy created for the VPC firewall for a transit router.
        
        @param tmp_req: ModifyTrFirewallV2RoutePolicyScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTrFirewallV2RoutePolicyScopeResponse
        """
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
        if not UtilClient.is_unset(request.should_recover):
            query['ShouldRecover'] = request.should_recover
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
        """
        @summary Modifies the effective scope of the routing policy created for the VPC firewall for a transit router.
        
        @param request: ModifyTrFirewallV2RoutePolicyScopeRequest
        @return: ModifyTrFirewallV2RoutePolicyScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_tr_firewall_v2route_policy_scope_with_options(request, runtime)

    async def modify_tr_firewall_v2route_policy_scope_async(
        self,
        request: cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
    ) -> cloudfw_20171207_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        """
        @summary Modifies the effective scope of the routing policy created for the VPC firewall for a transit router.
        
        @param request: ModifyTrFirewallV2RoutePolicyScopeRequest
        @return: ModifyTrFirewallV2RoutePolicyScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_tr_firewall_v2route_policy_scope_with_options_async(request, runtime)

    def modify_user_ipswhitelist_with_options(
        self,
        request: cloudfw_20171207_models.ModifyUserIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyUserIPSWhitelistResponse:
        """
        @summary 修改用户IPS白名单
        
        @param request: ModifyUserIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserIPSWhitelistResponse
        """
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
        """
        @summary 修改用户IPS白名单
        
        @param request: ModifyUserIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserIPSWhitelistResponse
        """
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
        """
        @summary 修改用户IPS白名单
        
        @param request: ModifyUserIPSWhitelistRequest
        @return: ModifyUserIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_ipswhitelist_with_options(request, runtime)

    async def modify_user_ipswhitelist_async(
        self,
        request: cloudfw_20171207_models.ModifyUserIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.ModifyUserIPSWhitelistResponse:
        """
        @summary 修改用户IPS白名单
        
        @param request: ModifyUserIPSWhitelistRequest
        @return: ModifyUserIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_ipswhitelist_with_options_async(request, runtime)

    def modify_vpc_firewall_cen_configure_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallCenConfigureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallCenConfigureResponse:
        """
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenConfigure operation to modify the configurations of a VPC firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a Cloud Enterprise Network (CEN) instance.
        
        @description You can call the ModifyVpcFirewallCenSwitchStatus operation to enable or disable a VPC firewall. A VPC firewall protects mutual access traffic between a specified VPC and a network instance that is attached to a CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. After you enable the VPC firewall, the VPC firewall protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance. After you disable the VPC firewall, the VPC firewall no longer protects mutual access traffic between a VPC and a specified network instance that is attached to a CEN instance.
        Before you call this operation, make sure that you have created a VPC firewall by calling the [CreateVpcFirewallCenConfigure](https://help.aliyun.com/document_detail/345772.html) operation.
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
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Modifies the configurations of a virtual private cloud (VPC) firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallConfigure operation to modify the configurations of a VPC firewall. The VPC firewall controls traffic between two VPCs that are connected by using an Express Connect circuit. Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Modifies the configurations of an access control policy that is created for a virtual private cloud (VPC) firewall in a specified policy group.
        
        @description You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Modifies the configurations of an access control policy that is created for a virtual private cloud (VPC) firewall in a specified policy group.
        
        @description You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
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
        if not UtilClient.is_unset(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
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
        @summary Modifies the configurations of an access control policy that is created for a virtual private cloud (VPC) firewall in a specified policy group.
        
        @description You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
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
        @summary Modifies the configurations of an access control policy that is created for a virtual private cloud (VPC) firewall in a specified policy group.
        
        @description You can call the ModifyVpcFirewallControlPolicy operation to modify the configurations of an access control policy that is created for a VPC firewall in a specified policy group. Different access control policies are used for the VPC firewalls that are used to protect each Cloud Enterprise Network (CEN) instance and the VPC firewalls that are used to protect each Express Connect circuit.
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
        @summary Modifies the priority of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
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
        @summary Modifies the priority of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
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
        @summary Modifies the priority of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
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
        @summary Modifies the priority of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can use this operation to modify the priority of an access control policy that is created for a VPC firewall in a specific policy group.
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
        @summary Modifies the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call this operation to modify the intrusion prevention configurations of a VPC firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        if not UtilClient.is_unset(request.rule_class):
            query['RuleClass'] = request.rule_class
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
        @summary Modifies the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call this operation to modify the intrusion prevention configurations of a VPC firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        if not UtilClient.is_unset(request.rule_class):
            query['RuleClass'] = request.rule_class
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
        @summary Modifies the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call this operation to modify the intrusion prevention configurations of a VPC firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Modifies the intrusion prevention configurations of a virtual private cloud (VPC) firewall.
        
        @description You can call this operation to modify the intrusion prevention configurations of a VPC firewall.
        ## [](#qps-)Limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ModifyVpcFirewallDefaultIPSConfigRequest
        @return: ModifyVpcFirewallDefaultIPSConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_default_ipsconfig_with_options_async(request, runtime)

    def modify_vpc_firewall_ipswhitelist_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistResponse:
        """
        @summary Modifies the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: ModifyVpcFirewallIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallIPSWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.list_type):
            query['ListType'] = request.list_type
        if not UtilClient.is_unset(request.list_value):
            query['ListValue'] = request.list_value
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallIPSWhitelist',
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
            cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_ipswhitelist_with_options_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistResponse:
        """
        @summary Modifies the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: ModifyVpcFirewallIPSWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVpcFirewallIPSWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.list_type):
            query['ListType'] = request.list_type
        if not UtilClient.is_unset(request.list_value):
            query['ListValue'] = request.list_value
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not UtilClient.is_unset(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVpcFirewallIPSWhitelist',
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
            cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_ipswhitelist(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistResponse:
        """
        @summary Modifies the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: ModifyVpcFirewallIPSWhitelistRequest
        @return: ModifyVpcFirewallIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_firewall_ipswhitelist_with_options(request, runtime)

    async def modify_vpc_firewall_ipswhitelist_async(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistRequest,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallIPSWhitelistResponse:
        """
        @summary Modifies the IPS whitelist of a virtual private cloud (VPC) firewall.
        
        @param request: ModifyVpcFirewallIPSWhitelistRequest
        @return: ModifyVpcFirewallIPSWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_firewall_ipswhitelist_with_options_async(request, runtime)

    def modify_vpc_firewall_switch_status_with_options(
        self,
        request: cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ModifyVpcFirewallSwitchStatusResponse:
        """
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Enables or disables a virtual private cloud (VPC) firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit.
        
        @description You can call the ModifyVpcFirewallSwitchStatus operation to enable or disable a VPC firewall. The VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit. After you enable the VPC firewall, the VPC firewall protects access traffic between two VPCs that are connected by using an Express Connect circuit. After you disable the VPC firewall, the VPC firewall no longer protects access traffic between two VPCs that are connected by using an Express Connect circuit.
        Before you call the operation, make sure that you created a VPC firewall by calling the [CreateVpcFirewallConfigure](https://help.aliyun.com/document_detail/342893.html) operation.
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
        @summary Turns off all firewall switches.
        
        @description You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Turns off all firewall switches.
        
        @description You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Turns off all firewall switches.
        
        @description You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Turns off all firewall switches.
        
        @description You can call the PutDisableAllFwSwitch operation to turn off all firewall switches.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Disable a firewall for specific assets.
        
        @description You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
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
        @summary Disable a firewall for specific assets.
        
        @description You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
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
        @summary Disable a firewall for specific assets.
        
        @description You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
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
        @summary Disable a firewall for specific assets.
        
        @description You can call the PutDisableFwSwitch operation to disable a firewall for specific assets. After you disable the firewall, traffic does not pass through Cloud Firewall.
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
        @summary Enables a firewall for all public IP addresses within your Alibaba Cloud account.
        
        @description You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
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
        @summary Enables a firewall for all public IP addresses within your Alibaba Cloud account.
        
        @description You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
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
        @summary Enables a firewall for all public IP addresses within your Alibaba Cloud account.
        
        @description You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
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
        @summary Enables a firewall for all public IP addresses within your Alibaba Cloud account.
        
        @description You can call the PutEnableAllFwSwitch operation to enable a firewall for all public IP addresses within your Alibaba Cloud account.
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
        @summary Enables firewalls for specific assets.
        
        @description You can call this operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Enables firewalls for specific assets.
        
        @description You can call this operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Enables firewalls for specific assets.
        
        @description You can call this operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
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
        @summary Enables firewalls for specific assets.
        
        @description You can call this operation to enable a firewall. After you enable a firewall, traffic passes through Cloud Firewall.
        ## [](#qps-)Limits
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: PutEnableFwSwitchRequest
        @return: PutEnableFwSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_enable_fw_switch_with_options_async(request, runtime)

    def release_post_instance_with_options(
        self,
        request: cloudfw_20171207_models.ReleasePostInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ReleasePostInstanceResponse:
        """
        @summary Releases Cloud Firewall that uses the pay-as-you-go billing method.
        
        @param request: ReleasePostInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePostInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePostInstance',
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
            cloudfw_20171207_models.ReleasePostInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_post_instance_with_options_async(
        self,
        request: cloudfw_20171207_models.ReleasePostInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ReleasePostInstanceResponse:
        """
        @summary Releases Cloud Firewall that uses the pay-as-you-go billing method.
        
        @param request: ReleasePostInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleasePostInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePostInstance',
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
            cloudfw_20171207_models.ReleasePostInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_post_instance(
        self,
        request: cloudfw_20171207_models.ReleasePostInstanceRequest,
    ) -> cloudfw_20171207_models.ReleasePostInstanceResponse:
        """
        @summary Releases Cloud Firewall that uses the pay-as-you-go billing method.
        
        @param request: ReleasePostInstanceRequest
        @return: ReleasePostInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_post_instance_with_options(request, runtime)

    async def release_post_instance_async(
        self,
        request: cloudfw_20171207_models.ReleasePostInstanceRequest,
    ) -> cloudfw_20171207_models.ReleasePostInstanceResponse:
        """
        @summary Releases Cloud Firewall that uses the pay-as-you-go billing method.
        
        @param request: ReleasePostInstanceRequest
        @return: ReleasePostInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_post_instance_with_options_async(request, runtime)

    def reset_nat_firewall_rule_hit_count_with_options(
        self,
        request: cloudfw_20171207_models.ResetNatFirewallRuleHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ResetNatFirewallRuleHitCountResponse:
        """
        @summary Resets the number of NAT firewall hits.
        
        @param request: ResetNatFirewallRuleHitCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetNatFirewallRuleHitCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNatFirewallRuleHitCount',
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
            cloudfw_20171207_models.ResetNatFirewallRuleHitCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_nat_firewall_rule_hit_count_with_options_async(
        self,
        request: cloudfw_20171207_models.ResetNatFirewallRuleHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ResetNatFirewallRuleHitCountResponse:
        """
        @summary Resets the number of NAT firewall hits.
        
        @param request: ResetNatFirewallRuleHitCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetNatFirewallRuleHitCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNatFirewallRuleHitCount',
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
            cloudfw_20171207_models.ResetNatFirewallRuleHitCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_nat_firewall_rule_hit_count(
        self,
        request: cloudfw_20171207_models.ResetNatFirewallRuleHitCountRequest,
    ) -> cloudfw_20171207_models.ResetNatFirewallRuleHitCountResponse:
        """
        @summary Resets the number of NAT firewall hits.
        
        @param request: ResetNatFirewallRuleHitCountRequest
        @return: ResetNatFirewallRuleHitCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_nat_firewall_rule_hit_count_with_options(request, runtime)

    async def reset_nat_firewall_rule_hit_count_async(
        self,
        request: cloudfw_20171207_models.ResetNatFirewallRuleHitCountRequest,
    ) -> cloudfw_20171207_models.ResetNatFirewallRuleHitCountResponse:
        """
        @summary Resets the number of NAT firewall hits.
        
        @param request: ResetNatFirewallRuleHitCountRequest
        @return: ResetNatFirewallRuleHitCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_nat_firewall_rule_hit_count_with_options_async(request, runtime)

    def reset_vpc_firewall_rule_hit_count_with_options(
        self,
        request: cloudfw_20171207_models.ResetVpcFirewallRuleHitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.ResetVpcFirewallRuleHitCountResponse:
        """
        @summary Clears the count on hits of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
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
        @summary Clears the count on hits of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
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
        @summary Clears the count on hits of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
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
        @summary Clears the count on hits of an access control policy that is created for a virtual private cloud (VPC) firewall in a specific policy group.
        
        @description You can call the ResetVpcFirewallRuleHitCount operation to clear the count on hits of an access control policy that is created for a VPC firewall in a specific policy group.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ResetVpcFirewallRuleHitCountRequest
        @return: ResetVpcFirewallRuleHitCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_vpc_firewall_rule_hit_count_with_options_async(request, runtime)

    def switch_security_proxy_with_options(
        self,
        request: cloudfw_20171207_models.SwitchSecurityProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.SwitchSecurityProxyResponse:
        """
        @summary Enables or disables a NAT firewall.
        
        @param request: SwitchSecurityProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchSecurityProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.switch):
            query['Switch'] = request.switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSecurityProxy',
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
            cloudfw_20171207_models.SwitchSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_security_proxy_with_options_async(
        self,
        request: cloudfw_20171207_models.SwitchSecurityProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudfw_20171207_models.SwitchSecurityProxyResponse:
        """
        @summary Enables or disables a NAT firewall.
        
        @param request: SwitchSecurityProxyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchSecurityProxyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.switch):
            query['Switch'] = request.switch
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSecurityProxy',
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
            cloudfw_20171207_models.SwitchSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_security_proxy(
        self,
        request: cloudfw_20171207_models.SwitchSecurityProxyRequest,
    ) -> cloudfw_20171207_models.SwitchSecurityProxyResponse:
        """
        @summary Enables or disables a NAT firewall.
        
        @param request: SwitchSecurityProxyRequest
        @return: SwitchSecurityProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_security_proxy_with_options(request, runtime)

    async def switch_security_proxy_async(
        self,
        request: cloudfw_20171207_models.SwitchSecurityProxyRequest,
    ) -> cloudfw_20171207_models.SwitchSecurityProxyResponse:
        """
        @summary Enables or disables a NAT firewall.
        
        @param request: SwitchSecurityProxyRequest
        @return: SwitchSecurityProxyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_security_proxy_with_options_async(request, runtime)
