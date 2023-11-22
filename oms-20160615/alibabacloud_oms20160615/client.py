# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_oms20160615 import models as oms_20160615_models
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
        self._endpoint_map = {
            'ap-southeast-1': 'oms.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou': 'pre-oms.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('oms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_ready_flag_with_options(
        self,
        request: oms_20160615_models.CheckReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.CheckReadyFlagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycles):
            query['Cycles'] = request.cycles
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckReadyFlag',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.CheckReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_ready_flag_with_options_async(
        self,
        request: oms_20160615_models.CheckReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.CheckReadyFlagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycles):
            query['Cycles'] = request.cycles
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckReadyFlag',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.CheckReadyFlagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_ready_flag(
        self,
        request: oms_20160615_models.CheckReadyFlagRequest,
    ) -> oms_20160615_models.CheckReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_ready_flag_with_options(request, runtime)

    async def check_ready_flag_async(
        self,
        request: oms_20160615_models.CheckReadyFlagRequest,
    ) -> oms_20160615_models.CheckReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_ready_flag_with_options_async(request, runtime)

    def delete_domain_part_with_options(
        self,
        request: oms_20160615_models.DeleteDomainPartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.DeleteDomainPartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.part):
            query['Part'] = request.part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainPart',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.DeleteDomainPartResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_part_with_options_async(
        self,
        request: oms_20160615_models.DeleteDomainPartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.DeleteDomainPartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.part):
            query['Part'] = request.part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainPart',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.DeleteDomainPartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_part(
        self,
        request: oms_20160615_models.DeleteDomainPartRequest,
    ) -> oms_20160615_models.DeleteDomainPartResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_part_with_options(request, runtime)

    async def delete_domain_part_async(
        self,
        request: oms_20160615_models.DeleteDomainPartRequest,
    ) -> oms_20160615_models.DeleteDomainPartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_part_with_options_async(request, runtime)

    def delete_domain_part_by_proxy_with_options(
        self,
        request: oms_20160615_models.DeleteDomainPartByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.DeleteDomainPartByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.part):
            query['Part'] = request.part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainPartByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.DeleteDomainPartByProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_part_by_proxy_with_options_async(
        self,
        request: oms_20160615_models.DeleteDomainPartByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.DeleteDomainPartByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.part):
            query['Part'] = request.part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainPartByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.DeleteDomainPartByProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_part_by_proxy(
        self,
        request: oms_20160615_models.DeleteDomainPartByProxyRequest,
    ) -> oms_20160615_models.DeleteDomainPartByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_part_by_proxy_with_options(request, runtime)

    async def delete_domain_part_by_proxy_async(
        self,
        request: oms_20160615_models.DeleteDomainPartByProxyRequest,
    ) -> oms_20160615_models.DeleteDomainPartByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_part_by_proxy_with_options_async(request, runtime)

    def get_access_policy_config_with_options(
        self,
        request: oms_20160615_models.GetAccessPolicyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetAccessPolicyConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessPolicyConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetAccessPolicyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_policy_config_with_options_async(
        self,
        request: oms_20160615_models.GetAccessPolicyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetAccessPolicyConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessPolicyConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetAccessPolicyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_policy_config(
        self,
        request: oms_20160615_models.GetAccessPolicyConfigRequest,
    ) -> oms_20160615_models.GetAccessPolicyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_policy_config_with_options(request, runtime)

    async def get_access_policy_config_async(
        self,
        request: oms_20160615_models.GetAccessPolicyConfigRequest,
    ) -> oms_20160615_models.GetAccessPolicyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_policy_config_with_options_async(request, runtime)

    def get_domain_config_with_options(
        self,
        request: oms_20160615_models.GetDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_config_with_options_async(
        self,
        request: oms_20160615_models.GetDomainConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_config(
        self,
        request: oms_20160615_models.GetDomainConfigRequest,
    ) -> oms_20160615_models.GetDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_config_with_options(request, runtime)

    async def get_domain_config_async(
        self,
        request: oms_20160615_models.GetDomainConfigRequest,
    ) -> oms_20160615_models.GetDomainConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_config_with_options_async(request, runtime)

    def get_domain_part_with_options(
        self,
        request: oms_20160615_models.GetDomainPartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainPartResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainPart',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainPartResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_part_with_options_async(
        self,
        request: oms_20160615_models.GetDomainPartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainPartResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainPart',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainPartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_part(
        self,
        request: oms_20160615_models.GetDomainPartRequest,
    ) -> oms_20160615_models.GetDomainPartResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_part_with_options(request, runtime)

    async def get_domain_part_async(
        self,
        request: oms_20160615_models.GetDomainPartRequest,
    ) -> oms_20160615_models.GetDomainPartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_part_with_options_async(request, runtime)

    def get_domain_part_by_proxy_with_options(
        self,
        request: oms_20160615_models.GetDomainPartByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainPartByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compress_enable):
            query['CompressEnable'] = request.compress_enable
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.part):
            query['Part'] = request.part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainPartByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainPartByProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_part_by_proxy_with_options_async(
        self,
        request: oms_20160615_models.GetDomainPartByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainPartByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compress_enable):
            query['CompressEnable'] = request.compress_enable
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.part):
            query['Part'] = request.part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainPartByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainPartByProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_part_by_proxy(
        self,
        request: oms_20160615_models.GetDomainPartByProxyRequest,
    ) -> oms_20160615_models.GetDomainPartByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_part_by_proxy_with_options(request, runtime)

    async def get_domain_part_by_proxy_async(
        self,
        request: oms_20160615_models.GetDomainPartByProxyRequest,
    ) -> oms_20160615_models.GetDomainPartByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_part_by_proxy_with_options_async(request, runtime)

    def get_domain_part_config_with_options(
        self,
        request: oms_20160615_models.GetDomainPartConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainPartConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainPartConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainPartConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_part_config_with_options_async(
        self,
        request: oms_20160615_models.GetDomainPartConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetDomainPartConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainPartConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetDomainPartConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_part_config(
        self,
        request: oms_20160615_models.GetDomainPartConfigRequest,
    ) -> oms_20160615_models.GetDomainPartConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_domain_part_config_with_options(request, runtime)

    async def get_domain_part_config_async(
        self,
        request: oms_20160615_models.GetDomainPartConfigRequest,
    ) -> oms_20160615_models.GetDomainPartConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_part_config_with_options_async(request, runtime)

    def get_file_config_with_options(
        self,
        request: oms_20160615_models.GetFileConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetFileConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetFileConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_config_with_options_async(
        self,
        request: oms_20160615_models.GetFileConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetFileConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetFileConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_config(
        self,
        request: oms_20160615_models.GetFileConfigRequest,
    ) -> oms_20160615_models.GetFileConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_file_config_with_options(request, runtime)

    async def get_file_config_async(
        self,
        request: oms_20160615_models.GetFileConfigRequest,
    ) -> oms_20160615_models.GetFileConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_config_with_options_async(request, runtime)

    def get_increment_measure_data_by_proxy_with_options(
        self,
        request: oms_20160615_models.GetIncrementMeasureDataByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetIncrementMeasureDataByProxyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIncrementMeasureDataByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetIncrementMeasureDataByProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_increment_measure_data_by_proxy_with_options_async(
        self,
        request: oms_20160615_models.GetIncrementMeasureDataByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetIncrementMeasureDataByProxyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIncrementMeasureDataByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetIncrementMeasureDataByProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_increment_measure_data_by_proxy(
        self,
        request: oms_20160615_models.GetIncrementMeasureDataByProxyRequest,
    ) -> oms_20160615_models.GetIncrementMeasureDataByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_increment_measure_data_by_proxy_with_options(request, runtime)

    async def get_increment_measure_data_by_proxy_async(
        self,
        request: oms_20160615_models.GetIncrementMeasureDataByProxyRequest,
    ) -> oms_20160615_models.GetIncrementMeasureDataByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_increment_measure_data_by_proxy_with_options_async(request, runtime)

    def get_measure_data_with_options(
        self,
        request: oms_20160615_models.GetMeasureDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetMeasureDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compress_enable):
            query['CompressEnable'] = request.compress_enable
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_field):
            query['QueryField'] = request.query_field
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMeasureData',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetMeasureDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_measure_data_with_options_async(
        self,
        request: oms_20160615_models.GetMeasureDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetMeasureDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compress_enable):
            query['CompressEnable'] = request.compress_enable
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_field):
            query['QueryField'] = request.query_field
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMeasureData',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetMeasureDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_measure_data(
        self,
        request: oms_20160615_models.GetMeasureDataRequest,
    ) -> oms_20160615_models.GetMeasureDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_measure_data_with_options(request, runtime)

    async def get_measure_data_async(
        self,
        request: oms_20160615_models.GetMeasureDataRequest,
    ) -> oms_20160615_models.GetMeasureDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_measure_data_with_options_async(request, runtime)

    def get_open_api_config_with_options(
        self,
        request: oms_20160615_models.GetOpenApiConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetOpenApiConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpenApiConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetOpenApiConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_open_api_config_with_options_async(
        self,
        request: oms_20160615_models.GetOpenApiConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetOpenApiConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpenApiConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetOpenApiConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_open_api_config(
        self,
        request: oms_20160615_models.GetOpenApiConfigRequest,
    ) -> oms_20160615_models.GetOpenApiConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_open_api_config_with_options(request, runtime)

    async def get_open_api_config_async(
        self,
        request: oms_20160615_models.GetOpenApiConfigRequest,
    ) -> oms_20160615_models.GetOpenApiConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_open_api_config_with_options_async(request, runtime)

    def get_ready_flag_with_options(
        self,
        request: oms_20160615_models.GetReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetReadyFlagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReadyFlag',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ready_flag_with_options_async(
        self,
        request: oms_20160615_models.GetReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetReadyFlagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReadyFlag',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetReadyFlagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ready_flag(
        self,
        request: oms_20160615_models.GetReadyFlagRequest,
    ) -> oms_20160615_models.GetReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ready_flag_with_options(request, runtime)

    async def get_ready_flag_async(
        self,
        request: oms_20160615_models.GetReadyFlagRequest,
    ) -> oms_20160615_models.GetReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ready_flag_with_options_async(request, runtime)

    def get_ready_flag_alert_config_with_options(
        self,
        request: oms_20160615_models.GetReadyFlagAlertConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetReadyFlagAlertConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReadyFlagAlertConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetReadyFlagAlertConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ready_flag_alert_config_with_options_async(
        self,
        request: oms_20160615_models.GetReadyFlagAlertConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetReadyFlagAlertConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReadyFlagAlertConfig',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetReadyFlagAlertConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ready_flag_alert_config(
        self,
        request: oms_20160615_models.GetReadyFlagAlertConfigRequest,
    ) -> oms_20160615_models.GetReadyFlagAlertConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ready_flag_alert_config_with_options(request, runtime)

    async def get_ready_flag_alert_config_async(
        self,
        request: oms_20160615_models.GetReadyFlagAlertConfigRequest,
    ) -> oms_20160615_models.GetReadyFlagAlertConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ready_flag_alert_config_with_options_async(request, runtime)

    def get_ready_flag_by_proxy_with_options(
        self,
        request: oms_20160615_models.GetReadyFlagByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetReadyFlagByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compress_enable):
            query['CompressEnable'] = request.compress_enable
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReadyFlagByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetReadyFlagByProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ready_flag_by_proxy_with_options_async(
        self,
        request: oms_20160615_models.GetReadyFlagByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.GetReadyFlagByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compress_enable):
            query['CompressEnable'] = request.compress_enable
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReadyFlagByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.GetReadyFlagByProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ready_flag_by_proxy(
        self,
        request: oms_20160615_models.GetReadyFlagByProxyRequest,
    ) -> oms_20160615_models.GetReadyFlagByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ready_flag_by_proxy_with_options(request, runtime)

    async def get_ready_flag_by_proxy_async(
        self,
        request: oms_20160615_models.GetReadyFlagByProxyRequest,
    ) -> oms_20160615_models.GetReadyFlagByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ready_flag_by_proxy_with_options_async(request, runtime)

    def put_domain_part_with_options(
        self,
        request: oms_20160615_models.PutDomainPartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutDomainPartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDomainPart',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutDomainPartResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_domain_part_with_options_async(
        self,
        request: oms_20160615_models.PutDomainPartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutDomainPartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDomainPart',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutDomainPartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_domain_part(
        self,
        request: oms_20160615_models.PutDomainPartRequest,
    ) -> oms_20160615_models.PutDomainPartResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_domain_part_with_options(request, runtime)

    async def put_domain_part_async(
        self,
        request: oms_20160615_models.PutDomainPartRequest,
    ) -> oms_20160615_models.PutDomainPartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_domain_part_with_options_async(request, runtime)

    def put_domain_part_by_proxy_with_options(
        self,
        request: oms_20160615_models.PutDomainPartByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutDomainPartByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDomainPartByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutDomainPartByProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_domain_part_by_proxy_with_options_async(
        self,
        request: oms_20160615_models.PutDomainPartByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutDomainPartByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutDomainPartByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutDomainPartByProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_domain_part_by_proxy(
        self,
        request: oms_20160615_models.PutDomainPartByProxyRequest,
    ) -> oms_20160615_models.PutDomainPartByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_domain_part_by_proxy_with_options(request, runtime)

    async def put_domain_part_by_proxy_async(
        self,
        request: oms_20160615_models.PutDomainPartByProxyRequest,
    ) -> oms_20160615_models.PutDomainPartByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_domain_part_by_proxy_with_options_async(request, runtime)

    def put_measure_data_with_options(
        self,
        request: oms_20160615_models.PutMeasureDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutMeasureDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMeasureData',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutMeasureDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_measure_data_with_options_async(
        self,
        request: oms_20160615_models.PutMeasureDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutMeasureDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMeasureData',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutMeasureDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_measure_data(
        self,
        request: oms_20160615_models.PutMeasureDataRequest,
    ) -> oms_20160615_models.PutMeasureDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_measure_data_with_options(request, runtime)

    async def put_measure_data_async(
        self,
        request: oms_20160615_models.PutMeasureDataRequest,
    ) -> oms_20160615_models.PutMeasureDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_measure_data_with_options_async(request, runtime)

    def put_measure_data_by_proxy_with_options(
        self,
        request: oms_20160615_models.PutMeasureDataByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutMeasureDataByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMeasureDataByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutMeasureDataByProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_measure_data_by_proxy_with_options_async(
        self,
        request: oms_20160615_models.PutMeasureDataByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutMeasureDataByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutMeasureDataByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutMeasureDataByProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_measure_data_by_proxy(
        self,
        request: oms_20160615_models.PutMeasureDataByProxyRequest,
    ) -> oms_20160615_models.PutMeasureDataByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_measure_data_by_proxy_with_options(request, runtime)

    async def put_measure_data_by_proxy_async(
        self,
        request: oms_20160615_models.PutMeasureDataByProxyRequest,
    ) -> oms_20160615_models.PutMeasureDataByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_measure_data_by_proxy_with_options_async(request, runtime)

    def put_ready_flag_with_options(
        self,
        request: oms_20160615_models.PutReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutReadyFlagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutReadyFlag',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutReadyFlagResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_ready_flag_with_options_async(
        self,
        request: oms_20160615_models.PutReadyFlagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutReadyFlagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        if not UtilClient.is_unset(request.source_request_id):
            query['SourceRequestId'] = request.source_request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutReadyFlag',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutReadyFlagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_ready_flag(
        self,
        request: oms_20160615_models.PutReadyFlagRequest,
    ) -> oms_20160615_models.PutReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_ready_flag_with_options(request, runtime)

    async def put_ready_flag_async(
        self,
        request: oms_20160615_models.PutReadyFlagRequest,
    ) -> oms_20160615_models.PutReadyFlagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_ready_flag_with_options_async(request, runtime)

    def put_ready_flag_by_proxy_with_options(
        self,
        request: oms_20160615_models.PutReadyFlagByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutReadyFlagByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutReadyFlagByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutReadyFlagByProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_ready_flag_by_proxy_with_options_async(
        self,
        request: oms_20160615_models.PutReadyFlagByProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oms_20160615_models.PutReadyFlagByProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_type):
            query['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.compressed):
            query['Compressed'] = request.compressed
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.domain_code):
            query['DomainCode'] = request.domain_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutReadyFlagByProxy',
            version='2016-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            oms_20160615_models.PutReadyFlagByProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_ready_flag_by_proxy(
        self,
        request: oms_20160615_models.PutReadyFlagByProxyRequest,
    ) -> oms_20160615_models.PutReadyFlagByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_ready_flag_by_proxy_with_options(request, runtime)

    async def put_ready_flag_by_proxy_async(
        self,
        request: oms_20160615_models.PutReadyFlagByProxyRequest,
    ) -> oms_20160615_models.PutReadyFlagByProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_ready_flag_by_proxy_with_options_async(request, runtime)
