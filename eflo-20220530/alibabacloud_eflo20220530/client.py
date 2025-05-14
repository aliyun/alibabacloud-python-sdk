# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eflo20220530 import models as eflo_20220530_models
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
        self._endpoint = self.get_endpoint('eflo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assign_leni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.AssignLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssignLeniPrivateIpAddressResponse:
        """
        @summary Apply for a secondary private IP address for the current Lingjun Elastic Network Interface. You can automatically assign a secondary private IP address.
        
        @description Apply for a secondary private IP address for the specified Lingjun Elastic Network Interface.
        If the PrivateIp field is empty, a secondary private IP address is automatically assigned and the unique identifier of the IP address is returned.
        You can use the GetLeniPrivateIpAddress or ListLeniPrivateIpAddresses interface to check whether the secondary private IP address is assigned.
        
        @param request: AssignLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssignLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_leni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.AssignLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssignLeniPrivateIpAddressResponse:
        """
        @summary Apply for a secondary private IP address for the current Lingjun Elastic Network Interface. You can automatically assign a secondary private IP address.
        
        @description Apply for a secondary private IP address for the specified Lingjun Elastic Network Interface.
        If the PrivateIp field is empty, a secondary private IP address is automatically assigned and the unique identifier of the IP address is returned.
        You can use the GetLeniPrivateIpAddress or ListLeniPrivateIpAddresses interface to check whether the secondary private IP address is assigned.
        
        @param request: AssignLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssignLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_leni_private_ip_address(
        self,
        request: eflo_20220530_models.AssignLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.AssignLeniPrivateIpAddressResponse:
        """
        @summary Apply for a secondary private IP address for the current Lingjun Elastic Network Interface. You can automatically assign a secondary private IP address.
        
        @description Apply for a secondary private IP address for the specified Lingjun Elastic Network Interface.
        If the PrivateIp field is empty, a secondary private IP address is automatically assigned and the unique identifier of the IP address is returned.
        You can use the GetLeniPrivateIpAddress or ListLeniPrivateIpAddresses interface to check whether the secondary private IP address is assigned.
        
        @param request: AssignLeniPrivateIpAddressRequest
        @return: AssignLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_leni_private_ip_address_with_options(request, runtime)

    async def assign_leni_private_ip_address_async(
        self,
        request: eflo_20220530_models.AssignLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.AssignLeniPrivateIpAddressResponse:
        """
        @summary Apply for a secondary private IP address for the current Lingjun Elastic Network Interface. You can automatically assign a secondary private IP address.
        
        @description Apply for a secondary private IP address for the specified Lingjun Elastic Network Interface.
        If the PrivateIp field is empty, a secondary private IP address is automatically assigned and the unique identifier of the IP address is returned.
        You can use the GetLeniPrivateIpAddress or ListLeniPrivateIpAddresses interface to check whether the secondary private IP address is assigned.
        
        @param request: AssignLeniPrivateIpAddressRequest
        @return: AssignLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_leni_private_ip_address_with_options_async(request, runtime)

    def assign_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        """
        @summary Applies for a private secondary IP address for the current LNI. You can also call this operation to assign a secondary MAC address to the current LNI.
        
        @description >  Apply for secondary private IP addresses
        By default, each network interface controller can apply for three secondary private IP addresses. If the quota is exceeded, contact the administrator.
        The secondary private IP address is allocated from the Lingjun subnet to which the current network interface controller belongs. The first address and the last two addresses belong to reserved addresses and do not participate in the allocation.
        
        @param request: AssignPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_mac):
            body['AssignMac'] = request.assign_mac
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_config):
            body['SkipConfig'] = request.skip_config
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        """
        @summary Applies for a private secondary IP address for the current LNI. You can also call this operation to assign a secondary MAC address to the current LNI.
        
        @description >  Apply for secondary private IP addresses
        By default, each network interface controller can apply for three secondary private IP addresses. If the quota is exceeded, contact the administrator.
        The secondary private IP address is allocated from the Lingjun subnet to which the current network interface controller belongs. The first address and the last two addresses belong to reserved addresses and do not participate in the allocation.
        
        @param request: AssignPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_mac):
            body['AssignMac'] = request.assign_mac
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_config):
            body['SkipConfig'] = request.skip_config
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssignPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_private_ip_address(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        """
        @summary Applies for a private secondary IP address for the current LNI. You can also call this operation to assign a secondary MAC address to the current LNI.
        
        @description >  Apply for secondary private IP addresses
        By default, each network interface controller can apply for three secondary private IP addresses. If the quota is exceeded, contact the administrator.
        The secondary private IP address is allocated from the Lingjun subnet to which the current network interface controller belongs. The first address and the last two addresses belong to reserved addresses and do not participate in the allocation.
        
        @param request: AssignPrivateIpAddressRequest
        @return: AssignPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_private_ip_address_with_options(request, runtime)

    async def assign_private_ip_address_async(
        self,
        request: eflo_20220530_models.AssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.AssignPrivateIpAddressResponse:
        """
        @summary Applies for a private secondary IP address for the current LNI. You can also call this operation to assign a secondary MAC address to the current LNI.
        
        @description >  Apply for secondary private IP addresses
        By default, each network interface controller can apply for three secondary private IP addresses. If the quota is exceeded, contact the administrator.
        The secondary private IP address is allocated from the Lingjun subnet to which the current network interface controller belongs. The first address and the last two addresses belong to reserved addresses and do not participate in the allocation.
        
        @param request: AssignPrivateIpAddressRequest
        @return: AssignPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_private_ip_address_with_options_async(request, runtime)

    def associate_vpd_cidr_block_with_options(
        self,
        request: eflo_20220530_models.AssociateVpdCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssociateVpdCidrBlockResponse:
        """
        @summary When the VPD primary network segment address is not enough to allocate, you can choose to create an additional network segment as the additional network segment of the VPD primary network segment.
        
        @description >  *Add a CIDR block**\
        The CIDR block cannot start with 0. The subnet mask must be 8 to 28 bits in length.
        The secondary IPv4 CIDR block must not overlap with the primary IPv4 CIDR block of the Lingjun CIDR block and the added secondary IPv4 CIDR block.
        You cannot use 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 as the CIDR block of Lingjun. Example: In the Lingjun CIDR block whose primary IPv4 CIDR block is 192.168.0.0/16, you cannot add the following CIDR blocks as additional IPv4 CIDR blocks. The CIDR block that is in the same range as 192.168.0.0/16. A CIDR block that is larger than 192.168.0.0/16. Example: 192.168.0.0/8. A CIDR block that is smaller than 192.168.0.0/16. Example: 192.168.0.0/24.
        By default, each tenant can create three additional CIDR blocks in each region.
        
        @param request: AssociateVpdCidrBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateVpdCidrBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateVpdCidrBlock',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssociateVpdCidrBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_vpd_cidr_block_with_options_async(
        self,
        request: eflo_20220530_models.AssociateVpdCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AssociateVpdCidrBlockResponse:
        """
        @summary When the VPD primary network segment address is not enough to allocate, you can choose to create an additional network segment as the additional network segment of the VPD primary network segment.
        
        @description >  *Add a CIDR block**\
        The CIDR block cannot start with 0. The subnet mask must be 8 to 28 bits in length.
        The secondary IPv4 CIDR block must not overlap with the primary IPv4 CIDR block of the Lingjun CIDR block and the added secondary IPv4 CIDR block.
        You cannot use 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 as the CIDR block of Lingjun. Example: In the Lingjun CIDR block whose primary IPv4 CIDR block is 192.168.0.0/16, you cannot add the following CIDR blocks as additional IPv4 CIDR blocks. The CIDR block that is in the same range as 192.168.0.0/16. A CIDR block that is larger than 192.168.0.0/16. Example: 192.168.0.0/8. A CIDR block that is smaller than 192.168.0.0/16. Example: 192.168.0.0/24.
        By default, each tenant can create three additional CIDR blocks in each region.
        
        @param request: AssociateVpdCidrBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateVpdCidrBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateVpdCidrBlock',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AssociateVpdCidrBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_vpd_cidr_block(
        self,
        request: eflo_20220530_models.AssociateVpdCidrBlockRequest,
    ) -> eflo_20220530_models.AssociateVpdCidrBlockResponse:
        """
        @summary When the VPD primary network segment address is not enough to allocate, you can choose to create an additional network segment as the additional network segment of the VPD primary network segment.
        
        @description >  *Add a CIDR block**\
        The CIDR block cannot start with 0. The subnet mask must be 8 to 28 bits in length.
        The secondary IPv4 CIDR block must not overlap with the primary IPv4 CIDR block of the Lingjun CIDR block and the added secondary IPv4 CIDR block.
        You cannot use 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 as the CIDR block of Lingjun. Example: In the Lingjun CIDR block whose primary IPv4 CIDR block is 192.168.0.0/16, you cannot add the following CIDR blocks as additional IPv4 CIDR blocks. The CIDR block that is in the same range as 192.168.0.0/16. A CIDR block that is larger than 192.168.0.0/16. Example: 192.168.0.0/8. A CIDR block that is smaller than 192.168.0.0/16. Example: 192.168.0.0/24.
        By default, each tenant can create three additional CIDR blocks in each region.
        
        @param request: AssociateVpdCidrBlockRequest
        @return: AssociateVpdCidrBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_vpd_cidr_block_with_options(request, runtime)

    async def associate_vpd_cidr_block_async(
        self,
        request: eflo_20220530_models.AssociateVpdCidrBlockRequest,
    ) -> eflo_20220530_models.AssociateVpdCidrBlockResponse:
        """
        @summary When the VPD primary network segment address is not enough to allocate, you can choose to create an additional network segment as the additional network segment of the VPD primary network segment.
        
        @description >  *Add a CIDR block**\
        The CIDR block cannot start with 0. The subnet mask must be 8 to 28 bits in length.
        The secondary IPv4 CIDR block must not overlap with the primary IPv4 CIDR block of the Lingjun CIDR block and the added secondary IPv4 CIDR block.
        You cannot use 100.64.0.0/10, 224.0.0.0/4, 127.0.0.0/8, or 169.254.0.0/16 as the CIDR block of Lingjun. Example: In the Lingjun CIDR block whose primary IPv4 CIDR block is 192.168.0.0/16, you cannot add the following CIDR blocks as additional IPv4 CIDR blocks. The CIDR block that is in the same range as 192.168.0.0/16. A CIDR block that is larger than 192.168.0.0/16. Example: 192.168.0.0/8. A CIDR block that is smaller than 192.168.0.0/16. Example: 192.168.0.0/24.
        By default, each tenant can create three additional CIDR blocks in each region.
        
        @param request: AssociateVpdCidrBlockRequest
        @return: AssociateVpdCidrBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_vpd_cidr_block_with_options_async(request, runtime)

    def attach_elastic_network_interface_with_options(
        self,
        request: eflo_20220530_models.AttachElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AttachElasticNetworkInterfaceResponse:
        """
        @summary Lingjun ENI is bound to NC.
        
        @description This interface is an asynchronous interface. You need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the available state.
        
        @param request: AttachElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AttachElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_elastic_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.AttachElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.AttachElasticNetworkInterfaceResponse:
        """
        @summary Lingjun ENI is bound to NC.
        
        @description This interface is an asynchronous interface. You need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the available state.
        
        @param request: AttachElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.AttachElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_elastic_network_interface(
        self,
        request: eflo_20220530_models.AttachElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.AttachElasticNetworkInterfaceResponse:
        """
        @summary Lingjun ENI is bound to NC.
        
        @description This interface is an asynchronous interface. You need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the available state.
        
        @param request: AttachElasticNetworkInterfaceRequest
        @return: AttachElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_elastic_network_interface_with_options(request, runtime)

    async def attach_elastic_network_interface_async(
        self,
        request: eflo_20220530_models.AttachElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.AttachElasticNetworkInterfaceResponse:
        """
        @summary Lingjun ENI is bound to NC.
        
        @description This interface is an asynchronous interface. You need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the available state.
        
        @param request: AttachElasticNetworkInterfaceRequest
        @return: AttachElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_elastic_network_interface_with_options_async(request, runtime)

    def create_elastic_network_interface_with_options(
        self,
        request: eflo_20220530_models.CreateElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateElasticNetworkInterfaceResponse:
        """
        @summary Creates an LENI.
        
        @param request: CreateElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.CreateElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateElasticNetworkInterfaceResponse:
        """
        @summary Creates an LENI.
        
        @param request: CreateElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_jumbo_frame):
            body['EnableJumboFrame'] = request.enable_jumbo_frame
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_network_interface(
        self,
        request: eflo_20220530_models.CreateElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.CreateElasticNetworkInterfaceResponse:
        """
        @summary Creates an LENI.
        
        @param request: CreateElasticNetworkInterfaceRequest
        @return: CreateElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_elastic_network_interface_with_options(request, runtime)

    async def create_elastic_network_interface_async(
        self,
        request: eflo_20220530_models.CreateElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.CreateElasticNetworkInterfaceResponse:
        """
        @summary Creates an LENI.
        
        @param request: CreateElasticNetworkInterfaceRequest
        @return: CreateElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_elastic_network_interface_with_options_async(request, runtime)

    def create_er_with_options(
        self,
        request: eflo_20220530_models.CreateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErResponse:
        """
        @summary Create a Lingjun HUB.
        
        @description When you call this operation to create a Lingjun HUB, note that:
        Make sure that you have sufficient Lingjun HUB quota.
        This interface is an asynchronous interface. After this interface is called, the system will return the ID of a Lingjun HUB. At this time, the Lingjun HUB instance may not be created yet, and the system background creation task is still in progress. You can call the ListErs or GetEr operation to query the status of the Lingjun HUB.
        If the status of the Lingjun HUB is Executing, it indicates that it is being created.
        If the status of the Lingjun HUB is Available, the creation is successful.
        
        @param request: CreateErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_with_options_async(
        self,
        request: eflo_20220530_models.CreateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErResponse:
        """
        @summary Create a Lingjun HUB.
        
        @description When you call this operation to create a Lingjun HUB, note that:
        Make sure that you have sufficient Lingjun HUB quota.
        This interface is an asynchronous interface. After this interface is called, the system will return the ID of a Lingjun HUB. At this time, the Lingjun HUB instance may not be created yet, and the system background creation task is still in progress. You can call the ListErs or GetEr operation to query the status of the Lingjun HUB.
        If the status of the Lingjun HUB is Executing, it indicates that it is being created.
        If the status of the Lingjun HUB is Available, the creation is successful.
        
        @param request: CreateErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er(
        self,
        request: eflo_20220530_models.CreateErRequest,
    ) -> eflo_20220530_models.CreateErResponse:
        """
        @summary Create a Lingjun HUB.
        
        @description When you call this operation to create a Lingjun HUB, note that:
        Make sure that you have sufficient Lingjun HUB quota.
        This interface is an asynchronous interface. After this interface is called, the system will return the ID of a Lingjun HUB. At this time, the Lingjun HUB instance may not be created yet, and the system background creation task is still in progress. You can call the ListErs or GetEr operation to query the status of the Lingjun HUB.
        If the status of the Lingjun HUB is Executing, it indicates that it is being created.
        If the status of the Lingjun HUB is Available, the creation is successful.
        
        @param request: CreateErRequest
        @return: CreateErResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_er_with_options(request, runtime)

    async def create_er_async(
        self,
        request: eflo_20220530_models.CreateErRequest,
    ) -> eflo_20220530_models.CreateErResponse:
        """
        @summary Create a Lingjun HUB.
        
        @description When you call this operation to create a Lingjun HUB, note that:
        Make sure that you have sufficient Lingjun HUB quota.
        This interface is an asynchronous interface. After this interface is called, the system will return the ID of a Lingjun HUB. At this time, the Lingjun HUB instance may not be created yet, and the system background creation task is still in progress. You can call the ListErs or GetEr operation to query the status of the Lingjun HUB.
        If the status of the Lingjun HUB is Executing, it indicates that it is being created.
        If the status of the Lingjun HUB is Available, the creation is successful.
        
        @param request: CreateErRequest
        @return: CreateErResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_er_with_options_async(request, runtime)

    def create_er_attachment_with_options(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        """
        @summary Create a network instance connection.
        
        @description When you call this operation to create a network instance connection, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have sufficient quota for network instance connections.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the network instance connection. In this case, the network instance connection may not be created yet, and the system is still creating the network instance in the background. You can query the connection status of a network instance by ListErAttachments or GetErAttachment:
        If the connection status of the network instance is Executing, the network instance is being created.
        If the connection status of the network instance is Available, the network instance is created.
        
        @param request: CreateErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        """
        @summary Create a network instance connection.
        
        @description When you call this operation to create a network instance connection, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have sufficient quota for network instance connections.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the network instance connection. In this case, the network instance connection may not be created yet, and the system is still creating the network instance in the background. You can query the connection status of a network instance by ListErAttachments or GetErAttachment:
        If the connection status of the network instance is Executing, the network instance is being created.
        If the connection status of the network instance is Available, the network instance is created.
        
        @param request: CreateErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er_attachment(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        """
        @summary Create a network instance connection.
        
        @description When you call this operation to create a network instance connection, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have sufficient quota for network instance connections.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the network instance connection. In this case, the network instance connection may not be created yet, and the system is still creating the network instance in the background. You can query the connection status of a network instance by ListErAttachments or GetErAttachment:
        If the connection status of the network instance is Executing, the network instance is being created.
        If the connection status of the network instance is Available, the network instance is created.
        
        @param request: CreateErAttachmentRequest
        @return: CreateErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_er_attachment_with_options(request, runtime)

    async def create_er_attachment_async(
        self,
        request: eflo_20220530_models.CreateErAttachmentRequest,
    ) -> eflo_20220530_models.CreateErAttachmentResponse:
        """
        @summary Create a network instance connection.
        
        @description When you call this operation to create a network instance connection, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have sufficient quota for network instance connections.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the network instance connection. In this case, the network instance connection may not be created yet, and the system is still creating the network instance in the background. You can query the connection status of a network instance by ListErAttachments or GetErAttachment:
        If the connection status of the network instance is Executing, the network instance is being created.
        If the connection status of the network instance is Available, the network instance is created.
        
        @param request: CreateErAttachmentRequest
        @return: CreateErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_er_attachment_with_options_async(request, runtime)

    def create_er_route_map_with_options(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        """
        @summary Users can use this API to create routing policy by specifying the network instance connection under Lingjun HUB.
        
        @description When you call this operation to create a routing policy, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have created a network instance connection.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the routing policy. In this case, the routing policy instance may not be created yet, and the system background creation task is still in progress. You can use ListErRouteMaps or GetErRouteMap to query the status of a routing policy.
        If the status of the routing policy is Execute, the system is creating the instance.
        If the status of the routing policy is Available, the creation is successful.
        
        @param request: CreateErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_owner):
            body['ReceptionInstanceOwner'] = request.reception_instance_owner
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.route_map_num):
            body['RouteMapNum'] = request.route_map_num
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_owner):
            body['TransmissionInstanceOwner'] = request.transmission_instance_owner
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        """
        @summary Users can use this API to create routing policy by specifying the network instance connection under Lingjun HUB.
        
        @description When you call this operation to create a routing policy, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have created a network instance connection.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the routing policy. In this case, the routing policy instance may not be created yet, and the system background creation task is still in progress. You can use ListErRouteMaps or GetErRouteMap to query the status of a routing policy.
        If the status of the routing policy is Execute, the system is creating the instance.
        If the status of the routing policy is Available, the creation is successful.
        
        @param request: CreateErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_owner):
            body['ReceptionInstanceOwner'] = request.reception_instance_owner
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.route_map_num):
            body['RouteMapNum'] = request.route_map_num
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_owner):
            body['TransmissionInstanceOwner'] = request.transmission_instance_owner
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_er_route_map(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        """
        @summary Users can use this API to create routing policy by specifying the network instance connection under Lingjun HUB.
        
        @description When you call this operation to create a routing policy, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have created a network instance connection.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the routing policy. In this case, the routing policy instance may not be created yet, and the system background creation task is still in progress. You can use ListErRouteMaps or GetErRouteMap to query the status of a routing policy.
        If the status of the routing policy is Execute, the system is creating the instance.
        If the status of the routing policy is Available, the creation is successful.
        
        @param request: CreateErRouteMapRequest
        @return: CreateErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_er_route_map_with_options(request, runtime)

    async def create_er_route_map_async(
        self,
        request: eflo_20220530_models.CreateErRouteMapRequest,
    ) -> eflo_20220530_models.CreateErRouteMapResponse:
        """
        @summary Users can use this API to create routing policy by specifying the network instance connection under Lingjun HUB.
        
        @description When you call this operation to create a routing policy, note that:
        Make sure that you have created a Lingjun HUB instance.
        Make sure that you have created a network instance connection.
        This operation is an asynchronous operation. After you call this operation, the system returns the ID of the routing policy. In this case, the routing policy instance may not be created yet, and the system background creation task is still in progress. You can use ListErRouteMaps or GetErRouteMap to query the status of a routing policy.
        If the status of the routing policy is Execute, the system is creating the instance.
        If the status of the routing policy is Available, the creation is successful.
        
        @param request: CreateErRouteMapRequest
        @return: CreateErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_er_route_map_with_options_async(request, runtime)

    def create_subnet_with_options(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        """
        @summary Users can use this API to create a Lingjun subnet under the Lingjun network segment.
        
        @description When you call this operation to create a Lingjun subnet, note that:
        You have created a Lingjun CIDR block.
        Only one network segment can be specified for a Lingjun subnet.
        The network segment cannot be modified after the Lingjun subnet is created.
        Make sure that you have sufficient Lingjun subnet quota.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun subnet. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListSubnets or GetSubnet operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun subnet is Executed, it indicates that it is being created.
        If the status of the Lingjun subnet is Available, the creation is successful.
        
        @param request: CreateSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subnet_with_options_async(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        """
        @summary Users can use this API to create a Lingjun subnet under the Lingjun network segment.
        
        @description When you call this operation to create a Lingjun subnet, note that:
        You have created a Lingjun CIDR block.
        Only one network segment can be specified for a Lingjun subnet.
        The network segment cannot be modified after the Lingjun subnet is created.
        Make sure that you have sufficient Lingjun subnet quota.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun subnet. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListSubnets or GetSubnet operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun subnet is Executed, it indicates that it is being created.
        If the status of the Lingjun subnet is Available, the creation is successful.
        
        @param request: CreateSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subnet(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        """
        @summary Users can use this API to create a Lingjun subnet under the Lingjun network segment.
        
        @description When you call this operation to create a Lingjun subnet, note that:
        You have created a Lingjun CIDR block.
        Only one network segment can be specified for a Lingjun subnet.
        The network segment cannot be modified after the Lingjun subnet is created.
        Make sure that you have sufficient Lingjun subnet quota.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun subnet. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListSubnets or GetSubnet operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun subnet is Executed, it indicates that it is being created.
        If the status of the Lingjun subnet is Available, the creation is successful.
        
        @param request: CreateSubnetRequest
        @return: CreateSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_subnet_with_options(request, runtime)

    async def create_subnet_async(
        self,
        request: eflo_20220530_models.CreateSubnetRequest,
    ) -> eflo_20220530_models.CreateSubnetResponse:
        """
        @summary Users can use this API to create a Lingjun subnet under the Lingjun network segment.
        
        @description When you call this operation to create a Lingjun subnet, note that:
        You have created a Lingjun CIDR block.
        Only one network segment can be specified for a Lingjun subnet.
        The network segment cannot be modified after the Lingjun subnet is created.
        Make sure that you have sufficient Lingjun subnet quota.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun subnet. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListSubnets or GetSubnet operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun subnet is Executed, it indicates that it is being created.
        If the status of the Lingjun subnet is Available, the creation is successful.
        
        @param request: CreateSubnetRequest
        @return: CreateSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_subnet_with_options_async(request, runtime)

    def create_vcc_with_options(
        self,
        request: eflo_20220530_models.CreateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccResponse:
        """
        @summary You can create a Lingjun connection to connect Lingjun network environment and Alibaba Cloud network environment.
        
        @description When you call this operation to create a Lingjun connection, note that:
        When you specify the vccId parameter, the system will configure the purchased Lingjun connection for you. When the default vccId parameter is set, the system will automatically place an order and configure the Lingjun connection for you.
        Make sure that you have called the InitializeVcc operation to grant permissions.
        This interface is an asynchronous interface. After this interface is called, the system will return the Lingjun connection ID, but the Lingjun connection instance may not be created yet, and the system background creation task is still in progress. You can call the ListVccs or GetVcc operation to query the status of the Lingjun connection.
        If the status of the Lingjun connection is Executed, the Lingjun connection is being created.
        If the status of the Lingjun connection is Available, the Lingjun connection is created.
        
        @param request: CreateVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_could_service):
            body['AccessCouldService'] = request.access_could_service
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bgp_asn):
            body['BgpAsn'] = request.bgp_asn
        if not UtilClient.is_unset(request.bgp_cidr):
            body['BgpCidr'] = request.bgp_cidr
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            body['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_with_options_async(
        self,
        request: eflo_20220530_models.CreateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccResponse:
        """
        @summary You can create a Lingjun connection to connect Lingjun network environment and Alibaba Cloud network environment.
        
        @description When you call this operation to create a Lingjun connection, note that:
        When you specify the vccId parameter, the system will configure the purchased Lingjun connection for you. When the default vccId parameter is set, the system will automatically place an order and configure the Lingjun connection for you.
        Make sure that you have called the InitializeVcc operation to grant permissions.
        This interface is an asynchronous interface. After this interface is called, the system will return the Lingjun connection ID, but the Lingjun connection instance may not be created yet, and the system background creation task is still in progress. You can call the ListVccs or GetVcc operation to query the status of the Lingjun connection.
        If the status of the Lingjun connection is Executed, the Lingjun connection is being created.
        If the status of the Lingjun connection is Available, the Lingjun connection is created.
        
        @param request: CreateVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_could_service):
            body['AccessCouldService'] = request.access_could_service
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.bgp_asn):
            body['BgpAsn'] = request.bgp_asn
        if not UtilClient.is_unset(request.bgp_cidr):
            body['BgpCidr'] = request.bgp_cidr
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            body['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.connection_type):
            body['ConnectionType'] = request.connection_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc(
        self,
        request: eflo_20220530_models.CreateVccRequest,
    ) -> eflo_20220530_models.CreateVccResponse:
        """
        @summary You can create a Lingjun connection to connect Lingjun network environment and Alibaba Cloud network environment.
        
        @description When you call this operation to create a Lingjun connection, note that:
        When you specify the vccId parameter, the system will configure the purchased Lingjun connection for you. When the default vccId parameter is set, the system will automatically place an order and configure the Lingjun connection for you.
        Make sure that you have called the InitializeVcc operation to grant permissions.
        This interface is an asynchronous interface. After this interface is called, the system will return the Lingjun connection ID, but the Lingjun connection instance may not be created yet, and the system background creation task is still in progress. You can call the ListVccs or GetVcc operation to query the status of the Lingjun connection.
        If the status of the Lingjun connection is Executed, the Lingjun connection is being created.
        If the status of the Lingjun connection is Available, the Lingjun connection is created.
        
        @param request: CreateVccRequest
        @return: CreateVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_with_options(request, runtime)

    async def create_vcc_async(
        self,
        request: eflo_20220530_models.CreateVccRequest,
    ) -> eflo_20220530_models.CreateVccResponse:
        """
        @summary You can create a Lingjun connection to connect Lingjun network environment and Alibaba Cloud network environment.
        
        @description When you call this operation to create a Lingjun connection, note that:
        When you specify the vccId parameter, the system will configure the purchased Lingjun connection for you. When the default vccId parameter is set, the system will automatically place an order and configure the Lingjun connection for you.
        Make sure that you have called the InitializeVcc operation to grant permissions.
        This interface is an asynchronous interface. After this interface is called, the system will return the Lingjun connection ID, but the Lingjun connection instance may not be created yet, and the system background creation task is still in progress. You can call the ListVccs or GetVcc operation to query the status of the Lingjun connection.
        If the status of the Lingjun connection is Executed, the Lingjun connection is being created.
        If the status of the Lingjun connection is Available, the Lingjun connection is created.
        
        @param request: CreateVccRequest
        @return: CreateVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vcc_with_options_async(request, runtime)

    def create_vcc_grant_rule_with_options(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        """
        @summary Users can use this API to connect Lingjun instance to the Lingjun HUB instance of the target account. After authorization, the target account can be associated with your Lingjun connection by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVccGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVccGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        """
        @summary Users can use this API to connect Lingjun instance to the Lingjun HUB instance of the target account. After authorization, the target account can be associated with your Lingjun connection by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVccGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVccGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc_grant_rule(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        """
        @summary Users can use this API to connect Lingjun instance to the Lingjun HUB instance of the target account. After authorization, the target account can be associated with your Lingjun connection by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVccGrantRuleRequest
        @return: CreateVccGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_grant_rule_with_options(request, runtime)

    async def create_vcc_grant_rule_async(
        self,
        request: eflo_20220530_models.CreateVccGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVccGrantRuleResponse:
        """
        @summary Users can use this API to connect Lingjun instance to the Lingjun HUB instance of the target account. After authorization, the target account can be associated with your Lingjun connection by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVccGrantRuleRequest
        @return: CreateVccGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vcc_grant_rule_with_options_async(request, runtime)

    def create_vcc_route_entry_with_options(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        """
        @summary Create a Lingjun connection route entry.
        
        @description When you call this operation to create a VBR route entry, take note of the following items:
        After you call this operation, static route entries and BGP network announcements are created on the VBR to which the Lingjun connection belongs.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entry may not be created yet, and the system still creates the static route entry in the background. You can query the status of VBR static route entries by ListVccRouteEntries or GetVccRouteEntry:
        If the VBR static route entry is in the Executing state, it indicates that it is being created.
        If the status of the VBR static route entry is Available, the VBR is created.
        
        @param request: CreateVccRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVccRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vcc_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        """
        @summary Create a Lingjun connection route entry.
        
        @description When you call this operation to create a VBR route entry, take note of the following items:
        After you call this operation, static route entries and BGP network announcements are created on the VBR to which the Lingjun connection belongs.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entry may not be created yet, and the system still creates the static route entry in the background. You can query the status of VBR static route entries by ListVccRouteEntries or GetVccRouteEntry:
        If the VBR static route entry is in the Executing state, it indicates that it is being created.
        If the status of the VBR static route entry is Available, the VBR is created.
        
        @param request: CreateVccRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVccRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vcc_route_entry(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        """
        @summary Create a Lingjun connection route entry.
        
        @description When you call this operation to create a VBR route entry, take note of the following items:
        After you call this operation, static route entries and BGP network announcements are created on the VBR to which the Lingjun connection belongs.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entry may not be created yet, and the system still creates the static route entry in the background. You can query the status of VBR static route entries by ListVccRouteEntries or GetVccRouteEntry:
        If the VBR static route entry is in the Executing state, it indicates that it is being created.
        If the status of the VBR static route entry is Available, the VBR is created.
        
        @param request: CreateVccRouteEntryRequest
        @return: CreateVccRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vcc_route_entry_with_options(request, runtime)

    async def create_vcc_route_entry_async(
        self,
        request: eflo_20220530_models.CreateVccRouteEntryRequest,
    ) -> eflo_20220530_models.CreateVccRouteEntryResponse:
        """
        @summary Create a Lingjun connection route entry.
        
        @description When you call this operation to create a VBR route entry, take note of the following items:
        After you call this operation, static route entries and BGP network announcements are created on the VBR to which the Lingjun connection belongs.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entry may not be created yet, and the system still creates the static route entry in the background. You can query the status of VBR static route entries by ListVccRouteEntries or GetVccRouteEntry:
        If the VBR static route entry is in the Executing state, it indicates that it is being created.
        If the status of the VBR static route entry is Available, the VBR is created.
        
        @param request: CreateVccRouteEntryRequest
        @return: CreateVccRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vcc_route_entry_with_options_async(request, runtime)

    def create_vpd_with_options(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdResponse:
        """
        @summary Create a private Lingjun CIDR block. This CIDR block has an independent network environment.
        
        @description When you call this operation to create a CIDR block for Lingjun, take note of the following:
        A Lingjun network segment can specify an additional network segment in addition to a main network segment.
        After the Lingjun network segment is created, the network segment cannot be modified.
        Make sure that you have a sufficient quota of Lingjun CIDR blocks.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun network segment. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListVpds or GetVpd operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun CIDR block is Executed, the CIDR block is being created.
        If the status of the Lingjun CIDR block is Available, the creation is successful.
        
        @param request: CreateVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subnets):
            body['Subnets'] = request.subnets
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpd_with_options_async(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdResponse:
        """
        @summary Create a private Lingjun CIDR block. This CIDR block has an independent network environment.
        
        @description When you call this operation to create a CIDR block for Lingjun, take note of the following:
        A Lingjun network segment can specify an additional network segment in addition to a main network segment.
        After the Lingjun network segment is created, the network segment cannot be modified.
        Make sure that you have a sufficient quota of Lingjun CIDR blocks.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun network segment. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListVpds or GetVpd operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun CIDR block is Executed, the CIDR block is being created.
        If the status of the Lingjun CIDR block is Available, the creation is successful.
        
        @param request: CreateVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cidr):
            body['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subnets):
            body['Subnets'] = request.subnets
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpd(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
    ) -> eflo_20220530_models.CreateVpdResponse:
        """
        @summary Create a private Lingjun CIDR block. This CIDR block has an independent network environment.
        
        @description When you call this operation to create a CIDR block for Lingjun, take note of the following:
        A Lingjun network segment can specify an additional network segment in addition to a main network segment.
        After the Lingjun network segment is created, the network segment cannot be modified.
        Make sure that you have a sufficient quota of Lingjun CIDR blocks.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun network segment. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListVpds or GetVpd operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun CIDR block is Executed, the CIDR block is being created.
        If the status of the Lingjun CIDR block is Available, the creation is successful.
        
        @param request: CreateVpdRequest
        @return: CreateVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vpd_with_options(request, runtime)

    async def create_vpd_async(
        self,
        request: eflo_20220530_models.CreateVpdRequest,
    ) -> eflo_20220530_models.CreateVpdResponse:
        """
        @summary Create a private Lingjun CIDR block. This CIDR block has an independent network environment.
        
        @description When you call this operation to create a CIDR block for Lingjun, take note of the following:
        A Lingjun network segment can specify an additional network segment in addition to a main network segment.
        After the Lingjun network segment is created, the network segment cannot be modified.
        Make sure that you have a sufficient quota of Lingjun CIDR blocks.
        This interface is an asynchronous interface. After calling this interface, the system will return the ID of a Lingjun network segment. At this time, the Lingjun network segment may not be created yet, and the system background creation task is still in progress. You can call the ListVpds or GetVpd operation to query the status of the CIDR block of Lingjun.
        If the status of the Lingjun CIDR block is Executed, the CIDR block is being created.
        If the status of the Lingjun CIDR block is Available, the creation is successful.
        
        @param request: CreateVpdRequest
        @return: CreateVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vpd_with_options_async(request, runtime)

    def create_vpd_grant_rule_with_options(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        """
        @summary Users can use this API to authorize Lingjun HUB instances of the target account. After authorization, the target account can be associated with your Lingjun CIDR block by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVpdGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpdGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vpd_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        """
        @summary Users can use this API to authorize Lingjun HUB instances of the target account. After authorization, the target account can be associated with your Lingjun CIDR block by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVpdGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVpdGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.CreateVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vpd_grant_rule(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        """
        @summary Users can use this API to authorize Lingjun HUB instances of the target account. After authorization, the target account can be associated with your Lingjun CIDR block by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVpdGrantRuleRequest
        @return: CreateVpdGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vpd_grant_rule_with_options(request, runtime)

    async def create_vpd_grant_rule_async(
        self,
        request: eflo_20220530_models.CreateVpdGrantRuleRequest,
    ) -> eflo_20220530_models.CreateVpdGrantRuleResponse:
        """
        @summary Users can use this API to authorize Lingjun HUB instances of the target account. After authorization, the target account can be associated with your Lingjun CIDR block by using the authorized Lingjun HUB instance.
        
        @description When you call this operation to create cross-account authorization for Lingjun HUB, note that:
        Make sure that the Alibaba Cloud ID and Lingjun HUB instance that you want to authorize are correct.
        If you authorize the account of the other party, the account of the other party can load your local network instance to its Lingjun HUB, and the other party\\"s network will be connected to your network. Please proceed with caution.
        
        @param request: CreateVpdGrantRuleRequest
        @return: CreateVpdGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vpd_grant_rule_with_options_async(request, runtime)

    def delete_elastic_network_interface_with_options(
        self,
        request: eflo_20220530_models.DeleteElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteElasticNetworkInterfaceResponse:
        """
        @summary Delete Lingjun Elastic Network Interface. After deletion, all relevant data will be lost and cannot be recovered. Please operate with caution.
        
        @param request: DeleteElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.DeleteElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteElasticNetworkInterfaceResponse:
        """
        @summary Delete Lingjun Elastic Network Interface. After deletion, all relevant data will be lost and cannot be recovered. Please operate with caution.
        
        @param request: DeleteElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_network_interface(
        self,
        request: eflo_20220530_models.DeleteElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.DeleteElasticNetworkInterfaceResponse:
        """
        @summary Delete Lingjun Elastic Network Interface. After deletion, all relevant data will be lost and cannot be recovered. Please operate with caution.
        
        @param request: DeleteElasticNetworkInterfaceRequest
        @return: DeleteElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_elastic_network_interface_with_options(request, runtime)

    async def delete_elastic_network_interface_async(
        self,
        request: eflo_20220530_models.DeleteElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.DeleteElasticNetworkInterfaceResponse:
        """
        @summary Delete Lingjun Elastic Network Interface. After deletion, all relevant data will be lost and cannot be recovered. Please operate with caution.
        
        @param request: DeleteElasticNetworkInterfaceRequest
        @return: DeleteElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_elastic_network_interface_with_options_async(request, runtime)

    def delete_er_with_options(
        self,
        request: eflo_20220530_models.DeleteErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErResponse:
        """
        @summary After you delete a Lingjun HUB instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete the Lingjun HUB, note that:
        Before you delete the instance, make sure that no network instance is connected to the Lingjun HUB instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun HUB instance may not be deleted, and the system background deletion task is still in progress. You can call the ListErs or GetEr operation to query the deletion status of the Lingjun HUB.
        If the status of the Lingjun HUB is Deleting, the Lingjun HUB instance is being deleted.
        If no Lingjun HUB instance is recorded, the Lingjun HUB instance has been deleted.
        
        @param request: DeleteErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_with_options_async(
        self,
        request: eflo_20220530_models.DeleteErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErResponse:
        """
        @summary After you delete a Lingjun HUB instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete the Lingjun HUB, note that:
        Before you delete the instance, make sure that no network instance is connected to the Lingjun HUB instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun HUB instance may not be deleted, and the system background deletion task is still in progress. You can call the ListErs or GetEr operation to query the deletion status of the Lingjun HUB.
        If the status of the Lingjun HUB is Deleting, the Lingjun HUB instance is being deleted.
        If no Lingjun HUB instance is recorded, the Lingjun HUB instance has been deleted.
        
        @param request: DeleteErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er(
        self,
        request: eflo_20220530_models.DeleteErRequest,
    ) -> eflo_20220530_models.DeleteErResponse:
        """
        @summary After you delete a Lingjun HUB instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete the Lingjun HUB, note that:
        Before you delete the instance, make sure that no network instance is connected to the Lingjun HUB instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun HUB instance may not be deleted, and the system background deletion task is still in progress. You can call the ListErs or GetEr operation to query the deletion status of the Lingjun HUB.
        If the status of the Lingjun HUB is Deleting, the Lingjun HUB instance is being deleted.
        If no Lingjun HUB instance is recorded, the Lingjun HUB instance has been deleted.
        
        @param request: DeleteErRequest
        @return: DeleteErResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_er_with_options(request, runtime)

    async def delete_er_async(
        self,
        request: eflo_20220530_models.DeleteErRequest,
    ) -> eflo_20220530_models.DeleteErResponse:
        """
        @summary After you delete a Lingjun HUB instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete the Lingjun HUB, note that:
        Before you delete the instance, make sure that no network instance is connected to the Lingjun HUB instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun HUB instance may not be deleted, and the system background deletion task is still in progress. You can call the ListErs or GetEr operation to query the deletion status of the Lingjun HUB.
        If the status of the Lingjun HUB is Deleting, the Lingjun HUB instance is being deleted.
        If no Lingjun HUB instance is recorded, the Lingjun HUB instance has been deleted.
        
        @param request: DeleteErRequest
        @return: DeleteErResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_er_with_options_async(request, runtime)

    def delete_er_attachment_with_options(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        """
        @summary If you delete a network instance that is connected to an instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a network instance connection, take note of the following:
        Before you delete the instance, make sure that no routing policy exists under the network instance connection instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the network instance that is connected to the instance may not be deleted. The system still deletes the instance in the background. You can call the ListErAttachments or GetErAttachment to query the deletion status of network instance connections:
        If the status of the network instance connection is Deleting, the network instance connection is being deleted.
        If there is no connection record for the network instance, the connection to the network instance has been deleted.
        
        @param request: DeleteErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        """
        @summary If you delete a network instance that is connected to an instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a network instance connection, take note of the following:
        Before you delete the instance, make sure that no routing policy exists under the network instance connection instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the network instance that is connected to the instance may not be deleted. The system still deletes the instance in the background. You can call the ListErAttachments or GetErAttachment to query the deletion status of network instance connections:
        If the status of the network instance connection is Deleting, the network instance connection is being deleted.
        If there is no connection record for the network instance, the connection to the network instance has been deleted.
        
        @param request: DeleteErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er_attachment(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        """
        @summary If you delete a network instance that is connected to an instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a network instance connection, take note of the following:
        Before you delete the instance, make sure that no routing policy exists under the network instance connection instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the network instance that is connected to the instance may not be deleted. The system still deletes the instance in the background. You can call the ListErAttachments or GetErAttachment to query the deletion status of network instance connections:
        If the status of the network instance connection is Deleting, the network instance connection is being deleted.
        If there is no connection record for the network instance, the connection to the network instance has been deleted.
        
        @param request: DeleteErAttachmentRequest
        @return: DeleteErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_er_attachment_with_options(request, runtime)

    async def delete_er_attachment_async(
        self,
        request: eflo_20220530_models.DeleteErAttachmentRequest,
    ) -> eflo_20220530_models.DeleteErAttachmentResponse:
        """
        @summary If you delete a network instance that is connected to an instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a network instance connection, take note of the following:
        Before you delete the instance, make sure that no routing policy exists under the network instance connection instance.
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the network instance that is connected to the instance may not be deleted. The system still deletes the instance in the background. You can call the ListErAttachments or GetErAttachment to query the deletion status of network instance connections:
        If the status of the network instance connection is Deleting, the network instance connection is being deleted.
        If there is no connection record for the network instance, the connection to the network instance has been deleted.
        
        @param request: DeleteErAttachmentRequest
        @return: DeleteErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_er_attachment_with_options_async(request, runtime)

    def delete_er_route_map_with_options(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        """
        @summary If you delete a routing policy instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a routing policy, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the routing policy instance may not be deleted yet, and the system background deletion task is still in progress. You can call the ListErRouteMaps or GetErRouteMap operation to query the deletion status of a routing policy.
        If the routing policy is in the Deleting state, the routing policy instance is being deleted.
        If no routing policy instance is recorded, the routing policy instance has been deleted.
        
        @param request: DeleteErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_ids):
            body['ErRouteMapIds'] = request.er_route_map_ids
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        """
        @summary If you delete a routing policy instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a routing policy, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the routing policy instance may not be deleted yet, and the system background deletion task is still in progress. You can call the ListErRouteMaps or GetErRouteMap operation to query the deletion status of a routing policy.
        If the routing policy is in the Deleting state, the routing policy instance is being deleted.
        If no routing policy instance is recorded, the routing policy instance has been deleted.
        
        @param request: DeleteErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_ids):
            body['ErRouteMapIds'] = request.er_route_map_ids
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_er_route_map(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        """
        @summary If you delete a routing policy instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a routing policy, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the routing policy instance may not be deleted yet, and the system background deletion task is still in progress. You can call the ListErRouteMaps or GetErRouteMap operation to query the deletion status of a routing policy.
        If the routing policy is in the Deleting state, the routing policy instance is being deleted.
        If no routing policy instance is recorded, the routing policy instance has been deleted.
        
        @param request: DeleteErRouteMapRequest
        @return: DeleteErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_er_route_map_with_options(request, runtime)

    async def delete_er_route_map_async(
        self,
        request: eflo_20220530_models.DeleteErRouteMapRequest,
    ) -> eflo_20220530_models.DeleteErRouteMapResponse:
        """
        @summary If you delete a routing policy instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a routing policy, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the routing policy instance may not be deleted yet, and the system background deletion task is still in progress. You can call the ListErRouteMaps or GetErRouteMap operation to query the deletion status of a routing policy.
        If the routing policy is in the Deleting state, the routing policy instance is being deleted.
        If no routing policy instance is recorded, the routing policy instance has been deleted.
        
        @param request: DeleteErRouteMapRequest
        @return: DeleteErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_er_route_map_with_options_async(request, runtime)

    def delete_subnet_with_options(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        """
        @summary If you delete a Lingjun subnet instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun subnet, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun subnet instance may not be deleted, and the system background deletion task is still in progress. You can call the ListSubnets or GetSubnet operation to query the deletion status of the subnet.
        If the status of the Lingjun subnet is Deleting, the Lingjun subnet instance is being deleted.
        If there is no record of the Lingjun subnet instance, the Lingjun subnet instance has been deleted.
        
        @param request: DeleteSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_subnet_with_options_async(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        """
        @summary If you delete a Lingjun subnet instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun subnet, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun subnet instance may not be deleted, and the system background deletion task is still in progress. You can call the ListSubnets or GetSubnet operation to query the deletion status of the subnet.
        If the status of the Lingjun subnet is Deleting, the Lingjun subnet instance is being deleted.
        If there is no record of the Lingjun subnet instance, the Lingjun subnet instance has been deleted.
        
        @param request: DeleteSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_subnet(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        """
        @summary If you delete a Lingjun subnet instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun subnet, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun subnet instance may not be deleted, and the system background deletion task is still in progress. You can call the ListSubnets or GetSubnet operation to query the deletion status of the subnet.
        If the status of the Lingjun subnet is Deleting, the Lingjun subnet instance is being deleted.
        If there is no record of the Lingjun subnet instance, the Lingjun subnet instance has been deleted.
        
        @param request: DeleteSubnetRequest
        @return: DeleteSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_subnet_with_options(request, runtime)

    async def delete_subnet_async(
        self,
        request: eflo_20220530_models.DeleteSubnetRequest,
    ) -> eflo_20220530_models.DeleteSubnetResponse:
        """
        @summary If you delete a Lingjun subnet instance, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun subnet, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This interface is an asynchronous interface. After this interface is called, the Lingjun subnet instance may not be deleted, and the system background deletion task is still in progress. You can call the ListSubnets or GetSubnet operation to query the deletion status of the subnet.
        If the status of the Lingjun subnet is Deleting, the Lingjun subnet instance is being deleted.
        If there is no record of the Lingjun subnet instance, the Lingjun subnet instance has been deleted.
        
        @param request: DeleteSubnetRequest
        @return: DeleteSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_subnet_with_options_async(request, runtime)

    def delete_vcc_grant_rule_with_options(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        """
        @summary If you delete a Lingjun HUB cross-account authorization that is connected to Lingjun, the related data is lost and cannot be recovered.
        
        @param request: DeleteVccGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVccGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vcc_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        """
        @summary If you delete a Lingjun HUB cross-account authorization that is connected to Lingjun, the related data is lost and cannot be recovered.
        
        @param request: DeleteVccGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVccGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vcc_grant_rule(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        """
        @summary If you delete a Lingjun HUB cross-account authorization that is connected to Lingjun, the related data is lost and cannot be recovered.
        
        @param request: DeleteVccGrantRuleRequest
        @return: DeleteVccGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vcc_grant_rule_with_options(request, runtime)

    async def delete_vcc_grant_rule_async(
        self,
        request: eflo_20220530_models.DeleteVccGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVccGrantRuleResponse:
        """
        @summary If you delete a Lingjun HUB cross-account authorization that is connected to Lingjun, the related data is lost and cannot be recovered.
        
        @param request: DeleteVccGrantRuleRequest
        @return: DeleteVccGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vcc_grant_rule_with_options_async(request, runtime)

    def delete_vcc_route_entry_with_options(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        """
        @summary Delete a Lingjun connection route entry.
        
        @description When you call this operation to delete a VBR static route entry, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entries may not be deleted. The system still deletes the VBR static route entries in the background. You can call the ListVccRouteEntries or GetVccRouteEntry to query the deletion status of VBR static route entries:
        If the VBR static route entry is in the Deleting state, the VBR static route entry is being deleted.
        If no VBR static route entry instance is recorded, the VBR static route entry instance has been deleted.
        
        @param request: DeleteVccRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVccRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vcc_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        """
        @summary Delete a Lingjun connection route entry.
        
        @description When you call this operation to delete a VBR static route entry, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entries may not be deleted. The system still deletes the VBR static route entries in the background. You can call the ListVccRouteEntries or GetVccRouteEntry to query the deletion status of VBR static route entries:
        If the VBR static route entry is in the Deleting state, the VBR static route entry is being deleted.
        If no VBR static route entry instance is recorded, the VBR static route entry instance has been deleted.
        
        @param request: DeleteVccRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVccRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vcc_route_entry(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        """
        @summary Delete a Lingjun connection route entry.
        
        @description When you call this operation to delete a VBR static route entry, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entries may not be deleted. The system still deletes the VBR static route entries in the background. You can call the ListVccRouteEntries or GetVccRouteEntry to query the deletion status of VBR static route entries:
        If the VBR static route entry is in the Deleting state, the VBR static route entry is being deleted.
        If no VBR static route entry instance is recorded, the VBR static route entry instance has been deleted.
        
        @param request: DeleteVccRouteEntryRequest
        @return: DeleteVccRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vcc_route_entry_with_options(request, runtime)

    async def delete_vcc_route_entry_async(
        self,
        request: eflo_20220530_models.DeleteVccRouteEntryRequest,
    ) -> eflo_20220530_models.DeleteVccRouteEntryResponse:
        """
        @summary Delete a Lingjun connection route entry.
        
        @description When you call this operation to delete a VBR static route entry, note that:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        This operation is an asynchronous operation. After you call this operation, the VBR static route entries may not be deleted. The system still deletes the VBR static route entries in the background. You can call the ListVccRouteEntries or GetVccRouteEntry to query the deletion status of VBR static route entries:
        If the VBR static route entry is in the Deleting state, the VBR static route entry is being deleted.
        If no VBR static route entry instance is recorded, the VBR static route entry instance has been deleted.
        
        @param request: DeleteVccRouteEntryRequest
        @return: DeleteVccRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vcc_route_entry_with_options_async(request, runtime)

    def delete_vpd_with_options(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        """
        @summary After you delete a Lingjun CIDR block, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun CIDR block, take note of the following items:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        Before deleting, make sure that all Lingjun subnet instances under the Lingjun CIDR block have been deleted.
        This interface is an asynchronous interface. After this interface is called, the Lingjun network segment instance may not be deleted, and the system background deletion task is still in progress. You can call the ListVpds or GetVpd operation to query the deletion status of the CIDR block.
        If the status of the Lingjun CIDR block is Deleting, the Lingjun CIDR block is being deleted.
        If there is no record of the Lingjun CIDR block instance, the Lingjun CIDR block instance has been deleted.
        
        @param request: DeleteVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpd_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        """
        @summary After you delete a Lingjun CIDR block, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun CIDR block, take note of the following items:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        Before deleting, make sure that all Lingjun subnet instances under the Lingjun CIDR block have been deleted.
        This interface is an asynchronous interface. After this interface is called, the Lingjun network segment instance may not be deleted, and the system background deletion task is still in progress. You can call the ListVpds or GetVpd operation to query the deletion status of the CIDR block.
        If the status of the Lingjun CIDR block is Deleting, the Lingjun CIDR block is being deleted.
        If there is no record of the Lingjun CIDR block instance, the Lingjun CIDR block instance has been deleted.
        
        @param request: DeleteVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpd(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        """
        @summary After you delete a Lingjun CIDR block, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun CIDR block, take note of the following items:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        Before deleting, make sure that all Lingjun subnet instances under the Lingjun CIDR block have been deleted.
        This interface is an asynchronous interface. After this interface is called, the Lingjun network segment instance may not be deleted, and the system background deletion task is still in progress. You can call the ListVpds or GetVpd operation to query the deletion status of the CIDR block.
        If the status of the Lingjun CIDR block is Deleting, the Lingjun CIDR block is being deleted.
        If there is no record of the Lingjun CIDR block instance, the Lingjun CIDR block instance has been deleted.
        
        @param request: DeleteVpdRequest
        @return: DeleteVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vpd_with_options(request, runtime)

    async def delete_vpd_async(
        self,
        request: eflo_20220530_models.DeleteVpdRequest,
    ) -> eflo_20220530_models.DeleteVpdResponse:
        """
        @summary After you delete a Lingjun CIDR block, the related data is lost and cannot be recovered.
        
        @description When you call this operation to delete a Lingjun CIDR block, take note of the following items:
        After deletion, all related data is lost and cannot be recovered. Exercise caution when performing this operation.
        Before deleting, make sure that all Lingjun subnet instances under the Lingjun CIDR block have been deleted.
        This interface is an asynchronous interface. After this interface is called, the Lingjun network segment instance may not be deleted, and the system background deletion task is still in progress. You can call the ListVpds or GetVpd operation to query the deletion status of the CIDR block.
        If the status of the Lingjun CIDR block is Deleting, the Lingjun CIDR block is being deleted.
        If there is no record of the Lingjun CIDR block instance, the Lingjun CIDR block instance has been deleted.
        
        @param request: DeleteVpdRequest
        @return: DeleteVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpd_with_options_async(request, runtime)

    def delete_vpd_grant_rule_with_options(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        """
        @summary Delete the Lingjun HUB cross-account authorization for a Lingjun CIDR block. After the deletion, the related data is lost and cannot be recovered.
        
        @param request: DeleteVpdGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpdGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vpd_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        """
        @summary Delete the Lingjun HUB cross-account authorization for a Lingjun CIDR block. After the deletion, the related data is lost and cannot be recovered.
        
        @param request: DeleteVpdGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVpdGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DeleteVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vpd_grant_rule(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        """
        @summary Delete the Lingjun HUB cross-account authorization for a Lingjun CIDR block. After the deletion, the related data is lost and cannot be recovered.
        
        @param request: DeleteVpdGrantRuleRequest
        @return: DeleteVpdGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vpd_grant_rule_with_options(request, runtime)

    async def delete_vpd_grant_rule_async(
        self,
        request: eflo_20220530_models.DeleteVpdGrantRuleRequest,
    ) -> eflo_20220530_models.DeleteVpdGrantRuleResponse:
        """
        @summary Delete the Lingjun HUB cross-account authorization for a Lingjun CIDR block. After the deletion, the related data is lost and cannot be recovered.
        
        @param request: DeleteVpdGrantRuleRequest
        @return: DeleteVpdGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpd_grant_rule_with_options_async(request, runtime)

    def describe_slr_with_options(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        """
        @summary Query whether the user has the SLR role-AliyunServiceRoleForEfloVcc required for Lingjun connection.
        
        @description You can call this operation to query whether a user account has a *AliyunServiceRoleForEfloVcc** role.
        >  If you do not have a *AliyunServiceRoleForEfloVcc** role, you need to use the initializeVcc interface to complete authorization, otherwise users will not be able to use Lingjun to connect to the product.
        
        @param request: DescribeSlrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlrResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DescribeSlrResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slr_with_options_async(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        """
        @summary Query whether the user has the SLR role-AliyunServiceRoleForEfloVcc required for Lingjun connection.
        
        @description You can call this operation to query whether a user account has a *AliyunServiceRoleForEfloVcc** role.
        >  If you do not have a *AliyunServiceRoleForEfloVcc** role, you need to use the initializeVcc interface to complete authorization, otherwise users will not be able to use Lingjun to connect to the product.
        
        @param request: DescribeSlrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlrResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSlr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DescribeSlrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slr(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        """
        @summary Query whether the user has the SLR role-AliyunServiceRoleForEfloVcc required for Lingjun connection.
        
        @description You can call this operation to query whether a user account has a *AliyunServiceRoleForEfloVcc** role.
        >  If you do not have a *AliyunServiceRoleForEfloVcc** role, you need to use the initializeVcc interface to complete authorization, otherwise users will not be able to use Lingjun to connect to the product.
        
        @param request: DescribeSlrRequest
        @return: DescribeSlrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slr_with_options(request, runtime)

    async def describe_slr_async(
        self,
        request: eflo_20220530_models.DescribeSlrRequest,
    ) -> eflo_20220530_models.DescribeSlrResponse:
        """
        @summary Query whether the user has the SLR role-AliyunServiceRoleForEfloVcc required for Lingjun connection.
        
        @description You can call this operation to query whether a user account has a *AliyunServiceRoleForEfloVcc** role.
        >  If you do not have a *AliyunServiceRoleForEfloVcc** role, you need to use the initializeVcc interface to complete authorization, otherwise users will not be able to use Lingjun to connect to the product.
        
        @param request: DescribeSlrRequest
        @return: DescribeSlrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slr_with_options_async(request, runtime)

    def detach_elastic_network_interface_with_options(
        self,
        request: eflo_20220530_models.DetachElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DetachElasticNetworkInterfaceResponse:
        """
        @summary Unbind Lingjun ENI from NC.
        
        @description This interface is an asynchronous interface, and you need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the unbound state.
        
        @param request: DetachElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DetachElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_elastic_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.DetachElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.DetachElasticNetworkInterfaceResponse:
        """
        @summary Unbind Lingjun ENI from NC.
        
        @description This interface is an asynchronous interface, and you need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the unbound state.
        
        @param request: DetachElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.DetachElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_elastic_network_interface(
        self,
        request: eflo_20220530_models.DetachElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.DetachElasticNetworkInterfaceResponse:
        """
        @summary Unbind Lingjun ENI from NC.
        
        @description This interface is an asynchronous interface, and you need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the unbound state.
        
        @param request: DetachElasticNetworkInterfaceRequest
        @return: DetachElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_elastic_network_interface_with_options(request, runtime)

    async def detach_elastic_network_interface_async(
        self,
        request: eflo_20220530_models.DetachElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.DetachElasticNetworkInterfaceResponse:
        """
        @summary Unbind Lingjun ENI from NC.
        
        @description This interface is an asynchronous interface, and you need to use the query interface to wait for the Lingjun Elastic Network Interface to reach the unbound state.
        
        @param request: DetachElasticNetworkInterfaceRequest
        @return: DetachElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_elastic_network_interface_with_options_async(request, runtime)

    def get_destination_cidr_block_with_options(
        self,
        request: eflo_20220530_models.GetDestinationCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetDestinationCidrBlockResponse:
        """
        @summary Users can use this API to query the destination CIDR block of the source policy instance when creating a routing strategy.
        
        @param request: GetDestinationCidrBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDestinationCidrBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDestinationCidrBlock',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetDestinationCidrBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_destination_cidr_block_with_options_async(
        self,
        request: eflo_20220530_models.GetDestinationCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetDestinationCidrBlockResponse:
        """
        @summary Users can use this API to query the destination CIDR block of the source policy instance when creating a routing strategy.
        
        @param request: GetDestinationCidrBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDestinationCidrBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDestinationCidrBlock',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetDestinationCidrBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_destination_cidr_block(
        self,
        request: eflo_20220530_models.GetDestinationCidrBlockRequest,
    ) -> eflo_20220530_models.GetDestinationCidrBlockResponse:
        """
        @summary Users can use this API to query the destination CIDR block of the source policy instance when creating a routing strategy.
        
        @param request: GetDestinationCidrBlockRequest
        @return: GetDestinationCidrBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_destination_cidr_block_with_options(request, runtime)

    async def get_destination_cidr_block_async(
        self,
        request: eflo_20220530_models.GetDestinationCidrBlockRequest,
    ) -> eflo_20220530_models.GetDestinationCidrBlockResponse:
        """
        @summary Users can use this API to query the destination CIDR block of the source policy instance when creating a routing strategy.
        
        @param request: GetDestinationCidrBlockRequest
        @return: GetDestinationCidrBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_destination_cidr_block_with_options_async(request, runtime)

    def get_elastic_network_interface_with_options(
        self,
        request: eflo_20220530_models.GetElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetElasticNetworkInterfaceResponse:
        """
        @summary Queries the details of an LENI.
        
        @param request: GetElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_elastic_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.GetElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetElasticNetworkInterfaceResponse:
        """
        @summary Queries the details of an LENI.
        
        @param request: GetElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_elastic_network_interface(
        self,
        request: eflo_20220530_models.GetElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.GetElasticNetworkInterfaceResponse:
        """
        @summary Queries the details of an LENI.
        
        @param request: GetElasticNetworkInterfaceRequest
        @return: GetElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_elastic_network_interface_with_options(request, runtime)

    async def get_elastic_network_interface_async(
        self,
        request: eflo_20220530_models.GetElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.GetElasticNetworkInterfaceResponse:
        """
        @summary Queries the details of an LENI.
        
        @param request: GetElasticNetworkInterfaceRequest
        @return: GetElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_elastic_network_interface_with_options_async(request, runtime)

    def get_er_with_options(
        self,
        request: eflo_20220530_models.GetErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: GetErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_with_options_async(
        self,
        request: eflo_20220530_models.GetErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: GetErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er(
        self,
        request: eflo_20220530_models.GetErRequest,
    ) -> eflo_20220530_models.GetErResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: GetErRequest
        @return: GetErResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_er_with_options(request, runtime)

    async def get_er_async(
        self,
        request: eflo_20220530_models.GetErRequest,
    ) -> eflo_20220530_models.GetErResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: GetErRequest
        @return: GetErResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_er_with_options_async(request, runtime)

    def get_er_attachment_with_options(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        """
        @summary Queries network instance connections.
        
        @param request: GetErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        """
        @summary Queries network instance connections.
        
        @param request: GetErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_attachment(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        """
        @summary Queries network instance connections.
        
        @param request: GetErAttachmentRequest
        @return: GetErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_er_attachment_with_options(request, runtime)

    async def get_er_attachment_async(
        self,
        request: eflo_20220530_models.GetErAttachmentRequest,
    ) -> eflo_20220530_models.GetErAttachmentResponse:
        """
        @summary Queries network instance connections.
        
        @param request: GetErAttachmentRequest
        @return: GetErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_er_attachment_with_options_async(request, runtime)

    def get_er_route_entry_with_options(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        """
        @summary Queries the details of Lingjun HUB route entries.
        
        @param request: GetErRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_entry_id):
            body['ErRouteEntryId'] = request.er_route_entry_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        """
        @summary Queries the details of Lingjun HUB route entries.
        
        @param request: GetErRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_entry_id):
            body['ErRouteEntryId'] = request.er_route_entry_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_route_entry(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        """
        @summary Queries the details of Lingjun HUB route entries.
        
        @param request: GetErRouteEntryRequest
        @return: GetErRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_er_route_entry_with_options(request, runtime)

    async def get_er_route_entry_async(
        self,
        request: eflo_20220530_models.GetErRouteEntryRequest,
    ) -> eflo_20220530_models.GetErRouteEntryResponse:
        """
        @summary Queries the details of Lingjun HUB route entries.
        
        @param request: GetErRouteEntryRequest
        @return: GetErRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_er_route_entry_with_options_async(request, runtime)

    def get_er_route_map_with_options(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        """
        @summary query lingjun hub routing policy details.
        
        @param request: GetErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        """
        @summary query lingjun hub routing policy details.
        
        @param request: GetErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_route_map(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        """
        @summary query lingjun hub routing policy details.
        
        @param request: GetErRouteMapRequest
        @return: GetErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_er_route_map_with_options(request, runtime)

    async def get_er_route_map_async(
        self,
        request: eflo_20220530_models.GetErRouteMapRequest,
    ) -> eflo_20220530_models.GetErRouteMapResponse:
        """
        @summary query lingjun hub routing policy details.
        
        @param request: GetErRouteMapRequest
        @return: GetErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_er_route_map_with_options_async(request, runtime)

    def get_fabric_topology_with_options(
        self,
        request: eflo_20220530_models.GetFabricTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetFabricTopologyResponse:
        """
        @summary Query the physical topology information of Lingjun network interface controller and Lingjun nodes under VPD.
        
        @param request: GetFabricTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFabricTopologyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.lni_ids):
            body['LniIds'] = request.lni_ids
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFabricTopology',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetFabricTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fabric_topology_with_options_async(
        self,
        request: eflo_20220530_models.GetFabricTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetFabricTopologyResponse:
        """
        @summary Query the physical topology information of Lingjun network interface controller and Lingjun nodes under VPD.
        
        @param request: GetFabricTopologyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFabricTopologyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.lni_ids):
            body['LniIds'] = request.lni_ids
        if not UtilClient.is_unset(request.node_ids):
            body['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFabricTopology',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetFabricTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fabric_topology(
        self,
        request: eflo_20220530_models.GetFabricTopologyRequest,
    ) -> eflo_20220530_models.GetFabricTopologyResponse:
        """
        @summary Query the physical topology information of Lingjun network interface controller and Lingjun nodes under VPD.
        
        @param request: GetFabricTopologyRequest
        @return: GetFabricTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fabric_topology_with_options(request, runtime)

    async def get_fabric_topology_async(
        self,
        request: eflo_20220530_models.GetFabricTopologyRequest,
    ) -> eflo_20220530_models.GetFabricTopologyResponse:
        """
        @summary Query the physical topology information of Lingjun network interface controller and Lingjun nodes under VPD.
        
        @param request: GetFabricTopologyRequest
        @return: GetFabricTopologyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fabric_topology_with_options_async(request, runtime)

    def get_leni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.GetLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetLeniPrivateIpAddressResponse:
        """
        @summary Obtains the details of the secondary private IP address of a specified Lingjun Elastic Network Interface.
        
        @param request: GetLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_leni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.GetLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetLeniPrivateIpAddressResponse:
        """
        @summary Obtains the details of the secondary private IP address of a specified Lingjun Elastic Network Interface.
        
        @param request: GetLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_leni_private_ip_address(
        self,
        request: eflo_20220530_models.GetLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.GetLeniPrivateIpAddressResponse:
        """
        @summary Obtains the details of the secondary private IP address of a specified Lingjun Elastic Network Interface.
        
        @param request: GetLeniPrivateIpAddressRequest
        @return: GetLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_leni_private_ip_address_with_options(request, runtime)

    async def get_leni_private_ip_address_async(
        self,
        request: eflo_20220530_models.GetLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.GetLeniPrivateIpAddressResponse:
        """
        @summary Obtains the details of the secondary private IP address of a specified Lingjun Elastic Network Interface.
        
        @param request: GetLeniPrivateIpAddressRequest
        @return: GetLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_leni_private_ip_address_with_options_async(request, runtime)

    def get_lni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        """
        @summary Obtains the details about the secondary private IP address.
        
        @param request: GetLniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        """
        @summary Obtains the details about the secondary private IP address.
        
        @param request: GetLniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetLniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lni_private_ip_address(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        """
        @summary Obtains the details about the secondary private IP address.
        
        @param request: GetLniPrivateIpAddressRequest
        @return: GetLniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_lni_private_ip_address_with_options(request, runtime)

    async def get_lni_private_ip_address_async(
        self,
        request: eflo_20220530_models.GetLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.GetLniPrivateIpAddressResponse:
        """
        @summary Obtains the details about the secondary private IP address.
        
        @param request: GetLniPrivateIpAddressRequest
        @return: GetLniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_lni_private_ip_address_with_options_async(request, runtime)

    def get_network_interface_with_options(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        """
        @summary Queries information about an LNI.
        
        @param request: GetNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        """
        @summary Queries information about an LNI.
        
        @param request: GetNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_interface(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        """
        @summary Queries information about an LNI.
        
        @param request: GetNetworkInterfaceRequest
        @return: GetNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_network_interface_with_options(request, runtime)

    async def get_network_interface_async(
        self,
        request: eflo_20220530_models.GetNetworkInterfaceRequest,
    ) -> eflo_20220530_models.GetNetworkInterfaceResponse:
        """
        @summary Queries information about an LNI.
        
        @param request: GetNetworkInterfaceRequest
        @return: GetNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_network_interface_with_options_async(request, runtime)

    def get_node_info_for_pod_with_options(
        self,
        request: eflo_20220530_models.GetNodeInfoForPodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetNodeInfoForPodResponse:
        """
        @summary Queries the network information of a node.
        
        @param request: GetNodeInfoForPodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeInfoForPodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeInfoForPod',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetNodeInfoForPodResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_info_for_pod_with_options_async(
        self,
        request: eflo_20220530_models.GetNodeInfoForPodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetNodeInfoForPodResponse:
        """
        @summary Queries the network information of a node.
        
        @param request: GetNodeInfoForPodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeInfoForPodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeInfoForPod',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetNodeInfoForPodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_info_for_pod(
        self,
        request: eflo_20220530_models.GetNodeInfoForPodRequest,
    ) -> eflo_20220530_models.GetNodeInfoForPodResponse:
        """
        @summary Queries the network information of a node.
        
        @param request: GetNodeInfoForPodRequest
        @return: GetNodeInfoForPodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_info_for_pod_with_options(request, runtime)

    async def get_node_info_for_pod_async(
        self,
        request: eflo_20220530_models.GetNodeInfoForPodRequest,
    ) -> eflo_20220530_models.GetNodeInfoForPodResponse:
        """
        @summary Queries the network information of a node.
        
        @param request: GetNodeInfoForPodRequest
        @return: GetNodeInfoForPodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_node_info_for_pod_with_options_async(request, runtime)

    def get_subnet_with_options(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetSubnetResponse:
        """
        @summary Queries the details of a Lingjun subnet, including the type, CIDR block, instance ID, instance status, and number of NCs.
        
        @param request: GetSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subnet_with_options_async(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetSubnetResponse:
        """
        @summary Queries the details of a Lingjun subnet, including the type, CIDR block, instance ID, instance status, and number of NCs.
        
        @param request: GetSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subnet(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
    ) -> eflo_20220530_models.GetSubnetResponse:
        """
        @summary Queries the details of a Lingjun subnet, including the type, CIDR block, instance ID, instance status, and number of NCs.
        
        @param request: GetSubnetRequest
        @return: GetSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_subnet_with_options(request, runtime)

    async def get_subnet_async(
        self,
        request: eflo_20220530_models.GetSubnetRequest,
    ) -> eflo_20220530_models.GetSubnetResponse:
        """
        @summary Queries the details of a Lingjun subnet, including the type, CIDR block, instance ID, instance status, and number of NCs.
        
        @param request: GetSubnetRequest
        @return: GetSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_subnet_with_options_async(request, runtime)

    def get_vcc_with_options(
        self,
        request: eflo_20220530_models.GetVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccResponse:
        """
        @summary Queries the details of a Lingjun connection, including the specification, Express Connect circuit access port type, instance status, bandwidth, and BGP CIDR block.
        
        @param request: GetVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_with_options_async(
        self,
        request: eflo_20220530_models.GetVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccResponse:
        """
        @summary Queries the details of a Lingjun connection, including the specification, Express Connect circuit access port type, instance status, bandwidth, and BGP CIDR block.
        
        @param request: GetVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc(
        self,
        request: eflo_20220530_models.GetVccRequest,
    ) -> eflo_20220530_models.GetVccResponse:
        """
        @summary Queries the details of a Lingjun connection, including the specification, Express Connect circuit access port type, instance status, bandwidth, and BGP CIDR block.
        
        @param request: GetVccRequest
        @return: GetVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_with_options(request, runtime)

    async def get_vcc_async(
        self,
        request: eflo_20220530_models.GetVccRequest,
    ) -> eflo_20220530_models.GetVccResponse:
        """
        @summary Queries the details of a Lingjun connection, including the specification, Express Connect circuit access port type, instance status, bandwidth, and BGP CIDR block.
        
        @param request: GetVccRequest
        @return: GetVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vcc_with_options_async(request, runtime)

    def get_vcc_grant_rule_with_options(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun connection, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVccGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVccGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun connection, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVccGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVccGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc_grant_rule(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun connection, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVccGrantRuleRequest
        @return: GetVccGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_grant_rule_with_options(request, runtime)

    async def get_vcc_grant_rule_async(
        self,
        request: eflo_20220530_models.GetVccGrantRuleRequest,
    ) -> eflo_20220530_models.GetVccGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun connection, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVccGrantRuleRequest
        @return: GetVccGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vcc_grant_rule_with_options_async(request, runtime)

    def get_vcc_route_entry_with_options(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVccRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVccRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vcc_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVccRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVccRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_route_entry_id):
            body['VccRouteEntryId'] = request.vcc_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVccRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVccRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vcc_route_entry(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVccRouteEntryRequest
        @return: GetVccRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vcc_route_entry_with_options(request, runtime)

    async def get_vcc_route_entry_async(
        self,
        request: eflo_20220530_models.GetVccRouteEntryRequest,
    ) -> eflo_20220530_models.GetVccRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVccRouteEntryRequest
        @return: GetVccRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vcc_route_entry_with_options_async(request, runtime)

    def get_vpd_with_options(
        self,
        request: eflo_20220530_models.GetVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdResponse:
        """
        @summary Queries the details of a Lingjun CIDR block, including the status of the Lingjun CIDR block, the CIDR block, the number of subnets and NCs.
        
        @param request: GetVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_with_options_async(
        self,
        request: eflo_20220530_models.GetVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdResponse:
        """
        @summary Queries the details of a Lingjun CIDR block, including the status of the Lingjun CIDR block, the CIDR block, the number of subnets and NCs.
        
        @param request: GetVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd(
        self,
        request: eflo_20220530_models.GetVpdRequest,
    ) -> eflo_20220530_models.GetVpdResponse:
        """
        @summary Queries the details of a Lingjun CIDR block, including the status of the Lingjun CIDR block, the CIDR block, the number of subnets and NCs.
        
        @param request: GetVpdRequest
        @return: GetVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_with_options(request, runtime)

    async def get_vpd_async(
        self,
        request: eflo_20220530_models.GetVpdRequest,
    ) -> eflo_20220530_models.GetVpdResponse:
        """
        @summary Queries the details of a Lingjun CIDR block, including the status of the Lingjun CIDR block, the CIDR block, the number of subnets and NCs.
        
        @param request: GetVpdRequest
        @return: GetVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vpd_with_options_async(request, runtime)

    def get_vpd_grant_rule_with_options(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun CIDR block, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVpdGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpdGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdGrantRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_grant_rule_with_options_async(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun CIDR block, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVpdGrantRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpdGrantRuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdGrantRule',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdGrantRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd_grant_rule(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun CIDR block, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVpdGrantRuleRequest
        @return: GetVpdGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_grant_rule_with_options(request, runtime)

    async def get_vpd_grant_rule_async(
        self,
        request: eflo_20220530_models.GetVpdGrantRuleRequest,
    ) -> eflo_20220530_models.GetVpdGrantRuleResponse:
        """
        @summary Queries the details of cross-account resource authorization for a Lingjun CIDR block, including the authorized tenant ID, Lingjun HUB instance ID, and network instance ID.
        
        @param request: GetVpdGrantRuleRequest
        @return: GetVpdGrantRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vpd_grant_rule_with_options_async(request, runtime)

    def get_vpd_route_entry_with_options(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVpdRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpdRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdRouteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vpd_route_entry_with_options_async(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVpdRouteEntryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVpdRouteEntryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVpdRouteEntry',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.GetVpdRouteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vpd_route_entry(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVpdRouteEntryRequest
        @return: GetVpdRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vpd_route_entry_with_options(request, runtime)

    async def get_vpd_route_entry_async(
        self,
        request: eflo_20220530_models.GetVpdRouteEntryRequest,
    ) -> eflo_20220530_models.GetVpdRouteEntryResponse:
        """
        @summary Queries route entries.
        
        @param request: GetVpdRouteEntryRequest
        @return: GetVpdRouteEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vpd_route_entry_with_options_async(request, runtime)

    def initialize_vcc_with_options(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.InitializeVccResponse:
        """
        @summary Initialize the Lingjun connection and authorize Intelligent Computing Lingjun to create an SLR in your account.
        
        @param request: InitializeVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitializeVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.InitializeVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_vcc_with_options_async(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.InitializeVccResponse:
        """
        @summary Initialize the Lingjun connection and authorize Intelligent Computing Lingjun to create an SLR in your account.
        
        @param request: InitializeVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitializeVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.InitializeVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_vcc(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
    ) -> eflo_20220530_models.InitializeVccResponse:
        """
        @summary Initialize the Lingjun connection and authorize Intelligent Computing Lingjun to create an SLR in your account.
        
        @param request: InitializeVccRequest
        @return: InitializeVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initialize_vcc_with_options(request, runtime)

    async def initialize_vcc_async(
        self,
        request: eflo_20220530_models.InitializeVccRequest,
    ) -> eflo_20220530_models.InitializeVccResponse:
        """
        @summary Initialize the Lingjun connection and authorize Intelligent Computing Lingjun to create an SLR in your account.
        
        @param request: InitializeVccRequest
        @return: InitializeVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initialize_vcc_with_options_async(request, runtime)

    def list_elastic_network_interfaces_with_options(
        self,
        request: eflo_20220530_models.ListElasticNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListElasticNetworkInterfacesResponse:
        """
        @summary Queries the LENIs that are associated with a Lingjun node.
        
        @param request: ListElasticNetworkInterfacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListElasticNetworkInterfacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListElasticNetworkInterfaces',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListElasticNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_elastic_network_interfaces_with_options_async(
        self,
        request: eflo_20220530_models.ListElasticNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListElasticNetworkInterfacesResponse:
        """
        @summary Queries the LENIs that are associated with a Lingjun node.
        
        @param request: ListElasticNetworkInterfacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListElasticNetworkInterfacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.v_switch_id):
            body['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListElasticNetworkInterfaces',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListElasticNetworkInterfacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_elastic_network_interfaces(
        self,
        request: eflo_20220530_models.ListElasticNetworkInterfacesRequest,
    ) -> eflo_20220530_models.ListElasticNetworkInterfacesResponse:
        """
        @summary Queries the LENIs that are associated with a Lingjun node.
        
        @param request: ListElasticNetworkInterfacesRequest
        @return: ListElasticNetworkInterfacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_elastic_network_interfaces_with_options(request, runtime)

    async def list_elastic_network_interfaces_async(
        self,
        request: eflo_20220530_models.ListElasticNetworkInterfacesRequest,
    ) -> eflo_20220530_models.ListElasticNetworkInterfacesResponse:
        """
        @summary Queries the LENIs that are associated with a Lingjun node.
        
        @param request: ListElasticNetworkInterfacesRequest
        @return: ListElasticNetworkInterfacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_elastic_network_interfaces_with_options_async(request, runtime)

    def list_er_attachments_with_options(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        """
        @summary Queries network instance connections.
        
        @param request: ListErAttachmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErAttachmentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErAttachments',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_attachments_with_options_async(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        """
        @summary Queries network instance connections.
        
        @param request: ListErAttachmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErAttachmentsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_receive_all_route):
            body['AutoReceiveAllRoute'] = request.auto_receive_all_route
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_tenant_id):
            body['ResourceTenantId'] = request.resource_tenant_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErAttachments',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_attachments(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        """
        @summary Queries network instance connections.
        
        @param request: ListErAttachmentsRequest
        @return: ListErAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_er_attachments_with_options(request, runtime)

    async def list_er_attachments_async(
        self,
        request: eflo_20220530_models.ListErAttachmentsRequest,
    ) -> eflo_20220530_models.ListErAttachmentsResponse:
        """
        @summary Queries network instance connections.
        
        @param request: ListErAttachmentsRequest
        @return: ListErAttachmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_er_attachments_with_options_async(request, runtime)

    def list_er_route_entries_with_options(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun HUB.
        
        @param request: ListErRouteEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErRouteEntriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_route_entries_with_options_async(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun HUB.
        
        @param request: ListErRouteEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErRouteEntriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_route_entries(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun HUB.
        
        @param request: ListErRouteEntriesRequest
        @return: ListErRouteEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_er_route_entries_with_options(request, runtime)

    async def list_er_route_entries_async(
        self,
        request: eflo_20220530_models.ListErRouteEntriesRequest,
    ) -> eflo_20220530_models.ListErRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun HUB.
        
        @param request: ListErRouteEntriesRequest
        @return: ListErRouteEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_er_route_entries_with_options_async(request, runtime)

    def list_er_route_maps_with_options(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        """
        @summary Routing policies are queried.
        
        @param request: ListErRouteMapsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErRouteMapsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.er_route_map_num):
            body['ErRouteMapNum'] = request.er_route_map_num
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_name):
            body['ReceptionInstanceName'] = request.reception_instance_name
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_name):
            body['TransmissionInstanceName'] = request.transmission_instance_name
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteMaps',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_er_route_maps_with_options_async(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        """
        @summary Routing policies are queried.
        
        @param request: ListErRouteMapsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErRouteMapsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.er_route_map_num):
            body['ErRouteMapNum'] = request.er_route_map_num
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.reception_instance_id):
            body['ReceptionInstanceId'] = request.reception_instance_id
        if not UtilClient.is_unset(request.reception_instance_name):
            body['ReceptionInstanceName'] = request.reception_instance_name
        if not UtilClient.is_unset(request.reception_instance_type):
            body['ReceptionInstanceType'] = request.reception_instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_map_action):
            body['RouteMapAction'] = request.route_map_action
        if not UtilClient.is_unset(request.transmission_instance_id):
            body['TransmissionInstanceId'] = request.transmission_instance_id
        if not UtilClient.is_unset(request.transmission_instance_name):
            body['TransmissionInstanceName'] = request.transmission_instance_name
        if not UtilClient.is_unset(request.transmission_instance_type):
            body['TransmissionInstanceType'] = request.transmission_instance_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErRouteMaps',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErRouteMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_er_route_maps(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        """
        @summary Routing policies are queried.
        
        @param request: ListErRouteMapsRequest
        @return: ListErRouteMapsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_er_route_maps_with_options(request, runtime)

    async def list_er_route_maps_async(
        self,
        request: eflo_20220530_models.ListErRouteMapsRequest,
    ) -> eflo_20220530_models.ListErRouteMapsResponse:
        """
        @summary Routing policies are queried.
        
        @param request: ListErRouteMapsRequest
        @return: ListErRouteMapsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_er_route_maps_with_options_async(request, runtime)

    def list_ers_with_options(
        self,
        request: eflo_20220530_models.ListErsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErsResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: ListErsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ers_with_options_async(
        self,
        request: eflo_20220530_models.ListErsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListErsResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: ListErsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListErsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.master_zone_id):
            body['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListErs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListErsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ers(
        self,
        request: eflo_20220530_models.ListErsRequest,
    ) -> eflo_20220530_models.ListErsResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: ListErsRequest
        @return: ListErsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_ers_with_options(request, runtime)

    async def list_ers_async(
        self,
        request: eflo_20220530_models.ListErsRequest,
    ) -> eflo_20220530_models.ListErsResponse:
        """
        @summary Queries the Lingjun HUB.
        
        @param request: ListErsRequest
        @return: ListErsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_ers_with_options_async(request, runtime)

    def list_instances_by_ncd_with_options(
        self,
        request: eflo_20220530_models.ListInstancesByNcdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListInstancesByNcdResponse:
        """
        @summary Queries the GPU node list of a specified GPU node whose communication distance does not exceed the specified NCD.
        
        @param request: ListInstancesByNcdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesByNcdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_ncd):
            body['MaxNcd'] = request.max_ncd
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstancesByNcd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListInstancesByNcdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_by_ncd_with_options_async(
        self,
        request: eflo_20220530_models.ListInstancesByNcdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListInstancesByNcdResponse:
        """
        @summary Queries the GPU node list of a specified GPU node whose communication distance does not exceed the specified NCD.
        
        @param request: ListInstancesByNcdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesByNcdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_ncd):
            body['MaxNcd'] = request.max_ncd
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstancesByNcd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListInstancesByNcdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_by_ncd(
        self,
        request: eflo_20220530_models.ListInstancesByNcdRequest,
    ) -> eflo_20220530_models.ListInstancesByNcdResponse:
        """
        @summary Queries the GPU node list of a specified GPU node whose communication distance does not exceed the specified NCD.
        
        @param request: ListInstancesByNcdRequest
        @return: ListInstancesByNcdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_by_ncd_with_options(request, runtime)

    async def list_instances_by_ncd_async(
        self,
        request: eflo_20220530_models.ListInstancesByNcdRequest,
    ) -> eflo_20220530_models.ListInstancesByNcdResponse:
        """
        @summary Queries the GPU node list of a specified GPU node whose communication distance does not exceed the specified NCD.
        
        @param request: ListInstancesByNcdRequest
        @return: ListInstancesByNcdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_by_ncd_with_options_async(request, runtime)

    def list_leni_private_ip_addresses_with_options(
        self,
        request: eflo_20220530_models.ListLeniPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListLeniPrivateIpAddressesResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun Elastic Network Interface.
        
        @param request: ListLeniPrivateIpAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLeniPrivateIpAddressesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLeniPrivateIpAddresses',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListLeniPrivateIpAddressesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_leni_private_ip_addresses_with_options_async(
        self,
        request: eflo_20220530_models.ListLeniPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListLeniPrivateIpAddressesResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun Elastic Network Interface.
        
        @param request: ListLeniPrivateIpAddressesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLeniPrivateIpAddressesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLeniPrivateIpAddresses',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListLeniPrivateIpAddressesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_leni_private_ip_addresses(
        self,
        request: eflo_20220530_models.ListLeniPrivateIpAddressesRequest,
    ) -> eflo_20220530_models.ListLeniPrivateIpAddressesResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun Elastic Network Interface.
        
        @param request: ListLeniPrivateIpAddressesRequest
        @return: ListLeniPrivateIpAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_leni_private_ip_addresses_with_options(request, runtime)

    async def list_leni_private_ip_addresses_async(
        self,
        request: eflo_20220530_models.ListLeniPrivateIpAddressesRequest,
    ) -> eflo_20220530_models.ListLeniPrivateIpAddressesResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun Elastic Network Interface.
        
        @param request: ListLeniPrivateIpAddressesRequest
        @return: ListLeniPrivateIpAddressesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_leni_private_ip_addresses_with_options_async(request, runtime)

    def list_lni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun network interface controller.
        
        @param request: ListLniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListLniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun network interface controller.
        
        @param request: ListLniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListLniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lni_private_ip_address(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun network interface controller.
        
        @param request: ListLniPrivateIpAddressRequest
        @return: ListLniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_lni_private_ip_address_with_options(request, runtime)

    async def list_lni_private_ip_address_async(
        self,
        request: eflo_20220530_models.ListLniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.ListLniPrivateIpAddressResponse:
        """
        @summary Queries the list of secondary private IP addresses of Lingjun network interface controller.
        
        @param request: ListLniPrivateIpAddressRequest
        @return: ListLniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_lni_private_ip_address_with_options_async(request, runtime)

    def list_network_interfaces_with_options(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        """
        @summary Queries Lingjun network interfaces (LNIs).
        
        @param request: ListNetworkInterfacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkInterfacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNetworkInterfaces',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListNetworkInterfacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_interfaces_with_options_async(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        """
        @summary Queries Lingjun network interfaces (LNIs).
        
        @param request: ListNetworkInterfacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkInterfacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNetworkInterfaces',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListNetworkInterfacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_interfaces(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        """
        @summary Queries Lingjun network interfaces (LNIs).
        
        @param request: ListNetworkInterfacesRequest
        @return: ListNetworkInterfacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_interfaces_with_options(request, runtime)

    async def list_network_interfaces_async(
        self,
        request: eflo_20220530_models.ListNetworkInterfacesRequest,
    ) -> eflo_20220530_models.ListNetworkInterfacesResponse:
        """
        @summary Queries Lingjun network interfaces (LNIs).
        
        @param request: ListNetworkInterfacesRequest
        @return: ListNetworkInterfacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_interfaces_with_options_async(request, runtime)

    def list_node_infos_for_pod_with_options(
        self,
        request: eflo_20220530_models.ListNodeInfosForPodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListNodeInfosForPodResponse:
        """
        @summary Queries node network information.
        
        @param request: ListNodeInfosForPodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeInfosForPodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeInfosForPod',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListNodeInfosForPodResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_infos_for_pod_with_options_async(
        self,
        request: eflo_20220530_models.ListNodeInfosForPodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListNodeInfosForPodResponse:
        """
        @summary Queries node network information.
        
        @param request: ListNodeInfosForPodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeInfosForPodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeInfosForPod',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListNodeInfosForPodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_infos_for_pod(
        self,
        request: eflo_20220530_models.ListNodeInfosForPodRequest,
    ) -> eflo_20220530_models.ListNodeInfosForPodResponse:
        """
        @summary Queries node network information.
        
        @param request: ListNodeInfosForPodRequest
        @return: ListNodeInfosForPodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_infos_for_pod_with_options(request, runtime)

    async def list_node_infos_for_pod_async(
        self,
        request: eflo_20220530_models.ListNodeInfosForPodRequest,
    ) -> eflo_20220530_models.ListNodeInfosForPodResponse:
        """
        @summary Queries node network information.
        
        @param request: ListNodeInfosForPodRequest
        @return: ListNodeInfosForPodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_node_infos_for_pod_with_options_async(request, runtime)

    def list_subnets_with_options(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        """
        @summary You can call this operation to query the details of one or more Lingjun subnets, including the Lingjun subnet type, network address segment, and instance ID of the Lingjun CIDR block.
        
        @param request: ListSubnetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubnetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubnets',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListSubnetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subnets_with_options_async(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        """
        @summary You can call this operation to query the details of one or more Lingjun subnets, including the Lingjun subnet type, network address segment, and instance ID of the Lingjun CIDR block.
        
        @param request: ListSubnetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubnetsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubnets',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListSubnetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subnets(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        """
        @summary You can call this operation to query the details of one or more Lingjun subnets, including the Lingjun subnet type, network address segment, and instance ID of the Lingjun CIDR block.
        
        @param request: ListSubnetsRequest
        @return: ListSubnetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_subnets_with_options(request, runtime)

    async def list_subnets_async(
        self,
        request: eflo_20220530_models.ListSubnetsRequest,
    ) -> eflo_20220530_models.ListSubnetsResponse:
        """
        @summary You can call this operation to query the details of one or more Lingjun subnets, including the Lingjun subnet type, network address segment, and instance ID of the Lingjun CIDR block.
        
        @param request: ListSubnetsRequest
        @return: ListSubnetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_subnets_with_options_async(request, runtime)

    def list_vcc_flow_infos_with_options(
        self,
        request: eflo_20220530_models.ListVccFlowInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccFlowInfosResponse:
        """
        @summary Queries the traffic rate of a Lingjun connection.
        
        @param request: ListVccFlowInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccFlowInfosResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.direction):
            body['Direction'] = request.direction
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.metric_name):
            body['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccFlowInfos',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccFlowInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_flow_infos_with_options_async(
        self,
        request: eflo_20220530_models.ListVccFlowInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccFlowInfosResponse:
        """
        @summary Queries the traffic rate of a Lingjun connection.
        
        @param request: ListVccFlowInfosRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccFlowInfosResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.direction):
            body['Direction'] = request.direction
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.metric_name):
            body['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccFlowInfos',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccFlowInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_flow_infos(
        self,
        request: eflo_20220530_models.ListVccFlowInfosRequest,
    ) -> eflo_20220530_models.ListVccFlowInfosResponse:
        """
        @summary Queries the traffic rate of a Lingjun connection.
        
        @param request: ListVccFlowInfosRequest
        @return: ListVccFlowInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vcc_flow_infos_with_options(request, runtime)

    async def list_vcc_flow_infos_async(
        self,
        request: eflo_20220530_models.ListVccFlowInfosRequest,
    ) -> eflo_20220530_models.ListVccFlowInfosResponse:
        """
        @summary Queries the traffic rate of a Lingjun connection.
        
        @param request: ListVccFlowInfosRequest
        @return: ListVccFlowInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vcc_flow_infos_with_options_async(request, runtime)

    def list_vcc_grant_rules_with_options(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        """
        @summary Queries the details of a Lingjun connection authorization, including the authorized tenant ID, region, and Lingjun HUB instance information.
        
        @param request: ListVccGrantRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccGrantRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_grant_rules_with_options_async(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        """
        @summary Queries the details of a Lingjun connection authorization, including the authorized tenant ID, region, and Lingjun HUB instance information.
        
        @param request: ListVccGrantRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccGrantRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_grant_rules(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        """
        @summary Queries the details of a Lingjun connection authorization, including the authorized tenant ID, region, and Lingjun HUB instance information.
        
        @param request: ListVccGrantRulesRequest
        @return: ListVccGrantRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vcc_grant_rules_with_options(request, runtime)

    async def list_vcc_grant_rules_async(
        self,
        request: eflo_20220530_models.ListVccGrantRulesRequest,
    ) -> eflo_20220530_models.ListVccGrantRulesResponse:
        """
        @summary Queries the details of a Lingjun connection authorization, including the authorized tenant ID, region, and Lingjun HUB instance information.
        
        @param request: ListVccGrantRulesRequest
        @return: ListVccGrantRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vcc_grant_rules_with_options_async(request, runtime)

    def list_vcc_route_entries_with_options(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        """
        @summary Queries Lingjun connection route entries.
        
        @param request: ListVccRouteEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccRouteEntriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vcc_route_entries_with_options_async(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        """
        @summary Queries Lingjun connection route entries.
        
        @param request: ListVccRouteEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccRouteEntriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vcc_route_entries(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        """
        @summary Queries Lingjun connection route entries.
        
        @param request: ListVccRouteEntriesRequest
        @return: ListVccRouteEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vcc_route_entries_with_options(request, runtime)

    async def list_vcc_route_entries_async(
        self,
        request: eflo_20220530_models.ListVccRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVccRouteEntriesResponse:
        """
        @summary Queries Lingjun connection route entries.
        
        @param request: ListVccRouteEntriesRequest
        @return: ListVccRouteEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vcc_route_entries_with_options_async(request, runtime)

    def list_vccs_with_options(
        self,
        request: eflo_20220530_models.ListVccsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccsResponse:
        """
        @summary query the details of one or more lingjun connections, including the specification, Express Connect circuit access port type, instance status, bandwidth, and bgp network segment.
        
        @param request: ListVccsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ex_status):
            body['ExStatus'] = request.ex_status
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vccs_with_options_async(
        self,
        request: eflo_20220530_models.ListVccsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVccsResponse:
        """
        @summary query the details of one or more lingjun connections, including the specification, Express Connect circuit access port type, instance status, bandwidth, and bgp network segment.
        
        @param request: ListVccsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVccsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            body['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ex_status):
            body['ExStatus'] = request.ex_status
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVccs',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVccsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vccs(
        self,
        request: eflo_20220530_models.ListVccsRequest,
    ) -> eflo_20220530_models.ListVccsResponse:
        """
        @summary query the details of one or more lingjun connections, including the specification, Express Connect circuit access port type, instance status, bandwidth, and bgp network segment.
        
        @param request: ListVccsRequest
        @return: ListVccsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vccs_with_options(request, runtime)

    async def list_vccs_async(
        self,
        request: eflo_20220530_models.ListVccsRequest,
    ) -> eflo_20220530_models.ListVccsResponse:
        """
        @summary query the details of one or more lingjun connections, including the specification, Express Connect circuit access port type, instance status, bandwidth, and bgp network segment.
        
        @param request: ListVccsRequest
        @return: ListVccsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vccs_with_options_async(request, runtime)

    def list_vpd_grant_rules_with_options(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        """
        @summary Queries the details of one or more route entries in the CIDR block of Lingjun, including the route type, route entry status, destination CIDR block, and instance information of the next route entry.
        
        @param request: ListVpdGrantRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpdGrantRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdGrantRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpd_grant_rules_with_options_async(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        """
        @summary Queries the details of one or more route entries in the CIDR block of Lingjun, including the route type, route entry status, destination CIDR block, and instance information of the next route entry.
        
        @param request: ListVpdGrantRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpdGrantRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.grant_rule_id):
            body['GrantRuleId'] = request.grant_rule_id
        if not UtilClient.is_unset(request.grant_tenant_id):
            body['GrantTenantId'] = request.grant_tenant_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdGrantRules',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdGrantRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpd_grant_rules(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        """
        @summary Queries the details of one or more route entries in the CIDR block of Lingjun, including the route type, route entry status, destination CIDR block, and instance information of the next route entry.
        
        @param request: ListVpdGrantRulesRequest
        @return: ListVpdGrantRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vpd_grant_rules_with_options(request, runtime)

    async def list_vpd_grant_rules_async(
        self,
        request: eflo_20220530_models.ListVpdGrantRulesRequest,
    ) -> eflo_20220530_models.ListVpdGrantRulesResponse:
        """
        @summary Queries the details of one or more route entries in the CIDR block of Lingjun, including the route type, route entry status, destination CIDR block, and instance information of the next route entry.
        
        @param request: ListVpdGrantRulesRequest
        @return: ListVpdGrantRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vpd_grant_rules_with_options_async(request, runtime)

    def list_vpd_route_entries_with_options(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun CIDR block.
        
        @param request: ListVpdRouteEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpdRouteEntriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdRouteEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpd_route_entries_with_options_async(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun CIDR block.
        
        @param request: ListVpdRouteEntriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpdRouteEntriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.destination_cidr_block):
            body['DestinationCidrBlock'] = request.destination_cidr_block
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.ignore_detailed_route_entry):
            body['IgnoreDetailedRouteEntry'] = request.ignore_detailed_route_entry
        if not UtilClient.is_unset(request.next_hop_id):
            body['NextHopId'] = request.next_hop_id
        if not UtilClient.is_unset(request.next_hop_type):
            body['NextHopType'] = request.next_hop_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.route_type):
            body['RouteType'] = request.route_type
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_route_entry_id):
            body['VpdRouteEntryId'] = request.vpd_route_entry_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpdRouteEntries',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdRouteEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpd_route_entries(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun CIDR block.
        
        @param request: ListVpdRouteEntriesRequest
        @return: ListVpdRouteEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vpd_route_entries_with_options(request, runtime)

    async def list_vpd_route_entries_async(
        self,
        request: eflo_20220530_models.ListVpdRouteEntriesRequest,
    ) -> eflo_20220530_models.ListVpdRouteEntriesResponse:
        """
        @summary Queries the route entries of the Lingjun CIDR block.
        
        @param request: ListVpdRouteEntriesRequest
        @return: ListVpdRouteEntriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vpd_route_entries_with_options_async(request, runtime)

    def list_vpds_with_options(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdsResponse:
        """
        @summary Queries the details of one or more Lingjun CIDR blocks, including the status of Lingjun CIDR blocks, Cidr addresses, service CIDR blocks, and Subnet.
        
        @param request: ListVpdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpdsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        if not UtilClient.is_unset(request.with_dependence):
            body['WithDependence'] = request.with_dependence
        if not UtilClient.is_unset(request.without_vcc):
            body['WithoutVcc'] = request.without_vcc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpds',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpds_with_options_async(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.ListVpdsResponse:
        """
        @summary Queries the details of one or more Lingjun CIDR blocks, including the status of Lingjun CIDR blocks, Cidr addresses, service CIDR blocks, and Subnet.
        
        @param request: ListVpdsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpdsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_page):
            body['EnablePage'] = request.enable_page
        if not UtilClient.is_unset(request.filter_er_id):
            body['FilterErId'] = request.filter_er_id
        if not UtilClient.is_unset(request.for_select):
            body['ForSelect'] = request.for_select
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        if not UtilClient.is_unset(request.with_dependence):
            body['WithDependence'] = request.with_dependence
        if not UtilClient.is_unset(request.without_vcc):
            body['WithoutVcc'] = request.without_vcc
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVpds',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.ListVpdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpds(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
    ) -> eflo_20220530_models.ListVpdsResponse:
        """
        @summary Queries the details of one or more Lingjun CIDR blocks, including the status of Lingjun CIDR blocks, Cidr addresses, service CIDR blocks, and Subnet.
        
        @param request: ListVpdsRequest
        @return: ListVpdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vpds_with_options(request, runtime)

    async def list_vpds_async(
        self,
        request: eflo_20220530_models.ListVpdsRequest,
    ) -> eflo_20220530_models.ListVpdsResponse:
        """
        @summary Queries the details of one or more Lingjun CIDR blocks, including the status of Lingjun CIDR blocks, Cidr addresses, service CIDR blocks, and Subnet.
        
        @param request: ListVpdsRequest
        @return: ListVpdsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vpds_with_options_async(request, runtime)

    def query_instance_ncd_with_options(
        self,
        request: eflo_20220530_models.QueryInstanceNcdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.QueryInstanceNcdResponse:
        """
        @summary Query the network communication distance (Network Communication Distance,NCD) between instances (Lingjun node, Lingjun network interface controller).
        
        @param request: QueryInstanceNcdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstanceNcdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id_1):
            body['InstanceId1'] = request.instance_id_1
        if not UtilClient.is_unset(request.instance_id_2):
            body['InstanceId2'] = request.instance_id_2
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInstanceNcd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.QueryInstanceNcdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_ncd_with_options_async(
        self,
        request: eflo_20220530_models.QueryInstanceNcdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.QueryInstanceNcdResponse:
        """
        @summary Query the network communication distance (Network Communication Distance,NCD) between instances (Lingjun node, Lingjun network interface controller).
        
        @param request: QueryInstanceNcdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstanceNcdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id_1):
            body['InstanceId1'] = request.instance_id_1
        if not UtilClient.is_unset(request.instance_id_2):
            body['InstanceId2'] = request.instance_id_2
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInstanceNcd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.QueryInstanceNcdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_ncd(
        self,
        request: eflo_20220530_models.QueryInstanceNcdRequest,
    ) -> eflo_20220530_models.QueryInstanceNcdResponse:
        """
        @summary Query the network communication distance (Network Communication Distance,NCD) between instances (Lingjun node, Lingjun network interface controller).
        
        @param request: QueryInstanceNcdRequest
        @return: QueryInstanceNcdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_instance_ncd_with_options(request, runtime)

    async def query_instance_ncd_async(
        self,
        request: eflo_20220530_models.QueryInstanceNcdRequest,
    ) -> eflo_20220530_models.QueryInstanceNcdResponse:
        """
        @summary Query the network communication distance (Network Communication Distance,NCD) between instances (Lingjun node, Lingjun network interface controller).
        
        @param request: QueryInstanceNcdRequest
        @return: QueryInstanceNcdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_ncd_with_options_async(request, runtime)

    def refund_vcc_with_options(
        self,
        request: eflo_20220530_models.RefundVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.RefundVccResponse:
        """
        @summary Unsubscribe inactive Lingjun connection
        
        @description Only unsubscribable for Lingjun connections in the prepayment status.
        
        @param request: RefundVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefundVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.RefundVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_vcc_with_options_async(
        self,
        request: eflo_20220530_models.RefundVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.RefundVccResponse:
        """
        @summary Unsubscribe inactive Lingjun connection
        
        @description Only unsubscribable for Lingjun connections in the prepayment status.
        
        @param request: RefundVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefundVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.RefundVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_vcc(
        self,
        request: eflo_20220530_models.RefundVccRequest,
    ) -> eflo_20220530_models.RefundVccResponse:
        """
        @summary Unsubscribe inactive Lingjun connection
        
        @description Only unsubscribable for Lingjun connections in the prepayment status.
        
        @param request: RefundVccRequest
        @return: RefundVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refund_vcc_with_options(request, runtime)

    async def refund_vcc_async(
        self,
        request: eflo_20220530_models.RefundVccRequest,
    ) -> eflo_20220530_models.RefundVccResponse:
        """
        @summary Unsubscribe inactive Lingjun connection
        
        @description Only unsubscribable for Lingjun connections in the prepayment status.
        
        @param request: RefundVccRequest
        @return: RefundVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refund_vcc_with_options_async(request, runtime)

    def retry_vcc_with_options(
        self,
        request: eflo_20220530_models.RetryVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.RetryVccResponse:
        """
        @summary Retry trying to create /delete a Lingjun connection.
        
        @description This operation allows the user to retry the operation if the Lingjun connection creation and deletion processes fail. Only the Lingjun connection in the creation failure and deletion failure state can be retried
        
        @param request: RetryVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.RetryVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_vcc_with_options_async(
        self,
        request: eflo_20220530_models.RetryVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.RetryVccResponse:
        """
        @summary Retry trying to create /delete a Lingjun connection.
        
        @description This operation allows the user to retry the operation if the Lingjun connection creation and deletion processes fail. Only the Lingjun connection in the creation failure and deletion failure state can be retried
        
        @param request: RetryVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.RetryVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_vcc(
        self,
        request: eflo_20220530_models.RetryVccRequest,
    ) -> eflo_20220530_models.RetryVccResponse:
        """
        @summary Retry trying to create /delete a Lingjun connection.
        
        @description This operation allows the user to retry the operation if the Lingjun connection creation and deletion processes fail. Only the Lingjun connection in the creation failure and deletion failure state can be retried
        
        @param request: RetryVccRequest
        @return: RetryVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_vcc_with_options(request, runtime)

    async def retry_vcc_async(
        self,
        request: eflo_20220530_models.RetryVccRequest,
    ) -> eflo_20220530_models.RetryVccResponse:
        """
        @summary Retry trying to create /delete a Lingjun connection.
        
        @description This operation allows the user to retry the operation if the Lingjun connection creation and deletion processes fail. Only the Lingjun connection in the creation failure and deletion failure state can be retried
        
        @param request: RetryVccRequest
        @return: RetryVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retry_vcc_with_options_async(request, runtime)

    def un_assign_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        """
        @summary Deletes an assigned secondary private IP address.
        
        @param request: UnAssignPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnAssignPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnAssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnAssignPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_assign_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        """
        @summary Deletes an assigned secondary private IP address.
        
        @param request: UnAssignPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnAssignPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.network_interface_id):
            body['NetworkInterfaceId'] = request.network_interface_id
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnAssignPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnAssignPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_assign_private_ip_address(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        """
        @summary Deletes an assigned secondary private IP address.
        
        @param request: UnAssignPrivateIpAddressRequest
        @return: UnAssignPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_assign_private_ip_address_with_options(request, runtime)

    async def un_assign_private_ip_address_async(
        self,
        request: eflo_20220530_models.UnAssignPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UnAssignPrivateIpAddressResponse:
        """
        @summary Deletes an assigned secondary private IP address.
        
        @param request: UnAssignPrivateIpAddressRequest
        @return: UnAssignPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_assign_private_ip_address_with_options_async(request, runtime)

    def un_associate_vpd_cidr_block_with_options(
        self,
        request: eflo_20220530_models.UnAssociateVpdCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnAssociateVpdCidrBlockResponse:
        """
        @summary This function can be used to delete the additional network segment of VPD.
        
        @description *\
        *Warning** If the attached CIDR block has Lingjun subnet resources, you must delete the dependent resources before you can delete the attached CIDR block.
        
        @param request: UnAssociateVpdCidrBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnAssociateVpdCidrBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnAssociateVpdCidrBlock',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnAssociateVpdCidrBlockResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_associate_vpd_cidr_block_with_options_async(
        self,
        request: eflo_20220530_models.UnAssociateVpdCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnAssociateVpdCidrBlockResponse:
        """
        @summary This function can be used to delete the additional network segment of VPD.
        
        @description *\
        *Warning** If the attached CIDR block has Lingjun subnet resources, you must delete the dependent resources before you can delete the attached CIDR block.
        
        @param request: UnAssociateVpdCidrBlockRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnAssociateVpdCidrBlockResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.secondary_cidr_block):
            body['SecondaryCidrBlock'] = request.secondary_cidr_block
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnAssociateVpdCidrBlock',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnAssociateVpdCidrBlockResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_associate_vpd_cidr_block(
        self,
        request: eflo_20220530_models.UnAssociateVpdCidrBlockRequest,
    ) -> eflo_20220530_models.UnAssociateVpdCidrBlockResponse:
        """
        @summary This function can be used to delete the additional network segment of VPD.
        
        @description *\
        *Warning** If the attached CIDR block has Lingjun subnet resources, you must delete the dependent resources before you can delete the attached CIDR block.
        
        @param request: UnAssociateVpdCidrBlockRequest
        @return: UnAssociateVpdCidrBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_associate_vpd_cidr_block_with_options(request, runtime)

    async def un_associate_vpd_cidr_block_async(
        self,
        request: eflo_20220530_models.UnAssociateVpdCidrBlockRequest,
    ) -> eflo_20220530_models.UnAssociateVpdCidrBlockResponse:
        """
        @summary This function can be used to delete the additional network segment of VPD.
        
        @description *\
        *Warning** If the attached CIDR block has Lingjun subnet resources, you must delete the dependent resources before you can delete the attached CIDR block.
        
        @param request: UnAssociateVpdCidrBlockRequest
        @return: UnAssociateVpdCidrBlockResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_associate_vpd_cidr_block_with_options_async(request, runtime)

    def unassign_leni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.UnassignLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnassignLeniPrivateIpAddressResponse:
        """
        @summary Delete the assigned secondary private IP address of Lingjun Elastic Network Interface.
        
        @param request: UnassignLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnassignLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnassignLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnassignLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def unassign_leni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.UnassignLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UnassignLeniPrivateIpAddressResponse:
        """
        @summary Delete the assigned secondary private IP address of Lingjun Elastic Network Interface.
        
        @param request: UnassignLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnassignLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnassignLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UnassignLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unassign_leni_private_ip_address(
        self,
        request: eflo_20220530_models.UnassignLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UnassignLeniPrivateIpAddressResponse:
        """
        @summary Delete the assigned secondary private IP address of Lingjun Elastic Network Interface.
        
        @param request: UnassignLeniPrivateIpAddressRequest
        @return: UnassignLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unassign_leni_private_ip_address_with_options(request, runtime)

    async def unassign_leni_private_ip_address_async(
        self,
        request: eflo_20220530_models.UnassignLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UnassignLeniPrivateIpAddressResponse:
        """
        @summary Delete the assigned secondary private IP address of Lingjun Elastic Network Interface.
        
        @param request: UnassignLeniPrivateIpAddressRequest
        @return: UnassignLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unassign_leni_private_ip_address_with_options_async(request, runtime)

    def update_elastic_network_interface_with_options(
        self,
        request: eflo_20220530_models.UpdateElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateElasticNetworkInterfaceResponse:
        """
        @summary Update Lingjun Elastic Network Interface information.
        
        @param request: UpdateElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateElasticNetworkInterfaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_elastic_network_interface_with_options_async(
        self,
        request: eflo_20220530_models.UpdateElasticNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateElasticNetworkInterfaceResponse:
        """
        @summary Update Lingjun Elastic Network Interface information.
        
        @param request: UpdateElasticNetworkInterfaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateElasticNetworkInterfaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            body['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateElasticNetworkInterface',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateElasticNetworkInterfaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_elastic_network_interface(
        self,
        request: eflo_20220530_models.UpdateElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.UpdateElasticNetworkInterfaceResponse:
        """
        @summary Update Lingjun Elastic Network Interface information.
        
        @param request: UpdateElasticNetworkInterfaceRequest
        @return: UpdateElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_elastic_network_interface_with_options(request, runtime)

    async def update_elastic_network_interface_async(
        self,
        request: eflo_20220530_models.UpdateElasticNetworkInterfaceRequest,
    ) -> eflo_20220530_models.UpdateElasticNetworkInterfaceResponse:
        """
        @summary Update Lingjun Elastic Network Interface information.
        
        @param request: UpdateElasticNetworkInterfaceRequest
        @return: UpdateElasticNetworkInterfaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_elastic_network_interface_with_options_async(request, runtime)

    def update_er_with_options(
        self,
        request: eflo_20220530_models.UpdateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErResponse:
        """
        @summary Updated Lingjun HUB.
        
        @param request: UpdateErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_with_options_async(
        self,
        request: eflo_20220530_models.UpdateErRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErResponse:
        """
        @summary Updated Lingjun HUB.
        
        @param request: UpdateErRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateErResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_name):
            body['ErName'] = request.er_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEr',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er(
        self,
        request: eflo_20220530_models.UpdateErRequest,
    ) -> eflo_20220530_models.UpdateErResponse:
        """
        @summary Updated Lingjun HUB.
        
        @param request: UpdateErRequest
        @return: UpdateErResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_er_with_options(request, runtime)

    async def update_er_async(
        self,
        request: eflo_20220530_models.UpdateErRequest,
    ) -> eflo_20220530_models.UpdateErResponse:
        """
        @summary Updated Lingjun HUB.
        
        @param request: UpdateErRequest
        @return: UpdateErResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_er_with_options_async(request, runtime)

    def update_er_attachment_with_options(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        """
        @summary Updates a network instance connection.
        
        @param request: UpdateErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_attachment_with_options_async(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        """
        @summary Updates a network instance connection.
        
        @param request: UpdateErAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateErAttachmentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.er_attachment_id):
            body['ErAttachmentId'] = request.er_attachment_id
        if not UtilClient.is_unset(request.er_attachment_name):
            body['ErAttachmentName'] = request.er_attachment_name
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErAttachment',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er_attachment(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        """
        @summary Updates a network instance connection.
        
        @param request: UpdateErAttachmentRequest
        @return: UpdateErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_er_attachment_with_options(request, runtime)

    async def update_er_attachment_async(
        self,
        request: eflo_20220530_models.UpdateErAttachmentRequest,
    ) -> eflo_20220530_models.UpdateErAttachmentResponse:
        """
        @summary Updates a network instance connection.
        
        @param request: UpdateErAttachmentRequest
        @return: UpdateErAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_er_attachment_with_options_async(request, runtime)

    def update_er_route_map_with_options(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        """
        @summary Update some information about the routing policy, including the description and name of the routing policy.
        
        @param request: UpdateErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErRouteMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_er_route_map_with_options_async(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        """
        @summary Update some information about the routing policy, including the description and name of the routing policy.
        
        @param request: UpdateErRouteMapRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateErRouteMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.er_id):
            body['ErId'] = request.er_id
        if not UtilClient.is_unset(request.er_route_map_id):
            body['ErRouteMapId'] = request.er_route_map_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateErRouteMap',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateErRouteMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_er_route_map(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        """
        @summary Update some information about the routing policy, including the description and name of the routing policy.
        
        @param request: UpdateErRouteMapRequest
        @return: UpdateErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_er_route_map_with_options(request, runtime)

    async def update_er_route_map_async(
        self,
        request: eflo_20220530_models.UpdateErRouteMapRequest,
    ) -> eflo_20220530_models.UpdateErRouteMapResponse:
        """
        @summary Update some information about the routing policy, including the description and name of the routing policy.
        
        @param request: UpdateErRouteMapRequest
        @return: UpdateErRouteMapResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_er_route_map_with_options_async(request, runtime)

    def update_leni_private_ip_address_with_options(
        self,
        request: eflo_20220530_models.UpdateLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateLeniPrivateIpAddressResponse:
        """
        @summary Updated the description of the secondary private network assigned by the Lingjun Elastic Network Interface.
        
        @param request: UpdateLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateLeniPrivateIpAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_leni_private_ip_address_with_options_async(
        self,
        request: eflo_20220530_models.UpdateLeniPrivateIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateLeniPrivateIpAddressResponse:
        """
        @summary Updated the description of the secondary private network assigned by the Lingjun Elastic Network Interface.
        
        @param request: UpdateLeniPrivateIpAddressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLeniPrivateIpAddressResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.elastic_network_interface_id):
            body['ElasticNetworkInterfaceId'] = request.elastic_network_interface_id
        if not UtilClient.is_unset(request.ip_name):
            body['IpName'] = request.ip_name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLeniPrivateIpAddress',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateLeniPrivateIpAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_leni_private_ip_address(
        self,
        request: eflo_20220530_models.UpdateLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UpdateLeniPrivateIpAddressResponse:
        """
        @summary Updated the description of the secondary private network assigned by the Lingjun Elastic Network Interface.
        
        @param request: UpdateLeniPrivateIpAddressRequest
        @return: UpdateLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_leni_private_ip_address_with_options(request, runtime)

    async def update_leni_private_ip_address_async(
        self,
        request: eflo_20220530_models.UpdateLeniPrivateIpAddressRequest,
    ) -> eflo_20220530_models.UpdateLeniPrivateIpAddressResponse:
        """
        @summary Updated the description of the secondary private network assigned by the Lingjun Elastic Network Interface.
        
        @param request: UpdateLeniPrivateIpAddressRequest
        @return: UpdateLeniPrivateIpAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_leni_private_ip_address_with_options_async(request, runtime)

    def update_subnet_with_options(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        """
        @summary Updates some information about a specified subnet instance, including the name of the subnet instance.
        
        @param request: UpdateSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateSubnetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subnet_with_options_async(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        """
        @summary Updates some information about a specified subnet instance, including the name of the subnet instance.
        
        @param request: UpdateSubnetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSubnetResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subnet_id):
            body['SubnetId'] = request.subnet_id
        if not UtilClient.is_unset(request.subnet_name):
            body['SubnetName'] = request.subnet_name
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubnet',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateSubnetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subnet(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        """
        @summary Updates some information about a specified subnet instance, including the name of the subnet instance.
        
        @param request: UpdateSubnetRequest
        @return: UpdateSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_subnet_with_options(request, runtime)

    async def update_subnet_async(
        self,
        request: eflo_20220530_models.UpdateSubnetRequest,
    ) -> eflo_20220530_models.UpdateSubnetResponse:
        """
        @summary Updates some information about a specified subnet instance, including the name of the subnet instance.
        
        @param request: UpdateSubnetRequest
        @return: UpdateSubnetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_subnet_with_options_async(request, runtime)

    def update_vcc_with_options(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVccResponse:
        """
        @summary Updates the information about a Lingjun connection instance, including the peak bandwidth and name of the Lingjun connection instance.
        
        @param request: UpdateVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVccResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vcc_with_options_async(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVccResponse:
        """
        @summary Updates the information about a Lingjun connection instance, including the peak bandwidth and name of the Lingjun connection instance.
        
        @param request: UpdateVccRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVccResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vcc_id):
            body['VccId'] = request.vcc_id
        if not UtilClient.is_unset(request.vcc_name):
            body['VccName'] = request.vcc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVcc',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vcc(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
    ) -> eflo_20220530_models.UpdateVccResponse:
        """
        @summary Updates the information about a Lingjun connection instance, including the peak bandwidth and name of the Lingjun connection instance.
        
        @param request: UpdateVccRequest
        @return: UpdateVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_vcc_with_options(request, runtime)

    async def update_vcc_async(
        self,
        request: eflo_20220530_models.UpdateVccRequest,
    ) -> eflo_20220530_models.UpdateVccResponse:
        """
        @summary Updates the information about a Lingjun connection instance, including the peak bandwidth and name of the Lingjun connection instance.
        
        @param request: UpdateVccRequest
        @return: UpdateVccResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_vcc_with_options_async(request, runtime)

    def update_vpd_with_options(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        """
        @summary Updates the information about the Lingjun CIDR block, including the name of the Lingjun CIDR block.
        
        @param request: UpdateVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVpdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vpd_with_options_async(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        """
        @summary Updates the information about the Lingjun CIDR block, including the name of the Lingjun CIDR block.
        
        @param request: UpdateVpdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVpdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpd_id):
            body['VpdId'] = request.vpd_id
        if not UtilClient.is_unset(request.vpd_name):
            body['VpdName'] = request.vpd_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVpd',
            version='2022-05-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_20220530_models.UpdateVpdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vpd(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        """
        @summary Updates the information about the Lingjun CIDR block, including the name of the Lingjun CIDR block.
        
        @param request: UpdateVpdRequest
        @return: UpdateVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_vpd_with_options(request, runtime)

    async def update_vpd_async(
        self,
        request: eflo_20220530_models.UpdateVpdRequest,
    ) -> eflo_20220530_models.UpdateVpdResponse:
        """
        @summary Updates the information about the Lingjun CIDR block, including the name of the Lingjun CIDR block.
        
        @param request: UpdateVpdRequest
        @return: UpdateVpdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_vpd_with_options_async(request, runtime)
