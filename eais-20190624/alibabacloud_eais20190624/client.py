# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eais20190624 import models as eais_20190624_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-1': 'eais.aliyuncs.com',
            'ap-northeast-2-pop': 'eais.aliyuncs.com',
            'ap-south-1': 'eais.aliyuncs.com',
            'ap-southeast-1': 'eais.aliyuncs.com',
            'ap-southeast-2': 'eais.aliyuncs.com',
            'ap-southeast-3': 'eais.aliyuncs.com',
            'ap-southeast-5': 'eais.aliyuncs.com',
            'cn-beijing-finance-1': 'eais.aliyuncs.com',
            'cn-beijing-finance-pop': 'eais.aliyuncs.com',
            'cn-beijing-gov-1': 'eais.aliyuncs.com',
            'cn-beijing-nu16-b01': 'eais.aliyuncs.com',
            'cn-edge-1': 'eais.aliyuncs.com',
            'cn-fujian': 'eais.aliyuncs.com',
            'cn-haidian-cm12-c01': 'eais.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'eais.aliyuncs.com',
            'cn-hangzhou-finance': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'eais.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'eais.aliyuncs.com',
            'cn-hangzhou-test-306': 'eais.aliyuncs.com',
            'cn-hongkong': 'eais.aliyuncs.com',
            'cn-hongkong-finance-pop': 'eais.aliyuncs.com',
            'cn-huhehaote': 'eais.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'eais.aliyuncs.com',
            'cn-north-2-gov-1': 'eais.aliyuncs.com',
            'cn-qingdao': 'eais.aliyuncs.com',
            'cn-qingdao-nebula': 'eais.aliyuncs.com',
            'cn-shanghai-et15-b01': 'eais.aliyuncs.com',
            'cn-shanghai-et2-b01': 'eais.aliyuncs.com',
            'cn-shanghai-finance-1': 'eais.aliyuncs.com',
            'cn-shanghai-inner': 'eais.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'eais.aliyuncs.com',
            'cn-shenzhen-finance-1': 'eais.aliyuncs.com',
            'cn-shenzhen-inner': 'eais.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'eais.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'eais.aliyuncs.com',
            'cn-wuhan': 'eais.aliyuncs.com',
            'cn-wulanchabu': 'eais.aliyuncs.com',
            'cn-yushanfang': 'eais.aliyuncs.com',
            'cn-zhangbei': 'eais.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'eais.aliyuncs.com',
            'cn-zhangjiakou': 'eais.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'eais.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'eais.aliyuncs.com',
            'eu-central-1': 'eais.aliyuncs.com',
            'eu-west-1': 'eais.aliyuncs.com',
            'eu-west-1-oxs': 'eais.aliyuncs.com',
            'me-east-1': 'eais.aliyuncs.com',
            'rus-west-1-pop': 'eais.aliyuncs.com',
            'us-east-1': 'eais.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('eais', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_eai_with_options(
        self,
        request: eais_20190624_models.AttachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.AttachEaiResponse:
        """
        @summary 将弹性加速计算实例挂载到ECS实例上
        
        @param request: AttachEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachEai',
            version='2019-06-24',
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
                eais_20190624_models.AttachEaiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.AttachEaiResponse(),
                self.execute(params, req, runtime)
            )

    async def attach_eai_with_options_async(
        self,
        request: eais_20190624_models.AttachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.AttachEaiResponse:
        """
        @summary 将弹性加速计算实例挂载到ECS实例上
        
        @param request: AttachEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachEai',
            version='2019-06-24',
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
                eais_20190624_models.AttachEaiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.AttachEaiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def attach_eai(
        self,
        request: eais_20190624_models.AttachEaiRequest,
    ) -> eais_20190624_models.AttachEaiResponse:
        """
        @summary 将弹性加速计算实例挂载到ECS实例上
        
        @param request: AttachEaiRequest
        @return: AttachEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_eai_with_options(request, runtime)

    async def attach_eai_async(
        self,
        request: eais_20190624_models.AttachEaiRequest,
    ) -> eais_20190624_models.AttachEaiResponse:
        """
        @summary 将弹性加速计算实例挂载到ECS实例上
        
        @param request: AttachEaiRequest
        @return: AttachEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_eai_with_options_async(request, runtime)

    def attach_eais_ei_with_options(
        self,
        request: eais_20190624_models.AttachEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.AttachEaisEiResponse:
        """
        @summary 将EI绑定到ECS或ECI实例上
        
        @param request: AttachEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.ei_instance_type):
            query['EiInstanceType'] = request.ei_instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.AttachEaisEiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.AttachEaisEiResponse(),
                self.execute(params, req, runtime)
            )

    async def attach_eais_ei_with_options_async(
        self,
        request: eais_20190624_models.AttachEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.AttachEaisEiResponse:
        """
        @summary 将EI绑定到ECS或ECI实例上
        
        @param request: AttachEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.ei_instance_type):
            query['EiInstanceType'] = request.ei_instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.AttachEaisEiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.AttachEaisEiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def attach_eais_ei(
        self,
        request: eais_20190624_models.AttachEaisEiRequest,
    ) -> eais_20190624_models.AttachEaisEiResponse:
        """
        @summary 将EI绑定到ECS或ECI实例上
        
        @param request: AttachEaisEiRequest
        @return: AttachEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_eais_ei_with_options(request, runtime)

    async def attach_eais_ei_async(
        self,
        request: eais_20190624_models.AttachEaisEiRequest,
    ) -> eais_20190624_models.AttachEaisEiResponse:
        """
        @summary 将EI绑定到ECS或ECI实例上
        
        @param request: AttachEaisEiRequest
        @return: AttachEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_eais_ei_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: eais_20190624_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-06-24',
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
                eais_20190624_models.ChangeResourceGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.ChangeResourceGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def change_resource_group_with_options_async(
        self,
        request: eais_20190624_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-06-24',
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
                eais_20190624_models.ChangeResourceGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.ChangeResourceGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def change_resource_group(
        self,
        request: eais_20190624_models.ChangeResourceGroupRequest,
    ) -> eais_20190624_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: eais_20190624_models.ChangeResourceGroupRequest,
    ) -> eais_20190624_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_eai_with_options(
        self,
        request: eais_20190624_models.CreateEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEai',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiResponse(),
                self.execute(params, req, runtime)
            )

    async def create_eai_with_options_async(
        self,
        request: eais_20190624_models.CreateEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEai',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_eai(
        self,
        request: eais_20190624_models.CreateEaiRequest,
    ) -> eais_20190624_models.CreateEaiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaiRequest
        @return: CreateEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eai_with_options(request, runtime)

    async def create_eai_async(
        self,
        request: eais_20190624_models.CreateEaiRequest,
    ) -> eais_20190624_models.CreateEaiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaiRequest
        @return: CreateEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_with_options_async(request, runtime)

    def create_eai_eci_with_options(
        self,
        tmp_req: eais_20190624_models.CreateEaiEciRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiEciResponse:
        """
        @summary 创建一个EAIS实例和ECI实例并绑定
        
        @param tmp_req: CreateEaiEciRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiEciResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiEciShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.eci):
            request.eci_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.eci, 'Eci', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_name):
            query['EaisName'] = request.eais_name
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.eci_shrink):
            query['Eci'] = request.eci_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiEci',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiEciResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiEciResponse(),
                self.execute(params, req, runtime)
            )

    async def create_eai_eci_with_options_async(
        self,
        tmp_req: eais_20190624_models.CreateEaiEciRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiEciResponse:
        """
        @summary 创建一个EAIS实例和ECI实例并绑定
        
        @param tmp_req: CreateEaiEciRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiEciResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiEciShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.eci):
            request.eci_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.eci, 'Eci', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_name):
            query['EaisName'] = request.eais_name
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.eci_shrink):
            query['Eci'] = request.eci_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiEci',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiEciResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiEciResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_eai_eci(
        self,
        request: eais_20190624_models.CreateEaiEciRequest,
    ) -> eais_20190624_models.CreateEaiEciResponse:
        """
        @summary 创建一个EAIS实例和ECI实例并绑定
        
        @param request: CreateEaiEciRequest
        @return: CreateEaiEciResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eai_eci_with_options(request, runtime)

    async def create_eai_eci_async(
        self,
        request: eais_20190624_models.CreateEaiEciRequest,
    ) -> eais_20190624_models.CreateEaiEciResponse:
        """
        @summary 创建一个EAIS实例和ECI实例并绑定
        
        @param request: CreateEaiEciRequest
        @return: CreateEaiEciResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_eci_with_options_async(request, runtime)

    def create_eai_ecs_with_options(
        self,
        tmp_req: eais_20190624_models.CreateEaiEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiEcsResponse:
        """
        @summary 创建一个EAIS实例和ECS实例并绑定
        
        @param tmp_req: CreateEaiEcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiEcsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiEcsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ecs):
            request.ecs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ecs, 'Ecs', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_name):
            query['EaisName'] = request.eais_name
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.ecs_shrink):
            query['Ecs'] = request.ecs_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiEcs',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiEcsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiEcsResponse(),
                self.execute(params, req, runtime)
            )

    async def create_eai_ecs_with_options_async(
        self,
        tmp_req: eais_20190624_models.CreateEaiEcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiEcsResponse:
        """
        @summary 创建一个EAIS实例和ECS实例并绑定
        
        @param tmp_req: CreateEaiEcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiEcsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiEcsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ecs):
            request.ecs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ecs, 'Ecs', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_name):
            query['EaisName'] = request.eais_name
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.ecs_shrink):
            query['Ecs'] = request.ecs_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiEcs',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiEcsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiEcsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_eai_ecs(
        self,
        request: eais_20190624_models.CreateEaiEcsRequest,
    ) -> eais_20190624_models.CreateEaiEcsResponse:
        """
        @summary 创建一个EAIS实例和ECS实例并绑定
        
        @param request: CreateEaiEcsRequest
        @return: CreateEaiEcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eai_ecs_with_options(request, runtime)

    async def create_eai_ecs_async(
        self,
        request: eais_20190624_models.CreateEaiEcsRequest,
    ) -> eais_20190624_models.CreateEaiEcsResponse:
        """
        @summary 创建一个EAIS实例和ECS实例并绑定
        
        @param request: CreateEaiEcsRequest
        @return: CreateEaiEcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_ecs_with_options_async(request, runtime)

    def create_eai_jupyter_with_options(
        self,
        tmp_req: eais_20190624_models.CreateEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        """
        @summary 创建一个EAIS Jupyter环境
        
        @param tmp_req: CreateEaiJupyterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiJupyterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiJupyterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment_var):
            request.environment_var_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment_var, 'EnvironmentVar', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_name):
            query['EaisName'] = request.eais_name
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.environment_var_shrink):
            query['EnvironmentVar'] = request.environment_var_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiJupyter',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiJupyterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiJupyterResponse(),
                self.execute(params, req, runtime)
            )

    async def create_eai_jupyter_with_options_async(
        self,
        tmp_req: eais_20190624_models.CreateEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        """
        @summary 创建一个EAIS Jupyter环境
        
        @param tmp_req: CreateEaiJupyterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaiJupyterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiJupyterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment_var):
            request.environment_var_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment_var, 'EnvironmentVar', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_name):
            query['EaisName'] = request.eais_name
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.environment_var_shrink):
            query['EnvironmentVar'] = request.environment_var_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiJupyter',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaiJupyterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaiJupyterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_eai_jupyter(
        self,
        request: eais_20190624_models.CreateEaiJupyterRequest,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        """
        @summary 创建一个EAIS Jupyter环境
        
        @param request: CreateEaiJupyterRequest
        @return: CreateEaiJupyterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eai_jupyter_with_options(request, runtime)

    async def create_eai_jupyter_async(
        self,
        request: eais_20190624_models.CreateEaiJupyterRequest,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        """
        @summary 创建一个EAIS Jupyter环境
        
        @param request: CreateEaiJupyterRequest
        @return: CreateEaiJupyterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_jupyter_with_options_async(request, runtime)

    def create_eais_ei_with_options(
        self,
        request: eais_20190624_models.CreateEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaisEiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaisEiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaisEiResponse(),
                self.execute(params, req, runtime)
            )

    async def create_eais_ei_with_options_async(
        self,
        request: eais_20190624_models.CreateEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaisEiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.CreateEaisEiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.CreateEaisEiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_eais_ei(
        self,
        request: eais_20190624_models.CreateEaisEiRequest,
    ) -> eais_20190624_models.CreateEaisEiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaisEiRequest
        @return: CreateEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eais_ei_with_options(request, runtime)

    async def create_eais_ei_async(
        self,
        request: eais_20190624_models.CreateEaisEiRequest,
    ) -> eais_20190624_models.CreateEaisEiResponse:
        """
        @summary 创建一个弹性加速计算实例
        
        @param request: CreateEaisEiRequest
        @return: CreateEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eais_ei_with_options_async(request, runtime)

    def delete_eai_with_options(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiResponse:
        """
        @summary 释放一个弹性加速计算实例
        
        @param request: DeleteEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEai',
            version='2019-06-24',
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
                eais_20190624_models.DeleteEaiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DeleteEaiResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_eai_with_options_async(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiResponse:
        """
        @summary 释放一个弹性加速计算实例
        
        @param request: DeleteEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEai',
            version='2019-06-24',
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
                eais_20190624_models.DeleteEaiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DeleteEaiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_eai(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
    ) -> eais_20190624_models.DeleteEaiResponse:
        """
        @summary 释放一个弹性加速计算实例
        
        @param request: DeleteEaiRequest
        @return: DeleteEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_with_options(request, runtime)

    async def delete_eai_async(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
    ) -> eais_20190624_models.DeleteEaiResponse:
        """
        @summary 释放一个弹性加速计算实例
        
        @param request: DeleteEaiRequest
        @return: DeleteEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_eai_with_options_async(request, runtime)

    def delete_eai_all_with_options(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        """
        @summary 释放一个弹性加速计算实例以及与其绑定的ECS或ECI实例
        
        @param request: DeleteEaiAllRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEaiAllResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEaiAll',
            version='2019-06-24',
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
                eais_20190624_models.DeleteEaiAllResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DeleteEaiAllResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_eai_all_with_options_async(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        """
        @summary 释放一个弹性加速计算实例以及与其绑定的ECS或ECI实例
        
        @param request: DeleteEaiAllRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEaiAllResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEaiAll',
            version='2019-06-24',
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
                eais_20190624_models.DeleteEaiAllResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DeleteEaiAllResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_eai_all(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        """
        @summary 释放一个弹性加速计算实例以及与其绑定的ECS或ECI实例
        
        @param request: DeleteEaiAllRequest
        @return: DeleteEaiAllResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_all_with_options(request, runtime)

    async def delete_eai_all_async(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        """
        @summary 释放一个弹性加速计算实例以及与其绑定的ECS或ECI实例
        
        @param request: DeleteEaiAllRequest
        @return: DeleteEaiAllResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_eai_all_with_options_async(request, runtime)

    def delete_eais_ei_with_options(
        self,
        request: eais_20190624_models.DeleteEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaisEiResponse:
        """
        @summary 释放弹性加速计算实例
        
        @param request: DeleteEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.DeleteEaisEiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DeleteEaisEiResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_eais_ei_with_options_async(
        self,
        request: eais_20190624_models.DeleteEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaisEiResponse:
        """
        @summary 释放弹性加速计算实例
        
        @param request: DeleteEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.DeleteEaisEiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DeleteEaisEiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_eais_ei(
        self,
        request: eais_20190624_models.DeleteEaisEiRequest,
    ) -> eais_20190624_models.DeleteEaisEiResponse:
        """
        @summary 释放弹性加速计算实例
        
        @param request: DeleteEaisEiRequest
        @return: DeleteEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_eais_ei_with_options(request, runtime)

    async def delete_eais_ei_async(
        self,
        request: eais_20190624_models.DeleteEaisEiRequest,
    ) -> eais_20190624_models.DeleteEaisEiResponse:
        """
        @summary 释放弹性加速计算实例
        
        @param request: DeleteEaisEiRequest
        @return: DeleteEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_eais_ei_with_options_async(request, runtime)

    def describe_eais_with_options(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeEaisResponse:
        """
        @summary 查询一个或多个弹性加速计算实例的详细信息
        
        @param request: DescribeEaisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEaisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.elastic_accelerated_instance_ids):
            query['ElasticAcceleratedInstanceIds'] = request.elastic_accelerated_instance_ids
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEais',
            version='2019-06-24',
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
                eais_20190624_models.DescribeEaisResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DescribeEaisResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_eais_with_options_async(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeEaisResponse:
        """
        @summary 查询一个或多个弹性加速计算实例的详细信息
        
        @param request: DescribeEaisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEaisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_instance_id):
            query['ClientInstanceId'] = request.client_instance_id
        if not UtilClient.is_unset(request.elastic_accelerated_instance_ids):
            query['ElasticAcceleratedInstanceIds'] = request.elastic_accelerated_instance_ids
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEais',
            version='2019-06-24',
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
                eais_20190624_models.DescribeEaisResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DescribeEaisResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_eais(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
    ) -> eais_20190624_models.DescribeEaisResponse:
        """
        @summary 查询一个或多个弹性加速计算实例的详细信息
        
        @param request: DescribeEaisRequest
        @return: DescribeEaisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_eais_with_options(request, runtime)

    async def describe_eais_async(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
    ) -> eais_20190624_models.DescribeEaisResponse:
        """
        @summary 查询一个或多个弹性加速计算实例的详细信息
        
        @param request: DescribeEaisRequest
        @return: DescribeEaisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_eais_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeRegionsResponse:
        """
        @summary 查询您可以使用的阿里云地域
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-06-24',
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
                eais_20190624_models.DescribeRegionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DescribeRegionsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeRegionsResponse:
        """
        @summary 查询您可以使用的阿里云地域
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-06-24',
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
                eais_20190624_models.DescribeRegionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DescribeRegionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_regions(self) -> eais_20190624_models.DescribeRegionsResponse:
        """
        @summary 查询您可以使用的阿里云地域
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> eais_20190624_models.DescribeRegionsResponse:
        """
        @summary 查询您可以使用的阿里云地域
        
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def detach_eai_with_options(
        self,
        request: eais_20190624_models.DetachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaiResponse:
        """
        @summary 从ECS实例上卸载弹性加速计算实例
        
        @param request: DetachEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachEai',
            version='2019-06-24',
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
                eais_20190624_models.DetachEaiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DetachEaiResponse(),
                self.execute(params, req, runtime)
            )

    async def detach_eai_with_options_async(
        self,
        request: eais_20190624_models.DetachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaiResponse:
        """
        @summary 从ECS实例上卸载弹性加速计算实例
        
        @param request: DetachEaiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachEaiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.elastic_accelerated_instance_id):
            query['ElasticAcceleratedInstanceId'] = request.elastic_accelerated_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachEai',
            version='2019-06-24',
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
                eais_20190624_models.DetachEaiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DetachEaiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def detach_eai(
        self,
        request: eais_20190624_models.DetachEaiRequest,
    ) -> eais_20190624_models.DetachEaiResponse:
        """
        @summary 从ECS实例上卸载弹性加速计算实例
        
        @param request: DetachEaiRequest
        @return: DetachEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_eai_with_options(request, runtime)

    async def detach_eai_async(
        self,
        request: eais_20190624_models.DetachEaiRequest,
    ) -> eais_20190624_models.DetachEaiResponse:
        """
        @summary 从ECS实例上卸载弹性加速计算实例
        
        @param request: DetachEaiRequest
        @return: DetachEaiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_eai_with_options_async(request, runtime)

    def detach_eais_ei_with_options(
        self,
        request: eais_20190624_models.DetachEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaisEiResponse:
        """
        @summary 将EI实例与ECS或ECI实例解绑
        
        @param request: DetachEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.DetachEaisEiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DetachEaisEiResponse(),
                self.execute(params, req, runtime)
            )

    async def detach_eais_ei_with_options_async(
        self,
        request: eais_20190624_models.DetachEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaisEiResponse:
        """
        @summary 将EI实例与ECS或ECI实例解绑
        
        @param request: DetachEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.DetachEaisEiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.DetachEaisEiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def detach_eais_ei(
        self,
        request: eais_20190624_models.DetachEaisEiRequest,
    ) -> eais_20190624_models.DetachEaisEiResponse:
        """
        @summary 将EI实例与ECS或ECI实例解绑
        
        @param request: DetachEaisEiRequest
        @return: DetachEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_eais_ei_with_options(request, runtime)

    async def detach_eais_ei_async(
        self,
        request: eais_20190624_models.DetachEaisEiRequest,
    ) -> eais_20190624_models.DetachEaisEiResponse:
        """
        @summary 将EI实例与ECS或ECI实例解绑
        
        @param request: DetachEaisEiRequest
        @return: DetachEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_eais_ei_with_options_async(request, runtime)

    def get_instance_metrics_with_options(
        self,
        request: eais_20190624_models.GetInstanceMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.GetInstanceMetricsResponse:
        """
        @summary 获取EAIS实例级别的监控数据
        
        @param request: GetInstanceMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceMetrics',
            version='2019-06-24',
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
                eais_20190624_models.GetInstanceMetricsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.GetInstanceMetricsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_instance_metrics_with_options_async(
        self,
        request: eais_20190624_models.GetInstanceMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.GetInstanceMetricsResponse:
        """
        @summary 获取EAIS实例级别的监控数据
        
        @param request: GetInstanceMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_step):
            query['TimeStep'] = request.time_step
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceMetrics',
            version='2019-06-24',
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
                eais_20190624_models.GetInstanceMetricsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.GetInstanceMetricsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_instance_metrics(
        self,
        request: eais_20190624_models.GetInstanceMetricsRequest,
    ) -> eais_20190624_models.GetInstanceMetricsResponse:
        """
        @summary 获取EAIS实例级别的监控数据
        
        @param request: GetInstanceMetricsRequest
        @return: GetInstanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_metrics_with_options(request, runtime)

    async def get_instance_metrics_async(
        self,
        request: eais_20190624_models.GetInstanceMetricsRequest,
    ) -> eais_20190624_models.GetInstanceMetricsResponse:
        """
        @summary 获取EAIS实例级别的监控数据
        
        @param request: GetInstanceMetricsRequest
        @return: GetInstanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_metrics_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: eais_20190624_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.ListTagResourcesResponse:
        """
        @summary 查询标签列表
        
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
            version='2019-06-24',
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
                eais_20190624_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: eais_20190624_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.ListTagResourcesResponse:
        """
        @summary 查询标签列表
        
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
            version='2019-06-24',
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
                eais_20190624_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: eais_20190624_models.ListTagResourcesRequest,
    ) -> eais_20190624_models.ListTagResourcesResponse:
        """
        @summary 查询标签列表
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: eais_20190624_models.ListTagResourcesRequest,
    ) -> eais_20190624_models.ListTagResourcesResponse:
        """
        @summary 查询标签列表
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def start_eai_jupyter_with_options(
        self,
        request: eais_20190624_models.StartEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StartEaiJupyterResponse:
        """
        @summary 启动一个部署了notebook的弹性加速计算实例
        
        @param request: StartEaiJupyterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEaiJupyterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEaiJupyter',
            version='2019-06-24',
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
                eais_20190624_models.StartEaiJupyterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StartEaiJupyterResponse(),
                self.execute(params, req, runtime)
            )

    async def start_eai_jupyter_with_options_async(
        self,
        request: eais_20190624_models.StartEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StartEaiJupyterResponse:
        """
        @summary 启动一个部署了notebook的弹性加速计算实例
        
        @param request: StartEaiJupyterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEaiJupyterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEaiJupyter',
            version='2019-06-24',
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
                eais_20190624_models.StartEaiJupyterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StartEaiJupyterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_eai_jupyter(
        self,
        request: eais_20190624_models.StartEaiJupyterRequest,
    ) -> eais_20190624_models.StartEaiJupyterResponse:
        """
        @summary 启动一个部署了notebook的弹性加速计算实例
        
        @param request: StartEaiJupyterRequest
        @return: StartEaiJupyterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_eai_jupyter_with_options(request, runtime)

    async def start_eai_jupyter_async(
        self,
        request: eais_20190624_models.StartEaiJupyterRequest,
    ) -> eais_20190624_models.StartEaiJupyterResponse:
        """
        @summary 启动一个部署了notebook的弹性加速计算实例
        
        @param request: StartEaiJupyterRequest
        @return: StartEaiJupyterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_eai_jupyter_with_options_async(request, runtime)

    def start_eais_ei_with_options(
        self,
        request: eais_20190624_models.StartEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StartEaisEiResponse:
        """
        @summary 启动一个弹性加速计算实例
        
        @param request: StartEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.StartEaisEiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StartEaisEiResponse(),
                self.execute(params, req, runtime)
            )

    async def start_eais_ei_with_options_async(
        self,
        request: eais_20190624_models.StartEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StartEaisEiResponse:
        """
        @summary 启动一个弹性加速计算实例
        
        @param request: StartEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.StartEaisEiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StartEaisEiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def start_eais_ei(
        self,
        request: eais_20190624_models.StartEaisEiRequest,
    ) -> eais_20190624_models.StartEaisEiResponse:
        """
        @summary 启动一个弹性加速计算实例
        
        @param request: StartEaisEiRequest
        @return: StartEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_eais_ei_with_options(request, runtime)

    async def start_eais_ei_async(
        self,
        request: eais_20190624_models.StartEaisEiRequest,
    ) -> eais_20190624_models.StartEaisEiResponse:
        """
        @summary 启动一个弹性加速计算实例
        
        @param request: StartEaisEiRequest
        @return: StartEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_eais_ei_with_options_async(request, runtime)

    def stop_eai_jupyter_with_options(
        self,
        request: eais_20190624_models.StopEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StopEaiJupyterResponse:
        """
        @summary 停止一个部署了notebook的弹性加速计算实例
        
        @param request: StopEaiJupyterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopEaiJupyterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopEaiJupyter',
            version='2019-06-24',
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
                eais_20190624_models.StopEaiJupyterResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StopEaiJupyterResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_eai_jupyter_with_options_async(
        self,
        request: eais_20190624_models.StopEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StopEaiJupyterResponse:
        """
        @summary 停止一个部署了notebook的弹性加速计算实例
        
        @param request: StopEaiJupyterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopEaiJupyterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopEaiJupyter',
            version='2019-06-24',
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
                eais_20190624_models.StopEaiJupyterResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StopEaiJupyterResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_eai_jupyter(
        self,
        request: eais_20190624_models.StopEaiJupyterRequest,
    ) -> eais_20190624_models.StopEaiJupyterResponse:
        """
        @summary 停止一个部署了notebook的弹性加速计算实例
        
        @param request: StopEaiJupyterRequest
        @return: StopEaiJupyterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_eai_jupyter_with_options(request, runtime)

    async def stop_eai_jupyter_async(
        self,
        request: eais_20190624_models.StopEaiJupyterRequest,
    ) -> eais_20190624_models.StopEaiJupyterResponse:
        """
        @summary 停止一个部署了notebook的弹性加速计算实例
        
        @param request: StopEaiJupyterRequest
        @return: StopEaiJupyterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_eai_jupyter_with_options_async(request, runtime)

    def stop_eais_ei_with_options(
        self,
        request: eais_20190624_models.StopEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StopEaisEiResponse:
        """
        @summary 停止一个弹性加速计算实例
        
        @param request: StopEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.StopEaisEiResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StopEaisEiResponse(),
                self.execute(params, req, runtime)
            )

    async def stop_eais_ei_with_options_async(
        self,
        request: eais_20190624_models.StopEaisEiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.StopEaisEiResponse:
        """
        @summary 停止一个弹性加速计算实例
        
        @param request: StopEaisEiRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopEaisEiResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ei_instance_id):
            query['EiInstanceId'] = request.ei_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopEaisEi',
            version='2019-06-24',
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
                eais_20190624_models.StopEaisEiResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.StopEaisEiResponse(),
                await self.execute_async(params, req, runtime)
            )

    def stop_eais_ei(
        self,
        request: eais_20190624_models.StopEaisEiRequest,
    ) -> eais_20190624_models.StopEaisEiResponse:
        """
        @summary 停止一个弹性加速计算实例
        
        @param request: StopEaisEiRequest
        @return: StopEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_eais_ei_with_options(request, runtime)

    async def stop_eais_ei_async(
        self,
        request: eais_20190624_models.StopEaisEiRequest,
    ) -> eais_20190624_models.StopEaisEiResponse:
        """
        @summary 停止一个弹性加速计算实例
        
        @param request: StopEaisEiRequest
        @return: StopEaisEiResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_eais_ei_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: eais_20190624_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.TagResourcesResponse:
        """
        @summary 为弹性加速计算实例创建并绑定标签
        
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
            version='2019-06-24',
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
                eais_20190624_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: eais_20190624_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.TagResourcesResponse:
        """
        @summary 为弹性加速计算实例创建并绑定标签
        
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
            version='2019-06-24',
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
                eais_20190624_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: eais_20190624_models.TagResourcesRequest,
    ) -> eais_20190624_models.TagResourcesResponse:
        """
        @summary 为弹性加速计算实例创建并绑定标签
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: eais_20190624_models.TagResourcesRequest,
    ) -> eais_20190624_models.TagResourcesResponse:
        """
        @summary 为弹性加速计算实例创建并绑定标签
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: eais_20190624_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.UntagResourcesResponse:
        """
        @summary 解绑并删除标签
        
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
            version='2019-06-24',
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
                eais_20190624_models.UntagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.UntagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def untag_resources_with_options_async(
        self,
        request: eais_20190624_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.UntagResourcesResponse:
        """
        @summary 解绑并删除标签
        
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
            version='2019-06-24',
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
                eais_20190624_models.UntagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                eais_20190624_models.UntagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def untag_resources(
        self,
        request: eais_20190624_models.UntagResourcesRequest,
    ) -> eais_20190624_models.UntagResourcesResponse:
        """
        @summary 解绑并删除标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: eais_20190624_models.UntagResourcesRequest,
    ) -> eais_20190624_models.UntagResourcesResponse:
        """
        @summary 解绑并删除标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
