# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudfw20171207 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_acl_backup_data_with_options(
        self,
        request: main_models.AddAclBackupDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAclBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_up_time):
            query['BackUpTime'] = request.back_up_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAclBackupData',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAclBackupDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_acl_backup_data_with_options_async(
        self,
        request: main_models.AddAclBackupDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAclBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_up_time):
            query['BackUpTime'] = request.back_up_time
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAclBackupData',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAclBackupDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_acl_backup_data(
        self,
        request: main_models.AddAclBackupDataRequest,
    ) -> main_models.AddAclBackupDataResponse:
        runtime = RuntimeOptions()
        return self.add_acl_backup_data_with_options(request, runtime)

    async def add_acl_backup_data_async(
        self,
        request: main_models.AddAclBackupDataRequest,
    ) -> main_models.AddAclBackupDataResponse:
        runtime = RuntimeOptions()
        return await self.add_acl_backup_data_with_options_async(request, runtime)

    def add_address_book_with_options(
        self,
        request: main_models.AddAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ack_cluster_connector_id):
            query['AckClusterConnectorId'] = request.ack_cluster_connector_id
        if not DaraCore.is_null(request.ack_labels):
            query['AckLabels'] = request.ack_labels
        if not DaraCore.is_null(request.ack_namespaces):
            query['AckNamespaces'] = request.ack_namespaces
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        if not DaraCore.is_null(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_address_book_with_options_async(
        self,
        request: main_models.AddAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ack_cluster_connector_id):
            query['AckClusterConnectorId'] = request.ack_cluster_connector_id
        if not DaraCore.is_null(request.ack_labels):
            query['AckLabels'] = request.ack_labels
        if not DaraCore.is_null(request.ack_namespaces):
            query['AckNamespaces'] = request.ack_namespaces
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        if not DaraCore.is_null(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_address_book(
        self,
        request: main_models.AddAddressBookRequest,
    ) -> main_models.AddAddressBookResponse:
        runtime = RuntimeOptions()
        return self.add_address_book_with_options(request, runtime)

    async def add_address_book_async(
        self,
        request: main_models.AddAddressBookRequest,
    ) -> main_models.AddAddressBookResponse:
        runtime = RuntimeOptions()
        return await self.add_address_book_with_options_async(request, runtime)

    def add_control_policy_with_options(
        self,
        request: main_models.AddControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_control_policy_with_options_async(
        self,
        request: main_models.AddControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_control_policy(
        self,
        request: main_models.AddControlPolicyRequest,
    ) -> main_models.AddControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.add_control_policy_with_options(request, runtime)

    async def add_control_policy_async(
        self,
        request: main_models.AddControlPolicyRequest,
    ) -> main_models.AddControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.add_control_policy_with_options_async(request, runtime)

    def add_dns_firewall_policy_with_options(
        self,
        request: main_models.AddDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsFirewallPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_dns_firewall_policy_with_options_async(
        self,
        request: main_models.AddDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDnsFirewallPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_dns_firewall_policy(
        self,
        request: main_models.AddDnsFirewallPolicyRequest,
    ) -> main_models.AddDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return self.add_dns_firewall_policy_with_options(request, runtime)

    async def add_dns_firewall_policy_async(
        self,
        request: main_models.AddDnsFirewallPolicyRequest,
    ) -> main_models.AddDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return await self.add_dns_firewall_policy_with_options_async(request, runtime)

    def add_domain_resolve_realtime_task_with_options(
        self,
        request: main_models.AddDomainResolveRealtimeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainResolveRealtimeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainResolveRealtimeTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainResolveRealtimeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_domain_resolve_realtime_task_with_options_async(
        self,
        request: main_models.AddDomainResolveRealtimeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDomainResolveRealtimeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDomainResolveRealtimeTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDomainResolveRealtimeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_domain_resolve_realtime_task(
        self,
        request: main_models.AddDomainResolveRealtimeTaskRequest,
    ) -> main_models.AddDomainResolveRealtimeTaskResponse:
        runtime = RuntimeOptions()
        return self.add_domain_resolve_realtime_task_with_options(request, runtime)

    async def add_domain_resolve_realtime_task_async(
        self,
        request: main_models.AddDomainResolveRealtimeTaskRequest,
    ) -> main_models.AddDomainResolveRealtimeTaskResponse:
        runtime = RuntimeOptions()
        return await self.add_domain_resolve_realtime_task_with_options_async(request, runtime)

    def add_instance_members_with_options(
        self,
        request: main_models.AddInstanceMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddInstanceMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddInstanceMembers',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddInstanceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_instance_members_with_options_async(
        self,
        request: main_models.AddInstanceMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddInstanceMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddInstanceMembers',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddInstanceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_instance_members(
        self,
        request: main_models.AddInstanceMembersRequest,
    ) -> main_models.AddInstanceMembersResponse:
        runtime = RuntimeOptions()
        return self.add_instance_members_with_options(request, runtime)

    async def add_instance_members_async(
        self,
        request: main_models.AddInstanceMembersRequest,
    ) -> main_models.AddInstanceMembersResponse:
        runtime = RuntimeOptions()
        return await self.add_instance_members_with_options_async(request, runtime)

    def add_private_dns_domain_name_with_options(
        self,
        request: main_models.AddPrivateDnsDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrivateDnsDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.domain_name_list):
            query['DomainNameList'] = request.domain_name_list
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrivateDnsDomainName',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrivateDnsDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_private_dns_domain_name_with_options_async(
        self,
        request: main_models.AddPrivateDnsDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrivateDnsDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.domain_name_list):
            query['DomainNameList'] = request.domain_name_list
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrivateDnsDomainName',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrivateDnsDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_private_dns_domain_name(
        self,
        request: main_models.AddPrivateDnsDomainNameRequest,
    ) -> main_models.AddPrivateDnsDomainNameResponse:
        runtime = RuntimeOptions()
        return self.add_private_dns_domain_name_with_options(request, runtime)

    async def add_private_dns_domain_name_async(
        self,
        request: main_models.AddPrivateDnsDomainNameRequest,
    ) -> main_models.AddPrivateDnsDomainNameResponse:
        runtime = RuntimeOptions()
        return await self.add_private_dns_domain_name_with_options_async(request, runtime)

    def batch_copy_vpc_firewall_control_policy_with_options(
        self,
        request: main_models.BatchCopyVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCopyVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_vpc_firewall_id):
            query['SourceVpcFirewallId'] = request.source_vpc_firewall_id
        if not DaraCore.is_null(request.target_vpc_firewall_id):
            query['TargetVpcFirewallId'] = request.target_vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCopyVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCopyVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_copy_vpc_firewall_control_policy_with_options_async(
        self,
        request: main_models.BatchCopyVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCopyVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_vpc_firewall_id):
            query['SourceVpcFirewallId'] = request.source_vpc_firewall_id
        if not DaraCore.is_null(request.target_vpc_firewall_id):
            query['TargetVpcFirewallId'] = request.target_vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCopyVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCopyVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_copy_vpc_firewall_control_policy(
        self,
        request: main_models.BatchCopyVpcFirewallControlPolicyRequest,
    ) -> main_models.BatchCopyVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.batch_copy_vpc_firewall_control_policy_with_options(request, runtime)

    async def batch_copy_vpc_firewall_control_policy_async(
        self,
        request: main_models.BatchCopyVpcFirewallControlPolicyRequest,
    ) -> main_models.BatchCopyVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.batch_copy_vpc_firewall_control_policy_with_options_async(request, runtime)

    def batch_delete_vpc_firewall_control_policy_with_options(
        self,
        request: main_models.BatchDeleteVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_vpc_firewall_control_policy_with_options_async(
        self,
        request: main_models.BatchDeleteVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_vpc_firewall_control_policy(
        self,
        request: main_models.BatchDeleteVpcFirewallControlPolicyRequest,
    ) -> main_models.BatchDeleteVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_vpc_firewall_control_policy_with_options(request, runtime)

    async def batch_delete_vpc_firewall_control_policy_async(
        self,
        request: main_models.BatchDeleteVpcFirewallControlPolicyRequest,
    ) -> main_models.BatchDeleteVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_vpc_firewall_control_policy_with_options_async(request, runtime)

    def clear_log_store_storage_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ClearLogStoreStorageResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ClearLogStoreStorage',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearLogStoreStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_log_store_storage_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ClearLogStoreStorageResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ClearLogStoreStorage',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearLogStoreStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_log_store_storage(self) -> main_models.ClearLogStoreStorageResponse:
        runtime = RuntimeOptions()
        return self.clear_log_store_storage_with_options(runtime)

    async def clear_log_store_storage_async(self) -> main_models.ClearLogStoreStorageResponse:
        runtime = RuntimeOptions()
        return await self.clear_log_store_storage_with_options_async(runtime)

    def create_ack_cluster_connector_with_options(
        self,
        request: main_models.CreateAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.connector_name):
            query['ConnectorName'] = request.connector_name
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVswitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_vswitch_ip):
            query['PrimaryVswitchIp'] = request.primary_vswitch_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVswitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_vswitch_ip):
            query['StandbyVswitchIp'] = request.standby_vswitch_ip
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAckClusterConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ack_cluster_connector_with_options_async(
        self,
        request: main_models.CreateAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.connector_name):
            query['ConnectorName'] = request.connector_name
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVswitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_vswitch_ip):
            query['PrimaryVswitchIp'] = request.primary_vswitch_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVswitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_vswitch_ip):
            query['StandbyVswitchIp'] = request.standby_vswitch_ip
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAckClusterConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ack_cluster_connector(
        self,
        request: main_models.CreateAckClusterConnectorRequest,
    ) -> main_models.CreateAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return self.create_ack_cluster_connector_with_options(request, runtime)

    async def create_ack_cluster_connector_async(
        self,
        request: main_models.CreateAckClusterConnectorRequest,
    ) -> main_models.CreateAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return await self.create_ack_cluster_connector_with_options_async(request, runtime)

    def create_acl_check_with_options(
        self,
        request: main_models.CreateAclCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.check_names):
            query['CheckNames'] = request.check_names
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAclCheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_acl_check_with_options_async(
        self,
        request: main_models.CreateAclCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_type):
            query['AclType'] = request.acl_type
        if not DaraCore.is_null(request.check_names):
            query['CheckNames'] = request.check_names
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAclCheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAclCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_acl_check(
        self,
        request: main_models.CreateAclCheckRequest,
    ) -> main_models.CreateAclCheckResponse:
        runtime = RuntimeOptions()
        return self.create_acl_check_with_options(request, runtime)

    async def create_acl_check_async(
        self,
        request: main_models.CreateAclCheckRequest,
    ) -> main_models.CreateAclCheckResponse:
        runtime = RuntimeOptions()
        return await self.create_acl_check_with_options_async(request, runtime)

    def create_download_task_with_options(
        self,
        request: main_models.CreateDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_data):
            query['TaskData'] = request.task_data
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_download_task_with_options_async(
        self,
        request: main_models.CreateDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_data):
            query['TaskData'] = request.task_data
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.time_zone):
            query['TimeZone'] = request.time_zone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownloadTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_download_task(
        self,
        request: main_models.CreateDownloadTaskRequest,
    ) -> main_models.CreateDownloadTaskResponse:
        runtime = RuntimeOptions()
        return self.create_download_task_with_options(request, runtime)

    async def create_download_task_async(
        self,
        request: main_models.CreateDownloadTaskRequest,
    ) -> main_models.CreateDownloadTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_download_task_with_options_async(request, runtime)

    def create_instance_sync_task_with_options(
        self,
        request: main_models.CreateInstanceSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceSyncTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_sync_task_with_options_async(
        self,
        request: main_models.CreateInstanceSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceSyncTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_sync_task(
        self,
        request: main_models.CreateInstanceSyncTaskRequest,
    ) -> main_models.CreateInstanceSyncTaskResponse:
        runtime = RuntimeOptions()
        return self.create_instance_sync_task_with_options(request, runtime)

    async def create_instance_sync_task_async(
        self,
        request: main_models.CreateInstanceSyncTaskRequest,
    ) -> main_models.CreateInstanceSyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_sync_task_with_options_async(request, runtime)

    def create_ips_private_assoc_with_options(
        self,
        request: main_models.CreateIpsPrivateAssocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpsPrivateAssocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpsPrivateAssoc',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpsPrivateAssocResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ips_private_assoc_with_options_async(
        self,
        request: main_models.CreateIpsPrivateAssocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpsPrivateAssocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpsPrivateAssoc',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpsPrivateAssocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ips_private_assoc(
        self,
        request: main_models.CreateIpsPrivateAssocRequest,
    ) -> main_models.CreateIpsPrivateAssocResponse:
        runtime = RuntimeOptions()
        return self.create_ips_private_assoc_with_options(request, runtime)

    async def create_ips_private_assoc_async(
        self,
        request: main_models.CreateIpsPrivateAssocRequest,
    ) -> main_models.CreateIpsPrivateAssocResponse:
        runtime = RuntimeOptions()
        return await self.create_ips_private_assoc_with_options_async(request, runtime)

    def create_nat_firewall_control_policy_with_options(
        self,
        request: main_models.CreateNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nat_firewall_control_policy_with_options_async(
        self,
        request: main_models.CreateNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nat_firewall_control_policy(
        self,
        request: main_models.CreateNatFirewallControlPolicyRequest,
    ) -> main_models.CreateNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_nat_firewall_control_policy_with_options(request, runtime)

    async def create_nat_firewall_control_policy_async(
        self,
        request: main_models.CreateNatFirewallControlPolicyRequest,
    ) -> main_models.CreateNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_nat_firewall_control_policy_with_options_async(request, runtime)

    def create_nat_firewall_pre_check_with_options(
        self,
        request: main_models.CreateNatFirewallPreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNatFirewallPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not DaraCore.is_null(request.nat_gateway_id):
            body['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.region_no):
            body['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNatFirewallPreCheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNatFirewallPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nat_firewall_pre_check_with_options_async(
        self,
        request: main_models.CreateNatFirewallPreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNatFirewallPreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        body = {}
        if not DaraCore.is_null(request.nat_gateway_id):
            body['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.region_no):
            body['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNatFirewallPreCheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNatFirewallPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nat_firewall_pre_check(
        self,
        request: main_models.CreateNatFirewallPreCheckRequest,
    ) -> main_models.CreateNatFirewallPreCheckResponse:
        runtime = RuntimeOptions()
        return self.create_nat_firewall_pre_check_with_options(request, runtime)

    async def create_nat_firewall_pre_check_async(
        self,
        request: main_models.CreateNatFirewallPreCheckRequest,
    ) -> main_models.CreateNatFirewallPreCheckResponse:
        runtime = RuntimeOptions()
        return await self.create_nat_firewall_pre_check_with_options_async(request, runtime)

    def create_nat_firewall_sync_task_with_options(
        self,
        request: main_models.CreateNatFirewallSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNatFirewallSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNatFirewallSyncTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNatFirewallSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nat_firewall_sync_task_with_options_async(
        self,
        request: main_models.CreateNatFirewallSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNatFirewallSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNatFirewallSyncTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNatFirewallSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nat_firewall_sync_task(
        self,
        request: main_models.CreateNatFirewallSyncTaskRequest,
    ) -> main_models.CreateNatFirewallSyncTaskResponse:
        runtime = RuntimeOptions()
        return self.create_nat_firewall_sync_task_with_options(request, runtime)

    async def create_nat_firewall_sync_task_async(
        self,
        request: main_models.CreateNatFirewallSyncTaskRequest,
    ) -> main_models.CreateNatFirewallSyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_nat_firewall_sync_task_with_options_async(request, runtime)

    def create_private_dns_endpoint_with_options(
        self,
        request: main_models.CreatePrivateDnsEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateDnsEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_name):
            query['AccessInstanceName'] = request.access_instance_name
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.primary_dns):
            query['PrimaryDns'] = request.primary_dns
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_vswitch_ip):
            query['PrimaryVSwitchIp'] = request.primary_vswitch_ip
        if not DaraCore.is_null(request.private_dns_type):
            query['PrivateDnsType'] = request.private_dns_type
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.standby_dns):
            query['StandbyDns'] = request.standby_dns
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_vswitch_ip):
            query['StandbyVSwitchIp'] = request.standby_vswitch_ip
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateDnsEndpoint',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateDnsEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_dns_endpoint_with_options_async(
        self,
        request: main_models.CreatePrivateDnsEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateDnsEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_name):
            query['AccessInstanceName'] = request.access_instance_name
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.primary_dns):
            query['PrimaryDns'] = request.primary_dns
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_vswitch_ip):
            query['PrimaryVSwitchIp'] = request.primary_vswitch_ip
        if not DaraCore.is_null(request.private_dns_type):
            query['PrivateDnsType'] = request.private_dns_type
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.standby_dns):
            query['StandbyDns'] = request.standby_dns
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_vswitch_ip):
            query['StandbyVSwitchIp'] = request.standby_vswitch_ip
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateDnsEndpoint',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateDnsEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_dns_endpoint(
        self,
        request: main_models.CreatePrivateDnsEndpointRequest,
    ) -> main_models.CreatePrivateDnsEndpointResponse:
        runtime = RuntimeOptions()
        return self.create_private_dns_endpoint_with_options(request, runtime)

    async def create_private_dns_endpoint_async(
        self,
        request: main_models.CreatePrivateDnsEndpointRequest,
    ) -> main_models.CreatePrivateDnsEndpointResponse:
        runtime = RuntimeOptions()
        return await self.create_private_dns_endpoint_with_options_async(request, runtime)

    def create_security_proxy_with_options(
        self,
        request: main_models.CreateSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.nat_route_entry_list):
            query['NatRouteEntryList'] = request.nat_route_entry_list
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_auto):
            query['VswitchAuto'] = request.vswitch_auto
        if not DaraCore.is_null(request.vswitch_cidr):
            query['VswitchCidr'] = request.vswitch_cidr
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_proxy_with_options_async(
        self,
        request: main_models.CreateSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.nat_route_entry_list):
            query['NatRouteEntryList'] = request.nat_route_entry_list
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_auto):
            query['VswitchAuto'] = request.vswitch_auto
        if not DaraCore.is_null(request.vswitch_cidr):
            query['VswitchCidr'] = request.vswitch_cidr
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_proxy(
        self,
        request: main_models.CreateSecurityProxyRequest,
    ) -> main_models.CreateSecurityProxyResponse:
        runtime = RuntimeOptions()
        return self.create_security_proxy_with_options(request, runtime)

    async def create_security_proxy_async(
        self,
        request: main_models.CreateSecurityProxyRequest,
    ) -> main_models.CreateSecurityProxyResponse:
        runtime = RuntimeOptions()
        return await self.create_security_proxy_with_options_async(request, runtime)

    def create_sls_log_dispatch_with_options(
        self,
        request: main_models.CreateSlsLogDispatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlsLogDispatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.sls_region_id):
            body['SlsRegionId'] = request.sls_region_id
        if not DaraCore.is_null(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlsLogDispatch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlsLogDispatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sls_log_dispatch_with_options_async(
        self,
        request: main_models.CreateSlsLogDispatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlsLogDispatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.sls_region_id):
            body['SlsRegionId'] = request.sls_region_id
        if not DaraCore.is_null(request.ttl):
            body['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlsLogDispatch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlsLogDispatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sls_log_dispatch(
        self,
        request: main_models.CreateSlsLogDispatchRequest,
    ) -> main_models.CreateSlsLogDispatchResponse:
        runtime = RuntimeOptions()
        return self.create_sls_log_dispatch_with_options(request, runtime)

    async def create_sls_log_dispatch_async(
        self,
        request: main_models.CreateSlsLogDispatchRequest,
    ) -> main_models.CreateSlsLogDispatchResponse:
        runtime = RuntimeOptions()
        return await self.create_sls_log_dispatch_with_options_async(request, runtime)

    def create_tr_firewall_v2with_options(
        self,
        request: main_models.CreateTrFirewallV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrFirewallV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.firewall_description):
            query['FirewallDescription'] = request.firewall_description
        if not DaraCore.is_null(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not DaraCore.is_null(request.firewall_subnet_cidr):
            query['FirewallSubnetCidr'] = request.firewall_subnet_cidr
        if not DaraCore.is_null(request.firewall_vpc_cidr):
            query['FirewallVpcCidr'] = request.firewall_vpc_cidr
        if not DaraCore.is_null(request.firewall_vpc_id):
            query['FirewallVpcId'] = request.firewall_vpc_id
        if not DaraCore.is_null(request.firewall_vswitch_id):
            query['FirewallVswitchId'] = request.firewall_vswitch_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not DaraCore.is_null(request.tr_attachment_master_cidr):
            query['TrAttachmentMasterCidr'] = request.tr_attachment_master_cidr
        if not DaraCore.is_null(request.tr_attachment_master_zone):
            query['TrAttachmentMasterZone'] = request.tr_attachment_master_zone
        if not DaraCore.is_null(request.tr_attachment_slave_cidr):
            query['TrAttachmentSlaveCidr'] = request.tr_attachment_slave_cidr
        if not DaraCore.is_null(request.tr_attachment_slave_zone):
            query['TrAttachmentSlaveZone'] = request.tr_attachment_slave_zone
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrFirewallV2',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrFirewallV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_tr_firewall_v2with_options_async(
        self,
        request: main_models.CreateTrFirewallV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrFirewallV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.firewall_description):
            query['FirewallDescription'] = request.firewall_description
        if not DaraCore.is_null(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not DaraCore.is_null(request.firewall_subnet_cidr):
            query['FirewallSubnetCidr'] = request.firewall_subnet_cidr
        if not DaraCore.is_null(request.firewall_vpc_cidr):
            query['FirewallVpcCidr'] = request.firewall_vpc_cidr
        if not DaraCore.is_null(request.firewall_vpc_id):
            query['FirewallVpcId'] = request.firewall_vpc_id
        if not DaraCore.is_null(request.firewall_vswitch_id):
            query['FirewallVswitchId'] = request.firewall_vswitch_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not DaraCore.is_null(request.tr_attachment_master_cidr):
            query['TrAttachmentMasterCidr'] = request.tr_attachment_master_cidr
        if not DaraCore.is_null(request.tr_attachment_master_zone):
            query['TrAttachmentMasterZone'] = request.tr_attachment_master_zone
        if not DaraCore.is_null(request.tr_attachment_slave_cidr):
            query['TrAttachmentSlaveCidr'] = request.tr_attachment_slave_cidr
        if not DaraCore.is_null(request.tr_attachment_slave_zone):
            query['TrAttachmentSlaveZone'] = request.tr_attachment_slave_zone
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrFirewallV2',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrFirewallV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tr_firewall_v2(
        self,
        request: main_models.CreateTrFirewallV2Request,
    ) -> main_models.CreateTrFirewallV2Response:
        runtime = RuntimeOptions()
        return self.create_tr_firewall_v2with_options(request, runtime)

    async def create_tr_firewall_v2_async(
        self,
        request: main_models.CreateTrFirewallV2Request,
    ) -> main_models.CreateTrFirewallV2Response:
        runtime = RuntimeOptions()
        return await self.create_tr_firewall_v2with_options_async(request, runtime)

    def create_tr_firewall_v2route_policy_with_options(
        self,
        tmp_req: main_models.CreateTrFirewallV2RoutePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrFirewallV2RoutePolicyResponse:
        tmp_req.validate()
        request = main_models.CreateTrFirewallV2RoutePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not DaraCore.is_null(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not DaraCore.is_null(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.policy_description):
            query['PolicyDescription'] = request.policy_description
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrFirewallV2RoutePolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrFirewallV2RoutePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tr_firewall_v2route_policy_with_options_async(
        self,
        tmp_req: main_models.CreateTrFirewallV2RoutePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrFirewallV2RoutePolicyResponse:
        tmp_req.validate()
        request = main_models.CreateTrFirewallV2RoutePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not DaraCore.is_null(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not DaraCore.is_null(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.policy_description):
            query['PolicyDescription'] = request.policy_description
        if not DaraCore.is_null(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrFirewallV2RoutePolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrFirewallV2RoutePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tr_firewall_v2route_policy(
        self,
        request: main_models.CreateTrFirewallV2RoutePolicyRequest,
    ) -> main_models.CreateTrFirewallV2RoutePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_tr_firewall_v2route_policy_with_options(request, runtime)

    async def create_tr_firewall_v2route_policy_async(
        self,
        request: main_models.CreateTrFirewallV2RoutePolicyRequest,
    ) -> main_models.CreateTrFirewallV2RoutePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_tr_firewall_v2route_policy_with_options_async(request, runtime)

    def create_vpc_firewall_cen_configure_with_options(
        self,
        request: main_models.CreateVpcFirewallCenConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallCenConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.firewall_vswitch_cidr_block):
            query['FirewallVSwitchCidrBlock'] = request.firewall_vswitch_cidr_block
        if not DaraCore.is_null(request.firewall_vpc_cidr_block):
            query['FirewallVpcCidrBlock'] = request.firewall_vpc_cidr_block
        if not DaraCore.is_null(request.firewall_vpc_standby_zone_id):
            query['FirewallVpcStandbyZoneId'] = request.firewall_vpc_standby_zone_id
        if not DaraCore.is_null(request.firewall_vpc_zone_id):
            query['FirewallVpcZoneId'] = request.firewall_vpc_zone_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not DaraCore.is_null(request.vpc_region):
            query['VpcRegion'] = request.vpc_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallCenConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallCenConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_cen_configure_with_options_async(
        self,
        request: main_models.CreateVpcFirewallCenConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallCenConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.firewall_vswitch_cidr_block):
            query['FirewallVSwitchCidrBlock'] = request.firewall_vswitch_cidr_block
        if not DaraCore.is_null(request.firewall_vpc_cidr_block):
            query['FirewallVpcCidrBlock'] = request.firewall_vpc_cidr_block
        if not DaraCore.is_null(request.firewall_vpc_standby_zone_id):
            query['FirewallVpcStandbyZoneId'] = request.firewall_vpc_standby_zone_id
        if not DaraCore.is_null(request.firewall_vpc_zone_id):
            query['FirewallVpcZoneId'] = request.firewall_vpc_zone_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not DaraCore.is_null(request.vpc_region):
            query['VpcRegion'] = request.vpc_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallCenConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallCenConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_cen_configure(
        self,
        request: main_models.CreateVpcFirewallCenConfigureRequest,
    ) -> main_models.CreateVpcFirewallCenConfigureResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_firewall_cen_configure_with_options(request, runtime)

    async def create_vpc_firewall_cen_configure_async(
        self,
        request: main_models.CreateVpcFirewallCenConfigureRequest,
    ) -> main_models.CreateVpcFirewallCenConfigureResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def create_vpc_firewall_cen_manual_configure_with_options(
        self,
        request: main_models.CreateVpcFirewallCenManualConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallCenManualConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallCenManualConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallCenManualConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_cen_manual_configure_with_options_async(
        self,
        request: main_models.CreateVpcFirewallCenManualConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallCenManualConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallCenManualConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallCenManualConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_cen_manual_configure(
        self,
        request: main_models.CreateVpcFirewallCenManualConfigureRequest,
    ) -> main_models.CreateVpcFirewallCenManualConfigureResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_firewall_cen_manual_configure_with_options(request, runtime)

    async def create_vpc_firewall_cen_manual_configure_async(
        self,
        request: main_models.CreateVpcFirewallCenManualConfigureRequest,
    ) -> main_models.CreateVpcFirewallCenManualConfigureResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_firewall_cen_manual_configure_with_options_async(request, runtime)

    def create_vpc_firewall_configure_with_options(
        self,
        request: main_models.CreateVpcFirewallConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not DaraCore.is_null(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not DaraCore.is_null(request.local_vpc_region):
            query['LocalVpcRegion'] = request.local_vpc_region
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.peer_vpc_region):
            query['PeerVpcRegion'] = request.peer_vpc_region
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_configure_with_options_async(
        self,
        request: main_models.CreateVpcFirewallConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not DaraCore.is_null(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not DaraCore.is_null(request.local_vpc_region):
            query['LocalVpcRegion'] = request.local_vpc_region
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.peer_vpc_region):
            query['PeerVpcRegion'] = request.peer_vpc_region
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_configure(
        self,
        request: main_models.CreateVpcFirewallConfigureRequest,
    ) -> main_models.CreateVpcFirewallConfigureResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_firewall_configure_with_options(request, runtime)

    async def create_vpc_firewall_configure_async(
        self,
        request: main_models.CreateVpcFirewallConfigureRequest,
    ) -> main_models.CreateVpcFirewallConfigureResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_firewall_configure_with_options_async(request, runtime)

    def create_vpc_firewall_control_policy_with_options(
        self,
        request: main_models.CreateVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_control_policy_with_options_async(
        self,
        request: main_models.CreateVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_control_policy(
        self,
        request: main_models.CreateVpcFirewallControlPolicyRequest,
    ) -> main_models.CreateVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_firewall_control_policy_with_options(request, runtime)

    async def create_vpc_firewall_control_policy_async(
        self,
        request: main_models.CreateVpcFirewallControlPolicyRequest,
    ) -> main_models.CreateVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_firewall_control_policy_with_options_async(request, runtime)

    def create_vpc_firewall_precheck_with_options(
        self,
        request: main_models.CreateVpcFirewallPrecheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallPrecheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_type):
            query['NetworkInstanceType'] = request.network_instance_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallPrecheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallPrecheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_precheck_with_options_async(
        self,
        request: main_models.CreateVpcFirewallPrecheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallPrecheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_type):
            query['NetworkInstanceType'] = request.network_instance_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallPrecheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallPrecheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_precheck(
        self,
        request: main_models.CreateVpcFirewallPrecheckRequest,
    ) -> main_models.CreateVpcFirewallPrecheckResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_firewall_precheck_with_options(request, runtime)

    async def create_vpc_firewall_precheck_async(
        self,
        request: main_models.CreateVpcFirewallPrecheckRequest,
    ) -> main_models.CreateVpcFirewallPrecheckResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_firewall_precheck_with_options_async(request, runtime)

    def create_vpc_firewall_task_with_options(
        self,
        request: main_models.CreateVpcFirewallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpc_firewall_task_with_options_async(
        self,
        request: main_models.CreateVpcFirewallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVpcFirewallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVpcFirewallTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVpcFirewallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpc_firewall_task(
        self,
        request: main_models.CreateVpcFirewallTaskRequest,
    ) -> main_models.CreateVpcFirewallTaskResponse:
        runtime = RuntimeOptions()
        return self.create_vpc_firewall_task_with_options(request, runtime)

    async def create_vpc_firewall_task_async(
        self,
        request: main_models.CreateVpcFirewallTaskRequest,
    ) -> main_models.CreateVpcFirewallTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_vpc_firewall_task_with_options_async(request, runtime)

    def delete_ack_cluster_connector_with_options(
        self,
        request: main_models.DeleteAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAckClusterConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ack_cluster_connector_with_options_async(
        self,
        request: main_models.DeleteAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAckClusterConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ack_cluster_connector(
        self,
        request: main_models.DeleteAckClusterConnectorRequest,
    ) -> main_models.DeleteAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return self.delete_ack_cluster_connector_with_options(request, runtime)

    async def delete_ack_cluster_connector_async(
        self,
        request: main_models.DeleteAckClusterConnectorRequest,
    ) -> main_models.DeleteAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return await self.delete_ack_cluster_connector_with_options_async(request, runtime)

    def delete_acl_backup_data_with_options(
        self,
        request: main_models.DeleteAclBackupDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_up_time):
            query['BackUpTime'] = request.back_up_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAclBackupData',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclBackupDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acl_backup_data_with_options_async(
        self,
        request: main_models.DeleteAclBackupDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAclBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_up_time):
            query['BackUpTime'] = request.back_up_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAclBackupData',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAclBackupDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acl_backup_data(
        self,
        request: main_models.DeleteAclBackupDataRequest,
    ) -> main_models.DeleteAclBackupDataResponse:
        runtime = RuntimeOptions()
        return self.delete_acl_backup_data_with_options(request, runtime)

    async def delete_acl_backup_data_async(
        self,
        request: main_models.DeleteAclBackupDataRequest,
    ) -> main_models.DeleteAclBackupDataResponse:
        runtime = RuntimeOptions()
        return await self.delete_acl_backup_data_with_options_async(request, runtime)

    def delete_address_book_with_options(
        self,
        request: main_models.DeleteAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_address_book_with_options_async(
        self,
        request: main_models.DeleteAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_address_book(
        self,
        request: main_models.DeleteAddressBookRequest,
    ) -> main_models.DeleteAddressBookResponse:
        runtime = RuntimeOptions()
        return self.delete_address_book_with_options(request, runtime)

    async def delete_address_book_async(
        self,
        request: main_models.DeleteAddressBookRequest,
    ) -> main_models.DeleteAddressBookResponse:
        runtime = RuntimeOptions()
        return await self.delete_address_book_with_options_async(request, runtime)

    def delete_control_policy_with_options(
        self,
        request: main_models.DeleteControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_policy_with_options_async(
        self,
        request: main_models.DeleteControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_control_policy(
        self,
        request: main_models.DeleteControlPolicyRequest,
    ) -> main_models.DeleteControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    async def delete_control_policy_async(
        self,
        request: main_models.DeleteControlPolicyRequest,
    ) -> main_models.DeleteControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_control_policy_template_with_options(
        self,
        request: main_models.DeleteControlPolicyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlPolicyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlPolicyTemplate',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlPolicyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_policy_template_with_options_async(
        self,
        request: main_models.DeleteControlPolicyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteControlPolicyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteControlPolicyTemplate',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteControlPolicyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_control_policy_template(
        self,
        request: main_models.DeleteControlPolicyTemplateRequest,
    ) -> main_models.DeleteControlPolicyTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_control_policy_template_with_options(request, runtime)

    async def delete_control_policy_template_async(
        self,
        request: main_models.DeleteControlPolicyTemplateRequest,
    ) -> main_models.DeleteControlPolicyTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_control_policy_template_with_options_async(request, runtime)

    def delete_dns_firewall_policy_with_options(
        self,
        request: main_models.DeleteDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsFirewallPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dns_firewall_policy_with_options_async(
        self,
        request: main_models.DeleteDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDnsFirewallPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dns_firewall_policy(
        self,
        request: main_models.DeleteDnsFirewallPolicyRequest,
    ) -> main_models.DeleteDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_dns_firewall_policy_with_options(request, runtime)

    async def delete_dns_firewall_policy_async(
        self,
        request: main_models.DeleteDnsFirewallPolicyRequest,
    ) -> main_models.DeleteDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_dns_firewall_policy_with_options_async(request, runtime)

    def delete_download_task_with_options(
        self,
        request: main_models.DeleteDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDownloadTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_download_task_with_options_async(
        self,
        request: main_models.DeleteDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDownloadTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_download_task(
        self,
        request: main_models.DeleteDownloadTaskRequest,
    ) -> main_models.DeleteDownloadTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_download_task_with_options(request, runtime)

    async def delete_download_task_async(
        self,
        request: main_models.DeleteDownloadTaskRequest,
    ) -> main_models.DeleteDownloadTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_download_task_with_options_async(request, runtime)

    def delete_firewall_v2route_policies_with_options(
        self,
        request: main_models.DeleteFirewallV2RoutePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallV2RoutePoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallV2RoutePolicies',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallV2RoutePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_firewall_v2route_policies_with_options_async(
        self,
        request: main_models.DeleteFirewallV2RoutePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFirewallV2RoutePoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFirewallV2RoutePolicies',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFirewallV2RoutePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_firewall_v2route_policies(
        self,
        request: main_models.DeleteFirewallV2RoutePoliciesRequest,
    ) -> main_models.DeleteFirewallV2RoutePoliciesResponse:
        runtime = RuntimeOptions()
        return self.delete_firewall_v2route_policies_with_options(request, runtime)

    async def delete_firewall_v2route_policies_async(
        self,
        request: main_models.DeleteFirewallV2RoutePoliciesRequest,
    ) -> main_models.DeleteFirewallV2RoutePoliciesResponse:
        runtime = RuntimeOptions()
        return await self.delete_firewall_v2route_policies_with_options_async(request, runtime)

    def delete_instance_members_with_options(
        self,
        request: main_models.DeleteInstanceMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_uids):
            query['MemberUids'] = request.member_uids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceMembers',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_members_with_options_async(
        self,
        request: main_models.DeleteInstanceMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_uids):
            query['MemberUids'] = request.member_uids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceMembers',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_members(
        self,
        request: main_models.DeleteInstanceMembersRequest,
    ) -> main_models.DeleteInstanceMembersResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_members_with_options(request, runtime)

    async def delete_instance_members_async(
        self,
        request: main_models.DeleteInstanceMembersRequest,
    ) -> main_models.DeleteInstanceMembersResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_members_with_options_async(request, runtime)

    def delete_ips_private_assoc_with_options(
        self,
        request: main_models.DeleteIpsPrivateAssocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpsPrivateAssocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpsPrivateAssoc',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpsPrivateAssocResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ips_private_assoc_with_options_async(
        self,
        request: main_models.DeleteIpsPrivateAssocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpsPrivateAssocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpsPrivateAssoc',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpsPrivateAssocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ips_private_assoc(
        self,
        request: main_models.DeleteIpsPrivateAssocRequest,
    ) -> main_models.DeleteIpsPrivateAssocResponse:
        runtime = RuntimeOptions()
        return self.delete_ips_private_assoc_with_options(request, runtime)

    async def delete_ips_private_assoc_async(
        self,
        request: main_models.DeleteIpsPrivateAssocRequest,
    ) -> main_models.DeleteIpsPrivateAssocResponse:
        runtime = RuntimeOptions()
        return await self.delete_ips_private_assoc_with_options_async(request, runtime)

    def delete_nat_firewall_control_policy_with_options(
        self,
        request: main_models.DeleteNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nat_firewall_control_policy_with_options_async(
        self,
        request: main_models.DeleteNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nat_firewall_control_policy(
        self,
        request: main_models.DeleteNatFirewallControlPolicyRequest,
    ) -> main_models.DeleteNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_nat_firewall_control_policy_with_options(request, runtime)

    async def delete_nat_firewall_control_policy_async(
        self,
        request: main_models.DeleteNatFirewallControlPolicyRequest,
    ) -> main_models.DeleteNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_nat_firewall_control_policy_with_options_async(request, runtime)

    def delete_nat_firewall_control_policy_batch_with_options(
        self,
        request: main_models.DeleteNatFirewallControlPolicyBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNatFirewallControlPolicyBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNatFirewallControlPolicyBatch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNatFirewallControlPolicyBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nat_firewall_control_policy_batch_with_options_async(
        self,
        request: main_models.DeleteNatFirewallControlPolicyBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNatFirewallControlPolicyBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid_list):
            query['AclUuidList'] = request.acl_uuid_list
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNatFirewallControlPolicyBatch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNatFirewallControlPolicyBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nat_firewall_control_policy_batch(
        self,
        request: main_models.DeleteNatFirewallControlPolicyBatchRequest,
    ) -> main_models.DeleteNatFirewallControlPolicyBatchResponse:
        runtime = RuntimeOptions()
        return self.delete_nat_firewall_control_policy_batch_with_options(request, runtime)

    async def delete_nat_firewall_control_policy_batch_async(
        self,
        request: main_models.DeleteNatFirewallControlPolicyBatchRequest,
    ) -> main_models.DeleteNatFirewallControlPolicyBatchResponse:
        runtime = RuntimeOptions()
        return await self.delete_nat_firewall_control_policy_batch_with_options_async(request, runtime)

    def delete_private_dns_all_domain_name_with_options(
        self,
        request: main_models.DeletePrivateDnsAllDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDnsAllDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDnsAllDomainName',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDnsAllDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_dns_all_domain_name_with_options_async(
        self,
        request: main_models.DeletePrivateDnsAllDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDnsAllDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDnsAllDomainName',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDnsAllDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_dns_all_domain_name(
        self,
        request: main_models.DeletePrivateDnsAllDomainNameRequest,
    ) -> main_models.DeletePrivateDnsAllDomainNameResponse:
        runtime = RuntimeOptions()
        return self.delete_private_dns_all_domain_name_with_options(request, runtime)

    async def delete_private_dns_all_domain_name_async(
        self,
        request: main_models.DeletePrivateDnsAllDomainNameRequest,
    ) -> main_models.DeletePrivateDnsAllDomainNameResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_dns_all_domain_name_with_options_async(request, runtime)

    def delete_private_dns_domain_name_with_options(
        self,
        request: main_models.DeletePrivateDnsDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDnsDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.domain_name_list):
            query['DomainNameList'] = request.domain_name_list
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDnsDomainName',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDnsDomainNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_dns_domain_name_with_options_async(
        self,
        request: main_models.DeletePrivateDnsDomainNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDnsDomainNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.domain_name_list):
            query['DomainNameList'] = request.domain_name_list
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDnsDomainName',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDnsDomainNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_dns_domain_name(
        self,
        request: main_models.DeletePrivateDnsDomainNameRequest,
    ) -> main_models.DeletePrivateDnsDomainNameResponse:
        runtime = RuntimeOptions()
        return self.delete_private_dns_domain_name_with_options(request, runtime)

    async def delete_private_dns_domain_name_async(
        self,
        request: main_models.DeletePrivateDnsDomainNameRequest,
    ) -> main_models.DeletePrivateDnsDomainNameResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_dns_domain_name_with_options_async(request, runtime)

    def delete_private_dns_endpoint_with_options(
        self,
        request: main_models.DeletePrivateDnsEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDnsEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDnsEndpoint',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDnsEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_dns_endpoint_with_options_async(
        self,
        request: main_models.DeletePrivateDnsEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateDnsEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateDnsEndpoint',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateDnsEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_dns_endpoint(
        self,
        request: main_models.DeletePrivateDnsEndpointRequest,
    ) -> main_models.DeletePrivateDnsEndpointResponse:
        runtime = RuntimeOptions()
        return self.delete_private_dns_endpoint_with_options(request, runtime)

    async def delete_private_dns_endpoint_async(
        self,
        request: main_models.DeletePrivateDnsEndpointRequest,
    ) -> main_models.DeletePrivateDnsEndpointResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_dns_endpoint_with_options_async(request, runtime)

    def delete_security_proxy_with_options(
        self,
        request: main_models.DeleteSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_proxy_with_options_async(
        self,
        request: main_models.DeleteSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_proxy(
        self,
        request: main_models.DeleteSecurityProxyRequest,
    ) -> main_models.DeleteSecurityProxyResponse:
        runtime = RuntimeOptions()
        return self.delete_security_proxy_with_options(request, runtime)

    async def delete_security_proxy_async(
        self,
        request: main_models.DeleteSecurityProxyRequest,
    ) -> main_models.DeleteSecurityProxyResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_proxy_with_options_async(request, runtime)

    def delete_tr_firewall_v2with_options(
        self,
        request: main_models.DeleteTrFirewallV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrFirewallV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrFirewallV2',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrFirewallV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_tr_firewall_v2with_options_async(
        self,
        request: main_models.DeleteTrFirewallV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTrFirewallV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrFirewallV2',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTrFirewallV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tr_firewall_v2(
        self,
        request: main_models.DeleteTrFirewallV2Request,
    ) -> main_models.DeleteTrFirewallV2Response:
        runtime = RuntimeOptions()
        return self.delete_tr_firewall_v2with_options(request, runtime)

    async def delete_tr_firewall_v2_async(
        self,
        request: main_models.DeleteTrFirewallV2Request,
    ) -> main_models.DeleteTrFirewallV2Response:
        runtime = RuntimeOptions()
        return await self.delete_tr_firewall_v2with_options_async(request, runtime)

    def delete_vpc_firewall_cen_configure_with_options(
        self,
        request: main_models.DeleteVpcFirewallCenConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcFirewallCenConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcFirewallCenConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcFirewallCenConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_firewall_cen_configure_with_options_async(
        self,
        request: main_models.DeleteVpcFirewallCenConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcFirewallCenConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcFirewallCenConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcFirewallCenConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_firewall_cen_configure(
        self,
        request: main_models.DeleteVpcFirewallCenConfigureRequest,
    ) -> main_models.DeleteVpcFirewallCenConfigureResponse:
        runtime = RuntimeOptions()
        return self.delete_vpc_firewall_cen_configure_with_options(request, runtime)

    async def delete_vpc_firewall_cen_configure_async(
        self,
        request: main_models.DeleteVpcFirewallCenConfigureRequest,
    ) -> main_models.DeleteVpcFirewallCenConfigureResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def delete_vpc_firewall_configure_with_options(
        self,
        request: main_models.DeleteVpcFirewallConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcFirewallConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcFirewallConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcFirewallConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_firewall_configure_with_options_async(
        self,
        request: main_models.DeleteVpcFirewallConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcFirewallConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id_list):
            query['VpcFirewallIdList'] = request.vpc_firewall_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcFirewallConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcFirewallConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_firewall_configure(
        self,
        request: main_models.DeleteVpcFirewallConfigureRequest,
    ) -> main_models.DeleteVpcFirewallConfigureResponse:
        runtime = RuntimeOptions()
        return self.delete_vpc_firewall_configure_with_options(request, runtime)

    async def delete_vpc_firewall_configure_async(
        self,
        request: main_models.DeleteVpcFirewallConfigureRequest,
    ) -> main_models.DeleteVpcFirewallConfigureResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpc_firewall_configure_with_options_async(request, runtime)

    def delete_vpc_firewall_control_policy_with_options(
        self,
        request: main_models.DeleteVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpc_firewall_control_policy_with_options_async(
        self,
        request: main_models.DeleteVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpc_firewall_control_policy(
        self,
        request: main_models.DeleteVpcFirewallControlPolicyRequest,
    ) -> main_models.DeleteVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_vpc_firewall_control_policy_with_options(request, runtime)

    async def delete_vpc_firewall_control_policy_async(
        self,
        request: main_models.DeleteVpcFirewallControlPolicyRequest,
    ) -> main_models.DeleteVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_vpc_firewall_control_policy_with_options_async(request, runtime)

    def describe_aclprotect_trend_with_options(
        self,
        request: main_models.DescribeACLProtectTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeACLProtectTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeACLProtectTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeACLProtectTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aclprotect_trend_with_options_async(
        self,
        request: main_models.DescribeACLProtectTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeACLProtectTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeACLProtectTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeACLProtectTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aclprotect_trend(
        self,
        request: main_models.DescribeACLProtectTrendRequest,
    ) -> main_models.DescribeACLProtectTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_aclprotect_trend_with_options(request, runtime)

    async def describe_aclprotect_trend_async(
        self,
        request: main_models.DescribeACLProtectTrendRequest,
    ) -> main_models.DescribeACLProtectTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_aclprotect_trend_with_options_async(request, runtime)

    def describe_aitraffic_analysis_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAITrafficAnalysisStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAITrafficAnalysisStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAITrafficAnalysisStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aitraffic_analysis_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAITrafficAnalysisStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeAITrafficAnalysisStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAITrafficAnalysisStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aitraffic_analysis_status(self) -> main_models.DescribeAITrafficAnalysisStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_aitraffic_analysis_status_with_options(runtime)

    async def describe_aitraffic_analysis_status_async(self) -> main_models.DescribeAITrafficAnalysisStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_aitraffic_analysis_status_with_options_async(runtime)

    def describe_access_instance_region_list_with_options(
        self,
        request: main_models.DescribeAccessInstanceRegionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceRegionListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceRegionList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_instance_region_list_with_options_async(
        self,
        request: main_models.DescribeAccessInstanceRegionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceRegionListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceRegionList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_instance_region_list(
        self,
        request: main_models.DescribeAccessInstanceRegionListRequest,
    ) -> main_models.DescribeAccessInstanceRegionListResponse:
        runtime = RuntimeOptions()
        return self.describe_access_instance_region_list_with_options(request, runtime)

    async def describe_access_instance_region_list_async(
        self,
        request: main_models.DescribeAccessInstanceRegionListRequest,
    ) -> main_models.DescribeAccessInstanceRegionListResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_instance_region_list_with_options_async(request, runtime)

    def describe_access_instance_task_with_options(
        self,
        request: main_models.DescribeAccessInstanceTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_instance_task_with_options_async(
        self,
        request: main_models.DescribeAccessInstanceTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_instance_task(
        self,
        request: main_models.DescribeAccessInstanceTaskRequest,
    ) -> main_models.DescribeAccessInstanceTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_access_instance_task_with_options(request, runtime)

    async def describe_access_instance_task_async(
        self,
        request: main_models.DescribeAccessInstanceTaskRequest,
    ) -> main_models.DescribeAccessInstanceTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_instance_task_with_options_async(request, runtime)

    def describe_access_instance_vswitch_list_with_options(
        self,
        request: main_models.DescribeAccessInstanceVSwitchListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceVSwitchListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceVSwitchList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceVSwitchListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_instance_vswitch_list_with_options_async(
        self,
        request: main_models.DescribeAccessInstanceVSwitchListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceVSwitchListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceVSwitchList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceVSwitchListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_instance_vswitch_list(
        self,
        request: main_models.DescribeAccessInstanceVSwitchListRequest,
    ) -> main_models.DescribeAccessInstanceVSwitchListResponse:
        runtime = RuntimeOptions()
        return self.describe_access_instance_vswitch_list_with_options(request, runtime)

    async def describe_access_instance_vswitch_list_async(
        self,
        request: main_models.DescribeAccessInstanceVSwitchListRequest,
    ) -> main_models.DescribeAccessInstanceVSwitchListResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_instance_vswitch_list_with_options_async(request, runtime)

    def describe_access_instance_vpc_list_with_options(
        self,
        request: main_models.DescribeAccessInstanceVpcListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceVpcListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceVpcList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceVpcListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_instance_vpc_list_with_options_async(
        self,
        request: main_models.DescribeAccessInstanceVpcListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceVpcListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceVpcList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceVpcListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_instance_vpc_list(
        self,
        request: main_models.DescribeAccessInstanceVpcListRequest,
    ) -> main_models.DescribeAccessInstanceVpcListResponse:
        runtime = RuntimeOptions()
        return self.describe_access_instance_vpc_list_with_options(request, runtime)

    async def describe_access_instance_vpc_list_async(
        self,
        request: main_models.DescribeAccessInstanceVpcListRequest,
    ) -> main_models.DescribeAccessInstanceVpcListResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_instance_vpc_list_with_options_async(request, runtime)

    def describe_access_instance_zone_list_with_options(
        self,
        request: main_models.DescribeAccessInstanceZoneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceZoneListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceZoneList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceZoneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_instance_zone_list_with_options_async(
        self,
        request: main_models.DescribeAccessInstanceZoneListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessInstanceZoneListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessInstanceZoneList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessInstanceZoneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_instance_zone_list(
        self,
        request: main_models.DescribeAccessInstanceZoneListRequest,
    ) -> main_models.DescribeAccessInstanceZoneListResponse:
        runtime = RuntimeOptions()
        return self.describe_access_instance_zone_list_with_options(request, runtime)

    async def describe_access_instance_zone_list_async(
        self,
        request: main_models.DescribeAccessInstanceZoneListRequest,
    ) -> main_models.DescribeAccessInstanceZoneListResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_instance_zone_list_with_options_async(request, runtime)

    def describe_ack_cluster_connector_with_options(
        self,
        request: main_models.DescribeAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ack_cluster_connector_with_options_async(
        self,
        request: main_models.DescribeAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ack_cluster_connector(
        self,
        request: main_models.DescribeAckClusterConnectorRequest,
    ) -> main_models.DescribeAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return self.describe_ack_cluster_connector_with_options(request, runtime)

    async def describe_ack_cluster_connector_async(
        self,
        request: main_models.DescribeAckClusterConnectorRequest,
    ) -> main_models.DescribeAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return await self.describe_ack_cluster_connector_with_options_async(request, runtime)

    def describe_ack_cluster_connectors_with_options(
        self,
        request: main_models.DescribeAckClusterConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.connector_name):
            query['ConnectorName'] = request.connector_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterConnectors',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ack_cluster_connectors_with_options_async(
        self,
        request: main_models.DescribeAckClusterConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterConnectorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.connector_name):
            query['ConnectorName'] = request.connector_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterConnectors',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ack_cluster_connectors(
        self,
        request: main_models.DescribeAckClusterConnectorsRequest,
    ) -> main_models.DescribeAckClusterConnectorsResponse:
        runtime = RuntimeOptions()
        return self.describe_ack_cluster_connectors_with_options(request, runtime)

    async def describe_ack_cluster_connectors_async(
        self,
        request: main_models.DescribeAckClusterConnectorsRequest,
    ) -> main_models.DescribeAckClusterConnectorsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ack_cluster_connectors_with_options_async(request, runtime)

    def describe_ack_cluster_namespaces_with_options(
        self,
        request: main_models.DescribeAckClusterNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterNamespaces',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ack_cluster_namespaces_with_options_async(
        self,
        request: main_models.DescribeAckClusterNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterNamespaces',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ack_cluster_namespaces(
        self,
        request: main_models.DescribeAckClusterNamespacesRequest,
    ) -> main_models.DescribeAckClusterNamespacesResponse:
        runtime = RuntimeOptions()
        return self.describe_ack_cluster_namespaces_with_options(request, runtime)

    async def describe_ack_cluster_namespaces_async(
        self,
        request: main_models.DescribeAckClusterNamespacesRequest,
    ) -> main_models.DescribeAckClusterNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.describe_ack_cluster_namespaces_with_options_async(request, runtime)

    def describe_ack_cluster_pod_labels_with_options(
        self,
        request: main_models.DescribeAckClusterPodLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterPodLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterPodLabels',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterPodLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ack_cluster_pod_labels_with_options_async(
        self,
        request: main_models.DescribeAckClusterPodLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClusterPodLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusterPodLabels',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClusterPodLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ack_cluster_pod_labels(
        self,
        request: main_models.DescribeAckClusterPodLabelsRequest,
    ) -> main_models.DescribeAckClusterPodLabelsResponse:
        runtime = RuntimeOptions()
        return self.describe_ack_cluster_pod_labels_with_options(request, runtime)

    async def describe_ack_cluster_pod_labels_async(
        self,
        request: main_models.DescribeAckClusterPodLabelsRequest,
    ) -> main_models.DescribeAckClusterPodLabelsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ack_cluster_pod_labels_with_options_async(request, runtime)

    def describe_ack_clusters_with_options(
        self,
        request: main_models.DescribeAckClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_spec):
            query['ClusterSpec'] = request.cluster_spec
        if not DaraCore.is_null(request.connector_status):
            query['ConnectorStatus'] = request.connector_status
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusters',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ack_clusters_with_options_async(
        self,
        request: main_models.DescribeAckClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAckClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_spec):
            query['ClusterSpec'] = request.cluster_spec
        if not DaraCore.is_null(request.connector_status):
            query['ConnectorStatus'] = request.connector_status
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAckClusters',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAckClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ack_clusters(
        self,
        request: main_models.DescribeAckClustersRequest,
    ) -> main_models.DescribeAckClustersResponse:
        runtime = RuntimeOptions()
        return self.describe_ack_clusters_with_options(request, runtime)

    async def describe_ack_clusters_async(
        self,
        request: main_models.DescribeAckClustersRequest,
    ) -> main_models.DescribeAckClustersResponse:
        runtime = RuntimeOptions()
        return await self.describe_ack_clusters_with_options_async(request, runtime)

    def describe_acl_apps_with_options(
        self,
        request: main_models.DescribeAclAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclAppsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclApps',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_apps_with_options_async(
        self,
        request: main_models.DescribeAclAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclAppsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclApps',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_apps(
        self,
        request: main_models.DescribeAclAppsRequest,
    ) -> main_models.DescribeAclAppsResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_apps_with_options(request, runtime)

    async def describe_acl_apps_async(
        self,
        request: main_models.DescribeAclAppsRequest,
    ) -> main_models.DescribeAclAppsResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_apps_with_options_async(request, runtime)

    def describe_acl_backup_list_with_options(
        self,
        request: main_models.DescribeAclBackupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclBackupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclBackupList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_backup_list_with_options_async(
        self,
        request: main_models.DescribeAclBackupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclBackupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclBackupList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclBackupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_backup_list(
        self,
        request: main_models.DescribeAclBackupListRequest,
    ) -> main_models.DescribeAclBackupListResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_backup_list_with_options(request, runtime)

    async def describe_acl_backup_list_async(
        self,
        request: main_models.DescribeAclBackupListRequest,
    ) -> main_models.DescribeAclBackupListResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_backup_list_with_options_async(request, runtime)

    def describe_acl_check_with_options(
        self,
        request: main_models.DescribeAclCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclCheckResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclCheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_check_with_options_async(
        self,
        request: main_models.DescribeAclCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclCheckResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclCheck',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_check(
        self,
        request: main_models.DescribeAclCheckRequest,
    ) -> main_models.DescribeAclCheckResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_check_with_options(request, runtime)

    async def describe_acl_check_async(
        self,
        request: main_models.DescribeAclCheckRequest,
    ) -> main_models.DescribeAclCheckResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_check_with_options_async(request, runtime)

    def describe_acl_check_quota_with_options(
        self,
        request: main_models.DescribeAclCheckQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclCheckQuotaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclCheckQuota',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclCheckQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_check_quota_with_options_async(
        self,
        request: main_models.DescribeAclCheckQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclCheckQuotaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclCheckQuota',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclCheckQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_check_quota(
        self,
        request: main_models.DescribeAclCheckQuotaRequest,
    ) -> main_models.DescribeAclCheckQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_check_quota_with_options(request, runtime)

    async def describe_acl_check_quota_async(
        self,
        request: main_models.DescribeAclCheckQuotaRequest,
    ) -> main_models.DescribeAclCheckQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_check_quota_with_options_async(request, runtime)

    def describe_acl_checks_with_options(
        self,
        request: main_models.DescribeAclChecksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclChecksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclChecks',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclChecksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_checks_with_options_async(
        self,
        request: main_models.DescribeAclChecksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclChecksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclChecks',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclChecksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_checks(
        self,
        request: main_models.DescribeAclChecksRequest,
    ) -> main_models.DescribeAclChecksResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_checks_with_options(request, runtime)

    async def describe_acl_checks_async(
        self,
        request: main_models.DescribeAclChecksRequest,
    ) -> main_models.DescribeAclChecksResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_checks_with_options_async(request, runtime)

    def describe_acl_rule_count_with_options(
        self,
        request: main_models.DescribeAclRuleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclRuleCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclRuleCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclRuleCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_rule_count_with_options_async(
        self,
        request: main_models.DescribeAclRuleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclRuleCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclRuleCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclRuleCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_rule_count(
        self,
        request: main_models.DescribeAclRuleCountRequest,
    ) -> main_models.DescribeAclRuleCountResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_rule_count_with_options(request, runtime)

    async def describe_acl_rule_count_async(
        self,
        request: main_models.DescribeAclRuleCountRequest,
    ) -> main_models.DescribeAclRuleCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_rule_count_with_options_async(request, runtime)

    def describe_acl_whitelist_with_options(
        self,
        request: main_models.DescribeAclWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_acl_whitelist_with_options_async(
        self,
        request: main_models.DescribeAclWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAclWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAclWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAclWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_acl_whitelist(
        self,
        request: main_models.DescribeAclWhitelistRequest,
    ) -> main_models.DescribeAclWhitelistResponse:
        runtime = RuntimeOptions()
        return self.describe_acl_whitelist_with_options(request, runtime)

    async def describe_acl_whitelist_async(
        self,
        request: main_models.DescribeAclWhitelistRequest,
    ) -> main_models.DescribeAclWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.describe_acl_whitelist_with_options_async(request, runtime)

    def describe_address_book_with_options(
        self,
        request: main_models.DescribeAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contain_port):
            query['ContainPort'] = request.contain_port
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_address_book_with_options_async(
        self,
        request: main_models.DescribeAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contain_port):
            query['ContainPort'] = request.contain_port
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_address_book(
        self,
        request: main_models.DescribeAddressBookRequest,
    ) -> main_models.DescribeAddressBookResponse:
        runtime = RuntimeOptions()
        return self.describe_address_book_with_options(request, runtime)

    async def describe_address_book_async(
        self,
        request: main_models.DescribeAddressBookRequest,
    ) -> main_models.DescribeAddressBookResponse:
        runtime = RuntimeOptions()
        return await self.describe_address_book_with_options_async(request, runtime)

    def describe_asset_list_with_options(
        self,
        request: main_models.DescribeAssetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.new_resource_tag):
            query['NewResourceTag'] = request.new_resource_tag
        if not DaraCore.is_null(request.out_statistic):
            query['OutStatistic'] = request.out_statistic
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.search_item):
            query['SearchItem'] = request.search_item
        if not DaraCore.is_null(request.sensitive_status):
            query['SensitiveStatus'] = request.sensitive_status
        if not DaraCore.is_null(request.sg_status):
            query['SgStatus'] = request.sg_status
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_list_with_options_async(
        self,
        request: main_models.DescribeAssetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.new_resource_tag):
            query['NewResourceTag'] = request.new_resource_tag
        if not DaraCore.is_null(request.out_statistic):
            query['OutStatistic'] = request.out_statistic
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.search_item):
            query['SearchItem'] = request.search_item
        if not DaraCore.is_null(request.sensitive_status):
            query['SensitiveStatus'] = request.sensitive_status
        if not DaraCore.is_null(request.sg_status):
            query['SgStatus'] = request.sg_status
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_list(
        self,
        request: main_models.DescribeAssetListRequest,
    ) -> main_models.DescribeAssetListResponse:
        runtime = RuntimeOptions()
        return self.describe_asset_list_with_options(request, runtime)

    async def describe_asset_list_async(
        self,
        request: main_models.DescribeAssetListRequest,
    ) -> main_models.DescribeAssetListResponse:
        runtime = RuntimeOptions()
        return await self.describe_asset_list_with_options_async(request, runtime)

    def describe_asset_risk_list_with_options(
        self,
        request: main_models.DescribeAssetRiskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetRiskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetRiskList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetRiskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_risk_list_with_options_async(
        self,
        request: main_models.DescribeAssetRiskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetRiskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_addr_list):
            query['IpAddrList'] = request.ip_addr_list
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetRiskList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetRiskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_risk_list(
        self,
        request: main_models.DescribeAssetRiskListRequest,
    ) -> main_models.DescribeAssetRiskListResponse:
        runtime = RuntimeOptions()
        return self.describe_asset_risk_list_with_options(request, runtime)

    async def describe_asset_risk_list_async(
        self,
        request: main_models.DescribeAssetRiskListRequest,
    ) -> main_models.DescribeAssetRiskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_asset_risk_list_with_options_async(request, runtime)

    def describe_asset_statistic_with_options(
        self,
        request: main_models.DescribeAssetStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asset_statistic_with_options_async(
        self,
        request: main_models.DescribeAssetStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAssetStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAssetStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAssetStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asset_statistic(
        self,
        request: main_models.DescribeAssetStatisticRequest,
    ) -> main_models.DescribeAssetStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_asset_statistic_with_options(request, runtime)

    async def describe_asset_statistic_async(
        self,
        request: main_models.DescribeAssetStatisticRequest,
    ) -> main_models.DescribeAssetStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_asset_statistic_with_options_async(request, runtime)

    def describe_attack_app_category_with_options(
        self,
        request: main_models.DescribeAttackAppCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttackAppCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttackAppCategory',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttackAppCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_app_category_with_options_async(
        self,
        request: main_models.DescribeAttackAppCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttackAppCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttackAppCategory',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttackAppCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_app_category(
        self,
        request: main_models.DescribeAttackAppCategoryRequest,
    ) -> main_models.DescribeAttackAppCategoryResponse:
        runtime = RuntimeOptions()
        return self.describe_attack_app_category_with_options(request, runtime)

    async def describe_attack_app_category_async(
        self,
        request: main_models.DescribeAttackAppCategoryRequest,
    ) -> main_models.DescribeAttackAppCategoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_attack_app_category_with_options_async(request, runtime)

    def describe_batch_sls_dispatch_status_with_options(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchSlsDispatchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchSlsDispatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_batch_sls_dispatch_status_with_options_async(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBatchSlsDispatchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBatchSlsDispatchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_batch_sls_dispatch_status(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_batch_sls_dispatch_status_with_options(request, runtime)

    async def describe_batch_sls_dispatch_status_async(
        self,
        request: main_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> main_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_batch_sls_dispatch_status_with_options_async(request, runtime)

    def describe_cfw_risk_level_summary_with_options(
        self,
        request: main_models.DescribeCfwRiskLevelSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCfwRiskLevelSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCfwRiskLevelSummary',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCfwRiskLevelSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cfw_risk_level_summary_with_options_async(
        self,
        request: main_models.DescribeCfwRiskLevelSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCfwRiskLevelSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCfwRiskLevelSummary',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCfwRiskLevelSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cfw_risk_level_summary(
        self,
        request: main_models.DescribeCfwRiskLevelSummaryRequest,
    ) -> main_models.DescribeCfwRiskLevelSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_cfw_risk_level_summary_with_options(request, runtime)

    async def describe_cfw_risk_level_summary_async(
        self,
        request: main_models.DescribeCfwRiskLevelSummaryRequest,
    ) -> main_models.DescribeCfwRiskLevelSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_cfw_risk_level_summary_with_options_async(request, runtime)

    def describe_clear_auth_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClearAuthInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeClearAuthInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClearAuthInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clear_auth_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClearAuthInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeClearAuthInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClearAuthInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clear_auth_info(self) -> main_models.DescribeClearAuthInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_clear_auth_info_with_options(runtime)

    async def describe_clear_auth_info_async(self) -> main_models.DescribeClearAuthInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_clear_auth_info_with_options_async(runtime)

    def describe_configured_destination_ipwith_options(
        self,
        request: main_models.DescribeConfiguredDestinationIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfiguredDestinationIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.destination_ip):
            query['DestinationIP'] = request.destination_ip
        if not DaraCore.is_null(request.destination_isp):
            query['DestinationISP'] = request.destination_isp
        if not DaraCore.is_null(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfiguredDestinationIP',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfiguredDestinationIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configured_destination_ipwith_options_async(
        self,
        request: main_models.DescribeConfiguredDestinationIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfiguredDestinationIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.destination_ip):
            query['DestinationIP'] = request.destination_ip
        if not DaraCore.is_null(request.destination_isp):
            query['DestinationISP'] = request.destination_isp
        if not DaraCore.is_null(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfiguredDestinationIP',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfiguredDestinationIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configured_destination_ip(
        self,
        request: main_models.DescribeConfiguredDestinationIPRequest,
    ) -> main_models.DescribeConfiguredDestinationIPResponse:
        runtime = RuntimeOptions()
        return self.describe_configured_destination_ipwith_options(request, runtime)

    async def describe_configured_destination_ip_async(
        self,
        request: main_models.DescribeConfiguredDestinationIPRequest,
    ) -> main_models.DescribeConfiguredDestinationIPResponse:
        runtime = RuntimeOptions()
        return await self.describe_configured_destination_ipwith_options_async(request, runtime)

    def describe_configured_domain_names_with_options(
        self,
        request: main_models.DescribeConfiguredDomainNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfiguredDomainNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfiguredDomainNames',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfiguredDomainNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configured_domain_names_with_options_async(
        self,
        request: main_models.DescribeConfiguredDomainNamesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfiguredDomainNamesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfiguredDomainNames',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfiguredDomainNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configured_domain_names(
        self,
        request: main_models.DescribeConfiguredDomainNamesRequest,
    ) -> main_models.DescribeConfiguredDomainNamesResponse:
        runtime = RuntimeOptions()
        return self.describe_configured_domain_names_with_options(request, runtime)

    async def describe_configured_domain_names_async(
        self,
        request: main_models.DescribeConfiguredDomainNamesRequest,
    ) -> main_models.DescribeConfiguredDomainNamesResponse:
        runtime = RuntimeOptions()
        return await self.describe_configured_domain_names_with_options_async(request, runtime)

    def describe_control_policy_with_options(
        self,
        request: main_models.DescribeControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_control_policy_with_options_async(
        self,
        request: main_models.DescribeControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_control_policy(
        self,
        request: main_models.DescribeControlPolicyRequest,
    ) -> main_models.DescribeControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_control_policy_with_options(request, runtime)

    async def describe_control_policy_async(
        self,
        request: main_models.DescribeControlPolicyRequest,
    ) -> main_models.DescribeControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_control_policy_with_options_async(request, runtime)

    def describe_control_policy_domain_resolve_with_options(
        self,
        request: main_models.DescribeControlPolicyDomainResolveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeControlPolicyDomainResolveResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeControlPolicyDomainResolve',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeControlPolicyDomainResolveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_control_policy_domain_resolve_with_options_async(
        self,
        request: main_models.DescribeControlPolicyDomainResolveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeControlPolicyDomainResolveResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeControlPolicyDomainResolve',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeControlPolicyDomainResolveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_control_policy_domain_resolve(
        self,
        request: main_models.DescribeControlPolicyDomainResolveRequest,
    ) -> main_models.DescribeControlPolicyDomainResolveResponse:
        runtime = RuntimeOptions()
        return self.describe_control_policy_domain_resolve_with_options(request, runtime)

    async def describe_control_policy_domain_resolve_async(
        self,
        request: main_models.DescribeControlPolicyDomainResolveRequest,
    ) -> main_models.DescribeControlPolicyDomainResolveResponse:
        runtime = RuntimeOptions()
        return await self.describe_control_policy_domain_resolve_with_options_async(request, runtime)

    def describe_created_nat_firewall_with_options(
        self,
        request: main_models.DescribeCreatedNatFirewallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCreatedNatFirewallResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCreatedNatFirewall',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCreatedNatFirewallResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_created_nat_firewall_with_options_async(
        self,
        request: main_models.DescribeCreatedNatFirewallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCreatedNatFirewallResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCreatedNatFirewall',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCreatedNatFirewallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_created_nat_firewall(
        self,
        request: main_models.DescribeCreatedNatFirewallRequest,
    ) -> main_models.DescribeCreatedNatFirewallResponse:
        runtime = RuntimeOptions()
        return self.describe_created_nat_firewall_with_options(request, runtime)

    async def describe_created_nat_firewall_async(
        self,
        request: main_models.DescribeCreatedNatFirewallRequest,
    ) -> main_models.DescribeCreatedNatFirewallResponse:
        runtime = RuntimeOptions()
        return await self.describe_created_nat_firewall_with_options_async(request, runtime)

    def describe_ctrl_instance_member_accounts_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCtrlInstanceMemberAccountsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCtrlInstanceMemberAccounts',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCtrlInstanceMemberAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ctrl_instance_member_accounts_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCtrlInstanceMemberAccountsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCtrlInstanceMemberAccounts',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCtrlInstanceMemberAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ctrl_instance_member_accounts(self) -> main_models.DescribeCtrlInstanceMemberAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_ctrl_instance_member_accounts_with_options(runtime)

    async def describe_ctrl_instance_member_accounts_async(self) -> main_models.DescribeCtrlInstanceMemberAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ctrl_instance_member_accounts_with_options_async(runtime)

    def describe_default_ipsconfig_with_options(
        self,
        request: main_models.DescribeDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_default_ipsconfig_with_options_async(
        self,
        request: main_models.DescribeDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_default_ipsconfig(
        self,
        request: main_models.DescribeDefaultIPSConfigRequest,
    ) -> main_models.DescribeDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_default_ipsconfig_with_options(request, runtime)

    async def describe_default_ipsconfig_async(
        self,
        request: main_models.DescribeDefaultIPSConfigRequest,
    ) -> main_models.DescribeDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_default_ipsconfig_with_options_async(request, runtime)

    def describe_dns_firewall_policy_with_options(
        self,
        request: main_models.DescribeDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsFirewallPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dns_firewall_policy_with_options_async(
        self,
        request: main_models.DescribeDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDnsFirewallPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dns_firewall_policy(
        self,
        request: main_models.DescribeDnsFirewallPolicyRequest,
    ) -> main_models.DescribeDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_dns_firewall_policy_with_options(request, runtime)

    async def describe_dns_firewall_policy_async(
        self,
        request: main_models.DescribeDnsFirewallPolicyRequest,
    ) -> main_models.DescribeDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_dns_firewall_policy_with_options_async(request, runtime)

    def describe_domain_resolve_with_options(
        self,
        request: main_models.DescribeDomainResolveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResolveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainResolve',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResolveResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resolve_with_options_async(
        self,
        request: main_models.DescribeDomainResolveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDomainResolveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDomainResolve',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDomainResolveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_resolve(
        self,
        request: main_models.DescribeDomainResolveRequest,
    ) -> main_models.DescribeDomainResolveResponse:
        runtime = RuntimeOptions()
        return self.describe_domain_resolve_with_options(request, runtime)

    async def describe_domain_resolve_async(
        self,
        request: main_models.DescribeDomainResolveRequest,
    ) -> main_models.DescribeDomainResolveResponse:
        runtime = RuntimeOptions()
        return await self.describe_domain_resolve_with_options_async(request, runtime)

    def describe_download_task_with_options(
        self,
        request: main_models.DescribeDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_task_with_options_async(
        self,
        request: main_models.DescribeDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_task(
        self,
        request: main_models.DescribeDownloadTaskRequest,
    ) -> main_models.DescribeDownloadTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_download_task_with_options(request, runtime)

    async def describe_download_task_async(
        self,
        request: main_models.DescribeDownloadTaskRequest,
    ) -> main_models.DescribeDownloadTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_task_with_options_async(request, runtime)

    def describe_download_task_type_with_options(
        self,
        request: main_models.DescribeDownloadTaskTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadTaskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadTaskType',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadTaskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_task_type_with_options_async(
        self,
        request: main_models.DescribeDownloadTaskTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadTaskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadTaskType',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadTaskTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_task_type(
        self,
        request: main_models.DescribeDownloadTaskTypeRequest,
    ) -> main_models.DescribeDownloadTaskTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_download_task_type_with_options(request, runtime)

    async def describe_download_task_type_async(
        self,
        request: main_models.DescribeDownloadTaskTypeRequest,
    ) -> main_models.DescribeDownloadTaskTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_task_type_with_options_async(request, runtime)

    def describe_firewall_drop_statistics_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallDropStatisticsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeFirewallDropStatistics',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallDropStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_drop_statistics_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallDropStatisticsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeFirewallDropStatistics',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallDropStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_drop_statistics(self) -> main_models.DescribeFirewallDropStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_firewall_drop_statistics_with_options(runtime)

    async def describe_firewall_drop_statistics_async(self) -> main_models.DescribeFirewallDropStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_firewall_drop_statistics_with_options_async(runtime)

    def describe_firewall_task_with_options(
        self,
        request: main_models.DescribeFirewallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_task_with_options_async(
        self,
        request: main_models.DescribeFirewallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_instance_id):
            query['ChildInstanceId'] = request.child_instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallTask',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_task(
        self,
        request: main_models.DescribeFirewallTaskRequest,
    ) -> main_models.DescribeFirewallTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_firewall_task_with_options(request, runtime)

    async def describe_firewall_task_async(
        self,
        request: main_models.DescribeFirewallTaskRequest,
    ) -> main_models.DescribeFirewallTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_firewall_task_with_options_async(request, runtime)

    def describe_firewall_vswitch_with_options(
        self,
        request: main_models.DescribeFirewallVSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallVSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallVSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallVSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_vswitch_with_options_async(
        self,
        request: main_models.DescribeFirewallVSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallVSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallVSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallVSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_vswitch(
        self,
        request: main_models.DescribeFirewallVSwitchRequest,
    ) -> main_models.DescribeFirewallVSwitchResponse:
        runtime = RuntimeOptions()
        return self.describe_firewall_vswitch_with_options(request, runtime)

    async def describe_firewall_vswitch_async(
        self,
        request: main_models.DescribeFirewallVSwitchRequest,
    ) -> main_models.DescribeFirewallVSwitchResponse:
        runtime = RuntimeOptions()
        return await self.describe_firewall_vswitch_with_options_async(request, runtime)

    def describe_firewall_vswitch_resources_with_options(
        self,
        request: main_models.DescribeFirewallVswitchResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallVswitchResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallVswitchResources',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallVswitchResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_firewall_vswitch_resources_with_options_async(
        self,
        request: main_models.DescribeFirewallVswitchResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFirewallVswitchResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFirewallVswitchResources',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFirewallVswitchResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_firewall_vswitch_resources(
        self,
        request: main_models.DescribeFirewallVswitchResourcesRequest,
    ) -> main_models.DescribeFirewallVswitchResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_firewall_vswitch_resources_with_options(request, runtime)

    async def describe_firewall_vswitch_resources_async(
        self,
        request: main_models.DescribeFirewallVswitchResourcesRequest,
    ) -> main_models.DescribeFirewallVswitchResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_firewall_vswitch_resources_with_options_async(request, runtime)

    def describe_instance_members_with_options(
        self,
        request: main_models.DescribeInstanceMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.member_desc):
            query['MemberDesc'] = request.member_desc
        if not DaraCore.is_null(request.member_display_name):
            query['MemberDisplayName'] = request.member_display_name
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceMembers',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_members_with_options_async(
        self,
        request: main_models.DescribeInstanceMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.member_desc):
            query['MemberDesc'] = request.member_desc
        if not DaraCore.is_null(request.member_display_name):
            query['MemberDisplayName'] = request.member_display_name
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceMembers',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_members(
        self,
        request: main_models.DescribeInstanceMembersRequest,
    ) -> main_models.DescribeInstanceMembersResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_members_with_options(request, runtime)

    async def describe_instance_members_async(
        self,
        request: main_models.DescribeInstanceMembersRequest,
    ) -> main_models.DescribeInstanceMembersResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_members_with_options_async(request, runtime)

    def describe_instance_rd_accounts_with_options(
        self,
        request: main_models.DescribeInstanceRdAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRdAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_desc):
            query['MemberDesc'] = request.member_desc
        if not DaraCore.is_null(request.member_display_name):
            query['MemberDisplayName'] = request.member_display_name
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRdAccounts',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRdAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_rd_accounts_with_options_async(
        self,
        request: main_models.DescribeInstanceRdAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRdAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_desc):
            query['MemberDesc'] = request.member_desc
        if not DaraCore.is_null(request.member_display_name):
            query['MemberDisplayName'] = request.member_display_name
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRdAccounts',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRdAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_rd_accounts(
        self,
        request: main_models.DescribeInstanceRdAccountsRequest,
    ) -> main_models.DescribeInstanceRdAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_rd_accounts_with_options(request, runtime)

    async def describe_instance_rd_accounts_async(
        self,
        request: main_models.DescribeInstanceRdAccountsRequest,
    ) -> main_models.DescribeInstanceRdAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_rd_accounts_with_options_async(request, runtime)

    def describe_instance_risk_levels_with_options(
        self,
        request: main_models.DescribeInstanceRiskLevelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRiskLevelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRiskLevels',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRiskLevelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_risk_levels_with_options_async(
        self,
        request: main_models.DescribeInstanceRiskLevelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRiskLevelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRiskLevels',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRiskLevelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_risk_levels(
        self,
        request: main_models.DescribeInstanceRiskLevelsRequest,
    ) -> main_models.DescribeInstanceRiskLevelsResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_risk_levels_with_options(request, runtime)

    async def describe_instance_risk_levels_async(
        self,
        request: main_models.DescribeInstanceRiskLevelsRequest,
    ) -> main_models.DescribeInstanceRiskLevelsResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_risk_levels_with_options_async(request, runtime)

    def describe_internet_drop_traffic_trend_with_options(
        self,
        request: main_models.DescribeInternetDropTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetDropTrafficTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetDropTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetDropTrafficTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_drop_traffic_trend_with_options_async(
        self,
        request: main_models.DescribeInternetDropTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetDropTrafficTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetDropTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetDropTrafficTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_drop_traffic_trend(
        self,
        request: main_models.DescribeInternetDropTrafficTrendRequest,
    ) -> main_models.DescribeInternetDropTrafficTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_drop_traffic_trend_with_options(request, runtime)

    async def describe_internet_drop_traffic_trend_async(
        self,
        request: main_models.DescribeInternetDropTrafficTrendRequest,
    ) -> main_models.DescribeInternetDropTrafficTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_drop_traffic_trend_with_options_async(request, runtime)

    def describe_internet_open_detail_with_options(
        self,
        request: main_models.DescribeInternetOpenDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not DaraCore.is_null(request.assets_type):
            query['AssetsType'] = request.assets_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_name_fuzzy):
            query['ServiceNameFuzzy'] = request.service_name_fuzzy
        if not DaraCore.is_null(request.sort_list):
            query['SortList'] = request.sort_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.suggest_level):
            query['SuggestLevel'] = request.suggest_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_open_detail_with_options_async(
        self,
        request: main_models.DescribeInternetOpenDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not DaraCore.is_null(request.assets_type):
            query['AssetsType'] = request.assets_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_name_fuzzy):
            query['ServiceNameFuzzy'] = request.service_name_fuzzy
        if not DaraCore.is_null(request.sort_list):
            query['SortList'] = request.sort_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.suggest_level):
            query['SuggestLevel'] = request.suggest_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_open_detail(
        self,
        request: main_models.DescribeInternetOpenDetailRequest,
    ) -> main_models.DescribeInternetOpenDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_open_detail_with_options(request, runtime)

    async def describe_internet_open_detail_async(
        self,
        request: main_models.DescribeInternetOpenDetailRequest,
    ) -> main_models.DescribeInternetOpenDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_open_detail_with_options_async(request, runtime)

    def describe_internet_open_ip_with_options(
        self,
        request: main_models.DescribeInternetOpenIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not DaraCore.is_null(request.assets_type):
            query['AssetsType'] = request.assets_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenIp',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_open_ip_with_options_async(
        self,
        request: main_models.DescribeInternetOpenIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not DaraCore.is_null(request.assets_type):
            query['AssetsType'] = request.assets_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenIp',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_open_ip(
        self,
        request: main_models.DescribeInternetOpenIpRequest,
    ) -> main_models.DescribeInternetOpenIpResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_open_ip_with_options(request, runtime)

    async def describe_internet_open_ip_async(
        self,
        request: main_models.DescribeInternetOpenIpRequest,
    ) -> main_models.DescribeInternetOpenIpResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_open_ip_with_options_async(request, runtime)

    def describe_internet_open_port_with_options(
        self,
        request: main_models.DescribeInternetOpenPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_name_fuzzy):
            query['ServiceNameFuzzy'] = request.service_name_fuzzy
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.suggest_level):
            query['SuggestLevel'] = request.suggest_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenPort',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_open_port_with_options_async(
        self,
        request: main_models.DescribeInternetOpenPortRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenPortResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_name_fuzzy):
            query['ServiceNameFuzzy'] = request.service_name_fuzzy
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.suggest_level):
            query['SuggestLevel'] = request.suggest_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenPort',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_open_port(
        self,
        request: main_models.DescribeInternetOpenPortRequest,
    ) -> main_models.DescribeInternetOpenPortResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_open_port_with_options(request, runtime)

    async def describe_internet_open_port_async(
        self,
        request: main_models.DescribeInternetOpenPortRequest,
    ) -> main_models.DescribeInternetOpenPortResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_open_port_with_options_async(request, runtime)

    def describe_internet_open_service_with_options(
        self,
        request: main_models.DescribeInternetOpenServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_name_fuzzy):
            query['ServiceNameFuzzy'] = request.service_name_fuzzy
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.suggest_level):
            query['SuggestLevel'] = request.suggest_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenService',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_open_service_with_options_async(
        self,
        request: main_models.DescribeInternetOpenServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_name_fuzzy):
            query['ServiceNameFuzzy'] = request.service_name_fuzzy
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.suggest_level):
            query['SuggestLevel'] = request.suggest_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenService',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_open_service(
        self,
        request: main_models.DescribeInternetOpenServiceRequest,
    ) -> main_models.DescribeInternetOpenServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_open_service_with_options(request, runtime)

    async def describe_internet_open_service_async(
        self,
        request: main_models.DescribeInternetOpenServiceRequest,
    ) -> main_models.DescribeInternetOpenServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_open_service_with_options_async(request, runtime)

    def describe_internet_open_statistic_with_options(
        self,
        request: main_models.DescribeInternetOpenStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_open_statistic_with_options_async(
        self,
        request: main_models.DescribeInternetOpenStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetOpenStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetOpenStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetOpenStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_open_statistic(
        self,
        request: main_models.DescribeInternetOpenStatisticRequest,
    ) -> main_models.DescribeInternetOpenStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_open_statistic_with_options(request, runtime)

    async def describe_internet_open_statistic_async(
        self,
        request: main_models.DescribeInternetOpenStatisticRequest,
    ) -> main_models.DescribeInternetOpenStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_open_statistic_with_options_async(request, runtime)

    def describe_internet_service_name_list_with_options(
        self,
        request: main_models.DescribeInternetServiceNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetServiceNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetServiceNameList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetServiceNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_service_name_list_with_options_async(
        self,
        request: main_models.DescribeInternetServiceNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetServiceNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetServiceNameList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetServiceNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_service_name_list(
        self,
        request: main_models.DescribeInternetServiceNameListRequest,
    ) -> main_models.DescribeInternetServiceNameListResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_service_name_list_with_options(request, runtime)

    async def describe_internet_service_name_list_async(
        self,
        request: main_models.DescribeInternetServiceNameListRequest,
    ) -> main_models.DescribeInternetServiceNameListResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_service_name_list_with_options_async(request, runtime)

    def describe_internet_slb_with_options(
        self,
        request: main_models.DescribeInternetSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetSlb',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_slb_with_options_async(
        self,
        request: main_models.DescribeInternetSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetSlb',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_slb(
        self,
        request: main_models.DescribeInternetSlbRequest,
    ) -> main_models.DescribeInternetSlbResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_slb_with_options(request, runtime)

    async def describe_internet_slb_async(
        self,
        request: main_models.DescribeInternetSlbRequest,
    ) -> main_models.DescribeInternetSlbResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_slb_with_options_async(request, runtime)

    def describe_internet_time_top_with_options(
        self,
        request: main_models.DescribeInternetTimeTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetTimeTopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.nat_ip):
            query['NatIP'] = request.nat_ip
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.traffic_time):
            query['TrafficTime'] = request.traffic_time
        if not DaraCore.is_null(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetTimeTop',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetTimeTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_time_top_with_options_async(
        self,
        request: main_models.DescribeInternetTimeTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetTimeTopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.nat_ip):
            query['NatIP'] = request.nat_ip
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.traffic_time):
            query['TrafficTime'] = request.traffic_time
        if not DaraCore.is_null(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetTimeTop',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetTimeTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_time_top(
        self,
        request: main_models.DescribeInternetTimeTopRequest,
    ) -> main_models.DescribeInternetTimeTopResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_time_top_with_options(request, runtime)

    async def describe_internet_time_top_async(
        self,
        request: main_models.DescribeInternetTimeTopRequest,
    ) -> main_models.DescribeInternetTimeTopResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_time_top_with_options_async(request, runtime)

    def describe_internet_traffic_top_with_options(
        self,
        request: main_models.DescribeInternetTrafficTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetTrafficTopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not DaraCore.is_null(request.show_country_name):
            query['ShowCountryName'] = request.show_country_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetTrafficTop',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetTrafficTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_traffic_top_with_options_async(
        self,
        request: main_models.DescribeInternetTrafficTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetTrafficTopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not DaraCore.is_null(request.show_country_name):
            query['ShowCountryName'] = request.show_country_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetTrafficTop',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetTrafficTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_traffic_top(
        self,
        request: main_models.DescribeInternetTrafficTopRequest,
    ) -> main_models.DescribeInternetTrafficTopResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_traffic_top_with_options(request, runtime)

    async def describe_internet_traffic_top_async(
        self,
        request: main_models.DescribeInternetTrafficTopRequest,
    ) -> main_models.DescribeInternetTrafficTopResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_traffic_top_with_options_async(request, runtime)

    def describe_internet_traffic_trend_with_options(
        self,
        request: main_models.DescribeInternetTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetTrafficTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_private_ip):
            query['SrcPrivateIP'] = request.src_private_ip
        if not DaraCore.is_null(request.src_public_ip):
            query['SrcPublicIP'] = request.src_public_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetTrafficTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_internet_traffic_trend_with_options_async(
        self,
        request: main_models.DescribeInternetTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInternetTrafficTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_private_ip):
            query['SrcPrivateIP'] = request.src_private_ip
        if not DaraCore.is_null(request.src_public_ip):
            query['SrcPublicIP'] = request.src_public_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInternetTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInternetTrafficTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_internet_traffic_trend(
        self,
        request: main_models.DescribeInternetTrafficTrendRequest,
    ) -> main_models.DescribeInternetTrafficTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_internet_traffic_trend_with_options(request, runtime)

    async def describe_internet_traffic_trend_async(
        self,
        request: main_models.DescribeInternetTrafficTrendRequest,
    ) -> main_models.DescribeInternetTrafficTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_internet_traffic_trend_with_options_async(request, runtime)

    def describe_invade_ecs_trend_with_options(
        self,
        request: main_models.DescribeInvadeEcsTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEcsTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEcsTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEcsTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invade_ecs_trend_with_options_async(
        self,
        request: main_models.DescribeInvadeEcsTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEcsTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEcsTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEcsTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invade_ecs_trend(
        self,
        request: main_models.DescribeInvadeEcsTrendRequest,
    ) -> main_models.DescribeInvadeEcsTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_invade_ecs_trend_with_options(request, runtime)

    async def describe_invade_ecs_trend_async(
        self,
        request: main_models.DescribeInvadeEcsTrendRequest,
    ) -> main_models.DescribeInvadeEcsTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_invade_ecs_trend_with_options_async(request, runtime)

    def describe_invade_event_detail_with_options(
        self,
        request: main_models.DescribeInvadeEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invade_event_detail_with_options_async(
        self,
        request: main_models.DescribeInvadeEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invade_event_detail(
        self,
        request: main_models.DescribeInvadeEventDetailRequest,
    ) -> main_models.DescribeInvadeEventDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_invade_event_detail_with_options(request, runtime)

    async def describe_invade_event_detail_async(
        self,
        request: main_models.DescribeInvadeEventDetailRequest,
    ) -> main_models.DescribeInvadeEventDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_invade_event_detail_with_options_async(request, runtime)

    def describe_invade_event_list_with_options(
        self,
        request: main_models.DescribeInvadeEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_ip):
            query['AssetsIP'] = request.assets_ip
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_key):
            query['EventKey'] = request.event_key
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not DaraCore.is_null(request.is_ignore):
            query['IsIgnore'] = request.is_ignore
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_status_list):
            query['ProcessStatusList'] = request.process_status_list
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invade_event_list_with_options_async(
        self,
        request: main_models.DescribeInvadeEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_ip):
            query['AssetsIP'] = request.assets_ip
        if not DaraCore.is_null(request.assets_instance_id):
            query['AssetsInstanceId'] = request.assets_instance_id
        if not DaraCore.is_null(request.assets_instance_name):
            query['AssetsInstanceName'] = request.assets_instance_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_key):
            query['EventKey'] = request.event_key
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.event_uuid):
            query['EventUuid'] = request.event_uuid
        if not DaraCore.is_null(request.is_ignore):
            query['IsIgnore'] = request.is_ignore
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_status_list):
            query['ProcessStatusList'] = request.process_status_list
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invade_event_list(
        self,
        request: main_models.DescribeInvadeEventListRequest,
    ) -> main_models.DescribeInvadeEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_invade_event_list_with_options(request, runtime)

    async def describe_invade_event_list_async(
        self,
        request: main_models.DescribeInvadeEventListRequest,
    ) -> main_models.DescribeInvadeEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_invade_event_list_with_options_async(request, runtime)

    def describe_invade_event_name_list_with_options(
        self,
        request: main_models.DescribeInvadeEventNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventNameList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invade_event_name_list_with_options_async(
        self,
        request: main_models.DescribeInvadeEventNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventNameListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventNameList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invade_event_name_list(
        self,
        request: main_models.DescribeInvadeEventNameListRequest,
    ) -> main_models.DescribeInvadeEventNameListResponse:
        runtime = RuntimeOptions()
        return self.describe_invade_event_name_list_with_options(request, runtime)

    async def describe_invade_event_name_list_async(
        self,
        request: main_models.DescribeInvadeEventNameListRequest,
    ) -> main_models.DescribeInvadeEventNameListResponse:
        runtime = RuntimeOptions()
        return await self.describe_invade_event_name_list_with_options_async(request, runtime)

    def describe_invade_event_statistic_with_options(
        self,
        request: main_models.DescribeInvadeEventStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invade_event_statistic_with_options_async(
        self,
        request: main_models.DescribeInvadeEventStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvadeEventStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvadeEventStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvadeEventStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invade_event_statistic(
        self,
        request: main_models.DescribeInvadeEventStatisticRequest,
    ) -> main_models.DescribeInvadeEventStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_invade_event_statistic_with_options(request, runtime)

    async def describe_invade_event_statistic_async(
        self,
        request: main_models.DescribeInvadeEventStatisticRequest,
    ) -> main_models.DescribeInvadeEventStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_invade_event_statistic_with_options_async(request, runtime)

    def describe_ips_private_assoc_with_options(
        self,
        request: main_models.DescribeIpsPrivateAssocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpsPrivateAssocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpsPrivateAssoc',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpsPrivateAssocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ips_private_assoc_with_options_async(
        self,
        request: main_models.DescribeIpsPrivateAssocRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpsPrivateAssocResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.public_ip):
            query['PublicIp'] = request.public_ip
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpsPrivateAssoc',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpsPrivateAssocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ips_private_assoc(
        self,
        request: main_models.DescribeIpsPrivateAssocRequest,
    ) -> main_models.DescribeIpsPrivateAssocResponse:
        runtime = RuntimeOptions()
        return self.describe_ips_private_assoc_with_options(request, runtime)

    async def describe_ips_private_assoc_async(
        self,
        request: main_models.DescribeIpsPrivateAssocRequest,
    ) -> main_models.DescribeIpsPrivateAssocResponse:
        runtime = RuntimeOptions()
        return await self.describe_ips_private_assoc_with_options_async(request, runtime)

    def describe_isp_info_with_options(
        self,
        request: main_models.DescribeIspInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_isp_info_with_options_async(
        self,
        request: main_models.DescribeIspInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIspInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIspInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIspInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_isp_info(
        self,
        request: main_models.DescribeIspInfoRequest,
    ) -> main_models.DescribeIspInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_isp_info_with_options(request, runtime)

    async def describe_isp_info_async(
        self,
        request: main_models.DescribeIspInfoRequest,
    ) -> main_models.DescribeIspInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_isp_info_with_options_async(request, runtime)

    def describe_location_info_with_options(
        self,
        request: main_models.DescribeLocationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLocationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLocationInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLocationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_location_info_with_options_async(
        self,
        request: main_models.DescribeLocationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLocationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLocationInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLocationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_location_info(
        self,
        request: main_models.DescribeLocationInfoRequest,
    ) -> main_models.DescribeLocationInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_location_info_with_options(request, runtime)

    async def describe_location_info_async(
        self,
        request: main_models.DescribeLocationInfoRequest,
    ) -> main_models.DescribeLocationInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_location_info_with_options_async(request, runtime)

    def describe_log_store_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store_info(self) -> main_models.DescribeLogStoreInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_log_store_info_with_options(runtime)

    async def describe_log_store_info_async(self) -> main_models.DescribeLogStoreInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_store_info_with_options_async(runtime)

    def describe_member_info_with_options(
        self,
        request: main_models.DescribeMemberInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMemberInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMemberInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMemberInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_member_info_with_options_async(
        self,
        request: main_models.DescribeMemberInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMemberInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMemberInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMemberInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_member_info(
        self,
        request: main_models.DescribeMemberInfoRequest,
    ) -> main_models.DescribeMemberInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_member_info_with_options(request, runtime)

    async def describe_member_info_async(
        self,
        request: main_models.DescribeMemberInfoRequest,
    ) -> main_models.DescribeMemberInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_member_info_with_options_async(request, runtime)

    def describe_nat_acl_page_status_with_options(
        self,
        request: main_models.DescribeNatAclPageStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatAclPageStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatAclPageStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatAclPageStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_acl_page_status_with_options_async(
        self,
        request: main_models.DescribeNatAclPageStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatAclPageStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatAclPageStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatAclPageStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_acl_page_status(
        self,
        request: main_models.DescribeNatAclPageStatusRequest,
    ) -> main_models.DescribeNatAclPageStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_acl_page_status_with_options(request, runtime)

    async def describe_nat_acl_page_status_async(
        self,
        request: main_models.DescribeNatAclPageStatusRequest,
    ) -> main_models.DescribeNatAclPageStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_acl_page_status_with_options_async(request, runtime)

    def describe_nat_firewall_acl_group_list_with_options(
        self,
        request: main_models.DescribeNatFirewallAclGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallAclGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallAclGroupList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallAclGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_acl_group_list_with_options_async(
        self,
        request: main_models.DescribeNatFirewallAclGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallAclGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallAclGroupList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallAclGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_acl_group_list(
        self,
        request: main_models.DescribeNatFirewallAclGroupListRequest,
    ) -> main_models.DescribeNatFirewallAclGroupListResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_acl_group_list_with_options(request, runtime)

    async def describe_nat_firewall_acl_group_list_async(
        self,
        request: main_models.DescribeNatFirewallAclGroupListRequest,
    ) -> main_models.DescribeNatFirewallAclGroupListResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_acl_group_list_with_options_async(request, runtime)

    def describe_nat_firewall_control_policy_with_options(
        self,
        request: main_models.DescribeNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_control_policy_with_options_async(
        self,
        request: main_models.DescribeNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_control_policy(
        self,
        request: main_models.DescribeNatFirewallControlPolicyRequest,
    ) -> main_models.DescribeNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_control_policy_with_options(request, runtime)

    async def describe_nat_firewall_control_policy_async(
        self,
        request: main_models.DescribeNatFirewallControlPolicyRequest,
    ) -> main_models.DescribeNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_control_policy_with_options_async(request, runtime)

    def describe_nat_firewall_drop_traffic_trend_with_options(
        self,
        request: main_models.DescribeNatFirewallDropTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallDropTrafficTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallDropTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallDropTrafficTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_drop_traffic_trend_with_options_async(
        self,
        request: main_models.DescribeNatFirewallDropTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallDropTrafficTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallDropTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallDropTrafficTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_drop_traffic_trend(
        self,
        request: main_models.DescribeNatFirewallDropTrafficTrendRequest,
    ) -> main_models.DescribeNatFirewallDropTrafficTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_drop_traffic_trend_with_options(request, runtime)

    async def describe_nat_firewall_drop_traffic_trend_async(
        self,
        request: main_models.DescribeNatFirewallDropTrafficTrendRequest,
    ) -> main_models.DescribeNatFirewallDropTrafficTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_drop_traffic_trend_with_options_async(request, runtime)

    def describe_nat_firewall_list_with_options(
        self,
        request: main_models.DescribeNatFirewallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_list_with_options_async(
        self,
        request: main_models.DescribeNatFirewallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_list(
        self,
        request: main_models.DescribeNatFirewallListRequest,
    ) -> main_models.DescribeNatFirewallListResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_list_with_options(request, runtime)

    async def describe_nat_firewall_list_async(
        self,
        request: main_models.DescribeNatFirewallListRequest,
    ) -> main_models.DescribeNatFirewallListResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_list_with_options_async(request, runtime)

    def describe_nat_firewall_policy_prior_used_with_options(
        self,
        request: main_models.DescribeNatFirewallPolicyPriorUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallPolicyPriorUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallPolicyPriorUsed',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallPolicyPriorUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_policy_prior_used_with_options_async(
        self,
        request: main_models.DescribeNatFirewallPolicyPriorUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallPolicyPriorUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallPolicyPriorUsed',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallPolicyPriorUsedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_policy_prior_used(
        self,
        request: main_models.DescribeNatFirewallPolicyPriorUsedRequest,
    ) -> main_models.DescribeNatFirewallPolicyPriorUsedResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_policy_prior_used_with_options(request, runtime)

    async def describe_nat_firewall_policy_prior_used_async(
        self,
        request: main_models.DescribeNatFirewallPolicyPriorUsedRequest,
    ) -> main_models.DescribeNatFirewallPolicyPriorUsedResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_policy_prior_used_with_options_async(request, runtime)

    def describe_nat_firewall_precheck_detail_with_options(
        self,
        request: main_models.DescribeNatFirewallPrecheckDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallPrecheckDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallPrecheckDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallPrecheckDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_precheck_detail_with_options_async(
        self,
        request: main_models.DescribeNatFirewallPrecheckDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallPrecheckDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallPrecheckDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallPrecheckDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_precheck_detail(
        self,
        request: main_models.DescribeNatFirewallPrecheckDetailRequest,
    ) -> main_models.DescribeNatFirewallPrecheckDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_precheck_detail_with_options(request, runtime)

    async def describe_nat_firewall_precheck_detail_async(
        self,
        request: main_models.DescribeNatFirewallPrecheckDetailRequest,
    ) -> main_models.DescribeNatFirewallPrecheckDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_precheck_detail_with_options_async(request, runtime)

    def describe_nat_firewall_quota_with_options(
        self,
        request: main_models.DescribeNatFirewallQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallQuotaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallQuota',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_quota_with_options_async(
        self,
        request: main_models.DescribeNatFirewallQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallQuotaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallQuota',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_quota(
        self,
        request: main_models.DescribeNatFirewallQuotaRequest,
    ) -> main_models.DescribeNatFirewallQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_quota_with_options(request, runtime)

    async def describe_nat_firewall_quota_async(
        self,
        request: main_models.DescribeNatFirewallQuotaRequest,
    ) -> main_models.DescribeNatFirewallQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_quota_with_options_async(request, runtime)

    def describe_nat_firewall_time_top_with_options(
        self,
        request: main_models.DescribeNatFirewallTimeTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallTimeTopResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallTimeTop',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallTimeTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_time_top_with_options_async(
        self,
        request: main_models.DescribeNatFirewallTimeTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallTimeTopResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallTimeTop',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallTimeTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_time_top(
        self,
        request: main_models.DescribeNatFirewallTimeTopRequest,
    ) -> main_models.DescribeNatFirewallTimeTopResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_time_top_with_options(request, runtime)

    async def describe_nat_firewall_time_top_async(
        self,
        request: main_models.DescribeNatFirewallTimeTopRequest,
    ) -> main_models.DescribeNatFirewallTimeTopResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_time_top_with_options_async(request, runtime)

    def describe_nat_firewall_traffic_trend_with_options(
        self,
        request: main_models.DescribeNatFirewallTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallTrafficTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallTrafficTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_firewall_traffic_trend_with_options_async(
        self,
        request: main_models.DescribeNatFirewallTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNatFirewallTrafficTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNatFirewallTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNatFirewallTrafficTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_firewall_traffic_trend(
        self,
        request: main_models.DescribeNatFirewallTrafficTrendRequest,
    ) -> main_models.DescribeNatFirewallTrafficTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_nat_firewall_traffic_trend_with_options(request, runtime)

    async def describe_nat_firewall_traffic_trend_async(
        self,
        request: main_models.DescribeNatFirewallTrafficTrendRequest,
    ) -> main_models.DescribeNatFirewallTrafficTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_nat_firewall_traffic_trend_with_options_async(request, runtime)

    def describe_network_instance_list_with_options(
        self,
        request: main_models.DescribeNetworkInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkInstanceList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_instance_list_with_options_async(
        self,
        request: main_models.DescribeNetworkInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkInstanceList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_instance_list(
        self,
        request: main_models.DescribeNetworkInstanceListRequest,
    ) -> main_models.DescribeNetworkInstanceListResponse:
        runtime = RuntimeOptions()
        return self.describe_network_instance_list_with_options(request, runtime)

    async def describe_network_instance_list_async(
        self,
        request: main_models.DescribeNetworkInstanceListRequest,
    ) -> main_models.DescribeNetworkInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_instance_list_with_options_async(request, runtime)

    def describe_network_instance_relation_list_with_options(
        self,
        request: main_models.DescribeNetworkInstanceRelationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkInstanceRelationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.firewall_configure_status):
            query['FirewallConfigureStatus'] = request.firewall_configure_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.peer_network_instance_id):
            query['PeerNetworkInstanceId'] = request.peer_network_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkInstanceRelationList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkInstanceRelationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_instance_relation_list_with_options_async(
        self,
        request: main_models.DescribeNetworkInstanceRelationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkInstanceRelationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_type):
            query['ConnectType'] = request.connect_type
        if not DaraCore.is_null(request.firewall_configure_status):
            query['FirewallConfigureStatus'] = request.firewall_configure_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.peer_network_instance_id):
            query['PeerNetworkInstanceId'] = request.peer_network_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkInstanceRelationList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkInstanceRelationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_instance_relation_list(
        self,
        request: main_models.DescribeNetworkInstanceRelationListRequest,
    ) -> main_models.DescribeNetworkInstanceRelationListResponse:
        runtime = RuntimeOptions()
        return self.describe_network_instance_relation_list_with_options(request, runtime)

    async def describe_network_instance_relation_list_async(
        self,
        request: main_models.DescribeNetworkInstanceRelationListRequest,
    ) -> main_models.DescribeNetworkInstanceRelationListResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_instance_relation_list_with_options_async(request, runtime)

    def describe_network_traffic_top_ratio_with_options(
        self,
        request: main_models.DescribeNetworkTrafficTopRatioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkTrafficTopRatioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_ip):
            query['AssetIP'] = request.asset_ip
        if not DaraCore.is_null(request.asset_region):
            query['AssetRegion'] = request.asset_region
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_property):
            query['IpProperty'] = request.ip_property
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkTrafficTopRatio',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkTrafficTopRatioResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_traffic_top_ratio_with_options_async(
        self,
        request: main_models.DescribeNetworkTrafficTopRatioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetworkTrafficTopRatioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_ip):
            query['AssetIP'] = request.asset_ip
        if not DaraCore.is_null(request.asset_region):
            query['AssetRegion'] = request.asset_region
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ip_property):
            query['IpProperty'] = request.ip_property
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetworkTrafficTopRatio',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetworkTrafficTopRatioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_traffic_top_ratio(
        self,
        request: main_models.DescribeNetworkTrafficTopRatioRequest,
    ) -> main_models.DescribeNetworkTrafficTopRatioResponse:
        runtime = RuntimeOptions()
        return self.describe_network_traffic_top_ratio_with_options(request, runtime)

    async def describe_network_traffic_top_ratio_async(
        self,
        request: main_models.DescribeNetworkTrafficTopRatioRequest,
    ) -> main_models.DescribeNetworkTrafficTopRatioResponse:
        runtime = RuntimeOptions()
        return await self.describe_network_traffic_top_ratio_with_options_async(request, runtime)

    def describe_open_ip_access_src_stat_with_options(
        self,
        request: main_models.DescribeOpenIpAccessSrcStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenIpAccessSrcStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenIpAccessSrcStat',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenIpAccessSrcStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_open_ip_access_src_stat_with_options_async(
        self,
        request: main_models.DescribeOpenIpAccessSrcStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenIpAccessSrcStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenIpAccessSrcStat',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenIpAccessSrcStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_open_ip_access_src_stat(
        self,
        request: main_models.DescribeOpenIpAccessSrcStatRequest,
    ) -> main_models.DescribeOpenIpAccessSrcStatResponse:
        runtime = RuntimeOptions()
        return self.describe_open_ip_access_src_stat_with_options(request, runtime)

    async def describe_open_ip_access_src_stat_async(
        self,
        request: main_models.DescribeOpenIpAccessSrcStatRequest,
    ) -> main_models.DescribeOpenIpAccessSrcStatResponse:
        runtime = RuntimeOptions()
        return await self.describe_open_ip_access_src_stat_with_options_async(request, runtime)

    def describe_outgoing_asset_list_with_options(
        self,
        request: main_models.DescribeOutgoingAssetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingAssetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_region):
            query['AssetsRegion'] = request.assets_region
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.nat_gateway_name):
            query['NatGatewayName'] = request.nat_gateway_name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_risk):
            query['SecurityRisk'] = request.security_risk
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingAssetList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingAssetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_asset_list_with_options_async(
        self,
        request: main_models.DescribeOutgoingAssetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingAssetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.assets_region):
            query['AssetsRegion'] = request.assets_region
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.nat_gateway_name):
            query['NatGatewayName'] = request.nat_gateway_name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.security_risk):
            query['SecurityRisk'] = request.security_risk
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingAssetList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingAssetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_asset_list(
        self,
        request: main_models.DescribeOutgoingAssetListRequest,
    ) -> main_models.DescribeOutgoingAssetListResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_asset_list_with_options(request, runtime)

    async def describe_outgoing_asset_list_async(
        self,
        request: main_models.DescribeOutgoingAssetListRequest,
    ) -> main_models.DescribeOutgoingAssetListResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_asset_list_with_options_async(request, runtime)

    def describe_outgoing_destination_with_options(
        self,
        request: main_models.DescribeOutgoingDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_coverage):
            query['AclCoverage'] = request.acl_coverage
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.security_suggest):
            query['SecuritySuggest'] = request.security_suggest
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestination',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_destination_with_options_async(
        self,
        request: main_models.DescribeOutgoingDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_coverage):
            query['AclCoverage'] = request.acl_coverage
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.security_suggest):
            query['SecuritySuggest'] = request.security_suggest
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestination',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_destination(
        self,
        request: main_models.DescribeOutgoingDestinationRequest,
    ) -> main_models.DescribeOutgoingDestinationResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_destination_with_options(request, runtime)

    async def describe_outgoing_destination_async(
        self,
        request: main_models.DescribeOutgoingDestinationRequest,
    ) -> main_models.DescribeOutgoingDestinationResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_destination_with_options_async(request, runtime)

    def describe_outgoing_destination_category_with_options(
        self,
        request: main_models.DescribeOutgoingDestinationCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestinationCategory',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_destination_category_with_options_async(
        self,
        request: main_models.DescribeOutgoingDestinationCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestinationCategory',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_destination_category(
        self,
        request: main_models.DescribeOutgoingDestinationCategoryRequest,
    ) -> main_models.DescribeOutgoingDestinationCategoryResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_destination_category_with_options(request, runtime)

    async def describe_outgoing_destination_category_async(
        self,
        request: main_models.DescribeOutgoingDestinationCategoryRequest,
    ) -> main_models.DescribeOutgoingDestinationCategoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_destination_category_with_options_async(request, runtime)

    def describe_outgoing_destination_ipwith_options(
        self,
        request: main_models.DescribeOutgoingDestinationIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestinationIP',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_destination_ipwith_options_async(
        self,
        request: main_models.DescribeOutgoingDestinationIPRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationIPResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestinationIP',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_destination_ip(
        self,
        request: main_models.DescribeOutgoingDestinationIPRequest,
    ) -> main_models.DescribeOutgoingDestinationIPResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_destination_ipwith_options(request, runtime)

    async def describe_outgoing_destination_ip_async(
        self,
        request: main_models.DescribeOutgoingDestinationIPRequest,
    ) -> main_models.DescribeOutgoingDestinationIPResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_destination_ipwith_options_async(request, runtime)

    def describe_outgoing_destination_ipdetail_with_options(
        self,
        request: main_models.DescribeOutgoingDestinationIPDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationIPDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_coverage):
            query['AclCoverage'] = request.acl_coverage
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestinationIPDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationIPDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_destination_ipdetail_with_options_async(
        self,
        request: main_models.DescribeOutgoingDestinationIPDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDestinationIPDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_coverage):
            query['AclCoverage'] = request.acl_coverage
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDestinationIPDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDestinationIPDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_destination_ipdetail(
        self,
        request: main_models.DescribeOutgoingDestinationIPDetailRequest,
    ) -> main_models.DescribeOutgoingDestinationIPDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_destination_ipdetail_with_options(request, runtime)

    async def describe_outgoing_destination_ipdetail_async(
        self,
        request: main_models.DescribeOutgoingDestinationIPDetailRequest,
    ) -> main_models.DescribeOutgoingDestinationIPDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_destination_ipdetail_with_options_async(request, runtime)

    def describe_outgoing_domain_with_options(
        self,
        request: main_models.DescribeOutgoingDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDomain',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_domain_with_options_async(
        self,
        request: main_models.DescribeOutgoingDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id_new):
            query['TagIdNew'] = request.tag_id_new
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDomain',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_domain(
        self,
        request: main_models.DescribeOutgoingDomainRequest,
    ) -> main_models.DescribeOutgoingDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_domain_with_options(request, runtime)

    async def describe_outgoing_domain_async(
        self,
        request: main_models.DescribeOutgoingDomainRequest,
    ) -> main_models.DescribeOutgoingDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_domain_with_options_async(request, runtime)

    def describe_outgoing_domain_detail_with_options(
        self,
        request: main_models.DescribeOutgoingDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_coverage):
            query['AclCoverage'] = request.acl_coverage
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDomainDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_domain_detail_with_options_async(
        self,
        request: main_models.DescribeOutgoingDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_coverage):
            query['AclCoverage'] = request.acl_coverage
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.iptype):
            query['IPType'] = request.iptype
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_ip):
            query['PrivateIP'] = request.private_ip
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingDomainDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_domain_detail(
        self,
        request: main_models.DescribeOutgoingDomainDetailRequest,
    ) -> main_models.DescribeOutgoingDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_domain_detail_with_options(request, runtime)

    async def describe_outgoing_domain_detail_async(
        self,
        request: main_models.DescribeOutgoingDomainDetailRequest,
    ) -> main_models.DescribeOutgoingDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_domain_detail_with_options_async(request, runtime)

    def describe_outgoing_risk_domain_and_ip_count_with_options(
        self,
        request: main_models.DescribeOutgoingRiskDomainAndIpCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingRiskDomainAndIpCountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingRiskDomainAndIpCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingRiskDomainAndIpCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_risk_domain_and_ip_count_with_options_async(
        self,
        request: main_models.DescribeOutgoingRiskDomainAndIpCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingRiskDomainAndIpCountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingRiskDomainAndIpCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingRiskDomainAndIpCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_risk_domain_and_ip_count(
        self,
        request: main_models.DescribeOutgoingRiskDomainAndIpCountRequest,
    ) -> main_models.DescribeOutgoingRiskDomainAndIpCountResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_risk_domain_and_ip_count_with_options(request, runtime)

    async def describe_outgoing_risk_domain_and_ip_count_async(
        self,
        request: main_models.DescribeOutgoingRiskDomainAndIpCountRequest,
    ) -> main_models.DescribeOutgoingRiskDomainAndIpCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_risk_domain_and_ip_count_with_options_async(request, runtime)

    def describe_outgoing_risk_trend_with_options(
        self,
        request: main_models.DescribeOutgoingRiskTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingRiskTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingRiskTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingRiskTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_risk_trend_with_options_async(
        self,
        request: main_models.DescribeOutgoingRiskTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingRiskTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingRiskTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingRiskTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_risk_trend(
        self,
        request: main_models.DescribeOutgoingRiskTrendRequest,
    ) -> main_models.DescribeOutgoingRiskTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_risk_trend_with_options(request, runtime)

    async def describe_outgoing_risk_trend_async(
        self,
        request: main_models.DescribeOutgoingRiskTrendRequest,
    ) -> main_models.DescribeOutgoingRiskTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_risk_trend_with_options_async(request, runtime)

    def describe_outgoing_statistic_with_options(
        self,
        request: main_models.DescribeOutgoingStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_statistic_with_options_async(
        self,
        request: main_models.DescribeOutgoingStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_statistic(
        self,
        request: main_models.DescribeOutgoingStatisticRequest,
    ) -> main_models.DescribeOutgoingStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_statistic_with_options(request, runtime)

    async def describe_outgoing_statistic_async(
        self,
        request: main_models.DescribeOutgoingStatisticRequest,
    ) -> main_models.DescribeOutgoingStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_statistic_with_options_async(request, runtime)

    def describe_outgoing_tag_with_options(
        self,
        request: main_models.DescribeOutgoingTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingTag',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_outgoing_tag_with_options_async(
        self,
        request: main_models.DescribeOutgoingTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOutgoingTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOutgoingTag',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOutgoingTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_outgoing_tag(
        self,
        request: main_models.DescribeOutgoingTagRequest,
    ) -> main_models.DescribeOutgoingTagResponse:
        runtime = RuntimeOptions()
        return self.describe_outgoing_tag_with_options(request, runtime)

    async def describe_outgoing_tag_async(
        self,
        request: main_models.DescribeOutgoingTagRequest,
    ) -> main_models.DescribeOutgoingTagResponse:
        runtime = RuntimeOptions()
        return await self.describe_outgoing_tag_with_options_async(request, runtime)

    def describe_page_documents_with_options(
        self,
        request: main_models.DescribePageDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePageDocumentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_name):
            query['PageName'] = request.page_name
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tab_name):
            query['TabName'] = request.tab_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePageDocuments',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePageDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_page_documents_with_options_async(
        self,
        request: main_models.DescribePageDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePageDocumentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_name):
            query['PageName'] = request.page_name
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tab_name):
            query['TabName'] = request.tab_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePageDocuments',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePageDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_page_documents(
        self,
        request: main_models.DescribePageDocumentsRequest,
    ) -> main_models.DescribePageDocumentsResponse:
        runtime = RuntimeOptions()
        return self.describe_page_documents_with_options(request, runtime)

    async def describe_page_documents_async(
        self,
        request: main_models.DescribePageDocumentsRequest,
    ) -> main_models.DescribePageDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.describe_page_documents_with_options_async(request, runtime)

    def describe_policy_advanced_config_with_options(
        self,
        request: main_models.DescribePolicyAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyAdvancedConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyAdvancedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_advanced_config_with_options_async(
        self,
        request: main_models.DescribePolicyAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyAdvancedConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyAdvancedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_advanced_config(
        self,
        request: main_models.DescribePolicyAdvancedConfigRequest,
    ) -> main_models.DescribePolicyAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_policy_advanced_config_with_options(request, runtime)

    async def describe_policy_advanced_config_async(
        self,
        request: main_models.DescribePolicyAdvancedConfigRequest,
    ) -> main_models.DescribePolicyAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_policy_advanced_config_with_options_async(request, runtime)

    def describe_policy_prior_used_with_options(
        self,
        request: main_models.DescribePolicyPriorUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyPriorUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyPriorUsed',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyPriorUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_prior_used_with_options_async(
        self,
        request: main_models.DescribePolicyPriorUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyPriorUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyPriorUsed',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyPriorUsedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_prior_used(
        self,
        request: main_models.DescribePolicyPriorUsedRequest,
    ) -> main_models.DescribePolicyPriorUsedResponse:
        runtime = RuntimeOptions()
        return self.describe_policy_prior_used_with_options(request, runtime)

    async def describe_policy_prior_used_async(
        self,
        request: main_models.DescribePolicyPriorUsedRequest,
    ) -> main_models.DescribePolicyPriorUsedResponse:
        runtime = RuntimeOptions()
        return await self.describe_policy_prior_used_with_options_async(request, runtime)

    def describe_postpay_enabled_protection_with_options(
        self,
        request: main_models.DescribePostpayEnabledProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayEnabledProtectionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayEnabledProtection',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayEnabledProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_enabled_protection_with_options_async(
        self,
        request: main_models.DescribePostpayEnabledProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayEnabledProtectionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayEnabledProtection',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayEnabledProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_enabled_protection(
        self,
        request: main_models.DescribePostpayEnabledProtectionRequest,
    ) -> main_models.DescribePostpayEnabledProtectionResponse:
        runtime = RuntimeOptions()
        return self.describe_postpay_enabled_protection_with_options(request, runtime)

    async def describe_postpay_enabled_protection_async(
        self,
        request: main_models.DescribePostpayEnabledProtectionRequest,
    ) -> main_models.DescribePostpayEnabledProtectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_postpay_enabled_protection_with_options_async(request, runtime)

    def describe_postpay_traffic_detail_with_options(
        self,
        request: main_models.DescribePostpayTrafficDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayTrafficDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.search_item):
            query['SearchItem'] = request.search_item
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayTrafficDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayTrafficDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_traffic_detail_with_options_async(
        self,
        request: main_models.DescribePostpayTrafficDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayTrafficDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.search_item):
            query['SearchItem'] = request.search_item
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.traffic_type):
            query['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayTrafficDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayTrafficDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_traffic_detail(
        self,
        request: main_models.DescribePostpayTrafficDetailRequest,
    ) -> main_models.DescribePostpayTrafficDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_postpay_traffic_detail_with_options(request, runtime)

    async def describe_postpay_traffic_detail_async(
        self,
        request: main_models.DescribePostpayTrafficDetailRequest,
    ) -> main_models.DescribePostpayTrafficDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_postpay_traffic_detail_with_options_async(request, runtime)

    def describe_postpay_traffic_total_with_options(
        self,
        request: main_models.DescribePostpayTrafficTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayTrafficTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayTrafficTotal',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayTrafficTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_traffic_total_with_options_async(
        self,
        request: main_models.DescribePostpayTrafficTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayTrafficTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayTrafficTotal',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayTrafficTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_traffic_total(
        self,
        request: main_models.DescribePostpayTrafficTotalRequest,
    ) -> main_models.DescribePostpayTrafficTotalResponse:
        runtime = RuntimeOptions()
        return self.describe_postpay_traffic_total_with_options(request, runtime)

    async def describe_postpay_traffic_total_async(
        self,
        request: main_models.DescribePostpayTrafficTotalRequest,
    ) -> main_models.DescribePostpayTrafficTotalResponse:
        runtime = RuntimeOptions()
        return await self.describe_postpay_traffic_total_with_options_async(request, runtime)

    def describe_postpay_user_internet_status_with_options(
        self,
        request: main_models.DescribePostpayUserInternetStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayUserInternetStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayUserInternetStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayUserInternetStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_user_internet_status_with_options_async(
        self,
        request: main_models.DescribePostpayUserInternetStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayUserInternetStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayUserInternetStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayUserInternetStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_user_internet_status(
        self,
        request: main_models.DescribePostpayUserInternetStatusRequest,
    ) -> main_models.DescribePostpayUserInternetStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_postpay_user_internet_status_with_options(request, runtime)

    async def describe_postpay_user_internet_status_async(
        self,
        request: main_models.DescribePostpayUserInternetStatusRequest,
    ) -> main_models.DescribePostpayUserInternetStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_postpay_user_internet_status_with_options_async(request, runtime)

    def describe_postpay_user_nat_status_with_options(
        self,
        request: main_models.DescribePostpayUserNatStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayUserNatStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayUserNatStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayUserNatStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_user_nat_status_with_options_async(
        self,
        request: main_models.DescribePostpayUserNatStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayUserNatStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayUserNatStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayUserNatStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_user_nat_status(
        self,
        request: main_models.DescribePostpayUserNatStatusRequest,
    ) -> main_models.DescribePostpayUserNatStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_postpay_user_nat_status_with_options(request, runtime)

    async def describe_postpay_user_nat_status_async(
        self,
        request: main_models.DescribePostpayUserNatStatusRequest,
    ) -> main_models.DescribePostpayUserNatStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_postpay_user_nat_status_with_options_async(request, runtime)

    def describe_postpay_user_vpc_status_with_options(
        self,
        request: main_models.DescribePostpayUserVpcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayUserVpcStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayUserVpcStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayUserVpcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_postpay_user_vpc_status_with_options_async(
        self,
        request: main_models.DescribePostpayUserVpcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePostpayUserVpcStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePostpayUserVpcStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePostpayUserVpcStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_postpay_user_vpc_status(
        self,
        request: main_models.DescribePostpayUserVpcStatusRequest,
    ) -> main_models.DescribePostpayUserVpcStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_postpay_user_vpc_status_with_options(request, runtime)

    async def describe_postpay_user_vpc_status_async(
        self,
        request: main_models.DescribePostpayUserVpcStatusRequest,
    ) -> main_models.DescribePostpayUserVpcStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_postpay_user_vpc_status_with_options_async(request, runtime)

    def describe_prefix_lists_with_options(
        self,
        request: main_models.DescribePrefixListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrefixListsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrefixLists',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrefixListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prefix_lists_with_options_async(
        self,
        request: main_models.DescribePrefixListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrefixListsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrefixLists',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrefixListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prefix_lists(
        self,
        request: main_models.DescribePrefixListsRequest,
    ) -> main_models.DescribePrefixListsResponse:
        runtime = RuntimeOptions()
        return self.describe_prefix_lists_with_options(request, runtime)

    async def describe_prefix_lists_async(
        self,
        request: main_models.DescribePrefixListsRequest,
    ) -> main_models.DescribePrefixListsResponse:
        runtime = RuntimeOptions()
        return await self.describe_prefix_lists_with_options_async(request, runtime)

    def describe_private_dns_domain_name_list_with_options(
        self,
        request: main_models.DescribePrivateDnsDomainNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsDomainNameListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsDomainNameList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsDomainNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_private_dns_domain_name_list_with_options_async(
        self,
        request: main_models.DescribePrivateDnsDomainNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsDomainNameListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsDomainNameList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsDomainNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_private_dns_domain_name_list(
        self,
        request: main_models.DescribePrivateDnsDomainNameListRequest,
    ) -> main_models.DescribePrivateDnsDomainNameListResponse:
        runtime = RuntimeOptions()
        return self.describe_private_dns_domain_name_list_with_options(request, runtime)

    async def describe_private_dns_domain_name_list_async(
        self,
        request: main_models.DescribePrivateDnsDomainNameListRequest,
    ) -> main_models.DescribePrivateDnsDomainNameListResponse:
        runtime = RuntimeOptions()
        return await self.describe_private_dns_domain_name_list_with_options_async(request, runtime)

    def describe_private_dns_endpoint_detail_with_options(
        self,
        request: main_models.DescribePrivateDnsEndpointDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsEndpointDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsEndpointDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsEndpointDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_private_dns_endpoint_detail_with_options_async(
        self,
        request: main_models.DescribePrivateDnsEndpointDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsEndpointDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsEndpointDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsEndpointDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_private_dns_endpoint_detail(
        self,
        request: main_models.DescribePrivateDnsEndpointDetailRequest,
    ) -> main_models.DescribePrivateDnsEndpointDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_private_dns_endpoint_detail_with_options(request, runtime)

    async def describe_private_dns_endpoint_detail_async(
        self,
        request: main_models.DescribePrivateDnsEndpointDetailRequest,
    ) -> main_models.DescribePrivateDnsEndpointDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_private_dns_endpoint_detail_with_options_async(request, runtime)

    def describe_private_dns_endpoint_list_with_options(
        self,
        request: main_models.DescribePrivateDnsEndpointListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsEndpointListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsEndpointList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsEndpointListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_private_dns_endpoint_list_with_options_async(
        self,
        request: main_models.DescribePrivateDnsEndpointListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsEndpointListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsEndpointList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsEndpointListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_private_dns_endpoint_list(
        self,
        request: main_models.DescribePrivateDnsEndpointListRequest,
    ) -> main_models.DescribePrivateDnsEndpointListResponse:
        runtime = RuntimeOptions()
        return self.describe_private_dns_endpoint_list_with_options(request, runtime)

    async def describe_private_dns_endpoint_list_async(
        self,
        request: main_models.DescribePrivateDnsEndpointListRequest,
    ) -> main_models.DescribePrivateDnsEndpointListResponse:
        runtime = RuntimeOptions()
        return await self.describe_private_dns_endpoint_list_with_options_async(request, runtime)

    def describe_private_dns_statistics_with_options(
        self,
        request: main_models.DescribePrivateDnsStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name_created_end_time):
            query['DomainNameCreatedEndTime'] = request.domain_name_created_end_time
        if not DaraCore.is_null(request.domain_name_created_start_time):
            query['DomainNameCreatedStartTime'] = request.domain_name_created_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsStatistics',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_private_dns_statistics_with_options_async(
        self,
        request: main_models.DescribePrivateDnsStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrivateDnsStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name_created_end_time):
            query['DomainNameCreatedEndTime'] = request.domain_name_created_end_time
        if not DaraCore.is_null(request.domain_name_created_start_time):
            query['DomainNameCreatedStartTime'] = request.domain_name_created_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrivateDnsStatistics',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrivateDnsStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_private_dns_statistics(
        self,
        request: main_models.DescribePrivateDnsStatisticsRequest,
    ) -> main_models.DescribePrivateDnsStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_private_dns_statistics_with_options(request, runtime)

    async def describe_private_dns_statistics_async(
        self,
        request: main_models.DescribePrivateDnsStatisticsRequest,
    ) -> main_models.DescribePrivateDnsStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_private_dns_statistics_with_options_async(request, runtime)

    def describe_region_info_with_options(
        self,
        request: main_models.DescribeRegionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegionInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_region_info_with_options_async(
        self,
        request: main_models.DescribeRegionInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegionInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_region_info(
        self,
        request: main_models.DescribeRegionInfoRequest,
    ) -> main_models.DescribeRegionInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_region_info_with_options(request, runtime)

    async def describe_region_info_async(
        self,
        request: main_models.DescribeRegionInfoRequest,
    ) -> main_models.DescribeRegionInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_region_info_with_options_async(request, runtime)

    def describe_resource_type_auto_enable_with_options(
        self,
        request: main_models.DescribeResourceTypeAutoEnableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceTypeAutoEnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceTypeAutoEnable',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceTypeAutoEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_type_auto_enable_with_options_async(
        self,
        request: main_models.DescribeResourceTypeAutoEnableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceTypeAutoEnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceTypeAutoEnable',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceTypeAutoEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_type_auto_enable(
        self,
        request: main_models.DescribeResourceTypeAutoEnableRequest,
    ) -> main_models.DescribeResourceTypeAutoEnableResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_type_auto_enable_with_options(request, runtime)

    async def describe_resource_type_auto_enable_async(
        self,
        request: main_models.DescribeResourceTypeAutoEnableRequest,
    ) -> main_models.DescribeResourceTypeAutoEnableResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_type_auto_enable_with_options_async(request, runtime)

    def describe_risk_event_group_with_options(
        self,
        request: main_models.DescribeRiskEventGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_app_category):
            query['AttackAppCategory'] = request.attack_app_category
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_network_instance_id):
            query['DstNetworkInstanceId'] = request.dst_network_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.is_only_private_assoc):
            query['IsOnlyPrivateAssoc'] = request.is_only_private_assoc
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.no_location):
            query['NoLocation'] = request.no_location
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_network_instance_id):
            query['SrcNetworkInstanceId'] = request.src_network_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vul_level):
            query['VulLevel'] = request.vul_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventGroup',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_group_with_options_async(
        self,
        request: main_models.DescribeRiskEventGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_app_category):
            query['AttackAppCategory'] = request.attack_app_category
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_network_instance_id):
            query['DstNetworkInstanceId'] = request.dst_network_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.is_only_private_assoc):
            query['IsOnlyPrivateAssoc'] = request.is_only_private_assoc
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.no_location):
            query['NoLocation'] = request.no_location
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_network_instance_id):
            query['SrcNetworkInstanceId'] = request.src_network_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vul_level):
            query['VulLevel'] = request.vul_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventGroup',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_group(
        self,
        request: main_models.DescribeRiskEventGroupRequest,
    ) -> main_models.DescribeRiskEventGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_event_group_with_options(request, runtime)

    async def describe_risk_event_group_async(
        self,
        request: main_models.DescribeRiskEventGroupRequest,
    ) -> main_models.DescribeRiskEventGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_event_group_with_options_async(request, runtime)

    def describe_risk_event_payload_with_options(
        self,
        request: main_models.DescribeRiskEventPayloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventPayloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventPayload',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventPayloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_payload_with_options_async(
        self,
        request: main_models.DescribeRiskEventPayloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventPayloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.public_ip):
            query['PublicIP'] = request.public_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventPayload',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventPayloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_payload(
        self,
        request: main_models.DescribeRiskEventPayloadRequest,
    ) -> main_models.DescribeRiskEventPayloadResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_event_payload_with_options(request, runtime)

    async def describe_risk_event_payload_async(
        self,
        request: main_models.DescribeRiskEventPayloadRequest,
    ) -> main_models.DescribeRiskEventPayloadResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_event_payload_with_options_async(request, runtime)

    def describe_risk_event_statistic_with_options(
        self,
        request: main_models.DescribeRiskEventStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_statistic_with_options_async(
        self,
        request: main_models.DescribeRiskEventStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_statistic(
        self,
        request: main_models.DescribeRiskEventStatisticRequest,
    ) -> main_models.DescribeRiskEventStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_event_statistic_with_options(request, runtime)

    async def describe_risk_event_statistic_async(
        self,
        request: main_models.DescribeRiskEventStatisticRequest,
    ) -> main_models.DescribeRiskEventStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_event_statistic_with_options_async(request, runtime)

    def describe_risk_event_top_attack_app_with_options(
        self,
        request: main_models.DescribeRiskEventTopAttackAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventTopAttackAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventTopAttackApp',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventTopAttackAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_top_attack_app_with_options_async(
        self,
        request: main_models.DescribeRiskEventTopAttackAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventTopAttackAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventTopAttackApp',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventTopAttackAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_top_attack_app(
        self,
        request: main_models.DescribeRiskEventTopAttackAppRequest,
    ) -> main_models.DescribeRiskEventTopAttackAppResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_event_top_attack_app_with_options(request, runtime)

    async def describe_risk_event_top_attack_app_async(
        self,
        request: main_models.DescribeRiskEventTopAttackAppRequest,
    ) -> main_models.DescribeRiskEventTopAttackAppResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_event_top_attack_app_with_options_async(request, runtime)

    def describe_risk_event_top_attack_asset_with_options(
        self,
        request: main_models.DescribeRiskEventTopAttackAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventTopAttackAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventTopAttackAsset',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventTopAttackAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_top_attack_asset_with_options_async(
        self,
        request: main_models.DescribeRiskEventTopAttackAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventTopAttackAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventTopAttackAsset',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventTopAttackAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_top_attack_asset(
        self,
        request: main_models.DescribeRiskEventTopAttackAssetRequest,
    ) -> main_models.DescribeRiskEventTopAttackAssetResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_event_top_attack_asset_with_options(request, runtime)

    async def describe_risk_event_top_attack_asset_async(
        self,
        request: main_models.DescribeRiskEventTopAttackAssetRequest,
    ) -> main_models.DescribeRiskEventTopAttackAssetResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_event_top_attack_asset_with_options_async(request, runtime)

    def describe_risk_event_top_attack_type_with_options(
        self,
        request: main_models.DescribeRiskEventTopAttackTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventTopAttackTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventTopAttackType',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventTopAttackTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_event_top_attack_type_with_options_async(
        self,
        request: main_models.DescribeRiskEventTopAttackTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskEventTopAttackTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskEventTopAttackType',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskEventTopAttackTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_event_top_attack_type(
        self,
        request: main_models.DescribeRiskEventTopAttackTypeRequest,
    ) -> main_models.DescribeRiskEventTopAttackTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_event_top_attack_type_with_options(request, runtime)

    async def describe_risk_event_top_attack_type_async(
        self,
        request: main_models.DescribeRiskEventTopAttackTypeRequest,
    ) -> main_models.DescribeRiskEventTopAttackTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_event_top_attack_type_with_options_async(request, runtime)

    def describe_risk_security_group_detail_with_options(
        self,
        request: main_models.DescribeRiskSecurityGroupDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskSecurityGroupDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_uuid):
            query['RuleUuid'] = request.rule_uuid
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskSecurityGroupDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskSecurityGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_security_group_detail_with_options_async(
        self,
        request: main_models.DescribeRiskSecurityGroupDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskSecurityGroupDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_uuid):
            query['RuleUuid'] = request.rule_uuid
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskSecurityGroupDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskSecurityGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_security_group_detail(
        self,
        request: main_models.DescribeRiskSecurityGroupDetailRequest,
    ) -> main_models.DescribeRiskSecurityGroupDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_security_group_detail_with_options(request, runtime)

    async def describe_risk_security_group_detail_async(
        self,
        request: main_models.DescribeRiskSecurityGroupDetailRequest,
    ) -> main_models.DescribeRiskSecurityGroupDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_security_group_detail_with_options_async(request, runtime)

    def describe_sdl_event_detail_with_options(
        self,
        request: main_models.DescribeSdlEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdl_event_detail_with_options_async(
        self,
        request: main_models.DescribeSdlEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdl_event_detail(
        self,
        request: main_models.DescribeSdlEventDetailRequest,
    ) -> main_models.DescribeSdlEventDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_sdl_event_detail_with_options(request, runtime)

    async def describe_sdl_event_detail_async(
        self,
        request: main_models.DescribeSdlEventDetailRequest,
    ) -> main_models.DescribeSdlEventDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_sdl_event_detail_with_options_async(request, runtime)

    def describe_sdl_event_list_with_options(
        self,
        request: main_models.DescribeSdlEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.only_ai_evt):
            query['OnlyAiEvt'] = request.only_ai_evt
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdl_event_list_with_options_async(
        self,
        request: main_models.DescribeSdlEventListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.only_ai_evt):
            query['OnlyAiEvt'] = request.only_ai_evt
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdl_event_list(
        self,
        request: main_models.DescribeSdlEventListRequest,
    ) -> main_models.DescribeSdlEventListResponse:
        runtime = RuntimeOptions()
        return self.describe_sdl_event_list_with_options(request, runtime)

    async def describe_sdl_event_list_async(
        self,
        request: main_models.DescribeSdlEventListRequest,
    ) -> main_models.DescribeSdlEventListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sdl_event_list_with_options_async(request, runtime)

    def describe_sdl_event_sd_list_with_options(
        self,
        request: main_models.DescribeSdlEventSdListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventSdListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventSdList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventSdListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdl_event_sd_list_with_options_async(
        self,
        request: main_models.DescribeSdlEventSdListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventSdListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_ip):
            query['DstIp'] = request.dst_ip
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventSdList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventSdListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdl_event_sd_list(
        self,
        request: main_models.DescribeSdlEventSdListRequest,
    ) -> main_models.DescribeSdlEventSdListResponse:
        runtime = RuntimeOptions()
        return self.describe_sdl_event_sd_list_with_options(request, runtime)

    async def describe_sdl_event_sd_list_async(
        self,
        request: main_models.DescribeSdlEventSdListRequest,
    ) -> main_models.DescribeSdlEventSdListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sdl_event_sd_list_with_options_async(request, runtime)

    def describe_sdl_event_statistic_with_options(
        self,
        request: main_models.DescribeSdlEventStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdl_event_statistic_with_options_async(
        self,
        request: main_models.DescribeSdlEventStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlEventStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlEventStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlEventStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdl_event_statistic(
        self,
        request: main_models.DescribeSdlEventStatisticRequest,
    ) -> main_models.DescribeSdlEventStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_sdl_event_statistic_with_options(request, runtime)

    async def describe_sdl_event_statistic_async(
        self,
        request: main_models.DescribeSdlEventStatisticRequest,
    ) -> main_models.DescribeSdlEventStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_sdl_event_statistic_with_options_async(request, runtime)

    def describe_sdl_statistic_with_options(
        self,
        request: main_models.DescribeSdlStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdl_statistic_with_options_async(
        self,
        request: main_models.DescribeSdlStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSdlStatisticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSdlStatistic',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSdlStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdl_statistic(
        self,
        request: main_models.DescribeSdlStatisticRequest,
    ) -> main_models.DescribeSdlStatisticResponse:
        runtime = RuntimeOptions()
        return self.describe_sdl_statistic_with_options(request, runtime)

    async def describe_sdl_statistic_async(
        self,
        request: main_models.DescribeSdlStatisticRequest,
    ) -> main_models.DescribeSdlStatisticResponse:
        runtime = RuntimeOptions()
        return await self.describe_sdl_statistic_with_options_async(request, runtime)

    def describe_security_mode_with_options(
        self,
        request: main_models.DescribeSecurityModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityMode',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_mode_with_options_async(
        self,
        request: main_models.DescribeSecurityModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityMode',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_mode(
        self,
        request: main_models.DescribeSecurityModeRequest,
    ) -> main_models.DescribeSecurityModeResponse:
        runtime = RuntimeOptions()
        return self.describe_security_mode_with_options(request, runtime)

    async def describe_security_mode_async(
        self,
        request: main_models.DescribeSecurityModeRequest,
    ) -> main_models.DescribeSecurityModeResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_mode_with_options_async(request, runtime)

    def describe_security_proxy_with_options(
        self,
        request: main_models.DescribeSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_proxy_with_options_async(
        self,
        request: main_models.DescribeSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_proxy(
        self,
        request: main_models.DescribeSecurityProxyRequest,
    ) -> main_models.DescribeSecurityProxyResponse:
        runtime = RuntimeOptions()
        return self.describe_security_proxy_with_options(request, runtime)

    async def describe_security_proxy_async(
        self,
        request: main_models.DescribeSecurityProxyRequest,
    ) -> main_models.DescribeSecurityProxyResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_proxy_with_options_async(request, runtime)

    def describe_security_proxy_resources_with_options(
        self,
        request: main_models.DescribeSecurityProxyResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityProxyResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityProxyResources',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityProxyResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_proxy_resources_with_options_async(
        self,
        request: main_models.DescribeSecurityProxyResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityProxyResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityProxyResources',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityProxyResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_proxy_resources(
        self,
        request: main_models.DescribeSecurityProxyResourcesRequest,
    ) -> main_models.DescribeSecurityProxyResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_security_proxy_resources_with_options(request, runtime)

    async def describe_security_proxy_resources_async(
        self,
        request: main_models.DescribeSecurityProxyResourcesRequest,
    ) -> main_models.DescribeSecurityProxyResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_proxy_resources_with_options_async(request, runtime)

    def describe_sensitive_switch_with_options(
        self,
        request: main_models.DescribeSensitiveSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not DaraCore.is_null(request.sensitive_category):
            query['SensitiveCategory'] = request.sensitive_category
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sensitive_switch_with_options_async(
        self,
        request: main_models.DescribeSensitiveSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSensitiveSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not DaraCore.is_null(request.sensitive_category):
            query['SensitiveCategory'] = request.sensitive_category
        if not DaraCore.is_null(request.sensitive_level):
            query['SensitiveLevel'] = request.sensitive_level
        if not DaraCore.is_null(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSensitiveSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSensitiveSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sensitive_switch(
        self,
        request: main_models.DescribeSensitiveSwitchRequest,
    ) -> main_models.DescribeSensitiveSwitchResponse:
        runtime = RuntimeOptions()
        return self.describe_sensitive_switch_with_options(request, runtime)

    async def describe_sensitive_switch_async(
        self,
        request: main_models.DescribeSensitiveSwitchRequest,
    ) -> main_models.DescribeSensitiveSwitchResponse:
        runtime = RuntimeOptions()
        return await self.describe_sensitive_switch_with_options_async(request, runtime)

    def describe_signature_lib_version_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSignatureLibVersionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSignatureLibVersion',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSignatureLibVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_signature_lib_version_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSignatureLibVersionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSignatureLibVersion',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSignatureLibVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_signature_lib_version(self) -> main_models.DescribeSignatureLibVersionResponse:
        runtime = RuntimeOptions()
        return self.describe_signature_lib_version_with_options(runtime)

    async def describe_signature_lib_version_async(self) -> main_models.DescribeSignatureLibVersionResponse:
        runtime = RuntimeOptions()
        return await self.describe_signature_lib_version_with_options_async(runtime)

    def describe_slr_grant_with_options(
        self,
        request: main_models.DescribeSlrGrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlrGrantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlrGrant',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlrGrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slr_grant_with_options_async(
        self,
        request: main_models.DescribeSlrGrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlrGrantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlrGrant',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlrGrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slr_grant(
        self,
        request: main_models.DescribeSlrGrantRequest,
    ) -> main_models.DescribeSlrGrantResponse:
        runtime = RuntimeOptions()
        return self.describe_slr_grant_with_options(request, runtime)

    async def describe_slr_grant_async(
        self,
        request: main_models.DescribeSlrGrantRequest,
    ) -> main_models.DescribeSlrGrantResponse:
        runtime = RuntimeOptions()
        return await self.describe_slr_grant_with_options_async(request, runtime)

    def describe_sls_analyze_open_status_with_options(
        self,
        request: main_models.DescribeSlsAnalyzeOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAnalyzeOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAnalyzeOpenStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAnalyzeOpenStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sls_analyze_open_status_with_options_async(
        self,
        request: main_models.DescribeSlsAnalyzeOpenStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlsAnalyzeOpenStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlsAnalyzeOpenStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlsAnalyzeOpenStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sls_analyze_open_status(
        self,
        request: main_models.DescribeSlsAnalyzeOpenStatusRequest,
    ) -> main_models.DescribeSlsAnalyzeOpenStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_sls_analyze_open_status_with_options(request, runtime)

    async def describe_sls_analyze_open_status_async(
        self,
        request: main_models.DescribeSlsAnalyzeOpenStatusRequest,
    ) -> main_models.DescribeSlsAnalyzeOpenStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_sls_analyze_open_status_with_options_async(request, runtime)

    def describe_threat_intelligence_switch_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeThreatIntelligenceSwitchResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeThreatIntelligenceSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeThreatIntelligenceSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_threat_intelligence_switch_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeThreatIntelligenceSwitchResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeThreatIntelligenceSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeThreatIntelligenceSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_threat_intelligence_switch(self) -> main_models.DescribeThreatIntelligenceSwitchResponse:
        runtime = RuntimeOptions()
        return self.describe_threat_intelligence_switch_with_options(runtime)

    async def describe_threat_intelligence_switch_async(self) -> main_models.DescribeThreatIntelligenceSwitchResponse:
        runtime = RuntimeOptions()
        return await self.describe_threat_intelligence_switch_with_options_async(runtime)

    def describe_tr_firewall_policy_back_up_association_list_with_options(
        self,
        tmp_req: main_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        tmp_req.validate()
        request = main_models.DescribeTrFirewallPolicyBackUpAssociationListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.candidate_list):
            request.candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.candidate_list, 'CandidateList', 'json')
        query = {}
        if not DaraCore.is_null(request.candidate_list_shrink):
            query['CandidateList'] = request.candidate_list_shrink
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallPolicyBackUpAssociationList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallPolicyBackUpAssociationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewall_policy_back_up_association_list_with_options_async(
        self,
        tmp_req: main_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        tmp_req.validate()
        request = main_models.DescribeTrFirewallPolicyBackUpAssociationListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.candidate_list):
            request.candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.candidate_list, 'CandidateList', 'json')
        query = {}
        if not DaraCore.is_null(request.candidate_list_shrink):
            query['CandidateList'] = request.candidate_list_shrink
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallPolicyBackUpAssociationList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallPolicyBackUpAssociationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewall_policy_back_up_association_list(
        self,
        request: main_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
    ) -> main_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        runtime = RuntimeOptions()
        return self.describe_tr_firewall_policy_back_up_association_list_with_options(request, runtime)

    async def describe_tr_firewall_policy_back_up_association_list_async(
        self,
        request: main_models.DescribeTrFirewallPolicyBackUpAssociationListRequest,
    ) -> main_models.DescribeTrFirewallPolicyBackUpAssociationListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tr_firewall_policy_back_up_association_list_with_options_async(request, runtime)

    def describe_tr_firewall_v2route_policy_list_with_options(
        self,
        request: main_models.DescribeTrFirewallV2RoutePolicyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallV2RoutePolicyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallV2RoutePolicyList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallV2RoutePolicyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewall_v2route_policy_list_with_options_async(
        self,
        request: main_models.DescribeTrFirewallV2RoutePolicyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallV2RoutePolicyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallV2RoutePolicyList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallV2RoutePolicyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewall_v2route_policy_list(
        self,
        request: main_models.DescribeTrFirewallV2RoutePolicyListRequest,
    ) -> main_models.DescribeTrFirewallV2RoutePolicyListResponse:
        runtime = RuntimeOptions()
        return self.describe_tr_firewall_v2route_policy_list_with_options(request, runtime)

    async def describe_tr_firewall_v2route_policy_list_async(
        self,
        request: main_models.DescribeTrFirewallV2RoutePolicyListRequest,
    ) -> main_models.DescribeTrFirewallV2RoutePolicyListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tr_firewall_v2route_policy_list_with_options_async(request, runtime)

    def describe_tr_firewalls_v2detail_with_options(
        self,
        request: main_models.DescribeTrFirewallsV2DetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallsV2DetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallsV2Detail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallsV2DetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewalls_v2detail_with_options_async(
        self,
        request: main_models.DescribeTrFirewallsV2DetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallsV2DetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallsV2Detail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallsV2DetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewalls_v2detail(
        self,
        request: main_models.DescribeTrFirewallsV2DetailRequest,
    ) -> main_models.DescribeTrFirewallsV2DetailResponse:
        runtime = RuntimeOptions()
        return self.describe_tr_firewalls_v2detail_with_options(request, runtime)

    async def describe_tr_firewalls_v2detail_async(
        self,
        request: main_models.DescribeTrFirewallsV2DetailRequest,
    ) -> main_models.DescribeTrFirewallsV2DetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_tr_firewalls_v2detail_with_options_async(request, runtime)

    def describe_tr_firewalls_v2list_with_options(
        self,
        request: main_models.DescribeTrFirewallsV2ListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallsV2ListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not DaraCore.is_null(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallsV2List',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallsV2ListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewalls_v2list_with_options_async(
        self,
        request: main_models.DescribeTrFirewallsV2ListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallsV2ListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not DaraCore.is_null(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallsV2List',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallsV2ListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewalls_v2list(
        self,
        request: main_models.DescribeTrFirewallsV2ListRequest,
    ) -> main_models.DescribeTrFirewallsV2ListResponse:
        runtime = RuntimeOptions()
        return self.describe_tr_firewalls_v2list_with_options(request, runtime)

    async def describe_tr_firewalls_v2list_async(
        self,
        request: main_models.DescribeTrFirewallsV2ListRequest,
    ) -> main_models.DescribeTrFirewallsV2ListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tr_firewalls_v2list_with_options_async(request, runtime)

    def describe_tr_firewalls_v2route_list_with_options(
        self,
        request: main_models.DescribeTrFirewallsV2RouteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallsV2RouteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallsV2RouteList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallsV2RouteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tr_firewalls_v2route_list_with_options_async(
        self,
        request: main_models.DescribeTrFirewallsV2RouteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrFirewallsV2RouteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrFirewallsV2RouteList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrFirewallsV2RouteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tr_firewalls_v2route_list(
        self,
        request: main_models.DescribeTrFirewallsV2RouteListRequest,
    ) -> main_models.DescribeTrFirewallsV2RouteListResponse:
        runtime = RuntimeOptions()
        return self.describe_tr_firewalls_v2route_list_with_options(request, runtime)

    async def describe_tr_firewalls_v2route_list_async(
        self,
        request: main_models.DescribeTrFirewallsV2RouteListRequest,
    ) -> main_models.DescribeTrFirewallsV2RouteListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tr_firewalls_v2route_list_with_options_async(request, runtime)

    def describe_traffic_log_with_options(
        self,
        request: main_models.DescribeTrafficLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_pre_rule_id):
            query['AclPreRuleId'] = request.acl_pre_rule_id
        if not DaraCore.is_null(request.acl_pre_state):
            query['AclPreState'] = request.acl_pre_state
        if not DaraCore.is_null(request.app_dpi_state):
            query['AppDpiState'] = request.app_dpi_state
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.asset_region):
            query['AssetRegion'] = request.asset_region
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_url):
            query['DomainUrl'] = request.domain_url
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not DaraCore.is_null(request.dst_vpc_region_no):
            query['DstVpcRegionNo'] = request.dst_vpc_region_no
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.flow_type):
            query['FlowType'] = request.flow_type
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_firewall_id):
            query['NatFirewallId'] = request.nat_firewall_id
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_port):
            query['SrcPort'] = request.src_port
        if not DaraCore.is_null(request.src_private_ip):
            query['SrcPrivateIP'] = request.src_private_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.src_vpc_region_no):
            query['SrcVpcRegionNo'] = request.src_vpc_region_no
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tls_scope_id):
            query['TlsScopeId'] = request.tls_scope_id
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vul_level):
            query['VulLevel'] = request.vul_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrafficLog',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_log_with_options_async(
        self,
        request: main_models.DescribeTrafficLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTrafficLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_pre_rule_id):
            query['AclPreRuleId'] = request.acl_pre_rule_id
        if not DaraCore.is_null(request.acl_pre_state):
            query['AclPreState'] = request.acl_pre_state
        if not DaraCore.is_null(request.app_dpi_state):
            query['AppDpiState'] = request.app_dpi_state
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.asset_region):
            query['AssetRegion'] = request.asset_region
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_url):
            query['DomainUrl'] = request.domain_url
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_port):
            query['DstPort'] = request.dst_port
        if not DaraCore.is_null(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not DaraCore.is_null(request.dst_vpc_region_no):
            query['DstVpcRegionNo'] = request.dst_vpc_region_no
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.flow_type):
            query['FlowType'] = request.flow_type
        if not DaraCore.is_null(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.nat_firewall_id):
            query['NatFirewallId'] = request.nat_firewall_id
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_result):
            query['RuleResult'] = request.rule_result
        if not DaraCore.is_null(request.rule_source):
            query['RuleSource'] = request.rule_source
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_port):
            query['SrcPort'] = request.src_port
        if not DaraCore.is_null(request.src_private_ip):
            query['SrcPrivateIP'] = request.src_private_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.src_vpc_region_no):
            query['SrcVpcRegionNo'] = request.src_vpc_region_no
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tls_scope_id):
            query['TlsScopeId'] = request.tls_scope_id
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vul_level):
            query['VulLevel'] = request.vul_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrafficLog',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTrafficLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic_log(
        self,
        request: main_models.DescribeTrafficLogRequest,
    ) -> main_models.DescribeTrafficLogResponse:
        runtime = RuntimeOptions()
        return self.describe_traffic_log_with_options(request, runtime)

    async def describe_traffic_log_async(
        self,
        request: main_models.DescribeTrafficLogRequest,
    ) -> main_models.DescribeTrafficLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_traffic_log_with_options_async(request, runtime)

    def describe_transit_router_resources_list_with_options(
        self,
        request: main_models.DescribeTransitRouterResourcesListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransitRouterResourcesListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransitRouterResourcesList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransitRouterResourcesListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transit_router_resources_list_with_options_async(
        self,
        request: main_models.DescribeTransitRouterResourcesListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransitRouterResourcesListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransitRouterResourcesList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransitRouterResourcesListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transit_router_resources_list(
        self,
        request: main_models.DescribeTransitRouterResourcesListRequest,
    ) -> main_models.DescribeTransitRouterResourcesListResponse:
        runtime = RuntimeOptions()
        return self.describe_transit_router_resources_list_with_options(request, runtime)

    async def describe_transit_router_resources_list_async(
        self,
        request: main_models.DescribeTransitRouterResourcesListRequest,
    ) -> main_models.DescribeTransitRouterResourcesListResponse:
        runtime = RuntimeOptions()
        return await self.describe_transit_router_resources_list_with_options_async(request, runtime)

    def describe_unprotected_port_trend_with_options(
        self,
        request: main_models.DescribeUnprotectedPortTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnprotectedPortTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnprotectedPortTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnprotectedPortTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_unprotected_port_trend_with_options_async(
        self,
        request: main_models.DescribeUnprotectedPortTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnprotectedPortTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnprotectedPortTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnprotectedPortTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_unprotected_port_trend(
        self,
        request: main_models.DescribeUnprotectedPortTrendRequest,
    ) -> main_models.DescribeUnprotectedPortTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_unprotected_port_trend_with_options(request, runtime)

    async def describe_unprotected_port_trend_async(
        self,
        request: main_models.DescribeUnprotectedPortTrendRequest,
    ) -> main_models.DescribeUnprotectedPortTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_unprotected_port_trend_with_options_async(request, runtime)

    def describe_unprotected_vuln_trend_with_options(
        self,
        request: main_models.DescribeUnprotectedVulnTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnprotectedVulnTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnprotectedVulnTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnprotectedVulnTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_unprotected_vuln_trend_with_options_async(
        self,
        request: main_models.DescribeUnprotectedVulnTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnprotectedVulnTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnprotectedVulnTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnprotectedVulnTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_unprotected_vuln_trend(
        self,
        request: main_models.DescribeUnprotectedVulnTrendRequest,
    ) -> main_models.DescribeUnprotectedVulnTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_unprotected_vuln_trend_with_options(request, runtime)

    async def describe_unprotected_vuln_trend_async(
        self,
        request: main_models.DescribeUnprotectedVulnTrendRequest,
    ) -> main_models.DescribeUnprotectedVulnTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_unprotected_vuln_trend_with_options_async(request, runtime)

    def describe_user_alarm_config_with_options(
        self,
        request: main_models.DescribeUserAlarmConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAlarmConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAlarmConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAlarmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_alarm_config_with_options_async(
        self,
        request: main_models.DescribeUserAlarmConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAlarmConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAlarmConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAlarmConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_alarm_config(
        self,
        request: main_models.DescribeUserAlarmConfigRequest,
    ) -> main_models.DescribeUserAlarmConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_user_alarm_config_with_options(request, runtime)

    async def describe_user_alarm_config_async(
        self,
        request: main_models.DescribeUserAlarmConfigRequest,
    ) -> main_models.DescribeUserAlarmConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_alarm_config_with_options_async(request, runtime)

    def describe_user_asset_iptraffic_info_with_options(
        self,
        request: main_models.DescribeUserAssetIPTrafficInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAssetIPTrafficInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAssetIPTrafficInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAssetIPTrafficInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_asset_iptraffic_info_with_options_async(
        self,
        request: main_models.DescribeUserAssetIPTrafficInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserAssetIPTrafficInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserAssetIPTrafficInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserAssetIPTrafficInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_asset_iptraffic_info(
        self,
        request: main_models.DescribeUserAssetIPTrafficInfoRequest,
    ) -> main_models.DescribeUserAssetIPTrafficInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_user_asset_iptraffic_info_with_options(request, runtime)

    async def describe_user_asset_iptraffic_info_async(
        self,
        request: main_models.DescribeUserAssetIPTrafficInfoRequest,
    ) -> main_models.DescribeUserAssetIPTrafficInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_asset_iptraffic_info_with_options_async(request, runtime)

    def describe_user_buy_version_with_options(
        self,
        request: main_models.DescribeUserBuyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserBuyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserBuyVersion',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserBuyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_buy_version_with_options_async(
        self,
        request: main_models.DescribeUserBuyVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserBuyVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserBuyVersion',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserBuyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_buy_version(
        self,
        request: main_models.DescribeUserBuyVersionRequest,
    ) -> main_models.DescribeUserBuyVersionResponse:
        runtime = RuntimeOptions()
        return self.describe_user_buy_version_with_options(request, runtime)

    async def describe_user_buy_version_async(
        self,
        request: main_models.DescribeUserBuyVersionRequest,
    ) -> main_models.DescribeUserBuyVersionResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_buy_version_with_options_async(request, runtime)

    def describe_user_ipswhitelist_with_options(
        self,
        request: main_models.DescribeUserIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_ipswhitelist_with_options_async(
        self,
        request: main_models.DescribeUserIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_ipswhitelist(
        self,
        request: main_models.DescribeUserIPSWhitelistRequest,
    ) -> main_models.DescribeUserIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return self.describe_user_ipswhitelist_with_options(request, runtime)

    async def describe_user_ipswhitelist_async(
        self,
        request: main_models.DescribeUserIPSWhitelistRequest,
    ) -> main_models.DescribeUserIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_ipswhitelist_with_options_async(request, runtime)

    def describe_vfw_ipsconfig_list_with_options(
        self,
        request: main_models.DescribeVfwIPSConfigListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVfwIPSConfigListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVfwIPSConfigList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVfwIPSConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vfw_ipsconfig_list_with_options_async(
        self,
        request: main_models.DescribeVfwIPSConfigListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVfwIPSConfigListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVfwIPSConfigList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVfwIPSConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vfw_ipsconfig_list(
        self,
        request: main_models.DescribeVfwIPSConfigListRequest,
    ) -> main_models.DescribeVfwIPSConfigListResponse:
        runtime = RuntimeOptions()
        return self.describe_vfw_ipsconfig_list_with_options(request, runtime)

    async def describe_vfw_ipsconfig_list_async(
        self,
        request: main_models.DescribeVfwIPSConfigListRequest,
    ) -> main_models.DescribeVfwIPSConfigListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vfw_ipsconfig_list_with_options_async(request, runtime)

    def describe_vpc_firewall_access_detail_with_options(
        self,
        request: main_models.DescribeVpcFirewallAccessDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAccessDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_ip):
            query['AssetIP'] = request.asset_ip
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ipprotocol):
            query['IPProtocol'] = request.ipprotocol
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.peer_asset_ip):
            query['PeerAssetIP'] = request.peer_asset_ip
        if not DaraCore.is_null(request.peer_asset_instance_id):
            query['PeerAssetInstanceId'] = request.peer_asset_instance_id
        if not DaraCore.is_null(request.peer_asset_instance_name):
            query['PeerAssetInstanceName'] = request.peer_asset_instance_name
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAccessDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAccessDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_access_detail_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallAccessDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAccessDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_ip):
            query['AssetIP'] = request.asset_ip
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ipprotocol):
            query['IPProtocol'] = request.ipprotocol
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.peer_asset_ip):
            query['PeerAssetIP'] = request.peer_asset_ip
        if not DaraCore.is_null(request.peer_asset_instance_id):
            query['PeerAssetInstanceId'] = request.peer_asset_instance_id
        if not DaraCore.is_null(request.peer_asset_instance_name):
            query['PeerAssetInstanceName'] = request.peer_asset_instance_name
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAccessDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAccessDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_access_detail(
        self,
        request: main_models.DescribeVpcFirewallAccessDetailRequest,
    ) -> main_models.DescribeVpcFirewallAccessDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_access_detail_with_options(request, runtime)

    async def describe_vpc_firewall_access_detail_async(
        self,
        request: main_models.DescribeVpcFirewallAccessDetailRequest,
    ) -> main_models.DescribeVpcFirewallAccessDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_access_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_acl_group_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAclGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_configure_status):
            query['FirewallConfigureStatus'] = request.firewall_configure_status
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAclGroupList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAclGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_acl_group_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallAclGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAclGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_configure_status):
            query['FirewallConfigureStatus'] = request.firewall_configure_status
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAclGroupList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAclGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_acl_group_list(
        self,
        request: main_models.DescribeVpcFirewallAclGroupListRequest,
    ) -> main_models.DescribeVpcFirewallAclGroupListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_acl_group_list_with_options(request, runtime)

    async def describe_vpc_firewall_acl_group_list_async(
        self,
        request: main_models.DescribeVpcFirewallAclGroupListRequest,
    ) -> main_models.DescribeVpcFirewallAclGroupListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_acl_group_list_with_options_async(request, runtime)

    def describe_vpc_firewall_asset_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallAssetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAssetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_ip):
            query['AssetIP'] = request.asset_ip
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.ecs_instance_name):
            query['EcsInstanceName'] = request.ecs_instance_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ipprotocol):
            query['IPProtocol'] = request.ipprotocol
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAssetList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAssetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_asset_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallAssetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAssetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.asset_ip):
            query['AssetIP'] = request.asset_ip
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.ecs_instance_name):
            query['EcsInstanceName'] = request.ecs_instance_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.ipprotocol):
            query['IPProtocol'] = request.ipprotocol
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAssetList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAssetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_asset_list(
        self,
        request: main_models.DescribeVpcFirewallAssetListRequest,
    ) -> main_models.DescribeVpcFirewallAssetListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_asset_list_with_options(request, runtime)

    async def describe_vpc_firewall_asset_list_async(
        self,
        request: main_models.DescribeVpcFirewallAssetListRequest,
    ) -> main_models.DescribeVpcFirewallAssetListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_asset_list_with_options_async(request, runtime)

    def describe_vpc_firewall_asset_region_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallAssetRegionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAssetRegionListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAssetRegionList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAssetRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_asset_region_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallAssetRegionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallAssetRegionListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallAssetRegionList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallAssetRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_asset_region_list(
        self,
        request: main_models.DescribeVpcFirewallAssetRegionListRequest,
    ) -> main_models.DescribeVpcFirewallAssetRegionListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_asset_region_list_with_options(request, runtime)

    async def describe_vpc_firewall_asset_region_list_async(
        self,
        request: main_models.DescribeVpcFirewallAssetRegionListRequest,
    ) -> main_models.DescribeVpcFirewallAssetRegionListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_asset_region_list_with_options_async(request, runtime)

    def describe_vpc_firewall_cen_detail_with_options(
        self,
        request: main_models.DescribeVpcFirewallCenDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallCenDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallCenDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallCenDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_cen_detail_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallCenDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallCenDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallCenDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallCenDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_cen_detail(
        self,
        request: main_models.DescribeVpcFirewallCenDetailRequest,
    ) -> main_models.DescribeVpcFirewallCenDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_cen_detail_with_options(request, runtime)

    async def describe_vpc_firewall_cen_detail_async(
        self,
        request: main_models.DescribeVpcFirewallCenDetailRequest,
    ) -> main_models.DescribeVpcFirewallCenDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_cen_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_cen_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallCenListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallCenListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not DaraCore.is_null(request.transit_router_type):
            query['TransitRouterType'] = request.transit_router_type
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallCenList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallCenListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_cen_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallCenListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallCenListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_id):
            query['NetworkInstanceId'] = request.network_instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.route_mode):
            query['RouteMode'] = request.route_mode
        if not DaraCore.is_null(request.transit_router_type):
            query['TransitRouterType'] = request.transit_router_type
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallCenList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallCenListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_cen_list(
        self,
        request: main_models.DescribeVpcFirewallCenListRequest,
    ) -> main_models.DescribeVpcFirewallCenListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_cen_list_with_options(request, runtime)

    async def describe_vpc_firewall_cen_list_async(
        self,
        request: main_models.DescribeVpcFirewallCenListRequest,
    ) -> main_models.DescribeVpcFirewallCenListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_cen_list_with_options_async(request, runtime)

    def describe_vpc_firewall_cen_summary_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallCenSummaryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallCenSummaryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.transit_router_type):
            query['TransitRouterType'] = request.transit_router_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallCenSummaryList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallCenSummaryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_cen_summary_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallCenSummaryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallCenSummaryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.transit_router_type):
            query['TransitRouterType'] = request.transit_router_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallCenSummaryList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallCenSummaryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_cen_summary_list(
        self,
        request: main_models.DescribeVpcFirewallCenSummaryListRequest,
    ) -> main_models.DescribeVpcFirewallCenSummaryListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_cen_summary_list_with_options(request, runtime)

    async def describe_vpc_firewall_cen_summary_list_async(
        self,
        request: main_models.DescribeVpcFirewallCenSummaryListRequest,
    ) -> main_models.DescribeVpcFirewallCenSummaryListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_cen_summary_list_with_options_async(request, runtime)

    def describe_vpc_firewall_control_policy_with_options(
        self,
        request: main_models.DescribeVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_control_policy_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_control_policy(
        self,
        request: main_models.DescribeVpcFirewallControlPolicyRequest,
    ) -> main_models.DescribeVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_control_policy_with_options(request, runtime)

    async def describe_vpc_firewall_control_policy_async(
        self,
        request: main_models.DescribeVpcFirewallControlPolicyRequest,
    ) -> main_models.DescribeVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_control_policy_with_options_async(request, runtime)

    def describe_vpc_firewall_default_ipsconfig_with_options(
        self,
        request: main_models.DescribeVpcFirewallDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_default_ipsconfig_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_default_ipsconfig(
        self,
        request: main_models.DescribeVpcFirewallDefaultIPSConfigRequest,
    ) -> main_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_default_ipsconfig_with_options(request, runtime)

    async def describe_vpc_firewall_default_ipsconfig_async(
        self,
        request: main_models.DescribeVpcFirewallDefaultIPSConfigRequest,
    ) -> main_models.DescribeVpcFirewallDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_default_ipsconfig_with_options_async(request, runtime)

    def describe_vpc_firewall_detail_with_options(
        self,
        request: main_models.DescribeVpcFirewallDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_detail_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.local_vpc_id):
            query['LocalVpcId'] = request.local_vpc_id
        if not DaraCore.is_null(request.peer_vpc_id):
            query['PeerVpcId'] = request.peer_vpc_id
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_detail(
        self,
        request: main_models.DescribeVpcFirewallDetailRequest,
    ) -> main_models.DescribeVpcFirewallDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_detail_with_options(request, runtime)

    async def describe_vpc_firewall_detail_async(
        self,
        request: main_models.DescribeVpcFirewallDetailRequest,
    ) -> main_models.DescribeVpcFirewallDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_domain_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDomainList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_domain_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_aitraffic):
            query['IsAITraffic'] = request.is_aitraffic
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDomainList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_domain_list(
        self,
        request: main_models.DescribeVpcFirewallDomainListRequest,
    ) -> main_models.DescribeVpcFirewallDomainListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_domain_list_with_options(request, runtime)

    async def describe_vpc_firewall_domain_list_async(
        self,
        request: main_models.DescribeVpcFirewallDomainListRequest,
    ) -> main_models.DescribeVpcFirewallDomainListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_domain_list_with_options_async(request, runtime)

    def describe_vpc_firewall_domain_relation_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallDomainRelationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDomainRelationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDomainRelationList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDomainRelationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_domain_relation_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallDomainRelationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDomainRelationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain_list):
            query['DomainList'] = request.domain_list
        if not DaraCore.is_null(request.dst_ip):
            query['DstIP'] = request.dst_ip
        if not DaraCore.is_null(request.dst_vpc_id):
            query['DstVpcId'] = request.dst_vpc_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.src_ip):
            query['SrcIP'] = request.src_ip
        if not DaraCore.is_null(request.src_vpc_id):
            query['SrcVpcId'] = request.src_vpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDomainRelationList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDomainRelationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_domain_relation_list(
        self,
        request: main_models.DescribeVpcFirewallDomainRelationListRequest,
    ) -> main_models.DescribeVpcFirewallDomainRelationListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_domain_relation_list_with_options(request, runtime)

    async def describe_vpc_firewall_domain_relation_list_async(
        self,
        request: main_models.DescribeVpcFirewallDomainRelationListRequest,
    ) -> main_models.DescribeVpcFirewallDomainRelationListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_domain_relation_list_with_options_async(request, runtime)

    def describe_vpc_firewall_drop_traffic_trend_with_options(
        self,
        request: main_models.DescribeVpcFirewallDropTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDropTrafficTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDropTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDropTrafficTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_drop_traffic_trend_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallDropTrafficTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallDropTrafficTrendResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallDropTrafficTrend',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallDropTrafficTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_drop_traffic_trend(
        self,
        request: main_models.DescribeVpcFirewallDropTrafficTrendRequest,
    ) -> main_models.DescribeVpcFirewallDropTrafficTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_drop_traffic_trend_with_options(request, runtime)

    async def describe_vpc_firewall_drop_traffic_trend_async(
        self,
        request: main_models.DescribeVpcFirewallDropTrafficTrendRequest,
    ) -> main_models.DescribeVpcFirewallDropTrafficTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_drop_traffic_trend_with_options_async(request, runtime)

    def describe_vpc_firewall_ipswhitelist_with_options(
        self,
        request: main_models.DescribeVpcFirewallIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_ipswhitelist_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_ipswhitelist(
        self,
        request: main_models.DescribeVpcFirewallIPSWhitelistRequest,
    ) -> main_models.DescribeVpcFirewallIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_ipswhitelist_with_options(request, runtime)

    async def describe_vpc_firewall_ipswhitelist_async(
        self,
        request: main_models.DescribeVpcFirewallIPSWhitelistRequest,
    ) -> main_models.DescribeVpcFirewallIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_ipswhitelist_with_options_async(request, runtime)

    def describe_vpc_firewall_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_sub_type):
            query['ConnectSubType'] = request.connect_sub_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.peer_uid):
            query['PeerUid'] = request.peer_uid
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connect_sub_type):
            query['ConnectSubType'] = request.connect_sub_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.firewall_switch_status):
            query['FirewallSwitchStatus'] = request.firewall_switch_status
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.peer_uid):
            query['PeerUid'] = request.peer_uid
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_list(
        self,
        request: main_models.DescribeVpcFirewallListRequest,
    ) -> main_models.DescribeVpcFirewallListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_list_with_options(request, runtime)

    async def describe_vpc_firewall_list_async(
        self,
        request: main_models.DescribeVpcFirewallListRequest,
    ) -> main_models.DescribeVpcFirewallListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_list_with_options_async(request, runtime)

    def describe_vpc_firewall_manual_vswitch_list_with_options(
        self,
        request: main_models.DescribeVpcFirewallManualVSwitchListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallManualVSwitchListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallManualVSwitchList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallManualVSwitchListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_manual_vswitch_list_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallManualVSwitchListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallManualVSwitchListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallManualVSwitchList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallManualVSwitchListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_manual_vswitch_list(
        self,
        request: main_models.DescribeVpcFirewallManualVSwitchListRequest,
    ) -> main_models.DescribeVpcFirewallManualVSwitchListResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_manual_vswitch_list_with_options(request, runtime)

    async def describe_vpc_firewall_manual_vswitch_list_async(
        self,
        request: main_models.DescribeVpcFirewallManualVSwitchListRequest,
    ) -> main_models.DescribeVpcFirewallManualVSwitchListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_manual_vswitch_list_with_options_async(request, runtime)

    def describe_vpc_firewall_policy_prior_used_with_options(
        self,
        request: main_models.DescribeVpcFirewallPolicyPriorUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallPolicyPriorUsed',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallPolicyPriorUsedResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_policy_prior_used_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallPolicyPriorUsedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallPolicyPriorUsed',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallPolicyPriorUsedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_policy_prior_used(
        self,
        request: main_models.DescribeVpcFirewallPolicyPriorUsedRequest,
    ) -> main_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_policy_prior_used_with_options(request, runtime)

    async def describe_vpc_firewall_policy_prior_used_async(
        self,
        request: main_models.DescribeVpcFirewallPolicyPriorUsedRequest,
    ) -> main_models.DescribeVpcFirewallPolicyPriorUsedResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_policy_prior_used_with_options_async(request, runtime)

    def describe_vpc_firewall_precheck_detail_with_options(
        self,
        request: main_models.DescribeVpcFirewallPrecheckDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallPrecheckDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_type):
            query['NetworkInstanceType'] = request.network_instance_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallPrecheckDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallPrecheckDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_precheck_detail_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallPrecheckDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallPrecheckDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.network_instance_type):
            query['NetworkInstanceType'] = request.network_instance_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallPrecheckDetail',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallPrecheckDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_precheck_detail(
        self,
        request: main_models.DescribeVpcFirewallPrecheckDetailRequest,
    ) -> main_models.DescribeVpcFirewallPrecheckDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_precheck_detail_with_options(request, runtime)

    async def describe_vpc_firewall_precheck_detail_async(
        self,
        request: main_models.DescribeVpcFirewallPrecheckDetailRequest,
    ) -> main_models.DescribeVpcFirewallPrecheckDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_precheck_detail_with_options_async(request, runtime)

    def describe_vpc_firewall_summary_info_with_options(
        self,
        request: main_models.DescribeVpcFirewallSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallSummaryInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallSummaryInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_summary_info_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallSummaryInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallSummaryInfo',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_summary_info(
        self,
        request: main_models.DescribeVpcFirewallSummaryInfoRequest,
    ) -> main_models.DescribeVpcFirewallSummaryInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_summary_info_with_options(request, runtime)

    async def describe_vpc_firewall_summary_info_async(
        self,
        request: main_models.DescribeVpcFirewallSummaryInfoRequest,
    ) -> main_models.DescribeVpcFirewallSummaryInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_summary_info_with_options_async(request, runtime)

    def describe_vpc_firewall_zone_with_options(
        self,
        request: main_models.DescribeVpcFirewallZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallZone',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_firewall_zone_with_options_async(
        self,
        request: main_models.DescribeVpcFirewallZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcFirewallZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cen_id):
            query['CenId'] = request.cen_id
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.transit_router_id):
            query['TransitRouterId'] = request.transit_router_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcFirewallZone',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcFirewallZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_firewall_zone(
        self,
        request: main_models.DescribeVpcFirewallZoneRequest,
    ) -> main_models.DescribeVpcFirewallZoneResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_firewall_zone_with_options(request, runtime)

    async def describe_vpc_firewall_zone_async(
        self,
        request: main_models.DescribeVpcFirewallZoneRequest,
    ) -> main_models.DescribeVpcFirewallZoneResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_firewall_zone_with_options_async(request, runtime)

    def describe_vpc_list_lite_with_options(
        self,
        request: main_models.DescribeVpcListLiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcListLiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcListLite',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcListLiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_list_lite_with_options_async(
        self,
        request: main_models.DescribeVpcListLiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcListLiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_name):
            query['VpcName'] = request.vpc_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcListLite',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcListLiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_list_lite(
        self,
        request: main_models.DescribeVpcListLiteRequest,
    ) -> main_models.DescribeVpcListLiteResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_list_lite_with_options(request, runtime)

    async def describe_vpc_list_lite_async(
        self,
        request: main_models.DescribeVpcListLiteRequest,
    ) -> main_models.DescribeVpcListLiteResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_list_lite_with_options_async(request, runtime)

    def describe_vpc_zone_with_options(
        self,
        request: main_models.DescribeVpcZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcZone',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpc_zone_with_options_async(
        self,
        request: main_models.DescribeVpcZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment):
            query['Environment'] = request.environment
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcZone',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpc_zone(
        self,
        request: main_models.DescribeVpcZoneRequest,
    ) -> main_models.DescribeVpcZoneResponse:
        runtime = RuntimeOptions()
        return self.describe_vpc_zone_with_options(request, runtime)

    async def describe_vpc_zone_async(
        self,
        request: main_models.DescribeVpcZoneRequest,
    ) -> main_models.DescribeVpcZoneResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpc_zone_with_options_async(request, runtime)

    def describe_vulnerability_protected_list_with_options(
        self,
        request: main_models.DescribeVulnerabilityProtectedListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVulnerabilityProtectedListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_tag):
            query['RuleTag'] = request.rule_tag
        if not DaraCore.is_null(request.sort_key):
            query['SortKey'] = request.sort_key
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        if not DaraCore.is_null(request.vuln_cve_name):
            query['VulnCveName'] = request.vuln_cve_name
        if not DaraCore.is_null(request.vuln_level):
            query['VulnLevel'] = request.vuln_level
        if not DaraCore.is_null(request.vuln_resource):
            query['VulnResource'] = request.vuln_resource
        if not DaraCore.is_null(request.vuln_status):
            query['VulnStatus'] = request.vuln_status
        if not DaraCore.is_null(request.vuln_type):
            query['VulnType'] = request.vuln_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVulnerabilityProtectedList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVulnerabilityProtectedListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vulnerability_protected_list_with_options_async(
        self,
        request: main_models.DescribeVulnerabilityProtectedListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVulnerabilityProtectedListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.buy_version):
            query['BuyVersion'] = request.buy_version
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_tag):
            query['RuleTag'] = request.rule_tag
        if not DaraCore.is_null(request.sort_key):
            query['SortKey'] = request.sort_key
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        if not DaraCore.is_null(request.vuln_cve_name):
            query['VulnCveName'] = request.vuln_cve_name
        if not DaraCore.is_null(request.vuln_level):
            query['VulnLevel'] = request.vuln_level
        if not DaraCore.is_null(request.vuln_resource):
            query['VulnResource'] = request.vuln_resource
        if not DaraCore.is_null(request.vuln_status):
            query['VulnStatus'] = request.vuln_status
        if not DaraCore.is_null(request.vuln_type):
            query['VulnType'] = request.vuln_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVulnerabilityProtectedList',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVulnerabilityProtectedListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vulnerability_protected_list(
        self,
        request: main_models.DescribeVulnerabilityProtectedListRequest,
    ) -> main_models.DescribeVulnerabilityProtectedListResponse:
        runtime = RuntimeOptions()
        return self.describe_vulnerability_protected_list_with_options(request, runtime)

    async def describe_vulnerability_protected_list_async(
        self,
        request: main_models.DescribeVulnerabilityProtectedListRequest,
    ) -> main_models.DescribeVulnerabilityProtectedListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vulnerability_protected_list_with_options_async(request, runtime)

    def disable_sdl_protected_asset_with_options(
        self,
        request: main_models.DisableSdlProtectedAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSdlProtectedAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSdlProtectedAsset',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSdlProtectedAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sdl_protected_asset_with_options_async(
        self,
        request: main_models.DisableSdlProtectedAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSdlProtectedAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSdlProtectedAsset',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSdlProtectedAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_sdl_protected_asset(
        self,
        request: main_models.DisableSdlProtectedAssetRequest,
    ) -> main_models.DisableSdlProtectedAssetResponse:
        runtime = RuntimeOptions()
        return self.disable_sdl_protected_asset_with_options(request, runtime)

    async def disable_sdl_protected_asset_async(
        self,
        request: main_models.DisableSdlProtectedAssetRequest,
    ) -> main_models.DisableSdlProtectedAssetResponse:
        runtime = RuntimeOptions()
        return await self.disable_sdl_protected_asset_with_options_async(request, runtime)

    def enable_sdl_protected_asset_with_options(
        self,
        request: main_models.EnableSdlProtectedAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSdlProtectedAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSdlProtectedAsset',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSdlProtectedAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sdl_protected_asset_with_options_async(
        self,
        request: main_models.EnableSdlProtectedAssetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSdlProtectedAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSdlProtectedAsset',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSdlProtectedAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sdl_protected_asset(
        self,
        request: main_models.EnableSdlProtectedAssetRequest,
    ) -> main_models.EnableSdlProtectedAssetResponse:
        runtime = RuntimeOptions()
        return self.enable_sdl_protected_asset_with_options(request, runtime)

    async def enable_sdl_protected_asset_async(
        self,
        request: main_models.EnableSdlProtectedAssetRequest,
    ) -> main_models.EnableSdlProtectedAssetResponse:
        runtime = RuntimeOptions()
        return await self.enable_sdl_protected_asset_with_options_async(request, runtime)

    def get_tls_inspect_certificate_download_url_with_options(
        self,
        request: main_models.GetTlsInspectCertificateDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlsInspectCertificateDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_cert_id):
            query['CaCertId'] = request.ca_cert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTlsInspectCertificateDownloadUrl',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlsInspectCertificateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tls_inspect_certificate_download_url_with_options_async(
        self,
        request: main_models.GetTlsInspectCertificateDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTlsInspectCertificateDownloadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_cert_id):
            query['CaCertId'] = request.ca_cert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTlsInspectCertificateDownloadUrl',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTlsInspectCertificateDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tls_inspect_certificate_download_url(
        self,
        request: main_models.GetTlsInspectCertificateDownloadUrlRequest,
    ) -> main_models.GetTlsInspectCertificateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.get_tls_inspect_certificate_download_url_with_options(request, runtime)

    async def get_tls_inspect_certificate_download_url_async(
        self,
        request: main_models.GetTlsInspectCertificateDownloadUrlRequest,
    ) -> main_models.GetTlsInspectCertificateDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_tls_inspect_certificate_download_url_with_options_async(request, runtime)

    def list_tls_inspect_cacertificates_with_options(
        self,
        request: main_models.ListTlsInspectCACertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTlsInspectCACertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_cert_id):
            query['CaCertId'] = request.ca_cert_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTlsInspectCACertificates',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTlsInspectCACertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tls_inspect_cacertificates_with_options_async(
        self,
        request: main_models.ListTlsInspectCACertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTlsInspectCACertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_cert_id):
            query['CaCertId'] = request.ca_cert_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTlsInspectCACertificates',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTlsInspectCACertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tls_inspect_cacertificates(
        self,
        request: main_models.ListTlsInspectCACertificatesRequest,
    ) -> main_models.ListTlsInspectCACertificatesResponse:
        runtime = RuntimeOptions()
        return self.list_tls_inspect_cacertificates_with_options(request, runtime)

    async def list_tls_inspect_cacertificates_async(
        self,
        request: main_models.ListTlsInspectCACertificatesRequest,
    ) -> main_models.ListTlsInspectCACertificatesResponse:
        runtime = RuntimeOptions()
        return await self.list_tls_inspect_cacertificates_with_options_async(request, runtime)

    def modify_address_book_with_options(
        self,
        request: main_models.ModifyAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ack_labels):
            query['AckLabels'] = request.ack_labels
        if not DaraCore.is_null(request.ack_namespaces):
            query['AckNamespaces'] = request.ack_namespaces
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        if not DaraCore.is_null(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAddressBookResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_address_book_with_options_async(
        self,
        request: main_models.ModifyAddressBookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAddressBookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ack_labels):
            query['AckLabels'] = request.ack_labels
        if not DaraCore.is_null(request.ack_namespaces):
            query['AckNamespaces'] = request.ack_namespaces
        if not DaraCore.is_null(request.address_list):
            query['AddressList'] = request.address_list
        if not DaraCore.is_null(request.auto_add_tag_ecs):
            query['AutoAddTagEcs'] = request.auto_add_tag_ecs
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_uuid):
            query['GroupUuid'] = request.group_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.tag_list):
            query['TagList'] = request.tag_list
        if not DaraCore.is_null(request.tag_relation):
            query['TagRelation'] = request.tag_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAddressBook',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAddressBookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_address_book(
        self,
        request: main_models.ModifyAddressBookRequest,
    ) -> main_models.ModifyAddressBookResponse:
        runtime = RuntimeOptions()
        return self.modify_address_book_with_options(request, runtime)

    async def modify_address_book_async(
        self,
        request: main_models.ModifyAddressBookRequest,
    ) -> main_models.ModifyAddressBookResponse:
        runtime = RuntimeOptions()
        return await self.modify_address_book_with_options_async(request, runtime)

    def modify_cfw_instance_with_options(
        self,
        request: main_models.ModifyCfwInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCfwInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.update_list):
            query['UpdateList'] = request.update_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCfwInstance',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCfwInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cfw_instance_with_options_async(
        self,
        request: main_models.ModifyCfwInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCfwInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.update_list):
            query['UpdateList'] = request.update_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCfwInstance',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCfwInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cfw_instance(
        self,
        request: main_models.ModifyCfwInstanceRequest,
    ) -> main_models.ModifyCfwInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_cfw_instance_with_options(request, runtime)

    async def modify_cfw_instance_async(
        self,
        request: main_models.ModifyCfwInstanceRequest,
    ) -> main_models.ModifyCfwInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_cfw_instance_with_options_async(request, runtime)

    def modify_control_policy_with_options(
        self,
        request: main_models.ModifyControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_control_policy_with_options_async(
        self,
        request: main_models.ModifyControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_control_policy(
        self,
        request: main_models.ModifyControlPolicyRequest,
    ) -> main_models.ModifyControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_control_policy_with_options(request, runtime)

    async def modify_control_policy_async(
        self,
        request: main_models.ModifyControlPolicyRequest,
    ) -> main_models.ModifyControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_control_policy_with_options_async(request, runtime)

    def modify_control_policy_position_with_options(
        self,
        request: main_models.ModifyControlPolicyPositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlPolicyPositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.old_order):
            query['OldOrder'] = request.old_order
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlPolicyPosition',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlPolicyPositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_control_policy_position_with_options_async(
        self,
        request: main_models.ModifyControlPolicyPositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlPolicyPositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.old_order):
            query['OldOrder'] = request.old_order
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlPolicyPosition',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlPolicyPositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_control_policy_position(
        self,
        request: main_models.ModifyControlPolicyPositionRequest,
    ) -> main_models.ModifyControlPolicyPositionResponse:
        runtime = RuntimeOptions()
        return self.modify_control_policy_position_with_options(request, runtime)

    async def modify_control_policy_position_async(
        self,
        request: main_models.ModifyControlPolicyPositionRequest,
    ) -> main_models.ModifyControlPolicyPositionResponse:
        runtime = RuntimeOptions()
        return await self.modify_control_policy_position_with_options_async(request, runtime)

    def modify_control_policy_priority_with_options(
        self,
        request: main_models.ModifyControlPolicyPriorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlPolicyPriorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlPolicyPriority',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlPolicyPriorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_control_policy_priority_with_options_async(
        self,
        request: main_models.ModifyControlPolicyPriorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyControlPolicyPriorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyControlPolicyPriority',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyControlPolicyPriorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_control_policy_priority(
        self,
        request: main_models.ModifyControlPolicyPriorityRequest,
    ) -> main_models.ModifyControlPolicyPriorityResponse:
        runtime = RuntimeOptions()
        return self.modify_control_policy_priority_with_options(request, runtime)

    async def modify_control_policy_priority_async(
        self,
        request: main_models.ModifyControlPolicyPriorityRequest,
    ) -> main_models.ModifyControlPolicyPriorityResponse:
        runtime = RuntimeOptions()
        return await self.modify_control_policy_priority_with_options_async(request, runtime)

    def modify_default_ipsconfig_with_options(
        self,
        request: main_models.ModifyDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not DaraCore.is_null(request.cti_rules):
            query['CtiRules'] = request.cti_rules
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_sdl):
            query['MaxSdl'] = request.max_sdl
        if not DaraCore.is_null(request.patch_rules):
            query['PatchRules'] = request.patch_rules
        if not DaraCore.is_null(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_default_ipsconfig_with_options_async(
        self,
        request: main_models.ModifyDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not DaraCore.is_null(request.cti_rules):
            query['CtiRules'] = request.cti_rules
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_sdl):
            query['MaxSdl'] = request.max_sdl
        if not DaraCore.is_null(request.patch_rules):
            query['PatchRules'] = request.patch_rules
        if not DaraCore.is_null(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_default_ipsconfig(
        self,
        request: main_models.ModifyDefaultIPSConfigRequest,
    ) -> main_models.ModifyDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_default_ipsconfig_with_options(request, runtime)

    async def modify_default_ipsconfig_async(
        self,
        request: main_models.ModifyDefaultIPSConfigRequest,
    ) -> main_models.ModifyDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_default_ipsconfig_with_options_async(request, runtime)

    def modify_dns_firewall_policy_with_options(
        self,
        request: main_models.ModifyDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDnsFirewallPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dns_firewall_policy_with_options_async(
        self,
        request: main_models.ModifyDnsFirewallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDnsFirewallPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDnsFirewallPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDnsFirewallPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dns_firewall_policy(
        self,
        request: main_models.ModifyDnsFirewallPolicyRequest,
    ) -> main_models.ModifyDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_dns_firewall_policy_with_options(request, runtime)

    async def modify_dns_firewall_policy_async(
        self,
        request: main_models.ModifyDnsFirewallPolicyRequest,
    ) -> main_models.ModifyDnsFirewallPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_dns_firewall_policy_with_options_async(request, runtime)

    def modify_firewall_v2route_policy_switch_with_options(
        self,
        request: main_models.ModifyFirewallV2RoutePolicySwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirewallV2RoutePolicySwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.should_recover):
            query['ShouldRecover'] = request.should_recover
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        if not DaraCore.is_null(request.tr_firewall_route_policy_switch_status):
            query['TrFirewallRoutePolicySwitchStatus'] = request.tr_firewall_route_policy_switch_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirewallV2RoutePolicySwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirewallV2RoutePolicySwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_firewall_v2route_policy_switch_with_options_async(
        self,
        request: main_models.ModifyFirewallV2RoutePolicySwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFirewallV2RoutePolicySwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.should_recover):
            query['ShouldRecover'] = request.should_recover
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        if not DaraCore.is_null(request.tr_firewall_route_policy_switch_status):
            query['TrFirewallRoutePolicySwitchStatus'] = request.tr_firewall_route_policy_switch_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFirewallV2RoutePolicySwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFirewallV2RoutePolicySwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_firewall_v2route_policy_switch(
        self,
        request: main_models.ModifyFirewallV2RoutePolicySwitchRequest,
    ) -> main_models.ModifyFirewallV2RoutePolicySwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_firewall_v2route_policy_switch_with_options(request, runtime)

    async def modify_firewall_v2route_policy_switch_async(
        self,
        request: main_models.ModifyFirewallV2RoutePolicySwitchRequest,
    ) -> main_models.ModifyFirewallV2RoutePolicySwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_firewall_v2route_policy_switch_with_options_async(request, runtime)

    def modify_instance_member_attributes_with_options(
        self,
        request: main_models.ModifyInstanceMemberAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceMemberAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceMemberAttributes',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceMemberAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_member_attributes_with_options_async(
        self,
        request: main_models.ModifyInstanceMemberAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceMemberAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.members):
            query['Members'] = request.members
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceMemberAttributes',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceMemberAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_member_attributes(
        self,
        request: main_models.ModifyInstanceMemberAttributesRequest,
    ) -> main_models.ModifyInstanceMemberAttributesResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_member_attributes_with_options(request, runtime)

    async def modify_instance_member_attributes_async(
        self,
        request: main_models.ModifyInstanceMemberAttributesRequest,
    ) -> main_models.ModifyInstanceMemberAttributesResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_member_attributes_with_options_async(request, runtime)

    def modify_ips_rules_with_options(
        self,
        request: main_models.ModifyIpsRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpsRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpsRules',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpsRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ips_rules_with_options_async(
        self,
        request: main_models.ModifyIpsRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpsRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_action):
            query['RuleAction'] = request.rule_action
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpsRules',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpsRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ips_rules(
        self,
        request: main_models.ModifyIpsRulesRequest,
    ) -> main_models.ModifyIpsRulesResponse:
        runtime = RuntimeOptions()
        return self.modify_ips_rules_with_options(request, runtime)

    async def modify_ips_rules_async(
        self,
        request: main_models.ModifyIpsRulesRequest,
    ) -> main_models.ModifyIpsRulesResponse:
        runtime = RuntimeOptions()
        return await self.modify_ips_rules_with_options_async(request, runtime)

    def modify_ips_rules_to_default_with_options(
        self,
        request: main_models.ModifyIpsRulesToDefaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpsRulesToDefaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpsRulesToDefault',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpsRulesToDefaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ips_rules_to_default_with_options_async(
        self,
        request: main_models.ModifyIpsRulesToDefaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpsRulesToDefaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attack_app):
            query['AttackApp'] = request.attack_app
        if not DaraCore.is_null(request.firewall_type):
            query['FirewallType'] = request.firewall_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpsRulesToDefault',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpsRulesToDefaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ips_rules_to_default(
        self,
        request: main_models.ModifyIpsRulesToDefaultRequest,
    ) -> main_models.ModifyIpsRulesToDefaultResponse:
        runtime = RuntimeOptions()
        return self.modify_ips_rules_to_default_with_options(request, runtime)

    async def modify_ips_rules_to_default_async(
        self,
        request: main_models.ModifyIpsRulesToDefaultRequest,
    ) -> main_models.ModifyIpsRulesToDefaultResponse:
        runtime = RuntimeOptions()
        return await self.modify_ips_rules_to_default_with_options_async(request, runtime)

    def modify_nat_firewall_control_policy_with_options(
        self,
        request: main_models.ModifyNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNatFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_nat_firewall_control_policy_with_options_async(
        self,
        request: main_models.ModifyNatFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNatFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNatFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNatFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_nat_firewall_control_policy(
        self,
        request: main_models.ModifyNatFirewallControlPolicyRequest,
    ) -> main_models.ModifyNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_nat_firewall_control_policy_with_options(request, runtime)

    async def modify_nat_firewall_control_policy_async(
        self,
        request: main_models.ModifyNatFirewallControlPolicyRequest,
    ) -> main_models.ModifyNatFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_nat_firewall_control_policy_with_options_async(request, runtime)

    def modify_nat_firewall_control_policy_position_with_options(
        self,
        request: main_models.ModifyNatFirewallControlPolicyPositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNatFirewallControlPolicyPositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNatFirewallControlPolicyPosition',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNatFirewallControlPolicyPositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_nat_firewall_control_policy_position_with_options_async(
        self,
        request: main_models.ModifyNatFirewallControlPolicyPositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNatFirewallControlPolicyPositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNatFirewallControlPolicyPosition',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNatFirewallControlPolicyPositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_nat_firewall_control_policy_position(
        self,
        request: main_models.ModifyNatFirewallControlPolicyPositionRequest,
    ) -> main_models.ModifyNatFirewallControlPolicyPositionResponse:
        runtime = RuntimeOptions()
        return self.modify_nat_firewall_control_policy_position_with_options(request, runtime)

    async def modify_nat_firewall_control_policy_position_async(
        self,
        request: main_models.ModifyNatFirewallControlPolicyPositionRequest,
    ) -> main_models.ModifyNatFirewallControlPolicyPositionResponse:
        runtime = RuntimeOptions()
        return await self.modify_nat_firewall_control_policy_position_with_options_async(request, runtime)

    def modify_object_group_operation_with_options(
        self,
        request: main_models.ModifyObjectGroupOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyObjectGroupOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_list):
            query['ObjectList'] = request.object_list
        if not DaraCore.is_null(request.object_operation):
            query['ObjectOperation'] = request.object_operation
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyObjectGroupOperation',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyObjectGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_object_group_operation_with_options_async(
        self,
        request: main_models.ModifyObjectGroupOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyObjectGroupOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_list):
            query['ObjectList'] = request.object_list
        if not DaraCore.is_null(request.object_operation):
            query['ObjectOperation'] = request.object_operation
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyObjectGroupOperation',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyObjectGroupOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_object_group_operation(
        self,
        request: main_models.ModifyObjectGroupOperationRequest,
    ) -> main_models.ModifyObjectGroupOperationResponse:
        runtime = RuntimeOptions()
        return self.modify_object_group_operation_with_options(request, runtime)

    async def modify_object_group_operation_async(
        self,
        request: main_models.ModifyObjectGroupOperationRequest,
    ) -> main_models.ModifyObjectGroupOperationResponse:
        runtime = RuntimeOptions()
        return await self.modify_object_group_operation_with_options_async(request, runtime)

    def modify_policy_advanced_config_with_options(
        self,
        request: main_models.ModifyPolicyAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eips):
            query['Eips'] = request.eips
        if not DaraCore.is_null(request.internet_switch):
            query['InternetSwitch'] = request.internet_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyAdvancedConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyAdvancedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_advanced_config_with_options_async(
        self,
        request: main_models.ModifyPolicyAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.eips):
            query['Eips'] = request.eips
        if not DaraCore.is_null(request.internet_switch):
            query['InternetSwitch'] = request.internet_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyAdvancedConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyAdvancedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_advanced_config(
        self,
        request: main_models.ModifyPolicyAdvancedConfigRequest,
    ) -> main_models.ModifyPolicyAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_policy_advanced_config_with_options(request, runtime)

    async def modify_policy_advanced_config_async(
        self,
        request: main_models.ModifyPolicyAdvancedConfigRequest,
    ) -> main_models.ModifyPolicyAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_policy_advanced_config_with_options_async(request, runtime)

    def modify_private_dns_endpoint_with_options(
        self,
        request: main_models.ModifyPrivateDnsEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPrivateDnsEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.access_instance_name):
            query['AccessInstanceName'] = request.access_instance_name
        if not DaraCore.is_null(request.primary_dns):
            query['PrimaryDns'] = request.primary_dns
        if not DaraCore.is_null(request.private_dns_type):
            query['PrivateDnsType'] = request.private_dns_type
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.standby_dns):
            query['StandbyDns'] = request.standby_dns
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPrivateDnsEndpoint',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPrivateDnsEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_private_dns_endpoint_with_options_async(
        self,
        request: main_models.ModifyPrivateDnsEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPrivateDnsEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_instance_id):
            query['AccessInstanceId'] = request.access_instance_id
        if not DaraCore.is_null(request.access_instance_name):
            query['AccessInstanceName'] = request.access_instance_name
        if not DaraCore.is_null(request.primary_dns):
            query['PrimaryDns'] = request.primary_dns
        if not DaraCore.is_null(request.private_dns_type):
            query['PrivateDnsType'] = request.private_dns_type
        if not DaraCore.is_null(request.region_no):
            query['RegionNo'] = request.region_no
        if not DaraCore.is_null(request.standby_dns):
            query['StandbyDns'] = request.standby_dns
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPrivateDnsEndpoint',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPrivateDnsEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_private_dns_endpoint(
        self,
        request: main_models.ModifyPrivateDnsEndpointRequest,
    ) -> main_models.ModifyPrivateDnsEndpointResponse:
        runtime = RuntimeOptions()
        return self.modify_private_dns_endpoint_with_options(request, runtime)

    async def modify_private_dns_endpoint_async(
        self,
        request: main_models.ModifyPrivateDnsEndpointRequest,
    ) -> main_models.ModifyPrivateDnsEndpointResponse:
        runtime = RuntimeOptions()
        return await self.modify_private_dns_endpoint_with_options_async(request, runtime)

    def modify_resource_type_auto_enable_with_options(
        self,
        request: main_models.ModifyResourceTypeAutoEnableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceTypeAutoEnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_type_auto_enable):
            query['ResourceTypeAutoEnable'] = request.resource_type_auto_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceTypeAutoEnable',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceTypeAutoEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_type_auto_enable_with_options_async(
        self,
        request: main_models.ModifyResourceTypeAutoEnableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceTypeAutoEnableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.resource_type_auto_enable):
            query['ResourceTypeAutoEnable'] = request.resource_type_auto_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceTypeAutoEnable',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceTypeAutoEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_type_auto_enable(
        self,
        request: main_models.ModifyResourceTypeAutoEnableRequest,
    ) -> main_models.ModifyResourceTypeAutoEnableResponse:
        runtime = RuntimeOptions()
        return self.modify_resource_type_auto_enable_with_options(request, runtime)

    async def modify_resource_type_auto_enable_async(
        self,
        request: main_models.ModifyResourceTypeAutoEnableRequest,
    ) -> main_models.ModifyResourceTypeAutoEnableResponse:
        runtime = RuntimeOptions()
        return await self.modify_resource_type_auto_enable_with_options_async(request, runtime)

    def modify_sensitive_switch_with_options(
        self,
        request: main_models.ModifySensitiveSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySensitiveSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sensitive_category):
            query['SensitiveCategory'] = request.sensitive_category
        if not DaraCore.is_null(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySensitiveSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySensitiveSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sensitive_switch_with_options_async(
        self,
        request: main_models.ModifySensitiveSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySensitiveSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sensitive_category):
            query['SensitiveCategory'] = request.sensitive_category
        if not DaraCore.is_null(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySensitiveSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySensitiveSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sensitive_switch(
        self,
        request: main_models.ModifySensitiveSwitchRequest,
    ) -> main_models.ModifySensitiveSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_sensitive_switch_with_options(request, runtime)

    async def modify_sensitive_switch_async(
        self,
        request: main_models.ModifySensitiveSwitchRequest,
    ) -> main_models.ModifySensitiveSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_sensitive_switch_with_options_async(request, runtime)

    def modify_sls_dispatch_status_with_options(
        self,
        request: main_models.ModifySlsDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySlsDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dispatch_value):
            query['DispatchValue'] = request.dispatch_value
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.filter_keys):
            query['FilterKeys'] = request.filter_keys
        if not DaraCore.is_null(request.new_region_id):
            query['NewRegionId'] = request.new_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySlsDispatchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySlsDispatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_sls_dispatch_status_with_options_async(
        self,
        request: main_models.ModifySlsDispatchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySlsDispatchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dispatch_value):
            query['DispatchValue'] = request.dispatch_value
        if not DaraCore.is_null(request.enable_status):
            query['EnableStatus'] = request.enable_status
        if not DaraCore.is_null(request.filter_keys):
            query['FilterKeys'] = request.filter_keys
        if not DaraCore.is_null(request.new_region_id):
            query['NewRegionId'] = request.new_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySlsDispatchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySlsDispatchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_sls_dispatch_status(
        self,
        request: main_models.ModifySlsDispatchStatusRequest,
    ) -> main_models.ModifySlsDispatchStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_sls_dispatch_status_with_options(request, runtime)

    async def modify_sls_dispatch_status_async(
        self,
        request: main_models.ModifySlsDispatchStatusRequest,
    ) -> main_models.ModifySlsDispatchStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_sls_dispatch_status_with_options_async(request, runtime)

    def modify_threat_intelligence_switch_with_options(
        self,
        request: main_models.ModifyThreatIntelligenceSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyThreatIntelligenceSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_list):
            query['CategoryList'] = request.category_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyThreatIntelligenceSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyThreatIntelligenceSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_threat_intelligence_switch_with_options_async(
        self,
        request: main_models.ModifyThreatIntelligenceSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyThreatIntelligenceSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_list):
            query['CategoryList'] = request.category_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyThreatIntelligenceSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyThreatIntelligenceSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_threat_intelligence_switch(
        self,
        request: main_models.ModifyThreatIntelligenceSwitchRequest,
    ) -> main_models.ModifyThreatIntelligenceSwitchResponse:
        runtime = RuntimeOptions()
        return self.modify_threat_intelligence_switch_with_options(request, runtime)

    async def modify_threat_intelligence_switch_async(
        self,
        request: main_models.ModifyThreatIntelligenceSwitchRequest,
    ) -> main_models.ModifyThreatIntelligenceSwitchResponse:
        runtime = RuntimeOptions()
        return await self.modify_threat_intelligence_switch_with_options_async(request, runtime)

    def modify_tr_firewall_v2configuration_with_options(
        self,
        request: main_models.ModifyTrFirewallV2ConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrFirewallV2ConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrFirewallV2Configuration',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrFirewallV2ConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tr_firewall_v2configuration_with_options_async(
        self,
        request: main_models.ModifyTrFirewallV2ConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrFirewallV2ConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.firewall_name):
            query['FirewallName'] = request.firewall_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrFirewallV2Configuration',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrFirewallV2ConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tr_firewall_v2configuration(
        self,
        request: main_models.ModifyTrFirewallV2ConfigurationRequest,
    ) -> main_models.ModifyTrFirewallV2ConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_tr_firewall_v2configuration_with_options(request, runtime)

    async def modify_tr_firewall_v2configuration_async(
        self,
        request: main_models.ModifyTrFirewallV2ConfigurationRequest,
    ) -> main_models.ModifyTrFirewallV2ConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_tr_firewall_v2configuration_with_options_async(request, runtime)

    def modify_tr_firewall_v2route_policy_scope_with_options(
        self,
        tmp_req: main_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        tmp_req.validate()
        request = main_models.ModifyTrFirewallV2RoutePolicyScopeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not DaraCore.is_null(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not DaraCore.is_null(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.should_recover):
            query['ShouldRecover'] = request.should_recover
        if not DaraCore.is_null(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrFirewallV2RoutePolicyScope',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrFirewallV2RoutePolicyScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_tr_firewall_v2route_policy_scope_with_options_async(
        self,
        tmp_req: main_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        tmp_req.validate()
        request = main_models.ModifyTrFirewallV2RoutePolicyScopeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_candidate_list):
            request.dest_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_candidate_list, 'DestCandidateList', 'json')
        if not DaraCore.is_null(tmp_req.src_candidate_list):
            request.src_candidate_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.src_candidate_list, 'SrcCandidateList', 'json')
        query = {}
        if not DaraCore.is_null(request.dest_candidate_list_shrink):
            query['DestCandidateList'] = request.dest_candidate_list_shrink
        if not DaraCore.is_null(request.firewall_id):
            query['FirewallId'] = request.firewall_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.should_recover):
            query['ShouldRecover'] = request.should_recover
        if not DaraCore.is_null(request.src_candidate_list_shrink):
            query['SrcCandidateList'] = request.src_candidate_list_shrink
        if not DaraCore.is_null(request.tr_firewall_route_policy_id):
            query['TrFirewallRoutePolicyId'] = request.tr_firewall_route_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTrFirewallV2RoutePolicyScope',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTrFirewallV2RoutePolicyScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_tr_firewall_v2route_policy_scope(
        self,
        request: main_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
    ) -> main_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        runtime = RuntimeOptions()
        return self.modify_tr_firewall_v2route_policy_scope_with_options(request, runtime)

    async def modify_tr_firewall_v2route_policy_scope_async(
        self,
        request: main_models.ModifyTrFirewallV2RoutePolicyScopeRequest,
    ) -> main_models.ModifyTrFirewallV2RoutePolicyScopeResponse:
        runtime = RuntimeOptions()
        return await self.modify_tr_firewall_v2route_policy_scope_with_options_async(request, runtime)

    def modify_user_alarm_config_with_options(
        self,
        request: main_models.ModifyUserAlarmConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserAlarmConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_config):
            query['AlarmConfig'] = request.alarm_config
        if not DaraCore.is_null(request.alarm_lang):
            query['AlarmLang'] = request.alarm_lang
        if not DaraCore.is_null(request.contact_config):
            query['ContactConfig'] = request.contact_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.use_default_contact):
            query['UseDefaultContact'] = request.use_default_contact
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserAlarmConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserAlarmConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_alarm_config_with_options_async(
        self,
        request: main_models.ModifyUserAlarmConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserAlarmConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_config):
            query['AlarmConfig'] = request.alarm_config
        if not DaraCore.is_null(request.alarm_lang):
            query['AlarmLang'] = request.alarm_lang
        if not DaraCore.is_null(request.contact_config):
            query['ContactConfig'] = request.contact_config
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.use_default_contact):
            query['UseDefaultContact'] = request.use_default_contact
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserAlarmConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserAlarmConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_alarm_config(
        self,
        request: main_models.ModifyUserAlarmConfigRequest,
    ) -> main_models.ModifyUserAlarmConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_user_alarm_config_with_options(request, runtime)

    async def modify_user_alarm_config_async(
        self,
        request: main_models.ModifyUserAlarmConfigRequest,
    ) -> main_models.ModifyUserAlarmConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_alarm_config_with_options_async(request, runtime)

    def modify_user_ipswhitelist_with_options(
        self,
        request: main_models.ModifyUserIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.list_type):
            query['ListType'] = request.list_type
        if not DaraCore.is_null(request.list_value):
            query['ListValue'] = request.list_value
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_ipswhitelist_with_options_async(
        self,
        request: main_models.ModifyUserIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.list_type):
            query['ListType'] = request.list_type
        if not DaraCore.is_null(request.list_value):
            query['ListValue'] = request.list_value
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_ipswhitelist(
        self,
        request: main_models.ModifyUserIPSWhitelistRequest,
    ) -> main_models.ModifyUserIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return self.modify_user_ipswhitelist_with_options(request, runtime)

    async def modify_user_ipswhitelist_async(
        self,
        request: main_models.ModifyUserIPSWhitelistRequest,
    ) -> main_models.ModifyUserIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_ipswhitelist_with_options_async(request, runtime)

    def modify_user_sls_log_storage_time_with_options(
        self,
        request: main_models.ModifyUserSlsLogStorageTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserSlsLogStorageTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.storage_time):
            query['StorageTime'] = request.storage_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserSlsLogStorageTime',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserSlsLogStorageTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_sls_log_storage_time_with_options_async(
        self,
        request: main_models.ModifyUserSlsLogStorageTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserSlsLogStorageTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.storage_time):
            query['StorageTime'] = request.storage_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUserSlsLogStorageTime',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserSlsLogStorageTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_sls_log_storage_time(
        self,
        request: main_models.ModifyUserSlsLogStorageTimeRequest,
    ) -> main_models.ModifyUserSlsLogStorageTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_user_sls_log_storage_time_with_options(request, runtime)

    async def modify_user_sls_log_storage_time_async(
        self,
        request: main_models.ModifyUserSlsLogStorageTimeRequest,
    ) -> main_models.ModifyUserSlsLogStorageTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_sls_log_storage_time_with_options_async(request, runtime)

    def modify_vpc_firewall_acl_engine_mode_with_options(
        self,
        request: main_models.ModifyVpcFirewallAclEngineModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallAclEngineModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallAclEngineMode',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallAclEngineModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_acl_engine_mode_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallAclEngineModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallAclEngineModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallAclEngineMode',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallAclEngineModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_acl_engine_mode(
        self,
        request: main_models.ModifyVpcFirewallAclEngineModeRequest,
    ) -> main_models.ModifyVpcFirewallAclEngineModeResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_acl_engine_mode_with_options(request, runtime)

    async def modify_vpc_firewall_acl_engine_mode_async(
        self,
        request: main_models.ModifyVpcFirewallAclEngineModeRequest,
    ) -> main_models.ModifyVpcFirewallAclEngineModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_acl_engine_mode_with_options_async(request, runtime)

    def modify_vpc_firewall_cen_configure_with_options(
        self,
        request: main_models.ModifyVpcFirewallCenConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallCenConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallCenConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallCenConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_cen_configure_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallCenConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallCenConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallCenConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallCenConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_cen_configure(
        self,
        request: main_models.ModifyVpcFirewallCenConfigureRequest,
    ) -> main_models.ModifyVpcFirewallCenConfigureResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_cen_configure_with_options(request, runtime)

    async def modify_vpc_firewall_cen_configure_async(
        self,
        request: main_models.ModifyVpcFirewallCenConfigureRequest,
    ) -> main_models.ModifyVpcFirewallCenConfigureResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_cen_configure_with_options_async(request, runtime)

    def modify_vpc_firewall_cen_switch_status_with_options(
        self,
        request: main_models.ModifyVpcFirewallCenSwitchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallCenSwitchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallCenSwitchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallCenSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_cen_switch_status_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallCenSwitchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallCenSwitchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallCenSwitchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallCenSwitchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_cen_switch_status(
        self,
        request: main_models.ModifyVpcFirewallCenSwitchStatusRequest,
    ) -> main_models.ModifyVpcFirewallCenSwitchStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_cen_switch_status_with_options(request, runtime)

    async def modify_vpc_firewall_cen_switch_status_async(
        self,
        request: main_models.ModifyVpcFirewallCenSwitchStatusRequest,
    ) -> main_models.ModifyVpcFirewallCenSwitchStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_cen_switch_status_with_options_async(request, runtime)

    def modify_vpc_firewall_configure_with_options(
        self,
        request: main_models.ModifyVpcFirewallConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallConfigureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_configure_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallConfigureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallConfigureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.local_vpc_cidr_table_list):
            query['LocalVpcCidrTableList'] = request.local_vpc_cidr_table_list
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.peer_vpc_cidr_table_list):
            query['PeerVpcCidrTableList'] = request.peer_vpc_cidr_table_list
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.vpc_firewall_name):
            query['VpcFirewallName'] = request.vpc_firewall_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallConfigure',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallConfigureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_configure(
        self,
        request: main_models.ModifyVpcFirewallConfigureRequest,
    ) -> main_models.ModifyVpcFirewallConfigureResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_configure_with_options(request, runtime)

    async def modify_vpc_firewall_configure_async(
        self,
        request: main_models.ModifyVpcFirewallConfigureRequest,
    ) -> main_models.ModifyVpcFirewallConfigureResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_configure_with_options_async(request, runtime)

    def modify_vpc_firewall_control_policy_with_options(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_control_policy_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallControlPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_action):
            query['AclAction'] = request.acl_action
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_name_list):
            query['ApplicationNameList'] = request.application_name_list
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dest_port):
            query['DestPort'] = request.dest_port
        if not DaraCore.is_null(request.dest_port_group):
            query['DestPortGroup'] = request.dest_port_group
        if not DaraCore.is_null(request.dest_port_type):
            query['DestPortType'] = request.dest_port_type
        if not DaraCore.is_null(request.destination):
            query['Destination'] = request.destination
        if not DaraCore.is_null(request.destination_type):
            query['DestinationType'] = request.destination_type
        if not DaraCore.is_null(request.domain_resolve_type):
            query['DomainResolveType'] = request.domain_resolve_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proto):
            query['Proto'] = request.proto
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repeat_days):
            query['RepeatDays'] = request.repeat_days
        if not DaraCore.is_null(request.repeat_end_time):
            query['RepeatEndTime'] = request.repeat_end_time
        if not DaraCore.is_null(request.repeat_start_time):
            query['RepeatStartTime'] = request.repeat_start_time
        if not DaraCore.is_null(request.repeat_type):
            query['RepeatType'] = request.repeat_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallControlPolicy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_control_policy(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyRequest,
    ) -> main_models.ModifyVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_control_policy_with_options(request, runtime)

    async def modify_vpc_firewall_control_policy_async(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyRequest,
    ) -> main_models.ModifyVpcFirewallControlPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_control_policy_with_options_async(request, runtime)

    def modify_vpc_firewall_control_policy_position_with_options(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyPositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallControlPolicyPositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.old_order):
            query['OldOrder'] = request.old_order
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallControlPolicyPosition',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallControlPolicyPositionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_control_policy_position_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyPositionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallControlPolicyPositionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.new_order):
            query['NewOrder'] = request.new_order
        if not DaraCore.is_null(request.old_order):
            query['OldOrder'] = request.old_order
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallControlPolicyPosition',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallControlPolicyPositionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_control_policy_position(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyPositionRequest,
    ) -> main_models.ModifyVpcFirewallControlPolicyPositionResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_control_policy_position_with_options(request, runtime)

    async def modify_vpc_firewall_control_policy_position_async(
        self,
        request: main_models.ModifyVpcFirewallControlPolicyPositionRequest,
    ) -> main_models.ModifyVpcFirewallControlPolicyPositionResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_control_policy_position_with_options_async(request, runtime)

    def modify_vpc_firewall_default_ipsconfig_with_options(
        self,
        request: main_models.ModifyVpcFirewallDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not DaraCore.is_null(request.enable_all_patch):
            query['EnableAllPatch'] = request.enable_all_patch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallDefaultIPSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_default_ipsconfig_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallDefaultIPSConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.basic_rules):
            query['BasicRules'] = request.basic_rules
        if not DaraCore.is_null(request.enable_all_patch):
            query['EnableAllPatch'] = request.enable_all_patch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.rule_class):
            query['RuleClass'] = request.rule_class
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallDefaultIPSConfig',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallDefaultIPSConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_default_ipsconfig(
        self,
        request: main_models.ModifyVpcFirewallDefaultIPSConfigRequest,
    ) -> main_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_default_ipsconfig_with_options(request, runtime)

    async def modify_vpc_firewall_default_ipsconfig_async(
        self,
        request: main_models.ModifyVpcFirewallDefaultIPSConfigRequest,
    ) -> main_models.ModifyVpcFirewallDefaultIPSConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_default_ipsconfig_with_options_async(request, runtime)

    def modify_vpc_firewall_ipswhitelist_with_options(
        self,
        request: main_models.ModifyVpcFirewallIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.list_type):
            query['ListType'] = request.list_type
        if not DaraCore.is_null(request.list_value):
            query['ListValue'] = request.list_value
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallIPSWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_ipswhitelist_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallIPSWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallIPSWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.list_type):
            query['ListType'] = request.list_type
        if not DaraCore.is_null(request.list_value):
            query['ListValue'] = request.list_value
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        if not DaraCore.is_null(request.white_type):
            query['WhiteType'] = request.white_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallIPSWhitelist',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallIPSWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_ipswhitelist(
        self,
        request: main_models.ModifyVpcFirewallIPSWhitelistRequest,
    ) -> main_models.ModifyVpcFirewallIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_ipswhitelist_with_options(request, runtime)

    async def modify_vpc_firewall_ipswhitelist_async(
        self,
        request: main_models.ModifyVpcFirewallIPSWhitelistRequest,
    ) -> main_models.ModifyVpcFirewallIPSWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_ipswhitelist_with_options_async(request, runtime)

    def modify_vpc_firewall_switch_status_with_options(
        self,
        request: main_models.ModifyVpcFirewallSwitchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallSwitchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallSwitchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vpc_firewall_switch_status_with_options_async(
        self,
        request: main_models.ModifyVpcFirewallSwitchStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVpcFirewallSwitchStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.firewall_switch):
            query['FirewallSwitch'] = request.firewall_switch
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.vpc_firewall_id):
            query['VpcFirewallId'] = request.vpc_firewall_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVpcFirewallSwitchStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVpcFirewallSwitchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vpc_firewall_switch_status(
        self,
        request: main_models.ModifyVpcFirewallSwitchStatusRequest,
    ) -> main_models.ModifyVpcFirewallSwitchStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_vpc_firewall_switch_status_with_options(request, runtime)

    async def modify_vpc_firewall_switch_status_async(
        self,
        request: main_models.ModifyVpcFirewallSwitchStatusRequest,
    ) -> main_models.ModifyVpcFirewallSwitchStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_vpc_firewall_switch_status_with_options_async(request, runtime)

    def put_disable_all_fw_switch_with_options(
        self,
        request: main_models.PutDisableAllFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDisableAllFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDisableAllFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDisableAllFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_disable_all_fw_switch_with_options_async(
        self,
        request: main_models.PutDisableAllFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDisableAllFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDisableAllFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDisableAllFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_disable_all_fw_switch(
        self,
        request: main_models.PutDisableAllFwSwitchRequest,
    ) -> main_models.PutDisableAllFwSwitchResponse:
        runtime = RuntimeOptions()
        return self.put_disable_all_fw_switch_with_options(request, runtime)

    async def put_disable_all_fw_switch_async(
        self,
        request: main_models.PutDisableAllFwSwitchRequest,
    ) -> main_models.PutDisableAllFwSwitchResponse:
        runtime = RuntimeOptions()
        return await self.put_disable_all_fw_switch_with_options_async(request, runtime)

    def put_disable_fw_switch_with_options(
        self,
        request: main_models.PutDisableFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDisableFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_list):
            query['RegionList'] = request.region_list
        if not DaraCore.is_null(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDisableFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDisableFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_disable_fw_switch_with_options_async(
        self,
        request: main_models.PutDisableFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutDisableFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_list):
            query['RegionList'] = request.region_list
        if not DaraCore.is_null(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutDisableFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutDisableFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_disable_fw_switch(
        self,
        request: main_models.PutDisableFwSwitchRequest,
    ) -> main_models.PutDisableFwSwitchResponse:
        runtime = RuntimeOptions()
        return self.put_disable_fw_switch_with_options(request, runtime)

    async def put_disable_fw_switch_async(
        self,
        request: main_models.PutDisableFwSwitchRequest,
    ) -> main_models.PutDisableFwSwitchResponse:
        runtime = RuntimeOptions()
        return await self.put_disable_fw_switch_with_options_async(request, runtime)

    def put_enable_all_fw_switch_with_options(
        self,
        request: main_models.PutEnableAllFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEnableAllFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEnableAllFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEnableAllFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_enable_all_fw_switch_with_options_async(
        self,
        request: main_models.PutEnableAllFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEnableAllFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEnableAllFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEnableAllFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_enable_all_fw_switch(
        self,
        request: main_models.PutEnableAllFwSwitchRequest,
    ) -> main_models.PutEnableAllFwSwitchResponse:
        runtime = RuntimeOptions()
        return self.put_enable_all_fw_switch_with_options(request, runtime)

    async def put_enable_all_fw_switch_async(
        self,
        request: main_models.PutEnableAllFwSwitchRequest,
    ) -> main_models.PutEnableAllFwSwitchResponse:
        runtime = RuntimeOptions()
        return await self.put_enable_all_fw_switch_with_options_async(request, runtime)

    def put_enable_fw_switch_with_options(
        self,
        request: main_models.PutEnableFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEnableFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_list):
            query['RegionList'] = request.region_list
        if not DaraCore.is_null(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEnableFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEnableFwSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_enable_fw_switch_with_options_async(
        self,
        request: main_models.PutEnableFwSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEnableFwSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ipaddr_list):
            query['IpaddrList'] = request.ipaddr_list
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_list):
            query['RegionList'] = request.region_list
        if not DaraCore.is_null(request.resource_type_list):
            query['ResourceTypeList'] = request.resource_type_list
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEnableFwSwitch',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEnableFwSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_enable_fw_switch(
        self,
        request: main_models.PutEnableFwSwitchRequest,
    ) -> main_models.PutEnableFwSwitchResponse:
        runtime = RuntimeOptions()
        return self.put_enable_fw_switch_with_options(request, runtime)

    async def put_enable_fw_switch_async(
        self,
        request: main_models.PutEnableFwSwitchRequest,
    ) -> main_models.PutEnableFwSwitchResponse:
        runtime = RuntimeOptions()
        return await self.put_enable_fw_switch_with_options_async(request, runtime)

    def release_expired_instance_with_options(
        self,
        request: main_models.ReleaseExpiredInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseExpiredInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseExpiredInstance',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseExpiredInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_expired_instance_with_options_async(
        self,
        request: main_models.ReleaseExpiredInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseExpiredInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseExpiredInstance',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseExpiredInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_expired_instance(
        self,
        request: main_models.ReleaseExpiredInstanceRequest,
    ) -> main_models.ReleaseExpiredInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_expired_instance_with_options(request, runtime)

    async def release_expired_instance_async(
        self,
        request: main_models.ReleaseExpiredInstanceRequest,
    ) -> main_models.ReleaseExpiredInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_expired_instance_with_options_async(request, runtime)

    def release_post_instance_with_options(
        self,
        request: main_models.ReleasePostInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleasePostInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleasePostInstance',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleasePostInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_post_instance_with_options_async(
        self,
        request: main_models.ReleasePostInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleasePostInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleasePostInstance',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleasePostInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_post_instance(
        self,
        request: main_models.ReleasePostInstanceRequest,
    ) -> main_models.ReleasePostInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_post_instance_with_options(request, runtime)

    async def release_post_instance_async(
        self,
        request: main_models.ReleasePostInstanceRequest,
    ) -> main_models.ReleasePostInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_post_instance_with_options_async(request, runtime)

    def reset_nat_firewall_rule_hit_count_with_options(
        self,
        request: main_models.ResetNatFirewallRuleHitCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetNatFirewallRuleHitCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetNatFirewallRuleHitCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetNatFirewallRuleHitCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_nat_firewall_rule_hit_count_with_options_async(
        self,
        request: main_models.ResetNatFirewallRuleHitCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetNatFirewallRuleHitCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetNatFirewallRuleHitCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetNatFirewallRuleHitCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_nat_firewall_rule_hit_count(
        self,
        request: main_models.ResetNatFirewallRuleHitCountRequest,
    ) -> main_models.ResetNatFirewallRuleHitCountResponse:
        runtime = RuntimeOptions()
        return self.reset_nat_firewall_rule_hit_count_with_options(request, runtime)

    async def reset_nat_firewall_rule_hit_count_async(
        self,
        request: main_models.ResetNatFirewallRuleHitCountRequest,
    ) -> main_models.ResetNatFirewallRuleHitCountResponse:
        runtime = RuntimeOptions()
        return await self.reset_nat_firewall_rule_hit_count_with_options_async(request, runtime)

    def reset_rule_hit_count_with_options(
        self,
        request: main_models.ResetRuleHitCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetRuleHitCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetRuleHitCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetRuleHitCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_rule_hit_count_with_options_async(
        self,
        request: main_models.ResetRuleHitCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetRuleHitCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetRuleHitCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetRuleHitCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_rule_hit_count(
        self,
        request: main_models.ResetRuleHitCountRequest,
    ) -> main_models.ResetRuleHitCountResponse:
        runtime = RuntimeOptions()
        return self.reset_rule_hit_count_with_options(request, runtime)

    async def reset_rule_hit_count_async(
        self,
        request: main_models.ResetRuleHitCountRequest,
    ) -> main_models.ResetRuleHitCountResponse:
        runtime = RuntimeOptions()
        return await self.reset_rule_hit_count_with_options_async(request, runtime)

    def reset_vpc_firewall_rule_hit_count_with_options(
        self,
        request: main_models.ResetVpcFirewallRuleHitCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetVpcFirewallRuleHitCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetVpcFirewallRuleHitCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetVpcFirewallRuleHitCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_vpc_firewall_rule_hit_count_with_options_async(
        self,
        request: main_models.ResetVpcFirewallRuleHitCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetVpcFirewallRuleHitCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_uuid):
            query['AclUuid'] = request.acl_uuid
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetVpcFirewallRuleHitCount',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetVpcFirewallRuleHitCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_vpc_firewall_rule_hit_count(
        self,
        request: main_models.ResetVpcFirewallRuleHitCountRequest,
    ) -> main_models.ResetVpcFirewallRuleHitCountResponse:
        runtime = RuntimeOptions()
        return self.reset_vpc_firewall_rule_hit_count_with_options(request, runtime)

    async def reset_vpc_firewall_rule_hit_count_async(
        self,
        request: main_models.ResetVpcFirewallRuleHitCountRequest,
    ) -> main_models.ResetVpcFirewallRuleHitCountResponse:
        runtime = RuntimeOptions()
        return await self.reset_vpc_firewall_rule_hit_count_with_options_async(request, runtime)

    def switch_security_proxy_with_options(
        self,
        request: main_models.SwitchSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.switch):
            query['Switch'] = request.switch
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_security_proxy_with_options_async(
        self,
        request: main_models.SwitchSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.switch):
            query['Switch'] = request.switch
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_security_proxy(
        self,
        request: main_models.SwitchSecurityProxyRequest,
    ) -> main_models.SwitchSecurityProxyResponse:
        runtime = RuntimeOptions()
        return self.switch_security_proxy_with_options(request, runtime)

    async def switch_security_proxy_async(
        self,
        request: main_models.SwitchSecurityProxyRequest,
    ) -> main_models.SwitchSecurityProxyResponse:
        runtime = RuntimeOptions()
        return await self.switch_security_proxy_with_options_async(request, runtime)

    def update_aitraffic_analysis_status_with_options(
        self,
        request: main_models.UpdateAITrafficAnalysisStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAITrafficAnalysisStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAITrafficAnalysisStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAITrafficAnalysisStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_aitraffic_analysis_status_with_options_async(
        self,
        request: main_models.UpdateAITrafficAnalysisStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAITrafficAnalysisStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAITrafficAnalysisStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAITrafficAnalysisStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_aitraffic_analysis_status(
        self,
        request: main_models.UpdateAITrafficAnalysisStatusRequest,
    ) -> main_models.UpdateAITrafficAnalysisStatusResponse:
        runtime = RuntimeOptions()
        return self.update_aitraffic_analysis_status_with_options(request, runtime)

    async def update_aitraffic_analysis_status_async(
        self,
        request: main_models.UpdateAITrafficAnalysisStatusRequest,
    ) -> main_models.UpdateAITrafficAnalysisStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_aitraffic_analysis_status_with_options_async(request, runtime)

    def update_ack_cluster_connector_with_options(
        self,
        request: main_models.UpdateAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_name):
            query['ConnectorName'] = request.connector_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAckClusterConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ack_cluster_connector_with_options_async(
        self,
        request: main_models.UpdateAckClusterConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAckClusterConnectorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.connector_name):
            query['ConnectorName'] = request.connector_name
        if not DaraCore.is_null(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAckClusterConnector',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAckClusterConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ack_cluster_connector(
        self,
        request: main_models.UpdateAckClusterConnectorRequest,
    ) -> main_models.UpdateAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return self.update_ack_cluster_connector_with_options(request, runtime)

    async def update_ack_cluster_connector_async(
        self,
        request: main_models.UpdateAckClusterConnectorRequest,
    ) -> main_models.UpdateAckClusterConnectorResponse:
        runtime = RuntimeOptions()
        return await self.update_ack_cluster_connector_with_options_async(request, runtime)

    def update_acl_check_detail_status_with_options(
        self,
        request: main_models.UpdateAclCheckDetailStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAclCheckDetailStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAclCheckDetailStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAclCheckDetailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_acl_check_detail_status_with_options_async(
        self,
        request: main_models.UpdateAclCheckDetailStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAclCheckDetailStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAclCheckDetailStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAclCheckDetailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_acl_check_detail_status(
        self,
        request: main_models.UpdateAclCheckDetailStatusRequest,
    ) -> main_models.UpdateAclCheckDetailStatusResponse:
        runtime = RuntimeOptions()
        return self.update_acl_check_detail_status_with_options(request, runtime)

    async def update_acl_check_detail_status_async(
        self,
        request: main_models.UpdateAclCheckDetailStatusRequest,
    ) -> main_models.UpdateAclCheckDetailStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_acl_check_detail_status_with_options_async(request, runtime)

    def update_postpay_user_internet_status_with_options(
        self,
        request: main_models.UpdatePostpayUserInternetStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostpayUserInternetStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostpayUserInternetStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostpayUserInternetStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_postpay_user_internet_status_with_options_async(
        self,
        request: main_models.UpdatePostpayUserInternetStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostpayUserInternetStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostpayUserInternetStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostpayUserInternetStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_postpay_user_internet_status(
        self,
        request: main_models.UpdatePostpayUserInternetStatusRequest,
    ) -> main_models.UpdatePostpayUserInternetStatusResponse:
        runtime = RuntimeOptions()
        return self.update_postpay_user_internet_status_with_options(request, runtime)

    async def update_postpay_user_internet_status_async(
        self,
        request: main_models.UpdatePostpayUserInternetStatusRequest,
    ) -> main_models.UpdatePostpayUserInternetStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_postpay_user_internet_status_with_options_async(request, runtime)

    def update_postpay_user_nat_status_with_options(
        self,
        request: main_models.UpdatePostpayUserNatStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostpayUserNatStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostpayUserNatStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostpayUserNatStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_postpay_user_nat_status_with_options_async(
        self,
        request: main_models.UpdatePostpayUserNatStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostpayUserNatStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostpayUserNatStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostpayUserNatStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_postpay_user_nat_status(
        self,
        request: main_models.UpdatePostpayUserNatStatusRequest,
    ) -> main_models.UpdatePostpayUserNatStatusResponse:
        runtime = RuntimeOptions()
        return self.update_postpay_user_nat_status_with_options(request, runtime)

    async def update_postpay_user_nat_status_async(
        self,
        request: main_models.UpdatePostpayUserNatStatusRequest,
    ) -> main_models.UpdatePostpayUserNatStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_postpay_user_nat_status_with_options_async(request, runtime)

    def update_postpay_user_vpc_status_with_options(
        self,
        request: main_models.UpdatePostpayUserVpcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostpayUserVpcStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostpayUserVpcStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostpayUserVpcStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_postpay_user_vpc_status_with_options_async(
        self,
        request: main_models.UpdatePostpayUserVpcStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePostpayUserVpcStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePostpayUserVpcStatus',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePostpayUserVpcStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_postpay_user_vpc_status(
        self,
        request: main_models.UpdatePostpayUserVpcStatusRequest,
    ) -> main_models.UpdatePostpayUserVpcStatusResponse:
        runtime = RuntimeOptions()
        return self.update_postpay_user_vpc_status_with_options(request, runtime)

    async def update_postpay_user_vpc_status_async(
        self,
        request: main_models.UpdatePostpayUserVpcStatusRequest,
    ) -> main_models.UpdatePostpayUserVpcStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_postpay_user_vpc_status_with_options_async(request, runtime)

    def update_security_proxy_with_options(
        self,
        request: main_models.UpdateSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_proxy_with_options_async(
        self,
        request: main_models.UpdateSecurityProxyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityProxyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not DaraCore.is_null(request.proxy_name):
            query['ProxyName'] = request.proxy_name
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityProxy',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_proxy(
        self,
        request: main_models.UpdateSecurityProxyRequest,
    ) -> main_models.UpdateSecurityProxyResponse:
        runtime = RuntimeOptions()
        return self.update_security_proxy_with_options(request, runtime)

    async def update_security_proxy_async(
        self,
        request: main_models.UpdateSecurityProxyRequest,
    ) -> main_models.UpdateSecurityProxyResponse:
        runtime = RuntimeOptions()
        return await self.update_security_proxy_with_options_async(request, runtime)

    def use_acl_backup_data_with_options(
        self,
        request: main_models.UseAclBackupDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UseAclBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_up_time):
            query['BackUpTime'] = request.back_up_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UseAclBackupData',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UseAclBackupDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def use_acl_backup_data_with_options_async(
        self,
        request: main_models.UseAclBackupDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UseAclBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_up_time):
            query['BackUpTime'] = request.back_up_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UseAclBackupData',
            version = '2017-12-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UseAclBackupDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def use_acl_backup_data(
        self,
        request: main_models.UseAclBackupDataRequest,
    ) -> main_models.UseAclBackupDataResponse:
        runtime = RuntimeOptions()
        return self.use_acl_backup_data_with_options(request, runtime)

    async def use_acl_backup_data_async(
        self,
        request: main_models.UseAclBackupDataRequest,
    ) -> main_models.UseAclBackupDataResponse:
        runtime = RuntimeOptions()
        return await self.use_acl_backup_data_with_options_async(request, runtime)
