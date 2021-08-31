# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_computenestsupplier20210521 import models as compute_nest_supplier_20210521_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('computenestsupplier', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_service_registration_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse(),
            self.do_rpcrequest('CancelServiceRegistration', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_service_registration_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse(),
            await self.do_rpcrequest_async('CancelServiceRegistration', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_service_registration(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_service_registration_with_options(request, runtime)

    async def cancel_service_registration_async(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_service_registration_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceResponse(),
            self.do_rpcrequest('CreateService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceResponse(),
            await self.do_rpcrequest_async('CreateService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

    def delete_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceResponse(),
            self.do_rpcrequest('DeleteService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceResponse(),
            await self.do_rpcrequest_async('DeleteService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceResponse(),
            self.do_rpcrequest('GetService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceResponse(),
            await self.do_rpcrequest_async('GetService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    async def get_service_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_with_options_async(request, runtime)

    def get_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
            self.do_rpcrequest('GetServiceInstance', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
            await self.do_rpcrequest_async('GetServiceInstance', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    async def get_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_instance_with_options_async(request, runtime)

    def get_supplier_information_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetSupplierInformationResponse(),
            self.do_rpcrequest('GetSupplierInformation', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_supplier_information_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetSupplierInformationResponse(),
            await self.do_rpcrequest_async('GetSupplierInformation', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_supplier_information(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_supplier_information_with_options(request, runtime)

    async def get_supplier_information_async(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_supplier_information_with_options_async(request, runtime)

    def launch_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.LaunchServiceResponse(),
            self.do_rpcrequest('LaunchService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def launch_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.LaunchServiceResponse(),
            await self.do_rpcrequest_async('LaunchService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def launch_service(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.launch_service_with_options(request, runtime)

    async def launch_service_async(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.launch_service_with_options_async(request, runtime)

    def list_service_instances_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
            self.do_rpcrequest('ListServiceInstances', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
            await self.do_rpcrequest_async('ListServiceInstances', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_instances(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    async def list_service_instances_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instances_with_options_async(request, runtime)

    def list_service_registrations_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse(),
            self.do_rpcrequest('ListServiceRegistrations', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_service_registrations_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse(),
            await self.do_rpcrequest_async('ListServiceRegistrations', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_registrations(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_registrations_with_options(request, runtime)

    async def list_service_registrations_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_registrations_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServicesResponse(),
            self.do_rpcrequest('ListServices', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServicesResponse(),
            await self.do_rpcrequest_async('ListServices', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_services(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def register_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RegisterServiceResponse(),
            self.do_rpcrequest('RegisterService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RegisterServiceResponse(),
            await self.do_rpcrequest_async('RegisterService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_service(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_service_with_options(request, runtime)

    async def register_service_async(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_service_with_options_async(request, runtime)

    def update_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceResponse(),
            self.do_rpcrequest('UpdateService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceResponse(),
            await self.do_rpcrequest_async('UpdateService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_service(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_service_with_options(request, runtime)

    async def update_service_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_with_options_async(request, runtime)

    def withdraw_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.WithdrawServiceResponse(),
            self.do_rpcrequest('WithdrawService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def withdraw_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.WithdrawServiceResponse(),
            await self.do_rpcrequest_async('WithdrawService', '2021-05-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def withdraw_service(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.withdraw_service_with_options(request, runtime)

    async def withdraw_service_async(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_service_with_options_async(request, runtime)
