# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_foasconsole20211028 import models as foasconsole_20211028_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('foasconsole', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def convert_hybrid_instance_with_options(
        self,
        tmp_req: foasconsole_20211028_models.ConvertHybridInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ConvertHybridInstanceResponse:
        """
        @summary 开通弹性计算
        
        @param tmp_req: ConvertHybridInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertHybridInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ConvertHybridInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            query['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertHybridInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertHybridInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertHybridInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def convert_hybrid_instance_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.ConvertHybridInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ConvertHybridInstanceResponse:
        """
        @summary 开通弹性计算
        
        @param tmp_req: ConvertHybridInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertHybridInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ConvertHybridInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            query['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertHybridInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertHybridInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertHybridInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def convert_hybrid_instance(
        self,
        request: foasconsole_20211028_models.ConvertHybridInstanceRequest,
    ) -> foasconsole_20211028_models.ConvertHybridInstanceResponse:
        """
        @summary 开通弹性计算
        
        @param request: ConvertHybridInstanceRequest
        @return: ConvertHybridInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_hybrid_instance_with_options(request, runtime)

    async def convert_hybrid_instance_async(
        self,
        request: foasconsole_20211028_models.ConvertHybridInstanceRequest,
    ) -> foasconsole_20211028_models.ConvertHybridInstanceResponse:
        """
        @summary 开通弹性计算
        
        @param request: ConvertHybridInstanceRequest
        @return: ConvertHybridInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_hybrid_instance_with_options_async(request, runtime)

    def convert_instance_with_options(
        self,
        tmp_req: foasconsole_20211028_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ConvertInstanceResponse:
        """
        @summary 按量付费转包年包月
        
        @param tmp_req: ConvertInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ConvertInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.namespace_resource_specs):
            request.namespace_resource_specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespace_resource_specs, 'NamespaceResourceSpecs', 'json')
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_auto_renew):
            body['IsAutoRenew'] = request.is_auto_renew
        if not UtilClient.is_unset(request.namespace_resource_specs_shrink):
            body['NamespaceResourceSpecs'] = request.namespace_resource_specs_shrink
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def convert_instance_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.ConvertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ConvertInstanceResponse:
        """
        @summary 按量付费转包年包月
        
        @param tmp_req: ConvertInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ConvertInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.namespace_resource_specs):
            request.namespace_resource_specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespace_resource_specs, 'NamespaceResourceSpecs', 'json')
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_auto_renew):
            body['IsAutoRenew'] = request.is_auto_renew
        if not UtilClient.is_unset(request.namespace_resource_specs_shrink):
            body['NamespaceResourceSpecs'] = request.namespace_resource_specs_shrink
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def convert_instance(
        self,
        request: foasconsole_20211028_models.ConvertInstanceRequest,
    ) -> foasconsole_20211028_models.ConvertInstanceResponse:
        """
        @summary 按量付费转包年包月
        
        @param request: ConvertInstanceRequest
        @return: ConvertInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_instance_with_options(request, runtime)

    async def convert_instance_async(
        self,
        request: foasconsole_20211028_models.ConvertInstanceRequest,
    ) -> foasconsole_20211028_models.ConvertInstanceResponse:
        """
        @summary 按量付费转包年包月
        
        @param request: ConvertInstanceRequest
        @return: ConvertInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_instance_with_options_async(request, runtime)

    def convert_prepay_instance_with_options(
        self,
        request: foasconsole_20211028_models.ConvertPrepayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ConvertPrepayInstanceResponse:
        """
        @summary 包年包月转按量付费
        
        @param request: ConvertPrepayInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertPrepayInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertPrepayInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertPrepayInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertPrepayInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def convert_prepay_instance_with_options_async(
        self,
        request: foasconsole_20211028_models.ConvertPrepayInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ConvertPrepayInstanceResponse:
        """
        @summary 包年包月转按量付费
        
        @param request: ConvertPrepayInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertPrepayInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConvertPrepayInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertPrepayInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ConvertPrepayInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def convert_prepay_instance(
        self,
        request: foasconsole_20211028_models.ConvertPrepayInstanceRequest,
    ) -> foasconsole_20211028_models.ConvertPrepayInstanceResponse:
        """
        @summary 包年包月转按量付费
        
        @param request: ConvertPrepayInstanceRequest
        @return: ConvertPrepayInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.convert_prepay_instance_with_options(request, runtime)

    async def convert_prepay_instance_async(
        self,
        request: foasconsole_20211028_models.ConvertPrepayInstanceRequest,
    ) -> foasconsole_20211028_models.ConvertPrepayInstanceResponse:
        """
        @summary 包年包月转按量付费
        
        @param request: ConvertPrepayInstanceRequest
        @return: ConvertPrepayInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.convert_prepay_instance_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        tmp_req: foasconsole_20211028_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param tmp_req: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.CreateInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.storage):
            request.storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage, 'Storage', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture_type):
            body['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.monitor_type):
            body['MonitorType'] = request.monitor_type
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.promotion_code):
            body['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        if not UtilClient.is_unset(request.storage_shrink):
            body['Storage'] = request.storage_shrink
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.use_promotion_code):
            body['UsePromotionCode'] = request.use_promotion_code
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_instance_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param tmp_req: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.CreateInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.storage):
            request.storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage, 'Storage', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture_type):
            body['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.monitor_type):
            body['MonitorType'] = request.monitor_type
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.promotion_code):
            body['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        if not UtilClient.is_unset(request.storage_shrink):
            body['Storage'] = request.storage_shrink
        if not UtilClient.is_unset(request.tag_shrink):
            body['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.use_promotion_code):
            body['UsePromotionCode'] = request.use_promotion_code
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_instance(
        self,
        request: foasconsole_20211028_models.CreateInstanceRequest,
    ) -> foasconsole_20211028_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: foasconsole_20211028_models.CreateInstanceRequest,
    ) -> foasconsole_20211028_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        tmp_req: foasconsole_20211028_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.CreateNamespaceResponse:
        """
        @summary 创建命名空间
        
        @param tmp_req: CreateNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.CreateNamespaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateNamespaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateNamespaceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_namespace_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.CreateNamespaceResponse:
        """
        @summary 创建命名空间
        
        @param tmp_req: CreateNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.CreateNamespaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateNamespaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.CreateNamespaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_namespace(
        self,
        request: foasconsole_20211028_models.CreateNamespaceRequest,
    ) -> foasconsole_20211028_models.CreateNamespaceResponse:
        """
        @summary 创建命名空间
        
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: foasconsole_20211028_models.CreateNamespaceRequest,
    ) -> foasconsole_20211028_models.CreateNamespaceResponse:
        """
        @summary 创建命名空间
        
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: foasconsole_20211028_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DeleteInstanceResponse:
        """
        @summary 释放按量付费的实例
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_instance_with_options_async(
        self,
        request: foasconsole_20211028_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DeleteInstanceResponse:
        """
        @summary 释放按量付费的实例
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_instance(
        self,
        request: foasconsole_20211028_models.DeleteInstanceRequest,
    ) -> foasconsole_20211028_models.DeleteInstanceResponse:
        """
        @summary 释放按量付费的实例
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: foasconsole_20211028_models.DeleteInstanceRequest,
    ) -> foasconsole_20211028_models.DeleteInstanceResponse:
        """
        @summary 释放按量付费的实例
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: foasconsole_20211028_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DeleteNamespaceResponse:
        """
        @summary 删除namespace
        
        @param request: DeleteNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteNamespaceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteNamespaceResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_namespace_with_options_async(
        self,
        request: foasconsole_20211028_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DeleteNamespaceResponse:
        """
        @summary 删除namespace
        
        @param request: DeleteNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNamespace',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteNamespaceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DeleteNamespaceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_namespace(
        self,
        request: foasconsole_20211028_models.DeleteNamespaceRequest,
    ) -> foasconsole_20211028_models.DeleteNamespaceResponse:
        """
        @summary 删除namespace
        
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: foasconsole_20211028_models.DeleteNamespaceRequest,
    ) -> foasconsole_20211028_models.DeleteNamespaceResponse:
        """
        @summary 删除namespace
        
        @param request: DeleteNamespaceRequest
        @return: DeleteNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        tmp_req: foasconsole_20211028_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeInstancesResponse:
        """
        @summary instance列表
        
        @param tmp_req: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.DescribeInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_instances_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeInstancesResponse:
        """
        @summary instance列表
        
        @param tmp_req: DescribeInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.DescribeInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_instances(
        self,
        request: foasconsole_20211028_models.DescribeInstancesRequest,
    ) -> foasconsole_20211028_models.DescribeInstancesResponse:
        """
        @summary instance列表
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: foasconsole_20211028_models.DescribeInstancesRequest,
    ) -> foasconsole_20211028_models.DescribeInstancesResponse:
        """
        @summary instance列表
        
        @param request: DescribeInstancesRequest
        @return: DescribeInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_namespaces_with_options(
        self,
        tmp_req: foasconsole_20211028_models.DescribeNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeNamespacesResponse:
        """
        @summary namespace列表
        
        @param tmp_req: DescribeNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.DescribeNamespacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeNamespacesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeNamespacesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_namespaces_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.DescribeNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeNamespacesResponse:
        """
        @summary namespace列表
        
        @param tmp_req: DescribeNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.DescribeNamespacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNamespaces',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeNamespacesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeNamespacesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_namespaces(
        self,
        request: foasconsole_20211028_models.DescribeNamespacesRequest,
    ) -> foasconsole_20211028_models.DescribeNamespacesResponse:
        """
        @summary namespace列表
        
        @param request: DescribeNamespacesRequest
        @return: DescribeNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_namespaces_with_options(request, runtime)

    async def describe_namespaces_async(
        self,
        request: foasconsole_20211028_models.DescribeNamespacesRequest,
    ) -> foasconsole_20211028_models.DescribeNamespacesResponse:
        """
        @summary namespace列表
        
        @param request: DescribeNamespacesRequest
        @return: DescribeNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_namespaces_with_options_async(request, runtime)

    def describe_supported_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeSupportedRegionsResponse:
        """
        @summary 获取支持的region列表
        
        @param request: DescribeSupportedRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSupportedRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSupportedRegions',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedRegionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedRegionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_supported_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeSupportedRegionsResponse:
        """
        @summary 获取支持的region列表
        
        @param request: DescribeSupportedRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSupportedRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeSupportedRegions',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedRegionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedRegionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_supported_regions(self) -> foasconsole_20211028_models.DescribeSupportedRegionsResponse:
        """
        @summary 获取支持的region列表
        
        @return: DescribeSupportedRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_supported_regions_with_options(runtime)

    async def describe_supported_regions_async(self) -> foasconsole_20211028_models.DescribeSupportedRegionsResponse:
        """
        @summary 获取支持的region列表
        
        @return: DescribeSupportedRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_supported_regions_with_options_async(runtime)

    def describe_supported_zones_with_options(
        self,
        request: foasconsole_20211028_models.DescribeSupportedZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeSupportedZonesResponse:
        """
        @summary 获取支持的zoneId列表
        
        @param request: DescribeSupportedZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSupportedZonesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportedZones',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedZonesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedZonesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_supported_zones_with_options_async(
        self,
        request: foasconsole_20211028_models.DescribeSupportedZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.DescribeSupportedZonesResponse:
        """
        @summary 获取支持的zoneId列表
        
        @param request: DescribeSupportedZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSupportedZonesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSupportedZones',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedZonesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.DescribeSupportedZonesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_supported_zones(
        self,
        request: foasconsole_20211028_models.DescribeSupportedZonesRequest,
    ) -> foasconsole_20211028_models.DescribeSupportedZonesResponse:
        """
        @summary 获取支持的zoneId列表
        
        @param request: DescribeSupportedZonesRequest
        @return: DescribeSupportedZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_supported_zones_with_options(request, runtime)

    async def describe_supported_zones_async(
        self,
        request: foasconsole_20211028_models.DescribeSupportedZonesRequest,
    ) -> foasconsole_20211028_models.DescribeSupportedZonesResponse:
        """
        @summary 获取支持的zoneId列表
        
        @param request: DescribeSupportedZonesRequest
        @return: DescribeSupportedZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_supported_zones_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: foasconsole_20211028_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ListTagResourcesResponse:
        """
        @summary 列举flinkasi标签
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: foasconsole_20211028_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ListTagResourcesResponse:
        """
        @summary 列举flinkasi标签
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: foasconsole_20211028_models.ListTagResourcesRequest,
    ) -> foasconsole_20211028_models.ListTagResourcesResponse:
        """
        @summary 列举flinkasi标签
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: foasconsole_20211028_models.ListTagResourcesRequest,
    ) -> foasconsole_20211028_models.ListTagResourcesResponse:
        """
        @summary 列举flinkasi标签
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_elastic_resource_spec_with_options(
        self,
        tmp_req: foasconsole_20211028_models.ModifyElasticResourceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyElasticResourceSpecResponse:
        """
        @summary 对按量弹性实例修改resource quota
        
        @param tmp_req: ModifyElasticResourceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticResourceSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyElasticResourceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyElasticResourceSpec',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyElasticResourceSpecResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyElasticResourceSpecResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_elastic_resource_spec_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.ModifyElasticResourceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyElasticResourceSpecResponse:
        """
        @summary 对按量弹性实例修改resource quota
        
        @param tmp_req: ModifyElasticResourceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyElasticResourceSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyElasticResourceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyElasticResourceSpec',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyElasticResourceSpecResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyElasticResourceSpecResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_elastic_resource_spec(
        self,
        request: foasconsole_20211028_models.ModifyElasticResourceSpecRequest,
    ) -> foasconsole_20211028_models.ModifyElasticResourceSpecResponse:
        """
        @summary 对按量弹性实例修改resource quota
        
        @param request: ModifyElasticResourceSpecRequest
        @return: ModifyElasticResourceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_resource_spec_with_options(request, runtime)

    async def modify_elastic_resource_spec_async(
        self,
        request: foasconsole_20211028_models.ModifyElasticResourceSpecRequest,
    ) -> foasconsole_20211028_models.ModifyElasticResourceSpecResponse:
        """
        @summary 对按量弹性实例修改resource quota
        
        @param request: ModifyElasticResourceSpecRequest
        @return: ModifyElasticResourceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_resource_spec_with_options_async(request, runtime)

    def modify_instance_vswitch_with_options(
        self,
        tmp_req: foasconsole_20211028_models.ModifyInstanceVswitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyInstanceVswitchResponse:
        """
        @summary 修改集群交换机
        
        @param tmp_req: ModifyInstanceVswitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVswitchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyInstanceVswitchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVswitch',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyInstanceVswitchResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyInstanceVswitchResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_instance_vswitch_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.ModifyInstanceVswitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyInstanceVswitchResponse:
        """
        @summary 修改集群交换机
        
        @param tmp_req: ModifyInstanceVswitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceVswitchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyInstanceVswitchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyInstanceVswitch',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyInstanceVswitchResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyInstanceVswitchResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_instance_vswitch(
        self,
        request: foasconsole_20211028_models.ModifyInstanceVswitchRequest,
    ) -> foasconsole_20211028_models.ModifyInstanceVswitchResponse:
        """
        @summary 修改集群交换机
        
        @param request: ModifyInstanceVswitchRequest
        @return: ModifyInstanceVswitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vswitch_with_options(request, runtime)

    async def modify_instance_vswitch_async(
        self,
        request: foasconsole_20211028_models.ModifyInstanceVswitchRequest,
    ) -> foasconsole_20211028_models.ModifyInstanceVswitchResponse:
        """
        @summary 修改集群交换机
        
        @param request: ModifyInstanceVswitchRequest
        @return: ModifyInstanceVswitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vswitch_with_options_async(request, runtime)

    def modify_namespace_spec_v2with_options(
        self,
        tmp_req: foasconsole_20211028_models.ModifyNamespaceSpecV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyNamespaceSpecV2Response:
        """
        @summary 修改namespace资源，包含按量和包年包月、混合计费
        
        @param tmp_req: ModifyNamespaceSpecV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNamespaceSpecV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyNamespaceSpecV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.elastic_resource_spec):
            request.elastic_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.elastic_resource_spec, 'ElasticResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.guaranteed_resource_spec):
            request.guaranteed_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.guaranteed_resource_spec, 'GuaranteedResourceSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.ha):
            query['Ha'] = request.ha
        body = {}
        if not UtilClient.is_unset(request.elastic_resource_spec_shrink):
            body['ElasticResourceSpec'] = request.elastic_resource_spec_shrink
        if not UtilClient.is_unset(request.guaranteed_resource_spec_shrink):
            body['GuaranteedResourceSpec'] = request.guaranteed_resource_spec_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNamespaceSpecV2',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyNamespaceSpecV2Response(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyNamespaceSpecV2Response(),
                self.execute(params, req, runtime)
            )

    async def modify_namespace_spec_v2with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.ModifyNamespaceSpecV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyNamespaceSpecV2Response:
        """
        @summary 修改namespace资源，包含按量和包年包月、混合计费
        
        @param tmp_req: ModifyNamespaceSpecV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNamespaceSpecV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyNamespaceSpecV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.elastic_resource_spec):
            request.elastic_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.elastic_resource_spec, 'ElasticResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.guaranteed_resource_spec):
            request.guaranteed_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.guaranteed_resource_spec, 'GuaranteedResourceSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.ha):
            query['Ha'] = request.ha
        body = {}
        if not UtilClient.is_unset(request.elastic_resource_spec_shrink):
            body['ElasticResourceSpec'] = request.elastic_resource_spec_shrink
        if not UtilClient.is_unset(request.guaranteed_resource_spec_shrink):
            body['GuaranteedResourceSpec'] = request.guaranteed_resource_spec_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNamespaceSpecV2',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyNamespaceSpecV2Response(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyNamespaceSpecV2Response(),
                await self.execute_async(params, req, runtime)
            )

    def modify_namespace_spec_v2(
        self,
        request: foasconsole_20211028_models.ModifyNamespaceSpecV2Request,
    ) -> foasconsole_20211028_models.ModifyNamespaceSpecV2Response:
        """
        @summary 修改namespace资源，包含按量和包年包月、混合计费
        
        @param request: ModifyNamespaceSpecV2Request
        @return: ModifyNamespaceSpecV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_namespace_spec_v2with_options(request, runtime)

    async def modify_namespace_spec_v2_async(
        self,
        request: foasconsole_20211028_models.ModifyNamespaceSpecV2Request,
    ) -> foasconsole_20211028_models.ModifyNamespaceSpecV2Response:
        """
        @summary 修改namespace资源，包含按量和包年包月、混合计费
        
        @param request: ModifyNamespaceSpecV2Request
        @return: ModifyNamespaceSpecV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_namespace_spec_v2with_options_async(request, runtime)

    def modify_prepay_instance_spec_with_options(
        self,
        tmp_req: foasconsole_20211028_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2021-10-28::ModifyInstanceSpec instead.
        
        @summary 扩容/缩容
        
        @param tmp_req: ModifyPrepayInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyPrepayInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.ha_zone_id):
            body['HaZoneId'] = request.ha_zone_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2021-10-28::ModifyInstanceSpec instead.
        
        @summary 扩容/缩容
        
        @param tmp_req: ModifyPrepayInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyPrepayInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.ha_zone_id):
            body['HaZoneId'] = request.ha_zone_id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_prepay_instance_spec(
        self,
        request: foasconsole_20211028_models.ModifyPrepayInstanceSpecRequest,
    ) -> foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2021-10-28::ModifyInstanceSpec instead.
        
        @summary 扩容/缩容
        
        @param request: ModifyPrepayInstanceSpecRequest
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: foasconsole_20211028_models.ModifyPrepayInstanceSpecRequest,
    ) -> foasconsole_20211028_models.ModifyPrepayInstanceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayInstanceSpec is deprecated, please use foasconsole::2021-10-28::ModifyInstanceSpec instead.
        
        @summary 扩容/缩容
        
        @param request: ModifyPrepayInstanceSpecRequest
        @return: ModifyPrepayInstanceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def modify_prepay_namespace_spec_with_options(
        self,
        tmp_req: foasconsole_20211028_models.ModifyPrepayNamespaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2021-10-28::ModifyNamespaceSpec instead.
        
        @summary 修改namespace资源分配
        
        @param tmp_req: ModifyPrepayNamespaceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyPrepayNamespaceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayNamespaceSpec',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse(),
                self.execute(params, req, runtime)
            )

    async def modify_prepay_namespace_spec_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.ModifyPrepayNamespaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2021-10-28::ModifyNamespaceSpec instead.
        
        @summary 修改namespace资源分配
        
        @param tmp_req: ModifyPrepayNamespaceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.ModifyPrepayNamespaceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayNamespaceSpec',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse(),
                await self.execute_async(params, req, runtime)
            )

    def modify_prepay_namespace_spec(
        self,
        request: foasconsole_20211028_models.ModifyPrepayNamespaceSpecRequest,
    ) -> foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2021-10-28::ModifyNamespaceSpec instead.
        
        @summary 修改namespace资源分配
        
        @param request: ModifyPrepayNamespaceSpecRequest
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_namespace_spec_with_options(request, runtime)

    async def modify_prepay_namespace_spec_async(
        self,
        request: foasconsole_20211028_models.ModifyPrepayNamespaceSpecRequest,
    ) -> foasconsole_20211028_models.ModifyPrepayNamespaceSpecResponse:
        """
        @deprecated OpenAPI ModifyPrepayNamespaceSpec is deprecated, please use foasconsole::2021-10-28::ModifyNamespaceSpec instead.
        
        @summary 修改namespace资源分配
        
        @param request: ModifyPrepayNamespaceSpecRequest
        @return: ModifyPrepayNamespaceSpecResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_namespace_spec_with_options_async(request, runtime)

    def query_convert_instance_price_with_options(
        self,
        tmp_req: foasconsole_20211028_models.QueryConvertInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryConvertInstancePriceResponse:
        """
        @summary 按量付费转包年包月询价
        
        @param tmp_req: QueryConvertInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConvertInstancePriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.QueryConvertInstancePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.namespace_resource_specs):
            request.namespace_resource_specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespace_resource_specs, 'NamespaceResourceSpecs', 'json')
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_auto_renew):
            body['IsAutoRenew'] = request.is_auto_renew
        if not UtilClient.is_unset(request.namespace_resource_specs_shrink):
            body['NamespaceResourceSpecs'] = request.namespace_resource_specs_shrink
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertInstancePriceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertInstancePriceResponse(),
                self.execute(params, req, runtime)
            )

    async def query_convert_instance_price_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.QueryConvertInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryConvertInstancePriceResponse:
        """
        @summary 按量付费转包年包月询价
        
        @param tmp_req: QueryConvertInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConvertInstancePriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.QueryConvertInstancePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.namespace_resource_specs):
            request.namespace_resource_specs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespace_resource_specs, 'NamespaceResourceSpecs', 'json')
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_auto_renew):
            body['IsAutoRenew'] = request.is_auto_renew
        if not UtilClient.is_unset(request.namespace_resource_specs_shrink):
            body['NamespaceResourceSpecs'] = request.namespace_resource_specs_shrink
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertInstancePriceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertInstancePriceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_convert_instance_price(
        self,
        request: foasconsole_20211028_models.QueryConvertInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryConvertInstancePriceResponse:
        """
        @summary 按量付费转包年包月询价
        
        @param request: QueryConvertInstancePriceRequest
        @return: QueryConvertInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_convert_instance_price_with_options(request, runtime)

    async def query_convert_instance_price_async(
        self,
        request: foasconsole_20211028_models.QueryConvertInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryConvertInstancePriceResponse:
        """
        @summary 按量付费转包年包月询价
        
        @param request: QueryConvertInstancePriceRequest
        @return: QueryConvertInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_convert_instance_price_with_options_async(request, runtime)

    def query_convert_prepay_instance_price_with_options(
        self,
        request: foasconsole_20211028_models.QueryConvertPrepayInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse:
        """
        @summary 包年包月转按量付费询价
        
        @param request: QueryConvertPrepayInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConvertPrepayInstancePriceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertPrepayInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse(),
                self.execute(params, req, runtime)
            )

    async def query_convert_prepay_instance_price_with_options_async(
        self,
        request: foasconsole_20211028_models.QueryConvertPrepayInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse:
        """
        @summary 包年包月转按量付费询价
        
        @param request: QueryConvertPrepayInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryConvertPrepayInstancePriceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryConvertPrepayInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_convert_prepay_instance_price(
        self,
        request: foasconsole_20211028_models.QueryConvertPrepayInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse:
        """
        @summary 包年包月转按量付费询价
        
        @param request: QueryConvertPrepayInstancePriceRequest
        @return: QueryConvertPrepayInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_convert_prepay_instance_price_with_options(request, runtime)

    async def query_convert_prepay_instance_price_async(
        self,
        request: foasconsole_20211028_models.QueryConvertPrepayInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryConvertPrepayInstancePriceResponse:
        """
        @summary 包年包月转按量付费询价
        
        @param request: QueryConvertPrepayInstancePriceRequest
        @return: QueryConvertPrepayInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_convert_prepay_instance_price_with_options_async(request, runtime)

    def query_create_instance_price_with_options(
        self,
        tmp_req: foasconsole_20211028_models.QueryCreateInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryCreateInstancePriceResponse:
        """
        @summary 获取创建实例的价格
        
        @param tmp_req: QueryCreateInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCreateInstancePriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.QueryCreateInstancePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.storage):
            request.storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage, 'Storage', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture_type):
            body['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.promotion_code):
            body['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        if not UtilClient.is_unset(request.storage_shrink):
            body['Storage'] = request.storage_shrink
        if not UtilClient.is_unset(request.use_promotion_code):
            body['UsePromotionCode'] = request.use_promotion_code
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCreateInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryCreateInstancePriceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryCreateInstancePriceResponse(),
                self.execute(params, req, runtime)
            )

    async def query_create_instance_price_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.QueryCreateInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryCreateInstancePriceResponse:
        """
        @summary 获取创建实例的价格
        
        @param tmp_req: QueryCreateInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCreateInstancePriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.QueryCreateInstancePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.storage):
            request.storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.storage, 'Storage', 'json')
        if not UtilClient.is_unset(tmp_req.v_switch_ids):
            request.v_switch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switch_ids, 'VSwitchIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.architecture_type):
            body['ArchitectureType'] = request.architecture_type
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.extra):
            body['Extra'] = request.extra
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.promotion_code):
            body['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        if not UtilClient.is_unset(request.storage_shrink):
            body['Storage'] = request.storage_shrink
        if not UtilClient.is_unset(request.use_promotion_code):
            body['UsePromotionCode'] = request.use_promotion_code
        if not UtilClient.is_unset(request.v_switch_ids_shrink):
            body['VSwitchIds'] = request.v_switch_ids_shrink
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCreateInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryCreateInstancePriceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryCreateInstancePriceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_create_instance_price(
        self,
        request: foasconsole_20211028_models.QueryCreateInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryCreateInstancePriceResponse:
        """
        @summary 获取创建实例的价格
        
        @param request: QueryCreateInstancePriceRequest
        @return: QueryCreateInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_create_instance_price_with_options(request, runtime)

    async def query_create_instance_price_async(
        self,
        request: foasconsole_20211028_models.QueryCreateInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryCreateInstancePriceResponse:
        """
        @summary 获取创建实例的价格
        
        @param request: QueryCreateInstancePriceRequest
        @return: QueryCreateInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_create_instance_price_with_options_async(request, runtime)

    def query_modify_instance_price_with_options(
        self,
        tmp_req: foasconsole_20211028_models.QueryModifyInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryModifyInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例修改资源规格的价格
        
        @param tmp_req: QueryModifyInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryModifyInstancePriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.QueryModifyInstancePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.promotion_code):
            body['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        if not UtilClient.is_unset(request.use_promotion_code):
            body['UsePromotionCode'] = request.use_promotion_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryModifyInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryModifyInstancePriceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryModifyInstancePriceResponse(),
                self.execute(params, req, runtime)
            )

    async def query_modify_instance_price_with_options_async(
        self,
        tmp_req: foasconsole_20211028_models.QueryModifyInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryModifyInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例修改资源规格的价格
        
        @param tmp_req: QueryModifyInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryModifyInstancePriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = foasconsole_20211028_models.QueryModifyInstancePriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ha_resource_spec):
            request.ha_resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_resource_spec, 'HaResourceSpec', 'json')
        if not UtilClient.is_unset(tmp_req.ha_vswitch_ids):
            request.ha_vswitch_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ha_vswitch_ids, 'HaVSwitchIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_spec):
            request.resource_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_spec, 'ResourceSpec', 'json')
        body = {}
        if not UtilClient.is_unset(request.ha):
            body['Ha'] = request.ha
        if not UtilClient.is_unset(request.ha_resource_spec_shrink):
            body['HaResourceSpec'] = request.ha_resource_spec_shrink
        if not UtilClient.is_unset(request.ha_vswitch_ids_shrink):
            body['HaVSwitchIds'] = request.ha_vswitch_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.promotion_code):
            body['PromotionCode'] = request.promotion_code
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.resource_spec_shrink):
            body['ResourceSpec'] = request.resource_spec_shrink
        if not UtilClient.is_unset(request.use_promotion_code):
            body['UsePromotionCode'] = request.use_promotion_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryModifyInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryModifyInstancePriceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryModifyInstancePriceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_modify_instance_price(
        self,
        request: foasconsole_20211028_models.QueryModifyInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryModifyInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例修改资源规格的价格
        
        @param request: QueryModifyInstancePriceRequest
        @return: QueryModifyInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_modify_instance_price_with_options(request, runtime)

    async def query_modify_instance_price_async(
        self,
        request: foasconsole_20211028_models.QueryModifyInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryModifyInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例修改资源规格的价格
        
        @param request: QueryModifyInstancePriceRequest
        @return: QueryModifyInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_modify_instance_price_with_options_async(request, runtime)

    def query_renew_instance_price_with_options(
        self,
        request: foasconsole_20211028_models.QueryRenewInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryRenewInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例续费价格
        
        @param request: QueryRenewInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRenewInstancePriceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRenewInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryRenewInstancePriceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryRenewInstancePriceResponse(),
                self.execute(params, req, runtime)
            )

    async def query_renew_instance_price_with_options_async(
        self,
        request: foasconsole_20211028_models.QueryRenewInstancePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.QueryRenewInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例续费价格
        
        @param request: QueryRenewInstancePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRenewInstancePriceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRenewInstancePrice',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryRenewInstancePriceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.QueryRenewInstancePriceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_renew_instance_price(
        self,
        request: foasconsole_20211028_models.QueryRenewInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryRenewInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例续费价格
        
        @param request: QueryRenewInstancePriceRequest
        @return: QueryRenewInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_renew_instance_price_with_options(request, runtime)

    async def query_renew_instance_price_async(
        self,
        request: foasconsole_20211028_models.QueryRenewInstancePriceRequest,
    ) -> foasconsole_20211028_models.QueryRenewInstancePriceResponse:
        """
        @summary 查询付费类型为包年包月的实例续费价格
        
        @param request: QueryRenewInstancePriceRequest
        @return: QueryRenewInstancePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_renew_instance_price_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: foasconsole_20211028_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.RenewInstanceResponse:
        """
        @summary 续费
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.RenewInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.RenewInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def renew_instance_with_options_async(
        self,
        request: foasconsole_20211028_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.RenewInstanceResponse:
        """
        @summary 续费
        
        @param request: RenewInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pricing_cycle):
            body['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.RenewInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.RenewInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def renew_instance(
        self,
        request: foasconsole_20211028_models.RenewInstanceRequest,
    ) -> foasconsole_20211028_models.RenewInstanceResponse:
        """
        @summary 续费
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: foasconsole_20211028_models.RenewInstanceRequest,
    ) -> foasconsole_20211028_models.RenewInstanceResponse:
        """
        @summary 续费
        
        @param request: RenewInstanceRequest
        @return: RenewInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: foasconsole_20211028_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: foasconsole_20211028_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: foasconsole_20211028_models.TagResourcesRequest,
    ) -> foasconsole_20211028_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: foasconsole_20211028_models.TagResourcesRequest,
    ) -> foasconsole_20211028_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: foasconsole_20211028_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.UntagResourcesResponse:
        """
        @summary flinkasi去标签
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: foasconsole_20211028_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> foasconsole_20211028_models.UntagResourcesResponse:
        """
        @summary flinkasi去标签
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2021-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                foasconsole_20211028_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                foasconsole_20211028_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: foasconsole_20211028_models.UntagResourcesRequest,
    ) -> foasconsole_20211028_models.UntagResourcesResponse:
        """
        @summary flinkasi去标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: foasconsole_20211028_models.UntagResourcesRequest,
    ) -> foasconsole_20211028_models.UntagResourcesResponse:
        """
        @summary flinkasi去标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
