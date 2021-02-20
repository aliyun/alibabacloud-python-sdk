# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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

    def add_network_interface_to_instance_with_options(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AddNetworkInterfaceToInstanceResponse().from_map(
            self.do_rpcrequest('AddNetworkInterfaceToInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_network_interface_to_instance_with_options_async(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AddNetworkInterfaceToInstanceResponse().from_map(
            await self.do_rpcrequest_async('AddNetworkInterfaceToInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_network_interface_to_instance(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_network_interface_to_instance_with_options(request, runtime)

    async def add_network_interface_to_instance_async(
        self,
        request: ens_20171110_models.AddNetworkInterfaceToInstanceRequest,
    ) -> ens_20171110_models.AddNetworkInterfaceToInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_network_interface_to_instance_with_options_async(request, runtime)

    def allocate_eip_address_with_options(
        self,
        request: ens_20171110_models.AllocateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AllocateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AllocateEipAddressResponse().from_map(
            self.do_rpcrequest('AllocateEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_eip_address_with_options_async(
        self,
        request: ens_20171110_models.AllocateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AllocateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AllocateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocateEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_eip_address(
        self,
        request: ens_20171110_models.AllocateEipAddressRequest,
    ) -> ens_20171110_models.AllocateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_address_with_options(request, runtime)

    async def allocate_eip_address_async(
        self,
        request: ens_20171110_models.AllocateEipAddressRequest,
    ) -> ens_20171110_models.AllocateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_eip_address_with_options_async(request, runtime)

    def associate_eip_address_with_options(
        self,
        request: ens_20171110_models.AssociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AssociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AssociateEipAddressResponse().from_map(
            self.do_rpcrequest('AssociateEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_eip_address_with_options_async(
        self,
        request: ens_20171110_models.AssociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AssociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AssociateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('AssociateEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_eip_address(
        self,
        request: ens_20171110_models.AssociateEipAddressRequest,
    ) -> ens_20171110_models.AssociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_address_with_options(request, runtime)

    async def associate_eip_address_async(
        self,
        request: ens_20171110_models.AssociateEipAddressRequest,
    ) -> ens_20171110_models.AssociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_eip_address_with_options_async(request, runtime)

    def attach_ens_instances_with_options(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AttachEnsInstancesResponse().from_map(
            self.do_rpcrequest('AttachEnsInstances', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_ens_instances_with_options_async(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AttachEnsInstancesResponse().from_map(
            await self.do_rpcrequest_async('AttachEnsInstances', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_ens_instances(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_ens_instances_with_options(request, runtime)

    async def attach_ens_instances_async(
        self,
        request: ens_20171110_models.AttachEnsInstancesRequest,
    ) -> ens_20171110_models.AttachEnsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_ens_instances_with_options_async(request, runtime)

    def authorize_security_group_with_options(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AuthorizeSecurityGroupResponse().from_map(
            self.do_rpcrequest('AuthorizeSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def authorize_security_group_with_options_async(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AuthorizeSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('AuthorizeSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AuthorizeSecurityGroupEgressResponse().from_map(
            self.do_rpcrequest('AuthorizeSecurityGroupEgress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def authorize_security_group_egress_with_options_async(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.AuthorizeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.AuthorizeSecurityGroupEgressResponse().from_map(
            await self.do_rpcrequest_async('AuthorizeSecurityGroupEgress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def authorize_security_group_egress(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.AuthorizeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_egress_with_options(request, runtime)

    async def authorize_security_group_egress_async(
        self,
        request: ens_20171110_models.AuthorizeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.AuthorizeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_security_group_egress_with_options_async(request, runtime)

    def check_quota_with_options(
        self,
        request: ens_20171110_models.CheckQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CheckQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CheckQuotaResponse().from_map(
            self.do_rpcrequest('CheckQuota', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_quota_with_options_async(
        self,
        request: ens_20171110_models.CheckQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CheckQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CheckQuotaResponse().from_map(
            await self.do_rpcrequest_async('CheckQuota', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_quota(
        self,
        request: ens_20171110_models.CheckQuotaRequest,
    ) -> ens_20171110_models.CheckQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_quota_with_options(request, runtime)

    async def check_quota_async(
        self,
        request: ens_20171110_models.CheckQuotaRequest,
    ) -> ens_20171110_models.CheckQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_quota_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: ens_20171110_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateApplicationResponse().from_map(
            self.do_rpcrequest('CreateApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: ens_20171110_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateApplicationResponse().from_map(
            await self.do_rpcrequest_async('CreateApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_ens_service_with_options(
        self,
        request: ens_20171110_models.CreateEnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateEnsServiceResponse().from_map(
            self.do_rpcrequest('CreateEnsService', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ens_service_with_options_async(
        self,
        request: ens_20171110_models.CreateEnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEnsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateEnsServiceResponse().from_map(
            await self.do_rpcrequest_async('CreateEnsService', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_epinstance_with_options(
        self,
        request: ens_20171110_models.CreateEPInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEPInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateEPInstanceResponse().from_map(
            self.do_rpcrequest('CreateEPInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_epinstance_with_options_async(
        self,
        request: ens_20171110_models.CreateEPInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEPInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateEPInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateEPInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_epinstance(
        self,
        request: ens_20171110_models.CreateEPInstanceRequest,
    ) -> ens_20171110_models.CreateEPInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_epinstance_with_options(request, runtime)

    async def create_epinstance_async(
        self,
        request: ens_20171110_models.CreateEPInstanceRequest,
    ) -> ens_20171110_models.CreateEPInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_epinstance_with_options_async(request, runtime)

    def create_epn_instance_with_options(
        self,
        request: ens_20171110_models.CreateEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateEpnInstanceResponse().from_map(
            self.do_rpcrequest('CreateEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.CreateEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_image_with_options(
        self,
        request: ens_20171110_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateImageResponse().from_map(
            self.do_rpcrequest('CreateImage', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: ens_20171110_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateImageResponse().from_map(
            await self.do_rpcrequest_async('CreateImage', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_key_pair_with_options(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateKeyPairResponse().from_map(
            self.do_rpcrequest('CreateKeyPair', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_key_pair_with_options_async(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateKeyPairResponse().from_map(
            await self.do_rpcrequest_async('CreateKeyPair', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_key_pair(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    async def create_key_pair_async(
        self,
        request: ens_20171110_models.CreateKeyPairRequest,
    ) -> ens_20171110_models.CreateKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_key_pair_with_options_async(request, runtime)

    def create_security_group_with_options(
        self,
        request: ens_20171110_models.CreateSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateSecurityGroupResponse().from_map(
            self.do_rpcrequest('CreateSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_security_group_with_options_async(
        self,
        request: ens_20171110_models.CreateSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_vm_and_save_stock_with_options(
        self,
        request: ens_20171110_models.CreateVmAndSaveStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateVmAndSaveStockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateVmAndSaveStockResponse().from_map(
            self.do_rpcrequest('CreateVmAndSaveStock', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vm_and_save_stock_with_options_async(
        self,
        request: ens_20171110_models.CreateVmAndSaveStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateVmAndSaveStockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateVmAndSaveStockResponse().from_map(
            await self.do_rpcrequest_async('CreateVmAndSaveStock', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vm_and_save_stock(
        self,
        request: ens_20171110_models.CreateVmAndSaveStockRequest,
    ) -> ens_20171110_models.CreateVmAndSaveStockResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vm_and_save_stock_with_options(request, runtime)

    async def create_vm_and_save_stock_async(
        self,
        request: ens_20171110_models.CreateVmAndSaveStockRequest,
    ) -> ens_20171110_models.CreateVmAndSaveStockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vm_and_save_stock_with_options_async(request, runtime)

    def create_vswitch_with_options(
        self,
        request: ens_20171110_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateVSwitchResponse().from_map(
            self.do_rpcrequest('CreateVSwitch', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vswitch_with_options_async(
        self,
        request: ens_20171110_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.CreateVSwitchResponse().from_map(
            await self.do_rpcrequest_async('CreateVSwitch', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteApplicationResponse().from_map(
            self.do_rpcrequest('DeleteApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: ens_20171110_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteApplicationResponse().from_map(
            await self.do_rpcrequest_async('DeleteApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_epn_instance_with_options(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteEpnInstanceResponse().from_map(
            self.do_rpcrequest('DeleteEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_epn_instance(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_epn_instance_with_options(request, runtime)

    async def delete_epn_instance_async(
        self,
        request: ens_20171110_models.DeleteEpnInstanceRequest,
    ) -> ens_20171110_models.DeleteEpnInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_epn_instance_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteKeyPairsResponse().from_map(
            self.do_rpcrequest('DeleteKeyPairs', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteKeyPairsResponse().from_map(
            await self.do_rpcrequest_async('DeleteKeyPairs', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_key_pairs(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: ens_20171110_models.DeleteKeyPairsRequest,
    ) -> ens_20171110_models.DeleteKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def delete_security_group_with_options(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteSecurityGroupResponse().from_map(
            self.do_rpcrequest('DeleteSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_security_group_with_options_async(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_security_group(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    async def delete_security_group_async(
        self,
        request: ens_20171110_models.DeleteSecurityGroupRequest,
    ) -> ens_20171110_models.DeleteSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_group_with_options_async(request, runtime)

    def delete_vm_with_options(
        self,
        request: ens_20171110_models.DeleteVmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteVmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteVmResponse().from_map(
            self.do_rpcrequest('DeleteVm', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vm_with_options_async(
        self,
        request: ens_20171110_models.DeleteVmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteVmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteVmResponse().from_map(
            await self.do_rpcrequest_async('DeleteVm', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vm(
        self,
        request: ens_20171110_models.DeleteVmRequest,
    ) -> ens_20171110_models.DeleteVmResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vm_with_options(request, runtime)

    async def delete_vm_async(
        self,
        request: ens_20171110_models.DeleteVmRequest,
    ) -> ens_20171110_models.DeleteVmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vm_with_options_async(request, runtime)

    def delete_vswitch_with_options(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteVSwitchResponse().from_map(
            self.do_rpcrequest('DeleteVSwitch', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vswitch_with_options_async(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DeleteVSwitchResponse().from_map(
            await self.do_rpcrequest_async('DeleteVSwitch', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vswitch(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vswitch_with_options(request, runtime)

    async def delete_vswitch_async(
        self,
        request: ens_20171110_models.DeleteVSwitchRequest,
    ) -> ens_20171110_models.DeleteVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vswitch_with_options_async(request, runtime)

    def describe_application_with_options(
        self,
        request: ens_20171110_models.DescribeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeApplicationResponse().from_map(
            self.do_rpcrequest('DescribeApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_application_with_options_async(
        self,
        request: ens_20171110_models.DescribeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeApplicationResponse().from_map(
            await self.do_rpcrequest_async('DescribeApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeApplicationResourceSummaryResponse().from_map(
            self.do_rpcrequest('DescribeApplicationResourceSummary', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_application_resource_summary_with_options_async(
        self,
        request: ens_20171110_models.DescribeApplicationResourceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeApplicationResourceSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeApplicationResourceSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeApplicationResourceSummary', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: ens_20171110_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeAvailableResourceResponse().from_map(
            self.do_rpcrequest('DescribeAvailableResource', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: ens_20171110_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeAvailableResourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableResource', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(
        self,
        request: ens_20171110_models.DescribeAvailableResourceRequest,
    ) -> ens_20171110_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: ens_20171110_models.DescribeAvailableResourceRequest,
    ) -> ens_20171110_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_bandwitdh_by_internet_charge_type_with_options(
        self,
        request: ens_20171110_models.DescribeBandwitdhByInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse().from_map(
            self.do_rpcrequest('DescribeBandwitdhByInternetChargeType', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bandwitdh_by_internet_charge_type_with_options_async(
        self,
        request: ens_20171110_models.DescribeBandwitdhByInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeBandwitdhByInternetChargeType', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_band_withd_charge_type_with_options(
        self,
        request: ens_20171110_models.DescribeBandWithdChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeBandWithdChargeTypeResponse().from_map(
            self.do_rpcrequest('DescribeBandWithdChargeType', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_band_withd_charge_type_with_options_async(
        self,
        request: ens_20171110_models.DescribeBandWithdChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeBandWithdChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeBandWithdChargeType', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_band_withd_charge_type(
        self,
        request: ens_20171110_models.DescribeBandWithdChargeTypeRequest,
    ) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_band_withd_charge_type_with_options(request, runtime)

    async def describe_band_withd_charge_type_async(
        self,
        request: ens_20171110_models.DescribeBandWithdChargeTypeRequest,
    ) -> ens_20171110_models.DescribeBandWithdChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_band_withd_charge_type_with_options_async(request, runtime)

    def describe_create_pre_paid_instance_result_with_options(
        self,
        request: ens_20171110_models.DescribeCreatePrePaidInstanceResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse().from_map(
            self.do_rpcrequest('DescribeCreatePrePaidInstanceResult', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_create_pre_paid_instance_result_with_options_async(
        self,
        request: ens_20171110_models.DescribeCreatePrePaidInstanceResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeCreatePrePaidInstanceResult', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: ens_20171110_models.DescribeDataDistResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataDistResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeDataDistResultResponse().from_map(
            self.do_rpcrequest('DescribeDataDistResult', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_dist_result_with_options_async(
        self,
        request: ens_20171110_models.DescribeDataDistResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataDistResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeDataDistResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeDataDistResult', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_data_push_result_with_options(
        self,
        request: ens_20171110_models.DescribeDataPushResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataPushResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeDataPushResultResponse().from_map(
            self.do_rpcrequest('DescribeDataPushResult', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_push_result_with_options_async(
        self,
        request: ens_20171110_models.DescribeDataPushResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeDataPushResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeDataPushResultResponse().from_map(
            await self.do_rpcrequest_async('DescribeDataPushResult', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_eip_addresses_with_options(
        self,
        request: ens_20171110_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEipAddressesResponse().from_map(
            self.do_rpcrequest('DescribeEipAddresses', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eip_addresses_with_options_async(
        self,
        request: ens_20171110_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEipAddressesResponse().from_map(
            await self.do_rpcrequest_async('DescribeEipAddresses', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_ens_net_district_with_options(
        self,
        request: ens_20171110_models.DescribeEnsNetDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetDistrictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsNetDistrictResponse().from_map(
            self.do_rpcrequest('DescribeEnsNetDistrict', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ens_net_district_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsNetDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetDistrictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsNetDistrictResponse().from_map(
            await self.do_rpcrequest_async('DescribeEnsNetDistrict', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: ens_20171110_models.DescribeEnsNetLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsNetLevelResponse().from_map(
            self.do_rpcrequest('DescribeEnsNetLevel', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ens_net_level_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsNetLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsNetLevelResponse().from_map(
            await self.do_rpcrequest_async('DescribeEnsNetLevel', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ens_net_level(
        self,
        request: ens_20171110_models.DescribeEnsNetLevelRequest,
    ) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_net_level_with_options(request, runtime)

    async def describe_ens_net_level_async(
        self,
        request: ens_20171110_models.DescribeEnsNetLevelRequest,
    ) -> ens_20171110_models.DescribeEnsNetLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_net_level_with_options_async(request, runtime)

    def describe_ens_net_sale_district_with_options(
        self,
        request: ens_20171110_models.DescribeEnsNetSaleDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetSaleDistrictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsNetSaleDistrictResponse().from_map(
            self.do_rpcrequest('DescribeEnsNetSaleDistrict', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ens_net_sale_district_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsNetSaleDistrictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsNetSaleDistrictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsNetSaleDistrictResponse().from_map(
            await self.do_rpcrequest_async('DescribeEnsNetSaleDistrict', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse().from_map(
            self.do_rpcrequest('DescribeEnsRegionIdIpv6Info', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ens_region_id_ipv_6info_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdIpv6InfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeEnsRegionIdIpv6Info', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsRegionIdResourceResponse().from_map(
            self.do_rpcrequest('DescribeEnsRegionIdResource', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ens_region_id_resource_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionIdResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsRegionIdResourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeEnsRegionIdResource', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ens_region_id_resource(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdResourceRequest,
    ) -> ens_20171110_models.DescribeEnsRegionIdResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_region_id_resource_with_options(request, runtime)

    async def describe_ens_region_id_resource_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionIdResourceRequest,
    ) -> ens_20171110_models.DescribeEnsRegionIdResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ens_region_id_resource_with_options_async(request, runtime)

    def describe_ens_regions_with_options(
        self,
        request: ens_20171110_models.DescribeEnsRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsRegionsResponse().from_map(
            self.do_rpcrequest('DescribeEnsRegions', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ens_regions_with_options_async(
        self,
        request: ens_20171110_models.DescribeEnsRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEnsRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEnsRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeEnsRegions', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_epn_band_width_data_with_options(
        self,
        request: ens_20171110_models.DescribeEpnBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnBandWidthDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnBandWidthDataResponse().from_map(
            self.do_rpcrequest('DescribeEpnBandWidthData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_epn_band_width_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnBandWidthDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnBandWidthDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeEpnBandWidthData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse().from_map(
            self.do_rpcrequest('DescribeEpnBandwitdhByInternetChargeType', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_epn_bandwitdh_by_internet_charge_type_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeEpnBandwitdhByInternetChargeType', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnInstanceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeEpnInstanceAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_epn_instance_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeEpnInstanceAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_epn_instance_attribute(
        self,
        request: ens_20171110_models.DescribeEpnInstanceAttributeRequest,
    ) -> ens_20171110_models.DescribeEpnInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_instance_attribute_with_options(request, runtime)

    async def describe_epn_instance_attribute_async(
        self,
        request: ens_20171110_models.DescribeEpnInstanceAttributeRequest,
    ) -> ens_20171110_models.DescribeEpnInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_epn_instance_attribute_with_options_async(request, runtime)

    def describe_epn_instances_with_options(
        self,
        request: ens_20171110_models.DescribeEpnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnInstancesResponse().from_map(
            self.do_rpcrequest('DescribeEpnInstances', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_epn_instances_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeEpnInstances', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnMeasurementDataResponse().from_map(
            self.do_rpcrequest('DescribeEpnMeasurementData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_epn_measurement_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeEpnMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeEpnMeasurementDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeEpnMeasurementDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeEpnMeasurementData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeExportImageInfoResponse().from_map(
            self.do_rpcrequest('DescribeExportImageInfo', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_export_image_info_with_options_async(
        self,
        request: ens_20171110_models.DescribeExportImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeExportImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeExportImageInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeExportImageInfo', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_export_image_info(
        self,
        request: ens_20171110_models.DescribeExportImageInfoRequest,
    ) -> ens_20171110_models.DescribeExportImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_export_image_info_with_options(request, runtime)

    async def describe_export_image_info_async(
        self,
        request: ens_20171110_models.DescribeExportImageInfoRequest,
    ) -> ens_20171110_models.DescribeExportImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_export_image_info_with_options_async(request, runtime)

    def describe_export_image_status_with_options(
        self,
        request: ens_20171110_models.DescribeExportImageStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeExportImageStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeExportImageStatusResponse().from_map(
            self.do_rpcrequest('DescribeExportImageStatus', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_export_image_status_with_options_async(
        self,
        request: ens_20171110_models.DescribeExportImageStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeExportImageStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeExportImageStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeExportImageStatus', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_image_infos_with_options(
        self,
        request: ens_20171110_models.DescribeImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeImageInfosResponse().from_map(
            self.do_rpcrequest('DescribeImageInfos', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_infos_with_options_async(
        self,
        request: ens_20171110_models.DescribeImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeImageInfosResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageInfos', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_images_with_options(
        self,
        request: ens_20171110_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeImagesResponse().from_map(
            self.do_rpcrequest('DescribeImages', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_images_with_options_async(
        self,
        request: ens_20171110_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeImagesResponse().from_map(
            await self.do_rpcrequest_async('DescribeImages', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAutoRenewAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_auto_renew_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAutoRenewAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeInstanceMonitorData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_monitor_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceMonitorData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: ens_20171110_models.DescribeInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceSpecResponse().from_map(
            self.do_rpcrequest('DescribeInstanceSpec', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_spec_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceSpec', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_spec(
        self,
        request: ens_20171110_models.DescribeInstanceSpecRequest,
    ) -> ens_20171110_models.DescribeInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_spec_with_options(request, runtime)

    async def describe_instance_spec_async(
        self,
        request: ens_20171110_models.DescribeInstanceSpecRequest,
    ) -> ens_20171110_models.DescribeInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_spec_with_options_async(request, runtime)

    def describe_instance_types_with_options(
        self,
        request: ens_20171110_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceTypesResponse().from_map(
            self.do_rpcrequest('DescribeInstanceTypes', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_types_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceTypesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceTypes', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_types(
        self,
        request: ens_20171110_models.DescribeInstanceTypesRequest,
    ) -> ens_20171110_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    async def describe_instance_types_async(
        self,
        request: ens_20171110_models.DescribeInstanceTypesRequest,
    ) -> ens_20171110_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_types_with_options_async(request, runtime)

    def describe_instance_vnc_url_with_options(
        self,
        request: ens_20171110_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceVncUrlResponse().from_map(
            self.do_rpcrequest('DescribeInstanceVncUrl', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_vnc_url_with_options_async(
        self,
        request: ens_20171110_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeInstanceVncUrlResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceVncUrl', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_key_pairs_with_options(
        self,
        request: ens_20171110_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeKeyPairsResponse().from_map(
            self.do_rpcrequest('DescribeKeyPairs', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_key_pairs_with_options_async(
        self,
        request: ens_20171110_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeKeyPairsResponse().from_map(
            await self.do_rpcrequest_async('DescribeKeyPairs', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_measurement_data_with_options(
        self,
        request: ens_20171110_models.DescribeMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeMeasurementDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeMeasurementDataResponse().from_map(
            self.do_rpcrequest('DescribeMeasurementData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_measurement_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeMeasurementDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeMeasurementDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeMeasurementData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_network_interfaces_with_options(
        self,
        request: ens_20171110_models.DescribeNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeNetworkInterfacesResponse().from_map(
            self.do_rpcrequest('DescribeNetworkInterfaces', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_interfaces_with_options_async(
        self,
        request: ens_20171110_models.DescribeNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeNetworkInterfacesResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkInterfaces', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_pre_paid_instance_stock_with_options(
        self,
        request: ens_20171110_models.DescribePrePaidInstanceStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePrePaidInstanceStockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribePrePaidInstanceStockResponse().from_map(
            self.do_rpcrequest('DescribePrePaidInstanceStock', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pre_paid_instance_stock_with_options_async(
        self,
        request: ens_20171110_models.DescribePrePaidInstanceStockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePrePaidInstanceStockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribePrePaidInstanceStockResponse().from_map(
            await self.do_rpcrequest_async('DescribePrePaidInstanceStock', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: ens_20171110_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribePriceResponse().from_map(
            self.do_rpcrequest('DescribePrice', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: ens_20171110_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribePriceResponse().from_map(
            await self.do_rpcrequest_async('DescribePrice', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_security_group_attribute_with_options(
        self,
        request: ens_20171110_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeSecurityGroupAttributeResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroupAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_attribute_with_options_async(
        self,
        request: ens_20171110_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeSecurityGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroupAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeSecurityGroupsResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroups', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_groups_with_options_async(
        self,
        request: ens_20171110_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeSecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroups', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_servcie_schedule_with_options(
        self,
        request: ens_20171110_models.DescribeServcieScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeServcieScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeServcieScheduleResponse().from_map(
            self.do_rpcrequest('DescribeServcieSchedule', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_servcie_schedule_with_options_async(
        self,
        request: ens_20171110_models.DescribeServcieScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeServcieScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeServcieScheduleResponse().from_map(
            await self.do_rpcrequest_async('DescribeServcieSchedule', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_user_band_width_data_with_options(
        self,
        request: ens_20171110_models.DescribeUserBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeUserBandWidthDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeUserBandWidthDataResponse().from_map(
            self.do_rpcrequest('DescribeUserBandWidthData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_band_width_data_with_options_async(
        self,
        request: ens_20171110_models.DescribeUserBandWidthDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeUserBandWidthDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeUserBandWidthDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserBandWidthData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeVSwitchesResponse().from_map(
            self.do_rpcrequest('DescribeVSwitches', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: ens_20171110_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.DescribeVSwitchesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVSwitches', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def export_bill_detail_data_with_options(
        self,
        request: ens_20171110_models.ExportBillDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportBillDetailDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ExportBillDetailDataResponse().from_map(
            self.do_rpcrequest('ExportBillDetailData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_bill_detail_data_with_options_async(
        self,
        request: ens_20171110_models.ExportBillDetailDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportBillDetailDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ExportBillDetailDataResponse().from_map(
            await self.do_rpcrequest_async('ExportBillDetailData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ExportImageResponse().from_map(
            self.do_rpcrequest('ExportImage', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_image_with_options_async(
        self,
        request: ens_20171110_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ExportImageResponse().from_map(
            await self.do_rpcrequest_async('ExportImage', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ExportMeasurementDataResponse().from_map(
            self.do_rpcrequest('ExportMeasurementData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_measurement_data_with_options_async(
        self,
        request: ens_20171110_models.ExportMeasurementDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ExportMeasurementDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ExportMeasurementDataResponse().from_map(
            await self.do_rpcrequest_async('ExportMeasurementData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_vm_list_with_options(
        self,
        request: ens_20171110_models.GetVmListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetVmListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ens_20171110_models.GetVmListResponse().from_map(
            self.do_rpcrequest('GetVmList', '2017-11-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_vm_list_with_options_async(
        self,
        request: ens_20171110_models.GetVmListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.GetVmListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ens_20171110_models.GetVmListResponse().from_map(
            await self.do_rpcrequest_async('GetVmList', '2017-11-10', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_vm_list(
        self,
        request: ens_20171110_models.GetVmListRequest,
    ) -> ens_20171110_models.GetVmListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vm_list_with_options(request, runtime)

    async def get_vm_list_async(
        self,
        request: ens_20171110_models.GetVmListRequest,
    ) -> ens_20171110_models.GetVmListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_list_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ImportKeyPairResponse().from_map(
            self.do_rpcrequest('ImportKeyPair', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ImportKeyPairResponse().from_map(
            await self.do_rpcrequest_async('ImportKeyPair', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_key_pair(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: ens_20171110_models.ImportKeyPairRequest,
    ) -> ens_20171110_models.ImportKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def join_public_ips_to_epn_instance_with_options(
        self,
        request: ens_20171110_models.JoinPublicIpsToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinPublicIpsToEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.JoinPublicIpsToEpnInstanceResponse().from_map(
            self.do_rpcrequest('JoinPublicIpsToEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_public_ips_to_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.JoinPublicIpsToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinPublicIpsToEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.JoinPublicIpsToEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('JoinPublicIpsToEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.JoinSecurityGroupResponse().from_map(
            self.do_rpcrequest('JoinSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_security_group_with_options_async(
        self,
        request: ens_20171110_models.JoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.JoinSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('JoinSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_security_group(
        self,
        request: ens_20171110_models.JoinSecurityGroupRequest,
    ) -> ens_20171110_models.JoinSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_security_group_with_options(request, runtime)

    async def join_security_group_async(
        self,
        request: ens_20171110_models.JoinSecurityGroupRequest,
    ) -> ens_20171110_models.JoinSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_security_group_with_options_async(request, runtime)

    def join_vswitches_to_epn_instance_with_options(
        self,
        request: ens_20171110_models.JoinVSwitchesToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinVSwitchesToEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.JoinVSwitchesToEpnInstanceResponse().from_map(
            self.do_rpcrequest('JoinVSwitchesToEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_vswitches_to_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.JoinVSwitchesToEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.JoinVSwitchesToEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.JoinVSwitchesToEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('JoinVSwitchesToEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.LeaveSecurityGroupResponse().from_map(
            self.do_rpcrequest('LeaveSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def leave_security_group_with_options_async(
        self,
        request: ens_20171110_models.LeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.LeaveSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.LeaveSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('LeaveSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def leave_security_group(
        self,
        request: ens_20171110_models.LeaveSecurityGroupRequest,
    ) -> ens_20171110_models.LeaveSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.leave_security_group_with_options(request, runtime)

    async def leave_security_group_async(
        self,
        request: ens_20171110_models.LeaveSecurityGroupRequest,
    ) -> ens_20171110_models.LeaveSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.leave_security_group_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: ens_20171110_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ListApplicationsResponse().from_map(
            self.do_rpcrequest('ListApplications', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: ens_20171110_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ListApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ListApplicationsResponse().from_map(
            await self.do_rpcrequest_async('ListApplications', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def modify_epn_instance_with_options(
        self,
        request: ens_20171110_models.ModifyEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyEpnInstanceResponse().from_map(
            self.do_rpcrequest('ModifyEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.ModifyEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('ModifyEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def modify_image_attribute_with_options(
        self,
        request: ens_20171110_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyImageAttributeResponse().from_map(
            self.do_rpcrequest('ModifyImageAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyImageAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyImageSharePermissionResponse().from_map(
            self.do_rpcrequest('ModifyImageSharePermission', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_share_permission_with_options_async(
        self,
        request: ens_20171110_models.ModifyImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyImageSharePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyImageSharePermissionResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageSharePermission', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: ens_20171110_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ModifyInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: ens_20171110_models.ModifyInstanceAttributeRequest,
    ) -> ens_20171110_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: ens_20171110_models.ModifyInstanceAttributeRequest,
    ) -> ens_20171110_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def pre_create_ens_service_with_options(
        self,
        request: ens_20171110_models.PreCreateEnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PreCreateEnsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.PreCreateEnsServiceResponse().from_map(
            self.do_rpcrequest('PreCreateEnsService', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pre_create_ens_service_with_options_async(
        self,
        request: ens_20171110_models.PreCreateEnsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PreCreateEnsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.PreCreateEnsServiceResponse().from_map(
            await self.do_rpcrequest_async('PreCreateEnsService', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pre_create_ens_service(
        self,
        request: ens_20171110_models.PreCreateEnsServiceRequest,
    ) -> ens_20171110_models.PreCreateEnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.pre_create_ens_service_with_options(request, runtime)

    async def pre_create_ens_service_async(
        self,
        request: ens_20171110_models.PreCreateEnsServiceRequest,
    ) -> ens_20171110_models.PreCreateEnsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pre_create_ens_service_with_options_async(request, runtime)

    def push_application_data_with_options(
        self,
        request: ens_20171110_models.PushApplicationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PushApplicationDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.PushApplicationDataResponse().from_map(
            self.do_rpcrequest('PushApplicationData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_application_data_with_options_async(
        self,
        request: ens_20171110_models.PushApplicationDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.PushApplicationDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.PushApplicationDataResponse().from_map(
            await self.do_rpcrequest_async('PushApplicationData', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def reboot_instance_with_options(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RebootInstanceResponse().from_map(
            self.do_rpcrequest('RebootInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RebootInstanceResponse().from_map(
            await self.do_rpcrequest_async('RebootInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instance(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
    ) -> ens_20171110_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    async def reboot_instance_async(
        self,
        request: ens_20171110_models.RebootInstanceRequest,
    ) -> ens_20171110_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instance_with_options_async(request, runtime)

    def re_init_disk_with_options(
        self,
        request: ens_20171110_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReInitDiskResponse().from_map(
            self.do_rpcrequest('ReInitDisk', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def re_init_disk_with_options_async(
        self,
        request: ens_20171110_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReInitDiskResponse().from_map(
            await self.do_rpcrequest_async('ReInitDisk', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def release_eip_address_with_options(
        self,
        request: ens_20171110_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReleaseEipAddressResponse().from_map(
            self.do_rpcrequest('ReleaseEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_eip_address_with_options_async(
        self,
        request: ens_20171110_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReleaseEipAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleaseEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_eip_address(
        self,
        request: ens_20171110_models.ReleaseEipAddressRequest,
    ) -> ens_20171110_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_eip_address_with_options(request, runtime)

    async def release_eip_address_async(
        self,
        request: ens_20171110_models.ReleaseEipAddressRequest,
    ) -> ens_20171110_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_eip_address_with_options_async(request, runtime)

    def release_post_paid_instance_with_options(
        self,
        request: ens_20171110_models.ReleasePostPaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleasePostPaidInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReleasePostPaidInstanceResponse().from_map(
            self.do_rpcrequest('ReleasePostPaidInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_post_paid_instance_with_options_async(
        self,
        request: ens_20171110_models.ReleasePostPaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleasePostPaidInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReleasePostPaidInstanceResponse().from_map(
            await self.do_rpcrequest_async('ReleasePostPaidInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReleasePrePaidInstanceResponse().from_map(
            self.do_rpcrequest('ReleasePrePaidInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_pre_paid_instance_with_options_async(
        self,
        request: ens_20171110_models.ReleasePrePaidInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.ReleasePrePaidInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.ReleasePrePaidInstanceResponse().from_map(
            await self.do_rpcrequest_async('ReleasePrePaidInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def remove_public_ips_from_epn_instance_with_options(
        self,
        request: ens_20171110_models.RemovePublicIpsFromEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse().from_map(
            self.do_rpcrequest('RemovePublicIpsFromEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_public_ips_from_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.RemovePublicIpsFromEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('RemovePublicIpsFromEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse().from_map(
            self.do_rpcrequest('RemoveVSwitchesFromEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_vswitches_from_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.RemoveVSwitchesFromEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('RemoveVSwitchesFromEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def rescale_application_with_options(
        self,
        request: ens_20171110_models.RescaleApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RescaleApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RescaleApplicationResponse().from_map(
            self.do_rpcrequest('RescaleApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rescale_application_with_options_async(
        self,
        request: ens_20171110_models.RescaleApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RescaleApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RescaleApplicationResponse().from_map(
            await self.do_rpcrequest_async('RescaleApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def revoke_security_group_with_options(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RevokeSecurityGroupResponse().from_map(
            self.do_rpcrequest('RevokeSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_security_group_with_options_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RevokeSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('RevokeSecurityGroup', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_security_group(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_with_options(request, runtime)

    async def revoke_security_group_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_with_options_async(request, runtime)

    def revoke_security_group_egress_with_options(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RevokeSecurityGroupEgressResponse().from_map(
            self.do_rpcrequest('RevokeSecurityGroupEgress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_security_group_egress_with_options_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RevokeSecurityGroupEgressResponse().from_map(
            await self.do_rpcrequest_async('RevokeSecurityGroupEgress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_security_group_egress(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_egress_with_options(request, runtime)

    async def revoke_security_group_egress_async(
        self,
        request: ens_20171110_models.RevokeSecurityGroupEgressRequest,
    ) -> ens_20171110_models.RevokeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_egress_with_options_async(request, runtime)

    def rollback_application_with_options(
        self,
        request: ens_20171110_models.RollbackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RollbackApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RollbackApplicationResponse().from_map(
            self.do_rpcrequest('RollbackApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_application_with_options_async(
        self,
        request: ens_20171110_models.RollbackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RollbackApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RollbackApplicationResponse().from_map(
            await self.do_rpcrequest_async('RollbackApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def run_service_schedule_with_options(
        self,
        request: ens_20171110_models.RunServiceScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RunServiceScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RunServiceScheduleResponse().from_map(
            self.do_rpcrequest('RunServiceSchedule', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_service_schedule_with_options_async(
        self,
        request: ens_20171110_models.RunServiceScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.RunServiceScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.RunServiceScheduleResponse().from_map(
            await self.do_rpcrequest_async('RunServiceSchedule', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def schedule_pod_with_options(
        self,
        request: ens_20171110_models.SchedulePodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SchedulePodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.SchedulePodResponse().from_map(
            self.do_rpcrequest('SchedulePod', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def schedule_pod_with_options_async(
        self,
        request: ens_20171110_models.SchedulePodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.SchedulePodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.SchedulePodResponse().from_map(
            await self.do_rpcrequest_async('SchedulePod', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def schedule_pod(
        self,
        request: ens_20171110_models.SchedulePodRequest,
    ) -> ens_20171110_models.SchedulePodResponse:
        runtime = util_models.RuntimeOptions()
        return self.schedule_pod_with_options(request, runtime)

    async def schedule_pod_async(
        self,
        request: ens_20171110_models.SchedulePodRequest,
    ) -> ens_20171110_models.SchedulePodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.schedule_pod_with_options_async(request, runtime)

    def start_epn_instance_with_options(
        self,
        request: ens_20171110_models.StartEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StartEpnInstanceResponse().from_map(
            self.do_rpcrequest('StartEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.StartEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StartEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('StartEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StartInstanceResponse().from_map(
            self.do_rpcrequest('StartInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: ens_20171110_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StartInstanceResponse().from_map(
            await self.do_rpcrequest_async('StartInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: ens_20171110_models.StartInstanceRequest,
    ) -> ens_20171110_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: ens_20171110_models.StartInstanceRequest,
    ) -> ens_20171110_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_epn_instance_with_options(
        self,
        request: ens_20171110_models.StopEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StopEpnInstanceResponse().from_map(
            self.do_rpcrequest('StopEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_epn_instance_with_options_async(
        self,
        request: ens_20171110_models.StopEpnInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopEpnInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StopEpnInstanceResponse().from_map(
            await self.do_rpcrequest_async('StopEpnInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StopInstanceResponse().from_map(
            self.do_rpcrequest('StopInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: ens_20171110_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.StopInstanceResponse().from_map(
            await self.do_rpcrequest_async('StopInstance', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(
        self,
        request: ens_20171110_models.StopInstanceRequest,
    ) -> ens_20171110_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: ens_20171110_models.StopInstanceRequest,
    ) -> ens_20171110_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def unassociate_eip_address_with_options(
        self,
        request: ens_20171110_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.UnassociateEipAddressResponse().from_map(
            self.do_rpcrequest('UnassociateEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_eip_address_with_options_async(
        self,
        request: ens_20171110_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.UnassociateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('UnassociateEipAddress', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_eip_address(
        self,
        request: ens_20171110_models.UnassociateEipAddressRequest,
    ) -> ens_20171110_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_eip_address_with_options(request, runtime)

    async def unassociate_eip_address_async(
        self,
        request: ens_20171110_models.UnassociateEipAddressRequest,
    ) -> ens_20171110_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_eip_address_with_options_async(request, runtime)

    def upgrade_application_with_options(
        self,
        request: ens_20171110_models.UpgradeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpgradeApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.UpgradeApplicationResponse().from_map(
            self.do_rpcrequest('UpgradeApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_application_with_options_async(
        self,
        request: ens_20171110_models.UpgradeApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ens_20171110_models.UpgradeApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ens_20171110_models.UpgradeApplicationResponse().from_map(
            await self.do_rpcrequest_async('UpgradeApplication', '2017-11-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
