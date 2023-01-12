# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cmn20200825 import models as cmn_20200825_models
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
        self._endpoint = self.get_endpoint('cmn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_ipwith_options(
        self,
        tmp_req: cmn_20200825_models.ApplyIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ApplyIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ApplyIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_type_id):
            query['BusinessTypeId'] = request.business_type_id
        if not UtilClient.is_unset(request.business_type_params):
            query['BusinessTypeParams'] = request.business_type_params
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            query['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.loopback_port):
            query['LoopbackPort'] = request.loopback_port
        if not UtilClient.is_unset(request.net_location):
            query['NetLocation'] = request.net_location
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyIP',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ApplyIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ipwith_options_async(
        self,
        tmp_req: cmn_20200825_models.ApplyIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ApplyIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ApplyIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.business_type_id):
            query['BusinessTypeId'] = request.business_type_id
        if not UtilClient.is_unset(request.business_type_params):
            query['BusinessTypeParams'] = request.business_type_params
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            query['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.loopback_port):
            query['LoopbackPort'] = request.loopback_port
        if not UtilClient.is_unset(request.net_location):
            query['NetLocation'] = request.net_location
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyIP',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ApplyIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ip(
        self,
        request: cmn_20200825_models.ApplyIPRequest,
    ) -> cmn_20200825_models.ApplyIPResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_ipwith_options(request, runtime)

    async def apply_ip_async(
        self,
        request: cmn_20200825_models.ApplyIPRequest,
    ) -> cmn_20200825_models.ApplyIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_ipwith_options_async(request, runtime)

    def auto_duty_with_options(
        self,
        request: cmn_20200825_models.AutoDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.AutoDutyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duty_batch):
            body['DutyBatch'] = request.duty_batch
        if not UtilClient.is_unset(request.duty_name):
            body['DutyName'] = request.duty_name
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AutoDuty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.AutoDutyResponse(),
            self.call_api(params, req, runtime)
        )

    async def auto_duty_with_options_async(
        self,
        request: cmn_20200825_models.AutoDutyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.AutoDutyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duty_batch):
            body['DutyBatch'] = request.duty_batch
        if not UtilClient.is_unset(request.duty_name):
            body['DutyName'] = request.duty_name
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AutoDuty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.AutoDutyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def auto_duty(
        self,
        request: cmn_20200825_models.AutoDutyRequest,
    ) -> cmn_20200825_models.AutoDutyResponse:
        runtime = util_models.RuntimeOptions()
        return self.auto_duty_with_options(request, runtime)

    async def auto_duty_async(
        self,
        request: cmn_20200825_models.AutoDutyRequest,
    ) -> cmn_20200825_models.AutoDutyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.auto_duty_with_options_async(request, runtime)

    def close_event_with_options(
        self,
        request: cmn_20200825_models.CloseEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CloseEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_object_id):
            body['EventObjectId'] = request.event_object_id
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseEvent',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CloseEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_event_with_options_async(
        self,
        request: cmn_20200825_models.CloseEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CloseEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_object_id):
            body['EventObjectId'] = request.event_object_id
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseEvent',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CloseEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_event(
        self,
        request: cmn_20200825_models.CloseEventRequest,
    ) -> cmn_20200825_models.CloseEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_event_with_options(request, runtime)

    async def close_event_async(
        self,
        request: cmn_20200825_models.CloseEventRequest,
    ) -> cmn_20200825_models.CloseEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_event_with_options_async(request, runtime)

    def create_configuration_specification_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param tmp_req: CreateConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.related_variate_shrink):
            body['RelatedVariate'] = request.related_variate_shrink
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.specification_content):
            body['SpecificationContent'] = request.specification_content
        if not UtilClient.is_unset(request.specification_name):
            body['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_configuration_specification_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param tmp_req: CreateConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.related_variate_shrink):
            body['RelatedVariate'] = request.related_variate_shrink
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.specification_content):
            body['SpecificationContent'] = request.specification_content
        if not UtilClient.is_unset(request.specification_name):
            body['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_configuration_specification(
        self,
        request: cmn_20200825_models.CreateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: CreateConfigurationSpecificationRequest
        @return: CreateConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_configuration_specification_with_options(request, runtime)

    async def create_configuration_specification_async(
        self,
        request: cmn_20200825_models.CreateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.CreateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: CreateConfigurationSpecificationRequest
        @return: CreateConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_configuration_specification_with_options_async(request, runtime)

    def create_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.format_function):
            body['FormatFunction'] = request.format_function
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.variate_name):
            body['VariateName'] = request.variate_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.format_function):
            body['FormatFunction'] = request.format_function
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.variate_name):
            body['VariateName'] = request.variate_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateConfigurationVariateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_configuration_variate(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_configuration_variate_with_options(request, runtime)

    async def create_configuration_variate_async(
        self,
        request: cmn_20200825_models.CreateConfigurationVariateRequest,
    ) -> cmn_20200825_models.CreateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_configuration_variate_with_options_async(request, runtime)

    def create_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.contact):
            body['Contact'] = request.contact
        if not UtilClient.is_unset(request.dedicated_line_gateway):
            body['DedicatedLineGateway'] = request.dedicated_line_gateway
        if not UtilClient.is_unset(request.dedicated_line_ip):
            body['DedicatedLineIp'] = request.dedicated_line_ip
        if not UtilClient.is_unset(request.dedicated_line_role):
            body['DedicatedLineRole'] = request.dedicated_line_role
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_port):
            body['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.expiration_date):
            body['ExpirationDate'] = request.expiration_date
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.isp):
            body['Isp'] = request.isp
        if not UtilClient.is_unset(request.isp_form_id):
            body['IspFormId'] = request.isp_form_id
        if not UtilClient.is_unset(request.isp_id):
            body['IspId'] = request.isp_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.online_date):
            body['OnlineDate'] = request.online_date
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.contact):
            body['Contact'] = request.contact
        if not UtilClient.is_unset(request.dedicated_line_gateway):
            body['DedicatedLineGateway'] = request.dedicated_line_gateway
        if not UtilClient.is_unset(request.dedicated_line_ip):
            body['DedicatedLineIp'] = request.dedicated_line_ip
        if not UtilClient.is_unset(request.dedicated_line_role):
            body['DedicatedLineRole'] = request.dedicated_line_role
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_port):
            body['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.expiration_date):
            body['ExpirationDate'] = request.expiration_date
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.isp):
            body['Isp'] = request.isp
        if not UtilClient.is_unset(request.isp_form_id):
            body['IspFormId'] = request.isp_form_id
        if not UtilClient.is_unset(request.isp_id):
            body['IspId'] = request.isp_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.online_date):
            body['OnlineDate'] = request.online_date
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDedicatedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dedicated_line(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_line_with_options(request, runtime)

    async def create_dedicated_line_async(
        self,
        request: cmn_20200825_models.CreateDedicatedLineRequest,
    ) -> cmn_20200825_models.CreateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_line_with_options_async(request, runtime)

    def create_device_with_options(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name):
            body['HostName'] = request.host_name
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_with_options_async(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name):
            body['HostName'] = request.host_name
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    async def create_device_async(
        self,
        request: cmn_20200825_models.CreateDeviceRequest,
    ) -> cmn_20200825_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_with_options_async(request, runtime)

    def create_device_form_with_options(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.account_config):
            body['AccountConfig'] = request.account_config
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_compare):
            body['ConfigCompare'] = request.config_compare
        if not UtilClient.is_unset(request.detail_display):
            body['DetailDisplay'] = request.detail_display
        if not UtilClient.is_unset(request.device_form_name):
            body['DeviceFormName'] = request.device_form_name
        if not UtilClient.is_unset(request.related_device_form_id):
            body['RelatedDeviceFormId'] = request.related_device_form_id
        if not UtilClient.is_unset(request.resource_use):
            body['ResourceUse'] = request.resource_use
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        if not UtilClient.is_unset(request.unique_key):
            body['UniqueKey'] = request.unique_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_form_with_options_async(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.account_config):
            body['AccountConfig'] = request.account_config
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_compare):
            body['ConfigCompare'] = request.config_compare
        if not UtilClient.is_unset(request.detail_display):
            body['DetailDisplay'] = request.detail_display
        if not UtilClient.is_unset(request.device_form_name):
            body['DeviceFormName'] = request.device_form_name
        if not UtilClient.is_unset(request.related_device_form_id):
            body['RelatedDeviceFormId'] = request.related_device_form_id
        if not UtilClient.is_unset(request.resource_use):
            body['ResourceUse'] = request.resource_use
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        if not UtilClient.is_unset(request.unique_key):
            body['UniqueKey'] = request.unique_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDeviceFormResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device_form(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_form_with_options(request, runtime)

    async def create_device_form_async(
        self,
        request: cmn_20200825_models.CreateDeviceFormRequest,
    ) -> cmn_20200825_models.CreateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_form_with_options_async(request, runtime)

    def create_device_property_with_options(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.property_content):
            body['PropertyContent'] = request.property_content
        if not UtilClient.is_unset(request.property_format):
            body['PropertyFormat'] = request.property_format
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_property_with_options_async(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.property_content):
            body['PropertyContent'] = request.property_content
        if not UtilClient.is_unset(request.property_format):
            body['PropertyFormat'] = request.property_format
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device_property(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_property_with_options(request, runtime)

    async def create_device_property_async(
        self,
        request: cmn_20200825_models.CreateDevicePropertyRequest,
    ) -> cmn_20200825_models.CreateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_property_with_options_async(request, runtime)

    def create_devices_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_param_model_list):
            request.device_param_model_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_param_model_list, 'DeviceParamModelList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.device_param_model_list_shrink):
            body['DeviceParamModelList'] = request.device_param_model_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_devices_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_param_model_list):
            request.device_param_model_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_param_model_list, 'DeviceParamModelList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.device_param_model_list_shrink):
            body['DeviceParamModelList'] = request.device_param_model_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_devices(
        self,
        request: cmn_20200825_models.CreateDevicesRequest,
    ) -> cmn_20200825_models.CreateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_devices_with_options(request, runtime)

    async def create_devices_async(
        self,
        request: cmn_20200825_models.CreateDevicesRequest,
    ) -> cmn_20200825_models.CreateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_devices_with_options_async(request, runtime)

    def create_event_definition_with_options(
        self,
        request: cmn_20200825_models.CreateEventDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateEventDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateEventDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_definition_with_options_async(
        self,
        request: cmn_20200825_models.CreateEventDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateEventDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateEventDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_definition(
        self,
        request: cmn_20200825_models.CreateEventDefinitionRequest,
    ) -> cmn_20200825_models.CreateEventDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_event_definition_with_options(request, runtime)

    async def create_event_definition_async(
        self,
        request: cmn_20200825_models.CreateEventDefinitionRequest,
    ) -> cmn_20200825_models.CreateEventDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_event_definition_with_options_async(request, runtime)

    def create_link_job_with_options(
        self,
        request: cmn_20200825_models.CreateLinkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateLinkJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.auto_confirm):
            body['AutoConfirm'] = request.auto_confirm
        if not UtilClient.is_unset(request.double_convert_strategy):
            body['DoubleConvertStrategy'] = request.double_convert_strategy
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.single_strategy):
            body['SingleStrategy'] = request.single_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLinkJob',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateLinkJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_link_job_with_options_async(
        self,
        request: cmn_20200825_models.CreateLinkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateLinkJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.auto_confirm):
            body['AutoConfirm'] = request.auto_confirm
        if not UtilClient.is_unset(request.double_convert_strategy):
            body['DoubleConvertStrategy'] = request.double_convert_strategy
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.single_strategy):
            body['SingleStrategy'] = request.single_strategy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLinkJob',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateLinkJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_link_job(
        self,
        request: cmn_20200825_models.CreateLinkJobRequest,
    ) -> cmn_20200825_models.CreateLinkJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_link_job_with_options(request, runtime)

    async def create_link_job_async(
        self,
        request: cmn_20200825_models.CreateLinkJobRequest,
    ) -> cmn_20200825_models.CreateLinkJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_link_job_with_options_async(request, runtime)

    def create_monitor_item_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateMonitorItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateMonitorItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_rule_list):
            request.alarm_rule_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_rule_list, 'AlarmRuleList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.alarm_rule_list_shrink):
            body['AlarmRuleList'] = request.alarm_rule_list_shrink
        if not UtilClient.is_unset(request.analysis_code):
            body['AnalysisCode'] = request.analysis_code
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.collection_type):
            body['CollectionType'] = request.collection_type
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.data_item):
            body['DataItem'] = request.data_item
        if not UtilClient.is_unset(request.device_form):
            body['DeviceForm'] = request.device_form
        if not UtilClient.is_unset(request.effective):
            body['Effective'] = request.effective
        if not UtilClient.is_unset(request.exec_interval):
            body['ExecInterval'] = request.exec_interval
        if not UtilClient.is_unset(request.monitor_item_description):
            body['MonitorItemDescription'] = request.monitor_item_description
        if not UtilClient.is_unset(request.monitor_item_name):
            body['MonitorItemName'] = request.monitor_item_name
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMonitorItem',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateMonitorItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_item_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateMonitorItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateMonitorItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_rule_list):
            request.alarm_rule_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_rule_list, 'AlarmRuleList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.alarm_rule_list_shrink):
            body['AlarmRuleList'] = request.alarm_rule_list_shrink
        if not UtilClient.is_unset(request.analysis_code):
            body['AnalysisCode'] = request.analysis_code
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.collection_type):
            body['CollectionType'] = request.collection_type
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.data_item):
            body['DataItem'] = request.data_item
        if not UtilClient.is_unset(request.device_form):
            body['DeviceForm'] = request.device_form
        if not UtilClient.is_unset(request.effective):
            body['Effective'] = request.effective
        if not UtilClient.is_unset(request.exec_interval):
            body['ExecInterval'] = request.exec_interval
        if not UtilClient.is_unset(request.monitor_item_description):
            body['MonitorItemDescription'] = request.monitor_item_description
        if not UtilClient.is_unset(request.monitor_item_name):
            body['MonitorItemName'] = request.monitor_item_name
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMonitorItem',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateMonitorItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_item(
        self,
        request: cmn_20200825_models.CreateMonitorItemRequest,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_item_with_options(request, runtime)

    async def create_monitor_item_async(
        self,
        request: cmn_20200825_models.CreateMonitorItemRequest,
    ) -> cmn_20200825_models.CreateMonitorItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_item_with_options_async(request, runtime)

    def create_os_version_with_options(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_os_version_with_options_async(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateOsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_os_version(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_os_version_with_options(request, runtime)

    async def create_os_version_async(
        self,
        request: cmn_20200825_models.CreateOsVersionRequest,
    ) -> cmn_20200825_models.CreateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_os_version_with_options_async(request, runtime)

    def create_physical_space_with_options(
        self,
        tmp_req: cmn_20200825_models.CreatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreatePhysicalSpaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.security_domain_list):
            request.security_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain_list, 'SecurityDomainList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.parent_uid):
            body['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_domain_list_shrink):
            body['SecurityDomainList'] = request.security_domain_list_shrink
        if not UtilClient.is_unset(request.space_abbreviation):
            body['SpaceAbbreviation'] = request.space_abbreviation
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreatePhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_physical_space_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreatePhysicalSpaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.security_domain_list):
            request.security_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain_list, 'SecurityDomainList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.parent_uid):
            body['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_domain_list_shrink):
            body['SecurityDomainList'] = request.security_domain_list_shrink
        if not UtilClient.is_unset(request.space_abbreviation):
            body['SpaceAbbreviation'] = request.space_abbreviation
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreatePhysicalSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_physical_space(
        self,
        request: cmn_20200825_models.CreatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_physical_space_with_options(request, runtime)

    async def create_physical_space_async(
        self,
        request: cmn_20200825_models.CreatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.CreatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_physical_space_with_options_async(request, runtime)

    def create_realtime_task_with_options(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.check_duplicate_policy):
            body['CheckDuplicatePolicy'] = request.check_duplicate_policy
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.item_name):
            body['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRealtimeTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateRealtimeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_realtime_task_with_options_async(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.check_duplicate_policy):
            body['CheckDuplicatePolicy'] = request.check_duplicate_policy
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.item_name):
            body['ItemName'] = request.item_name
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRealtimeTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateRealtimeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_realtime_task(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_realtime_task_with_options(request, runtime)

    async def create_realtime_task_async(
        self,
        request: cmn_20200825_models.CreateRealtimeTaskRequest,
    ) -> cmn_20200825_models.CreateRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_realtime_task_with_options_async(request, runtime)

    def create_resource_information_with_options(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        """
        @deprecated
        
        @param request: CreateResourceInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceInformationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.architecture_id):
            body['ArchitectureId'] = request.architecture_id
        body_flat = {}
        if not UtilClient.is_unset(request.information):
            body_flat['Information'] = request.information
        if not UtilClient.is_unset(request.resource_attribute):
            body['ResourceAttribute'] = request.resource_attribute
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateResourceInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_information_with_options_async(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        """
        @deprecated
        
        @param request: CreateResourceInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceInformationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.architecture_id):
            body['ArchitectureId'] = request.architecture_id
        body_flat = {}
        if not UtilClient.is_unset(request.information):
            body_flat['Information'] = request.information
        if not UtilClient.is_unset(request.resource_attribute):
            body['ResourceAttribute'] = request.resource_attribute
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateResourceInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_information(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        """
        @deprecated
        
        @param request: CreateResourceInformationRequest
        @return: CreateResourceInformationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_information_with_options(request, runtime)

    async def create_resource_information_async(
        self,
        request: cmn_20200825_models.CreateResourceInformationRequest,
    ) -> cmn_20200825_models.CreateResourceInformationResponse:
        """
        @deprecated
        
        @param request: CreateResourceInformationRequest
        @return: CreateResourceInformationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_information_with_options_async(request, runtime)

    def create_setup_project_with_options(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_time):
            body['DeliveryTime'] = request.delivery_time
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_setup_project_with_options_async(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_time):
            body['DeliveryTime'] = request.delivery_time
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSetupProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_setup_project(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_setup_project_with_options(request, runtime)

    async def create_setup_project_async(
        self,
        request: cmn_20200825_models.CreateSetupProjectRequest,
    ) -> cmn_20200825_models.CreateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_setup_project_with_options_async(request, runtime)

    def create_space_model_with_options(
        self,
        tmp_req: cmn_20200825_models.CreateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_space_model_with_options_async(
        self,
        tmp_req: cmn_20200825_models.CreateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.CreateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateSpaceModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_space_model(
        self,
        request: cmn_20200825_models.CreateSpaceModelRequest,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_space_model_with_options(request, runtime)

    async def create_space_model_async(
        self,
        request: cmn_20200825_models.CreateSpaceModelRequest,
    ) -> cmn_20200825_models.CreateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_space_model_with_options_async(request, runtime)

    def create_task_with_options(
        self,
        request: cmn_20200825_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: cmn_20200825_models.CreateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: cmn_20200825_models.CreateTaskRequest,
    ) -> cmn_20200825_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_task_with_options(request, runtime)

    async def create_task_async(
        self,
        request: cmn_20200825_models.CreateTaskRequest,
    ) -> cmn_20200825_models.CreateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_task_with_options_async(request, runtime)

    def create_time_period_with_options(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.time_period_description):
            body['TimePeriodDescription'] = request.time_period_description
        if not UtilClient.is_unset(request.time_period_name):
            body['TimePeriodName'] = request.time_period_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTimePeriod',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTimePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_time_period_with_options_async(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.time_period_description):
            body['TimePeriodDescription'] = request.time_period_description
        if not UtilClient.is_unset(request.time_period_name):
            body['TimePeriodName'] = request.time_period_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTimePeriod',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateTimePeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_time_period(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_time_period_with_options(request, runtime)

    async def create_time_period_async(
        self,
        request: cmn_20200825_models.CreateTimePeriodRequest,
    ) -> cmn_20200825_models.CreateTimePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_time_period_with_options_async(request, runtime)

    def create_work_order_with_options(
        self,
        request: cmn_20200825_models.CreateWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.alarm_happen_time):
            body['AlarmHappenTime'] = request.alarm_happen_time
        if not UtilClient.is_unset(request.alarm_recover_time):
            body['AlarmRecoverTime'] = request.alarm_recover_time
        if not UtilClient.is_unset(request.alarm_related):
            body['AlarmRelated'] = request.alarm_related
        if not UtilClient.is_unset(request.area):
            body['Area'] = request.area
        if not UtilClient.is_unset(request.circuit_id):
            body['CircuitId'] = request.circuit_id
        if not UtilClient.is_unset(request.circuit_name):
            body['CircuitName'] = request.circuit_name
        if not UtilClient.is_unset(request.circuit_type):
            body['CircuitType'] = request.circuit_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_ip):
            body['DeviceIp'] = request.device_ip
        if not UtilClient.is_unset(request.device_ip_a):
            body['DeviceIpA'] = request.device_ip_a
        if not UtilClient.is_unset(request.device_ip_b):
            body['DeviceIpB'] = request.device_ip_b
        if not UtilClient.is_unset(request.device_model_a):
            body['DeviceModelA'] = request.device_model_a
        if not UtilClient.is_unset(request.device_model_b):
            body['DeviceModelB'] = request.device_model_b
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_name_a):
            body['DeviceNameA'] = request.device_name_a
        if not UtilClient.is_unset(request.device_name_b):
            body['DeviceNameB'] = request.device_name_b
        if not UtilClient.is_unset(request.device_port_a):
            body['DevicePortA'] = request.device_port_a
        if not UtilClient.is_unset(request.device_port_b):
            body['DevicePortB'] = request.device_port_b
        if not UtilClient.is_unset(request.device_sn_a):
            body['DeviceSnA'] = request.device_sn_a
        if not UtilClient.is_unset(request.device_sn_b):
            body['DeviceSnB'] = request.device_sn_b
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.device_vendor):
            body['DeviceVendor'] = request.device_vendor
        if not UtilClient.is_unset(request.device_vendor_a):
            body['DeviceVendorA'] = request.device_vendor_a
        if not UtilClient.is_unset(request.device_vendor_b):
            body['DeviceVendorB'] = request.device_vendor_b
        if not UtilClient.is_unset(request.emergency_degree):
            body['EmergencyDegree'] = request.emergency_degree
        if not UtilClient.is_unset(request.impact_business):
            body['ImpactBusiness'] = request.impact_business
        if not UtilClient.is_unset(request.incident_description):
            body['IncidentDescription'] = request.incident_description
        if not UtilClient.is_unset(request.incident_sub_type):
            body['IncidentSubType'] = request.incident_sub_type
        if not UtilClient.is_unset(request.incident_type):
            body['IncidentType'] = request.incident_type
        if not UtilClient.is_unset(request.liable_man):
            body['LiableMan'] = request.liable_man
        if not UtilClient.is_unset(request.link_man):
            body['LinkMan'] = request.link_man
        if not UtilClient.is_unset(request.original_subject_alarm):
            body['OriginalSubjectAlarm'] = request.original_subject_alarm
        if not UtilClient.is_unset(request.process_limited):
            body['ProcessLimited'] = request.process_limited
        if not UtilClient.is_unset(request.process_man):
            body['ProcessMan'] = request.process_man
        if not UtilClient.is_unset(request.process_man_id):
            body['ProcessManId'] = request.process_man_id
        if not UtilClient.is_unset(request.skill_groups):
            body['SkillGroups'] = request.skill_groups
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_step):
            body['WorkOrderStep'] = request.work_order_step
        if not UtilClient.is_unset(request.work_order_title):
            body['WorkOrderTitle'] = request.work_order_title
        if not UtilClient.is_unset(request.work_order_type):
            body['WorkOrderType'] = request.work_order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateWorkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_work_order_with_options_async(
        self,
        request: cmn_20200825_models.CreateWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.CreateWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.alarm_happen_time):
            body['AlarmHappenTime'] = request.alarm_happen_time
        if not UtilClient.is_unset(request.alarm_recover_time):
            body['AlarmRecoverTime'] = request.alarm_recover_time
        if not UtilClient.is_unset(request.alarm_related):
            body['AlarmRelated'] = request.alarm_related
        if not UtilClient.is_unset(request.area):
            body['Area'] = request.area
        if not UtilClient.is_unset(request.circuit_id):
            body['CircuitId'] = request.circuit_id
        if not UtilClient.is_unset(request.circuit_name):
            body['CircuitName'] = request.circuit_name
        if not UtilClient.is_unset(request.circuit_type):
            body['CircuitType'] = request.circuit_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_ip):
            body['DeviceIp'] = request.device_ip
        if not UtilClient.is_unset(request.device_ip_a):
            body['DeviceIpA'] = request.device_ip_a
        if not UtilClient.is_unset(request.device_ip_b):
            body['DeviceIpB'] = request.device_ip_b
        if not UtilClient.is_unset(request.device_model_a):
            body['DeviceModelA'] = request.device_model_a
        if not UtilClient.is_unset(request.device_model_b):
            body['DeviceModelB'] = request.device_model_b
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_name_a):
            body['DeviceNameA'] = request.device_name_a
        if not UtilClient.is_unset(request.device_name_b):
            body['DeviceNameB'] = request.device_name_b
        if not UtilClient.is_unset(request.device_port_a):
            body['DevicePortA'] = request.device_port_a
        if not UtilClient.is_unset(request.device_port_b):
            body['DevicePortB'] = request.device_port_b
        if not UtilClient.is_unset(request.device_sn_a):
            body['DeviceSnA'] = request.device_sn_a
        if not UtilClient.is_unset(request.device_sn_b):
            body['DeviceSnB'] = request.device_sn_b
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.device_vendor):
            body['DeviceVendor'] = request.device_vendor
        if not UtilClient.is_unset(request.device_vendor_a):
            body['DeviceVendorA'] = request.device_vendor_a
        if not UtilClient.is_unset(request.device_vendor_b):
            body['DeviceVendorB'] = request.device_vendor_b
        if not UtilClient.is_unset(request.emergency_degree):
            body['EmergencyDegree'] = request.emergency_degree
        if not UtilClient.is_unset(request.impact_business):
            body['ImpactBusiness'] = request.impact_business
        if not UtilClient.is_unset(request.incident_description):
            body['IncidentDescription'] = request.incident_description
        if not UtilClient.is_unset(request.incident_sub_type):
            body['IncidentSubType'] = request.incident_sub_type
        if not UtilClient.is_unset(request.incident_type):
            body['IncidentType'] = request.incident_type
        if not UtilClient.is_unset(request.liable_man):
            body['LiableMan'] = request.liable_man
        if not UtilClient.is_unset(request.link_man):
            body['LinkMan'] = request.link_man
        if not UtilClient.is_unset(request.original_subject_alarm):
            body['OriginalSubjectAlarm'] = request.original_subject_alarm
        if not UtilClient.is_unset(request.process_limited):
            body['ProcessLimited'] = request.process_limited
        if not UtilClient.is_unset(request.process_man):
            body['ProcessMan'] = request.process_man
        if not UtilClient.is_unset(request.process_man_id):
            body['ProcessManId'] = request.process_man_id
        if not UtilClient.is_unset(request.skill_groups):
            body['SkillGroups'] = request.skill_groups
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_step):
            body['WorkOrderStep'] = request.work_order_step
        if not UtilClient.is_unset(request.work_order_title):
            body['WorkOrderTitle'] = request.work_order_title
        if not UtilClient.is_unset(request.work_order_type):
            body['WorkOrderType'] = request.work_order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.CreateWorkOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_work_order(
        self,
        request: cmn_20200825_models.CreateWorkOrderRequest,
    ) -> cmn_20200825_models.CreateWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_work_order_with_options(request, runtime)

    async def create_work_order_async(
        self,
        request: cmn_20200825_models.CreateWorkOrderRequest,
    ) -> cmn_20200825_models.CreateWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_work_order_with_options_async(request, runtime)

    def delete_configuration_specification_with_options(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: DeleteConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.configuration_specification_id):
            body['ConfigurationSpecificationId'] = request.configuration_specification_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_configuration_specification_with_options_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: DeleteConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.configuration_specification_id):
            body['ConfigurationSpecificationId'] = request.configuration_specification_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_configuration_specification(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: DeleteConfigurationSpecificationRequest
        @return: DeleteConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_configuration_specification_with_options(request, runtime)

    async def delete_configuration_specification_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.DeleteConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: DeleteConfigurationSpecificationRequest
        @return: DeleteConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_configuration_specification_with_options_async(request, runtime)

    def delete_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.configuration_variate_id):
            body['ConfigurationVariateId'] = request.configuration_variate_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.configuration_variate_id):
            body['ConfigurationVariateId'] = request.configuration_variate_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteConfigurationVariateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_configuration_variate(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_configuration_variate_with_options(request, runtime)

    async def delete_configuration_variate_async(
        self,
        request: cmn_20200825_models.DeleteConfigurationVariateRequest,
    ) -> cmn_20200825_models.DeleteConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_configuration_variate_with_options_async(request, runtime)

    def delete_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.dedicated_line_id):
            body['DedicatedLineId'] = request.dedicated_line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.dedicated_line_id):
            body['DedicatedLineId'] = request.dedicated_line_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDedicatedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dedicated_line(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_line_with_options(request, runtime)

    async def delete_dedicated_line_async(
        self,
        request: cmn_20200825_models.DeleteDedicatedLineRequest,
    ) -> cmn_20200825_models.DeleteDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_line_with_options_async(request, runtime)

    def delete_delivery_arch_version_with_options(
        self,
        request: cmn_20200825_models.DeleteDeliveryArchVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeliveryArchVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_arch_version_id):
            body['DeliveryArchVersionId'] = request.delivery_arch_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryArchVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeliveryArchVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_delivery_arch_version_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeliveryArchVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeliveryArchVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_arch_version_id):
            body['DeliveryArchVersionId'] = request.delivery_arch_version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryArchVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeliveryArchVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_delivery_arch_version(
        self,
        request: cmn_20200825_models.DeleteDeliveryArchVersionRequest,
    ) -> cmn_20200825_models.DeleteDeliveryArchVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_delivery_arch_version_with_options(request, runtime)

    async def delete_delivery_arch_version_async(
        self,
        request: cmn_20200825_models.DeleteDeliveryArchVersionRequest,
    ) -> cmn_20200825_models.DeleteDeliveryArchVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_delivery_arch_version_with_options_async(request, runtime)

    def delete_delivery_project_with_options(
        self,
        request: cmn_20200825_models.DeleteDeliveryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeliveryProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_project_id):
            body['DeliveryProjectId'] = request.delivery_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeliveryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_delivery_project_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeliveryProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeliveryProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.delivery_project_id):
            body['DeliveryProjectId'] = request.delivery_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeliveryProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_delivery_project(
        self,
        request: cmn_20200825_models.DeleteDeliveryProjectRequest,
    ) -> cmn_20200825_models.DeleteDeliveryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_delivery_project_with_options(request, runtime)

    async def delete_delivery_project_async(
        self,
        request: cmn_20200825_models.DeleteDeliveryProjectRequest,
    ) -> cmn_20200825_models.DeleteDeliveryProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_delivery_project_with_options_async(request, runtime)

    def delete_device_with_options(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    async def delete_device_async(
        self,
        request: cmn_20200825_models.DeleteDeviceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_with_options_async(request, runtime)

    def delete_device_form_with_options(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_form_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceFormResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device_form(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_form_with_options(request, runtime)

    async def delete_device_form_async(
        self,
        request: cmn_20200825_models.DeleteDeviceFormRequest,
    ) -> cmn_20200825_models.DeleteDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_form_with_options_async(request, runtime)

    def delete_device_property_with_options(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_property_id):
            body['DevicePropertyId'] = request.device_property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_property_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_property_id):
            body['DevicePropertyId'] = request.device_property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device_property(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_property_with_options(request, runtime)

    async def delete_device_property_async(
        self,
        request: cmn_20200825_models.DeleteDevicePropertyRequest,
    ) -> cmn_20200825_models.DeleteDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_property_with_options_async(request, runtime)

    def delete_device_resource_with_options(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_resource_with_options_async(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDeviceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device_resource(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_resource_with_options(request, runtime)

    async def delete_device_resource_async(
        self,
        request: cmn_20200825_models.DeleteDeviceResourceRequest,
    ) -> cmn_20200825_models.DeleteDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_resource_with_options_async(request, runtime)

    def delete_devices_with_options(
        self,
        tmp_req: cmn_20200825_models.DeleteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DeleteDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_ids_shrink):
            body['DeviceIds'] = request.device_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_devices_with_options_async(
        self,
        tmp_req: cmn_20200825_models.DeleteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DeleteDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_ids_shrink):
            body['DeviceIds'] = request.device_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_devices(
        self,
        request: cmn_20200825_models.DeleteDevicesRequest,
    ) -> cmn_20200825_models.DeleteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_devices_with_options(request, runtime)

    async def delete_devices_async(
        self,
        request: cmn_20200825_models.DeleteDevicesRequest,
    ) -> cmn_20200825_models.DeleteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_devices_with_options_async(request, runtime)

    def delete_event_definition_with_options(
        self,
        request: cmn_20200825_models.DeleteEventDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteEventDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteEventDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_definition_with_options_async(
        self,
        request: cmn_20200825_models.DeleteEventDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteEventDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteEventDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_definition(
        self,
        request: cmn_20200825_models.DeleteEventDefinitionRequest,
    ) -> cmn_20200825_models.DeleteEventDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_definition_with_options(request, runtime)

    async def delete_event_definition_async(
        self,
        request: cmn_20200825_models.DeleteEventDefinitionRequest,
    ) -> cmn_20200825_models.DeleteEventDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_definition_with_options_async(request, runtime)

    def delete_inspection_task_with_options(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInspectionTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_inspection_task_with_options_async(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInspectionTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_inspection_task(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_inspection_task_with_options(request, runtime)

    async def delete_inspection_task_async(
        self,
        request: cmn_20200825_models.DeleteInspectionTaskRequest,
    ) -> cmn_20200825_models.DeleteInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_inspection_task_with_options_async(request, runtime)

    def delete_os_version_with_options(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.os_version_id):
            body['OsVersionId'] = request.os_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_os_version_with_options_async(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.os_version_id):
            body['OsVersionId'] = request.os_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteOsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_os_version(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_os_version_with_options(request, runtime)

    async def delete_os_version_async(
        self,
        request: cmn_20200825_models.DeleteOsVersionRequest,
    ) -> cmn_20200825_models.DeleteOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_os_version_with_options_async(request, runtime)

    def delete_physical_space_with_options(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeletePhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_physical_space_with_options_async(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeletePhysicalSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_physical_space(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_physical_space_with_options(request, runtime)

    async def delete_physical_space_async(
        self,
        request: cmn_20200825_models.DeletePhysicalSpaceRequest,
    ) -> cmn_20200825_models.DeletePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_physical_space_with_options_async(request, runtime)

    def delete_resource_information_with_options(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.resource_information_id):
            body['ResourceInformationId'] = request.resource_information_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteResourceInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_information_with_options_async(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.resource_information_id):
            body['ResourceInformationId'] = request.resource_information_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteResourceInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_information(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_information_with_options(request, runtime)

    async def delete_resource_information_async(
        self,
        request: cmn_20200825_models.DeleteResourceInformationRequest,
    ) -> cmn_20200825_models.DeleteResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_information_with_options_async(request, runtime)

    def delete_setup_project_with_options(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_setup_project_with_options_async(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSetupProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_setup_project(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_setup_project_with_options(request, runtime)

    async def delete_setup_project_async(
        self,
        request: cmn_20200825_models.DeleteSetupProjectRequest,
    ) -> cmn_20200825_models.DeleteSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_setup_project_with_options_async(request, runtime)

    def delete_space_model_with_options(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.space_model_id):
            query['SpaceModelId'] = request.space_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_space_model_with_options_async(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.space_model_id):
            query['SpaceModelId'] = request.space_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteSpaceModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_space_model(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_space_model_with_options(request, runtime)

    async def delete_space_model_async(
        self,
        request: cmn_20200825_models.DeleteSpaceModelRequest,
    ) -> cmn_20200825_models.DeleteSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_space_model_with_options_async(request, runtime)

    def delete_work_order_with_options(
        self,
        request: cmn_20200825_models.DeleteWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.work_order_id):
            body['WorkOrderId'] = request.work_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteWorkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_work_order_with_options_async(
        self,
        request: cmn_20200825_models.DeleteWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DeleteWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.work_order_id):
            body['WorkOrderId'] = request.work_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DeleteWorkOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_work_order(
        self,
        request: cmn_20200825_models.DeleteWorkOrderRequest,
    ) -> cmn_20200825_models.DeleteWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_work_order_with_options(request, runtime)

    async def delete_work_order_async(
        self,
        request: cmn_20200825_models.DeleteWorkOrderRequest,
    ) -> cmn_20200825_models.DeleteWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_work_order_with_options_async(request, runtime)

    def disable_notification_with_options(
        self,
        tmp_req: cmn_20200825_models.DisableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DisableNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.expiry_time):
            body['ExpiryTime'] = request.expiry_time
        if not UtilClient.is_unset(request.list_shrink):
            body['List'] = request.list_shrink
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableNotification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DisableNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_notification_with_options_async(
        self,
        tmp_req: cmn_20200825_models.DisableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DisableNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.expiry_time):
            body['ExpiryTime'] = request.expiry_time
        if not UtilClient.is_unset(request.list_shrink):
            body['List'] = request.list_shrink
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableNotification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DisableNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_notification(
        self,
        request: cmn_20200825_models.DisableNotificationRequest,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_notification_with_options(request, runtime)

    async def disable_notification_async(
        self,
        request: cmn_20200825_models.DisableNotificationRequest,
    ) -> cmn_20200825_models.DisableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_notification_with_options_async(request, runtime)

    def download_device_resource_with_options(
        self,
        tmp_req: cmn_20200825_models.DownloadDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DownloadDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DownloadDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_device_resource_with_options_async(
        self,
        tmp_req: cmn_20200825_models.DownloadDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.DownloadDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.DownloadDeviceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_device_resource(
        self,
        request: cmn_20200825_models.DownloadDeviceResourceRequest,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_device_resource_with_options(request, runtime)

    async def download_device_resource_async(
        self,
        request: cmn_20200825_models.DownloadDeviceResourceRequest,
    ) -> cmn_20200825_models.DownloadDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_device_resource_with_options_async(request, runtime)

    def enable_notification_with_options(
        self,
        tmp_req: cmn_20200825_models.EnableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.EnableNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.list_shrink):
            body['List'] = request.list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableNotification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.EnableNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_notification_with_options_async(
        self,
        tmp_req: cmn_20200825_models.EnableNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.EnableNotificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list):
            request.list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list, 'List', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.list_shrink):
            body['List'] = request.list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableNotification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.EnableNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_notification(
        self,
        request: cmn_20200825_models.EnableNotificationRequest,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_notification_with_options(request, runtime)

    async def enable_notification_async(
        self,
        request: cmn_20200825_models.EnableNotificationRequest,
    ) -> cmn_20200825_models.EnableNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_notification_with_options_async(request, runtime)

    def get_alarm_status_with_options(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlarmStatus',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetAlarmStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alarm_status_with_options_async(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlarmStatus',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetAlarmStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alarm_status(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_alarm_status_with_options(request, runtime)

    async def get_alarm_status_async(
        self,
        request: cmn_20200825_models.GetAlarmStatusRequest,
    ) -> cmn_20200825_models.GetAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_alarm_status_with_options_async(request, runtime)

    def get_configuration_specification_with_options(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: GetConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_configuration_specification_with_options_async(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: GetConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_configuration_specification(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: GetConfigurationSpecificationRequest
        @return: GetConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_configuration_specification_with_options(request, runtime)

    async def get_configuration_specification_async(
        self,
        request: cmn_20200825_models.GetConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.GetConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: GetConfigurationSpecificationRequest
        @return: GetConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_configuration_specification_with_options_async(request, runtime)

    def get_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetConfigurationVariateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_configuration_variate(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_configuration_variate_with_options(request, runtime)

    async def get_configuration_variate_async(
        self,
        request: cmn_20200825_models.GetConfigurationVariateRequest,
    ) -> cmn_20200825_models.GetConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_configuration_variate_with_options_async(request, runtime)

    def get_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDedicatedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dedicated_line(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dedicated_line_with_options(request, runtime)

    async def get_dedicated_line_async(
        self,
        request: cmn_20200825_models.GetDedicatedLineRequest,
    ) -> cmn_20200825_models.GetDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dedicated_line_with_options_async(request, runtime)

    def get_device_with_options(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
    ) -> cmn_20200825_models.GetDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_with_options(request, runtime)

    async def get_device_async(
        self,
        request: cmn_20200825_models.GetDeviceRequest,
    ) -> cmn_20200825_models.GetDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_with_options_async(request, runtime)

    def get_device_config_with_options(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfig',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_config_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfig',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_config(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_with_options(request, runtime)

    async def get_device_config_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigRequest,
    ) -> cmn_20200825_models.GetDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_config_with_options_async(request, runtime)

    def get_device_config_date_with_options(
        self,
        request: cmn_20200825_models.GetDeviceConfigDateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigDateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigDate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_config_date_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigDateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigDateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigDate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_config_date(
        self,
        request: cmn_20200825_models.GetDeviceConfigDateRequest,
    ) -> cmn_20200825_models.GetDeviceConfigDateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_date_with_options(request, runtime)

    async def get_device_config_date_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigDateRequest,
    ) -> cmn_20200825_models.GetDeviceConfigDateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_config_date_with_options_async(request, runtime)

    def get_device_config_diff_with_options(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigDiff',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDiffResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_config_diff_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceConfigDiff',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceConfigDiffResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_config_diff(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_diff_with_options(request, runtime)

    async def get_device_config_diff_async(
        self,
        request: cmn_20200825_models.GetDeviceConfigDiffRequest,
    ) -> cmn_20200825_models.GetDeviceConfigDiffResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_config_diff_with_options_async(request, runtime)

    def get_device_form_with_options(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_form_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceFormResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_form(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_form_with_options(request, runtime)

    async def get_device_form_async(
        self,
        request: cmn_20200825_models.GetDeviceFormRequest,
    ) -> cmn_20200825_models.GetDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_form_with_options_async(request, runtime)

    def get_device_op_log_with_options(
        self,
        request: cmn_20200825_models.GetDeviceOpLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceOpLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceOpLog',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceOpLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_op_log_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceOpLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceOpLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceOpLog',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceOpLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_op_log(
        self,
        request: cmn_20200825_models.GetDeviceOpLogRequest,
    ) -> cmn_20200825_models.GetDeviceOpLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_op_log_with_options(request, runtime)

    async def get_device_op_log_async(
        self,
        request: cmn_20200825_models.GetDeviceOpLogRequest,
    ) -> cmn_20200825_models.GetDeviceOpLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_op_log_with_options_async(request, runtime)

    def get_device_property_with_options(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_property_with_options_async(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDevicePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_property(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_property_with_options(request, runtime)

    async def get_device_property_async(
        self,
        request: cmn_20200825_models.GetDevicePropertyRequest,
    ) -> cmn_20200825_models.GetDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_property_with_options_async(request, runtime)

    def get_device_resource_with_options(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_resource_with_options_async(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetDeviceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_resource(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_resource_with_options(request, runtime)

    async def get_device_resource_async(
        self,
        request: cmn_20200825_models.GetDeviceResourceRequest,
    ) -> cmn_20200825_models.GetDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_resource_with_options_async(request, runtime)

    def get_inspection_task_with_options(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInspectionTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inspection_task_with_options_async(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInspectionTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inspection_task(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inspection_task_with_options(request, runtime)

    async def get_inspection_task_async(
        self,
        request: cmn_20200825_models.GetInspectionTaskRequest,
    ) -> cmn_20200825_models.GetInspectionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inspection_task_with_options_async(request, runtime)

    def get_monitor_item_with_options(
        self,
        request: cmn_20200825_models.GetMonitorItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetMonitorItemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonitorItem',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetMonitorItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitor_item_with_options_async(
        self,
        request: cmn_20200825_models.GetMonitorItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetMonitorItemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonitorItem',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetMonitorItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitor_item(
        self,
        request: cmn_20200825_models.GetMonitorItemRequest,
    ) -> cmn_20200825_models.GetMonitorItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_item_with_options(request, runtime)

    async def get_monitor_item_async(
        self,
        request: cmn_20200825_models.GetMonitorItemRequest,
    ) -> cmn_20200825_models.GetMonitorItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_monitor_item_with_options_async(request, runtime)

    def get_os_download_path_with_options(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOsDownloadPath',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsDownloadPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_os_download_path_with_options_async(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOsDownloadPath',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsDownloadPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_os_download_path(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_os_download_path_with_options(request, runtime)

    async def get_os_download_path_async(
        self,
        request: cmn_20200825_models.GetOsDownloadPathRequest,
    ) -> cmn_20200825_models.GetOsDownloadPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_os_download_path_with_options_async(request, runtime)

    def get_os_version_with_options(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_os_version_with_options_async(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_os_version(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_os_version_with_options(request, runtime)

    async def get_os_version_async(
        self,
        request: cmn_20200825_models.GetOsVersionRequest,
    ) -> cmn_20200825_models.GetOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_os_version_with_options_async(request, runtime)

    def get_oss_policy_with_options(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssPolicy',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOssPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_policy_with_options_async(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssPolicy',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetOssPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_policy(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_policy_with_options(request, runtime)

    async def get_oss_policy_async(
        self,
        request: cmn_20200825_models.GetOssPolicyRequest,
    ) -> cmn_20200825_models.GetOssPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_policy_with_options_async(request, runtime)

    def get_physical_space_with_options(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_space_with_options_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_space(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_physical_space_with_options(request, runtime)

    async def get_physical_space_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_space_with_options_async(request, runtime)

    def get_physical_space_topo_with_options(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.physical_space_id):
            query['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.topo_type):
            query['TopoType'] = request.topo_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalSpaceTopo',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceTopoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_space_topo_with_options_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.physical_space_id):
            query['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.topo_type):
            query['TopoType'] = request.topo_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalSpaceTopo',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetPhysicalSpaceTopoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_space_topo(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_physical_space_topo_with_options(request, runtime)

    async def get_physical_space_topo_async(
        self,
        request: cmn_20200825_models.GetPhysicalSpaceTopoRequest,
    ) -> cmn_20200825_models.GetPhysicalSpaceTopoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_space_topo_with_options_async(request, runtime)

    def get_realtime_task_with_options(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetRealtimeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_task_with_options_async(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetRealtimeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_task(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_task_with_options(request, runtime)

    async def get_realtime_task_async(
        self,
        request: cmn_20200825_models.GetRealtimeTaskRequest,
    ) -> cmn_20200825_models.GetRealtimeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_task_with_options_async(request, runtime)

    def get_schedule_worker_with_options(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScheduleWorker',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleWorkerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_schedule_worker_with_options_async(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScheduleWorker',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetScheduleWorkerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_schedule_worker(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_schedule_worker_with_options(request, runtime)

    async def get_schedule_worker_async(
        self,
        request: cmn_20200825_models.GetScheduleWorkerRequest,
    ) -> cmn_20200825_models.GetScheduleWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_schedule_worker_with_options_async(request, runtime)

    def get_setup_project_with_options(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_setup_project_with_options_async(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSetupProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_setup_project(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_setup_project_with_options(request, runtime)

    async def get_setup_project_async(
        self,
        request: cmn_20200825_models.GetSetupProjectRequest,
    ) -> cmn_20200825_models.GetSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_setup_project_with_options_async(request, runtime)

    def get_space_model_with_options(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_space_model_with_options_async(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_space_model(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_with_options(request, runtime)

    async def get_space_model_async(
        self,
        request: cmn_20200825_models.GetSpaceModelRequest,
    ) -> cmn_20200825_models.GetSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_space_model_with_options_async(request, runtime)

    def get_space_model_instance_with_options(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModelInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_space_model_instance_with_options_async(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModelInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_space_model_instance(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_instance_with_options(request, runtime)

    async def get_space_model_instance_async(
        self,
        request: cmn_20200825_models.GetSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.GetSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_space_model_instance_with_options_async(request, runtime)

    def get_space_model_sort_with_options(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModelSort',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelSortResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_space_model_sort_with_options_async(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpaceModelSort',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetSpaceModelSortResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_space_model_sort(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_space_model_sort_with_options(request, runtime)

    async def get_space_model_sort_async(
        self,
        request: cmn_20200825_models.GetSpaceModelSortRequest,
    ) -> cmn_20200825_models.GetSpaceModelSortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_space_model_sort_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: cmn_20200825_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: cmn_20200825_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: cmn_20200825_models.GetTaskRequest,
    ) -> cmn_20200825_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: cmn_20200825_models.GetTaskRequest,
    ) -> cmn_20200825_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_work_order_with_options(
        self,
        request: cmn_20200825_models.GetWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetWorkOrderResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetWorkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_order_with_options_async(
        self,
        request: cmn_20200825_models.GetWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.GetWorkOrderResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.GetWorkOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_order(
        self,
        request: cmn_20200825_models.GetWorkOrderRequest,
    ) -> cmn_20200825_models.GetWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_work_order_with_options(request, runtime)

    async def get_work_order_async(
        self,
        request: cmn_20200825_models.GetWorkOrderRequest,
    ) -> cmn_20200825_models.GetWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_work_order_with_options_async(request, runtime)

    def list_alarm_status_with_options(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatus',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_status_with_options_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatus',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_status(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_with_options(request, runtime)

    async def list_alarm_status_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusRequest,
    ) -> cmn_20200825_models.ListAlarmStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_status_with_options_async(request, runtime)

    def list_alarm_status_histories_with_options(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatusHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_status_histories_with_options_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatusHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_status_histories(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_histories_with_options(request, runtime)

    async def list_alarm_status_histories_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusHistoriesRequest,
    ) -> cmn_20200825_models.ListAlarmStatusHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_status_histories_with_options_async(request, runtime)

    def list_alarm_status_statistics_with_options(
        self,
        request: cmn_20200825_models.ListAlarmStatusStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatusStatistics',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_status_statistics_with_options_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListAlarmStatusStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmStatusStatistics',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListAlarmStatusStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_status_statistics(
        self,
        request: cmn_20200825_models.ListAlarmStatusStatisticsRequest,
    ) -> cmn_20200825_models.ListAlarmStatusStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_status_statistics_with_options(request, runtime)

    async def list_alarm_status_statistics_async(
        self,
        request: cmn_20200825_models.ListAlarmStatusStatisticsRequest,
    ) -> cmn_20200825_models.ListAlarmStatusStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_status_statistics_with_options_async(request, runtime)

    def list_architecture_attribute_with_options(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        """
        @deprecated
        
        @param request: ListArchitectureAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArchitectureAttributeResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArchitectureAttribute',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListArchitectureAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_architecture_attribute_with_options_async(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        """
        @deprecated
        
        @param request: ListArchitectureAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArchitectureAttributeResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArchitectureAttribute',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListArchitectureAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_architecture_attribute(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        """
        @deprecated
        
        @param request: ListArchitectureAttributeRequest
        @return: ListArchitectureAttributeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_architecture_attribute_with_options(request, runtime)

    async def list_architecture_attribute_async(
        self,
        request: cmn_20200825_models.ListArchitectureAttributeRequest,
    ) -> cmn_20200825_models.ListArchitectureAttributeResponse:
        """
        @deprecated
        
        @param request: ListArchitectureAttributeRequest
        @return: ListArchitectureAttributeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_architecture_attribute_with_options_async(request, runtime)

    def list_configuration_specifications_with_options(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        """
        @deprecated
        
        @param request: ListConfigurationSpecificationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigurationSpecificationsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigurationSpecifications',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationSpecificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_configuration_specifications_with_options_async(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        """
        @deprecated
        
        @param request: ListConfigurationSpecificationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigurationSpecificationsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigurationSpecifications',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationSpecificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_configuration_specifications(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        """
        @deprecated
        
        @param request: ListConfigurationSpecificationsRequest
        @return: ListConfigurationSpecificationsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_configuration_specifications_with_options(request, runtime)

    async def list_configuration_specifications_async(
        self,
        request: cmn_20200825_models.ListConfigurationSpecificationsRequest,
    ) -> cmn_20200825_models.ListConfigurationSpecificationsResponse:
        """
        @deprecated
        
        @param request: ListConfigurationSpecificationsRequest
        @return: ListConfigurationSpecificationsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_configuration_specifications_with_options_async(request, runtime)

    def list_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConfigurationVariateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_configuration_variate(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_configuration_variate_with_options(request, runtime)

    async def list_configuration_variate_async(
        self,
        request: cmn_20200825_models.ListConfigurationVariateRequest,
    ) -> cmn_20200825_models.ListConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_configuration_variate_with_options_async(request, runtime)

    def list_connection_policies_with_options(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        """
        @deprecated
        
        @param request: ListConnectionPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectionPoliciesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.architecture_iteration_id):
            body['ArchitectureIterationId'] = request.architecture_iteration_id
        if not UtilClient.is_unset(request.connection_policy_id):
            body['ConnectionPolicyId'] = request.connection_policy_id
        if not UtilClient.is_unset(request.downlink_architecture_device_id):
            body['DownlinkArchitectureDeviceId'] = request.downlink_architecture_device_id
        if not UtilClient.is_unset(request.downlink_architecture_module_id):
            body['DownlinkArchitectureModuleId'] = request.downlink_architecture_module_id
        if not UtilClient.is_unset(request.uplink_architecture_device_id):
            body['UplinkArchitectureDeviceId'] = request.uplink_architecture_device_id
        if not UtilClient.is_unset(request.uplink_architecture_module_id):
            body['UplinkArchitectureModuleId'] = request.uplink_architecture_module_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConnectionPolicies',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConnectionPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connection_policies_with_options_async(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        """
        @deprecated
        
        @param request: ListConnectionPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectionPoliciesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.architecture_iteration_id):
            body['ArchitectureIterationId'] = request.architecture_iteration_id
        if not UtilClient.is_unset(request.connection_policy_id):
            body['ConnectionPolicyId'] = request.connection_policy_id
        if not UtilClient.is_unset(request.downlink_architecture_device_id):
            body['DownlinkArchitectureDeviceId'] = request.downlink_architecture_device_id
        if not UtilClient.is_unset(request.downlink_architecture_module_id):
            body['DownlinkArchitectureModuleId'] = request.downlink_architecture_module_id
        if not UtilClient.is_unset(request.uplink_architecture_device_id):
            body['UplinkArchitectureDeviceId'] = request.uplink_architecture_device_id
        if not UtilClient.is_unset(request.uplink_architecture_module_id):
            body['UplinkArchitectureModuleId'] = request.uplink_architecture_module_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConnectionPolicies',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListConnectionPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connection_policies(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        """
        @deprecated
        
        @param request: ListConnectionPoliciesRequest
        @return: ListConnectionPoliciesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_connection_policies_with_options(request, runtime)

    async def list_connection_policies_async(
        self,
        request: cmn_20200825_models.ListConnectionPoliciesRequest,
    ) -> cmn_20200825_models.ListConnectionPoliciesResponse:
        """
        @deprecated
        
        @param request: ListConnectionPoliciesRequest
        @return: ListConnectionPoliciesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_connection_policies_with_options_async(request, runtime)

    def list_dedicated_lines_with_options(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDedicatedLines',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDedicatedLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dedicated_lines_with_options_async(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDedicatedLines',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDedicatedLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dedicated_lines(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dedicated_lines_with_options(request, runtime)

    async def list_dedicated_lines_async(
        self,
        request: cmn_20200825_models.ListDedicatedLinesRequest,
    ) -> cmn_20200825_models.ListDedicatedLinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dedicated_lines_with_options_async(request, runtime)

    def list_device_forms_with_options(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceForms',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceFormsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_forms_with_options_async(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceForms',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceFormsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_forms(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_forms_with_options(request, runtime)

    async def list_device_forms_async(
        self,
        request: cmn_20200825_models.ListDeviceFormsRequest,
    ) -> cmn_20200825_models.ListDeviceFormsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_forms_with_options_async(request, runtime)

    def list_device_properties_with_options(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceProperties',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_properties_with_options_async(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceProperties',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_properties(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_properties_with_options(request, runtime)

    async def list_device_properties_async(
        self,
        request: cmn_20200825_models.ListDevicePropertiesRequest,
    ) -> cmn_20200825_models.ListDevicePropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_properties_with_options_async(request, runtime)

    def list_device_resources_with_options(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceResources',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_resources_with_options_async(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceResources',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_resources(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_resources_with_options(request, runtime)

    async def list_device_resources_async(
        self,
        request: cmn_20200825_models.ListDeviceResourcesRequest,
    ) -> cmn_20200825_models.ListDeviceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_resources_with_options_async(request, runtime)

    def list_device_values_with_options(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceValues',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_values_with_options_async(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceValues',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDeviceValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_values(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_values_with_options(request, runtime)

    async def list_device_values_async(
        self,
        request: cmn_20200825_models.ListDeviceValuesRequest,
    ) -> cmn_20200825_models.ListDeviceValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_values_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        tmp_req: cmn_20200825_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        if not UtilClient.is_unset(tmp_req.host_name):
            request.host_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.host_name, 'HostName', 'json')
        if not UtilClient.is_unset(tmp_req.ip):
            request.ip_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip, 'Ip', 'json')
        if not UtilClient.is_unset(tmp_req.mac):
            request.mac_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mac, 'Mac', 'json')
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        if not UtilClient.is_unset(tmp_req.security_domain):
            request.security_domain_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain, 'SecurityDomain', 'json')
        if not UtilClient.is_unset(tmp_req.service_status):
            request.service_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_status, 'ServiceStatus', 'json')
        if not UtilClient.is_unset(tmp_req.sn):
            request.sn_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sn, 'Sn', 'json')
        if not UtilClient.is_unset(tmp_req.vendor):
            request.vendor_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor, 'Vendor', 'json')
        query = {}
        if not UtilClient.is_unset(request.calculate_amount):
            query['CalculateAmount'] = request.calculate_amount
        if not UtilClient.is_unset(request.device_form_id):
            query['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.device_form_name):
            query['DeviceFormName'] = request.device_form_name
        if not UtilClient.is_unset(request.device_ids_shrink):
            query['DeviceIds'] = request.device_ids_shrink
        if not UtilClient.is_unset(request.ext_attributes):
            query['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name_shrink):
            query['HostName'] = request.host_name_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_shrink):
            query['Ip'] = request.ip_shrink
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.mac_shrink):
            query['Mac'] = request.mac_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.model_shrink):
            query['Model'] = request.model_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.physical_space_id):
            query['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_ids_shrink):
            query['PhysicalSpaceIds'] = request.physical_space_ids_shrink
        if not UtilClient.is_unset(request.security_domain_shrink):
            query['SecurityDomain'] = request.security_domain_shrink
        if not UtilClient.is_unset(request.service_status_shrink):
            query['ServiceStatus'] = request.service_status_shrink
        if not UtilClient.is_unset(request.sn_shrink):
            query['Sn'] = request.sn_shrink
        if not UtilClient.is_unset(request.vendor_shrink):
            query['Vendor'] = request.vendor_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        tmp_req: cmn_20200825_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        if not UtilClient.is_unset(tmp_req.host_name):
            request.host_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.host_name, 'HostName', 'json')
        if not UtilClient.is_unset(tmp_req.ip):
            request.ip_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip, 'Ip', 'json')
        if not UtilClient.is_unset(tmp_req.mac):
            request.mac_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.mac, 'Mac', 'json')
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        if not UtilClient.is_unset(tmp_req.security_domain):
            request.security_domain_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain, 'SecurityDomain', 'json')
        if not UtilClient.is_unset(tmp_req.service_status):
            request.service_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.service_status, 'ServiceStatus', 'json')
        if not UtilClient.is_unset(tmp_req.sn):
            request.sn_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sn, 'Sn', 'json')
        if not UtilClient.is_unset(tmp_req.vendor):
            request.vendor_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor, 'Vendor', 'json')
        query = {}
        if not UtilClient.is_unset(request.calculate_amount):
            query['CalculateAmount'] = request.calculate_amount
        if not UtilClient.is_unset(request.device_form_id):
            query['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.device_form_name):
            query['DeviceFormName'] = request.device_form_name
        if not UtilClient.is_unset(request.device_ids_shrink):
            query['DeviceIds'] = request.device_ids_shrink
        if not UtilClient.is_unset(request.ext_attributes):
            query['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name_shrink):
            query['HostName'] = request.host_name_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_shrink):
            query['Ip'] = request.ip_shrink
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.mac_shrink):
            query['Mac'] = request.mac_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.model_shrink):
            query['Model'] = request.model_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.physical_space_id):
            query['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_ids_shrink):
            query['PhysicalSpaceIds'] = request.physical_space_ids_shrink
        if not UtilClient.is_unset(request.security_domain_shrink):
            query['SecurityDomain'] = request.security_domain_shrink
        if not UtilClient.is_unset(request.service_status_shrink):
            query['ServiceStatus'] = request.service_status_shrink
        if not UtilClient.is_unset(request.sn_shrink):
            query['Sn'] = request.sn_shrink
        if not UtilClient.is_unset(request.vendor_shrink):
            query['Vendor'] = request.vendor_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_devices(
        self,
        request: cmn_20200825_models.ListDevicesRequest,
    ) -> cmn_20200825_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: cmn_20200825_models.ListDevicesRequest,
    ) -> cmn_20200825_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def list_event_definitions_with_options(
        self,
        request: cmn_20200825_models.ListEventDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListEventDefinitionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventDefinitions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListEventDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_definitions_with_options_async(
        self,
        request: cmn_20200825_models.ListEventDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListEventDefinitionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventDefinitions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListEventDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_definitions(
        self,
        request: cmn_20200825_models.ListEventDefinitionsRequest,
    ) -> cmn_20200825_models.ListEventDefinitionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_definitions_with_options(request, runtime)

    async def list_event_definitions_async(
        self,
        request: cmn_20200825_models.ListEventDefinitionsRequest,
    ) -> cmn_20200825_models.ListEventDefinitionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_definitions_with_options_async(request, runtime)

    def list_events_with_options(
        self,
        request: cmn_20200825_models.ListEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListEventsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvents',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_events_with_options_async(
        self,
        request: cmn_20200825_models.ListEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListEventsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvents',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_events(
        self,
        request: cmn_20200825_models.ListEventsRequest,
    ) -> cmn_20200825_models.ListEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_events_with_options(request, runtime)

    async def list_events_async(
        self,
        request: cmn_20200825_models.ListEventsRequest,
    ) -> cmn_20200825_models.ListEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_events_with_options_async(request, runtime)

    def list_inspection_devices_with_options(
        self,
        tmp_req: cmn_20200825_models.ListInspectionDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inspection_devices_with_options_async(
        self,
        tmp_req: cmn_20200825_models.ListInspectionDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model):
            request.model_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model, 'Model', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inspection_devices(
        self,
        request: cmn_20200825_models.ListInspectionDevicesRequest,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_devices_with_options(request, runtime)

    async def list_inspection_devices_async(
        self,
        request: cmn_20200825_models.ListInspectionDevicesRequest,
    ) -> cmn_20200825_models.ListInspectionDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inspection_devices_with_options_async(request, runtime)

    def list_inspection_task_reports_with_options(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionTaskReports',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTaskReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inspection_task_reports_with_options_async(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionTaskReports',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTaskReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inspection_task_reports(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_task_reports_with_options(request, runtime)

    async def list_inspection_task_reports_async(
        self,
        request: cmn_20200825_models.ListInspectionTaskReportsRequest,
    ) -> cmn_20200825_models.ListInspectionTaskReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inspection_task_reports_with_options_async(request, runtime)

    def list_inspection_tasks_with_options(
        self,
        tmp_req: cmn_20200825_models.ListInspectionTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_status):
            request.alarm_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_status, 'AlarmStatus', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionTasks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inspection_tasks_with_options_async(
        self,
        tmp_req: cmn_20200825_models.ListInspectionTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListInspectionTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alarm_status):
            request.alarm_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alarm_status, 'AlarmStatus', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionTasks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInspectionTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inspection_tasks(
        self,
        request: cmn_20200825_models.ListInspectionTasksRequest,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_tasks_with_options(request, runtime)

    async def list_inspection_tasks_async(
        self,
        request: cmn_20200825_models.ListInspectionTasksRequest,
    ) -> cmn_20200825_models.ListInspectionTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inspection_tasks_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInstancesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListInstancesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(self) -> cmn_20200825_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(runtime)

    async def list_instances_async(self) -> cmn_20200825_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(runtime)

    def list_ip_blocks_with_options(
        self,
        tmp_req: cmn_20200825_models.ListIpBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListIpBlocksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_list):
            request.ip_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_list, 'IpList', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpBlocks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListIpBlocksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ip_blocks_with_options_async(
        self,
        tmp_req: cmn_20200825_models.ListIpBlocksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListIpBlocksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_list):
            request.ip_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_list, 'IpList', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIpBlocks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListIpBlocksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ip_blocks(
        self,
        request: cmn_20200825_models.ListIpBlocksRequest,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ip_blocks_with_options(request, runtime)

    async def list_ip_blocks_async(
        self,
        request: cmn_20200825_models.ListIpBlocksRequest,
    ) -> cmn_20200825_models.ListIpBlocksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ip_blocks_with_options_async(request, runtime)

    def list_links_with_options(
        self,
        request: cmn_20200825_models.ListLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListLinksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLinks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListLinksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_links_with_options_async(
        self,
        request: cmn_20200825_models.ListLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListLinksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLinks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListLinksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_links(
        self,
        request: cmn_20200825_models.ListLinksRequest,
    ) -> cmn_20200825_models.ListLinksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_links_with_options(request, runtime)

    async def list_links_async(
        self,
        request: cmn_20200825_models.ListLinksRequest,
    ) -> cmn_20200825_models.ListLinksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_links_with_options_async(request, runtime)

    def list_logs_with_options(
        self,
        request: cmn_20200825_models.ListLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logs_with_options_async(
        self,
        request: cmn_20200825_models.ListLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logs(
        self,
        request: cmn_20200825_models.ListLogsRequest,
    ) -> cmn_20200825_models.ListLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_logs_with_options(request, runtime)

    async def list_logs_async(
        self,
        request: cmn_20200825_models.ListLogsRequest,
    ) -> cmn_20200825_models.ListLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_logs_with_options_async(request, runtime)

    def list_monitor_data_with_options(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMonitorData',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_monitor_data_with_options_async(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMonitorData',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_monitor_data(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_monitor_data_with_options(request, runtime)

    async def list_monitor_data_async(
        self,
        request: cmn_20200825_models.ListMonitorDataRequest,
    ) -> cmn_20200825_models.ListMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_monitor_data_with_options_async(request, runtime)

    def list_notification_histories_with_options(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_notification_histories_with_options_async(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_notification_histories(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_notification_histories_with_options(request, runtime)

    async def list_notification_histories_async(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesRequest,
    ) -> cmn_20200825_models.ListNotificationHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_notification_histories_with_options_async(request, runtime)

    def list_notification_histories_statistics_with_options(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListNotificationHistoriesStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationHistoriesStatistics',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_notification_histories_statistics_with_options_async(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListNotificationHistoriesStatisticsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationHistoriesStatistics',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListNotificationHistoriesStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_notification_histories_statistics(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesStatisticsRequest,
    ) -> cmn_20200825_models.ListNotificationHistoriesStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_notification_histories_statistics_with_options(request, runtime)

    async def list_notification_histories_statistics_async(
        self,
        request: cmn_20200825_models.ListNotificationHistoriesStatisticsRequest,
    ) -> cmn_20200825_models.ListNotificationHistoriesStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_notification_histories_statistics_with_options_async(request, runtime)

    def list_os_versions_with_options(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOsVersions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListOsVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_os_versions_with_options_async(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOsVersions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListOsVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_os_versions(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_os_versions_with_options(request, runtime)

    async def list_os_versions_async(
        self,
        request: cmn_20200825_models.ListOsVersionsRequest,
    ) -> cmn_20200825_models.ListOsVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_os_versions_with_options_async(request, runtime)

    def list_physical_spaces_with_options(
        self,
        tmp_req: cmn_20200825_models.ListPhysicalSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListPhysicalSpacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhysicalSpaces',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListPhysicalSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_physical_spaces_with_options_async(
        self,
        tmp_req: cmn_20200825_models.ListPhysicalSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListPhysicalSpacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPhysicalSpaces',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListPhysicalSpacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_physical_spaces(
        self,
        request: cmn_20200825_models.ListPhysicalSpacesRequest,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_physical_spaces_with_options(request, runtime)

    async def list_physical_spaces_async(
        self,
        request: cmn_20200825_models.ListPhysicalSpacesRequest,
    ) -> cmn_20200825_models.ListPhysicalSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_physical_spaces_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> cmn_20200825_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> cmn_20200825_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_resource_informations_with_options(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInformations',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInformationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_informations_with_options_async(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInformations',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInformationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_informations(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_informations_with_options(request, runtime)

    async def list_resource_informations_async(
        self,
        request: cmn_20200825_models.ListResourceInformationsRequest,
    ) -> cmn_20200825_models.ListResourceInformationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_informations_with_options_async(request, runtime)

    def list_resource_instances_with_options(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_instances_with_options_async(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceInstances',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_instances(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_instances_with_options(request, runtime)

    async def list_resource_instances_async(
        self,
        request: cmn_20200825_models.ListResourceInstancesRequest,
    ) -> cmn_20200825_models.ListResourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_instances_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(self) -> cmn_20200825_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(runtime)

    async def list_resource_types_async(self) -> cmn_20200825_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_types_with_options_async(runtime)

    def list_setup_projects_with_options(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSetupProjects',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSetupProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_setup_projects_with_options_async(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSetupProjects',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSetupProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_setup_projects(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_setup_projects_with_options(request, runtime)

    async def list_setup_projects_async(
        self,
        request: cmn_20200825_models.ListSetupProjectsRequest,
    ) -> cmn_20200825_models.ListSetupProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_setup_projects_with_options_async(request, runtime)

    def list_space_models_with_options(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpaceModels',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSpaceModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_space_models_with_options_async(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSpaceModels',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListSpaceModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_space_models(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_space_models_with_options(request, runtime)

    async def list_space_models_async(
        self,
        request: cmn_20200825_models.ListSpaceModelsRequest,
    ) -> cmn_20200825_models.ListSpaceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_space_models_with_options_async(request, runtime)

    def list_tasks_histories_with_options(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasksHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTasksHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_histories_with_options_async(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasksHistories',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTasksHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks_histories(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_histories_with_options(request, runtime)

    async def list_tasks_histories_async(
        self,
        request: cmn_20200825_models.ListTasksHistoriesRequest,
    ) -> cmn_20200825_models.ListTasksHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_histories_with_options_async(request, runtime)

    def list_tree_physical_spaces_with_options(
        self,
        tmp_req: cmn_20200825_models.ListTreePhysicalSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListTreePhysicalSpacesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListTreePhysicalSpacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTreePhysicalSpaces',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTreePhysicalSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tree_physical_spaces_with_options_async(
        self,
        tmp_req: cmn_20200825_models.ListTreePhysicalSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListTreePhysicalSpacesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ListTreePhysicalSpacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.physical_space_ids):
            request.physical_space_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.physical_space_ids, 'PhysicalSpaceIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTreePhysicalSpaces',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListTreePhysicalSpacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tree_physical_spaces(
        self,
        request: cmn_20200825_models.ListTreePhysicalSpacesRequest,
    ) -> cmn_20200825_models.ListTreePhysicalSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tree_physical_spaces_with_options(request, runtime)

    async def list_tree_physical_spaces_async(
        self,
        request: cmn_20200825_models.ListTreePhysicalSpacesRequest,
    ) -> cmn_20200825_models.ListTreePhysicalSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tree_physical_spaces_with_options_async(request, runtime)

    def list_work_orders_with_options(
        self,
        request: cmn_20200825_models.ListWorkOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListWorkOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.device_sn_a):
            body['DeviceSnA'] = request.device_sn_a
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_step):
            body['WorkOrderStep'] = request.work_order_step
        if not UtilClient.is_unset(request.work_order_title):
            body['WorkOrderTitle'] = request.work_order_title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkOrders',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListWorkOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_orders_with_options_async(
        self,
        request: cmn_20200825_models.ListWorkOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ListWorkOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.device_sn_a):
            body['DeviceSnA'] = request.device_sn_a
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_step):
            body['WorkOrderStep'] = request.work_order_step
        if not UtilClient.is_unset(request.work_order_title):
            body['WorkOrderTitle'] = request.work_order_title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkOrders',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ListWorkOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_work_orders(
        self,
        request: cmn_20200825_models.ListWorkOrdersRequest,
    ) -> cmn_20200825_models.ListWorkOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_work_orders_with_options(request, runtime)

    async def list_work_orders_async(
        self,
        request: cmn_20200825_models.ListWorkOrdersRequest,
    ) -> cmn_20200825_models.ListWorkOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_work_orders_with_options_async(request, runtime)

    def lock_space_model_with_options(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.space_model_id):
            query['SpaceModelId'] = request.space_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.LockSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_space_model_with_options_async(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.space_model_id):
            query['SpaceModelId'] = request.space_model_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.LockSpaceModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_space_model(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_space_model_with_options(request, runtime)

    async def lock_space_model_async(
        self,
        request: cmn_20200825_models.LockSpaceModelRequest,
    ) -> cmn_20200825_models.LockSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_space_model_with_options_async(request, runtime)

    def release_ipwith_options(
        self,
        tmp_req: cmn_20200825_models.ReleaseIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ReleaseIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            query['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseIP',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ReleaseIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_ipwith_options_async(
        self,
        tmp_req: cmn_20200825_models.ReleaseIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.ReleaseIPShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_resource_id):
            query['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            query['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseIP',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.ReleaseIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_ip(
        self,
        request: cmn_20200825_models.ReleaseIPRequest,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_ipwith_options(request, runtime)

    async def release_ip_async(
        self,
        request: cmn_20200825_models.ReleaseIPRequest,
    ) -> cmn_20200825_models.ReleaseIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_ipwith_options_async(request, runtime)

    def remark_work_order_with_options(
        self,
        request: cmn_20200825_models.RemarkWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.RemarkWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.work_order_id):
            body['WorkOrderId'] = request.work_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemarkWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.RemarkWorkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def remark_work_order_with_options_async(
        self,
        request: cmn_20200825_models.RemarkWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.RemarkWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.work_order_id):
            body['WorkOrderId'] = request.work_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemarkWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.RemarkWorkOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remark_work_order(
        self,
        request: cmn_20200825_models.RemarkWorkOrderRequest,
    ) -> cmn_20200825_models.RemarkWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.remark_work_order_with_options(request, runtime)

    async def remark_work_order_async(
        self,
        request: cmn_20200825_models.RemarkWorkOrderRequest,
    ) -> cmn_20200825_models.RemarkWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remark_work_order_with_options_async(request, runtime)

    def retry_tasks_with_options(
        self,
        tmp_req: cmn_20200825_models.RetryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.RetryTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.RetryTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_tasks):
            request.retry_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_tasks, 'RetryTasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.retry_tasks_shrink):
            query['RetryTasks'] = request.retry_tasks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryTasks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.RetryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_tasks_with_options_async(
        self,
        tmp_req: cmn_20200825_models.RetryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.RetryTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.RetryTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_tasks):
            request.retry_tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retry_tasks, 'RetryTasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.retry_tasks_shrink):
            query['RetryTasks'] = request.retry_tasks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryTasks',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.RetryTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_tasks(
        self,
        request: cmn_20200825_models.RetryTasksRequest,
    ) -> cmn_20200825_models.RetryTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_tasks_with_options(request, runtime)

    async def retry_tasks_async(
        self,
        request: cmn_20200825_models.RetryTasksRequest,
    ) -> cmn_20200825_models.RetryTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_tasks_with_options_async(request, runtime)

    def update_configuration_specification_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param tmp_req: UpdateConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.configuration_specification_id):
            body['ConfigurationSpecificationId'] = request.configuration_specification_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.related_variate_shrink):
            body['RelatedVariate'] = request.related_variate_shrink
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.specification_content):
            body['SpecificationContent'] = request.specification_content
        if not UtilClient.is_unset(request.specification_name):
            body['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_configuration_specification_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param tmp_req: UpdateConfigurationSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigurationSpecificationResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateConfigurationSpecificationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_variate):
            request.related_variate_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_variate, 'RelatedVariate', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.configuration_specification_id):
            body['ConfigurationSpecificationId'] = request.configuration_specification_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.related_variate_shrink):
            body['RelatedVariate'] = request.related_variate_shrink
        if not UtilClient.is_unset(request.role):
            body['Role'] = request.role
        if not UtilClient.is_unset(request.specification_content):
            body['SpecificationContent'] = request.specification_content
        if not UtilClient.is_unset(request.specification_name):
            body['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationSpecification',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_configuration_specification(
        self,
        request: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: UpdateConfigurationSpecificationRequest
        @return: UpdateConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_configuration_specification_with_options(request, runtime)

    async def update_configuration_specification_async(
        self,
        request: cmn_20200825_models.UpdateConfigurationSpecificationRequest,
    ) -> cmn_20200825_models.UpdateConfigurationSpecificationResponse:
        """
        @deprecated
        
        @param request: UpdateConfigurationSpecificationRequest
        @return: UpdateConfigurationSpecificationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_configuration_specification_with_options_async(request, runtime)

    def update_configuration_variate_with_options(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.configuration_variate_id):
            body['ConfigurationVariateId'] = request.configuration_variate_id
        if not UtilClient.is_unset(request.format_function):
            body['FormatFunction'] = request.format_function
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.variate_name):
            body['VariateName'] = request.variate_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationVariateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_configuration_variate_with_options_async(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.configuration_variate_id):
            body['ConfigurationVariateId'] = request.configuration_variate_id
        if not UtilClient.is_unset(request.format_function):
            body['FormatFunction'] = request.format_function
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.variate_name):
            body['VariateName'] = request.variate_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigurationVariate',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateConfigurationVariateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_configuration_variate(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_configuration_variate_with_options(request, runtime)

    async def update_configuration_variate_async(
        self,
        request: cmn_20200825_models.UpdateConfigurationVariateRequest,
    ) -> cmn_20200825_models.UpdateConfigurationVariateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_configuration_variate_with_options_async(request, runtime)

    def update_dedicated_line_with_options(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.contact):
            body['Contact'] = request.contact
        if not UtilClient.is_unset(request.dedicated_line_gateway):
            body['DedicatedLineGateway'] = request.dedicated_line_gateway
        if not UtilClient.is_unset(request.dedicated_line_id):
            body['DedicatedLineId'] = request.dedicated_line_id
        if not UtilClient.is_unset(request.dedicated_line_ip):
            body['DedicatedLineIp'] = request.dedicated_line_ip
        if not UtilClient.is_unset(request.dedicated_line_role):
            body['DedicatedLineRole'] = request.dedicated_line_role
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_port):
            body['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.expiration_date):
            body['ExpirationDate'] = request.expiration_date
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.isp):
            body['Isp'] = request.isp
        if not UtilClient.is_unset(request.isp_id):
            body['IspId'] = request.isp_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.online_date):
            body['OnlineDate'] = request.online_date
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDedicatedLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dedicated_line_with_options_async(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.bandwidth):
            body['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.contact):
            body['Contact'] = request.contact
        if not UtilClient.is_unset(request.dedicated_line_gateway):
            body['DedicatedLineGateway'] = request.dedicated_line_gateway
        if not UtilClient.is_unset(request.dedicated_line_id):
            body['DedicatedLineId'] = request.dedicated_line_id
        if not UtilClient.is_unset(request.dedicated_line_ip):
            body['DedicatedLineIp'] = request.dedicated_line_ip
        if not UtilClient.is_unset(request.dedicated_line_role):
            body['DedicatedLineRole'] = request.dedicated_line_role
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_port):
            body['DevicePort'] = request.device_port
        if not UtilClient.is_unset(request.expiration_date):
            body['ExpirationDate'] = request.expiration_date
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.isp):
            body['Isp'] = request.isp
        if not UtilClient.is_unset(request.isp_id):
            body['IspId'] = request.isp_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.online_date):
            body['OnlineDate'] = request.online_date
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDedicatedLine',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDedicatedLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dedicated_line(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dedicated_line_with_options(request, runtime)

    async def update_dedicated_line_async(
        self,
        request: cmn_20200825_models.UpdateDedicatedLineRequest,
    ) -> cmn_20200825_models.UpdateDedicatedLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dedicated_line_with_options_async(request, runtime)

    def update_device_with_options(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name):
            body['HostName'] = request.host_name
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_device_with_options_async(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.host_name):
            body['HostName'] = request.host_name
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.sn):
            body['Sn'] = request.sn
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevice',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_device(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_with_options(request, runtime)

    async def update_device_async(
        self,
        request: cmn_20200825_models.UpdateDeviceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_with_options_async(request, runtime)

    def update_device_form_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceFormShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_list):
            request.attribute_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_list, 'AttributeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.account_config):
            body['AccountConfig'] = request.account_config
        if not UtilClient.is_unset(request.attribute_list_shrink):
            body['AttributeList'] = request.attribute_list_shrink
        if not UtilClient.is_unset(request.config_compare):
            body['ConfigCompare'] = request.config_compare
        if not UtilClient.is_unset(request.detail_display):
            body['DetailDisplay'] = request.detail_display
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.related_device_form_id):
            body['RelatedDeviceFormId'] = request.related_device_form_id
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceFormResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_device_form_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceFormRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceFormShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_list):
            request.attribute_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_list, 'AttributeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.account_config):
            body['AccountConfig'] = request.account_config
        if not UtilClient.is_unset(request.attribute_list_shrink):
            body['AttributeList'] = request.attribute_list_shrink
        if not UtilClient.is_unset(request.config_compare):
            body['ConfigCompare'] = request.config_compare
        if not UtilClient.is_unset(request.detail_display):
            body['DetailDisplay'] = request.detail_display
        if not UtilClient.is_unset(request.device_form_id):
            body['DeviceFormId'] = request.device_form_id
        if not UtilClient.is_unset(request.related_device_form_id):
            body['RelatedDeviceFormId'] = request.related_device_form_id
        if not UtilClient.is_unset(request.script):
            body['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceForm',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceFormResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_device_form(
        self,
        request: cmn_20200825_models.UpdateDeviceFormRequest,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_form_with_options(request, runtime)

    async def update_device_form_async(
        self,
        request: cmn_20200825_models.UpdateDeviceFormRequest,
    ) -> cmn_20200825_models.UpdateDeviceFormResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_form_with_options_async(request, runtime)

    def update_device_property_with_options(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_property_id):
            body['DevicePropertyId'] = request.device_property_id
        if not UtilClient.is_unset(request.property_content):
            body['PropertyContent'] = request.property_content
        if not UtilClient.is_unset(request.property_format):
            body['PropertyFormat'] = request.property_format
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_device_property_with_options_async(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_property_id):
            body['DevicePropertyId'] = request.device_property_id
        if not UtilClient.is_unset(request.property_content):
            body['PropertyContent'] = request.property_content
        if not UtilClient.is_unset(request.property_format):
            body['PropertyFormat'] = request.property_format
        if not UtilClient.is_unset(request.property_name):
            body['PropertyName'] = request.property_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceProperty',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_device_property(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_property_with_options(request, runtime)

    async def update_device_property_async(
        self,
        request: cmn_20200825_models.UpdateDevicePropertyRequest,
    ) -> cmn_20200825_models.UpdateDevicePropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_property_with_options_async(request, runtime)

    def update_device_resource_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.device_resource_id):
            body['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            body['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.update_type):
            body['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_device_resource_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateDeviceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDeviceResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_resource_ids):
            request.device_resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_resource_ids, 'DeviceResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.device_resource_id):
            body['DeviceResourceId'] = request.device_resource_id
        if not UtilClient.is_unset(request.device_resource_ids_shrink):
            body['DeviceResourceIds'] = request.device_resource_ids_shrink
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.update_type):
            body['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceResource',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDeviceResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_device_resource(
        self,
        request: cmn_20200825_models.UpdateDeviceResourceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_resource_with_options(request, runtime)

    async def update_device_resource_async(
        self,
        request: cmn_20200825_models.UpdateDeviceResourceRequest,
    ) -> cmn_20200825_models.UpdateDeviceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_resource_with_options_async(request, runtime)

    def update_devices_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_ids_shrink):
            body['DeviceIds'] = request.device_ids_shrink
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_devices_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_ids):
            request.device_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_ids, 'DeviceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.device_ids_shrink):
            body['DeviceIds'] = request.device_ids_shrink
        if not UtilClient.is_unset(request.enable_password):
            body['EnablePassword'] = request.enable_password
        if not UtilClient.is_unset(request.ext_attributes):
            body['ExtAttributes'] = request.ext_attributes
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.login_type):
            body['LoginType'] = request.login_type
        if not UtilClient.is_unset(request.login_username):
            body['LoginUsername'] = request.login_username
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.security_domain):
            body['SecurityDomain'] = request.security_domain
        if not UtilClient.is_unset(request.service_status):
            body['ServiceStatus'] = request.service_status
        if not UtilClient.is_unset(request.snmp_account_type):
            body['SnmpAccountType'] = request.snmp_account_type
        if not UtilClient.is_unset(request.snmp_account_version):
            body['SnmpAccountVersion'] = request.snmp_account_version
        if not UtilClient.is_unset(request.snmp_auth_passphrase):
            body['SnmpAuthPassphrase'] = request.snmp_auth_passphrase
        if not UtilClient.is_unset(request.snmp_auth_protocol):
            body['SnmpAuthProtocol'] = request.snmp_auth_protocol
        if not UtilClient.is_unset(request.snmp_community):
            body['SnmpCommunity'] = request.snmp_community
        if not UtilClient.is_unset(request.snmp_privacy_passphrase):
            body['SnmpPrivacyPassphrase'] = request.snmp_privacy_passphrase
        if not UtilClient.is_unset(request.snmp_privacy_protocol):
            body['SnmpPrivacyProtocol'] = request.snmp_privacy_protocol
        if not UtilClient.is_unset(request.snmp_security_level):
            body['SnmpSecurityLevel'] = request.snmp_security_level
        if not UtilClient.is_unset(request.snmp_username):
            body['SnmpUsername'] = request.snmp_username
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevices',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_devices(
        self,
        request: cmn_20200825_models.UpdateDevicesRequest,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_devices_with_options(request, runtime)

    async def update_devices_async(
        self,
        request: cmn_20200825_models.UpdateDevicesRequest,
    ) -> cmn_20200825_models.UpdateDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_devices_with_options_async(request, runtime)

    def update_event_definition_with_options(
        self,
        request: cmn_20200825_models.UpdateEventDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateEventDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateEventDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_definition_with_options_async(
        self,
        request: cmn_20200825_models.UpdateEventDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateEventDefinitionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.event_id):
            body['EventId'] = request.event_id
        if not UtilClient.is_unset(request.event_name):
            body['EventName'] = request.event_name
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEventDefinition',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateEventDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_definition(
        self,
        request: cmn_20200825_models.UpdateEventDefinitionRequest,
    ) -> cmn_20200825_models.UpdateEventDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_event_definition_with_options(request, runtime)

    async def update_event_definition_async(
        self,
        request: cmn_20200825_models.UpdateEventDefinitionRequest,
    ) -> cmn_20200825_models.UpdateEventDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_event_definition_with_options_async(request, runtime)

    def update_information_key_action_with_options(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.key_action):
            query['KeyAction'] = request.key_action
        if not UtilClient.is_unset(request.resource_information_id):
            query['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInformationKeyAction',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInformationKeyActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_information_key_action_with_options_async(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.key_action):
            query['KeyAction'] = request.key_action
        if not UtilClient.is_unset(request.resource_information_id):
            query['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInformationKeyAction',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInformationKeyActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_information_key_action(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_information_key_action_with_options(request, runtime)

    async def update_information_key_action_async(
        self,
        request: cmn_20200825_models.UpdateInformationKeyActionRequest,
    ) -> cmn_20200825_models.UpdateInformationKeyActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_information_key_action_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: cmn_20200825_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: cmn_20200825_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: cmn_20200825_models.UpdateInstanceRequest,
    ) -> cmn_20200825_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: cmn_20200825_models.UpdateInstanceRequest,
    ) -> cmn_20200825_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_os_version_with_options(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.os_version_id):
            body['OsVersionId'] = request.os_version_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateOsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_os_version_with_options_async(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_version):
            body['OsVersion'] = request.os_version
        if not UtilClient.is_unset(request.os_version_id):
            body['OsVersionId'] = request.os_version_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOsVersion',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateOsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_os_version(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_with_options(request, runtime)

    async def update_os_version_async(
        self,
        request: cmn_20200825_models.UpdateOsVersionRequest,
    ) -> cmn_20200825_models.UpdateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_os_version_with_options_async(request, runtime)

    def update_physical_space_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdatePhysicalSpaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.security_domain_list):
            request.security_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain_list, 'SecurityDomainList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.move_action):
            body['MoveAction'] = request.move_action
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.parent_uid):
            body['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_domain_list_shrink):
            body['SecurityDomainList'] = request.security_domain_list_shrink
        if not UtilClient.is_unset(request.space_abbreviation):
            body['SpaceAbbreviation'] = request.space_abbreviation
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        if not UtilClient.is_unset(request.target_uid):
            body['TargetUid'] = request.target_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdatePhysicalSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_physical_space_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdatePhysicalSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdatePhysicalSpaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.security_domain_list):
            request.security_domain_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_domain_list, 'SecurityDomainList', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.city):
            body['City'] = request.city
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.move_action):
            body['MoveAction'] = request.move_action
        if not UtilClient.is_unset(request.owner):
            body['Owner'] = request.owner
        if not UtilClient.is_unset(request.parent_uid):
            body['ParentUid'] = request.parent_uid
        if not UtilClient.is_unset(request.physical_space_id):
            body['PhysicalSpaceId'] = request.physical_space_id
        if not UtilClient.is_unset(request.physical_space_name):
            body['PhysicalSpaceName'] = request.physical_space_name
        if not UtilClient.is_unset(request.province):
            body['Province'] = request.province
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.security_domain_list_shrink):
            body['SecurityDomainList'] = request.security_domain_list_shrink
        if not UtilClient.is_unset(request.space_abbreviation):
            body['SpaceAbbreviation'] = request.space_abbreviation
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        if not UtilClient.is_unset(request.target_uid):
            body['TargetUid'] = request.target_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePhysicalSpace',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdatePhysicalSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_physical_space(
        self,
        request: cmn_20200825_models.UpdatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_physical_space_with_options(request, runtime)

    async def update_physical_space_async(
        self,
        request: cmn_20200825_models.UpdatePhysicalSpaceRequest,
    ) -> cmn_20200825_models.UpdatePhysicalSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_physical_space_with_options_async(request, runtime)

    def update_project_progress_with_options(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.progress):
            body['Progress'] = request.progress
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectProgress',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateProjectProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_progress_with_options_async(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.progress):
            body['Progress'] = request.progress
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectProgress',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateProjectProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_progress(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_progress_with_options(request, runtime)

    async def update_project_progress_async(
        self,
        request: cmn_20200825_models.UpdateProjectProgressRequest,
    ) -> cmn_20200825_models.UpdateProjectProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_progress_with_options_async(request, runtime)

    def update_resource_information_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.information):
            request.information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.information, 'Information', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.information_shrink):
            body['Information'] = request.information_shrink
        if not UtilClient.is_unset(request.resource_attribute):
            body['ResourceAttribute'] = request.resource_attribute
        if not UtilClient.is_unset(request.resource_information_id):
            body['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_information_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInformationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.information):
            request.information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.information, 'Information', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.information_shrink):
            body['Information'] = request.information_shrink
        if not UtilClient.is_unset(request.resource_attribute):
            body['ResourceAttribute'] = request.resource_attribute
        if not UtilClient.is_unset(request.resource_information_id):
            body['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceInformation',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_information(
        self,
        request: cmn_20200825_models.UpdateResourceInformationRequest,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_information_with_options(request, runtime)

    async def update_resource_information_async(
        self,
        request: cmn_20200825_models.UpdateResourceInformationRequest,
    ) -> cmn_20200825_models.UpdateResourceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_information_with_options_async(request, runtime)

    def update_resource_instance_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_information):
            request.resource_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_information, 'ResourceInformation', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_information_shrink):
            query['ResourceInformation'] = request.resource_information_shrink
        if not UtilClient.is_unset(request.resource_information_id):
            query['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_instance_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateResourceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateResourceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_information):
            request.resource_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_information, 'ResourceInformation', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_information_shrink):
            query['ResourceInformation'] = request.resource_information_shrink
        if not UtilClient.is_unset(request.resource_information_id):
            query['ResourceInformationId'] = request.resource_information_id
        if not UtilClient.is_unset(request.setup_project_id):
            query['SetupProjectId'] = request.setup_project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateResourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_instance(
        self,
        request: cmn_20200825_models.UpdateResourceInstanceRequest,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_instance_with_options(request, runtime)

    async def update_resource_instance_async(
        self,
        request: cmn_20200825_models.UpdateResourceInstanceRequest,
    ) -> cmn_20200825_models.UpdateResourceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_instance_with_options_async(request, runtime)

    def update_setup_project_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSetupProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.packages):
            request.packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.packages, 'Packages', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.architecture_id):
            body['ArchitectureId'] = request.architecture_id
        if not UtilClient.is_unset(request.delivery_time):
            body['DeliveryTime'] = request.delivery_time
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.nodes):
            body['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.packages_shrink):
            body['Packages'] = request.packages_shrink
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSetupProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_setup_project_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateSetupProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSetupProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.packages):
            request.packages_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.packages, 'Packages', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.architecture_id):
            body['ArchitectureId'] = request.architecture_id
        if not UtilClient.is_unset(request.delivery_time):
            body['DeliveryTime'] = request.delivery_time
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.nodes):
            body['Nodes'] = request.nodes
        if not UtilClient.is_unset(request.packages_shrink):
            body['Packages'] = request.packages_shrink
        if not UtilClient.is_unset(request.setup_project_id):
            body['SetupProjectId'] = request.setup_project_id
        if not UtilClient.is_unset(request.space_id):
            body['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSetupProject',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSetupProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_setup_project(
        self,
        request: cmn_20200825_models.UpdateSetupProjectRequest,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_setup_project_with_options(request, runtime)

    async def update_setup_project_async(
        self,
        request: cmn_20200825_models.UpdateSetupProjectRequest,
    ) -> cmn_20200825_models.UpdateSetupProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_setup_project_with_options_async(request, runtime)

    def update_space_model_with_options(
        self,
        tmp_req: cmn_20200825_models.UpdateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.space_model_id):
            body['SpaceModelId'] = request.space_model_id
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_space_model_with_options_async(
        self,
        tmp_req: cmn_20200825_models.UpdateSpaceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        UtilClient.validate_model(tmp_req)
        request = cmn_20200825_models.UpdateSpaceModelShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.space_model_id):
            body['SpaceModelId'] = request.space_model_id
        if not UtilClient.is_unset(request.space_type):
            body['SpaceType'] = request.space_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSpaceModel',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_space_model(
        self,
        request: cmn_20200825_models.UpdateSpaceModelRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_space_model_with_options(request, runtime)

    async def update_space_model_async(
        self,
        request: cmn_20200825_models.UpdateSpaceModelRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_space_model_with_options_async(request, runtime)

    def update_space_model_instance_with_options(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.space_id):
            query['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSpaceModelInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_space_model_instance_with_options_async(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.space_id):
            query['SpaceId'] = request.space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSpaceModelInstance',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateSpaceModelInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_space_model_instance(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_space_model_instance_with_options(request, runtime)

    async def update_space_model_instance_async(
        self,
        request: cmn_20200825_models.UpdateSpaceModelInstanceRequest,
    ) -> cmn_20200825_models.UpdateSpaceModelInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_space_model_instance_with_options_async(request, runtime)

    def update_work_order_with_options(
        self,
        request: cmn_20200825_models.UpdateWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.alarm_happen_time):
            body['AlarmHappenTime'] = request.alarm_happen_time
        if not UtilClient.is_unset(request.alarm_recover_time):
            body['AlarmRecoverTime'] = request.alarm_recover_time
        if not UtilClient.is_unset(request.alarm_related):
            body['AlarmRelated'] = request.alarm_related
        if not UtilClient.is_unset(request.area):
            body['Area'] = request.area
        if not UtilClient.is_unset(request.circuit_id):
            body['CircuitId'] = request.circuit_id
        if not UtilClient.is_unset(request.circuit_name):
            body['CircuitName'] = request.circuit_name
        if not UtilClient.is_unset(request.circuit_type):
            body['CircuitType'] = request.circuit_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_ip):
            body['DeviceIp'] = request.device_ip
        if not UtilClient.is_unset(request.device_ip_a):
            body['DeviceIpA'] = request.device_ip_a
        if not UtilClient.is_unset(request.device_ip_b):
            body['DeviceIpB'] = request.device_ip_b
        if not UtilClient.is_unset(request.device_model_a):
            body['DeviceModelA'] = request.device_model_a
        if not UtilClient.is_unset(request.device_model_b):
            body['DeviceModelB'] = request.device_model_b
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_name_a):
            body['DeviceNameA'] = request.device_name_a
        if not UtilClient.is_unset(request.device_name_b):
            body['DeviceNameB'] = request.device_name_b
        if not UtilClient.is_unset(request.device_port_a):
            body['DevicePortA'] = request.device_port_a
        if not UtilClient.is_unset(request.device_port_b):
            body['DevicePortB'] = request.device_port_b
        if not UtilClient.is_unset(request.device_sn_a):
            body['DeviceSnA'] = request.device_sn_a
        if not UtilClient.is_unset(request.device_sn_b):
            body['DeviceSnB'] = request.device_sn_b
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.device_vendor):
            body['DeviceVendor'] = request.device_vendor
        if not UtilClient.is_unset(request.device_vendor_a):
            body['DeviceVendorA'] = request.device_vendor_a
        if not UtilClient.is_unset(request.device_vendor_b):
            body['DeviceVendorB'] = request.device_vendor_b
        if not UtilClient.is_unset(request.emergency_degree):
            body['EmergencyDegree'] = request.emergency_degree
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.hang_file_name):
            body['HangFileName'] = request.hang_file_name
        if not UtilClient.is_unset(request.hang_file_path):
            body['HangFilePath'] = request.hang_file_path
        if not UtilClient.is_unset(request.hang_reason):
            body['HangReason'] = request.hang_reason
        if not UtilClient.is_unset(request.impact_business):
            body['ImpactBusiness'] = request.impact_business
        if not UtilClient.is_unset(request.incident_description):
            body['IncidentDescription'] = request.incident_description
        if not UtilClient.is_unset(request.incident_sub_type):
            body['IncidentSubType'] = request.incident_sub_type
        if not UtilClient.is_unset(request.incident_type):
            body['IncidentType'] = request.incident_type
        if not UtilClient.is_unset(request.liable_man):
            body['LiableMan'] = request.liable_man
        if not UtilClient.is_unset(request.link_man):
            body['LinkMan'] = request.link_man
        if not UtilClient.is_unset(request.original_subject_alarm):
            body['OriginalSubjectAlarm'] = request.original_subject_alarm
        if not UtilClient.is_unset(request.process_limited):
            body['ProcessLimited'] = request.process_limited
        if not UtilClient.is_unset(request.process_man):
            body['ProcessMan'] = request.process_man
        if not UtilClient.is_unset(request.process_man_id):
            body['ProcessManId'] = request.process_man_id
        if not UtilClient.is_unset(request.process_result):
            body['ProcessResult'] = request.process_result
        if not UtilClient.is_unset(request.skill_groups):
            body['SkillGroups'] = request.skill_groups
        if not UtilClient.is_unset(request.work_order_id):
            body['WorkOrderId'] = request.work_order_id
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_step):
            body['WorkOrderStep'] = request.work_order_step
        if not UtilClient.is_unset(request.work_order_title):
            body['WorkOrderTitle'] = request.work_order_title
        if not UtilClient.is_unset(request.work_order_type):
            body['WorkOrderType'] = request.work_order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateWorkOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_work_order_with_options_async(
        self,
        request: cmn_20200825_models.UpdateWorkOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cmn_20200825_models.UpdateWorkOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        body = {}
        if not UtilClient.is_unset(request.alarm_happen_time):
            body['AlarmHappenTime'] = request.alarm_happen_time
        if not UtilClient.is_unset(request.alarm_recover_time):
            body['AlarmRecoverTime'] = request.alarm_recover_time
        if not UtilClient.is_unset(request.alarm_related):
            body['AlarmRelated'] = request.alarm_related
        if not UtilClient.is_unset(request.area):
            body['Area'] = request.area
        if not UtilClient.is_unset(request.circuit_id):
            body['CircuitId'] = request.circuit_id
        if not UtilClient.is_unset(request.circuit_name):
            body['CircuitName'] = request.circuit_name
        if not UtilClient.is_unset(request.circuit_type):
            body['CircuitType'] = request.circuit_type
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.device_ip):
            body['DeviceIp'] = request.device_ip
        if not UtilClient.is_unset(request.device_ip_a):
            body['DeviceIpA'] = request.device_ip_a
        if not UtilClient.is_unset(request.device_ip_b):
            body['DeviceIpB'] = request.device_ip_b
        if not UtilClient.is_unset(request.device_model_a):
            body['DeviceModelA'] = request.device_model_a
        if not UtilClient.is_unset(request.device_model_b):
            body['DeviceModelB'] = request.device_model_b
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_name_a):
            body['DeviceNameA'] = request.device_name_a
        if not UtilClient.is_unset(request.device_name_b):
            body['DeviceNameB'] = request.device_name_b
        if not UtilClient.is_unset(request.device_port_a):
            body['DevicePortA'] = request.device_port_a
        if not UtilClient.is_unset(request.device_port_b):
            body['DevicePortB'] = request.device_port_b
        if not UtilClient.is_unset(request.device_sn_a):
            body['DeviceSnA'] = request.device_sn_a
        if not UtilClient.is_unset(request.device_sn_b):
            body['DeviceSnB'] = request.device_sn_b
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.device_vendor):
            body['DeviceVendor'] = request.device_vendor
        if not UtilClient.is_unset(request.device_vendor_a):
            body['DeviceVendorA'] = request.device_vendor_a
        if not UtilClient.is_unset(request.device_vendor_b):
            body['DeviceVendorB'] = request.device_vendor_b
        if not UtilClient.is_unset(request.emergency_degree):
            body['EmergencyDegree'] = request.emergency_degree
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.hang_file_name):
            body['HangFileName'] = request.hang_file_name
        if not UtilClient.is_unset(request.hang_file_path):
            body['HangFilePath'] = request.hang_file_path
        if not UtilClient.is_unset(request.hang_reason):
            body['HangReason'] = request.hang_reason
        if not UtilClient.is_unset(request.impact_business):
            body['ImpactBusiness'] = request.impact_business
        if not UtilClient.is_unset(request.incident_description):
            body['IncidentDescription'] = request.incident_description
        if not UtilClient.is_unset(request.incident_sub_type):
            body['IncidentSubType'] = request.incident_sub_type
        if not UtilClient.is_unset(request.incident_type):
            body['IncidentType'] = request.incident_type
        if not UtilClient.is_unset(request.liable_man):
            body['LiableMan'] = request.liable_man
        if not UtilClient.is_unset(request.link_man):
            body['LinkMan'] = request.link_man
        if not UtilClient.is_unset(request.original_subject_alarm):
            body['OriginalSubjectAlarm'] = request.original_subject_alarm
        if not UtilClient.is_unset(request.process_limited):
            body['ProcessLimited'] = request.process_limited
        if not UtilClient.is_unset(request.process_man):
            body['ProcessMan'] = request.process_man
        if not UtilClient.is_unset(request.process_man_id):
            body['ProcessManId'] = request.process_man_id
        if not UtilClient.is_unset(request.process_result):
            body['ProcessResult'] = request.process_result
        if not UtilClient.is_unset(request.skill_groups):
            body['SkillGroups'] = request.skill_groups
        if not UtilClient.is_unset(request.work_order_id):
            body['WorkOrderId'] = request.work_order_id
        if not UtilClient.is_unset(request.work_order_source):
            body['WorkOrderSource'] = request.work_order_source
        if not UtilClient.is_unset(request.work_order_step):
            body['WorkOrderStep'] = request.work_order_step
        if not UtilClient.is_unset(request.work_order_title):
            body['WorkOrderTitle'] = request.work_order_title
        if not UtilClient.is_unset(request.work_order_type):
            body['WorkOrderType'] = request.work_order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkOrder',
            version='2020-08-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cmn_20200825_models.UpdateWorkOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_work_order(
        self,
        request: cmn_20200825_models.UpdateWorkOrderRequest,
    ) -> cmn_20200825_models.UpdateWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_work_order_with_options(request, runtime)

    async def update_work_order_async(
        self,
        request: cmn_20200825_models.UpdateWorkOrderRequest,
    ) -> cmn_20200825_models.UpdateWorkOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_work_order_with_options_async(request, runtime)
