# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ens20171110 import models as ens_20171110_models
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
        self._endpoint = self.get_endpoint('ens', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accosicate_network_acl_with_options(
        self,
        request: ens_20171110_models.AccosicateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AccosicateNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccosicateNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AccosicateNetworkAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def accosicate_network_acl_with_options_async(
        self,
        request: ens_20171110_models.AccosicateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AccosicateNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AccosicateNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AccosicateNetworkAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accosicate_network_acl(
        self,
        request: ens_20171110_models.AccosicateNetworkAclRequest,
    ) -> ens_20171110_models.AccosicateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.accosicate_network_acl_with_options(request, runtime)

    async def accosicate_network_acl_async(
        self,
        request: ens_20171110_models.AccosicateNetworkAclRequest,
    ) -> ens_20171110_models.AccosicateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accosicate_network_acl_with_options_async(request, runtime)

    def add_backend_servers_with_options(
        self,
        tmp_req: ens_20171110_models.AddBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param tmp_req: AddBackendServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBackendServersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.AddBackendServersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backend_servers):
            request.backend_servers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backend_servers, 'BackendServers', 'json')
        query = {}
        if not UtilClient.is_unset(request.backend_servers_shrink):
            query['BackendServers'] = request.backend_servers_shrink
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBackendServers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_backend_servers_with_options_async(
        self,
        tmp_req: ens_20171110_models.AddBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param tmp_req: AddBackendServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBackendServersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.AddBackendServersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backend_servers):
            request.backend_servers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backend_servers, 'BackendServers', 'json')
        query = {}
        if not UtilClient.is_unset(request.backend_servers_shrink):
            query['BackendServers'] = request.backend_servers_shrink
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBackendServers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_backend_servers(
        self,
        request: ens_20171110_models.AddBackendServersRequest,
    ) -> ens_20171110_models.AddBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: AddBackendServersRequest
        @return: AddBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_backend_servers_with_options(request, runtime)

    async def add_backend_servers_async(
        self,
        request: ens_20171110_models.AddBackendServersRequest,
    ) -> ens_20171110_models.AddBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: AddBackendServersRequest
        @return: AddBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_backend_servers_with_options_async(request, runtime)

    def add_device_internet_port_with_options(
        self,
        request: ens_20171110_models.AddDeviceInternetPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddDeviceInternetPortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDeviceInternetPort',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddDeviceInternetPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_device_internet_port_with_options_async(
        self,
        request: ens_20171110_models.AddDeviceInternetPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddDeviceInternetPortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDeviceInternetPort',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddDeviceInternetPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_device_internet_port(
        self,
        request: ens_20171110_models.AddDeviceInternetPortRequest,
    ) -> ens_20171110_models.AddDeviceInternetPortResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_device_internet_port_with_options(request, runtime)

    async def add_device_internet_port_async(
        self,
        request: ens_20171110_models.AddDeviceInternetPortRequest,
    ) -> ens_20171110_models.AddDeviceInternetPortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_device_internet_port_with_options_async(request, runtime)

    def add_network_interface_to_instance_with_options(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        *   Internal networks and IPv4 addresses are not supported.
        
        @param request: AddNetworkInterfaceToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddNetworkInterfaceToInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.networks):
            query['Networks'] = request.networks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNetworkInterfaceToInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddNetworkInterfaceToInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_network_interface_to_instance_with_options_async(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        *   Internal networks and IPv4 addresses are not supported.
        
        @param request: AddNetworkInterfaceToInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddNetworkInterfaceToInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.networks):
            query['Networks'] = request.networks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNetworkInterfaceToInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddNetworkInterfaceToInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_network_interface_to_instance(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        *   Internal networks and IPv4 addresses are not supported.
        
        @param request: AddNetworkInterfaceToInstanceRequest
        @return: AddNetworkInterfaceToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_network_interface_to_instance_with_options(request, runtime)

    async def add_network_interface_to_instance_async(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        *   Internal networks and IPv4 addresses are not supported.
        
        @param request: AddNetworkInterfaceToInstanceRequest
        @return: AddNetworkInterfaceToInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_network_interface_to_instance_with_options_async(request, runtime)

    def add_snat_ip_for_snat_entry_with_options(
        self,
        request: ens_20171110_models.AddSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddSnatIpForSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_snat_ip_for_snat_entry_with_options_async(
        self,
        request: ens_20171110_models.AddSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AddSnatIpForSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_snat_ip_for_snat_entry(
        self,
        request: ens_20171110_models.AddSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.AddSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_snat_ip_for_snat_entry_with_options(request, runtime)

    async def add_snat_ip_for_snat_entry_async(
        self,
        request: ens_20171110_models.AddSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.AddSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_snat_ip_for_snat_entry_with_options_async(request, runtime)

    def assign_private_ip_addresses_with_options(
        self,
        request: ens_20171110_models.AssignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AssignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AssignPrivateIpAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_private_ip_addresses_with_options_async(
        self,
        request: ens_20171110_models.AssignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AssignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AssignPrivateIpAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_private_ip_addresses(
        self,
        request: ens_20171110_models.AssignPrivateIpAddressesRequest,
    ) -> ens_20171110_models.AssignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_private_ip_addresses_with_options(request, runtime)

    async def assign_private_ip_addresses_async(
        self,
        request: ens_20171110_models.AssignPrivateIpAddressesRequest,
    ) -> ens_20171110_models.AssignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_private_ip_addresses_with_options_async(request, runtime)

    def associate_ens_eip_address_with_options(
        self,
        request: ens_20171110_models.AssociateEnsEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AssociateEnsEipAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.standby):
            query['Standby'] = request.standby
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateEnsEipAddress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AssociateEnsEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_ens_eip_address_with_options_async(
        self,
        request: ens_20171110_models.AssociateEnsEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AssociateEnsEipAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.standby):
            query['Standby'] = request.standby
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateEnsEipAddress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AssociateEnsEipAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_ens_eip_address(
        self,
        request: ens_20171110_models.AssociateEnsEipAddressRequest,
    ) -> ens_20171110_models.AssociateEnsEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_ens_eip_address_with_options(request, runtime)

    async def associate_ens_eip_address_async(
        self,
        request: ens_20171110_models.AssociateEnsEipAddressRequest,
    ) -> ens_20171110_models.AssociateEnsEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_ens_eip_address_with_options_async(request, runtime)

    def attach_disk_with_options(
        self,
        request: ens_20171110_models.AttachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AttachDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_with_instance):
            query['DeleteWithInstance'] = request.delete_with_instance
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AttachDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_disk_with_options_async(
        self,
        request: ens_20171110_models.AttachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AttachDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_with_instance):
            query['DeleteWithInstance'] = request.delete_with_instance
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AttachDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_disk(
        self,
        request: ens_20171110_models.AttachDiskRequest,
    ) -> ens_20171110_models.AttachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_disk_with_options(request, runtime)

    async def attach_disk_async(
        self,
        request: ens_20171110_models.AttachDiskRequest,
    ) -> ens_20171110_models.AttachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_disk_with_options_async(request, runtime)

    def attach_ens_instances_with_options(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   After you execute the command, the instance restarts loading.
        *   Limits: The instance has at least two vCPUs and 4 GB memory. An image of CentOS 7.4 or later is required.
        
        @param request: AttachEnsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEnsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scripts):
            query['Scripts'] = request.scripts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachEnsInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AttachEnsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_ens_instances_with_options_async(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   After you execute the command, the instance restarts loading.
        *   Limits: The instance has at least two vCPUs and 4 GB memory. An image of CentOS 7.4 or later is required.
        
        @param request: AttachEnsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEnsInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.scripts):
            query['Scripts'] = request.scripts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachEnsInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AttachEnsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_ens_instances(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   After you execute the command, the instance restarts loading.
        *   Limits: The instance has at least two vCPUs and 4 GB memory. An image of CentOS 7.4 or later is required.
        
        @param request: AttachEnsInstancesRequest
        @return: AttachEnsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_ens_instances_with_options(request, runtime)

    async def attach_ens_instances_async(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        """
        # [](#)Usage notes
        *   You can call this operation up to 10 times per second per account.
        *   After you execute the command, the instance restarts loading.
        *   Limits: The instance has at least two vCPUs and 4 GB memory. An image of CentOS 7.4 or later is required.
        
        @param request: AttachEnsInstancesRequest
        @return: AttachEnsInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_ens_instances_with_options_async(request, runtime)

    def authorize_security_group_with_options(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AuthorizeSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_security_group_with_options_async(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AuthorizeSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_security_group(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupRequest,
    ) -> ens_20171110_models.AuthorizeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_with_options(request, runtime)

    async def authorize_security_group_async(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupRequest,
    ) -> ens_20171110_models.AuthorizeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_security_group_with_options_async(request, runtime)

    def authorize_security_group_egress_with_options(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AuthorizeSecurityGroupEgressResponse:
        """
        In the security group-related API documents, outbound traffic refers to the traffic that is sent by the source device and received at the destination device.
        
        @param request: AuthorizeSecurityGroupEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeSecurityGroupEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroupEgress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AuthorizeSecurityGroupEgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_security_group_egress_with_options_async(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AuthorizeSecurityGroupEgressResponse:
        """
        In the security group-related API documents, outbound traffic refers to the traffic that is sent by the source device and received at the destination device.
        
        @param request: AuthorizeSecurityGroupEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeSecurityGroupEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroupEgress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.AuthorizeSecurityGroupEgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_security_group_egress(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.AuthorizeSecurityGroupEgressResponse:
        """
        In the security group-related API documents, outbound traffic refers to the traffic that is sent by the source device and received at the destination device.
        
        @param request: AuthorizeSecurityGroupEgressRequest
        @return: AuthorizeSecurityGroupEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_egress_with_options(request, runtime)

    async def authorize_security_group_egress_async(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.AuthorizeSecurityGroupEgressResponse:
        """
        In the security group-related API documents, outbound traffic refers to the traffic that is sent by the source device and received at the destination device.
        
        @param request: AuthorizeSecurityGroupEgressRequest
        @return: AuthorizeSecurityGroupEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_security_group_egress_with_options_async(request, runtime)

    def clean_dist_data_with_options(
        self,
        request: ens_20171110_models.CleanDistDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CleanDistDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.data_version):
            query['DataVersion'] = request.data_version
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CleanDistData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CleanDistDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def clean_dist_data_with_options_async(
        self,
        request: ens_20171110_models.CleanDistDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CleanDistDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data_name):
            query['DataName'] = request.data_name
        if not UtilClient.is_unset(request.data_version):
            query['DataVersion'] = request.data_version
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CleanDistData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CleanDistDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clean_dist_data(
        self,
        request: ens_20171110_models.CleanDistDataRequest,
    ) -> ens_20171110_models.CleanDistDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.clean_dist_data_with_options(request, runtime)

    async def clean_dist_data_async(
        self,
        request: ens_20171110_models.CleanDistDataRequest,
    ) -> ens_20171110_models.CleanDistDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clean_dist_data_with_options_async(request, runtime)

    def copy_sdgwith_options(
        self,
        tmp_req: ens_20171110_models.CopySDGRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CopySDGResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CopySDGShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_region_ids):
            request.destination_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_region_ids, 'DestinationRegionIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopySDG',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CopySDGResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_sdgwith_options_async(
        self,
        tmp_req: ens_20171110_models.CopySDGRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CopySDGResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CopySDGShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_region_ids):
            request.destination_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_region_ids, 'DestinationRegionIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopySDG',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CopySDGResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_sdg(
        self,
        request: ens_20171110_models.CopySDGRequest,
    ) -> ens_20171110_models.CopySDGResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_sdgwith_options(request, runtime)

    async def copy_sdg_async(
        self,
        request: ens_20171110_models.CopySDGRequest,
    ) -> ens_20171110_models.CopySDGResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_sdgwith_options_async(request, runtime)

    def copy_snapshot_with_options(
        self,
        tmp_req: ens_20171110_models.CopySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CopySnapshotResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CopySnapshotShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_region_ids):
            request.destination_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_region_ids, 'DestinationRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.destination_region_ids_shrink):
            query['DestinationRegionIds'] = request.destination_region_ids_shrink
        if not UtilClient.is_unset(request.destination_snapshot_description):
            query['DestinationSnapshotDescription'] = request.destination_snapshot_description
        if not UtilClient.is_unset(request.destination_snapshot_name):
            query['DestinationSnapshotName'] = request.destination_snapshot_name
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopySnapshot',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CopySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_snapshot_with_options_async(
        self,
        tmp_req: ens_20171110_models.CopySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CopySnapshotResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CopySnapshotShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.destination_region_ids):
            request.destination_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.destination_region_ids, 'DestinationRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.destination_region_ids_shrink):
            query['DestinationRegionIds'] = request.destination_region_ids_shrink
        if not UtilClient.is_unset(request.destination_snapshot_description):
            query['DestinationSnapshotDescription'] = request.destination_snapshot_description
        if not UtilClient.is_unset(request.destination_snapshot_name):
            query['DestinationSnapshotName'] = request.destination_snapshot_name
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopySnapshot',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CopySnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_snapshot(
        self,
        request: ens_20171110_models.CopySnapshotRequest,
    ) -> ens_20171110_models.CopySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_snapshot_with_options(request, runtime)

    async def copy_snapshot_async(
        self,
        request: ens_20171110_models.CopySnapshotRequest,
    ) -> ens_20171110_models.CopySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_snapshot_with_options_async(request, runtime)

    def create_armserver_instances_with_options(
        self,
        request: ens_20171110_models.CreateARMServerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateARMServerInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.server_name):
            query['ServerName'] = request.server_name
        if not UtilClient.is_unset(request.server_type):
            query['ServerType'] = request.server_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateARMServerInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateARMServerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_armserver_instances_with_options_async(
        self,
        request: ens_20171110_models.CreateARMServerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateARMServerInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.server_name):
            query['ServerName'] = request.server_name
        if not UtilClient.is_unset(request.server_type):
            query['ServerType'] = request.server_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateARMServerInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateARMServerInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_armserver_instances(
        self,
        request: ens_20171110_models.CreateARMServerInstancesRequest,
    ) -> ens_20171110_models.CreateARMServerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_armserver_instances_with_options(request, runtime)

    async def create_armserver_instances_async(
        self,
        request: ens_20171110_models.CreateARMServerInstancesRequest,
    ) -> ens_20171110_models.CreateARMServerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_armserver_instances_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: ens_20171110_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: ens_20171110_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: ens_20171110_models.CreateApplicationRequest,
    ) -> ens_20171110_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: ens_20171110_models.CreateApplicationRequest,
    ) -> ens_20171110_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_classic_network_with_options(
        self,
        request: ens_20171110_models.CreateClassicNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateClassicNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClassicNetwork',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateClassicNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_classic_network_with_options_async(
        self,
        request: ens_20171110_models.CreateClassicNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateClassicNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClassicNetwork',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateClassicNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_classic_network(
        self,
        request: ens_20171110_models.CreateClassicNetworkRequest,
    ) -> ens_20171110_models.CreateClassicNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_classic_network_with_options(request, runtime)

    async def create_classic_network_async(
        self,
        request: ens_20171110_models.CreateClassicNetworkRequest,
    ) -> ens_20171110_models.CreateClassicNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_classic_network_with_options_async(request, runtime)

    def create_disk_with_options(
        self,
        request: ens_20171110_models.CreateDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_with_options_async(
        self,
        request: ens_20171110_models.CreateDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk(
        self,
        request: ens_20171110_models.CreateDiskRequest,
    ) -> ens_20171110_models.CreateDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_disk_with_options(request, runtime)

    async def create_disk_async(
        self,
        request: ens_20171110_models.CreateDiskRequest,
    ) -> ens_20171110_models.CreateDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_disk_with_options_async(request, runtime)

    def create_eip_instance_with_options(
        self,
        request: ens_20171110_models.CreateEipInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEipInstanceResponse:
        """
        You can call this operation up to 5,000 times per second per account.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: CreateEipInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEipInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEipInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEipInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eip_instance_with_options_async(
        self,
        request: ens_20171110_models.CreateEipInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEipInstanceResponse:
        """
        You can call this operation up to 5,000 times per second per account.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: CreateEipInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEipInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEipInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEipInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eip_instance(
        self,
        request: ens_20171110_models.CreateEipInstanceRequest,
    ) -> ens_20171110_models.CreateEipInstanceResponse:
        """
        You can call this operation up to 5,000 times per second per account.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: CreateEipInstanceRequest
        @return: CreateEipInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eip_instance_with_options(request, runtime)

    async def create_eip_instance_async(
        self,
        request: ens_20171110_models.CreateEipInstanceRequest,
    ) -> ens_20171110_models.CreateEipInstanceResponse:
        """
        You can call this operation up to 5,000 times per second per account.
        *   You can call this operation up to 50 times per second per user.
        
        @param request: CreateEipInstanceRequest
        @return: CreateEipInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eip_instance_with_options_async(request, runtime)

    def create_ens_route_entry_with_options(
        self,
        request: ens_20171110_models.CreateEnsRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.next_hop_id):
            query['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.route_entry_name):
            query['RouteEntryName'] = request.route_entry_name
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnsRouteEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEnsRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ens_route_entry_with_options_async(
        self,
        request: ens_20171110_models.CreateEnsRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.next_hop_id):
            query['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.route_entry_name):
            query['RouteEntryName'] = request.route_entry_name
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnsRouteEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEnsRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ens_route_entry(
        self,
        request: ens_20171110_models.CreateEnsRouteEntryRequest,
    ) -> ens_20171110_models.CreateEnsRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ens_route_entry_with_options(request, runtime)

    async def create_ens_route_entry_async(
        self,
        request: ens_20171110_models.CreateEnsRouteEntryRequest,
    ) -> ens_20171110_models.CreateEnsRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ens_route_entry_with_options_async(request, runtime)

    def create_ens_sale_control_with_options(
        self,
        tmp_req: ens_20171110_models.CreateEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsSaleControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CreateEnsSaleControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEnsSaleControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ens_sale_control_with_options_async(
        self,
        tmp_req: ens_20171110_models.CreateEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsSaleControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CreateEnsSaleControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEnsSaleControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ens_sale_control(
        self,
        request: ens_20171110_models.CreateEnsSaleControlRequest,
    ) -> ens_20171110_models.CreateEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ens_sale_control_with_options(request, runtime)

    async def create_ens_sale_control_async(
        self,
        request: ens_20171110_models.CreateEnsSaleControlRequest,
    ) -> ens_20171110_models.CreateEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ens_sale_control_with_options_async(request, runtime)

    def create_ens_service_with_options(
        self,
        request: ens_20171110_models.CreateEnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_service_id):
            query['EnsServiceId'] = request.ens_service_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnsService',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ens_service_with_options_async(
        self,
        request: ens_20171110_models.CreateEnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_service_id):
            query['EnsServiceId'] = request.ens_service_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnsService',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ens_service(
        self,
        request: ens_20171110_models.CreateEnsServiceRequest,
    ) -> ens_20171110_models.CreateEnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ens_service_with_options(request, runtime)

    async def create_ens_service_async(
        self,
        request: ens_20171110_models.CreateEnsServiceRequest,
    ) -> ens_20171110_models.CreateEnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ens_service_with_options_async(request, runtime)

    def create_epn_instance_with_options(
        self,
        request: ens_20171110_models.CreateEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_name):
            query['EPNInstanceName'] = request.epninstance_name
        if not UtilClient.is_unset(request.epninstance_type):
            query['EPNInstanceType'] = request.epninstance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.CreateEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_name):
            query['EPNInstanceName'] = request.epninstance_name
        if not UtilClient.is_unset(request.epninstance_type):
            query['EPNInstanceType'] = request.epninstance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_epn_instance(
        self,
        request: ens_20171110_models.CreateEpnInstanceRequest,
    ) -> ens_20171110_models.CreateEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_epn_instance_with_options(request, runtime)

    async def create_epn_instance_async(
        self,
        request: ens_20171110_models.CreateEpnInstanceRequest,
    ) -> ens_20171110_models.CreateEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_epn_instance_with_options_async(request, runtime)

    def create_file_system_with_options(
        self,
        tmp_req: ens_20171110_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateFileSystemResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CreateFileSystemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_details):
            request.order_details_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_details, 'OrderDetails', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_system_with_options_async(
        self,
        tmp_req: ens_20171110_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateFileSystemResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CreateFileSystemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_details):
            request.order_details_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_details, 'OrderDetails', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_system(
        self,
        request: ens_20171110_models.CreateFileSystemRequest,
    ) -> ens_20171110_models.CreateFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_file_system_with_options(request, runtime)

    async def create_file_system_async(
        self,
        request: ens_20171110_models.CreateFileSystemRequest,
    ) -> ens_20171110_models.CreateFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_file_system_with_options_async(request, runtime)

    def create_forward_entry_with_options(
        self,
        request: ens_20171110_models.CreateForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateForwardEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.external_port):
            query['ExternalPort'] = request.external_port
        if not UtilClient.is_unset(request.forward_entry_name):
            query['ForwardEntryName'] = request.forward_entry_name
        if not UtilClient.is_unset(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.standby_external_ip):
            query['StandbyExternalIp'] = request.standby_external_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateForwardEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateForwardEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_forward_entry_with_options_async(
        self,
        request: ens_20171110_models.CreateForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateForwardEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.external_port):
            query['ExternalPort'] = request.external_port
        if not UtilClient.is_unset(request.forward_entry_name):
            query['ForwardEntryName'] = request.forward_entry_name
        if not UtilClient.is_unset(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.standby_external_ip):
            query['StandbyExternalIp'] = request.standby_external_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateForwardEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateForwardEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_forward_entry(
        self,
        request: ens_20171110_models.CreateForwardEntryRequest,
    ) -> ens_20171110_models.CreateForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_forward_entry_with_options(request, runtime)

    async def create_forward_entry_async(
        self,
        request: ens_20171110_models.CreateForwardEntryRequest,
    ) -> ens_20171110_models.CreateForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_forward_entry_with_options_async(request, runtime)

    def create_image_with_options(
        self,
        request: ens_20171110_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_after_image_upload):
            query['DeleteAfterImageUpload'] = request.delete_after_image_upload
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: ens_20171110_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_after_image_upload):
            query['DeleteAfterImageUpload'] = request.delete_after_image_upload
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image(
        self,
        request: ens_20171110_models.CreateImageRequest,
    ) -> ens_20171110_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    async def create_image_async(
        self,
        request: ens_20171110_models.CreateImageRequest,
    ) -> ens_20171110_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ens_20171110_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateInstanceResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   We recommend that you increase the request time because instance creation is an asynchronous operation. If the return code of the API operation is 0, it indicates that the request is successful, but does not indicate that the instance is created. If the request is successful, an instance ID is returned. You can check whether the instance is created based on the instance ID.
        *   InvalidUserData.NotInWhiteList operation restriction: You can create an instance only if you are in the whitelist in which members have the purchase permissions. Otherwise, an error is returned.
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.public_ip_identification):
            query['PublicIpIdentification'] = request.public_ip_identification
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: ens_20171110_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateInstanceResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   We recommend that you increase the request time because instance creation is an asynchronous operation. If the return code of the API operation is 0, it indicates that the request is successful, but does not indicate that the instance is created. If the request is successful, an instance ID is returned. You can check whether the instance is created based on the instance ID.
        *   InvalidUserData.NotInWhiteList operation restriction: You can create an instance only if you are in the whitelist in which members have the purchase permissions. Otherwise, an error is returned.
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.public_ip_identification):
            query['PublicIpIdentification'] = request.public_ip_identification
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: ens_20171110_models.CreateInstanceRequest,
    ) -> ens_20171110_models.CreateInstanceResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   We recommend that you increase the request time because instance creation is an asynchronous operation. If the return code of the API operation is 0, it indicates that the request is successful, but does not indicate that the instance is created. If the request is successful, an instance ID is returned. You can check whether the instance is created based on the instance ID.
        *   InvalidUserData.NotInWhiteList operation restriction: You can create an instance only if you are in the whitelist in which members have the purchase permissions. Otherwise, an error is returned.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ens_20171110_models.CreateInstanceRequest,
    ) -> ens_20171110_models.CreateInstanceResponse:
        """
        You can call this operation up to 10 times per second per account.
        *   We recommend that you increase the request time because instance creation is an asynchronous operation. If the return code of the API operation is 0, it indicates that the request is successful, but does not indicate that the instance is created. If the request is successful, an instance ID is returned. You can check whether the instance is created based on the instance ID.
        *   InvalidUserData.NotInWhiteList operation restriction: You can create an instance only if you are in the whitelist in which members have the purchase permissions. Otherwise, an error is returned.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_instance_active_ops_task_with_options(
        self,
        tmp_req: ens_20171110_models.CreateInstanceActiveOpsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateInstanceActiveOpsTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CreateInstanceActiveOpsTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceActiveOpsTask',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateInstanceActiveOpsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_active_ops_task_with_options_async(
        self,
        tmp_req: ens_20171110_models.CreateInstanceActiveOpsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateInstanceActiveOpsTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.CreateInstanceActiveOpsTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstanceActiveOpsTask',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateInstanceActiveOpsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_active_ops_task(
        self,
        request: ens_20171110_models.CreateInstanceActiveOpsTaskRequest,
    ) -> ens_20171110_models.CreateInstanceActiveOpsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_active_ops_task_with_options(request, runtime)

    async def create_instance_active_ops_task_async(
        self,
        request: ens_20171110_models.CreateInstanceActiveOpsTaskRequest,
    ) -> ens_20171110_models.CreateInstanceActiveOpsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_active_ops_task_with_options_async(request, runtime)

    def create_key_pair_with_options(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        """
        An SSH key pair consists of a public key and a private key. ENS stores the public key and returns the unencrypted private key that is PEM-encoded in the PKCS#8 format. You must securely lock away the private key.
        
        @param request: CreateKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyPair',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_key_pair_with_options_async(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        """
        An SSH key pair consists of a public key and a private key. ENS stores the public key and returns the unencrypted private key that is PEM-encoded in the PKCS#8 format. You must securely lock away the private key.
        
        @param request: CreateKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateKeyPair',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_key_pair(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        """
        An SSH key pair consists of a public key and a private key. ENS stores the public key and returns the unencrypted private key that is PEM-encoded in the PKCS#8 format. You must securely lock away the private key.
        
        @param request: CreateKeyPairRequest
        @return: CreateKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    async def create_key_pair_async(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        """
        An SSH key pair consists of a public key and a private key. ENS stores the public key and returns the unencrypted private key that is PEM-encoded in the PKCS#8 format. You must securely lock away the private key.
        
        @param request: CreateKeyPairRequest
        @return: CreateKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_key_pair_with_options_async(request, runtime)

    def create_load_balancer_with_options(
        self,
        request: ens_20171110_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_with_options_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateLoadBalancerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer(
        self,
        request: ens_20171110_models.CreateLoadBalancerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    async def create_load_balancer_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateLoadBalancerRequest
        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_with_options_async(request, runtime)

    def create_load_balancer_httplistener_with_options(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerHTTPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerHTTPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_httplistener_with_options_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerHTTPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerHTTPListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_httplistener(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPListenerRequest
        @return: CreateLoadBalancerHTTPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httplistener_with_options(request, runtime)

    async def create_load_balancer_httplistener_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPListenerRequest
        @return: CreateLoadBalancerHTTPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_httplistener_with_options_async(request, runtime)

    def create_load_balancer_httpslistener_with_options(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPSListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPSListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPSListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerHTTPSListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPSListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerHTTPSListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_httpslistener_with_options_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPSListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPSListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPSListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerHTTPSListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPSListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerHTTPSListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_httpslistener(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPSListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPSListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPSListenerRequest
        @return: CreateLoadBalancerHTTPSListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httpslistener_with_options(request, runtime)

    async def create_load_balancer_httpslistener_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerHTTPSListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerHTTPSListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerHTTPSListenerRequest
        @return: CreateLoadBalancerHTTPSListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_httpslistener_with_options_async(request, runtime)

    def create_load_balancer_tcplistener_with_options(
        self,
        request: ens_20171110_models.CreateLoadBalancerTCPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerTCPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerTCPListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerTCPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerTCPListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerTCPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_tcplistener_with_options_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerTCPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerTCPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerTCPListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerTCPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerTCPListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerTCPListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_tcplistener(
        self,
        request: ens_20171110_models.CreateLoadBalancerTCPListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerTCPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerTCPListenerRequest
        @return: CreateLoadBalancerTCPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_tcplistener_with_options(request, runtime)

    async def create_load_balancer_tcplistener_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerTCPListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerTCPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerTCPListenerRequest
        @return: CreateLoadBalancerTCPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_tcplistener_with_options_async(request, runtime)

    def create_load_balancer_udplistener_with_options(
        self,
        request: ens_20171110_models.CreateLoadBalancerUDPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerUDPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerUDPListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerUDPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_exp):
            query['HealthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_req):
            query['HealthCheckReq'] = request.health_check_req
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerUDPListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerUDPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_load_balancer_udplistener_with_options_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerUDPListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateLoadBalancerUDPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerUDPListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLoadBalancerUDPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_exp):
            query['HealthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_req):
            query['HealthCheckReq'] = request.health_check_req
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerUDPListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateLoadBalancerUDPListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_load_balancer_udplistener(
        self,
        request: ens_20171110_models.CreateLoadBalancerUDPListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerUDPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerUDPListenerRequest
        @return: CreateLoadBalancerUDPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_udplistener_with_options(request, runtime)

    async def create_load_balancer_udplistener_async(
        self,
        request: ens_20171110_models.CreateLoadBalancerUDPListenerRequest,
    ) -> ens_20171110_models.CreateLoadBalancerUDPListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: CreateLoadBalancerUDPListenerRequest
        @return: CreateLoadBalancerUDPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_load_balancer_udplistener_with_options_async(request, runtime)

    def create_mount_target_with_options(
        self,
        request: ens_20171110_models.CreateMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateMountTargetResponse:
        """
        ## [](#)Precautions
        After you call this operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the Active state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        
        @param request: CreateMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_name):
            query['MountTargetName'] = request.mount_target_name
        if not UtilClient.is_unset(request.net_work_id):
            query['NetWorkId'] = request.net_work_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMountTarget',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mount_target_with_options_async(
        self,
        request: ens_20171110_models.CreateMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateMountTargetResponse:
        """
        ## [](#)Precautions
        After you call this operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the Active state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        
        @param request: CreateMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_name):
            query['MountTargetName'] = request.mount_target_name
        if not UtilClient.is_unset(request.net_work_id):
            query['NetWorkId'] = request.net_work_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMountTarget',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mount_target(
        self,
        request: ens_20171110_models.CreateMountTargetRequest,
    ) -> ens_20171110_models.CreateMountTargetResponse:
        """
        ## [](#)Precautions
        After you call this operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the Active state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        
        @param request: CreateMountTargetRequest
        @return: CreateMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mount_target_with_options(request, runtime)

    async def create_mount_target_async(
        self,
        request: ens_20171110_models.CreateMountTargetRequest,
    ) -> ens_20171110_models.CreateMountTargetResponse:
        """
        ## [](#)Precautions
        After you call this operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the Active state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        
        @param request: CreateMountTargetRequest
        @return: CreateMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mount_target_with_options_async(request, runtime)

    def create_nat_gateway_with_options(
        self,
        request: ens_20171110_models.CreateNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNatGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNatGateway',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNatGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nat_gateway_with_options_async(
        self,
        request: ens_20171110_models.CreateNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNatGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNatGateway',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNatGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nat_gateway(
        self,
        request: ens_20171110_models.CreateNatGatewayRequest,
    ) -> ens_20171110_models.CreateNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nat_gateway_with_options(request, runtime)

    async def create_nat_gateway_async(
        self,
        request: ens_20171110_models.CreateNatGatewayRequest,
    ) -> ens_20171110_models.CreateNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nat_gateway_with_options_async(request, runtime)

    def create_network_with_options(
        self,
        request: ens_20171110_models.CreateNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNetworkResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetwork',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_with_options_async(
        self,
        request: ens_20171110_models.CreateNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNetworkResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetwork',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network(
        self,
        request: ens_20171110_models.CreateNetworkRequest,
    ) -> ens_20171110_models.CreateNetworkResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateNetworkRequest
        @return: CreateNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_with_options(request, runtime)

    async def create_network_async(
        self,
        request: ens_20171110_models.CreateNetworkRequest,
    ) -> ens_20171110_models.CreateNetworkResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: CreateNetworkRequest
        @return: CreateNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_with_options_async(request, runtime)

    def create_network_acl_with_options(
        self,
        request: ens_20171110_models.CreateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_acl_name):
            query['NetworkAclName'] = request.network_acl_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNetworkAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_acl_with_options_async(
        self,
        request: ens_20171110_models.CreateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_acl_name):
            query['NetworkAclName'] = request.network_acl_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNetworkAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_acl(
        self,
        request: ens_20171110_models.CreateNetworkAclRequest,
    ) -> ens_20171110_models.CreateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_acl_with_options(request, runtime)

    async def create_network_acl_async(
        self,
        request: ens_20171110_models.CreateNetworkAclRequest,
    ) -> ens_20171110_models.CreateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_acl_with_options_async(request, runtime)

    def create_network_acl_entry_with_options(
        self,
        request: ens_20171110_models.CreateNetworkAclEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNetworkAclEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.network_acl_entry_name):
            query['NetworkAclEntryName'] = request.network_acl_entry_name
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkAclEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNetworkAclEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_acl_entry_with_options_async(
        self,
        request: ens_20171110_models.CreateNetworkAclEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateNetworkAclEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.network_acl_entry_name):
            query['NetworkAclEntryName'] = request.network_acl_entry_name
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkAclEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateNetworkAclEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_acl_entry(
        self,
        request: ens_20171110_models.CreateNetworkAclEntryRequest,
    ) -> ens_20171110_models.CreateNetworkAclEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_acl_entry_with_options(request, runtime)

    async def create_network_acl_entry_async(
        self,
        request: ens_20171110_models.CreateNetworkAclEntryRequest,
    ) -> ens_20171110_models.CreateNetworkAclEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_acl_entry_with_options_async(request, runtime)

    def create_security_group_with_options(
        self,
        request: ens_20171110_models.CreateSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_group_with_options_async(
        self,
        request: ens_20171110_models.CreateSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_group(
        self,
        request: ens_20171110_models.CreateSecurityGroupRequest,
    ) -> ens_20171110_models.CreateSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_security_group_with_options(request, runtime)

    async def create_security_group_async(
        self,
        request: ens_20171110_models.CreateSecurityGroupRequest,
    ) -> ens_20171110_models.CreateSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_security_group_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: ens_20171110_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: ens_20171110_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: ens_20171110_models.CreateSnapshotRequest,
    ) -> ens_20171110_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: ens_20171110_models.CreateSnapshotRequest,
    ) -> ens_20171110_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def create_snat_entry_with_options(
        self,
        request: ens_20171110_models.CreateSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.snat_entry_name):
            query['SnatEntryName'] = request.snat_entry_name
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCIDR'] = request.source_cidr
        if not UtilClient.is_unset(request.source_network_id):
            query['SourceNetworkId'] = request.source_network_id
        if not UtilClient.is_unset(request.source_vswitch_id):
            query['SourceVSwitchId'] = request.source_vswitch_id
        if not UtilClient.is_unset(request.standby_snat_ip):
            query['StandbySnatIp'] = request.standby_snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snat_entry_with_options_async(
        self,
        request: ens_20171110_models.CreateSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.snat_entry_name):
            query['SnatEntryName'] = request.snat_entry_name
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        if not UtilClient.is_unset(request.source_cidr):
            query['SourceCIDR'] = request.source_cidr
        if not UtilClient.is_unset(request.source_network_id):
            query['SourceNetworkId'] = request.source_network_id
        if not UtilClient.is_unset(request.source_vswitch_id):
            query['SourceVSwitchId'] = request.source_vswitch_id
        if not UtilClient.is_unset(request.standby_snat_ip):
            query['StandbySnatIp'] = request.standby_snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snat_entry(
        self,
        request: ens_20171110_models.CreateSnatEntryRequest,
    ) -> ens_20171110_models.CreateSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snat_entry_with_options(request, runtime)

    async def create_snat_entry_async(
        self,
        request: ens_20171110_models.CreateSnatEntryRequest,
    ) -> ens_20171110_models.CreateSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snat_entry_with_options_async(request, runtime)

    def create_vswitch_with_options(
        self,
        request: ens_20171110_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVSwitch',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateVSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vswitch_with_options_async(
        self,
        request: ens_20171110_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVSwitch',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.CreateVSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vswitch(
        self,
        request: ens_20171110_models.CreateVSwitchRequest,
    ) -> ens_20171110_models.CreateVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vswitch_with_options(request, runtime)

    async def create_vswitch_async(
        self,
        request: ens_20171110_models.CreateVSwitchRequest,
    ) -> ens_20171110_models.CreateVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vswitch_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: ens_20171110_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: ens_20171110_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: ens_20171110_models.DeleteApplicationRequest,
    ) -> ens_20171110_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: ens_20171110_models.DeleteApplicationRequest,
    ) -> ens_20171110_models.DeleteApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def delete_bucket_with_options(
        self,
        request: ens_20171110_models.DeleteBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucket',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_bucket_with_options_async(
        self,
        request: ens_20171110_models.DeleteBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucket',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_bucket(
        self,
        request: ens_20171110_models.DeleteBucketRequest,
    ) -> ens_20171110_models.DeleteBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bucket_with_options(request, runtime)

    async def delete_bucket_async(
        self,
        request: ens_20171110_models.DeleteBucketRequest,
    ) -> ens_20171110_models.DeleteBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bucket_with_options_async(request, runtime)

    def delete_bucket_lifecycle_with_options(
        self,
        request: ens_20171110_models.DeleteBucketLifecycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteBucketLifecycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucketLifecycle',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteBucketLifecycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_bucket_lifecycle_with_options_async(
        self,
        request: ens_20171110_models.DeleteBucketLifecycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteBucketLifecycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucketLifecycle',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteBucketLifecycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_bucket_lifecycle(
        self,
        request: ens_20171110_models.DeleteBucketLifecycleRequest,
    ) -> ens_20171110_models.DeleteBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bucket_lifecycle_with_options(request, runtime)

    async def delete_bucket_lifecycle_async(
        self,
        request: ens_20171110_models.DeleteBucketLifecycleRequest,
    ) -> ens_20171110_models.DeleteBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bucket_lifecycle_with_options_async(request, runtime)

    def delete_device_internet_port_with_options(
        self,
        request: ens_20171110_models.DeleteDeviceInternetPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteDeviceInternetPortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceInternetPort',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteDeviceInternetPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_internet_port_with_options_async(
        self,
        request: ens_20171110_models.DeleteDeviceInternetPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteDeviceInternetPortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceInternetPort',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteDeviceInternetPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device_internet_port(
        self,
        request: ens_20171110_models.DeleteDeviceInternetPortRequest,
    ) -> ens_20171110_models.DeleteDeviceInternetPortResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_internet_port_with_options(request, runtime)

    async def delete_device_internet_port_async(
        self,
        request: ens_20171110_models.DeleteDeviceInternetPortRequest,
    ) -> ens_20171110_models.DeleteDeviceInternetPortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_internet_port_with_options_async(request, runtime)

    def delete_disk_with_options(
        self,
        request: ens_20171110_models.DeleteDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteDiskResponse:
        """
        When you release a disk, the disk must be in the Available state.
        
        @param request: DeleteDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disk_with_options_async(
        self,
        request: ens_20171110_models.DeleteDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteDiskResponse:
        """
        When you release a disk, the disk must be in the Available state.
        
        @param request: DeleteDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disk(
        self,
        request: ens_20171110_models.DeleteDiskRequest,
    ) -> ens_20171110_models.DeleteDiskResponse:
        """
        When you release a disk, the disk must be in the Available state.
        
        @param request: DeleteDiskRequest
        @return: DeleteDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_with_options(request, runtime)

    async def delete_disk_async(
        self,
        request: ens_20171110_models.DeleteDiskRequest,
    ) -> ens_20171110_models.DeleteDiskResponse:
        """
        When you release a disk, the disk must be in the Available state.
        
        @param request: DeleteDiskRequest
        @return: DeleteDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_disk_with_options_async(request, runtime)

    def delete_ens_route_entry_with_options(
        self,
        request: ens_20171110_models.DeleteEnsRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEnsRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.route_entry_id):
            query['RouteEntryId'] = request.route_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnsRouteEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEnsRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ens_route_entry_with_options_async(
        self,
        request: ens_20171110_models.DeleteEnsRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEnsRouteEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.route_entry_id):
            query['RouteEntryId'] = request.route_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnsRouteEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEnsRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ens_route_entry(
        self,
        request: ens_20171110_models.DeleteEnsRouteEntryRequest,
    ) -> ens_20171110_models.DeleteEnsRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ens_route_entry_with_options(request, runtime)

    async def delete_ens_route_entry_async(
        self,
        request: ens_20171110_models.DeleteEnsRouteEntryRequest,
    ) -> ens_20171110_models.DeleteEnsRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ens_route_entry_with_options_async(request, runtime)

    def delete_ens_sale_condition_control_with_options(
        self,
        tmp_req: ens_20171110_models.DeleteEnsSaleConditionControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEnsSaleConditionControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DeleteEnsSaleConditionControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnsSaleConditionControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEnsSaleConditionControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ens_sale_condition_control_with_options_async(
        self,
        tmp_req: ens_20171110_models.DeleteEnsSaleConditionControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEnsSaleConditionControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DeleteEnsSaleConditionControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnsSaleConditionControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEnsSaleConditionControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ens_sale_condition_control(
        self,
        request: ens_20171110_models.DeleteEnsSaleConditionControlRequest,
    ) -> ens_20171110_models.DeleteEnsSaleConditionControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ens_sale_condition_control_with_options(request, runtime)

    async def delete_ens_sale_condition_control_async(
        self,
        request: ens_20171110_models.DeleteEnsSaleConditionControlRequest,
    ) -> ens_20171110_models.DeleteEnsSaleConditionControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ens_sale_condition_control_with_options_async(request, runtime)

    def delete_ens_sale_control_with_options(
        self,
        tmp_req: ens_20171110_models.DeleteEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEnsSaleControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DeleteEnsSaleControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEnsSaleControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ens_sale_control_with_options_async(
        self,
        tmp_req: ens_20171110_models.DeleteEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEnsSaleControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DeleteEnsSaleControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEnsSaleControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ens_sale_control(
        self,
        request: ens_20171110_models.DeleteEnsSaleControlRequest,
    ) -> ens_20171110_models.DeleteEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ens_sale_control_with_options(request, runtime)

    async def delete_ens_sale_control_async(
        self,
        request: ens_20171110_models.DeleteEnsSaleControlRequest,
    ) -> ens_20171110_models.DeleteEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ens_sale_control_with_options_async(request, runtime)

    def delete_epn_instance_with_options(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        """
        You can delete an EPN instance only when the instance group information is empty.
        
        @param request: DeleteEpnInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEpnInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        """
        You can delete an EPN instance only when the instance group information is empty.
        
        @param request: DeleteEpnInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEpnInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_epn_instance(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        """
        You can delete an EPN instance only when the instance group information is empty.
        
        @param request: DeleteEpnInstanceRequest
        @return: DeleteEpnInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_epn_instance_with_options(request, runtime)

    async def delete_epn_instance_async(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        """
        You can delete an EPN instance only when the instance group information is empty.
        
        @param request: DeleteEpnInstanceRequest
        @return: DeleteEpnInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_epn_instance_with_options_async(request, runtime)

    def delete_file_system_with_options(
        self,
        request: ens_20171110_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteFileSystemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_system_with_options_async(
        self,
        request: ens_20171110_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteFileSystemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_system(
        self,
        request: ens_20171110_models.DeleteFileSystemRequest,
    ) -> ens_20171110_models.DeleteFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_file_system_with_options(request, runtime)

    async def delete_file_system_async(
        self,
        request: ens_20171110_models.DeleteFileSystemRequest,
    ) -> ens_20171110_models.DeleteFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_system_with_options_async(request, runtime)

    def delete_forward_entry_with_options(
        self,
        request: ens_20171110_models.DeleteForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteForwardEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteForwardEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteForwardEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_forward_entry_with_options_async(
        self,
        request: ens_20171110_models.DeleteForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteForwardEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteForwardEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteForwardEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_forward_entry(
        self,
        request: ens_20171110_models.DeleteForwardEntryRequest,
    ) -> ens_20171110_models.DeleteForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_forward_entry_with_options(request, runtime)

    async def delete_forward_entry_async(
        self,
        request: ens_20171110_models.DeleteForwardEntryRequest,
    ) -> ens_20171110_models.DeleteForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_forward_entry_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: ens_20171110_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: ens_20171110_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        request: ens_20171110_models.DeleteImageRequest,
    ) -> ens_20171110_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: ens_20171110_models.DeleteImageRequest,
    ) -> ens_20171110_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        """
        After you delete an SSH key pair, you can no longer query the key pair by calling the DescribeKeyPairs operation.
        *   If you delete an SSH key pair that is bound to an Edge Node Service (ENS) instance, ENS no longer stores the SSH key pair. However, you can still use the key pair to access the instance. When you call the DescribeInstance operation to query instance information, no other information but the name of the key pair (**KeyPairName**) is returned.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        """
        After you delete an SSH key pair, you can no longer query the key pair by calling the DescribeKeyPairs operation.
        *   If you delete an SSH key pair that is bound to an Edge Node Service (ENS) instance, ENS no longer stores the SSH key pair. However, you can still use the key pair to access the instance. When you call the DescribeInstance operation to query instance information, no other information but the name of the key pair (**KeyPairName**) is returned.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_pairs(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        """
        After you delete an SSH key pair, you can no longer query the key pair by calling the DescribeKeyPairs operation.
        *   If you delete an SSH key pair that is bound to an Edge Node Service (ENS) instance, ENS no longer stores the SSH key pair. However, you can still use the key pair to access the instance. When you call the DescribeInstance operation to query instance information, no other information but the name of the key pair (**KeyPairName**) is returned.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        """
        After you delete an SSH key pair, you can no longer query the key pair by calling the DescribeKeyPairs operation.
        *   If you delete an SSH key pair that is bound to an Edge Node Service (ENS) instance, ENS no longer stores the SSH key pair. However, you can still use the key pair to access the instance. When you call the DescribeInstance operation to query instance information, no other information but the name of the key pair (**KeyPairName**) is returned.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def delete_load_balancer_listener_with_options(
        self,
        request: ens_20171110_models.DeleteLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DeleteLoadBalancerListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancerListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_load_balancer_listener_with_options_async(
        self,
        request: ens_20171110_models.DeleteLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DeleteLoadBalancerListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancerListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_load_balancer_listener(
        self,
        request: ens_20171110_models.DeleteLoadBalancerListenerRequest,
    ) -> ens_20171110_models.DeleteLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DeleteLoadBalancerListenerRequest
        @return: DeleteLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_listener_with_options(request, runtime)

    async def delete_load_balancer_listener_async(
        self,
        request: ens_20171110_models.DeleteLoadBalancerListenerRequest,
    ) -> ens_20171110_models.DeleteLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DeleteLoadBalancerListenerRequest
        @return: DeleteLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_load_balancer_listener_with_options_async(request, runtime)

    def delete_mount_target_with_options(
        self,
        request: ens_20171110_models.DeleteMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteMountTargetResponse:
        """
        After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_name):
            query['MountTargetName'] = request.mount_target_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMountTarget',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mount_target_with_options_async(
        self,
        request: ens_20171110_models.DeleteMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteMountTargetResponse:
        """
        After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_name):
            query['MountTargetName'] = request.mount_target_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMountTarget',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mount_target(
        self,
        request: ens_20171110_models.DeleteMountTargetRequest,
    ) -> ens_20171110_models.DeleteMountTargetResponse:
        """
        After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @return: DeleteMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mount_target_with_options(request, runtime)

    async def delete_mount_target_async(
        self,
        request: ens_20171110_models.DeleteMountTargetRequest,
    ) -> ens_20171110_models.DeleteMountTargetResponse:
        """
        After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @return: DeleteMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mount_target_with_options_async(request, runtime)

    def delete_nat_gateway_with_options(
        self,
        request: ens_20171110_models.DeleteNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNatGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNatGateway',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNatGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nat_gateway_with_options_async(
        self,
        request: ens_20171110_models.DeleteNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNatGatewayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNatGateway',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNatGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nat_gateway(
        self,
        request: ens_20171110_models.DeleteNatGatewayRequest,
    ) -> ens_20171110_models.DeleteNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_gateway_with_options(request, runtime)

    async def delete_nat_gateway_async(
        self,
        request: ens_20171110_models.DeleteNatGatewayRequest,
    ) -> ens_20171110_models.DeleteNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_gateway_with_options_async(request, runtime)

    def delete_network_with_options(
        self,
        request: ens_20171110_models.DeleteNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetwork',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_with_options_async(
        self,
        request: ens_20171110_models.DeleteNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNetworkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetwork',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network(
        self,
        request: ens_20171110_models.DeleteNetworkRequest,
    ) -> ens_20171110_models.DeleteNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_with_options(request, runtime)

    async def delete_network_async(
        self,
        request: ens_20171110_models.DeleteNetworkRequest,
    ) -> ens_20171110_models.DeleteNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_with_options_async(request, runtime)

    def delete_network_acl_with_options(
        self,
        request: ens_20171110_models.DeleteNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNetworkAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_acl_with_options_async(
        self,
        request: ens_20171110_models.DeleteNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNetworkAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_acl(
        self,
        request: ens_20171110_models.DeleteNetworkAclRequest,
    ) -> ens_20171110_models.DeleteNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_acl_with_options(request, runtime)

    async def delete_network_acl_async(
        self,
        request: ens_20171110_models.DeleteNetworkAclRequest,
    ) -> ens_20171110_models.DeleteNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_acl_with_options_async(request, runtime)

    def delete_network_acl_entry_with_options(
        self,
        request: ens_20171110_models.DeleteNetworkAclEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNetworkAclEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_entry_id):
            query['NetworkAclEntryId'] = request.network_acl_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkAclEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNetworkAclEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_acl_entry_with_options_async(
        self,
        request: ens_20171110_models.DeleteNetworkAclEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteNetworkAclEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_entry_id):
            query['NetworkAclEntryId'] = request.network_acl_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkAclEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteNetworkAclEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_acl_entry(
        self,
        request: ens_20171110_models.DeleteNetworkAclEntryRequest,
    ) -> ens_20171110_models.DeleteNetworkAclEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_acl_entry_with_options(request, runtime)

    async def delete_network_acl_entry_async(
        self,
        request: ens_20171110_models.DeleteNetworkAclEntryRequest,
    ) -> ens_20171110_models.DeleteNetworkAclEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_acl_entry_with_options_async(request, runtime)

    def delete_object_with_options(
        self,
        request: ens_20171110_models.DeleteObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.object_key):
            query['ObjectKey'] = request.object_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObject',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_object_with_options_async(
        self,
        request: ens_20171110_models.DeleteObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.object_key):
            query['ObjectKey'] = request.object_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteObject',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_object(
        self,
        request: ens_20171110_models.DeleteObjectRequest,
    ) -> ens_20171110_models.DeleteObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_object_with_options(request, runtime)

    async def delete_object_async(
        self,
        request: ens_20171110_models.DeleteObjectRequest,
    ) -> ens_20171110_models.DeleteObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_object_with_options_async(request, runtime)

    def delete_security_group_with_options(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        """
        Before you delete a security group, make sure that no instances exist in the security group.
        
        @param request: DeleteSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_group_with_options_async(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        """
        Before you delete a security group, make sure that no instances exist in the security group.
        
        @param request: DeleteSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_group(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        """
        Before you delete a security group, make sure that no instances exist in the security group.
        
        @param request: DeleteSecurityGroupRequest
        @return: DeleteSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    async def delete_security_group_async(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        """
        Before you delete a security group, make sure that no instances exist in the security group.
        
        @param request: DeleteSecurityGroupRequest
        @return: DeleteSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_group_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: ens_20171110_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: ens_20171110_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: ens_20171110_models.DeleteSnapshotRequest,
    ) -> ens_20171110_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: ens_20171110_models.DeleteSnapshotRequest,
    ) -> ens_20171110_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_snat_entry_with_options(
        self,
        request: ens_20171110_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snat_entry_with_options_async(
        self,
        request: ens_20171110_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snat_entry(
        self,
        request: ens_20171110_models.DeleteSnatEntryRequest,
    ) -> ens_20171110_models.DeleteSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snat_entry_with_options(request, runtime)

    async def delete_snat_entry_async(
        self,
        request: ens_20171110_models.DeleteSnatEntryRequest,
    ) -> ens_20171110_models.DeleteSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snat_entry_with_options_async(request, runtime)

    def delete_snat_ip_for_snat_entry_with_options(
        self,
        request: ens_20171110_models.DeleteSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSnatIpForSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snat_ip_for_snat_entry_with_options_async(
        self,
        request: ens_20171110_models.DeleteSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteSnatIpForSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snat_ip_for_snat_entry(
        self,
        request: ens_20171110_models.DeleteSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.DeleteSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snat_ip_for_snat_entry_with_options(request, runtime)

    async def delete_snat_ip_for_snat_entry_async(
        self,
        request: ens_20171110_models.DeleteSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.DeleteSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snat_ip_for_snat_entry_with_options_async(request, runtime)

    def delete_vswitch_with_options(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        """
        Before you delete a vSwitch, make sure that no instances exist in the vSwitch.
        
        @param request: DeleteVSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVSwitch',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteVSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vswitch_with_options_async(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        """
        Before you delete a vSwitch, make sure that no instances exist in the vSwitch.
        
        @param request: DeleteVSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVSwitch',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeleteVSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vswitch(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        """
        Before you delete a vSwitch, make sure that no instances exist in the vSwitch.
        
        @param request: DeleteVSwitchRequest
        @return: DeleteVSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vswitch_with_options(request, runtime)

    async def delete_vswitch_async(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        """
        Before you delete a vSwitch, make sure that no instances exist in the vSwitch.
        
        @param request: DeleteVSwitchRequest
        @return: DeleteVSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vswitch_with_options_async(request, runtime)

    def deploy_sdgwith_options(
        self,
        tmp_req: ens_20171110_models.DeploySDGRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeploySDGResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DeploySDGShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeploySDG',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeploySDGResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_sdgwith_options_async(
        self,
        tmp_req: ens_20171110_models.DeploySDGRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeploySDGResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DeploySDGShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeploySDG',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DeploySDGResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_sdg(
        self,
        request: ens_20171110_models.DeploySDGRequest,
    ) -> ens_20171110_models.DeploySDGResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_sdgwith_options(request, runtime)

    async def deploy_sdg_async(
        self,
        request: ens_20171110_models.DeploySDGRequest,
    ) -> ens_20171110_models.DeploySDGResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_sdgwith_options_async(request, runtime)

    def describe_aicimages_with_options(
        self,
        request: ens_20171110_models.DescribeAICImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAICImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAICImages',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeAICImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aicimages_with_options_async(
        self,
        request: ens_20171110_models.DescribeAICImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAICImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAICImages',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeAICImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aicimages(
        self,
        request: ens_20171110_models.DescribeAICImagesRequest,
    ) -> ens_20171110_models.DescribeAICImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_aicimages_with_options(request, runtime)

    async def describe_aicimages_async(
        self,
        request: ens_20171110_models.DescribeAICImagesRequest,
    ) -> ens_20171110_models.DescribeAICImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_aicimages_with_options_async(request, runtime)

    def describe_armserver_instances_with_options(
        self,
        tmp_req: ens_20171110_models.DescribeARMServerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeARMServerInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribeARMServerInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aicspecs):
            request.aicspecs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aicspecs, 'AICSpecs', 'json')
        if not UtilClient.is_unset(tmp_req.ens_region_ids):
            request.ens_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ens_region_ids, 'EnsRegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.server_ids):
            request.server_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.server_ids, 'ServerIds', 'json')
        if not UtilClient.is_unset(tmp_req.server_specs):
            request.server_specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.server_specs, 'ServerSpecs', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'States', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeARMServerInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeARMServerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_armserver_instances_with_options_async(
        self,
        tmp_req: ens_20171110_models.DescribeARMServerInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeARMServerInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribeARMServerInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aicspecs):
            request.aicspecs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aicspecs, 'AICSpecs', 'json')
        if not UtilClient.is_unset(tmp_req.ens_region_ids):
            request.ens_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ens_region_ids, 'EnsRegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.server_ids):
            request.server_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.server_ids, 'ServerIds', 'json')
        if not UtilClient.is_unset(tmp_req.server_specs):
            request.server_specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.server_specs, 'ServerSpecs', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'States', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeARMServerInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeARMServerInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_armserver_instances(
        self,
        request: ens_20171110_models.DescribeARMServerInstancesRequest,
    ) -> ens_20171110_models.DescribeARMServerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_armserver_instances_with_options(request, runtime)

    async def describe_armserver_instances_async(
        self,
        request: ens_20171110_models.DescribeARMServerInstancesRequest,
    ) -> ens_20171110_models.DescribeARMServerInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_armserver_instances_with_options_async(request, runtime)

    def describe_application_with_options(
        self,
        request: ens_20171110_models.DescribeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_versions):
            query['AppVersions'] = request.app_versions
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.out_detail_stat_params):
            query['OutDetailStatParams'] = request.out_detail_stat_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_with_options_async(
        self,
        request: ens_20171110_models.DescribeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_versions):
            query['AppVersions'] = request.app_versions
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.out_detail_stat_params):
            query['OutDetailStatParams'] = request.out_detail_stat_params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application(
        self,
        request: ens_20171110_models.DescribeApplicationRequest,
    ) -> ens_20171110_models.DescribeApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_application_with_options(request, runtime)

    async def describe_application_async(
        self,
        request: ens_20171110_models.DescribeApplicationRequest,
    ) -> ens_20171110_models.DescribeApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_application_with_options_async(request, runtime)

    def describe_application_resource_summary_with_options(
        self,
        request: ens_20171110_models.DescribeApplicationResourceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeApplicationResourceSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationResourceSummary',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeApplicationResourceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_resource_summary_with_options_async(
        self,
        request: ens_20171110_models.DescribeApplicationResourceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeApplicationResourceSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationResourceSummary',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeApplicationResourceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_resource_summary(
        self,
        request: ens_20171110_models.DescribeApplicationResourceSummaryRequest,
    ) -> ens_20171110_models.DescribeApplicationResourceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_application_resource_summary_with_options(request, runtime)

    async def describe_application_resource_summary_async(
        self,
        request: ens_20171110_models.DescribeApplicationResourceSummaryRequest,
    ) -> ens_20171110_models.DescribeApplicationResourceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_application_resource_summary_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAvailableResourceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAvailableResourceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(self) -> ens_20171110_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(runtime)

    async def describe_available_resource_async(self) -> ens_20171110_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(runtime)

    def describe_available_resource_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAvailableResourceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAvailableResourceInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeAvailableResourceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAvailableResourceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAvailableResourceInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeAvailableResourceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource_info(self) -> ens_20171110_models.DescribeAvailableResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_info_with_options(runtime)

    async def describe_available_resource_info_async(self) -> ens_20171110_models.DescribeAvailableResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_info_with_options_async(runtime)

    def describe_band_withd_charge_type_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeBandWithdChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeBandWithdChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_band_withd_charge_type_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeBandWithdChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeBandWithdChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_band_withd_charge_type(self) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_band_withd_charge_type_with_options(runtime)

    async def describe_band_withd_charge_type_async(self) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_band_withd_charge_type_with_options_async(runtime)

    def describe_bandwitdh_by_internet_charge_type_with_options(
        self,
        request: ens_20171110_models.DescribeBandwitdhByInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwitdhByInternetChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bandwitdh_by_internet_charge_type_with_options_async(
        self,
        request: ens_20171110_models.DescribeBandwitdhByInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBandwitdhByInternetChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bandwitdh_by_internet_charge_type(
        self,
        request: ens_20171110_models.DescribeBandwitdhByInternetChargeTypeRequest,
    ) -> ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwitdh_by_internet_charge_type_with_options(request, runtime)

    async def describe_bandwitdh_by_internet_charge_type_async(
        self,
        request: ens_20171110_models.DescribeBandwitdhByInternetChargeTypeRequest,
    ) -> ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bandwitdh_by_internet_charge_type_with_options_async(request, runtime)

    def describe_cloud_disk_available_resource_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCloudDiskAvailableResourceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCloudDiskAvailableResourceInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeCloudDiskAvailableResourceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_disk_available_resource_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCloudDiskAvailableResourceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCloudDiskAvailableResourceInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeCloudDiskAvailableResourceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_disk_available_resource_info(self) -> ens_20171110_models.DescribeCloudDiskAvailableResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_disk_available_resource_info_with_options(runtime)

    async def describe_cloud_disk_available_resource_info_async(self) -> ens_20171110_models.DescribeCloudDiskAvailableResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_disk_available_resource_info_with_options_async(runtime)

    def describe_cloud_disk_types_with_options(
        self,
        request: ens_20171110_models.DescribeCloudDiskTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCloudDiskTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudDiskTypes',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeCloudDiskTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_disk_types_with_options_async(
        self,
        request: ens_20171110_models.DescribeCloudDiskTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCloudDiskTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudDiskTypes',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeCloudDiskTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_disk_types(
        self,
        request: ens_20171110_models.DescribeCloudDiskTypesRequest,
    ) -> ens_20171110_models.DescribeCloudDiskTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_disk_types_with_options(request, runtime)

    async def describe_cloud_disk_types_async(
        self,
        request: ens_20171110_models.DescribeCloudDiskTypesRequest,
    ) -> ens_20171110_models.DescribeCloudDiskTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_disk_types_with_options_async(request, runtime)

    def describe_create_pre_paid_instance_result_with_options(
        self,
        request: ens_20171110_models.DescribeCreatePrePaidInstanceResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCreatePrePaidInstanceResult',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_create_pre_paid_instance_result_with_options_async(
        self,
        request: ens_20171110_models.DescribeCreatePrePaidInstanceResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCreatePrePaidInstanceResult',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_create_pre_paid_instance_result(
        self,
        request: ens_20171110_models.DescribeCreatePrePaidInstanceResultRequest,
    ) -> ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_create_pre_paid_instance_result_with_options(request, runtime)

    async def describe_create_pre_paid_instance_result_async(
        self,
        request: ens_20171110_models.DescribeCreatePrePaidInstanceResultRequest,
    ) -> ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_create_pre_paid_instance_result_with_options_async(request, runtime)

    def describe_data_dist_result_with_options(
        self,
        tmp_req: ens_20171110_models.DescribeDataDistResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataDistResultResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribeDataDistResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ens_region_ids):
            request.ens_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ens_region_ids, 'EnsRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data_names):
            query['DataNames'] = request.data_names
        if not UtilClient.is_unset(request.data_versions):
            query['DataVersions'] = request.data_versions
        if not UtilClient.is_unset(request.ens_region_ids_shrink):
            query['EnsRegionIds'] = request.ens_region_ids_shrink
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataDistResult',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDataDistResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_dist_result_with_options_async(
        self,
        tmp_req: ens_20171110_models.DescribeDataDistResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataDistResultResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribeDataDistResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ens_region_ids):
            request.ens_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ens_region_ids, 'EnsRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data_names):
            query['DataNames'] = request.data_names
        if not UtilClient.is_unset(request.data_versions):
            query['DataVersions'] = request.data_versions
        if not UtilClient.is_unset(request.ens_region_ids_shrink):
            query['EnsRegionIds'] = request.ens_region_ids_shrink
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataDistResult',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDataDistResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_dist_result(
        self,
        request: ens_20171110_models.DescribeDataDistResultRequest,
    ) -> ens_20171110_models.DescribeDataDistResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_dist_result_with_options(request, runtime)

    async def describe_data_dist_result_async(
        self,
        request: ens_20171110_models.DescribeDataDistResultRequest,
    ) -> ens_20171110_models.DescribeDataDistResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_dist_result_with_options_async(request, runtime)

    def describe_data_download_urlwith_options(
        self,
        request: ens_20171110_models.DescribeDataDownloadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataDownloadURLResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataDownloadURL',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDataDownloadURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_download_urlwith_options_async(
        self,
        request: ens_20171110_models.DescribeDataDownloadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataDownloadURLResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataDownloadURL',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDataDownloadURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_download_url(
        self,
        request: ens_20171110_models.DescribeDataDownloadURLRequest,
    ) -> ens_20171110_models.DescribeDataDownloadURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_download_urlwith_options(request, runtime)

    async def describe_data_download_url_async(
        self,
        request: ens_20171110_models.DescribeDataDownloadURLRequest,
    ) -> ens_20171110_models.DescribeDataDownloadURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_download_urlwith_options_async(request, runtime)

    def describe_data_push_result_with_options(
        self,
        request: ens_20171110_models.DescribeDataPushResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataPushResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data_names):
            query['DataNames'] = request.data_names
        if not UtilClient.is_unset(request.data_versions):
            query['DataVersions'] = request.data_versions
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_ids):
            query['RegionIds'] = request.region_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataPushResult',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDataPushResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_push_result_with_options_async(
        self,
        request: ens_20171110_models.DescribeDataPushResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataPushResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data_names):
            query['DataNames'] = request.data_names
        if not UtilClient.is_unset(request.data_versions):
            query['DataVersions'] = request.data_versions
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_ids):
            query['RegionIds'] = request.region_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataPushResult',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDataPushResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_push_result(
        self,
        request: ens_20171110_models.DescribeDataPushResultRequest,
    ) -> ens_20171110_models.DescribeDataPushResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_push_result_with_options(request, runtime)

    async def describe_data_push_result_async(
        self,
        request: ens_20171110_models.DescribeDataPushResultRequest,
    ) -> ens_20171110_models.DescribeDataPushResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_push_result_with_options_async(request, runtime)

    def describe_device_service_with_options(
        self,
        request: ens_20171110_models.DescribeDeviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDeviceServiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceService',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDeviceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_service_with_options_async(
        self,
        request: ens_20171110_models.DescribeDeviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDeviceServiceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceService',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDeviceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_service(
        self,
        request: ens_20171110_models.DescribeDeviceServiceRequest,
    ) -> ens_20171110_models.DescribeDeviceServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_service_with_options(request, runtime)

    async def describe_device_service_async(
        self,
        request: ens_20171110_models.DescribeDeviceServiceRequest,
    ) -> ens_20171110_models.DescribeDeviceServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_service_with_options_async(request, runtime)

    def describe_disks_with_options(
        self,
        request: ens_20171110_models.DescribeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.disk_charge_type):
            query['DiskChargeType'] = request.disk_charge_type
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.ens_region_ids):
            query['EnsRegionIds'] = request.ens_region_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDisks',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disks_with_options_async(
        self,
        request: ens_20171110_models.DescribeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDisksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.disk_charge_type):
            query['DiskChargeType'] = request.disk_charge_type
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.disk_ids):
            query['DiskIds'] = request.disk_ids
        if not UtilClient.is_unset(request.disk_name):
            query['DiskName'] = request.disk_name
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.ens_region_ids):
            query['EnsRegionIds'] = request.ens_region_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDisks',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disks(
        self,
        request: ens_20171110_models.DescribeDisksRequest,
    ) -> ens_20171110_models.DescribeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_with_options(request, runtime)

    async def describe_disks_async(
        self,
        request: ens_20171110_models.DescribeDisksRequest,
    ) -> ens_20171110_models.DescribeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disks_with_options_async(request, runtime)

    def describe_eip_addresses_with_options(
        self,
        request: ens_20171110_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eips):
            query['Eips'] = request.eips
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEipAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEipAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eip_addresses_with_options_async(
        self,
        request: ens_20171110_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eips):
            query['Eips'] = request.eips
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEipAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEipAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eip_addresses(
        self,
        request: ens_20171110_models.DescribeEipAddressesRequest,
    ) -> ens_20171110_models.DescribeEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_addresses_with_options(request, runtime)

    async def describe_eip_addresses_async(
        self,
        request: ens_20171110_models.DescribeEipAddressesRequest,
    ) -> ens_20171110_models.DescribeEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_addresses_with_options_async(request, runtime)

    def describe_elb_available_resource_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeElbAvailableResourceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeElbAvailableResourceInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeElbAvailableResourceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elb_available_resource_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeElbAvailableResourceInfoResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeElbAvailableResourceInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeElbAvailableResourceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elb_available_resource_info(self) -> ens_20171110_models.DescribeElbAvailableResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_elb_available_resource_info_with_options(runtime)

    async def describe_elb_available_resource_info_async(self) -> ens_20171110_models.DescribeElbAvailableResourceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_elb_available_resource_info_with_options_async(runtime)

    def describe_ens_commodity_code_with_options(
        self,
        request: ens_20171110_models.DescribeEnsCommodityCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsCommodityCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsCommodityCode',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsCommodityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_commodity_code_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsCommodityCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsCommodityCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsCommodityCode',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsCommodityCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_commodity_code(
        self,
        request: ens_20171110_models.DescribeEnsCommodityCodeRequest,
    ) -> ens_20171110_models.DescribeEnsCommodityCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_commodity_code_with_options(request, runtime)

    async def describe_ens_commodity_code_async(
        self,
        request: ens_20171110_models.DescribeEnsCommodityCodeRequest,
    ) -> ens_20171110_models.DescribeEnsCommodityCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_commodity_code_with_options_async(request, runtime)

    def describe_ens_commodity_module_code_with_options(
        self,
        request: ens_20171110_models.DescribeEnsCommodityModuleCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsCommodityModuleCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.module_code):
            query['ModuleCode'] = request.module_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsCommodityModuleCode',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsCommodityModuleCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_commodity_module_code_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsCommodityModuleCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsCommodityModuleCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.module_code):
            query['ModuleCode'] = request.module_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsCommodityModuleCode',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsCommodityModuleCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_commodity_module_code(
        self,
        request: ens_20171110_models.DescribeEnsCommodityModuleCodeRequest,
    ) -> ens_20171110_models.DescribeEnsCommodityModuleCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_commodity_module_code_with_options(request, runtime)

    async def describe_ens_commodity_module_code_async(
        self,
        request: ens_20171110_models.DescribeEnsCommodityModuleCodeRequest,
    ) -> ens_20171110_models.DescribeEnsCommodityModuleCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_commodity_module_code_with_options_async(request, runtime)

    def describe_ens_eip_addresses_with_options(
        self,
        request: ens_20171110_models.DescribeEnsEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsEipAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.associated_instance_id):
            query['AssociatedInstanceId'] = request.associated_instance_id
        if not UtilClient.is_unset(request.associated_instance_type):
            query['AssociatedInstanceType'] = request.associated_instance_type
        if not UtilClient.is_unset(request.eip_address):
            query['EipAddress'] = request.eip_address
        if not UtilClient.is_unset(request.eip_name):
            query['EipName'] = request.eip_name
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.standby):
            query['Standby'] = request.standby
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsEipAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsEipAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_eip_addresses_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsEipAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.associated_instance_id):
            query['AssociatedInstanceId'] = request.associated_instance_id
        if not UtilClient.is_unset(request.associated_instance_type):
            query['AssociatedInstanceType'] = request.associated_instance_type
        if not UtilClient.is_unset(request.eip_address):
            query['EipAddress'] = request.eip_address
        if not UtilClient.is_unset(request.eip_name):
            query['EipName'] = request.eip_name
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.standby):
            query['Standby'] = request.standby
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsEipAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsEipAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_eip_addresses(
        self,
        request: ens_20171110_models.DescribeEnsEipAddressesRequest,
    ) -> ens_20171110_models.DescribeEnsEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_eip_addresses_with_options(request, runtime)

    async def describe_ens_eip_addresses_async(
        self,
        request: ens_20171110_models.DescribeEnsEipAddressesRequest,
    ) -> ens_20171110_models.DescribeEnsEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_eip_addresses_with_options_async(request, runtime)

    def describe_ens_net_district_with_options(
        self,
        request: ens_20171110_models.DescribeEnsNetDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetDistrictResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.net_district_code):
            query['NetDistrictCode'] = request.net_district_code
        if not UtilClient.is_unset(request.net_level_code):
            query['NetLevelCode'] = request.net_level_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsNetDistrict',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsNetDistrictResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_net_district_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsNetDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetDistrictResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.net_district_code):
            query['NetDistrictCode'] = request.net_district_code
        if not UtilClient.is_unset(request.net_level_code):
            query['NetLevelCode'] = request.net_level_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsNetDistrict',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsNetDistrictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_net_district(
        self,
        request: ens_20171110_models.DescribeEnsNetDistrictRequest,
    ) -> ens_20171110_models.DescribeEnsNetDistrictResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_net_district_with_options(request, runtime)

    async def describe_ens_net_district_async(
        self,
        request: ens_20171110_models.DescribeEnsNetDistrictRequest,
    ) -> ens_20171110_models.DescribeEnsNetDistrictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_net_district_with_options_async(request, runtime)

    def describe_ens_net_level_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEnsNetLevel',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsNetLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_net_level_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeEnsNetLevel',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsNetLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_net_level(self) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_net_level_with_options(runtime)

    async def describe_ens_net_level_async(self) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_net_level_with_options_async(runtime)

    def describe_ens_net_sale_district_with_options(
        self,
        request: ens_20171110_models.DescribeEnsNetSaleDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetSaleDistrictResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.net_district_code):
            query['NetDistrictCode'] = request.net_district_code
        if not UtilClient.is_unset(request.net_level_code):
            query['NetLevelCode'] = request.net_level_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsNetSaleDistrict',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsNetSaleDistrictResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_net_sale_district_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsNetSaleDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetSaleDistrictResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.net_district_code):
            query['NetDistrictCode'] = request.net_district_code
        if not UtilClient.is_unset(request.net_level_code):
            query['NetLevelCode'] = request.net_level_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsNetSaleDistrict',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsNetSaleDistrictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_net_sale_district(
        self,
        request: ens_20171110_models.DescribeEnsNetSaleDistrictRequest,
    ) -> ens_20171110_models.DescribeEnsNetSaleDistrictResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_net_sale_district_with_options(request, runtime)

    async def describe_ens_net_sale_district_async(
        self,
        request: ens_20171110_models.DescribeEnsNetSaleDistrictRequest,
    ) -> ens_20171110_models.DescribeEnsNetSaleDistrictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_net_sale_district_with_options_async(request, runtime)

    def describe_ens_region_id_ipv_6info_with_options(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdIpv6InfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRegionIdIpv6Info',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_region_id_ipv_6info_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdIpv6InfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRegionIdIpv6Info',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_region_id_ipv_6info(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdIpv6InfoRequest,
    ) -> ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_region_id_ipv_6info_with_options(request, runtime)

    async def describe_ens_region_id_ipv_6info_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdIpv6InfoRequest,
    ) -> ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_region_id_ipv_6info_with_options_async(request, runtime)

    def describe_ens_region_id_resource_with_options(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionIdResourceResponse:
        """
        ***\
        
        @param request: DescribeEnsRegionIdResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnsRegionIdResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRegionIdResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRegionIdResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_region_id_resource_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionIdResourceResponse:
        """
        ***\
        
        @param request: DescribeEnsRegionIdResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEnsRegionIdResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRegionIdResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRegionIdResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_region_id_resource(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdResourceRequest,
    ) -> ens_20171110_models.DescribeEnsRegionIdResourceResponse:
        """
        ***\
        
        @param request: DescribeEnsRegionIdResourceRequest
        @return: DescribeEnsRegionIdResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_region_id_resource_with_options(request, runtime)

    async def describe_ens_region_id_resource_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdResourceRequest,
    ) -> ens_20171110_models.DescribeEnsRegionIdResourceResponse:
        """
        ***\
        
        @param request: DescribeEnsRegionIdResourceRequest
        @return: DescribeEnsRegionIdResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_region_id_resource_with_options_async(request, runtime)

    def describe_ens_regions_with_options(
        self,
        request: ens_20171110_models.DescribeEnsRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRegions',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_regions_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRegions',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_regions(
        self,
        request: ens_20171110_models.DescribeEnsRegionsRequest,
    ) -> ens_20171110_models.DescribeEnsRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_regions_with_options(request, runtime)

    async def describe_ens_regions_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionsRequest,
    ) -> ens_20171110_models.DescribeEnsRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_regions_with_options_async(request, runtime)

    def describe_ens_resource_usage_with_options(
        self,
        request: ens_20171110_models.DescribeEnsResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsResourceUsageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsResourceUsage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_resource_usage_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsResourceUsageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsResourceUsage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_resource_usage(
        self,
        request: ens_20171110_models.DescribeEnsResourceUsageRequest,
    ) -> ens_20171110_models.DescribeEnsResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_resource_usage_with_options(request, runtime)

    async def describe_ens_resource_usage_async(
        self,
        request: ens_20171110_models.DescribeEnsResourceUsageRequest,
    ) -> ens_20171110_models.DescribeEnsResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_resource_usage_with_options_async(request, runtime)

    def describe_ens_route_entry_list_with_options(
        self,
        request: ens_20171110_models.DescribeEnsRouteEntryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRouteEntryListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.next_hop_id):
            query['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.route_entry_id):
            query['RouteEntryId'] = request.route_entry_id
        if not UtilClient.is_unset(request.route_entry_name):
            query['RouteEntryName'] = request.route_entry_name
        if not UtilClient.is_unset(request.route_entry_type):
            query['RouteEntryType'] = request.route_entry_type
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRouteEntryList',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRouteEntryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_route_entry_list_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsRouteEntryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRouteEntryListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            query['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.next_hop_id):
            query['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            query['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.route_entry_id):
            query['RouteEntryId'] = request.route_entry_id
        if not UtilClient.is_unset(request.route_entry_name):
            query['RouteEntryName'] = request.route_entry_name
        if not UtilClient.is_unset(request.route_entry_type):
            query['RouteEntryType'] = request.route_entry_type
        if not UtilClient.is_unset(request.route_table_id):
            query['RouteTableId'] = request.route_table_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsRouteEntryList',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsRouteEntryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_route_entry_list(
        self,
        request: ens_20171110_models.DescribeEnsRouteEntryListRequest,
    ) -> ens_20171110_models.DescribeEnsRouteEntryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_route_entry_list_with_options(request, runtime)

    async def describe_ens_route_entry_list_async(
        self,
        request: ens_20171110_models.DescribeEnsRouteEntryListRequest,
    ) -> ens_20171110_models.DescribeEnsRouteEntryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_route_entry_list_with_options_async(request, runtime)

    def describe_ens_sale_control_with_options(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsSaleControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.custom_account):
            query['CustomAccount'] = request.custom_account
        if not UtilClient.is_unset(request.module_code):
            query['ModuleCode'] = request.module_code
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsSaleControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_sale_control_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsSaleControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.custom_account):
            query['CustomAccount'] = request.custom_account
        if not UtilClient.is_unset(request.module_code):
            query['ModuleCode'] = request.module_code
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsSaleControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_sale_control(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlRequest,
    ) -> ens_20171110_models.DescribeEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_sale_control_with_options(request, runtime)

    async def describe_ens_sale_control_async(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlRequest,
    ) -> ens_20171110_models.DescribeEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_sale_control_with_options_async(request, runtime)

    def describe_ens_sale_control_available_resource_with_options(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsSaleControlAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.custom_account):
            query['CustomAccount'] = request.custom_account
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsSaleControlAvailableResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsSaleControlAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_sale_control_available_resource_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsSaleControlAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.custom_account):
            query['CustomAccount'] = request.custom_account
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsSaleControlAvailableResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsSaleControlAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_sale_control_available_resource(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlAvailableResourceRequest,
    ) -> ens_20171110_models.DescribeEnsSaleControlAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_sale_control_available_resource_with_options(request, runtime)

    async def describe_ens_sale_control_available_resource_async(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlAvailableResourceRequest,
    ) -> ens_20171110_models.DescribeEnsSaleControlAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_sale_control_available_resource_with_options_async(request, runtime)

    def describe_ens_sale_control_stock_with_options(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsSaleControlStockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.custom_account):
            query['CustomAccount'] = request.custom_account
        if not UtilClient.is_unset(request.module_code):
            query['ModuleCode'] = request.module_code
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsSaleControlStock',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsSaleControlStockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ens_sale_control_stock_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsSaleControlStockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.custom_account):
            query['CustomAccount'] = request.custom_account
        if not UtilClient.is_unset(request.module_code):
            query['ModuleCode'] = request.module_code
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnsSaleControlStock',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEnsSaleControlStockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ens_sale_control_stock(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlStockRequest,
    ) -> ens_20171110_models.DescribeEnsSaleControlStockResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_sale_control_stock_with_options(request, runtime)

    async def describe_ens_sale_control_stock_async(
        self,
        request: ens_20171110_models.DescribeEnsSaleControlStockRequest,
    ) -> ens_20171110_models.DescribeEnsSaleControlStockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_sale_control_stock_with_options_async(request, runtime)

    def describe_epn_band_width_data_with_options(
        self,
        request: ens_20171110_models.DescribeEpnBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnBandWidthDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnBandWidthData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnBandWidthDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_epn_band_width_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnBandWidthDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnBandWidthData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnBandWidthDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_epn_band_width_data(
        self,
        request: ens_20171110_models.DescribeEpnBandWidthDataRequest,
    ) -> ens_20171110_models.DescribeEpnBandWidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_band_width_data_with_options(request, runtime)

    async def describe_epn_band_width_data_async(
        self,
        request: ens_20171110_models.DescribeEpnBandWidthDataRequest,
    ) -> ens_20171110_models.DescribeEpnBandWidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_epn_band_width_data_with_options_async(request, runtime)

    def describe_epn_bandwitdh_by_internet_charge_type_with_options(
        self,
        request: ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnBandwitdhByInternetChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_epn_bandwitdh_by_internet_charge_type_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnBandwitdhByInternetChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_epn_bandwitdh_by_internet_charge_type(
        self,
        request: ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeRequest,
    ) -> ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_bandwitdh_by_internet_charge_type_with_options(request, runtime)

    async def describe_epn_bandwitdh_by_internet_charge_type_async(
        self,
        request: ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeRequest,
    ) -> ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_epn_bandwitdh_by_internet_charge_type_with_options_async(request, runtime)

    def describe_epn_instance_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeEpnInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnInstanceAttributeResponse:
        """
        In internal networking mode, the value of Instances is empty in the response. In public networking mode, the value of VSwitches is empty in the response.
        
        @param request: DescribeEpnInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEpnInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnInstanceAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_epn_instance_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnInstanceAttributeResponse:
        """
        In internal networking mode, the value of Instances is empty in the response. In public networking mode, the value of VSwitches is empty in the response.
        
        @param request: DescribeEpnInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEpnInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnInstanceAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_epn_instance_attribute(
        self,
        request: ens_20171110_models.DescribeEpnInstanceAttributeRequest,
    ) -> ens_20171110_models.DescribeEpnInstanceAttributeResponse:
        """
        In internal networking mode, the value of Instances is empty in the response. In public networking mode, the value of VSwitches is empty in the response.
        
        @param request: DescribeEpnInstanceAttributeRequest
        @return: DescribeEpnInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_instance_attribute_with_options(request, runtime)

    async def describe_epn_instance_attribute_async(
        self,
        request: ens_20171110_models.DescribeEpnInstanceAttributeRequest,
    ) -> ens_20171110_models.DescribeEpnInstanceAttributeResponse:
        """
        In internal networking mode, the value of Instances is empty in the response. In public networking mode, the value of VSwitches is empty in the response.
        
        @param request: DescribeEpnInstanceAttributeRequest
        @return: DescribeEpnInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_epn_instance_attribute_with_options_async(request, runtime)

    def describe_epn_instances_with_options(
        self,
        request: ens_20171110_models.DescribeEpnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.epninstance_name):
            query['EPNInstanceName'] = request.epninstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_epn_instances_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.epninstance_name):
            query['EPNInstanceName'] = request.epninstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_epn_instances(
        self,
        request: ens_20171110_models.DescribeEpnInstancesRequest,
    ) -> ens_20171110_models.DescribeEpnInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_instances_with_options(request, runtime)

    async def describe_epn_instances_async(
        self,
        request: ens_20171110_models.DescribeEpnInstancesRequest,
    ) -> ens_20171110_models.DescribeEpnInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_epn_instances_with_options_async(request, runtime)

    def describe_epn_measurement_data_with_options(
        self,
        request: ens_20171110_models.DescribeEpnMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnMeasurementDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnMeasurementData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnMeasurementDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_epn_measurement_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnMeasurementDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEpnMeasurementData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeEpnMeasurementDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_epn_measurement_data(
        self,
        request: ens_20171110_models.DescribeEpnMeasurementDataRequest,
    ) -> ens_20171110_models.DescribeEpnMeasurementDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_measurement_data_with_options(request, runtime)

    async def describe_epn_measurement_data_async(
        self,
        request: ens_20171110_models.DescribeEpnMeasurementDataRequest,
    ) -> ens_20171110_models.DescribeEpnMeasurementDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_epn_measurement_data_with_options_async(request, runtime)

    def describe_export_image_info_with_options(
        self,
        request: ens_20171110_models.DescribeExportImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeExportImageInfoResponse:
        """
        You can call this operation to query information about all custom images in your account. The information include the image properties, image export status, and the Object Storage Service (OSS) download links.
        *   Empty strings are returned for images that are not exported.
        *   The download links may become invalid if you delete objects in OSS.
        
        @param request: DescribeExportImageInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExportImageInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportImageInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeExportImageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_export_image_info_with_options_async(
        self,
        request: ens_20171110_models.DescribeExportImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeExportImageInfoResponse:
        """
        You can call this operation to query information about all custom images in your account. The information include the image properties, image export status, and the Object Storage Service (OSS) download links.
        *   Empty strings are returned for images that are not exported.
        *   The download links may become invalid if you delete objects in OSS.
        
        @param request: DescribeExportImageInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExportImageInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportImageInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeExportImageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_export_image_info(
        self,
        request: ens_20171110_models.DescribeExportImageInfoRequest,
    ) -> ens_20171110_models.DescribeExportImageInfoResponse:
        """
        You can call this operation to query information about all custom images in your account. The information include the image properties, image export status, and the Object Storage Service (OSS) download links.
        *   Empty strings are returned for images that are not exported.
        *   The download links may become invalid if you delete objects in OSS.
        
        @param request: DescribeExportImageInfoRequest
        @return: DescribeExportImageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_export_image_info_with_options(request, runtime)

    async def describe_export_image_info_async(
        self,
        request: ens_20171110_models.DescribeExportImageInfoRequest,
    ) -> ens_20171110_models.DescribeExportImageInfoResponse:
        """
        You can call this operation to query information about all custom images in your account. The information include the image properties, image export status, and the Object Storage Service (OSS) download links.
        *   Empty strings are returned for images that are not exported.
        *   The download links may become invalid if you delete objects in OSS.
        
        @param request: DescribeExportImageInfoRequest
        @return: DescribeExportImageInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_export_image_info_with_options_async(request, runtime)

    def describe_export_image_status_with_options(
        self,
        request: ens_20171110_models.DescribeExportImageStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeExportImageStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportImageStatus',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeExportImageStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_export_image_status_with_options_async(
        self,
        request: ens_20171110_models.DescribeExportImageStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeExportImageStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportImageStatus',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeExportImageStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_export_image_status(
        self,
        request: ens_20171110_models.DescribeExportImageStatusRequest,
    ) -> ens_20171110_models.DescribeExportImageStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_export_image_status_with_options(request, runtime)

    async def describe_export_image_status_async(
        self,
        request: ens_20171110_models.DescribeExportImageStatusRequest,
    ) -> ens_20171110_models.DescribeExportImageStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_export_image_status_with_options_async(request, runtime)

    def describe_file_systems_with_options(
        self,
        request: ens_20171110_models.DescribeFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeFileSystemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystems',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_systems_with_options_async(
        self,
        request: ens_20171110_models.DescribeFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeFileSystemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystems',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_systems(
        self,
        request: ens_20171110_models.DescribeFileSystemsRequest,
    ) -> ens_20171110_models.DescribeFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_file_systems_with_options(request, runtime)

    async def describe_file_systems_async(
        self,
        request: ens_20171110_models.DescribeFileSystemsRequest,
    ) -> ens_20171110_models.DescribeFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_systems_with_options_async(request, runtime)

    def describe_forward_table_entries_with_options(
        self,
        request: ens_20171110_models.DescribeForwardTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeForwardTableEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        if not UtilClient.is_unset(request.forward_entry_name):
            query['ForwardEntryName'] = request.forward_entry_name
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeForwardTableEntries',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeForwardTableEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_forward_table_entries_with_options_async(
        self,
        request: ens_20171110_models.DescribeForwardTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeForwardTableEntriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ip):
            query['ExternalIp'] = request.external_ip
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        if not UtilClient.is_unset(request.forward_entry_name):
            query['ForwardEntryName'] = request.forward_entry_name
        if not UtilClient.is_unset(request.internal_ip):
            query['InternalIp'] = request.internal_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeForwardTableEntries',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeForwardTableEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_forward_table_entries(
        self,
        request: ens_20171110_models.DescribeForwardTableEntriesRequest,
    ) -> ens_20171110_models.DescribeForwardTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_forward_table_entries_with_options(request, runtime)

    async def describe_forward_table_entries_async(
        self,
        request: ens_20171110_models.DescribeForwardTableEntriesRequest,
    ) -> ens_20171110_models.DescribeForwardTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_forward_table_entries_with_options_async(request, runtime)

    def describe_image_infos_with_options(
        self,
        request: ens_20171110_models.DescribeImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImageInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageInfos',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeImageInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_infos_with_options_async(
        self,
        request: ens_20171110_models.DescribeImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImageInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageInfos',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeImageInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_infos(
        self,
        request: ens_20171110_models.DescribeImageInfosRequest,
    ) -> ens_20171110_models.DescribeImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_infos_with_options(request, runtime)

    async def describe_image_infos_async(
        self,
        request: ens_20171110_models.DescribeImageInfosRequest,
    ) -> ens_20171110_models.DescribeImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_infos_with_options_async(request, runtime)

    def describe_image_share_permission_with_options(
        self,
        request: ens_20171110_models.DescribeImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImageSharePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_id):
            query['AliyunId'] = request.aliyun_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageSharePermission',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeImageSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_share_permission_with_options_async(
        self,
        request: ens_20171110_models.DescribeImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImageSharePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_id):
            query['AliyunId'] = request.aliyun_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageSharePermission',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeImageSharePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_share_permission(
        self,
        request: ens_20171110_models.DescribeImageSharePermissionRequest,
    ) -> ens_20171110_models.DescribeImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_share_permission_with_options(request, runtime)

    async def describe_image_share_permission_async(
        self,
        request: ens_20171110_models.DescribeImageSharePermissionRequest,
    ) -> ens_20171110_models.DescribeImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_share_permission_with_options_async(request, runtime)

    def describe_images_with_options(
        self,
        request: ens_20171110_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImages',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_images_with_options_async(
        self,
        request: ens_20171110_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImages',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_images(
        self,
        request: ens_20171110_models.DescribeImagesRequest,
    ) -> ens_20171110_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    async def describe_images_async(
        self,
        request: ens_20171110_models.DescribeImagesRequest,
    ) -> ens_20171110_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_images_with_options_async(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auto_renew_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAutoRenewAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auto_renew_attribute(
        self,
        request: ens_20171110_models.DescribeInstanceAutoRenewAttributeRequest,
    ) -> ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    async def describe_instance_auto_renew_attribute_async(
        self,
        request: ens_20171110_models.DescribeInstanceAutoRenewAttributeRequest,
    ) -> ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renew_attribute_with_options_async(request, runtime)

    def describe_instance_monitor_data_with_options(
        self,
        request: ens_20171110_models.DescribeInstanceMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceMonitorData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_monitor_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceMonitorDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceMonitorData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_monitor_data(
        self,
        request: ens_20171110_models.DescribeInstanceMonitorDataRequest,
    ) -> ens_20171110_models.DescribeInstanceMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_monitor_data_with_options(request, runtime)

    async def describe_instance_monitor_data_async(
        self,
        request: ens_20171110_models.DescribeInstanceMonitorDataRequest,
    ) -> ens_20171110_models.DescribeInstanceMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_monitor_data_with_options_async(request, runtime)

    def describe_instance_spec_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceSpecResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstanceSpec',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_spec_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceSpecResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstanceSpec',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_spec(self) -> ens_20171110_models.DescribeInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_spec_with_options(runtime)

    async def describe_instance_spec_async(self) -> ens_20171110_models.DescribeInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_spec_with_options_async(runtime)

    def describe_instance_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeInstanceTypes',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_types(self) -> ens_20171110_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(runtime)

    async def describe_instance_types_async(self) -> ens_20171110_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_types_with_options_async(runtime)

    def describe_instance_vnc_url_with_options(
        self,
        request: ens_20171110_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceVncUrl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceVncUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_vnc_url_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceVncUrl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstanceVncUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_vnc_url(
        self,
        request: ens_20171110_models.DescribeInstanceVncUrlRequest,
    ) -> ens_20171110_models.DescribeInstanceVncUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_url_with_options(request, runtime)

    async def describe_instance_vnc_url_async(
        self,
        request: ens_20171110_models.DescribeInstanceVncUrlRequest,
    ) -> ens_20171110_models.DescribeInstanceVncUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_vnc_url_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        tmp_req: ens_20171110_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstancesResponse:
        """
        You can call this operation up to 800 times per second per account.
        *   You can call this operation up to 100 times per second per user.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions. However, if InstanceIds is set to an empty JSON array, it is regarded as a valid filter condition and an empty result is returned.
        
        @param tmp_req: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribeInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.ens_region_ids):
            query['EnsRegionIds'] = request.ens_region_ids
        if not UtilClient.is_unset(request.ens_service_id):
            query['EnsServiceId'] = request.ens_service_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_resource_type):
            query['InstanceResourceType'] = request.instance_resource_type
        if not UtilClient.is_unset(request.intranet_ip):
            query['IntranetIp'] = request.intranet_ip
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        tmp_req: ens_20171110_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstancesResponse:
        """
        You can call this operation up to 800 times per second per account.
        *   You can call this operation up to 100 times per second per user.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions. However, if InstanceIds is set to an empty JSON array, it is regarded as a valid filter condition and an empty result is returned.
        
        @param tmp_req: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribeInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.ens_region_ids):
            query['EnsRegionIds'] = request.ens_region_ids
        if not UtilClient.is_unset(request.ens_service_id):
            query['EnsServiceId'] = request.ens_service_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_resource_type):
            query['InstanceResourceType'] = request.instance_resource_type
        if not UtilClient.is_unset(request.intranet_ip):
            query['IntranetIp'] = request.intranet_ip
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: ens_20171110_models.DescribeInstancesRequest,
    ) -> ens_20171110_models.DescribeInstancesResponse:
        """
        You can call this operation up to 800 times per second per account.
        *   You can call this operation up to 100 times per second per user.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions. However, if InstanceIds is set to an empty JSON array, it is regarded as a valid filter condition and an empty result is returned.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ens_20171110_models.DescribeInstancesRequest,
    ) -> ens_20171110_models.DescribeInstancesResponse:
        """
        You can call this operation up to 800 times per second per account.
        *   You can call this operation up to 100 times per second per user.
        *   You can specify multiple request parameters to be queried. Specified parameters are evaluated by using the AND operator. Only the specified parameters are included in the filter conditions. However, if InstanceIds is set to an empty JSON array, it is regarded as a valid filter condition and an empty result is returned.
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_key_pairs_with_options(
        self,
        request: ens_20171110_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeKeyPairsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyPairs',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_key_pairs_with_options_async(
        self,
        request: ens_20171110_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeKeyPairsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_id):
            query['KeyPairId'] = request.key_pair_id
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKeyPairs',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_key_pairs(
        self,
        request: ens_20171110_models.DescribeKeyPairsRequest,
    ) -> ens_20171110_models.DescribeKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_key_pairs_with_options(request, runtime)

    async def describe_key_pairs_async(
        self,
        request: ens_20171110_models.DescribeKeyPairsRequest,
    ) -> ens_20171110_models.DescribeKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_key_pairs_with_options_async(request, runtime)

    def describe_load_balancer_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_attribute(
        self,
        request: ens_20171110_models.DescribeLoadBalancerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerAttributeRequest
        @return: DescribeLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_attribute_with_options(request, runtime)

    async def describe_load_balancer_attribute_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerAttributeRequest
        @return: DescribeLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_attribute_with_options_async(request, runtime)

    def describe_load_balancer_httplistener_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerHTTPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerHTTPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_httplistener_attribute(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPListenerAttributeRequest
        @return: DescribeLoadBalancerHTTPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_httplistener_attribute_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPListenerAttributeRequest
        @return: DescribeLoadBalancerHTTPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_httplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancer_httpslistener_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPSListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerHTTPSListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPSListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPSListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerHTTPSListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPSListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_httpslistener_attribute(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPSListenerAttributeRequest
        @return: DescribeLoadBalancerHTTPSListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httpslistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_httpslistener_attribute_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerHTTPSListenerAttributeRequest
        @return: DescribeLoadBalancerHTTPSListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_httpslistener_attribute_with_options_async(request, runtime)

    def describe_load_balancer_spec_with_options(
        self,
        request: ens_20171110_models.DescribeLoadBalancerSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerSpecResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerSpec',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_spec_with_options_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerSpecResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerSpec',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_spec(
        self,
        request: ens_20171110_models.DescribeLoadBalancerSpecRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_spec_with_options(request, runtime)

    async def describe_load_balancer_spec_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerSpecRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_spec_with_options_async(request, runtime)

    def describe_load_balancer_tcplistener_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerTCPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerTCPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerTCPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerTCPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerTCPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerTCPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_tcplistener_attribute(
        self,
        request: ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerTCPListenerAttributeRequest
        @return: DescribeLoadBalancerTCPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_tcplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_tcplistener_attribute_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerTCPListenerAttributeRequest
        @return: DescribeLoadBalancerTCPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_tcplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancer_udplistener_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerUDPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerUDPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerUDPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerUDPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancerUDPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerUDPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancer_udplistener_attribute(
        self,
        request: ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerUDPListenerAttributeRequest
        @return: DescribeLoadBalancerUDPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_udplistener_attribute_with_options(request, runtime)

    async def describe_load_balancer_udplistener_attribute_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeRequest,
    ) -> ens_20171110_models.DescribeLoadBalancerUDPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancerUDPListenerAttributeRequest
        @return: DescribeLoadBalancerUDPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancer_udplistener_attribute_with_options_async(request, runtime)

    def describe_load_balancers_with_options(
        self,
        request: ens_20171110_models.DescribeLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancersResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_load_balancers_with_options_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeLoadBalancersResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_load_balancers(
        self,
        request: ens_20171110_models.DescribeLoadBalancersRequest,
    ) -> ens_20171110_models.DescribeLoadBalancersResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancersRequest
        @return: DescribeLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancers_with_options(request, runtime)

    async def describe_load_balancers_async(
        self,
        request: ens_20171110_models.DescribeLoadBalancersRequest,
    ) -> ens_20171110_models.DescribeLoadBalancersResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: DescribeLoadBalancersRequest
        @return: DescribeLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_load_balancers_with_options_async(request, runtime)

    def describe_measurement_data_with_options(
        self,
        request: ens_20171110_models.DescribeMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeMeasurementDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeasurementData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeMeasurementDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_measurement_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeMeasurementDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeasurementData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeMeasurementDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_measurement_data(
        self,
        request: ens_20171110_models.DescribeMeasurementDataRequest,
    ) -> ens_20171110_models.DescribeMeasurementDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_measurement_data_with_options(request, runtime)

    async def describe_measurement_data_async(
        self,
        request: ens_20171110_models.DescribeMeasurementDataRequest,
    ) -> ens_20171110_models.DescribeMeasurementDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_measurement_data_with_options_async(request, runtime)

    def describe_mount_targets_with_options(
        self,
        request: ens_20171110_models.DescribeMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeMountTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_name):
            query['MountTargetName'] = request.mount_target_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountTargets',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeMountTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mount_targets_with_options_async(
        self,
        request: ens_20171110_models.DescribeMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeMountTargetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_name):
            query['MountTargetName'] = request.mount_target_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountTargets',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeMountTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mount_targets(
        self,
        request: ens_20171110_models.DescribeMountTargetsRequest,
    ) -> ens_20171110_models.DescribeMountTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mount_targets_with_options(request, runtime)

    async def describe_mount_targets_async(
        self,
        request: ens_20171110_models.DescribeMountTargetsRequest,
    ) -> ens_20171110_models.DescribeMountTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mount_targets_with_options_async(request, runtime)

    def describe_ncinformation_with_options(
        self,
        request: ens_20171110_models.DescribeNCInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNCInformationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNCInformation',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNCInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ncinformation_with_options_async(
        self,
        request: ens_20171110_models.DescribeNCInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNCInformationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNCInformation',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNCInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ncinformation(
        self,
        request: ens_20171110_models.DescribeNCInformationRequest,
    ) -> ens_20171110_models.DescribeNCInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ncinformation_with_options(request, runtime)

    async def describe_ncinformation_async(
        self,
        request: ens_20171110_models.DescribeNCInformationRequest,
    ) -> ens_20171110_models.DescribeNCInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ncinformation_with_options_async(request, runtime)

    def describe_nat_gateways_with_options(
        self,
        request: ens_20171110_models.DescribeNatGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNatGatewaysResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatGateways',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNatGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nat_gateways_with_options_async(
        self,
        request: ens_20171110_models.DescribeNatGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNatGatewaysResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNatGateways',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNatGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nat_gateways(
        self,
        request: ens_20171110_models.DescribeNatGatewaysRequest,
    ) -> ens_20171110_models.DescribeNatGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_gateways_with_options(request, runtime)

    async def describe_nat_gateways_async(
        self,
        request: ens_20171110_models.DescribeNatGatewaysRequest,
    ) -> ens_20171110_models.DescribeNatGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_gateways_with_options_async(request, runtime)

    def describe_network_acls_with_options(
        self,
        request: ens_20171110_models.DescribeNetworkAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkAclsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkAcls',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworkAclsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_acls_with_options_async(
        self,
        request: ens_20171110_models.DescribeNetworkAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkAclsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkAcls',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworkAclsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_acls(
        self,
        request: ens_20171110_models.DescribeNetworkAclsRequest,
    ) -> ens_20171110_models.DescribeNetworkAclsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_acls_with_options(request, runtime)

    async def describe_network_acls_async(
        self,
        request: ens_20171110_models.DescribeNetworkAclsRequest,
    ) -> ens_20171110_models.DescribeNetworkAclsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_acls_with_options_async(request, runtime)

    def describe_network_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeNetworkAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworkAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworkAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeNetworkAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworkAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworkAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworkAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_attribute(
        self,
        request: ens_20171110_models.DescribeNetworkAttributeRequest,
    ) -> ens_20171110_models.DescribeNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworkAttributeRequest
        @return: DescribeNetworkAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_network_attribute_with_options(request, runtime)

    async def describe_network_attribute_async(
        self,
        request: ens_20171110_models.DescribeNetworkAttributeRequest,
    ) -> ens_20171110_models.DescribeNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworkAttributeRequest
        @return: DescribeNetworkAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_attribute_with_options_async(request, runtime)

    def describe_network_interfaces_with_options(
        self,
        request: ens_20171110_models.DescribeNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.network_interface_name):
            query['NetworkInterfaceName'] = request.network_interface_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.primary_ip_address):
            query['PrimaryIpAddress'] = request.primary_ip_address
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInterfaces',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_interfaces_with_options_async(
        self,
        request: ens_20171110_models.DescribeNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.network_interface_name):
            query['NetworkInterfaceName'] = request.network_interface_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.primary_ip_address):
            query['PrimaryIpAddress'] = request.primary_ip_address
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkInterfaces',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworkInterfacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_interfaces(
        self,
        request: ens_20171110_models.DescribeNetworkInterfacesRequest,
    ) -> ens_20171110_models.DescribeNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interfaces_with_options(request, runtime)

    async def describe_network_interfaces_async(
        self,
        request: ens_20171110_models.DescribeNetworkInterfacesRequest,
    ) -> ens_20171110_models.DescribeNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_interfaces_with_options_async(request, runtime)

    def describe_networks_with_options(
        self,
        request: ens_20171110_models.DescribeNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworksResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworks',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_networks_with_options_async(
        self,
        request: ens_20171110_models.DescribeNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworksResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetworksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworks',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeNetworksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_networks(
        self,
        request: ens_20171110_models.DescribeNetworksRequest,
    ) -> ens_20171110_models.DescribeNetworksResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworksRequest
        @return: DescribeNetworksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_networks_with_options(request, runtime)

    async def describe_networks_async(
        self,
        request: ens_20171110_models.DescribeNetworksRequest,
    ) -> ens_20171110_models.DescribeNetworksResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: DescribeNetworksRequest
        @return: DescribeNetworksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_networks_with_options_async(request, runtime)

    def describe_pre_paid_instance_stock_with_options(
        self,
        request: ens_20171110_models.DescribePrePaidInstanceStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePrePaidInstanceStockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.system_disk_size):
            query['SystemDiskSize'] = request.system_disk_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrePaidInstanceStock',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribePrePaidInstanceStockResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_paid_instance_stock_with_options_async(
        self,
        request: ens_20171110_models.DescribePrePaidInstanceStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePrePaidInstanceStockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.system_disk_size):
            query['SystemDiskSize'] = request.system_disk_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrePaidInstanceStock',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribePrePaidInstanceStockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_paid_instance_stock(
        self,
        request: ens_20171110_models.DescribePrePaidInstanceStockRequest,
    ) -> ens_20171110_models.DescribePrePaidInstanceStockResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_paid_instance_stock_with_options(request, runtime)

    async def describe_pre_paid_instance_stock_async(
        self,
        request: ens_20171110_models.DescribePrePaidInstanceStockRequest,
    ) -> ens_20171110_models.DescribePrePaidInstanceStockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_paid_instance_stock_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        tmp_req: ens_20171110_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePriceResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_disks):
            request.data_disks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_disks, 'DataDisks', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_disks_shrink):
            query['DataDisks'] = request.data_disks_shrink
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        tmp_req: ens_20171110_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePriceResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.DescribePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_disks):
            request.data_disks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_disks, 'DataDisks', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_disks_shrink):
            query['DataDisks'] = request.data_disks_shrink
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.data_disk):
            query['DataDisk'] = request.data_disk
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: ens_20171110_models.DescribePriceRequest,
    ) -> ens_20171110_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: ens_20171110_models.DescribePriceRequest,
    ) -> ens_20171110_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_region_isps_with_options(
        self,
        request: ens_20171110_models.DescribeRegionIspsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeRegionIspsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegionIsps',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeRegionIspsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_region_isps_with_options_async(
        self,
        request: ens_20171110_models.DescribeRegionIspsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeRegionIspsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegionIsps',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeRegionIspsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_region_isps(
        self,
        request: ens_20171110_models.DescribeRegionIspsRequest,
    ) -> ens_20171110_models.DescribeRegionIspsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_region_isps_with_options(request, runtime)

    async def describe_region_isps_async(
        self,
        request: ens_20171110_models.DescribeRegionIspsRequest,
    ) -> ens_20171110_models.DescribeRegionIspsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_region_isps_with_options_async(request, runtime)

    def describe_region_resource_with_options(
        self,
        request: ens_20171110_models.DescribeRegionResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeRegionResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegionResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeRegionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_region_resource_with_options_async(
        self,
        request: ens_20171110_models.DescribeRegionResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeRegionResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegionResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeRegionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_region_resource(
        self,
        request: ens_20171110_models.DescribeRegionResourceRequest,
    ) -> ens_20171110_models.DescribeRegionResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_region_resource_with_options(request, runtime)

    async def describe_region_resource_async(
        self,
        request: ens_20171110_models.DescribeRegionResourceRequest,
    ) -> ens_20171110_models.DescribeRegionResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_region_resource_with_options_async(request, runtime)

    def describe_reserved_resource_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeReservedResourceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeReservedResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeReservedResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reserved_resource_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeReservedResourceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeReservedResource',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeReservedResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reserved_resource(self) -> ens_20171110_models.DescribeReservedResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_resource_with_options(runtime)

    async def describe_reserved_resource_async(self) -> ens_20171110_models.DescribeReservedResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reserved_resource_with_options_async(runtime)

    def describe_resource_timeline_with_options(
        self,
        request: ens_20171110_models.DescribeResourceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeResourceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceTimeline',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeResourceTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_timeline_with_options_async(
        self,
        request: ens_20171110_models.DescribeResourceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeResourceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceTimeline',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeResourceTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_timeline(
        self,
        request: ens_20171110_models.DescribeResourceTimelineRequest,
    ) -> ens_20171110_models.DescribeResourceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_timeline_with_options(request, runtime)

    async def describe_resource_timeline_async(
        self,
        request: ens_20171110_models.DescribeResourceTimelineRequest,
    ) -> ens_20171110_models.DescribeResourceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_timeline_with_options_async(request, runtime)

    def describe_sdgdeployment_status_with_options(
        self,
        request: ens_20171110_models.DescribeSDGDeploymentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSDGDeploymentStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSDGDeploymentStatus',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSDGDeploymentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sdgdeployment_status_with_options_async(
        self,
        request: ens_20171110_models.DescribeSDGDeploymentStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSDGDeploymentStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSDGDeploymentStatus',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSDGDeploymentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sdgdeployment_status(
        self,
        request: ens_20171110_models.DescribeSDGDeploymentStatusRequest,
    ) -> ens_20171110_models.DescribeSDGDeploymentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdgdeployment_status_with_options(request, runtime)

    async def describe_sdgdeployment_status_async(
        self,
        request: ens_20171110_models.DescribeSDGDeploymentStatusRequest,
    ) -> ens_20171110_models.DescribeSDGDeploymentStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdgdeployment_status_with_options_async(request, runtime)

    def describe_security_group_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSecurityGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_group_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSecurityGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_group_attribute(
        self,
        request: ens_20171110_models.DescribeSecurityGroupAttributeRequest,
    ) -> ens_20171110_models.DescribeSecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_attribute_with_options(request, runtime)

    async def describe_security_group_attribute_async(
        self,
        request: ens_20171110_models.DescribeSecurityGroupAttributeRequest,
    ) -> ens_20171110_models.DescribeSecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_attribute_with_options_async(request, runtime)

    def describe_security_groups_with_options(
        self,
        request: ens_20171110_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroups',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_groups_with_options_async(
        self,
        request: ens_20171110_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroups',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_groups(
        self,
        request: ens_20171110_models.DescribeSecurityGroupsRequest,
    ) -> ens_20171110_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    async def describe_security_groups_async(
        self,
        request: ens_20171110_models.DescribeSecurityGroupsRequest,
    ) -> ens_20171110_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_groups_with_options_async(request, runtime)

    def describe_self_images_with_options(
        self,
        request: ens_20171110_models.DescribeSelfImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSelfImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSelfImages',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSelfImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_self_images_with_options_async(
        self,
        request: ens_20171110_models.DescribeSelfImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSelfImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSelfImages',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSelfImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_self_images(
        self,
        request: ens_20171110_models.DescribeSelfImagesRequest,
    ) -> ens_20171110_models.DescribeSelfImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_self_images_with_options(request, runtime)

    async def describe_self_images_async(
        self,
        request: ens_20171110_models.DescribeSelfImagesRequest,
    ) -> ens_20171110_models.DescribeSelfImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_self_images_with_options_async(request, runtime)

    def describe_servcie_schedule_with_options(
        self,
        request: ens_20171110_models.DescribeServcieScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeServcieScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.pod_config_name):
            query['PodConfigName'] = request.pod_config_name
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServcieSchedule',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeServcieScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_servcie_schedule_with_options_async(
        self,
        request: ens_20171110_models.DescribeServcieScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeServcieScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.pod_config_name):
            query['PodConfigName'] = request.pod_config_name
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServcieSchedule',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeServcieScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_servcie_schedule(
        self,
        request: ens_20171110_models.DescribeServcieScheduleRequest,
    ) -> ens_20171110_models.DescribeServcieScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_servcie_schedule_with_options(request, runtime)

    async def describe_servcie_schedule_async(
        self,
        request: ens_20171110_models.DescribeServcieScheduleRequest,
    ) -> ens_20171110_models.DescribeServcieScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_servcie_schedule_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: ens_20171110_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: ens_20171110_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snapshots(
        self,
        request: ens_20171110_models.DescribeSnapshotsRequest,
    ) -> ens_20171110_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: ens_20171110_models.DescribeSnapshotsRequest,
    ) -> ens_20171110_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_snat_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeSnatAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSnatAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnatAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSnatAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snat_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeSnatAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSnatAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnatAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSnatAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snat_attribute(
        self,
        request: ens_20171110_models.DescribeSnatAttributeRequest,
    ) -> ens_20171110_models.DescribeSnatAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snat_attribute_with_options(request, runtime)

    async def describe_snat_attribute_async(
        self,
        request: ens_20171110_models.DescribeSnatAttributeRequest,
    ) -> ens_20171110_models.DescribeSnatAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snat_attribute_with_options_async(request, runtime)

    def describe_snat_table_entries_with_options(
        self,
        request: ens_20171110_models.DescribeSnatTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSnatTableEntriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnatTableEntries',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSnatTableEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snat_table_entries_with_options_async(
        self,
        request: ens_20171110_models.DescribeSnatTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSnatTableEntriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnatTableEntries',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeSnatTableEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snat_table_entries(
        self,
        request: ens_20171110_models.DescribeSnatTableEntriesRequest,
    ) -> ens_20171110_models.DescribeSnatTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snat_table_entries_with_options(request, runtime)

    async def describe_snat_table_entries_async(
        self,
        request: ens_20171110_models.DescribeSnatTableEntriesRequest,
    ) -> ens_20171110_models.DescribeSnatTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snat_table_entries_with_options_async(request, runtime)

    def describe_user_band_width_data_with_options(
        self,
        request: ens_20171110_models.DescribeUserBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeUserBandWidthDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBandWidthData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeUserBandWidthDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_band_width_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeUserBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeUserBandWidthDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.isp):
            query['Isp'] = request.isp
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserBandWidthData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeUserBandWidthDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_band_width_data(
        self,
        request: ens_20171110_models.DescribeUserBandWidthDataRequest,
    ) -> ens_20171110_models.DescribeUserBandWidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_band_width_data_with_options(request, runtime)

    async def describe_user_band_width_data_async(
        self,
        request: ens_20171110_models.DescribeUserBandWidthDataRequest,
    ) -> ens_20171110_models.DescribeUserBandWidthDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_band_width_data_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: ens_20171110_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: ens_20171110_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.order_by_params):
            query['OrderByParams'] = request.order_by_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: ens_20171110_models.DescribeVSwitchesRequest,
    ) -> ens_20171110_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: ens_20171110_models.DescribeVSwitchesRequest,
    ) -> ens_20171110_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_workflow_with_options(
        self,
        request: ens_20171110_models.DescribeWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.work_flow_id):
            query['WorkFlowId'] = request.work_flow_id
        if not UtilClient.is_unset(request.work_flow_name):
            query['WorkFlowName'] = request.work_flow_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_workflow_with_options_async(
        self,
        request: ens_20171110_models.DescribeWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.work_flow_id):
            query['WorkFlowId'] = request.work_flow_id
        if not UtilClient.is_unset(request.work_flow_name):
            query['WorkFlowName'] = request.work_flow_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_workflow(
        self,
        request: ens_20171110_models.DescribeWorkflowRequest,
    ) -> ens_20171110_models.DescribeWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_workflow_with_options(request, runtime)

    async def describe_workflow_async(
        self,
        request: ens_20171110_models.DescribeWorkflowRequest,
    ) -> ens_20171110_models.DescribeWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_workflow_with_options_async(request, runtime)

    def describe_workflow_activity_with_options(
        self,
        request: ens_20171110_models.DescribeWorkflowActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeWorkflowActivityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.work_flow_id):
            query['WorkFlowId'] = request.work_flow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflowActivity',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeWorkflowActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_workflow_activity_with_options_async(
        self,
        request: ens_20171110_models.DescribeWorkflowActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeWorkflowActivityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.work_flow_id):
            query['WorkFlowId'] = request.work_flow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflowActivity',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DescribeWorkflowActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_workflow_activity(
        self,
        request: ens_20171110_models.DescribeWorkflowActivityRequest,
    ) -> ens_20171110_models.DescribeWorkflowActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_workflow_activity_with_options(request, runtime)

    async def describe_workflow_activity_async(
        self,
        request: ens_20171110_models.DescribeWorkflowActivityRequest,
    ) -> ens_20171110_models.DescribeWorkflowActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_workflow_activity_with_options_async(request, runtime)

    def detach_disk_with_options(
        self,
        request: ens_20171110_models.DetachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DetachDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DetachDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_disk_with_options_async(
        self,
        request: ens_20171110_models.DetachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DetachDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DetachDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_disk(
        self,
        request: ens_20171110_models.DetachDiskRequest,
    ) -> ens_20171110_models.DetachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_disk_with_options(request, runtime)

    async def detach_disk_async(
        self,
        request: ens_20171110_models.DetachDiskRequest,
    ) -> ens_20171110_models.DetachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_disk_with_options_async(request, runtime)

    def dist_application_data_with_options(
        self,
        request: ens_20171110_models.DistApplicationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DistApplicationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.dist_strategy):
            query['DistStrategy'] = request.dist_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DistApplicationData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DistApplicationDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def dist_application_data_with_options_async(
        self,
        request: ens_20171110_models.DistApplicationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DistApplicationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.dist_strategy):
            query['DistStrategy'] = request.dist_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DistApplicationData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.DistApplicationDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dist_application_data(
        self,
        request: ens_20171110_models.DistApplicationDataRequest,
    ) -> ens_20171110_models.DistApplicationDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.dist_application_data_with_options(request, runtime)

    async def dist_application_data_async(
        self,
        request: ens_20171110_models.DistApplicationDataRequest,
    ) -> ens_20171110_models.DistApplicationDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dist_application_data_with_options_async(request, runtime)

    def export_bill_detail_data_with_options(
        self,
        request: ens_20171110_models.ExportBillDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportBillDetailDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportBillDetailData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ExportBillDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_bill_detail_data_with_options_async(
        self,
        request: ens_20171110_models.ExportBillDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportBillDetailDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportBillDetailData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ExportBillDetailDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_bill_detail_data(
        self,
        request: ens_20171110_models.ExportBillDetailDataRequest,
    ) -> ens_20171110_models.ExportBillDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_bill_detail_data_with_options(request, runtime)

    async def export_bill_detail_data_async(
        self,
        request: ens_20171110_models.ExportBillDetailDataRequest,
    ) -> ens_20171110_models.ExportBillDetailDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_bill_detail_data_with_options_async(request, runtime)

    def export_image_with_options(
        self,
        request: ens_20171110_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.ossprefix):
            query['OSSPrefix'] = request.ossprefix
        if not UtilClient.is_unset(request.ossregion_id):
            query['OSSRegionId'] = request.ossregion_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ExportImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_image_with_options_async(
        self,
        request: ens_20171110_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.ossprefix):
            query['OSSPrefix'] = request.ossprefix
        if not UtilClient.is_unset(request.ossregion_id):
            query['OSSRegionId'] = request.ossregion_id
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ExportImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_image(
        self,
        request: ens_20171110_models.ExportImageRequest,
    ) -> ens_20171110_models.ExportImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_image_with_options(request, runtime)

    async def export_image_async(
        self,
        request: ens_20171110_models.ExportImageRequest,
    ) -> ens_20171110_models.ExportImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_image_with_options_async(request, runtime)

    def export_measurement_data_with_options(
        self,
        request: ens_20171110_models.ExportMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportMeasurementDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportMeasurementData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ExportMeasurementDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_measurement_data_with_options_async(
        self,
        request: ens_20171110_models.ExportMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportMeasurementDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportMeasurementData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ExportMeasurementDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_measurement_data(
        self,
        request: ens_20171110_models.ExportMeasurementDataRequest,
    ) -> ens_20171110_models.ExportMeasurementDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_measurement_data_with_options(request, runtime)

    async def export_measurement_data_async(
        self,
        request: ens_20171110_models.ExportMeasurementDataRequest,
    ) -> ens_20171110_models.ExportMeasurementDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_measurement_data_with_options_async(request, runtime)

    def get_bucket_acl_with_options(
        self,
        request: ens_20171110_models.GetBucketAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetBucketAclResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetBucketAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bucket_acl_with_options_async(
        self,
        request: ens_20171110_models.GetBucketAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetBucketAclResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetBucketAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bucket_acl(
        self,
        request: ens_20171110_models.GetBucketAclRequest,
    ) -> ens_20171110_models.GetBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bucket_acl_with_options(request, runtime)

    async def get_bucket_acl_async(
        self,
        request: ens_20171110_models.GetBucketAclRequest,
    ) -> ens_20171110_models.GetBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bucket_acl_with_options_async(request, runtime)

    def get_bucket_info_with_options(
        self,
        request: ens_20171110_models.GetBucketInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetBucketInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetBucketInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bucket_info_with_options_async(
        self,
        request: ens_20171110_models.GetBucketInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetBucketInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketInfo',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetBucketInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bucket_info(
        self,
        request: ens_20171110_models.GetBucketInfoRequest,
    ) -> ens_20171110_models.GetBucketInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bucket_info_with_options(request, runtime)

    async def get_bucket_info_async(
        self,
        request: ens_20171110_models.GetBucketInfoRequest,
    ) -> ens_20171110_models.GetBucketInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bucket_info_with_options_async(request, runtime)

    def get_bucket_lifecycle_with_options(
        self,
        request: ens_20171110_models.GetBucketLifecycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetBucketLifecycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketLifecycle',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetBucketLifecycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bucket_lifecycle_with_options_async(
        self,
        request: ens_20171110_models.GetBucketLifecycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetBucketLifecycleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketLifecycle',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetBucketLifecycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bucket_lifecycle(
        self,
        request: ens_20171110_models.GetBucketLifecycleRequest,
    ) -> ens_20171110_models.GetBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_bucket_lifecycle_with_options(request, runtime)

    async def get_bucket_lifecycle_async(
        self,
        request: ens_20171110_models.GetBucketLifecycleRequest,
    ) -> ens_20171110_models.GetBucketLifecycleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_bucket_lifecycle_with_options_async(request, runtime)

    def get_device_internet_port_with_options(
        self,
        request: ens_20171110_models.GetDeviceInternetPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetDeviceInternetPortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceInternetPort',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetDeviceInternetPortResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_internet_port_with_options_async(
        self,
        request: ens_20171110_models.GetDeviceInternetPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetDeviceInternetPortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceInternetPort',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetDeviceInternetPortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_internet_port(
        self,
        request: ens_20171110_models.GetDeviceInternetPortRequest,
    ) -> ens_20171110_models.GetDeviceInternetPortResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_internet_port_with_options(request, runtime)

    async def get_device_internet_port_async(
        self,
        request: ens_20171110_models.GetDeviceInternetPortRequest,
    ) -> ens_20171110_models.GetDeviceInternetPortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_internet_port_with_options_async(request, runtime)

    def get_oss_storage_and_acc_by_buckets_with_options(
        self,
        request: ens_20171110_models.GetOssStorageAndAccByBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetOssStorageAndAccByBucketsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssStorageAndAccByBuckets',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetOssStorageAndAccByBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_storage_and_acc_by_buckets_with_options_async(
        self,
        request: ens_20171110_models.GetOssStorageAndAccByBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetOssStorageAndAccByBucketsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssStorageAndAccByBuckets',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetOssStorageAndAccByBucketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_storage_and_acc_by_buckets(
        self,
        request: ens_20171110_models.GetOssStorageAndAccByBucketsRequest,
    ) -> ens_20171110_models.GetOssStorageAndAccByBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_storage_and_acc_by_buckets_with_options(request, runtime)

    async def get_oss_storage_and_acc_by_buckets_async(
        self,
        request: ens_20171110_models.GetOssStorageAndAccByBucketsRequest,
    ) -> ens_20171110_models.GetOssStorageAndAccByBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_storage_and_acc_by_buckets_with_options_async(request, runtime)

    def get_oss_usage_data_with_options(
        self,
        request: ens_20171110_models.GetOssUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetOssUsageDataResponse:
        """
        The query and aggregation granularity of bandwidth and storage usage cannot exceed one day. Data aggregation is to collect the maximum values of usage data within a period of time.
        
        @param request: GetOssUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssUsageData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetOssUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_usage_data_with_options_async(
        self,
        request: ens_20171110_models.GetOssUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetOssUsageDataResponse:
        """
        The query and aggregation granularity of bandwidth and storage usage cannot exceed one day. Data aggregation is to collect the maximum values of usage data within a period of time.
        
        @param request: GetOssUsageDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssUsageDataResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssUsageData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.GetOssUsageDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_usage_data(
        self,
        request: ens_20171110_models.GetOssUsageDataRequest,
    ) -> ens_20171110_models.GetOssUsageDataResponse:
        """
        The query and aggregation granularity of bandwidth and storage usage cannot exceed one day. Data aggregation is to collect the maximum values of usage data within a period of time.
        
        @param request: GetOssUsageDataRequest
        @return: GetOssUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oss_usage_data_with_options(request, runtime)

    async def get_oss_usage_data_async(
        self,
        request: ens_20171110_models.GetOssUsageDataRequest,
    ) -> ens_20171110_models.GetOssUsageDataResponse:
        """
        The query and aggregation granularity of bandwidth and storage usage cannot exceed one day. Data aggregation is to collect the maximum values of usage data within a period of time.
        
        @param request: GetOssUsageDataRequest
        @return: GetOssUsageDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_usage_data_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        """
        After the key pair is imported, ENS stores the public key. You must securely store the private key.
        *   The key pair can be only in the ssh-rsa format.
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ImportKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        """
        After the key pair is imported, ENS stores the public key. You must securely store the private key.
        *   The key pair can be only in the ssh-rsa format.
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ImportKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_pair(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        """
        After the key pair is imported, ENS stores the public key. You must securely store the private key.
        *   The key pair can be only in the ssh-rsa format.
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        """
        After the key pair is imported, ENS stores the public key. You must securely store the private key.
        *   The key pair can be only in the ssh-rsa format.
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def join_public_ips_to_epn_instance_with_options(
        self,
        request: ens_20171110_models.JoinPublicIpsToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinPublicIpsToEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.instance_infos):
            query['InstanceInfos'] = request.instance_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinPublicIpsToEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.JoinPublicIpsToEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_public_ips_to_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.JoinPublicIpsToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinPublicIpsToEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.instance_infos):
            query['InstanceInfos'] = request.instance_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinPublicIpsToEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.JoinPublicIpsToEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_public_ips_to_epn_instance(
        self,
        request: ens_20171110_models.JoinPublicIpsToEpnInstanceRequest,
    ) -> ens_20171110_models.JoinPublicIpsToEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_public_ips_to_epn_instance_with_options(request, runtime)

    async def join_public_ips_to_epn_instance_async(
        self,
        request: ens_20171110_models.JoinPublicIpsToEpnInstanceRequest,
    ) -> ens_20171110_models.JoinPublicIpsToEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_public_ips_to_epn_instance_with_options_async(request, runtime)

    def join_security_group_with_options(
        self,
        request: ens_20171110_models.JoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinSecurityGroupResponse:
        """
        Before you call this operation to add an instance to a security group, make sure that the instance is in the Stopped or Running state.
        
        @param request: JoinSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.JoinSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_security_group_with_options_async(
        self,
        request: ens_20171110_models.JoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinSecurityGroupResponse:
        """
        Before you call this operation to add an instance to a security group, make sure that the instance is in the Stopped or Running state.
        
        @param request: JoinSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.JoinSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_security_group(
        self,
        request: ens_20171110_models.JoinSecurityGroupRequest,
    ) -> ens_20171110_models.JoinSecurityGroupResponse:
        """
        Before you call this operation to add an instance to a security group, make sure that the instance is in the Stopped or Running state.
        
        @param request: JoinSecurityGroupRequest
        @return: JoinSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.join_security_group_with_options(request, runtime)

    async def join_security_group_async(
        self,
        request: ens_20171110_models.JoinSecurityGroupRequest,
    ) -> ens_20171110_models.JoinSecurityGroupResponse:
        """
        Before you call this operation to add an instance to a security group, make sure that the instance is in the Stopped or Running state.
        
        @param request: JoinSecurityGroupRequest
        @return: JoinSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.join_security_group_with_options_async(request, runtime)

    def join_vswitches_to_epn_instance_with_options(
        self,
        request: ens_20171110_models.JoinVSwitchesToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinVSwitchesToEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.v_switches_info):
            query['VSwitchesInfo'] = request.v_switches_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinVSwitchesToEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.JoinVSwitchesToEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_vswitches_to_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.JoinVSwitchesToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinVSwitchesToEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.v_switches_info):
            query['VSwitchesInfo'] = request.v_switches_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinVSwitchesToEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.JoinVSwitchesToEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_vswitches_to_epn_instance(
        self,
        request: ens_20171110_models.JoinVSwitchesToEpnInstanceRequest,
    ) -> ens_20171110_models.JoinVSwitchesToEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_vswitches_to_epn_instance_with_options(request, runtime)

    async def join_vswitches_to_epn_instance_async(
        self,
        request: ens_20171110_models.JoinVSwitchesToEpnInstanceRequest,
    ) -> ens_20171110_models.JoinVSwitchesToEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_vswitches_to_epn_instance_with_options_async(request, runtime)

    def leave_security_group_with_options(
        self,
        request: ens_20171110_models.LeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.LeaveSecurityGroupResponse:
        """
        Before you remove an instance from a security group, the instance must be in the Stopped or Running state.
        
        @param request: LeaveSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LeaveSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LeaveSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.LeaveSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def leave_security_group_with_options_async(
        self,
        request: ens_20171110_models.LeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.LeaveSecurityGroupResponse:
        """
        Before you remove an instance from a security group, the instance must be in the Stopped or Running state.
        
        @param request: LeaveSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LeaveSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LeaveSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.LeaveSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def leave_security_group(
        self,
        request: ens_20171110_models.LeaveSecurityGroupRequest,
    ) -> ens_20171110_models.LeaveSecurityGroupResponse:
        """
        Before you remove an instance from a security group, the instance must be in the Stopped or Running state.
        
        @param request: LeaveSecurityGroupRequest
        @return: LeaveSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.leave_security_group_with_options(request, runtime)

    async def leave_security_group_async(
        self,
        request: ens_20171110_models.LeaveSecurityGroupRequest,
    ) -> ens_20171110_models.LeaveSecurityGroupResponse:
        """
        Before you remove an instance from a security group, the instance must be in the Stopped or Running state.
        
        @param request: LeaveSecurityGroupRequest
        @return: LeaveSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.leave_security_group_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: ens_20171110_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_versions):
            query['AppVersions'] = request.app_versions
        if not UtilClient.is_unset(request.cluster_names):
            query['ClusterNames'] = request.cluster_names
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.out_app_info_params):
            query['OutAppInfoParams'] = request.out_app_info_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: ens_20171110_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_versions):
            query['AppVersions'] = request.app_versions
        if not UtilClient.is_unset(request.cluster_names):
            query['ClusterNames'] = request.cluster_names
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.max_date):
            query['MaxDate'] = request.max_date
        if not UtilClient.is_unset(request.min_date):
            query['MinDate'] = request.min_date
        if not UtilClient.is_unset(request.out_app_info_params):
            query['OutAppInfoParams'] = request.out_app_info_params
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: ens_20171110_models.ListApplicationsRequest,
    ) -> ens_20171110_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: ens_20171110_models.ListApplicationsRequest,
    ) -> ens_20171110_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def list_buckets_with_options(
        self,
        request: ens_20171110_models.ListBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListBucketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBuckets',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ListBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_buckets_with_options_async(
        self,
        request: ens_20171110_models.ListBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListBucketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBuckets',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ListBucketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_buckets(
        self,
        request: ens_20171110_models.ListBucketsRequest,
    ) -> ens_20171110_models.ListBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_buckets_with_options(request, runtime)

    async def list_buckets_async(
        self,
        request: ens_20171110_models.ListBucketsRequest,
    ) -> ens_20171110_models.ListBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_buckets_with_options_async(request, runtime)

    def list_objects_with_options(
        self,
        request: ens_20171110_models.ListObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListObjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.continuation_token):
            query['ContinuationToken'] = request.continuation_token
        if not UtilClient.is_unset(request.encoding_type):
            query['EncodingType'] = request.encoding_type
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_after):
            query['StartAfter'] = request.start_after
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjects',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ListObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_objects_with_options_async(
        self,
        request: ens_20171110_models.ListObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListObjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.continuation_token):
            query['ContinuationToken'] = request.continuation_token
        if not UtilClient.is_unset(request.encoding_type):
            query['EncodingType'] = request.encoding_type
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_after):
            query['StartAfter'] = request.start_after
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjects',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ListObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_objects(
        self,
        request: ens_20171110_models.ListObjectsRequest,
    ) -> ens_20171110_models.ListObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_objects_with_options(request, runtime)

    async def list_objects_async(
        self,
        request: ens_20171110_models.ListObjectsRequest,
    ) -> ens_20171110_models.ListObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_objects_with_options_async(request, runtime)

    def modify_ens_eip_address_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyEnsEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyEnsEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEnsEipAddressAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyEnsEipAddressAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ens_eip_address_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyEnsEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyEnsEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEnsEipAddressAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyEnsEipAddressAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ens_eip_address_attribute(
        self,
        request: ens_20171110_models.ModifyEnsEipAddressAttributeRequest,
    ) -> ens_20171110_models.ModifyEnsEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ens_eip_address_attribute_with_options(request, runtime)

    async def modify_ens_eip_address_attribute_async(
        self,
        request: ens_20171110_models.ModifyEnsEipAddressAttributeRequest,
    ) -> ens_20171110_models.ModifyEnsEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ens_eip_address_attribute_with_options_async(request, runtime)

    def modify_epn_instance_with_options(
        self,
        request: ens_20171110_models.ModifyEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.epninstance_name):
            query['EPNInstanceName'] = request.epninstance_name
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.ModifyEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.epninstance_name):
            query['EPNInstanceName'] = request.epninstance_name
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.networking_model):
            query['NetworkingModel'] = request.networking_model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_epn_instance(
        self,
        request: ens_20171110_models.ModifyEpnInstanceRequest,
    ) -> ens_20171110_models.ModifyEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_epn_instance_with_options(request, runtime)

    async def modify_epn_instance_async(
        self,
        request: ens_20171110_models.ModifyEpnInstanceRequest,
    ) -> ens_20171110_models.ModifyEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_epn_instance_with_options_async(request, runtime)

    def modify_file_system_with_options(
        self,
        request: ens_20171110_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_file_system_with_options_async(
        self,
        request: ens_20171110_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_file_system(
        self,
        request: ens_20171110_models.ModifyFileSystemRequest,
    ) -> ens_20171110_models.ModifyFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_file_system_with_options(request, runtime)

    async def modify_file_system_async(
        self,
        request: ens_20171110_models.ModifyFileSystemRequest,
    ) -> ens_20171110_models.ModifyFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_file_system_with_options_async(request, runtime)

    def modify_forward_entry_with_options(
        self,
        request: ens_20171110_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        if not UtilClient.is_unset(request.forward_entry_name):
            query['ForwardEntryName'] = request.forward_entry_name
        if not UtilClient.is_unset(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyForwardEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyForwardEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_forward_entry_with_options_async(
        self,
        request: ens_20171110_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.forward_entry_id):
            query['ForwardEntryId'] = request.forward_entry_id
        if not UtilClient.is_unset(request.forward_entry_name):
            query['ForwardEntryName'] = request.forward_entry_name
        if not UtilClient.is_unset(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyForwardEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyForwardEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_forward_entry(
        self,
        request: ens_20171110_models.ModifyForwardEntryRequest,
    ) -> ens_20171110_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_forward_entry_with_options(request, runtime)

    async def modify_forward_entry_async(
        self,
        request: ens_20171110_models.ModifyForwardEntryRequest,
    ) -> ens_20171110_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_forward_entry_with_options_async(request, runtime)

    def modify_image_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyImageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyImageAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_attribute(
        self,
        request: ens_20171110_models.ModifyImageAttributeRequest,
    ) -> ens_20171110_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    async def modify_image_attribute_async(
        self,
        request: ens_20171110_models.ModifyImageAttributeRequest,
    ) -> ens_20171110_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_attribute_with_options_async(request, runtime)

    def modify_image_share_permission_with_options(
        self,
        request: ens_20171110_models.ModifyImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyImageSharePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_accounts):
            query['AddAccounts'] = request.add_accounts
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.remove_accounts):
            query['RemoveAccounts'] = request.remove_accounts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageSharePermission',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyImageSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_share_permission_with_options_async(
        self,
        request: ens_20171110_models.ModifyImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyImageSharePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_accounts):
            query['AddAccounts'] = request.add_accounts
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.remove_accounts):
            query['RemoveAccounts'] = request.remove_accounts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageSharePermission',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyImageSharePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_share_permission(
        self,
        request: ens_20171110_models.ModifyImageSharePermissionRequest,
    ) -> ens_20171110_models.ModifyImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_permission_with_options(request, runtime)

    async def modify_image_share_permission_async(
        self,
        request: ens_20171110_models.ModifyImageSharePermissionRequest,
    ) -> ens_20171110_models.ModifyImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_share_permission_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyInstanceAttributeResponse:
        """
        If an instance is in the Starting state, you cannot reset the password of the instance.
        *   When the instance is in the Running state, you cannot change the password of the instance.
        *   After resetting the password, you must Restart the instance in the ECS console or call the RebootInstance operation to validate the modifications. The restart operation within the instance does not validate the modifications.
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyInstanceAttributeResponse:
        """
        If an instance is in the Starting state, you cannot reset the password of the instance.
        *   When the instance is in the Running state, you cannot change the password of the instance.
        *   After resetting the password, you must Restart the instance in the ECS console or call the RebootInstance operation to validate the modifications. The restart operation within the instance does not validate the modifications.
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: ens_20171110_models.ModifyInstanceAttributeRequest,
    ) -> ens_20171110_models.ModifyInstanceAttributeResponse:
        """
        If an instance is in the Starting state, you cannot reset the password of the instance.
        *   When the instance is in the Running state, you cannot change the password of the instance.
        *   After resetting the password, you must Restart the instance in the ECS console or call the RebootInstance operation to validate the modifications. The restart operation within the instance does not validate the modifications.
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: ens_20171110_models.ModifyInstanceAttributeRequest,
    ) -> ens_20171110_models.ModifyInstanceAttributeResponse:
        """
        If an instance is in the Starting state, you cannot reset the password of the instance.
        *   When the instance is in the Running state, you cannot change the password of the instance.
        *   After resetting the password, you must Restart the instance in the ECS console or call the RebootInstance operation to validate the modifications. The restart operation within the instance does not validate the modifications.
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_auto_renew_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyInstanceAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auto_renew_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAutoRenewAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyInstanceAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auto_renew_attribute(
        self,
        request: ens_20171110_models.ModifyInstanceAutoRenewAttributeRequest,
    ) -> ens_20171110_models.ModifyInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renew_attribute_with_options(request, runtime)

    async def modify_instance_auto_renew_attribute_async(
        self,
        request: ens_20171110_models.ModifyInstanceAutoRenewAttributeRequest,
    ) -> ens_20171110_models.ModifyInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renew_attribute_with_options_async(request, runtime)

    def modify_instance_charge_type_with_options(
        self,
        tmp_req: ens_20171110_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.ModifyInstanceChargeTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.include_data_disks):
            query['IncludeDataDisks'] = request.include_data_disks
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_charge_type_with_options_async(
        self,
        tmp_req: ens_20171110_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.ModifyInstanceChargeTypeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.include_data_disks):
            query['IncludeDataDisks'] = request.include_data_disks
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceChargeType',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_charge_type(
        self,
        request: ens_20171110_models.ModifyInstanceChargeTypeRequest,
    ) -> ens_20171110_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    async def modify_instance_charge_type_async(
        self,
        request: ens_20171110_models.ModifyInstanceChargeTypeRequest,
    ) -> ens_20171110_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_charge_type_with_options_async(request, runtime)

    def modify_load_balancer_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyLoadBalancerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: ModifyLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_load_balancer_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyLoadBalancerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyLoadBalancerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: ModifyLoadBalancerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyLoadBalancerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_load_balancer_attribute(
        self,
        request: ens_20171110_models.ModifyLoadBalancerAttributeRequest,
    ) -> ens_20171110_models.ModifyLoadBalancerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: ModifyLoadBalancerAttributeRequest
        @return: ModifyLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_attribute_with_options(request, runtime)

    async def modify_load_balancer_attribute_async(
        self,
        request: ens_20171110_models.ModifyLoadBalancerAttributeRequest,
    ) -> ens_20171110_models.ModifyLoadBalancerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: ModifyLoadBalancerAttributeRequest
        @return: ModifyLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_load_balancer_attribute_with_options_async(request, runtime)

    def modify_network_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyNetworkAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyNetworkAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNetworkAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyNetworkAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_network_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyNetworkAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyNetworkAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNetworkAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.network_id):
            query['NetworkId'] = request.network_id
        if not UtilClient.is_unset(request.network_name):
            query['NetworkName'] = request.network_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyNetworkAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_network_attribute(
        self,
        request: ens_20171110_models.ModifyNetworkAttributeRequest,
    ) -> ens_20171110_models.ModifyNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyNetworkAttributeRequest
        @return: ModifyNetworkAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_network_attribute_with_options(request, runtime)

    async def modify_network_attribute_async(
        self,
        request: ens_20171110_models.ModifyNetworkAttributeRequest,
    ) -> ens_20171110_models.ModifyNetworkAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyNetworkAttributeRequest
        @return: ModifyNetworkAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_attribute_with_options_async(request, runtime)

    def modify_prepay_instance_spec_with_options(
        self,
        request: ens_20171110_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyPrepayInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        request: ens_20171110_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyPrepayInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_prepay_instance_spec(
        self,
        request: ens_20171110_models.ModifyPrepayInstanceSpecRequest,
    ) -> ens_20171110_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: ens_20171110_models.ModifyPrepayInstanceSpecRequest,
    ) -> ens_20171110_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def modify_security_group_attribute_with_options(
        self,
        request: ens_20171110_models.ModifySecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifySecurityGroupAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifySecurityGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifySecurityGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_group_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifySecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifySecurityGroupAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifySecurityGroupAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityGroupAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifySecurityGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_group_attribute(
        self,
        request: ens_20171110_models.ModifySecurityGroupAttributeRequest,
    ) -> ens_20171110_models.ModifySecurityGroupAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifySecurityGroupAttributeRequest
        @return: ModifySecurityGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_attribute_with_options(request, runtime)

    async def modify_security_group_attribute_async(
        self,
        request: ens_20171110_models.ModifySecurityGroupAttributeRequest,
    ) -> ens_20171110_models.ModifySecurityGroupAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifySecurityGroupAttributeRequest
        @return: ModifySecurityGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_attribute_with_options_async(request, runtime)

    def modify_snapshot_attribute_with_options(
        self,
        request: ens_20171110_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySnapshotAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifySnapshotAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_snapshot_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySnapshotAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifySnapshotAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_snapshot_attribute(
        self,
        request: ens_20171110_models.ModifySnapshotAttributeRequest,
    ) -> ens_20171110_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_attribute_with_options(request, runtime)

    async def modify_snapshot_attribute_async(
        self,
        request: ens_20171110_models.ModifySnapshotAttributeRequest,
    ) -> ens_20171110_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_snapshot_attribute_with_options_async(request, runtime)

    def modify_vswitch_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyVSwitchAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyVSwitchAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVSwitchAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVSwitchAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyVSwitchAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_vswitch_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyVSwitchAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyVSwitchAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyVSwitchAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_name):
            query['VSwitchName'] = request.v_switch_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVSwitchAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ModifyVSwitchAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_vswitch_attribute(
        self,
        request: ens_20171110_models.ModifyVSwitchAttributeRequest,
    ) -> ens_20171110_models.ModifyVSwitchAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyVSwitchAttributeRequest
        @return: ModifyVSwitchAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vswitch_attribute_with_options(request, runtime)

    async def modify_vswitch_attribute_async(
        self,
        request: ens_20171110_models.ModifyVSwitchAttributeRequest,
    ) -> ens_20171110_models.ModifyVSwitchAttributeResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 5 times per second per user.
        
        @param request: ModifyVSwitchAttributeRequest
        @return: ModifyVSwitchAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_vswitch_attribute_with_options_async(request, runtime)

    def push_application_data_with_options(
        self,
        request: ens_20171110_models.PushApplicationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PushApplicationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.push_strategy):
            query['PushStrategy'] = request.push_strategy
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushApplicationData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PushApplicationDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_application_data_with_options_async(
        self,
        request: ens_20171110_models.PushApplicationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PushApplicationDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.push_strategy):
            query['PushStrategy'] = request.push_strategy
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushApplicationData',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PushApplicationDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_application_data(
        self,
        request: ens_20171110_models.PushApplicationDataRequest,
    ) -> ens_20171110_models.PushApplicationDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_application_data_with_options(request, runtime)

    async def push_application_data_async(
        self,
        request: ens_20171110_models.PushApplicationDataRequest,
    ) -> ens_20171110_models.PushApplicationDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_application_data_with_options_async(request, runtime)

    def put_bucket_with_options(
        self,
        request: ens_20171110_models.PutBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PutBucketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_acl):
            body['BucketAcl'] = request.bucket_acl
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ens_region_id):
            body['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.logical_bucket_type):
            body['LogicalBucketType'] = request.logical_bucket_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutBucket',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PutBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_bucket_with_options_async(
        self,
        request: ens_20171110_models.PutBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PutBucketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bucket_acl):
            body['BucketAcl'] = request.bucket_acl
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.ens_region_id):
            body['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.logical_bucket_type):
            body['LogicalBucketType'] = request.logical_bucket_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutBucket',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PutBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_bucket(
        self,
        request: ens_20171110_models.PutBucketRequest,
    ) -> ens_20171110_models.PutBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_bucket_with_options(request, runtime)

    async def put_bucket_async(
        self,
        request: ens_20171110_models.PutBucketRequest,
    ) -> ens_20171110_models.PutBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_bucket_with_options_async(request, runtime)

    def put_bucket_acl_with_options(
        self,
        request: ens_20171110_models.PutBucketAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PutBucketAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_acl):
            query['BucketAcl'] = request.bucket_acl
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutBucketAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PutBucketAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_bucket_acl_with_options_async(
        self,
        request: ens_20171110_models.PutBucketAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PutBucketAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_acl):
            query['BucketAcl'] = request.bucket_acl
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutBucketAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PutBucketAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_bucket_acl(
        self,
        request: ens_20171110_models.PutBucketAclRequest,
    ) -> ens_20171110_models.PutBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_bucket_acl_with_options(request, runtime)

    async def put_bucket_acl_async(
        self,
        request: ens_20171110_models.PutBucketAclRequest,
    ) -> ens_20171110_models.PutBucketAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_bucket_acl_with_options_async(request, runtime)

    def put_bucket_lifecycle_with_options(
        self,
        request: ens_20171110_models.PutBucketLifecycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PutBucketLifecycleResponse:
        """
        - You can configure up to 1000 rules.
        - If an object meets multiple rules, the rule that has the earliest expiration time prevails.
        
        @param request: PutBucketLifecycleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutBucketLifecycleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_same_action_overlap):
            query['AllowSameActionOverlap'] = request.allow_same_action_overlap
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.created_before_date):
            query['CreatedBeforeDate'] = request.created_before_date
        if not UtilClient.is_unset(request.expiration_days):
            query['ExpirationDays'] = request.expiration_days
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutBucketLifecycle',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PutBucketLifecycleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_bucket_lifecycle_with_options_async(
        self,
        request: ens_20171110_models.PutBucketLifecycleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PutBucketLifecycleResponse:
        """
        - You can configure up to 1000 rules.
        - If an object meets multiple rules, the rule that has the earliest expiration time prevails.
        
        @param request: PutBucketLifecycleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutBucketLifecycleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_same_action_overlap):
            query['AllowSameActionOverlap'] = request.allow_same_action_overlap
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.created_before_date):
            query['CreatedBeforeDate'] = request.created_before_date
        if not UtilClient.is_unset(request.expiration_days):
            query['ExpirationDays'] = request.expiration_days
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutBucketLifecycle',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.PutBucketLifecycleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_bucket_lifecycle(
        self,
        request: ens_20171110_models.PutBucketLifecycleRequest,
    ) -> ens_20171110_models.PutBucketLifecycleResponse:
        """
        - You can configure up to 1000 rules.
        - If an object meets multiple rules, the rule that has the earliest expiration time prevails.
        
        @param request: PutBucketLifecycleRequest
        @return: PutBucketLifecycleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_bucket_lifecycle_with_options(request, runtime)

    async def put_bucket_lifecycle_async(
        self,
        request: ens_20171110_models.PutBucketLifecycleRequest,
    ) -> ens_20171110_models.PutBucketLifecycleResponse:
        """
        - You can configure up to 1000 rules.
        - If an object meets multiple rules, the rule that has the earliest expiration time prevails.
        
        @param request: PutBucketLifecycleRequest
        @return: PutBucketLifecycleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_bucket_lifecycle_with_options_async(request, runtime)

    def re_init_disk_with_options(
        self,
        request: ens_20171110_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReInitDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReInitDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_init_disk_with_options_async(
        self,
        request: ens_20171110_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReInitDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReInitDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_init_disk(
        self,
        request: ens_20171110_models.ReInitDiskRequest,
    ) -> ens_20171110_models.ReInitDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_init_disk_with_options(request, runtime)

    async def re_init_disk_async(
        self,
        request: ens_20171110_models.ReInitDiskRequest,
    ) -> ens_20171110_models.ReInitDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_init_disk_with_options_async(request, runtime)

    def reboot_aicinstance_with_options(
        self,
        tmp_req: ens_20171110_models.RebootAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootAICInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RebootAICInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootAICInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_aicinstance_with_options_async(
        self,
        tmp_req: ens_20171110_models.RebootAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootAICInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RebootAICInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootAICInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_aicinstance(
        self,
        request: ens_20171110_models.RebootAICInstanceRequest,
    ) -> ens_20171110_models.RebootAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_aicinstance_with_options(request, runtime)

    async def reboot_aicinstance_async(
        self,
        request: ens_20171110_models.RebootAICInstanceRequest,
    ) -> ens_20171110_models.RebootAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_aicinstance_with_options_async(request, runtime)

    def reboot_armserver_instance_with_options(
        self,
        request: ens_20171110_models.RebootARMServerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootARMServerInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootARMServerInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootARMServerInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_armserver_instance_with_options_async(
        self,
        request: ens_20171110_models.RebootARMServerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootARMServerInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootARMServerInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootARMServerInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_armserver_instance(
        self,
        request: ens_20171110_models.RebootARMServerInstanceRequest,
    ) -> ens_20171110_models.RebootARMServerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_armserver_instance_with_options(request, runtime)

    async def reboot_armserver_instance_async(
        self,
        request: ens_20171110_models.RebootARMServerInstanceRequest,
    ) -> ens_20171110_models.RebootARMServerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_armserver_instance_with_options_async(request, runtime)

    def reboot_instance_with_options(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootInstanceResponse:
        """
        Only instances that are in the Running state can be restarted.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: RebootInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootInstanceResponse:
        """
        Only instances that are in the Running state can be restarted.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: RebootInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_instance(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
    ) -> ens_20171110_models.RebootInstanceResponse:
        """
        Only instances that are in the Running state can be restarted.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: RebootInstanceRequest
        @return: RebootInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    async def reboot_instance_async(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
    ) -> ens_20171110_models.RebootInstanceResponse:
        """
        Only instances that are in the Running state can be restarted.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: RebootInstanceRequest
        @return: RebootInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instance_with_options_async(request, runtime)

    def reboot_instances_with_options(
        self,
        tmp_req: ens_20171110_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RebootInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instances_with_options_async(
        self,
        tmp_req: ens_20171110_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RebootInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RebootInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_instances(
        self,
        request: ens_20171110_models.RebootInstancesRequest,
    ) -> ens_20171110_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    async def reboot_instances_async(
        self,
        request: ens_20171110_models.RebootInstancesRequest,
    ) -> ens_20171110_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instances_with_options_async(request, runtime)

    def recover_aicinstance_with_options(
        self,
        request: ens_20171110_models.RecoverAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RecoverAICInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RecoverAICInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_aicinstance_with_options_async(
        self,
        request: ens_20171110_models.RecoverAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RecoverAICInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RecoverAICInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_aicinstance(
        self,
        request: ens_20171110_models.RecoverAICInstanceRequest,
    ) -> ens_20171110_models.RecoverAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_aicinstance_with_options(request, runtime)

    async def recover_aicinstance_async(
        self,
        request: ens_20171110_models.RecoverAICInstanceRequest,
    ) -> ens_20171110_models.RecoverAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_aicinstance_with_options_async(request, runtime)

    def reinit_instance_with_options(
        self,
        request: ens_20171110_models.ReinitInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReinitInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReinitInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReinitInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reinit_instance_with_options_async(
        self,
        request: ens_20171110_models.ReinitInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReinitInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReinitInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReinitInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reinit_instance(
        self,
        request: ens_20171110_models.ReinitInstanceRequest,
    ) -> ens_20171110_models.ReinitInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reinit_instance_with_options(request, runtime)

    async def reinit_instance_async(
        self,
        request: ens_20171110_models.ReinitInstanceRequest,
    ) -> ens_20171110_models.ReinitInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reinit_instance_with_options_async(request, runtime)

    def reinit_instances_with_options(
        self,
        tmp_req: ens_20171110_models.ReinitInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReinitInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.ReinitInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReinitInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReinitInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reinit_instances_with_options_async(
        self,
        tmp_req: ens_20171110_models.ReinitInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReinitInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.ReinitInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReinitInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReinitInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reinit_instances(
        self,
        request: ens_20171110_models.ReinitInstancesRequest,
    ) -> ens_20171110_models.ReinitInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reinit_instances_with_options(request, runtime)

    async def reinit_instances_async(
        self,
        request: ens_20171110_models.ReinitInstancesRequest,
    ) -> ens_20171110_models.ReinitInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reinit_instances_with_options_async(request, runtime)

    def release_aicinstance_with_options(
        self,
        request: ens_20171110_models.ReleaseAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseAICInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleaseAICInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_aicinstance_with_options_async(
        self,
        request: ens_20171110_models.ReleaseAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseAICInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleaseAICInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_aicinstance(
        self,
        request: ens_20171110_models.ReleaseAICInstanceRequest,
    ) -> ens_20171110_models.ReleaseAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_aicinstance_with_options(request, runtime)

    async def release_aicinstance_async(
        self,
        request: ens_20171110_models.ReleaseAICInstanceRequest,
    ) -> ens_20171110_models.ReleaseAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_aicinstance_with_options_async(request, runtime)

    def release_armserver_instance_with_options(
        self,
        request: ens_20171110_models.ReleaseARMServerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseARMServerInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseARMServerInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleaseARMServerInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_armserver_instance_with_options_async(
        self,
        request: ens_20171110_models.ReleaseARMServerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseARMServerInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseARMServerInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleaseARMServerInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_armserver_instance(
        self,
        request: ens_20171110_models.ReleaseARMServerInstanceRequest,
    ) -> ens_20171110_models.ReleaseARMServerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_armserver_instance_with_options(request, runtime)

    async def release_armserver_instance_async(
        self,
        request: ens_20171110_models.ReleaseARMServerInstanceRequest,
    ) -> ens_20171110_models.ReleaseARMServerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_armserver_instance_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: ens_20171110_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseInstanceResponse:
        """
        You can call this operation up to 10,000 times per second per account.
        *   The maximum number of times that each user can call this operation per second is 50.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: ens_20171110_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseInstanceResponse:
        """
        You can call this operation up to 10,000 times per second per account.
        *   The maximum number of times that each user can call this operation per second is 50.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: ens_20171110_models.ReleaseInstanceRequest,
    ) -> ens_20171110_models.ReleaseInstanceResponse:
        """
        You can call this operation up to 10,000 times per second per account.
        *   The maximum number of times that each user can call this operation per second is 50.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: ens_20171110_models.ReleaseInstanceRequest,
    ) -> ens_20171110_models.ReleaseInstanceResponse:
        """
        You can call this operation up to 10,000 times per second per account.
        *   The maximum number of times that each user can call this operation per second is 50.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def release_post_paid_instance_with_options(
        self,
        request: ens_20171110_models.ReleasePostPaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleasePostPaidInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePostPaidInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleasePostPaidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_post_paid_instance_with_options_async(
        self,
        request: ens_20171110_models.ReleasePostPaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleasePostPaidInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePostPaidInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleasePostPaidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_post_paid_instance(
        self,
        request: ens_20171110_models.ReleasePostPaidInstanceRequest,
    ) -> ens_20171110_models.ReleasePostPaidInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_post_paid_instance_with_options(request, runtime)

    async def release_post_paid_instance_async(
        self,
        request: ens_20171110_models.ReleasePostPaidInstanceRequest,
    ) -> ens_20171110_models.ReleasePostPaidInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_post_paid_instance_with_options_async(request, runtime)

    def release_pre_paid_instance_with_options(
        self,
        request: ens_20171110_models.ReleasePrePaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleasePrePaidInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePrePaidInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleasePrePaidInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_pre_paid_instance_with_options_async(
        self,
        request: ens_20171110_models.ReleasePrePaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleasePrePaidInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleasePrePaidInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ReleasePrePaidInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_pre_paid_instance(
        self,
        request: ens_20171110_models.ReleasePrePaidInstanceRequest,
    ) -> ens_20171110_models.ReleasePrePaidInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_pre_paid_instance_with_options(request, runtime)

    async def release_pre_paid_instance_async(
        self,
        request: ens_20171110_models.ReleasePrePaidInstanceRequest,
    ) -> ens_20171110_models.ReleasePrePaidInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_pre_paid_instance_with_options_async(request, runtime)

    def remove_backend_servers_with_options(
        self,
        tmp_req: ens_20171110_models.RemoveBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemoveBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param tmp_req: RemoveBackendServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveBackendServersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RemoveBackendServersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backend_servers):
            request.backend_servers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backend_servers, 'BackendServers', 'json')
        query = {}
        if not UtilClient.is_unset(request.backend_servers_shrink):
            query['BackendServers'] = request.backend_servers_shrink
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBackendServers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RemoveBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_backend_servers_with_options_async(
        self,
        tmp_req: ens_20171110_models.RemoveBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemoveBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param tmp_req: RemoveBackendServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveBackendServersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RemoveBackendServersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backend_servers):
            request.backend_servers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backend_servers, 'BackendServers', 'json')
        query = {}
        if not UtilClient.is_unset(request.backend_servers_shrink):
            query['BackendServers'] = request.backend_servers_shrink
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBackendServers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RemoveBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_backend_servers(
        self,
        request: ens_20171110_models.RemoveBackendServersRequest,
    ) -> ens_20171110_models.RemoveBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: RemoveBackendServersRequest
        @return: RemoveBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_backend_servers_with_options(request, runtime)

    async def remove_backend_servers_async(
        self,
        request: ens_20171110_models.RemoveBackendServersRequest,
    ) -> ens_20171110_models.RemoveBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: RemoveBackendServersRequest
        @return: RemoveBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_backend_servers_with_options_async(request, runtime)

    def remove_public_ips_from_epn_instance_with_options(
        self,
        request: ens_20171110_models.RemovePublicIpsFromEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.instance_infos):
            query['InstanceInfos'] = request.instance_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePublicIpsFromEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_public_ips_from_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.RemovePublicIpsFromEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.instance_infos):
            query['InstanceInfos'] = request.instance_infos
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePublicIpsFromEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_public_ips_from_epn_instance(
        self,
        request: ens_20171110_models.RemovePublicIpsFromEpnInstanceRequest,
    ) -> ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_public_ips_from_epn_instance_with_options(request, runtime)

    async def remove_public_ips_from_epn_instance_async(
        self,
        request: ens_20171110_models.RemovePublicIpsFromEpnInstanceRequest,
    ) -> ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_public_ips_from_epn_instance_with_options_async(request, runtime)

    def remove_vswitches_from_epn_instance_with_options(
        self,
        request: ens_20171110_models.RemoveVSwitchesFromEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.v_switches_info):
            query['VSwitchesInfo'] = request.v_switches_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVSwitchesFromEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vswitches_from_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.RemoveVSwitchesFromEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        if not UtilClient.is_unset(request.v_switches_info):
            query['VSwitchesInfo'] = request.v_switches_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVSwitchesFromEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vswitches_from_epn_instance(
        self,
        request: ens_20171110_models.RemoveVSwitchesFromEpnInstanceRequest,
    ) -> ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_vswitches_from_epn_instance_with_options(request, runtime)

    async def remove_vswitches_from_epn_instance_async(
        self,
        request: ens_20171110_models.RemoveVSwitchesFromEpnInstanceRequest,
    ) -> ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_vswitches_from_epn_instance_with_options_async(request, runtime)

    def renew_armserver_instance_with_options(
        self,
        request: ens_20171110_models.RenewARMServerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RenewARMServerInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewARMServerInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RenewARMServerInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_armserver_instance_with_options_async(
        self,
        request: ens_20171110_models.RenewARMServerInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RenewARMServerInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewARMServerInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RenewARMServerInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_armserver_instance(
        self,
        request: ens_20171110_models.RenewARMServerInstanceRequest,
    ) -> ens_20171110_models.RenewARMServerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_armserver_instance_with_options(request, runtime)

    async def renew_armserver_instance_async(
        self,
        request: ens_20171110_models.RenewARMServerInstanceRequest,
    ) -> ens_20171110_models.RenewARMServerInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_armserver_instance_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: ens_20171110_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: ens_20171110_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: ens_20171110_models.RenewInstanceRequest,
    ) -> ens_20171110_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: ens_20171110_models.RenewInstanceRequest,
    ) -> ens_20171110_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def rescale_application_with_options(
        self,
        request: ens_20171110_models.RescaleApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RescaleApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.rescale_level):
            query['RescaleLevel'] = request.rescale_level
        if not UtilClient.is_unset(request.rescale_type):
            query['RescaleType'] = request.rescale_type
        if not UtilClient.is_unset(request.resource_selector):
            query['ResourceSelector'] = request.resource_selector
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.to_app_version):
            query['ToAppVersion'] = request.to_app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RescaleApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_application_with_options_async(
        self,
        request: ens_20171110_models.RescaleApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RescaleApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.rescale_level):
            query['RescaleLevel'] = request.rescale_level
        if not UtilClient.is_unset(request.rescale_type):
            query['RescaleType'] = request.rescale_type
        if not UtilClient.is_unset(request.resource_selector):
            query['ResourceSelector'] = request.resource_selector
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.to_app_version):
            query['ToAppVersion'] = request.to_app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RescaleApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RescaleApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_application(
        self,
        request: ens_20171110_models.RescaleApplicationRequest,
    ) -> ens_20171110_models.RescaleApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.rescale_application_with_options(request, runtime)

    async def rescale_application_async(
        self,
        request: ens_20171110_models.RescaleApplicationRequest,
    ) -> ens_20171110_models.RescaleApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rescale_application_with_options_async(request, runtime)

    def rescale_device_service_with_options(
        self,
        request: ens_20171110_models.RescaleDeviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RescaleDeviceServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.rescale_level):
            query['RescaleLevel'] = request.rescale_level
        if not UtilClient.is_unset(request.rescale_type):
            query['RescaleType'] = request.rescale_type
        if not UtilClient.is_unset(request.resource_spec):
            query['ResourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        body = {}
        if not UtilClient.is_unset(request.resource_info):
            body['ResourceInfo'] = request.resource_info
        if not UtilClient.is_unset(request.resource_selector):
            body['ResourceSelector'] = request.resource_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RescaleDeviceService',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RescaleDeviceServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rescale_device_service_with_options_async(
        self,
        request: ens_20171110_models.RescaleDeviceServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RescaleDeviceServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.rescale_level):
            query['RescaleLevel'] = request.rescale_level
        if not UtilClient.is_unset(request.rescale_type):
            query['RescaleType'] = request.rescale_type
        if not UtilClient.is_unset(request.resource_spec):
            query['ResourceSpec'] = request.resource_spec
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        body = {}
        if not UtilClient.is_unset(request.resource_info):
            body['ResourceInfo'] = request.resource_info
        if not UtilClient.is_unset(request.resource_selector):
            body['ResourceSelector'] = request.resource_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RescaleDeviceService',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RescaleDeviceServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rescale_device_service(
        self,
        request: ens_20171110_models.RescaleDeviceServiceRequest,
    ) -> ens_20171110_models.RescaleDeviceServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rescale_device_service_with_options(request, runtime)

    async def rescale_device_service_async(
        self,
        request: ens_20171110_models.RescaleDeviceServiceRequest,
    ) -> ens_20171110_models.RescaleDeviceServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rescale_device_service_with_options_async(request, runtime)

    def reset_aicinstance_with_options(
        self,
        tmp_req: ens_20171110_models.ResetAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResetAICInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.ResetAICInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResetAICInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_aicinstance_with_options_async(
        self,
        tmp_req: ens_20171110_models.ResetAICInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResetAICInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.ResetAICInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAICInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResetAICInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_aicinstance(
        self,
        request: ens_20171110_models.ResetAICInstanceRequest,
    ) -> ens_20171110_models.ResetAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_aicinstance_with_options(request, runtime)

    async def reset_aicinstance_async(
        self,
        request: ens_20171110_models.ResetAICInstanceRequest,
    ) -> ens_20171110_models.ResetAICInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_aicinstance_with_options_async(request, runtime)

    def reset_device_instance_with_options(
        self,
        request: ens_20171110_models.ResetDeviceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResetDeviceInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDeviceInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResetDeviceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_device_instance_with_options_async(
        self,
        request: ens_20171110_models.ResetDeviceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResetDeviceInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDeviceInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResetDeviceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_device_instance(
        self,
        request: ens_20171110_models.ResetDeviceInstanceRequest,
    ) -> ens_20171110_models.ResetDeviceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_device_instance_with_options(request, runtime)

    async def reset_device_instance_async(
        self,
        request: ens_20171110_models.ResetDeviceInstanceRequest,
    ) -> ens_20171110_models.ResetDeviceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_device_instance_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: ens_20171110_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResetDiskResponse:
        """
        When you call this operation, take note of the following items:
        *   The disk must be in the In Use (In_Use) or Unattached (Available) state.
        *   The instance to which the disk is attached must be in the Stopped (Stopped) state. You can call the **StopInstance** operation to stop an instance.
        *   The snapshot specified by the SnapshotId parameter must be created from the disk specified by the DiskId parameter.
        *   When you call the **DescribeInstance** operation to query instance information, if the response contains `{"OperationLocks": {"LockReason" : "security"}}` for an instance, the instance is locked for security reasons and you cannot perform operations on the instance.
        
        @param request: ResetDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResetDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_disk_with_options_async(
        self,
        request: ens_20171110_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResetDiskResponse:
        """
        When you call this operation, take note of the following items:
        *   The disk must be in the In Use (In_Use) or Unattached (Available) state.
        *   The instance to which the disk is attached must be in the Stopped (Stopped) state. You can call the **StopInstance** operation to stop an instance.
        *   The snapshot specified by the SnapshotId parameter must be created from the disk specified by the DiskId parameter.
        *   When you call the **DescribeInstance** operation to query instance information, if the response contains `{"OperationLocks": {"LockReason" : "security"}}` for an instance, the instance is locked for security reasons and you cannot perform operations on the instance.
        
        @param request: ResetDiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetDiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResetDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_disk(
        self,
        request: ens_20171110_models.ResetDiskRequest,
    ) -> ens_20171110_models.ResetDiskResponse:
        """
        When you call this operation, take note of the following items:
        *   The disk must be in the In Use (In_Use) or Unattached (Available) state.
        *   The instance to which the disk is attached must be in the Stopped (Stopped) state. You can call the **StopInstance** operation to stop an instance.
        *   The snapshot specified by the SnapshotId parameter must be created from the disk specified by the DiskId parameter.
        *   When you call the **DescribeInstance** operation to query instance information, if the response contains `{"OperationLocks": {"LockReason" : "security"}}` for an instance, the instance is locked for security reasons and you cannot perform operations on the instance.
        
        @param request: ResetDiskRequest
        @return: ResetDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    async def reset_disk_async(
        self,
        request: ens_20171110_models.ResetDiskRequest,
    ) -> ens_20171110_models.ResetDiskResponse:
        """
        When you call this operation, take note of the following items:
        *   The disk must be in the In Use (In_Use) or Unattached (Available) state.
        *   The instance to which the disk is attached must be in the Stopped (Stopped) state. You can call the **StopInstance** operation to stop an instance.
        *   The snapshot specified by the SnapshotId parameter must be created from the disk specified by the DiskId parameter.
        *   When you call the **DescribeInstance** operation to query instance information, if the response contains `{"OperationLocks": {"LockReason" : "security"}}` for an instance, the instance is locked for security reasons and you cannot perform operations on the instance.
        
        @param request: ResetDiskRequest
        @return: ResetDiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_disk_with_options_async(request, runtime)

    def resize_disk_with_options(
        self,
        request: ens_20171110_models.ResizeDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResizeDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.new_size):
            query['NewSize'] = request.new_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResizeDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_disk_with_options_async(
        self,
        request: ens_20171110_models.ResizeDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ResizeDiskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_id):
            query['DiskId'] = request.disk_id
        if not UtilClient.is_unset(request.new_size):
            query['NewSize'] = request.new_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResizeDisk',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.ResizeDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_disk(
        self,
        request: ens_20171110_models.ResizeDiskRequest,
    ) -> ens_20171110_models.ResizeDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_with_options(request, runtime)

    async def resize_disk_async(
        self,
        request: ens_20171110_models.ResizeDiskRequest,
    ) -> ens_20171110_models.ResizeDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_disk_with_options_async(request, runtime)

    def restart_device_instance_with_options(
        self,
        request: ens_20171110_models.RestartDeviceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RestartDeviceInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDeviceInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RestartDeviceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_device_instance_with_options_async(
        self,
        request: ens_20171110_models.RestartDeviceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RestartDeviceInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDeviceInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RestartDeviceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_device_instance(
        self,
        request: ens_20171110_models.RestartDeviceInstanceRequest,
    ) -> ens_20171110_models.RestartDeviceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_device_instance_with_options(request, runtime)

    async def restart_device_instance_async(
        self,
        request: ens_20171110_models.RestartDeviceInstanceRequest,
    ) -> ens_20171110_models.RestartDeviceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_device_instance_with_options_async(request, runtime)

    def restart_workflow_with_options(
        self,
        tmp_req: ens_20171110_models.RestartWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RestartWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RestartWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RestartWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_workflow_with_options_async(
        self,
        tmp_req: ens_20171110_models.RestartWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RestartWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RestartWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RestartWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_workflow(
        self,
        request: ens_20171110_models.RestartWorkflowRequest,
    ) -> ens_20171110_models.RestartWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_workflow_with_options(request, runtime)

    async def restart_workflow_async(
        self,
        request: ens_20171110_models.RestartWorkflowRequest,
    ) -> ens_20171110_models.RestartWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_workflow_with_options_async(request, runtime)

    def retry_workflow_with_options(
        self,
        tmp_req: ens_20171110_models.RetryWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RetryWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RetryWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RetryWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_workflow_with_options_async(
        self,
        tmp_req: ens_20171110_models.RetryWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RetryWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RetryWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RetryWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_workflow(
        self,
        request: ens_20171110_models.RetryWorkflowRequest,
    ) -> ens_20171110_models.RetryWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_workflow_with_options(request, runtime)

    async def retry_workflow_async(
        self,
        request: ens_20171110_models.RetryWorkflowRequest,
    ) -> ens_20171110_models.RetryWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_workflow_with_options_async(request, runtime)

    def revoke_security_group_with_options(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        """
        In the security group-related API documents, inbound traffic refers to the traffic sent by the source and received by the destination.
        *   You can determine an inbound security group rule by specifying one of the following groups of parameters. You cannot determine a security group rule by specifying only one parameter.
        *   You can specify one or more of the following parameters to remove access control for a CIDR block: IpProtocol, PortRange, Policy, and SourceCidrIp.
        
        @param request: RevokeSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RevokeSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_security_group_with_options_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        """
        In the security group-related API documents, inbound traffic refers to the traffic sent by the source and received by the destination.
        *   You can determine an inbound security group rule by specifying one of the following groups of parameters. You cannot determine a security group rule by specifying only one parameter.
        *   You can specify one or more of the following parameters to remove access control for a CIDR block: IpProtocol, PortRange, Policy, and SourceCidrIp.
        
        @param request: RevokeSecurityGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeSecurityGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSecurityGroup',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RevokeSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_security_group(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        """
        In the security group-related API documents, inbound traffic refers to the traffic sent by the source and received by the destination.
        *   You can determine an inbound security group rule by specifying one of the following groups of parameters. You cannot determine a security group rule by specifying only one parameter.
        *   You can specify one or more of the following parameters to remove access control for a CIDR block: IpProtocol, PortRange, Policy, and SourceCidrIp.
        
        @param request: RevokeSecurityGroupRequest
        @return: RevokeSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_with_options(request, runtime)

    async def revoke_security_group_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        """
        In the security group-related API documents, inbound traffic refers to the traffic sent by the source and received by the destination.
        *   You can determine an inbound security group rule by specifying one of the following groups of parameters. You cannot determine a security group rule by specifying only one parameter.
        *   You can specify one or more of the following parameters to remove access control for a CIDR block: IpProtocol, PortRange, Policy, and SourceCidrIp.
        
        @param request: RevokeSecurityGroupRequest
        @return: RevokeSecurityGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_with_options_async(request, runtime)

    def revoke_security_group_egress_with_options(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        """
        >  In the security group-related API documents, outbound traffic refers to the traffic sent by the source and received by the destination.
        
        @param request: RevokeSecurityGroupEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeSecurityGroupEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSecurityGroupEgress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RevokeSecurityGroupEgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_security_group_egress_with_options_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        """
        >  In the security group-related API documents, outbound traffic refers to the traffic sent by the source and received by the destination.
        
        @param request: RevokeSecurityGroupEgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeSecurityGroupEgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_cidr_ip):
            query['DestCidrIp'] = request.dest_cidr_ip
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.policy):
            query['Policy'] = request.policy
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.source_port_range):
            query['SourcePortRange'] = request.source_port_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeSecurityGroupEgress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RevokeSecurityGroupEgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_security_group_egress(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        """
        >  In the security group-related API documents, outbound traffic refers to the traffic sent by the source and received by the destination.
        
        @param request: RevokeSecurityGroupEgressRequest
        @return: RevokeSecurityGroupEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_egress_with_options(request, runtime)

    async def revoke_security_group_egress_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        """
        >  In the security group-related API documents, outbound traffic refers to the traffic sent by the source and received by the destination.
        
        @param request: RevokeSecurityGroupEgressRequest
        @return: RevokeSecurityGroupEgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_egress_with_options_async(request, runtime)

    def rollback_application_with_options(
        self,
        request: ens_20171110_models.RollbackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RollbackApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.from_app_version):
            query['FromAppVersion'] = request.from_app_version
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.to_app_version):
            query['ToAppVersion'] = request.to_app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RollbackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_application_with_options_async(
        self,
        request: ens_20171110_models.RollbackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RollbackApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.from_app_version):
            query['FromAppVersion'] = request.from_app_version
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.to_app_version):
            query['ToAppVersion'] = request.to_app_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RollbackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_application(
        self,
        request: ens_20171110_models.RollbackApplicationRequest,
    ) -> ens_20171110_models.RollbackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_application_with_options(request, runtime)

    async def rollback_application_async(
        self,
        request: ens_20171110_models.RollbackApplicationRequest,
    ) -> ens_20171110_models.RollbackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_application_with_options_async(request, runtime)

    def rollback_workflow_with_options(
        self,
        tmp_req: ens_20171110_models.RollbackWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RollbackWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RollbackWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RollbackWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_workflow_with_options_async(
        self,
        tmp_req: ens_20171110_models.RollbackWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RollbackWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RollbackWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RollbackWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_workflow(
        self,
        request: ens_20171110_models.RollbackWorkflowRequest,
    ) -> ens_20171110_models.RollbackWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_workflow_with_options(request, runtime)

    async def rollback_workflow_async(
        self,
        request: ens_20171110_models.RollbackWorkflowRequest,
    ) -> ens_20171110_models.RollbackWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_workflow_with_options_async(request, runtime)

    def run_instances_with_options(
        self,
        tmp_req: ens_20171110_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RunInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RunInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_disk):
            request.data_disk_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_disk, 'DataDisk', 'json')
        if not UtilClient.is_unset(tmp_req.system_disk):
            request.system_disk_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.system_disk, 'SystemDisk', 'json')
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.carrier):
            query['Carrier'] = request.carrier
        if not UtilClient.is_unset(request.data_disk_shrink):
            query['DataDisk'] = request.data_disk_shrink
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_strategy):
            query['InstanceChargeStrategy'] = request.instance_charge_strategy
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.net_district_code):
            query['NetDistrictCode'] = request.net_district_code
        if not UtilClient.is_unset(request.net_work_id):
            query['NetWorkId'] = request.net_work_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.public_ip_identification):
            query['PublicIpIdentification'] = request.public_ip_identification
        if not UtilClient.is_unset(request.schedule_area_level):
            query['ScheduleAreaLevel'] = request.schedule_area_level
        if not UtilClient.is_unset(request.scheduling_price_strategy):
            query['SchedulingPriceStrategy'] = request.scheduling_price_strategy
        if not UtilClient.is_unset(request.scheduling_strategy):
            query['SchedulingStrategy'] = request.scheduling_strategy
        if not UtilClient.is_unset(request.security_id):
            query['SecurityId'] = request.security_id
        if not UtilClient.is_unset(request.system_disk_shrink):
            query['SystemDisk'] = request.system_disk_shrink
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RunInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_instances_with_options_async(
        self,
        tmp_req: ens_20171110_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RunInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.RunInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_disk):
            request.data_disk_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_disk, 'DataDisk', 'json')
        if not UtilClient.is_unset(tmp_req.system_disk):
            request.system_disk_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.system_disk, 'SystemDisk', 'json')
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.carrier):
            query['Carrier'] = request.carrier
        if not UtilClient.is_unset(request.data_disk_shrink):
            query['DataDisk'] = request.data_disk_shrink
        if not UtilClient.is_unset(request.ens_region_id):
            query['EnsRegionId'] = request.ens_region_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_strategy):
            query['InstanceChargeStrategy'] = request.instance_charge_strategy
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.net_district_code):
            query['NetDistrictCode'] = request.net_district_code
        if not UtilClient.is_unset(request.net_work_id):
            query['NetWorkId'] = request.net_work_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.public_ip_identification):
            query['PublicIpIdentification'] = request.public_ip_identification
        if not UtilClient.is_unset(request.schedule_area_level):
            query['ScheduleAreaLevel'] = request.schedule_area_level
        if not UtilClient.is_unset(request.scheduling_price_strategy):
            query['SchedulingPriceStrategy'] = request.scheduling_price_strategy
        if not UtilClient.is_unset(request.scheduling_strategy):
            query['SchedulingStrategy'] = request.scheduling_strategy
        if not UtilClient.is_unset(request.security_id):
            query['SecurityId'] = request.security_id
        if not UtilClient.is_unset(request.system_disk_shrink):
            query['SystemDisk'] = request.system_disk_shrink
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unique_suffix):
            query['UniqueSuffix'] = request.unique_suffix
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RunInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_instances(
        self,
        request: ens_20171110_models.RunInstancesRequest,
    ) -> ens_20171110_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_instances_with_options(request, runtime)

    async def run_instances_async(
        self,
        request: ens_20171110_models.RunInstancesRequest,
    ) -> ens_20171110_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_instances_with_options_async(request, runtime)

    def run_service_schedule_with_options(
        self,
        request: ens_20171110_models.RunServiceScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RunServiceScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.directorys):
            query['Directorys'] = request.directorys
        if not UtilClient.is_unset(request.pod_config_name):
            query['PodConfigName'] = request.pod_config_name
        if not UtilClient.is_unset(request.pre_locked_timeout):
            query['PreLockedTimeout'] = request.pre_locked_timeout
        if not UtilClient.is_unset(request.schedule_strategy):
            query['ScheduleStrategy'] = request.schedule_strategy
        if not UtilClient.is_unset(request.service_action):
            query['ServiceAction'] = request.service_action
        if not UtilClient.is_unset(request.service_commands):
            query['ServiceCommands'] = request.service_commands
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunServiceSchedule',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RunServiceScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_service_schedule_with_options_async(
        self,
        request: ens_20171110_models.RunServiceScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RunServiceScheduleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.directorys):
            query['Directorys'] = request.directorys
        if not UtilClient.is_unset(request.pod_config_name):
            query['PodConfigName'] = request.pod_config_name
        if not UtilClient.is_unset(request.pre_locked_timeout):
            query['PreLockedTimeout'] = request.pre_locked_timeout
        if not UtilClient.is_unset(request.schedule_strategy):
            query['ScheduleStrategy'] = request.schedule_strategy
        if not UtilClient.is_unset(request.service_action):
            query['ServiceAction'] = request.service_action
        if not UtilClient.is_unset(request.service_commands):
            query['ServiceCommands'] = request.service_commands
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunServiceSchedule',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.RunServiceScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_service_schedule(
        self,
        request: ens_20171110_models.RunServiceScheduleRequest,
    ) -> ens_20171110_models.RunServiceScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_service_schedule_with_options(request, runtime)

    async def run_service_schedule_async(
        self,
        request: ens_20171110_models.RunServiceScheduleRequest,
    ) -> ens_20171110_models.RunServiceScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_service_schedule_with_options_async(request, runtime)

    def set_backend_servers_with_options(
        self,
        tmp_req: ens_20171110_models.SetBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param tmp_req: SetBackendServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetBackendServersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.SetBackendServersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backend_servers):
            request.backend_servers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backend_servers, 'BackendServers', 'json')
        query = {}
        if not UtilClient.is_unset(request.backend_servers_shrink):
            query['BackendServers'] = request.backend_servers_shrink
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackendServers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_backend_servers_with_options_async(
        self,
        tmp_req: ens_20171110_models.SetBackendServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param tmp_req: SetBackendServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetBackendServersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.SetBackendServersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.backend_servers):
            request.backend_servers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.backend_servers, 'BackendServers', 'json')
        query = {}
        if not UtilClient.is_unset(request.backend_servers_shrink):
            query['BackendServers'] = request.backend_servers_shrink
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackendServers',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetBackendServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_backend_servers(
        self,
        request: ens_20171110_models.SetBackendServersRequest,
    ) -> ens_20171110_models.SetBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: SetBackendServersRequest
        @return: SetBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_backend_servers_with_options(request, runtime)

    async def set_backend_servers_async(
        self,
        request: ens_20171110_models.SetBackendServersRequest,
    ) -> ens_20171110_models.SetBackendServersResponse:
        """
        You can call this operation up to 100 times per second.
        *   You can call this operation up to 10 times per second per account.
        
        @param request: SetBackendServersRequest
        @return: SetBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_backend_servers_with_options_async(request, runtime)

    def set_load_balancer_httplistener_attribute_with_options(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerHTTPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerHTTPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_httplistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerHTTPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerHTTPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_httplistener_attribute(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerHTTPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPListenerAttributeRequest
        @return: SetLoadBalancerHTTPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_httplistener_attribute_async(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerHTTPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPListenerAttributeRequest
        @return: SetLoadBalancerHTTPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_httplistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_httpslistener_attribute_with_options(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPSListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerHTTPSListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPSListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_httpslistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPSListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerHTTPSListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPSListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_httpslistener_attribute(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPSListenerAttributeRequest
        @return: SetLoadBalancerHTTPSListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httpslistener_attribute_with_options(request, runtime)

    async def set_load_balancer_httpslistener_attribute_async(
        self,
        request: ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerHTTPSListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerHTTPSListenerAttributeRequest
        @return: SetLoadBalancerHTTPSListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_httpslistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_status_with_options(
        self,
        request: ens_20171110_models.SetLoadBalancerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerStatusResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerStatus',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_status_with_options_async(
        self,
        request: ens_20171110_models.SetLoadBalancerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerStatusResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerStatus',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_status(
        self,
        request: ens_20171110_models.SetLoadBalancerStatusRequest,
    ) -> ens_20171110_models.SetLoadBalancerStatusResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerStatusRequest
        @return: SetLoadBalancerStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_status_with_options(request, runtime)

    async def set_load_balancer_status_async(
        self,
        request: ens_20171110_models.SetLoadBalancerStatusRequest,
    ) -> ens_20171110_models.SetLoadBalancerStatusResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerStatusRequest
        @return: SetLoadBalancerStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_status_with_options_async(request, runtime)

    def set_load_balancer_tcplistener_attribute_with_options(
        self,
        request: ens_20171110_models.SetLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerTCPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerTCPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerTCPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_tcplistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.SetLoadBalancerTCPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerTCPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerTCPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerTCPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerTCPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_tcplistener_attribute(
        self,
        request: ens_20171110_models.SetLoadBalancerTCPListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerTCPListenerAttributeRequest
        @return: SetLoadBalancerTCPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_tcplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_tcplistener_attribute_async(
        self,
        request: ens_20171110_models.SetLoadBalancerTCPListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerTCPListenerAttributeResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerTCPListenerAttributeRequest
        @return: SetLoadBalancerTCPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_tcplistener_attribute_with_options_async(request, runtime)

    def set_load_balancer_udplistener_attribute_with_options(
        self,
        request: ens_20171110_models.SetLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerUDPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerUDPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerUDPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_exp):
            query['HealthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_req):
            query['HealthCheckReq'] = request.health_check_req
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerUDPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_load_balancer_udplistener_attribute_with_options_async(
        self,
        request: ens_20171110_models.SetLoadBalancerUDPListenerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SetLoadBalancerUDPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerUDPListenerAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoadBalancerUDPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_transmit):
            query['EipTransmit'] = request.eip_transmit
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_exp):
            query['HealthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_req):
            query['HealthCheckReq'] = request.health_check_req
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerUDPListenerAttribute',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.SetLoadBalancerUDPListenerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_load_balancer_udplistener_attribute(
        self,
        request: ens_20171110_models.SetLoadBalancerUDPListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerUDPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerUDPListenerAttributeRequest
        @return: SetLoadBalancerUDPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_udplistener_attribute_with_options(request, runtime)

    async def set_load_balancer_udplistener_attribute_async(
        self,
        request: ens_20171110_models.SetLoadBalancerUDPListenerAttributeRequest,
    ) -> ens_20171110_models.SetLoadBalancerUDPListenerAttributeResponse:
        """
        >
        *   You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: SetLoadBalancerUDPListenerAttributeRequest
        @return: SetLoadBalancerUDPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_load_balancer_udplistener_attribute_with_options_async(request, runtime)

    def start_epn_instance_with_options(
        self,
        request: ens_20171110_models.StartEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.StartEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_epn_instance(
        self,
        request: ens_20171110_models.StartEpnInstanceRequest,
    ) -> ens_20171110_models.StartEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_epn_instance_with_options(request, runtime)

    async def start_epn_instance_async(
        self,
        request: ens_20171110_models.StartEpnInstanceRequest,
    ) -> ens_20171110_models.StartEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_epn_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: ens_20171110_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartInstanceResponse:
        """
        You can call the operation only when the instance is in the Stopped state.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: ens_20171110_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartInstanceResponse:
        """
        You can call the operation only when the instance is in the Stopped state.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: ens_20171110_models.StartInstanceRequest,
    ) -> ens_20171110_models.StartInstanceResponse:
        """
        You can call the operation only when the instance is in the Stopped state.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: ens_20171110_models.StartInstanceRequest,
    ) -> ens_20171110_models.StartInstanceResponse:
        """
        You can call the operation only when the instance is in the Stopped state.
        *   If the operation is successful, the status of the instance becomes Starting.
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def start_instances_with_options(
        self,
        tmp_req: ens_20171110_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.StartInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instances_with_options_async(
        self,
        tmp_req: ens_20171110_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.StartInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instances(
        self,
        request: ens_20171110_models.StartInstancesRequest,
    ) -> ens_20171110_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    async def start_instances_async(
        self,
        request: ens_20171110_models.StartInstancesRequest,
    ) -> ens_20171110_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instances_with_options_async(request, runtime)

    def start_load_balancer_listener_with_options(
        self,
        request: ens_20171110_models.StartLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StartLoadBalancerListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLoadBalancerListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_load_balancer_listener_with_options_async(
        self,
        request: ens_20171110_models.StartLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StartLoadBalancerListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLoadBalancerListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_load_balancer_listener(
        self,
        request: ens_20171110_models.StartLoadBalancerListenerRequest,
    ) -> ens_20171110_models.StartLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StartLoadBalancerListenerRequest
        @return: StartLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_load_balancer_listener_with_options(request, runtime)

    async def start_load_balancer_listener_async(
        self,
        request: ens_20171110_models.StartLoadBalancerListenerRequest,
    ) -> ens_20171110_models.StartLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StartLoadBalancerListenerRequest
        @return: StartLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_load_balancer_listener_with_options_async(request, runtime)

    def start_snat_ip_for_snat_entry_with_options(
        self,
        request: ens_20171110_models.StartSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartSnatIpForSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_snat_ip_for_snat_entry_with_options_async(
        self,
        request: ens_20171110_models.StartSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StartSnatIpForSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_snat_ip_for_snat_entry(
        self,
        request: ens_20171110_models.StartSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.StartSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_snat_ip_for_snat_entry_with_options(request, runtime)

    async def start_snat_ip_for_snat_entry_async(
        self,
        request: ens_20171110_models.StartSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.StartSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_snat_ip_for_snat_entry_with_options_async(request, runtime)

    def stop_epn_instance_with_options(
        self,
        request: ens_20171110_models.StopEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopEpnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.StopEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopEpnInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.epninstance_id):
            query['EPNInstanceId'] = request.epninstance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopEpnInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopEpnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_epn_instance(
        self,
        request: ens_20171110_models.StopEpnInstanceRequest,
    ) -> ens_20171110_models.StopEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_epn_instance_with_options(request, runtime)

    async def stop_epn_instance_async(
        self,
        request: ens_20171110_models.StopEpnInstanceRequest,
    ) -> ens_20171110_models.StopEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_epn_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: ens_20171110_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopInstanceResponse:
        """
        You can call this operation to stop instances that are only in the Running state.
        *   If the call is successful, the state of the instance becomes Stopping.
        *   Once the instance is stopped, the state of the instance becomes Stopped.
        *   Force stop is supported, which is equivalent to power-off. Data that is not written to disks on the instance may be lost.
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: ens_20171110_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopInstanceResponse:
        """
        You can call this operation to stop instances that are only in the Running state.
        *   If the call is successful, the state of the instance becomes Stopping.
        *   Once the instance is stopped, the state of the instance becomes Stopped.
        *   Force stop is supported, which is equivalent to power-off. Data that is not written to disks on the instance may be lost.
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_stop):
            query['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: ens_20171110_models.StopInstanceRequest,
    ) -> ens_20171110_models.StopInstanceResponse:
        """
        You can call this operation to stop instances that are only in the Running state.
        *   If the call is successful, the state of the instance becomes Stopping.
        *   Once the instance is stopped, the state of the instance becomes Stopped.
        *   Force stop is supported, which is equivalent to power-off. Data that is not written to disks on the instance may be lost.
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: ens_20171110_models.StopInstanceRequest,
    ) -> ens_20171110_models.StopInstanceResponse:
        """
        You can call this operation to stop instances that are only in the Running state.
        *   If the call is successful, the state of the instance becomes Stopping.
        *   Once the instance is stopped, the state of the instance becomes Stopped.
        *   Force stop is supported, which is equivalent to power-off. Data that is not written to disks on the instance may be lost.
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def stop_instances_with_options(
        self,
        tmp_req: ens_20171110_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.StopInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instances_with_options_async(
        self,
        tmp_req: ens_20171110_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.StopInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstances',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instances(
        self,
        request: ens_20171110_models.StopInstancesRequest,
    ) -> ens_20171110_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    async def stop_instances_async(
        self,
        request: ens_20171110_models.StopInstancesRequest,
    ) -> ens_20171110_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instances_with_options_async(request, runtime)

    def stop_load_balancer_listener_with_options(
        self,
        request: ens_20171110_models.StopLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StopLoadBalancerListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLoadBalancerListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_load_balancer_listener_with_options_async(
        self,
        request: ens_20171110_models.StopLoadBalancerListenerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StopLoadBalancerListenerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLoadBalancerListener',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopLoadBalancerListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_load_balancer_listener(
        self,
        request: ens_20171110_models.StopLoadBalancerListenerRequest,
    ) -> ens_20171110_models.StopLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StopLoadBalancerListenerRequest
        @return: StopLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_load_balancer_listener_with_options(request, runtime)

    async def stop_load_balancer_listener_async(
        self,
        request: ens_20171110_models.StopLoadBalancerListenerRequest,
    ) -> ens_20171110_models.StopLoadBalancerListenerResponse:
        """
        You can call this operation up to 100 times per second per account.
        *   You can call this operation up to 10 times per second per user.
        
        @param request: StopLoadBalancerListenerRequest
        @return: StopLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_load_balancer_listener_with_options_async(request, runtime)

    def stop_snat_ip_for_snat_entry_with_options(
        self,
        request: ens_20171110_models.StopSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopSnatIpForSnatEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_snat_ip_for_snat_entry_with_options_async(
        self,
        request: ens_20171110_models.StopSnatIpForSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopSnatIpForSnatEntryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snat_entry_id):
            query['SnatEntryId'] = request.snat_entry_id
        if not UtilClient.is_unset(request.snat_ip):
            query['SnatIp'] = request.snat_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSnatIpForSnatEntry',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.StopSnatIpForSnatEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_snat_ip_for_snat_entry(
        self,
        request: ens_20171110_models.StopSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.StopSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_snat_ip_for_snat_entry_with_options(request, runtime)

    async def stop_snat_ip_for_snat_entry_async(
        self,
        request: ens_20171110_models.StopSnatIpForSnatEntryRequest,
    ) -> ens_20171110_models.StopSnatIpForSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_snat_ip_for_snat_entry_with_options_async(request, runtime)

    def terminate_workflow_with_options(
        self,
        tmp_req: ens_20171110_models.TerminateWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.TerminateWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.TerminateWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.TerminateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_workflow_with_options_async(
        self,
        tmp_req: ens_20171110_models.TerminateWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.TerminateWorkflowResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.TerminateWorkflowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workflow_ids):
            request.workflow_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workflow_ids, 'WorkflowIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.workflow_ids_shrink):
            query['WorkflowIds'] = request.workflow_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateWorkflow',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.TerminateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_workflow(
        self,
        request: ens_20171110_models.TerminateWorkflowRequest,
    ) -> ens_20171110_models.TerminateWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_workflow_with_options(request, runtime)

    async def terminate_workflow_async(
        self,
        request: ens_20171110_models.TerminateWorkflowRequest,
    ) -> ens_20171110_models.TerminateWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_workflow_with_options_async(request, runtime)

    def un_associate_ens_eip_address_with_options(
        self,
        request: ens_20171110_models.UnAssociateEnsEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnAssociateEnsEipAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnAssociateEnsEipAddress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UnAssociateEnsEipAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_associate_ens_eip_address_with_options_async(
        self,
        request: ens_20171110_models.UnAssociateEnsEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnAssociateEnsEipAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allocation_id):
            query['AllocationId'] = request.allocation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnAssociateEnsEipAddress',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UnAssociateEnsEipAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_associate_ens_eip_address(
        self,
        request: ens_20171110_models.UnAssociateEnsEipAddressRequest,
    ) -> ens_20171110_models.UnAssociateEnsEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_associate_ens_eip_address_with_options(request, runtime)

    async def un_associate_ens_eip_address_async(
        self,
        request: ens_20171110_models.UnAssociateEnsEipAddressRequest,
    ) -> ens_20171110_models.UnAssociateEnsEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_associate_ens_eip_address_with_options_async(request, runtime)

    def unassign_private_ip_addresses_with_options(
        self,
        request: ens_20171110_models.UnassignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnassignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassignPrivateIpAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UnassignPrivateIpAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassign_private_ip_addresses_with_options_async(
        self,
        request: ens_20171110_models.UnassignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnassignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_interface_id):
            query['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassignPrivateIpAddresses',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UnassignPrivateIpAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassign_private_ip_addresses(
        self,
        request: ens_20171110_models.UnassignPrivateIpAddressesRequest,
    ) -> ens_20171110_models.UnassignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassign_private_ip_addresses_with_options(request, runtime)

    async def unassign_private_ip_addresses_async(
        self,
        request: ens_20171110_models.UnassignPrivateIpAddressesRequest,
    ) -> ens_20171110_models.UnassignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassign_private_ip_addresses_with_options_async(request, runtime)

    def unassociate_network_acl_with_options(
        self,
        request: ens_20171110_models.UnassociateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnassociateNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassociateNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UnassociateNetworkAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassociate_network_acl_with_options_async(
        self,
        request: ens_20171110_models.UnassociateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnassociateNetworkAclResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_acl_id):
            query['NetworkAclId'] = request.network_acl_id
        if not UtilClient.is_unset(request.resource):
            query['Resource'] = request.resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnassociateNetworkAcl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UnassociateNetworkAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassociate_network_acl(
        self,
        request: ens_20171110_models.UnassociateNetworkAclRequest,
    ) -> ens_20171110_models.UnassociateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_network_acl_with_options(request, runtime)

    async def unassociate_network_acl_async(
        self,
        request: ens_20171110_models.UnassociateNetworkAclRequest,
    ) -> ens_20171110_models.UnassociateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_network_acl_with_options_async(request, runtime)

    def update_ens_sale_control_with_options(
        self,
        tmp_req: ens_20171110_models.UpdateEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpdateEnsSaleControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.UpdateEnsSaleControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UpdateEnsSaleControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ens_sale_control_with_options_async(
        self,
        tmp_req: ens_20171110_models.UpdateEnsSaleControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpdateEnsSaleControlResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.UpdateEnsSaleControlShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sale_controls):
            request.sale_controls_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sale_controls, 'SaleControls', 'json')
        query = {}
        if not UtilClient.is_unset(request.ali_uid_account):
            query['AliUidAccount'] = request.ali_uid_account
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.sale_controls_shrink):
            query['SaleControls'] = request.sale_controls_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnsSaleControl',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UpdateEnsSaleControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ens_sale_control(
        self,
        request: ens_20171110_models.UpdateEnsSaleControlRequest,
    ) -> ens_20171110_models.UpdateEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ens_sale_control_with_options(request, runtime)

    async def update_ens_sale_control_async(
        self,
        request: ens_20171110_models.UpdateEnsSaleControlRequest,
    ) -> ens_20171110_models.UpdateEnsSaleControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ens_sale_control_with_options_async(request, runtime)

    def upgrade_aicinstance_image_with_options(
        self,
        tmp_req: ens_20171110_models.UpgradeAICInstanceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpgradeAICInstanceImageResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.UpgradeAICInstanceImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.server_ids):
            request.server_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.server_ids, 'ServerIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeAICInstanceImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UpgradeAICInstanceImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_aicinstance_image_with_options_async(
        self,
        tmp_req: ens_20171110_models.UpgradeAICInstanceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpgradeAICInstanceImageResponse:
        UtilClient.validate_model(tmp_req)
        request = ens_20171110_models.UpgradeAICInstanceImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.server_ids):
            request.server_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.server_ids, 'ServerIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeAICInstanceImage',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UpgradeAICInstanceImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_aicinstance_image(
        self,
        request: ens_20171110_models.UpgradeAICInstanceImageRequest,
    ) -> ens_20171110_models.UpgradeAICInstanceImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_aicinstance_image_with_options(request, runtime)

    async def upgrade_aicinstance_image_async(
        self,
        request: ens_20171110_models.UpgradeAICInstanceImageRequest,
    ) -> ens_20171110_models.UpgradeAICInstanceImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_aicinstance_image_with_options_async(request, runtime)

    def upgrade_application_with_options(
        self,
        request: ens_20171110_models.UpgradeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpgradeApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UpgradeApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_application_with_options_async(
        self,
        request: ens_20171110_models.UpgradeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpgradeApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeApplication',
            version='2017-11-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ens_20171110_models.UpgradeApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_application(
        self,
        request: ens_20171110_models.UpgradeApplicationRequest,
    ) -> ens_20171110_models.UpgradeApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_application_with_options(request, runtime)

    async def upgrade_application_async(
        self,
        request: ens_20171110_models.UpgradeApplicationRequest,
    ) -> ens_20171110_models.UpgradeApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_application_with_options_async(request, runtime)
