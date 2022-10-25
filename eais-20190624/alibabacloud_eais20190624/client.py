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
        return TeaCore.from_map(
            eais_20190624_models.AttachEaiResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_eai_with_options_async(
        self,
        request: eais_20190624_models.AttachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.AttachEaiResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.AttachEaiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_eai(
        self,
        request: eais_20190624_models.AttachEaiRequest,
    ) -> eais_20190624_models.AttachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_eai_with_options(request, runtime)

    async def attach_eai_async(
        self,
        request: eais_20190624_models.AttachEaiRequest,
    ) -> eais_20190624_models.AttachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_eai_with_options_async(request, runtime)

    def create_eai_with_options(
        self,
        request: eais_20190624_models.CreateEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiResponse:
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
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
        return TeaCore.from_map(
            eais_20190624_models.CreateEaiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eai_with_options_async(
        self,
        request: eais_20190624_models.CreateEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiResponse:
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
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
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
        return TeaCore.from_map(
            eais_20190624_models.CreateEaiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eai(
        self,
        request: eais_20190624_models.CreateEaiRequest,
    ) -> eais_20190624_models.CreateEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_eai_with_options(request, runtime)

    async def create_eai_async(
        self,
        request: eais_20190624_models.CreateEaiRequest,
    ) -> eais_20190624_models.CreateEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_with_options_async(request, runtime)

    def create_eai_all_with_options(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_image_id):
            query['ClientImageId'] = request.client_image_id
        if not UtilClient.is_unset(request.client_instance_name):
            query['ClientInstanceName'] = request.client_instance_name
        if not UtilClient.is_unset(request.client_instance_type):
            query['ClientInstanceType'] = request.client_instance_type
        if not UtilClient.is_unset(request.client_internet_max_bandwidth_in):
            query['ClientInternetMaxBandwidthIn'] = request.client_internet_max_bandwidth_in
        if not UtilClient.is_unset(request.client_internet_max_bandwidth_out):
            query['ClientInternetMaxBandwidthOut'] = request.client_internet_max_bandwidth_out
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_security_group_id):
            query['ClientSecurityGroupId'] = request.client_security_group_id
        if not UtilClient.is_unset(request.client_system_disk_category):
            query['ClientSystemDiskCategory'] = request.client_system_disk_category
        if not UtilClient.is_unset(request.client_system_disk_size):
            query['ClientSystemDiskSize'] = request.client_system_disk_size
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_vswitch_id):
            query['ClientVSwitchId'] = request.client_vswitch_id
        if not UtilClient.is_unset(request.client_zone_id):
            query['ClientZoneId'] = request.client_zone_id
        if not UtilClient.is_unset(request.eai_instance_type):
            query['EaiInstanceType'] = request.eai_instance_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiAll',
            version='2019-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eais_20190624_models.CreateEaiAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eai_all_with_options_async(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_image_id):
            query['ClientImageId'] = request.client_image_id
        if not UtilClient.is_unset(request.client_instance_name):
            query['ClientInstanceName'] = request.client_instance_name
        if not UtilClient.is_unset(request.client_instance_type):
            query['ClientInstanceType'] = request.client_instance_type
        if not UtilClient.is_unset(request.client_internet_max_bandwidth_in):
            query['ClientInternetMaxBandwidthIn'] = request.client_internet_max_bandwidth_in
        if not UtilClient.is_unset(request.client_internet_max_bandwidth_out):
            query['ClientInternetMaxBandwidthOut'] = request.client_internet_max_bandwidth_out
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_security_group_id):
            query['ClientSecurityGroupId'] = request.client_security_group_id
        if not UtilClient.is_unset(request.client_system_disk_category):
            query['ClientSystemDiskCategory'] = request.client_system_disk_category
        if not UtilClient.is_unset(request.client_system_disk_size):
            query['ClientSystemDiskSize'] = request.client_system_disk_size
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.client_vswitch_id):
            query['ClientVSwitchId'] = request.client_vswitch_id
        if not UtilClient.is_unset(request.client_zone_id):
            query['ClientZoneId'] = request.client_zone_id
        if not UtilClient.is_unset(request.eai_instance_type):
            query['EaiInstanceType'] = request.eai_instance_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEaiAll',
            version='2019-06-24',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eais_20190624_models.CreateEaiAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eai_all(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_eai_all_with_options(request, runtime)

    async def create_eai_all_async(
        self,
        request: eais_20190624_models.CreateEaiAllRequest,
    ) -> eais_20190624_models.CreateEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_all_with_options_async(request, runtime)

    def create_eai_jupyter_with_options(
        self,
        tmp_req: eais_20190624_models.CreateEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiJupyterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment_var):
            request.environment_var_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment_var, 'EnvironmentVar', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.environment_var_shrink):
            query['EnvironmentVar'] = request.environment_var_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
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
        return TeaCore.from_map(
            eais_20190624_models.CreateEaiJupyterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eai_jupyter_with_options_async(
        self,
        tmp_req: eais_20190624_models.CreateEaiJupyterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        UtilClient.validate_model(tmp_req)
        request = eais_20190624_models.CreateEaiJupyterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.environment_var):
            request.environment_var_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.environment_var, 'EnvironmentVar', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.eais_type):
            query['EaisType'] = request.eais_type
        if not UtilClient.is_unset(request.environment_var_shrink):
            query['EnvironmentVar'] = request.environment_var_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
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
        return TeaCore.from_map(
            eais_20190624_models.CreateEaiJupyterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eai_jupyter(
        self,
        request: eais_20190624_models.CreateEaiJupyterRequest,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_eai_jupyter_with_options(request, runtime)

    async def create_eai_jupyter_async(
        self,
        request: eais_20190624_models.CreateEaiJupyterRequest,
    ) -> eais_20190624_models.CreateEaiJupyterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_eai_jupyter_with_options_async(request, runtime)

    def delete_eai_with_options(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DeleteEaiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_eai_with_options_async(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DeleteEaiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_eai(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
    ) -> eais_20190624_models.DeleteEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_with_options(request, runtime)

    async def delete_eai_async(
        self,
        request: eais_20190624_models.DeleteEaiRequest,
    ) -> eais_20190624_models.DeleteEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_eai_with_options_async(request, runtime)

    def delete_eai_all_with_options(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DeleteEaiAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_eai_all_with_options_async(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DeleteEaiAllResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_eai_all(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_eai_all_with_options(request, runtime)

    async def delete_eai_all_async(
        self,
        request: eais_20190624_models.DeleteEaiAllRequest,
    ) -> eais_20190624_models.DeleteEaiAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_eai_all_with_options_async(request, runtime)

    def describe_eais_with_options(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeEaisResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
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
        return TeaCore.from_map(
            eais_20190624_models.DescribeEaisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eais_with_options_async(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeEaisResponse:
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
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
        return TeaCore.from_map(
            eais_20190624_models.DescribeEaisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eais(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
    ) -> eais_20190624_models.DescribeEaisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eais_with_options(request, runtime)

    async def describe_eais_async(
        self,
        request: eais_20190624_models.DescribeEaisRequest,
    ) -> eais_20190624_models.DescribeEaisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eais_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeRegionsResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DescribeRegionsResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> eais_20190624_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> eais_20190624_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def detach_eai_with_options(
        self,
        request: eais_20190624_models.DetachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaiResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DetachEaiResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_eai_with_options_async(
        self,
        request: eais_20190624_models.DetachEaiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eais_20190624_models.DetachEaiResponse:
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
        return TeaCore.from_map(
            eais_20190624_models.DetachEaiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_eai(
        self,
        request: eais_20190624_models.DetachEaiRequest,
    ) -> eais_20190624_models.DetachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_eai_with_options(request, runtime)

    async def detach_eai_async(
        self,
        request: eais_20190624_models.DetachEaiRequest,
    ) -> eais_20190624_models.DetachEaiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_eai_with_options_async(request, runtime)
