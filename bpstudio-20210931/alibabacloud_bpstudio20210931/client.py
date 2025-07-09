# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bpstudio20210931 import models as bpstudio_20210931_models
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
        self._endpoint = self.get_endpoint('bpstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def app_fail_back_with_options(
        self,
        request: bpstudio_20210931_models.AppFailBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.AppFailBackResponse:
        """
        @summary Switches a disaster recovery application back to the primary zone.
        
        @description You can call this operation to switch a disaster recovery application back to the primary zone.
        
        @param request: AppFailBackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppFailBackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppFailBack',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.AppFailBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def app_fail_back_with_options_async(
        self,
        request: bpstudio_20210931_models.AppFailBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.AppFailBackResponse:
        """
        @summary Switches a disaster recovery application back to the primary zone.
        
        @description You can call this operation to switch a disaster recovery application back to the primary zone.
        
        @param request: AppFailBackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppFailBackResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppFailBack',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.AppFailBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def app_fail_back(
        self,
        request: bpstudio_20210931_models.AppFailBackRequest,
    ) -> bpstudio_20210931_models.AppFailBackResponse:
        """
        @summary Switches a disaster recovery application back to the primary zone.
        
        @description You can call this operation to switch a disaster recovery application back to the primary zone.
        
        @param request: AppFailBackRequest
        @return: AppFailBackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.app_fail_back_with_options(request, runtime)

    async def app_fail_back_async(
        self,
        request: bpstudio_20210931_models.AppFailBackRequest,
    ) -> bpstudio_20210931_models.AppFailBackResponse:
        """
        @summary Switches a disaster recovery application back to the primary zone.
        
        @description You can call this operation to switch a disaster recovery application back to the primary zone.
        
        @param request: AppFailBackRequest
        @return: AppFailBackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.app_fail_back_with_options_async(request, runtime)

    def app_fail_over_with_options(
        self,
        request: bpstudio_20210931_models.AppFailOverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.AppFailOverResponse:
        """
        @summary Switches a disaster recovery application to another supported zone.
        
        @description You can call this operation to switch a disaster recovery application to another supported zone.
        
        @param request: AppFailOverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppFailOverResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.fail_zone):
            body['FailZone'] = request.fail_zone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppFailOver',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.AppFailOverResponse(),
            self.call_api(params, req, runtime)
        )

    async def app_fail_over_with_options_async(
        self,
        request: bpstudio_20210931_models.AppFailOverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.AppFailOverResponse:
        """
        @summary Switches a disaster recovery application to another supported zone.
        
        @description You can call this operation to switch a disaster recovery application to another supported zone.
        
        @param request: AppFailOverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AppFailOverResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.fail_zone):
            body['FailZone'] = request.fail_zone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AppFailOver',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.AppFailOverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def app_fail_over(
        self,
        request: bpstudio_20210931_models.AppFailOverRequest,
    ) -> bpstudio_20210931_models.AppFailOverResponse:
        """
        @summary Switches a disaster recovery application to another supported zone.
        
        @description You can call this operation to switch a disaster recovery application to another supported zone.
        
        @param request: AppFailOverRequest
        @return: AppFailOverResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.app_fail_over_with_options(request, runtime)

    async def app_fail_over_async(
        self,
        request: bpstudio_20210931_models.AppFailOverRequest,
    ) -> bpstudio_20210931_models.AppFailOverResponse:
        """
        @summary Switches a disaster recovery application to another supported zone.
        
        @description You can call this operation to switch a disaster recovery application to another supported zone.
        
        @param request: AppFailOverRequest
        @return: AppFailOverResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.app_fail_over_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an application or template belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an application or template belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an application or template belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: bpstudio_20210931_models.ChangeResourceGroupRequest,
    ) -> bpstudio_20210931_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an application or template belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        tmp_req: bpstudio_20210931_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        """
        @summary Creates an application based on an official template or private template in Cloud Architect Design Tool (CADT). Before you call this operation, make sure that you understand the billing methods and prices of Alibaba Cloud services to be used in the application.
        
        @param tmp_req: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        if not UtilClient.is_unset(tmp_req.process_variables):
            request.process_variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.process_variables, 'ProcessVariables', 'json')
        if not UtilClient.is_unset(tmp_req.variables):
            request.variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        body = {}
        if not UtilClient.is_unset(request.area_id):
            body['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        if not UtilClient.is_unset(request.instances_shrink):
            body['Instances'] = request.instances_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.process_variables_shrink):
            body['ProcessVariables'] = request.process_variables_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.variables_shrink):
            body['Variables'] = request.variables_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        """
        @summary Creates an application based on an official template or private template in Cloud Architect Design Tool (CADT). Before you call this operation, make sure that you understand the billing methods and prices of Alibaba Cloud services to be used in the application.
        
        @param tmp_req: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.CreateApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        if not UtilClient.is_unset(tmp_req.process_variables):
            request.process_variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.process_variables, 'ProcessVariables', 'json')
        if not UtilClient.is_unset(tmp_req.variables):
            request.variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        body = {}
        if not UtilClient.is_unset(request.area_id):
            body['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        if not UtilClient.is_unset(request.instances_shrink):
            body['Instances'] = request.instances_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.process_variables_shrink):
            body['ProcessVariables'] = request.process_variables_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.variables_shrink):
            body['Variables'] = request.variables_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: bpstudio_20210931_models.CreateApplicationRequest,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        """
        @summary Creates an application based on an official template or private template in Cloud Architect Design Tool (CADT). Before you call this operation, make sure that you understand the billing methods and prices of Alibaba Cloud services to be used in the application.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: bpstudio_20210931_models.CreateApplicationRequest,
    ) -> bpstudio_20210931_models.CreateApplicationResponse:
        """
        @summary Creates an application based on an official template or private template in Cloud Architect Design Tool (CADT). Before you call this operation, make sure that you understand the billing methods and prices of Alibaba Cloud services to be used in the application.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @description Before you call this operation to delete an application, make sure that the application is in the `Destroyed_Success` state. Otherwise, the application fails to be deleted.`` You can call the [GetApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-getapplication) operation to query the status of an application.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @description Before you call this operation to delete an application, make sure that the application is in the `Destroyed_Success` state. Otherwise, the application fails to be deleted.`` You can call the [GetApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-getapplication) operation to query the status of an application.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @description Before you call this operation to delete an application, make sure that the application is in the `Destroyed_Success` state. Otherwise, the application fails to be deleted.`` You can call the [GetApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-getapplication) operation to query the status of an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: bpstudio_20210931_models.DeleteApplicationRequest,
    ) -> bpstudio_20210931_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @description Before you call this operation to delete an application, make sure that the application is in the `Destroyed_Success` state. Otherwise, the application fails to be deleted.`` You can call the [GetApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-getapplication) operation to query the status of an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def deploy_application_with_options(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        """
        @summary Deploys an application after the payment.
        
        @param request: DeployApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        """
        @summary Deploys an application after the payment.
        
        @param request: DeployApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.DeployApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        """
        @summary Deploys an application after the payment.
        
        @param request: DeployApplicationRequest
        @return: DeployApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_application_with_options(request, runtime)

    async def deploy_application_async(
        self,
        request: bpstudio_20210931_models.DeployApplicationRequest,
    ) -> bpstudio_20210931_models.DeployApplicationResponse:
        """
        @summary Deploys an application after the payment.
        
        @param request: DeployApplicationRequest
        @return: DeployApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deploy_application_with_options_async(request, runtime)

    def execute_operation_async_with_options(
        self,
        tmp_req: bpstudio_20210931_models.ExecuteOperationASyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        """
        @summary Asynchronous execution of product operation functions.
        
        @param tmp_req: ExecuteOperationASyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteOperationASyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ExecuteOperationASyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteOperationASync',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ExecuteOperationASyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_operation_async_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.ExecuteOperationASyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        """
        @summary Asynchronous execution of product operation functions.
        
        @param tmp_req: ExecuteOperationASyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteOperationASyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ExecuteOperationASyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteOperationASync',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ExecuteOperationASyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_operation_async(
        self,
        request: bpstudio_20210931_models.ExecuteOperationASyncRequest,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        """
        @summary Asynchronous execution of product operation functions.
        
        @param request: ExecuteOperationASyncRequest
        @return: ExecuteOperationASyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_operation_async_with_options(request, runtime)

    async def execute_operation_async_async(
        self,
        request: bpstudio_20210931_models.ExecuteOperationASyncRequest,
    ) -> bpstudio_20210931_models.ExecuteOperationASyncResponse:
        """
        @summary Asynchronous execution of product operation functions.
        
        @param request: ExecuteOperationASyncRequest
        @return: ExecuteOperationASyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_operation_async_with_options_async(request, runtime)

    def execute_operation_sync_with_options(
        self,
        tmp_req: bpstudio_20210931_models.ExecuteOperationSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ExecuteOperationSyncResponse:
        """
        @summary 维护应用下资源API（同步操作）
        
        @param tmp_req: ExecuteOperationSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteOperationSyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ExecuteOperationSyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteOperationSync',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ExecuteOperationSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_operation_sync_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.ExecuteOperationSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ExecuteOperationSyncResponse:
        """
        @summary 维护应用下资源API（同步操作）
        
        @param tmp_req: ExecuteOperationSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteOperationSyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ExecuteOperationSyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attributes):
            request.attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attributes_shrink):
            body['Attributes'] = request.attributes_shrink
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteOperationSync',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ExecuteOperationSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_operation_sync(
        self,
        request: bpstudio_20210931_models.ExecuteOperationSyncRequest,
    ) -> bpstudio_20210931_models.ExecuteOperationSyncResponse:
        """
        @summary 维护应用下资源API（同步操作）
        
        @param request: ExecuteOperationSyncRequest
        @return: ExecuteOperationSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_operation_sync_with_options(request, runtime)

    async def execute_operation_sync_async(
        self,
        request: bpstudio_20210931_models.ExecuteOperationSyncRequest,
    ) -> bpstudio_20210931_models.ExecuteOperationSyncResponse:
        """
        @summary 维护应用下资源API（同步操作）
        
        @param request: ExecuteOperationSyncRequest
        @return: ExecuteOperationSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_operation_sync_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        """
        @summary The URL of the application topology image.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        """
        @summary The URL of the application topology image.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        """
        @summary The URL of the application topology image.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: bpstudio_20210931_models.GetApplicationRequest,
    ) -> bpstudio_20210931_models.GetApplicationResponse:
        """
        @summary The URL of the application topology image.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_application_variables_with_options(
        self,
        request: bpstudio_20210931_models.GetApplicationVariablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationVariablesResponse:
        """
        @summary 获取应用输入参数
        
        @param request: GetApplicationVariablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationVariablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplicationVariables',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationVariablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_variables_with_options_async(
        self,
        request: bpstudio_20210931_models.GetApplicationVariablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationVariablesResponse:
        """
        @summary 获取应用输入参数
        
        @param request: GetApplicationVariablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationVariablesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplicationVariables',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationVariablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_variables(
        self,
        request: bpstudio_20210931_models.GetApplicationVariablesRequest,
    ) -> bpstudio_20210931_models.GetApplicationVariablesResponse:
        """
        @summary 获取应用输入参数
        
        @param request: GetApplicationVariablesRequest
        @return: GetApplicationVariablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_variables_with_options(request, runtime)

    async def get_application_variables_async(
        self,
        request: bpstudio_20210931_models.GetApplicationVariablesRequest,
    ) -> bpstudio_20210931_models.GetApplicationVariablesResponse:
        """
        @summary 获取应用输入参数
        
        @param request: GetApplicationVariablesRequest
        @return: GetApplicationVariablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_variables_with_options_async(request, runtime)

    def get_application_variables_4fail_with_options(
        self,
        request: bpstudio_20210931_models.GetApplicationVariables4FailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationVariables4FailResponse:
        """
        @summary 获取需要重新配置的变量列表
        
        @param request: GetApplicationVariables4FailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationVariables4FailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationVariables4Fail',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationVariables4FailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_variables_4fail_with_options_async(
        self,
        request: bpstudio_20210931_models.GetApplicationVariables4FailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetApplicationVariables4FailResponse:
        """
        @summary 获取需要重新配置的变量列表
        
        @param request: GetApplicationVariables4FailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationVariables4FailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationVariables4Fail',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetApplicationVariables4FailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_variables_4fail(
        self,
        request: bpstudio_20210931_models.GetApplicationVariables4FailRequest,
    ) -> bpstudio_20210931_models.GetApplicationVariables4FailResponse:
        """
        @summary 获取需要重新配置的变量列表
        
        @param request: GetApplicationVariables4FailRequest
        @return: GetApplicationVariables4FailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_variables_4fail_with_options(request, runtime)

    async def get_application_variables_4fail_async(
        self,
        request: bpstudio_20210931_models.GetApplicationVariables4FailRequest,
    ) -> bpstudio_20210931_models.GetApplicationVariables4FailResponse:
        """
        @summary 获取需要重新配置的变量列表
        
        @param request: GetApplicationVariables4FailRequest
        @return: GetApplicationVariables4FailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_variables_4fail_with_options_async(request, runtime)

    def get_execute_operation_result_with_options(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        """
        @summary Asynchronously queries the result of an operation that is performed on a service instance.
        
        @param request: GetExecuteOperationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecuteOperationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation_id):
            body['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExecuteOperationResult',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetExecuteOperationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execute_operation_result_with_options_async(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        """
        @summary Asynchronously queries the result of an operation that is performed on a service instance.
        
        @param request: GetExecuteOperationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecuteOperationResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.operation_id):
            body['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetExecuteOperationResult',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetExecuteOperationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execute_operation_result(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        """
        @summary Asynchronously queries the result of an operation that is performed on a service instance.
        
        @param request: GetExecuteOperationResultRequest
        @return: GetExecuteOperationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_execute_operation_result_with_options(request, runtime)

    async def get_execute_operation_result_async(
        self,
        request: bpstudio_20210931_models.GetExecuteOperationResultRequest,
    ) -> bpstudio_20210931_models.GetExecuteOperationResultResponse:
        """
        @summary Asynchronously queries the result of an operation that is performed on a service instance.
        
        @param request: GetExecuteOperationResultRequest
        @return: GetExecuteOperationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_execute_operation_result_with_options_async(request, runtime)

    def get_fo_task_status_with_options(
        self,
        request: bpstudio_20210931_models.GetFoTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetFoTaskStatusResponse:
        """
        @summary Queries the status of a disaster recovery switchover task by task ID.
        
        @description You can call this operation to query the status of a disaster recovery switchover task by task ID.
        
        @param request: GetFoTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFoTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFoTaskStatus',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetFoTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fo_task_status_with_options_async(
        self,
        request: bpstudio_20210931_models.GetFoTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetFoTaskStatusResponse:
        """
        @summary Queries the status of a disaster recovery switchover task by task ID.
        
        @description You can call this operation to query the status of a disaster recovery switchover task by task ID.
        
        @param request: GetFoTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFoTaskStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFoTaskStatus',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetFoTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fo_task_status(
        self,
        request: bpstudio_20210931_models.GetFoTaskStatusRequest,
    ) -> bpstudio_20210931_models.GetFoTaskStatusResponse:
        """
        @summary Queries the status of a disaster recovery switchover task by task ID.
        
        @description You can call this operation to query the status of a disaster recovery switchover task by task ID.
        
        @param request: GetFoTaskStatusRequest
        @return: GetFoTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fo_task_status_with_options(request, runtime)

    async def get_fo_task_status_async(
        self,
        request: bpstudio_20210931_models.GetFoTaskStatusRequest,
    ) -> bpstudio_20210931_models.GetFoTaskStatusResponse:
        """
        @summary Queries the status of a disaster recovery switchover task by task ID.
        
        @description You can call this operation to query the status of a disaster recovery switchover task by task ID.
        
        @param request: GetFoTaskStatusRequest
        @return: GetFoTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fo_task_status_with_options_async(request, runtime)

    def get_potential_fail_zones_with_options(
        self,
        request: bpstudio_20210931_models.GetPotentialFailZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetPotentialFailZonesResponse:
        """
        @summary Queries the zones where the specified disaster recovery service can be switched.
        
        @description You can call this operation to query the zones where the specified disaster recovery service can be switched.
        
        @param request: GetPotentialFailZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPotentialFailZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_plan_id):
            body['IsPlanId'] = request.is_plan_id
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPotentialFailZones',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetPotentialFailZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_potential_fail_zones_with_options_async(
        self,
        request: bpstudio_20210931_models.GetPotentialFailZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetPotentialFailZonesResponse:
        """
        @summary Queries the zones where the specified disaster recovery service can be switched.
        
        @description You can call this operation to query the zones where the specified disaster recovery service can be switched.
        
        @param request: GetPotentialFailZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPotentialFailZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_plan_id):
            body['IsPlanId'] = request.is_plan_id
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPotentialFailZones',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetPotentialFailZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_potential_fail_zones(
        self,
        request: bpstudio_20210931_models.GetPotentialFailZonesRequest,
    ) -> bpstudio_20210931_models.GetPotentialFailZonesResponse:
        """
        @summary Queries the zones where the specified disaster recovery service can be switched.
        
        @description You can call this operation to query the zones where the specified disaster recovery service can be switched.
        
        @param request: GetPotentialFailZonesRequest
        @return: GetPotentialFailZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_potential_fail_zones_with_options(request, runtime)

    async def get_potential_fail_zones_async(
        self,
        request: bpstudio_20210931_models.GetPotentialFailZonesRequest,
    ) -> bpstudio_20210931_models.GetPotentialFailZonesResponse:
        """
        @summary Queries the zones where the specified disaster recovery service can be switched.
        
        @description You can call this operation to query the zones where the specified disaster recovery service can be switched.
        
        @param request: GetPotentialFailZonesRequest
        @return: GetPotentialFailZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_potential_fail_zones_with_options_async(request, runtime)

    def get_resource_4modify_record_with_options(
        self,
        request: bpstudio_20210931_models.GetResource4ModifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetResource4ModifyRecordResponse:
        """
        @summary 获取询价应用变配记录
        
        @param request: GetResource4ModifyRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResource4ModifyRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResource4ModifyRecord',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetResource4ModifyRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_4modify_record_with_options_async(
        self,
        request: bpstudio_20210931_models.GetResource4ModifyRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetResource4ModifyRecordResponse:
        """
        @summary 获取询价应用变配记录
        
        @param request: GetResource4ModifyRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResource4ModifyRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResource4ModifyRecord',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetResource4ModifyRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_4modify_record(
        self,
        request: bpstudio_20210931_models.GetResource4ModifyRecordRequest,
    ) -> bpstudio_20210931_models.GetResource4ModifyRecordResponse:
        """
        @summary 获取询价应用变配记录
        
        @param request: GetResource4ModifyRecordRequest
        @return: GetResource4ModifyRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_4modify_record_with_options(request, runtime)

    async def get_resource_4modify_record_async(
        self,
        request: bpstudio_20210931_models.GetResource4ModifyRecordRequest,
    ) -> bpstudio_20210931_models.GetResource4ModifyRecordResponse:
        """
        @summary 获取询价应用变配记录
        
        @param request: GetResource4ModifyRecordRequest
        @return: GetResource4ModifyRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_4modify_record_with_options_async(request, runtime)

    def get_result_4query_instance_price_4modify_with_options(
        self,
        request: bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyResponse:
        """
        @summary 获取询价结果
        
        @param request: GetResult4QueryInstancePrice4ModifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResult4QueryInstancePrice4ModifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResult4QueryInstancePrice4Modify',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_result_4query_instance_price_4modify_with_options_async(
        self,
        request: bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyResponse:
        """
        @summary 获取询价结果
        
        @param request: GetResult4QueryInstancePrice4ModifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResult4QueryInstancePrice4ModifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResult4QueryInstancePrice4Modify',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_result_4query_instance_price_4modify(
        self,
        request: bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyRequest,
    ) -> bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyResponse:
        """
        @summary 获取询价结果
        
        @param request: GetResult4QueryInstancePrice4ModifyRequest
        @return: GetResult4QueryInstancePrice4ModifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_result_4query_instance_price_4modify_with_options(request, runtime)

    async def get_result_4query_instance_price_4modify_async(
        self,
        request: bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyRequest,
    ) -> bpstudio_20210931_models.GetResult4QueryInstancePrice4ModifyResponse:
        """
        @summary 获取询价结果
        
        @param request: GetResult4QueryInstancePrice4ModifyRequest
        @return: GetResult4QueryInstancePrice4ModifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_result_4query_instance_price_4modify_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        """
        @summary Gets template images and information about architecture diagrams.
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        """
        @summary Gets template images and information about architecture diagrams.
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        """
        @summary Gets template images and information about architecture diagrams.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: bpstudio_20210931_models.GetTemplateRequest,
    ) -> bpstudio_20210931_models.GetTemplateResponse:
        """
        @summary Gets template images and information about architecture diagrams.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        """
        @deprecated OpenAPI GetToken is deprecated, please use BPStudio::2021-09-31::GetApplication instead.
        
        @summary Obtains a temporary token that is used to read the architecture diagram. The validity period of the token is 30 minutes.
        
        @description >Danger:  This API is no longer recommended, and the image related to the Application has included access authorization in the GetApplication property.
        
        @param request: GetTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        """
        @deprecated OpenAPI GetToken is deprecated, please use BPStudio::2021-09-31::GetApplication instead.
        
        @summary Obtains a temporary token that is used to read the architecture diagram. The validity period of the token is 30 minutes.
        
        @description >Danger:  This API is no longer recommended, and the image related to the Application has included access authorization in the GetApplication property.
        
        @param request: GetTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTokenResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetToken',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        """
        @deprecated OpenAPI GetToken is deprecated, please use BPStudio::2021-09-31::GetApplication instead.
        
        @summary Obtains a temporary token that is used to read the architecture diagram. The validity period of the token is 30 minutes.
        
        @description >Danger:  This API is no longer recommended, and the image related to the Application has included access authorization in the GetApplication property.
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: bpstudio_20210931_models.GetTokenRequest,
    ) -> bpstudio_20210931_models.GetTokenResponse:
        """
        @deprecated OpenAPI GetToken is deprecated, please use BPStudio::2021-09-31::GetApplication instead.
        
        @summary Obtains a temporary token that is used to read the architecture diagram. The validity period of the token is 30 minutes.
        
        @description >Danger:  This API is no longer recommended, and the image related to the Application has included access authorization in the GetApplication property.
        
        @param request: GetTokenRequest
        @return: GetTokenResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def init_app_fail_over_with_options(
        self,
        request: bpstudio_20210931_models.InitAppFailOverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.InitAppFailOverResponse:
        """
        @summary Prepares for application switchover and initiates a switchover task.
        
        @description You can call this operation to prepare for application switchover and initiate a switchover task.
        
        @param request: InitAppFailOverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitAppFailOverResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitAppFailOver',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.InitAppFailOverResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_app_fail_over_with_options_async(
        self,
        request: bpstudio_20210931_models.InitAppFailOverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.InitAppFailOverResponse:
        """
        @summary Prepares for application switchover and initiates a switchover task.
        
        @description You can call this operation to prepare for application switchover and initiate a switchover task.
        
        @param request: InitAppFailOverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitAppFailOverResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitAppFailOver',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.InitAppFailOverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_app_fail_over(
        self,
        request: bpstudio_20210931_models.InitAppFailOverRequest,
    ) -> bpstudio_20210931_models.InitAppFailOverResponse:
        """
        @summary Prepares for application switchover and initiates a switchover task.
        
        @description You can call this operation to prepare for application switchover and initiate a switchover task.
        
        @param request: InitAppFailOverRequest
        @return: InitAppFailOverResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_app_fail_over_with_options(request, runtime)

    async def init_app_fail_over_async(
        self,
        request: bpstudio_20210931_models.InitAppFailOverRequest,
    ) -> bpstudio_20210931_models.InitAppFailOverResponse:
        """
        @summary Prepares for application switchover and initiates a switchover task.
        
        @description You can call this operation to prepare for application switchover and initiate a switchover task.
        
        @param request: InitAppFailOverRequest
        @return: InitAppFailOverResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_app_fail_over_with_options_async(request, runtime)

    def list_application_with_options(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        """
        @summary This API provides a list of all applications under the current user. The optional keyword parameter defines the keywords contained in the application name.
        
        @param request: ListApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.show_hide):
            body['ShowHide'] = request.show_hide
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        """
        @summary This API provides a list of all applications under the current user. The optional keyword parameter defines the keywords contained in the application name.
        
        @param request: ListApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.show_hide):
            body['ShowHide'] = request.show_hide
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        """
        @summary This API provides a list of all applications under the current user. The optional keyword parameter defines the keywords contained in the application name.
        
        @param request: ListApplicationRequest
        @return: ListApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_with_options(request, runtime)

    async def list_application_async(
        self,
        request: bpstudio_20210931_models.ListApplicationRequest,
    ) -> bpstudio_20210931_models.ListApplicationResponse:
        """
        @summary This API provides a list of all applications under the current user. The optional keyword parameter defines the keywords contained in the application name.
        
        @param request: ListApplicationRequest
        @return: ListApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_with_options_async(request, runtime)

    def list_fo_created_apps_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListFoCreatedAppsResponse:
        """
        @summary Queries the information about all disaster recovery plans of the current account.
        
        @description Queries the information about all disaster recovery plans of the current account.
        
        @param request: ListFoCreatedAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFoCreatedAppsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListFoCreatedApps',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListFoCreatedAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fo_created_apps_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListFoCreatedAppsResponse:
        """
        @summary Queries the information about all disaster recovery plans of the current account.
        
        @description Queries the information about all disaster recovery plans of the current account.
        
        @param request: ListFoCreatedAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFoCreatedAppsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListFoCreatedApps',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListFoCreatedAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fo_created_apps(self) -> bpstudio_20210931_models.ListFoCreatedAppsResponse:
        """
        @summary Queries the information about all disaster recovery plans of the current account.
        
        @description Queries the information about all disaster recovery plans of the current account.
        
        @return: ListFoCreatedAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fo_created_apps_with_options(runtime)

    async def list_fo_created_apps_async(self) -> bpstudio_20210931_models.ListFoCreatedAppsResponse:
        """
        @summary Queries the information about all disaster recovery plans of the current account.
        
        @description Queries the information about all disaster recovery plans of the current account.
        
        @return: ListFoCreatedAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fo_created_apps_with_options_async(runtime)

    def list_tag_resources_with_options(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of one or more applications or templates.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of one or more applications or templates.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        body_flat = {}
        if not UtilClient.is_unset(request.resource_id):
            body_flat['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body_flat['Tag'] = request.tag
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of one or more applications or templates.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: bpstudio_20210931_models.ListTagResourcesRequest,
    ) -> bpstudio_20210931_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of one or more applications or templates.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_template_with_options(
        self,
        tmp_req: bpstudio_20210931_models.ListTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        """
        @summary Queries templates, including information such as the template name, architecture image URL, and URL of the serialized architecture image file.
        
        @param tmp_req: ListTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ListTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.tag_list):
            body['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.ListTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        """
        @summary Queries templates, including information such as the template name, architecture image URL, and URL of the serialized architecture image file.
        
        @param tmp_req: ListTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ListTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        body = {}
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_type):
            body['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.tag_list):
            body['TagList'] = request.tag_list
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ListTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        """
        @summary Queries templates, including information such as the template name, architecture image URL, and URL of the serialized architecture image file.
        
        @param request: ListTemplateRequest
        @return: ListTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_template_with_options(request, runtime)

    async def list_template_async(
        self,
        request: bpstudio_20210931_models.ListTemplateRequest,
    ) -> bpstudio_20210931_models.ListTemplateResponse:
        """
        @summary Queries templates, including information such as the template name, architecture image URL, and URL of the serialized architecture image file.
        
        @param request: ListTemplateRequest
        @return: ListTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_template_with_options_async(request, runtime)

    def modify_application_spec_with_options(
        self,
        tmp_req: bpstudio_20210931_models.ModifyApplicationSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ModifyApplicationSpecResponse:
        """
        @summary 提交应用变配
        
        @param tmp_req: ModifyApplicationSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApplicationSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ModifyApplicationSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_spec):
            request.instance_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_spec, 'InstanceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_spec_shrink):
            body['InstanceSpec'] = request.instance_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApplicationSpec',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ModifyApplicationSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_application_spec_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.ModifyApplicationSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ModifyApplicationSpecResponse:
        """
        @summary 提交应用变配
        
        @param tmp_req: ModifyApplicationSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApplicationSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ModifyApplicationSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_spec):
            request.instance_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_spec, 'InstanceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_spec_shrink):
            body['InstanceSpec'] = request.instance_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApplicationSpec',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ModifyApplicationSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_application_spec(
        self,
        request: bpstudio_20210931_models.ModifyApplicationSpecRequest,
    ) -> bpstudio_20210931_models.ModifyApplicationSpecResponse:
        """
        @summary 提交应用变配
        
        @param request: ModifyApplicationSpecRequest
        @return: ModifyApplicationSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_application_spec_with_options(request, runtime)

    async def modify_application_spec_async(
        self,
        request: bpstudio_20210931_models.ModifyApplicationSpecRequest,
    ) -> bpstudio_20210931_models.ModifyApplicationSpecResponse:
        """
        @summary 提交应用变配
        
        @param request: ModifyApplicationSpecRequest
        @return: ModifyApplicationSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_application_spec_with_options_async(request, runtime)

    def query_instance_price_4modify_with_options(
        self,
        tmp_req: bpstudio_20210931_models.QueryInstancePrice4ModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.QueryInstancePrice4ModifyResponse:
        """
        @summary 查询变配价格
        
        @param tmp_req: QueryInstancePrice4ModifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstancePrice4ModifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.QueryInstancePrice4ModifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInstancePrice4Modify',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.QueryInstancePrice4ModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_price_4modify_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.QueryInstancePrice4ModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.QueryInstancePrice4ModifyResponse:
        """
        @summary 查询变配价格
        
        @param tmp_req: QueryInstancePrice4ModifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstancePrice4ModifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.QueryInstancePrice4ModifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInstancePrice4Modify',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.QueryInstancePrice4ModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_price_4modify(
        self,
        request: bpstudio_20210931_models.QueryInstancePrice4ModifyRequest,
    ) -> bpstudio_20210931_models.QueryInstancePrice4ModifyResponse:
        """
        @summary 查询变配价格
        
        @param request: QueryInstancePrice4ModifyRequest
        @return: QueryInstancePrice4ModifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_instance_price_4modify_with_options(request, runtime)

    async def query_instance_price_4modify_async(
        self,
        request: bpstudio_20210931_models.QueryInstancePrice4ModifyRequest,
    ) -> bpstudio_20210931_models.QueryInstancePrice4ModifyResponse:
        """
        @summary 查询变配价格
        
        @param request: QueryInstancePrice4ModifyRequest
        @return: QueryInstancePrice4ModifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_price_4modify_with_options_async(request, runtime)

    def query_instance_spec_4modify_with_options(
        self,
        tmp_req: bpstudio_20210931_models.QueryInstanceSpec4ModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.QueryInstanceSpec4ModifyResponse:
        """
        @summary 查询变配规格列表
        
        @param tmp_req: QueryInstanceSpec4ModifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstanceSpec4ModifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.QueryInstanceSpec4ModifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.method_name):
            body['MethodName'] = request.method_name
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInstanceSpec4Modify',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.QueryInstanceSpec4ModifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_spec_4modify_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.QueryInstanceSpec4ModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.QueryInstanceSpec4ModifyResponse:
        """
        @summary 查询变配规格列表
        
        @param tmp_req: QueryInstanceSpec4ModifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstanceSpec4ModifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.QueryInstanceSpec4ModifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.method_name):
            body['MethodName'] = request.method_name
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInstanceSpec4Modify',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.QueryInstanceSpec4ModifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_spec_4modify(
        self,
        request: bpstudio_20210931_models.QueryInstanceSpec4ModifyRequest,
    ) -> bpstudio_20210931_models.QueryInstanceSpec4ModifyResponse:
        """
        @summary 查询变配规格列表
        
        @param request: QueryInstanceSpec4ModifyRequest
        @return: QueryInstanceSpec4ModifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_instance_spec_4modify_with_options(request, runtime)

    async def query_instance_spec_4modify_async(
        self,
        request: bpstudio_20210931_models.QueryInstanceSpec4ModifyRequest,
    ) -> bpstudio_20210931_models.QueryInstanceSpec4ModifyResponse:
        """
        @summary 查询变配规格列表
        
        @param request: QueryInstanceSpec4ModifyRequest
        @return: QueryInstanceSpec4ModifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_spec_4modify_with_options_async(request, runtime)

    def re_config_application_with_options(
        self,
        request: bpstudio_20210931_models.ReConfigApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReConfigApplicationResponse:
        """
        @summary 重新配置应用
        
        @param request: ReConfigApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReConfigApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.variables):
            body['Variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReConfigApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReConfigApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_config_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ReConfigApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReConfigApplicationResponse:
        """
        @summary 重新配置应用
        
        @param request: ReConfigApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReConfigApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.variables):
            body['Variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReConfigApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReConfigApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_config_application(
        self,
        request: bpstudio_20210931_models.ReConfigApplicationRequest,
    ) -> bpstudio_20210931_models.ReConfigApplicationResponse:
        """
        @summary 重新配置应用
        
        @param request: ReConfigApplicationRequest
        @return: ReConfigApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.re_config_application_with_options(request, runtime)

    async def re_config_application_async(
        self,
        request: bpstudio_20210931_models.ReConfigApplicationRequest,
    ) -> bpstudio_20210931_models.ReConfigApplicationResponse:
        """
        @summary 重新配置应用
        
        @param request: ReConfigApplicationRequest
        @return: ReConfigApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.re_config_application_with_options_async(request, runtime)

    def release_application_with_options(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        """
        @summary Releases the resources of an application.
        
        @param request: ReleaseApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReleaseApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        """
        @summary Releases the resources of an application.
        
        @param request: ReleaseApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ReleaseApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_application(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        """
        @summary Releases the resources of an application.
        
        @param request: ReleaseApplicationRequest
        @return: ReleaseApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_application_with_options(request, runtime)

    async def release_application_async(
        self,
        request: bpstudio_20210931_models.ReleaseApplicationRequest,
    ) -> bpstudio_20210931_models.ReleaseApplicationResponse:
        """
        @summary Releases the resources of an application.
        
        @param request: ReleaseApplicationRequest
        @return: ReleaseApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_application_with_options_async(request, runtime)

    def validate_application_with_options(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        """
        @summary Verifies the resources of an application. ValidateApplication is an asynchronous operation. You can call the GetApplication operation to query the verification result.
        
        @param request: ValidateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValidateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        """
        @summary Verifies the resources of an application. ValidateApplication is an asynchronous operation. You can call the GetApplication operation to query the verification result.
        
        @param request: ValidateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValidateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_application(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        """
        @summary Verifies the resources of an application. ValidateApplication is an asynchronous operation. You can call the GetApplication operation to query the verification result.
        
        @param request: ValidateApplicationRequest
        @return: ValidateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_application_with_options(request, runtime)

    async def validate_application_async(
        self,
        request: bpstudio_20210931_models.ValidateApplicationRequest,
    ) -> bpstudio_20210931_models.ValidateApplicationResponse:
        """
        @summary Verifies the resources of an application. ValidateApplication is an asynchronous operation. You can call the GetApplication operation to query the verification result.
        
        @param request: ValidateApplicationRequest
        @return: ValidateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_application_with_options_async(request, runtime)

    def valuate_application_with_options(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        """
        @summary Queries the prices of resources of an application. You can call the GetApplication operation to obtain the query results.
        
        @param request: ValuateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValuateApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValuateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def valuate_application_with_options_async(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        """
        @summary Queries the prices of resources of an application. You can call the GetApplication operation to obtain the query results.
        
        @param request: ValuateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValuateApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValuateApplication',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valuate_application(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        """
        @summary Queries the prices of resources of an application. You can call the GetApplication operation to obtain the query results.
        
        @param request: ValuateApplicationRequest
        @return: ValuateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.valuate_application_with_options(request, runtime)

    async def valuate_application_async(
        self,
        request: bpstudio_20210931_models.ValuateApplicationRequest,
    ) -> bpstudio_20210931_models.ValuateApplicationResponse:
        """
        @summary Queries the prices of resources of an application. You can call the GetApplication operation to obtain the query results.
        
        @param request: ValuateApplicationRequest
        @return: ValuateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.valuate_application_with_options_async(request, runtime)

    def valuate_template_with_options(
        self,
        tmp_req: bpstudio_20210931_models.ValuateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateTemplateResponse:
        """
        @summary Queries the price of a template.
        
        @param tmp_req: ValuateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValuateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ValuateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        if not UtilClient.is_unset(tmp_req.variables):
            request.variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        body = {}
        if not UtilClient.is_unset(request.area_id):
            body['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instances_shrink):
            body['Instances'] = request.instances_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.variables_shrink):
            body['Variables'] = request.variables_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValuateTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def valuate_template_with_options_async(
        self,
        tmp_req: bpstudio_20210931_models.ValuateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20210931_models.ValuateTemplateResponse:
        """
        @summary Queries the price of a template.
        
        @param tmp_req: ValuateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValuateTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bpstudio_20210931_models.ValuateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instances):
            request.instances_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instances, 'Instances', 'json')
        if not UtilClient.is_unset(tmp_req.variables):
            request.variables_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.variables, 'Variables', 'json')
        body = {}
        if not UtilClient.is_unset(request.area_id):
            body['AreaId'] = request.area_id
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instances_shrink):
            body['Instances'] = request.instances_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.variables_shrink):
            body['Variables'] = request.variables_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValuateTemplate',
            version='2021-09-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20210931_models.ValuateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def valuate_template(
        self,
        request: bpstudio_20210931_models.ValuateTemplateRequest,
    ) -> bpstudio_20210931_models.ValuateTemplateResponse:
        """
        @summary Queries the price of a template.
        
        @param request: ValuateTemplateRequest
        @return: ValuateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.valuate_template_with_options(request, runtime)

    async def valuate_template_async(
        self,
        request: bpstudio_20210931_models.ValuateTemplateRequest,
    ) -> bpstudio_20210931_models.ValuateTemplateResponse:
        """
        @summary Queries the price of a template.
        
        @param request: ValuateTemplateRequest
        @return: ValuateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.valuate_template_with_options_async(request, runtime)
