# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudapi20160201 import models as cloud_api20160201_models
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
            'cn-qingdao': 'apigateway.cn-qingdao.aliyuncs.com',
            'cn-beijing': 'apigateway.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'apigateway.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'apigateway.cn-huhehaote.aliyuncs.com',
            'cn-wulanchabu': 'apigateway.cn-wulanchabu.aliyuncs.com',
            'cn-hangzhou': 'apigateway.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'apigateway.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'apigateway.cn-shenzhen.aliyuncs.com',
            'cn-heyuan': 'apigateway.cn-heyuan.aliyuncs.com',
            'cn-guangzhou': 'apigateway.cn-guangzhou.aliyuncs.com',
            'cn-chengdu': 'apigateway.cn-chengdu.aliyuncs.com',
            'cn-hongkong': 'apigateway.cn-hongkong.aliyuncs.com',
            'ap-northeast-1': 'apigateway.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'apigateway.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'apigateway.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'apigateway.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'apigateway.ap-southeast-5.aliyuncs.com',
            'ap-southeast-6': 'apigateway.ap-southeast-6.aliyuncs.com',
            'ap-southeast-7': 'apigateway.ap-southeast-7.aliyuncs.com',
            'us-east-1': 'apigateway.us-east-1.aliyuncs.com',
            'us-west-1': 'apigateway.us-west-1.aliyuncs.com',
            'eu-west-1': 'apigateway.eu-west-1.aliyuncs.com',
            'eu-central-1': 'apigateway.eu-central-1.aliyuncs.com',
            'ap-south-1': 'apigateway.ap-south-1.aliyuncs.com',
            'me-east-1': 'apigateway.me-east-1.aliyuncs.com',
            'me-central-1': 'apigateway.me-central-1.aliyuncs.com',
            'cn-hangzhou-finance': 'apigateway.cn-hangzhou-finance.aliyuncs.com',
            'cn-shanghai-finance-1': 'apigateway.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shenzhen-finance-1': 'apigateway.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-north-2-gov-1': 'apigateway.cn-north-2-gov-1.aliyuncs.com',
            'ap-northeast-2-pop': 'apigateway.aliyuncs.com',
            'cn-beijing-finance-1': 'apigateway.cn-beijing-finance-1.aliyuncs.com',
            'cn-beijing-finance-pop': 'apigateway.aliyuncs.com',
            'cn-beijing-gov-1': 'apigateway.aliyuncs.com',
            'cn-beijing-nu16-b01': 'apigateway.aliyuncs.com',
            'cn-edge-1': 'apigateway.aliyuncs.com',
            'cn-fujian': 'apigateway.aliyuncs.com',
            'cn-haidian-cm12-c01': 'apigateway.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'apigateway.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'apigateway.aliyuncs.com',
            'cn-hangzhou-test-306': 'apigateway.aliyuncs.com',
            'cn-hongkong-finance-pop': 'apigateway.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'apigateway.aliyuncs.com',
            'cn-qingdao-nebula': 'apigateway.aliyuncs.com',
            'cn-shanghai-et15-b01': 'apigateway.aliyuncs.com',
            'cn-shanghai-et2-b01': 'apigateway.aliyuncs.com',
            'cn-shanghai-inner': 'apigateway.cn-shanghai-inner.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'apigateway.aliyuncs.com',
            'cn-shenzhen-inner': 'apigateway.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'apigateway.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'apigateway.aliyuncs.com',
            'cn-wuhan': 'apigateway.aliyuncs.com',
            'cn-yushanfang': 'apigateway.aliyuncs.com',
            'cn-zhangbei': 'apigateway.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'apigateway.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'apigateway.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'apigateway.aliyuncs.com',
            'eu-west-1-oxs': 'apigateway.aliyuncs.com',
            'rus-west-1-pop': 'apigateway.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abolish_api_with_options(
        self,
        request: cloud_api20160201_models.AbolishApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AbolishApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AbolishApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_api_with_options_async(
        self,
        request: cloud_api20160201_models.AbolishApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AbolishApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbolishApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AbolishApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_api(
        self,
        request: cloud_api20160201_models.AbolishApiRequest,
    ) -> cloud_api20160201_models.AbolishApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.abolish_api_with_options(request, runtime)

    async def abolish_api_async(
        self,
        request: cloud_api20160201_models.AbolishApiRequest,
    ) -> cloud_api20160201_models.AbolishApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abolish_api_with_options_async(request, runtime)

    def abolish_api_for_inner_with_options(
        self,
        request: cloud_api20160201_models.AbolishApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AbolishApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbolishApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AbolishApiForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def abolish_api_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.AbolishApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AbolishApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbolishApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AbolishApiForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abolish_api_for_inner(
        self,
        request: cloud_api20160201_models.AbolishApiForInnerRequest,
    ) -> cloud_api20160201_models.AbolishApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.abolish_api_for_inner_with_options(request, runtime)

    async def abolish_api_for_inner_async(
        self,
        request: cloud_api20160201_models.AbolishApiForInnerRequest,
    ) -> cloud_api20160201_models.AbolishApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abolish_api_for_inner_with_options_async(request, runtime)

    def add_black_list_with_options(
        self,
        request: cloud_api20160201_models.AddBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AddBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlackList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AddBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_black_list_with_options_async(
        self,
        request: cloud_api20160201_models.AddBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AddBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBlackList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AddBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_black_list(
        self,
        request: cloud_api20160201_models.AddBlackListRequest,
    ) -> cloud_api20160201_models.AddBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_black_list_with_options(request, runtime)

    async def add_black_list_async(
        self,
        request: cloud_api20160201_models.AddBlackListRequest,
    ) -> cloud_api20160201_models.AddBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_black_list_with_options_async(request, runtime)

    def add_traffic_special_control_with_options(
        self,
        request: cloud_api20160201_models.AddTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AddTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_value):
            query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AddTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160201_models.AddTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.AddTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_value):
            query['TrafficValue'] = request.traffic_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrafficSpecialControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.AddTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_traffic_special_control(
        self,
        request: cloud_api20160201_models.AddTrafficSpecialControlRequest,
    ) -> cloud_api20160201_models.AddTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_traffic_special_control_with_options(request, runtime)

    async def add_traffic_special_control_async(
        self,
        request: cloud_api20160201_models.AddTrafficSpecialControlRequest,
    ) -> cloud_api20160201_models.AddTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_traffic_special_control_with_options_async(request, runtime)

    def check_account_for_inner_with_options(
        self,
        request: cloud_api20160201_models.CheckAccountForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CheckAccountForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CheckAccountForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.CheckAccountForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CheckAccountForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CheckAccountForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account_for_inner(
        self,
        request: cloud_api20160201_models.CheckAccountForInnerRequest,
    ) -> cloud_api20160201_models.CheckAccountForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_account_for_inner_with_options(request, runtime)

    async def check_account_for_inner_async(
        self,
        request: cloud_api20160201_models.CheckAccountForInnerRequest,
    ) -> cloud_api20160201_models.CheckAccountForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_account_for_inner_with_options_async(request, runtime)

    def check_aone_app_audit_with_options(
        self,
        request: cloud_api20160201_models.CheckAoneAppAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CheckAoneAppAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aone_app_name):
            query['AoneAppName'] = request.aone_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAoneAppAudit',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CheckAoneAppAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_aone_app_audit_with_options_async(
        self,
        request: cloud_api20160201_models.CheckAoneAppAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CheckAoneAppAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aone_app_name):
            query['AoneAppName'] = request.aone_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAoneAppAudit',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CheckAoneAppAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_aone_app_audit(
        self,
        request: cloud_api20160201_models.CheckAoneAppAuditRequest,
    ) -> cloud_api20160201_models.CheckAoneAppAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_aone_app_audit_with_options(request, runtime)

    async def check_aone_app_audit_async(
        self,
        request: cloud_api20160201_models.CheckAoneAppAuditRequest,
    ) -> cloud_api20160201_models.CheckAoneAppAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_aone_app_audit_with_options_async(request, runtime)

    def copy_consumer_open_for_inner_with_options(
        self,
        request: cloud_api20160201_models.CopyConsumerOpenForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CopyConsumerOpenForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.copy_list):
            query['CopyList'] = request.copy_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyConsumerOpenForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CopyConsumerOpenForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_consumer_open_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.CopyConsumerOpenForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CopyConsumerOpenForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.copy_list):
            query['CopyList'] = request.copy_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyConsumerOpenForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CopyConsumerOpenForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_consumer_open_for_inner(
        self,
        request: cloud_api20160201_models.CopyConsumerOpenForInnerRequest,
    ) -> cloud_api20160201_models.CopyConsumerOpenForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_consumer_open_for_inner_with_options(request, runtime)

    async def copy_consumer_open_for_inner_async(
        self,
        request: cloud_api20160201_models.CopyConsumerOpenForInnerRequest,
    ) -> cloud_api20160201_models.CopyConsumerOpenForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_consumer_open_for_inner_with_options_async(request, runtime)

    def create_api_with_options(
        self,
        request: cloud_api20160201_models.CreateApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.body_format):
            query['BodyFormat'] = request.body_format
        if not UtilClient.is_unset(request.constant_parameters):
            query['ConstantParameters'] = request.constant_parameters
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.http_method):
            query['HttpMethod'] = request.http_method
        if not UtilClient.is_unset(request.http_protocol):
            query['HttpProtocol'] = request.http_protocol
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.path_parameters):
            query['PathParameters'] = request.path_parameters
        if not UtilClient.is_unset(request.post_body_description):
            query['PostBodyDescription'] = request.post_body_description
        if not UtilClient.is_unset(request.post_body_type):
            query['PostBodyType'] = request.post_body_type
        if not UtilClient.is_unset(request.request_body):
            query['RequestBody'] = request.request_body
        if not UtilClient.is_unset(request.request_headers):
            query['RequestHeaders'] = request.request_headers
        if not UtilClient.is_unset(request.request_queries):
            query['RequestQueries'] = request.request_queries
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_address):
            query['ServiceAddress'] = request.service_address
        if not UtilClient.is_unset(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not UtilClient.is_unset(request.service_timeout):
            query['ServiceTimeout'] = request.service_timeout
        if not UtilClient.is_unset(request.system_parameters):
            query['SystemParameters'] = request.system_parameters
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_with_options_async(
        self,
        request: cloud_api20160201_models.CreateApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.body_format):
            query['BodyFormat'] = request.body_format
        if not UtilClient.is_unset(request.constant_parameters):
            query['ConstantParameters'] = request.constant_parameters
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.http_method):
            query['HttpMethod'] = request.http_method
        if not UtilClient.is_unset(request.http_protocol):
            query['HttpProtocol'] = request.http_protocol
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.path_parameters):
            query['PathParameters'] = request.path_parameters
        if not UtilClient.is_unset(request.post_body_description):
            query['PostBodyDescription'] = request.post_body_description
        if not UtilClient.is_unset(request.post_body_type):
            query['PostBodyType'] = request.post_body_type
        if not UtilClient.is_unset(request.request_body):
            query['RequestBody'] = request.request_body
        if not UtilClient.is_unset(request.request_headers):
            query['RequestHeaders'] = request.request_headers
        if not UtilClient.is_unset(request.request_queries):
            query['RequestQueries'] = request.request_queries
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_address):
            query['ServiceAddress'] = request.service_address
        if not UtilClient.is_unset(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not UtilClient.is_unset(request.service_timeout):
            query['ServiceTimeout'] = request.service_timeout
        if not UtilClient.is_unset(request.system_parameters):
            query['SystemParameters'] = request.system_parameters
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api(
        self,
        request: cloud_api20160201_models.CreateApiRequest,
    ) -> cloud_api20160201_models.CreateApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_with_options(request, runtime)

    async def create_api_async(
        self,
        request: cloud_api20160201_models.CreateApiRequest,
    ) -> cloud_api20160201_models.CreateApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_with_options_async(request, runtime)

    def create_api_for_inner_with_options(
        self,
        request: cloud_api20160201_models.CreateApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.CreateApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_for_inner(
        self,
        request: cloud_api20160201_models.CreateApiForInnerRequest,
    ) -> cloud_api20160201_models.CreateApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_for_inner_with_options(request, runtime)

    async def create_api_for_inner_async(
        self,
        request: cloud_api20160201_models.CreateApiForInnerRequest,
    ) -> cloud_api20160201_models.CreateApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_for_inner_with_options_async(request, runtime)

    def create_api_group_with_options(
        self,
        request: cloud_api20160201_models.CreateApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_group_with_options_async(
        self,
        request: cloud_api20160201_models.CreateApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiGroup',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_group(
        self,
        request: cloud_api20160201_models.CreateApiGroupRequest,
    ) -> cloud_api20160201_models.CreateApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_group_with_options(request, runtime)

    async def create_api_group_async(
        self,
        request: cloud_api20160201_models.CreateApiGroupRequest,
    ) -> cloud_api20160201_models.CreateApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_group_with_options_async(request, runtime)

    def create_api_group_for_inner_with_options(
        self,
        request: cloud_api20160201_models.CreateApiGroupForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiGroupForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiGroupForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiGroupForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_group_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.CreateApiGroupForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateApiGroupForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiGroupForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateApiGroupForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_group_for_inner(
        self,
        request: cloud_api20160201_models.CreateApiGroupForInnerRequest,
    ) -> cloud_api20160201_models.CreateApiGroupForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_api_group_for_inner_with_options(request, runtime)

    async def create_api_group_for_inner_async(
        self,
        request: cloud_api20160201_models.CreateApiGroupForInnerRequest,
    ) -> cloud_api20160201_models.CreateApiGroupForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_api_group_for_inner_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: cloud_api20160201_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: cloud_api20160201_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: cloud_api20160201_models.CreateAppRequest,
    ) -> cloud_api20160201_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: cloud_api20160201_models.CreateAppRequest,
    ) -> cloud_api20160201_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_app_for_backend_with_options(
        self,
        request: cloud_api20160201_models.CreateAppForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateAppForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateAppForBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_for_backend_with_options_async(
        self,
        request: cloud_api20160201_models.CreateAppForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateAppForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateAppForBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_for_backend(
        self,
        request: cloud_api20160201_models.CreateAppForBackendRequest,
    ) -> cloud_api20160201_models.CreateAppForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_for_backend_with_options(request, runtime)

    async def create_app_for_backend_async(
        self,
        request: cloud_api20160201_models.CreateAppForBackendRequest,
    ) -> cloud_api20160201_models.CreateAppForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_for_backend_with_options_async(request, runtime)

    def create_app_for_inner_with_options(
        self,
        request: cloud_api20160201_models.CreateAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_secret):
            query['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateAppForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.CreateAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_secret):
            query['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateAppForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_for_inner(
        self,
        request: cloud_api20160201_models.CreateAppForInnerRequest,
    ) -> cloud_api20160201_models.CreateAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_for_inner_with_options(request, runtime)

    async def create_app_for_inner_async(
        self,
        request: cloud_api20160201_models.CreateAppForInnerRequest,
    ) -> cloud_api20160201_models.CreateAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_for_inner_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: cloud_api20160201_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_quantity):
            query['AccountQuantity'] = request.account_quantity
        if not UtilClient.is_unset(request.alarm_quota):
            query['AlarmQuota'] = request.alarm_quota
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.billing_type):
            query['BillingType'] = request.billing_type
        if not UtilClient.is_unset(request.cloud_market_instance_id):
            query['CloudMarketInstanceId'] = request.cloud_market_instance_id
        if not UtilClient.is_unset(request.expired_on):
            query['ExpiredOn'] = request.expired_on
        if not UtilClient.is_unset(request.instance_attributes):
            query['InstanceAttributes'] = request.instance_attributes
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: cloud_api20160201_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_quantity):
            query['AccountQuantity'] = request.account_quantity
        if not UtilClient.is_unset(request.alarm_quota):
            query['AlarmQuota'] = request.alarm_quota
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.billing_type):
            query['BillingType'] = request.billing_type
        if not UtilClient.is_unset(request.cloud_market_instance_id):
            query['CloudMarketInstanceId'] = request.cloud_market_instance_id
        if not UtilClient.is_unset(request.expired_on):
            query['ExpiredOn'] = request.expired_on
        if not UtilClient.is_unset(request.instance_attributes):
            query['InstanceAttributes'] = request.instance_attributes
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: cloud_api20160201_models.CreateInstanceRequest,
    ) -> cloud_api20160201_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: cloud_api20160201_models.CreateInstanceRequest,
    ) -> cloud_api20160201_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_race_work_for_inner_with_options(
        self,
        request: cloud_api20160201_models.CreateRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.short_description):
            query['ShortDescription'] = request.short_description
        if not UtilClient.is_unset(request.work_name):
            query['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRaceWorkForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateRaceWorkForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_race_work_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.CreateRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.keywords):
            query['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.short_description):
            query['ShortDescription'] = request.short_description
        if not UtilClient.is_unset(request.work_name):
            query['WorkName'] = request.work_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRaceWorkForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateRaceWorkForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_race_work_for_inner(
        self,
        request: cloud_api20160201_models.CreateRaceWorkForInnerRequest,
    ) -> cloud_api20160201_models.CreateRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_race_work_for_inner_with_options(request, runtime)

    async def create_race_work_for_inner_async(
        self,
        request: cloud_api20160201_models.CreateRaceWorkForInnerRequest,
    ) -> cloud_api20160201_models.CreateRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_race_work_for_inner_with_options_async(request, runtime)

    def create_secret_key_with_options(
        self,
        request: cloud_api20160201_models.CreateSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecretKey',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateSecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_key_with_options_async(
        self,
        request: cloud_api20160201_models.CreateSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSecretKey',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateSecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret_key(
        self,
        request: cloud_api20160201_models.CreateSecretKeyRequest,
    ) -> cloud_api20160201_models.CreateSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_secret_key_with_options(request, runtime)

    async def create_secret_key_async(
        self,
        request: cloud_api20160201_models.CreateSecretKeyRequest,
    ) -> cloud_api20160201_models.CreateSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_secret_key_with_options_async(request, runtime)

    def create_traffic_control_with_options(
        self,
        request: cloud_api20160201_models.CreateTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_traffic_control_with_options_async(
        self,
        request: cloud_api20160201_models.CreateTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrafficControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_traffic_control(
        self,
        request: cloud_api20160201_models.CreateTrafficControlRequest,
    ) -> cloud_api20160201_models.CreateTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_control_with_options(request, runtime)

    async def create_traffic_control_async(
        self,
        request: cloud_api20160201_models.CreateTrafficControlRequest,
    ) -> cloud_api20160201_models.CreateTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_traffic_control_with_options_async(request, runtime)

    def create_user_white_list_with_options(
        self,
        request: cloud_api20160201_models.CreateUserWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateUserWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aone_id):
            query['AoneId'] = request.aone_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.limit_count):
            query['LimitCount'] = request.limit_count
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserWhiteList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateUserWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_white_list_with_options_async(
        self,
        request: cloud_api20160201_models.CreateUserWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.CreateUserWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aone_id):
            query['AoneId'] = request.aone_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.limit_count):
            query['LimitCount'] = request.limit_count
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserWhiteList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.CreateUserWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_white_list(
        self,
        request: cloud_api20160201_models.CreateUserWhiteListRequest,
    ) -> cloud_api20160201_models.CreateUserWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_white_list_with_options(request, runtime)

    async def create_user_white_list_async(
        self,
        request: cloud_api20160201_models.CreateUserWhiteListRequest,
    ) -> cloud_api20160201_models.CreateUserWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_white_list_with_options_async(request, runtime)

    def delete_all_traffic_special_control_with_options(
        self,
        request: cloud_api20160201_models.DeleteAllTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteAllTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteAllTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_all_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteAllTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteAllTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAllTrafficSpecialControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteAllTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_all_traffic_special_control(
        self,
        request: cloud_api20160201_models.DeleteAllTrafficSpecialControlRequest,
    ) -> cloud_api20160201_models.DeleteAllTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_all_traffic_special_control_with_options(request, runtime)

    async def delete_all_traffic_special_control_async(
        self,
        request: cloud_api20160201_models.DeleteAllTrafficSpecialControlRequest,
    ) -> cloud_api20160201_models.DeleteAllTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_all_traffic_special_control_with_options_async(request, runtime)

    def delete_api_with_options(
        self,
        request: cloud_api20160201_models.DeleteApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api(
        self,
        request: cloud_api20160201_models.DeleteApiRequest,
    ) -> cloud_api20160201_models.DeleteApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_with_options(request, runtime)

    async def delete_api_async(
        self,
        request: cloud_api20160201_models.DeleteApiRequest,
    ) -> cloud_api20160201_models.DeleteApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_with_options_async(request, runtime)

    def delete_api_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DeleteApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteApiForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteApiForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_for_inner(
        self,
        request: cloud_api20160201_models.DeleteApiForInnerRequest,
    ) -> cloud_api20160201_models.DeleteApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_for_inner_with_options(request, runtime)

    async def delete_api_for_inner_async(
        self,
        request: cloud_api20160201_models.DeleteApiForInnerRequest,
    ) -> cloud_api20160201_models.DeleteApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_for_inner_with_options_async(request, runtime)

    def delete_api_group_with_options(
        self,
        request: cloud_api20160201_models.DeleteApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_group_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiGroup',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_group(
        self,
        request: cloud_api20160201_models.DeleteApiGroupRequest,
    ) -> cloud_api20160201_models.DeleteApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_api_group_with_options(request, runtime)

    async def delete_api_group_async(
        self,
        request: cloud_api20160201_models.DeleteApiGroupRequest,
    ) -> cloud_api20160201_models.DeleteApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_group_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: cloud_api20160201_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: cloud_api20160201_models.DeleteAppRequest,
    ) -> cloud_api20160201_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: cloud_api20160201_models.DeleteAppRequest,
    ) -> cloud_api20160201_models.DeleteAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_app_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DeleteAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteAppForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteAppForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_for_inner(
        self,
        request: cloud_api20160201_models.DeleteAppForInnerRequest,
    ) -> cloud_api20160201_models.DeleteAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_for_inner_with_options(request, runtime)

    async def delete_app_for_inner_async(
        self,
        request: cloud_api20160201_models.DeleteAppForInnerRequest,
    ) -> cloud_api20160201_models.DeleteAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_for_inner_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: cloud_api20160201_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: cloud_api20160201_models.DeleteDomainRequest,
    ) -> cloud_api20160201_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: cloud_api20160201_models.DeleteDomainRequest,
    ) -> cloud_api20160201_models.DeleteDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_certificate_with_options(
        self,
        request: cloud_api20160201_models.DeleteDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_certificate_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainCertificate',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_certificate(
        self,
        request: cloud_api20160201_models.DeleteDomainCertificateRequest,
    ) -> cloud_api20160201_models.DeleteDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_certificate_with_options(request, runtime)

    async def delete_domain_certificate_async(
        self,
        request: cloud_api20160201_models.DeleteDomainCertificateRequest,
    ) -> cloud_api20160201_models.DeleteDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_certificate_with_options_async(request, runtime)

    def delete_secret_key_with_options(
        self,
        request: cloud_api20160201_models.DeleteSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretKey',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteSecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_key_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteSecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteSecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSecretKey',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteSecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret_key(
        self,
        request: cloud_api20160201_models.DeleteSecretKeyRequest,
    ) -> cloud_api20160201_models.DeleteSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_key_with_options(request, runtime)

    async def delete_secret_key_async(
        self,
        request: cloud_api20160201_models.DeleteSecretKeyRequest,
    ) -> cloud_api20160201_models.DeleteSecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_key_with_options_async(request, runtime)

    def delete_traffic_control_with_options(
        self,
        request: cloud_api20160201_models.DeleteTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_control_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_control(
        self,
        request: cloud_api20160201_models.DeleteTrafficControlRequest,
    ) -> cloud_api20160201_models.DeleteTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_control_with_options(request, runtime)

    async def delete_traffic_control_async(
        self,
        request: cloud_api20160201_models.DeleteTrafficControlRequest,
    ) -> cloud_api20160201_models.DeleteTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_control_with_options_async(request, runtime)

    def delete_traffic_special_control_with_options(
        self,
        request: cloud_api20160201_models.DeleteTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteTrafficSpecialControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_traffic_special_control_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteTrafficSpecialControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteTrafficSpecialControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.special_key):
            query['SpecialKey'] = request.special_key
        if not UtilClient.is_unset(request.special_type):
            query['SpecialType'] = request.special_type
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrafficSpecialControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteTrafficSpecialControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_traffic_special_control(
        self,
        request: cloud_api20160201_models.DeleteTrafficSpecialControlRequest,
    ) -> cloud_api20160201_models.DeleteTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_special_control_with_options(request, runtime)

    async def delete_traffic_special_control_async(
        self,
        request: cloud_api20160201_models.DeleteTrafficSpecialControlRequest,
    ) -> cloud_api20160201_models.DeleteTrafficSpecialControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_special_control_with_options_async(request, runtime)

    def delete_user_white_list_by_type_with_options(
        self,
        request: cloud_api20160201_models.DeleteUserWhiteListByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteUserWhiteListByTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserWhiteListByType',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteUserWhiteListByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_white_list_by_type_with_options_async(
        self,
        request: cloud_api20160201_models.DeleteUserWhiteListByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeleteUserWhiteListByTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserWhiteListByType',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeleteUserWhiteListByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_white_list_by_type(
        self,
        request: cloud_api20160201_models.DeleteUserWhiteListByTypeRequest,
    ) -> cloud_api20160201_models.DeleteUserWhiteListByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_white_list_by_type_with_options(request, runtime)

    async def delete_user_white_list_by_type_async(
        self,
        request: cloud_api20160201_models.DeleteUserWhiteListByTypeRequest,
    ) -> cloud_api20160201_models.DeleteUserWhiteListByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_white_list_by_type_with_options_async(request, runtime)

    def deploy_api_with_options(
        self,
        request: cloud_api20160201_models.DeployApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeployApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeployApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_api_with_options_async(
        self,
        request: cloud_api20160201_models.DeployApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeployApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeployApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_api(
        self,
        request: cloud_api20160201_models.DeployApiRequest,
    ) -> cloud_api20160201_models.DeployApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_api_with_options(request, runtime)

    async def deploy_api_async(
        self,
        request: cloud_api20160201_models.DeployApiRequest,
    ) -> cloud_api20160201_models.DeployApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_api_with_options_async(request, runtime)

    def deploy_api_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DeployApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeployApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeployApiForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_api_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DeployApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DeployApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DeployApiForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_api_for_inner(
        self,
        request: cloud_api20160201_models.DeployApiForInnerRequest,
    ) -> cloud_api20160201_models.DeployApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_api_for_inner_with_options(request, runtime)

    async def deploy_api_for_inner_async(
        self,
        request: cloud_api20160201_models.DeployApiForInnerRequest,
    ) -> cloud_api20160201_models.DeployApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_api_for_inner_with_options_async(request, runtime)

    def describe_api_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api(
        self,
        request: cloud_api20160201_models.DescribeApiRequest,
    ) -> cloud_api20160201_models.DescribeApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_with_options(request, runtime)

    async def describe_api_async(
        self,
        request: cloud_api20160201_models.DescribeApiRequest,
    ) -> cloud_api20160201_models.DescribeApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_with_options_async(request, runtime)

    def describe_api_doc_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiDocResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiDocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_doc_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiDocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiDocResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDoc',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiDocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_doc(
        self,
        request: cloud_api20160201_models.DescribeApiDocRequest,
    ) -> cloud_api20160201_models.DescribeApiDocResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_doc_with_options(request, runtime)

    async def describe_api_doc_async(
        self,
        request: cloud_api20160201_models.DescribeApiDocRequest,
    ) -> cloud_api20160201_models.DescribeApiDocResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_doc_with_options_async(request, runtime)

    def describe_api_docs_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDocs',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiDocsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_docs_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiDocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiDocsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDocs',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiDocsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_docs(
        self,
        request: cloud_api20160201_models.DescribeApiDocsRequest,
    ) -> cloud_api20160201_models.DescribeApiDocsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_docs_with_options(request, runtime)

    async def describe_api_docs_async(
        self,
        request: cloud_api20160201_models.DescribeApiDocsRequest,
    ) -> cloud_api20160201_models.DescribeApiDocsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_docs_with_options_async(request, runtime)

    def describe_api_docs_for_backend_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiDocsForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiDocsForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDocsForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiDocsForBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_docs_for_backend_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiDocsForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiDocsForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiDocsForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiDocsForBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_docs_for_backend(
        self,
        request: cloud_api20160201_models.DescribeApiDocsForBackendRequest,
    ) -> cloud_api20160201_models.DescribeApiDocsForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_docs_for_backend_with_options(request, runtime)

    async def describe_api_docs_for_backend_async(
        self,
        request: cloud_api20160201_models.DescribeApiDocsForBackendRequest,
    ) -> cloud_api20160201_models.DescribeApiDocsForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_docs_for_backend_with_options_async(request, runtime)

    def describe_api_error_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiError',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_error_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiErrorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiErrorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiError',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiErrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_error(
        self,
        request: cloud_api20160201_models.DescribeApiErrorRequest,
    ) -> cloud_api20160201_models.DescribeApiErrorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_error_with_options(request, runtime)

    async def describe_api_error_async(
        self,
        request: cloud_api20160201_models.DescribeApiErrorRequest,
    ) -> cloud_api20160201_models.DescribeApiErrorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_error_with_options_async(request, runtime)

    def describe_api_group_detail_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupDetail',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_group_detail_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroupDetail',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_group_detail(
        self,
        request: cloud_api20160201_models.DescribeApiGroupDetailRequest,
    ) -> cloud_api20160201_models.DescribeApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_group_detail_with_options(request, runtime)

    async def describe_api_group_detail_async(
        self,
        request: cloud_api20160201_models.DescribeApiGroupDetailRequest,
    ) -> cloud_api20160201_models.DescribeApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_group_detail_with_options_async(request, runtime)

    def describe_api_groups_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_groups_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiGroups',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_groups(
        self,
        request: cloud_api20160201_models.DescribeApiGroupsRequest,
    ) -> cloud_api20160201_models.DescribeApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_groups_with_options(request, runtime)

    async def describe_api_groups_async(
        self,
        request: cloud_api20160201_models.DescribeApiGroupsRequest,
    ) -> cloud_api20160201_models.DescribeApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_groups_with_options_async(request, runtime)

    def describe_api_latency_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiLatencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiLatencyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiLatency',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiLatencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_latency_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiLatencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiLatencyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiLatency',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiLatencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_latency(
        self,
        request: cloud_api20160201_models.DescribeApiLatencyRequest,
    ) -> cloud_api20160201_models.DescribeApiLatencyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_latency_with_options(request, runtime)

    async def describe_api_latency_async(
        self,
        request: cloud_api20160201_models.DescribeApiLatencyRequest,
    ) -> cloud_api20160201_models.DescribeApiLatencyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_latency_with_options_async(request, runtime)

    def describe_api_market_instance_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiMarketInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiMarketInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiMarketInstance',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiMarketInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_market_instance_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiMarketInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiMarketInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiMarketInstance',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiMarketInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_market_instance(
        self,
        request: cloud_api20160201_models.DescribeApiMarketInstanceRequest,
    ) -> cloud_api20160201_models.DescribeApiMarketInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_market_instance_with_options(request, runtime)

    async def describe_api_market_instance_async(
        self,
        request: cloud_api20160201_models.DescribeApiMarketInstanceRequest,
    ) -> cloud_api20160201_models.DescribeApiMarketInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_market_instance_with_options_async(request, runtime)

    def describe_api_qps_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiQps',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiQpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_qps_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiQpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiQps',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiQpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_qps(
        self,
        request: cloud_api20160201_models.DescribeApiQpsRequest,
    ) -> cloud_api20160201_models.DescribeApiQpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_qps_with_options(request, runtime)

    async def describe_api_qps_async(
        self,
        request: cloud_api20160201_models.DescribeApiQpsRequest,
    ) -> cloud_api20160201_models.DescribeApiQpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_qps_with_options_async(request, runtime)

    def describe_api_rules_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiRules',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_rules_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiRules',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_rules(
        self,
        request: cloud_api20160201_models.DescribeApiRulesRequest,
    ) -> cloud_api20160201_models.DescribeApiRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_rules_with_options(request, runtime)

    async def describe_api_rules_async(
        self,
        request: cloud_api20160201_models.DescribeApiRulesRequest,
    ) -> cloud_api20160201_models.DescribeApiRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_rules_with_options_async(request, runtime)

    def describe_api_traffic_with_options(
        self,
        request: cloud_api20160201_models.DescribeApiTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiTraffic',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiTrafficResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_api_traffic_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApiTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApiTrafficResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApiTraffic',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApiTrafficResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_api_traffic(
        self,
        request: cloud_api20160201_models.DescribeApiTrafficRequest,
    ) -> cloud_api20160201_models.DescribeApiTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_traffic_with_options(request, runtime)

    async def describe_api_traffic_async(
        self,
        request: cloud_api20160201_models.DescribeApiTrafficRequest,
    ) -> cloud_api20160201_models.DescribeApiTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_traffic_with_options_async(request, runtime)

    def describe_apis_with_options(
        self,
        request: cloud_api20160201_models.DescribeApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis(
        self,
        request: cloud_api20160201_models.DescribeApisRequest,
    ) -> cloud_api20160201_models.DescribeApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_with_options(request, runtime)

    async def describe_apis_async(
        self,
        request: cloud_api20160201_models.DescribeApisRequest,
    ) -> cloud_api20160201_models.DescribeApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_with_options_async(request, runtime)

    def describe_apis_by_app_with_options(
        self,
        request: cloud_api20160201_models.DescribeApisByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_app_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApisByAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisByAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_app(
        self,
        request: cloud_api20160201_models.DescribeApisByAppRequest,
    ) -> cloud_api20160201_models.DescribeApisByAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_app_with_options(request, runtime)

    async def describe_apis_by_app_async(
        self,
        request: cloud_api20160201_models.DescribeApisByAppRequest,
    ) -> cloud_api20160201_models.DescribeApisByAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_app_with_options_async(request, runtime)

    def describe_apis_by_rule_with_options(
        self,
        request: cloud_api20160201_models.DescribeApisByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByRule',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_by_rule_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApisByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisByRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisByRule',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisByRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_by_rule(
        self,
        request: cloud_api20160201_models.DescribeApisByRuleRequest,
    ) -> cloud_api20160201_models.DescribeApisByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_by_rule_with_options(request, runtime)

    async def describe_apis_by_rule_async(
        self,
        request: cloud_api20160201_models.DescribeApisByRuleRequest,
    ) -> cloud_api20160201_models.DescribeApisByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_by_rule_with_options_async(request, runtime)

    def describe_apis_for_console_with_options(
        self,
        request: cloud_api20160201_models.DescribeApisForConsoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisForConsoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisForConsole',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisForConsoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apis_for_console_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeApisForConsoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeApisForConsoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApisForConsole',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeApisForConsoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apis_for_console(
        self,
        request: cloud_api20160201_models.DescribeApisForConsoleRequest,
    ) -> cloud_api20160201_models.DescribeApisForConsoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apis_for_console_with_options(request, runtime)

    async def describe_apis_for_console_async(
        self,
        request: cloud_api20160201_models.DescribeApisForConsoleRequest,
    ) -> cloud_api20160201_models.DescribeApisForConsoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apis_for_console_with_options_async(request, runtime)

    def describe_app_with_options(
        self,
        request: cloud_api20160201_models.DescribeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app(
        self,
        request: cloud_api20160201_models.DescribeAppRequest,
    ) -> cloud_api20160201_models.DescribeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_with_options(request, runtime)

    async def describe_app_async(
        self,
        request: cloud_api20160201_models.DescribeAppRequest,
    ) -> cloud_api20160201_models.DescribeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_with_options_async(request, runtime)

    def describe_app_securities_with_options(
        self,
        request: cloud_api20160201_models.DescribeAppSecuritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppSecuritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurities',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppSecuritiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_securities_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAppSecuritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppSecuritiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurities',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppSecuritiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_securities(
        self,
        request: cloud_api20160201_models.DescribeAppSecuritiesRequest,
    ) -> cloud_api20160201_models.DescribeAppSecuritiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_securities_with_options(request, runtime)

    async def describe_app_securities_async(
        self,
        request: cloud_api20160201_models.DescribeAppSecuritiesRequest,
    ) -> cloud_api20160201_models.DescribeAppSecuritiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_securities_with_options_async(request, runtime)

    def describe_app_security_with_options(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppSecurityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppSecurityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_security_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppSecurityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurity',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppSecurityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_security(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityRequest,
    ) -> cloud_api20160201_models.DescribeAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_security_with_options(request, runtime)

    async def describe_app_security_async(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityRequest,
    ) -> cloud_api20160201_models.DescribeAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_security_with_options_async(request, runtime)

    def describe_app_security_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppSecurityForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurityForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppSecurityForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_security_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppSecurityForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppSecurityForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppSecurityForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_security_for_inner(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityForInnerRequest,
    ) -> cloud_api20160201_models.DescribeAppSecurityForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_security_for_inner_with_options(request, runtime)

    async def describe_app_security_for_inner_async(
        self,
        request: cloud_api20160201_models.DescribeAppSecurityForInnerRequest,
    ) -> cloud_api20160201_models.DescribeAppSecurityForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_security_for_inner_with_options_async(request, runtime)

    def describe_apps_with_options(
        self,
        request: cloud_api20160201_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps(
        self,
        request: cloud_api20160201_models.DescribeAppsRequest,
    ) -> cloud_api20160201_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    async def describe_apps_async(
        self,
        request: cloud_api20160201_models.DescribeAppsRequest,
    ) -> cloud_api20160201_models.DescribeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_with_options_async(request, runtime)

    def describe_apps_by_api_with_options(
        self,
        request: cloud_api20160201_models.DescribeAppsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsByApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppsByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_by_api_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAppsByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppsByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsByApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppsByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps_by_api(
        self,
        request: cloud_api20160201_models.DescribeAppsByApiRequest,
    ) -> cloud_api20160201_models.DescribeAppsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_by_api_with_options(request, runtime)

    async def describe_apps_by_api_async(
        self,
        request: cloud_api20160201_models.DescribeAppsByApiRequest,
    ) -> cloud_api20160201_models.DescribeAppsByApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_by_api_with_options_async(request, runtime)

    def describe_apps_for_provider_with_options(
        self,
        request: cloud_api20160201_models.DescribeAppsForProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppsForProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_owner):
            query['AppOwner'] = request.app_owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsForProvider',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppsForProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_apps_for_provider_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAppsForProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAppsForProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_owner):
            query['AppOwner'] = request.app_owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppsForProvider',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAppsForProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_apps_for_provider(
        self,
        request: cloud_api20160201_models.DescribeAppsForProviderRequest,
    ) -> cloud_api20160201_models.DescribeAppsForProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_for_provider_with_options(request, runtime)

    async def describe_apps_for_provider_async(
        self,
        request: cloud_api20160201_models.DescribeAppsForProviderRequest,
    ) -> cloud_api20160201_models.DescribeAppsForProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_apps_for_provider_with_options_async(request, runtime)

    def describe_available_vips_with_options(
        self,
        request: cloud_api20160201_models.DescribeAvailableVipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAvailableVipsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vip):
            query['Vip'] = request.vip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableVips',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAvailableVipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_vips_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeAvailableVipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeAvailableVipsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vip):
            query['Vip'] = request.vip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableVips',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeAvailableVipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_vips(
        self,
        request: cloud_api20160201_models.DescribeAvailableVipsRequest,
    ) -> cloud_api20160201_models.DescribeAvailableVipsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_vips_with_options(request, runtime)

    async def describe_available_vips_async(
        self,
        request: cloud_api20160201_models.DescribeAvailableVipsRequest,
    ) -> cloud_api20160201_models.DescribeAvailableVipsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_vips_with_options_async(request, runtime)

    def describe_bid_by_user_id_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DescribeBidByUserIdForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeBidByUserIdForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBidByUserIdForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeBidByUserIdForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bid_by_user_id_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeBidByUserIdForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeBidByUserIdForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBidByUserIdForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeBidByUserIdForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bid_by_user_id_for_inner(
        self,
        request: cloud_api20160201_models.DescribeBidByUserIdForInnerRequest,
    ) -> cloud_api20160201_models.DescribeBidByUserIdForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bid_by_user_id_for_inner_with_options(request, runtime)

    async def describe_bid_by_user_id_for_inner_async(
        self,
        request: cloud_api20160201_models.DescribeBidByUserIdForInnerRequest,
    ) -> cloud_api20160201_models.DescribeBidByUserIdForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bid_by_user_id_for_inner_with_options_async(request, runtime)

    def describe_black_lists_with_options(
        self,
        request: cloud_api20160201_models.DescribeBlackListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeBlackListsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackLists',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeBlackListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_black_lists_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeBlackListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeBlackListsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackLists',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeBlackListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_black_lists(
        self,
        request: cloud_api20160201_models.DescribeBlackListsRequest,
    ) -> cloud_api20160201_models.DescribeBlackListsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_black_lists_with_options(request, runtime)

    async def describe_black_lists_async(
        self,
        request: cloud_api20160201_models.DescribeBlackListsRequest,
    ) -> cloud_api20160201_models.DescribeBlackListsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_black_lists_with_options_async(request, runtime)

    def describe_deployed_api_with_options(
        self,
        request: cloud_api20160201_models.DescribeDeployedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDeployedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDeployedApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_api_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeDeployedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDeployedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDeployedApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_api(
        self,
        request: cloud_api20160201_models.DescribeDeployedApiRequest,
    ) -> cloud_api20160201_models.DescribeDeployedApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_api_with_options(request, runtime)

    async def describe_deployed_api_async(
        self,
        request: cloud_api20160201_models.DescribeDeployedApiRequest,
    ) -> cloud_api20160201_models.DescribeDeployedApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployed_api_with_options_async(request, runtime)

    def describe_deployed_apis_with_options(
        self,
        request: cloud_api20160201_models.DescribeDeployedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDeployedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDeployedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployed_apis_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeDeployedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDeployedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployedApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDeployedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployed_apis(
        self,
        request: cloud_api20160201_models.DescribeDeployedApisRequest,
    ) -> cloud_api20160201_models.DescribeDeployedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployed_apis_with_options(request, runtime)

    async def describe_deployed_apis_async(
        self,
        request: cloud_api20160201_models.DescribeDeployedApisRequest,
    ) -> cloud_api20160201_models.DescribeDeployedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployed_apis_with_options_async(request, runtime)

    def describe_domain_with_options(
        self,
        request: cloud_api20160201_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain(
        self,
        request: cloud_api20160201_models.DescribeDomainRequest,
    ) -> cloud_api20160201_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    async def describe_domain_async(
        self,
        request: cloud_api20160201_models.DescribeDomainRequest,
    ) -> cloud_api20160201_models.DescribeDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_with_options_async(request, runtime)

    def describe_domain_resolution_with_options(
        self,
        request: cloud_api20160201_models.DescribeDomainResolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDomainResolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolution',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDomainResolutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_resolution_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeDomainResolutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeDomainResolutionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainResolution',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeDomainResolutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_resolution(
        self,
        request: cloud_api20160201_models.DescribeDomainResolutionRequest,
    ) -> cloud_api20160201_models.DescribeDomainResolutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_resolution_with_options(request, runtime)

    async def describe_domain_resolution_async(
        self,
        request: cloud_api20160201_models.DescribeDomainResolutionRequest,
    ) -> cloud_api20160201_models.DescribeDomainResolutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_resolution_with_options_async(request, runtime)

    def describe_history_api_with_options(
        self,
        request: cloud_api20160201_models.DescribeHistoryApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeHistoryApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeHistoryApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_api_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeHistoryApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeHistoryApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeHistoryApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_api(
        self,
        request: cloud_api20160201_models.DescribeHistoryApiRequest,
    ) -> cloud_api20160201_models.DescribeHistoryApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_api_with_options(request, runtime)

    async def describe_history_api_async(
        self,
        request: cloud_api20160201_models.DescribeHistoryApiRequest,
    ) -> cloud_api20160201_models.DescribeHistoryApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_api_with_options_async(request, runtime)

    def describe_history_apis_with_options(
        self,
        request: cloud_api20160201_models.DescribeHistoryApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeHistoryApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeHistoryApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_apis_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeHistoryApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeHistoryApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHistoryApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeHistoryApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_apis(
        self,
        request: cloud_api20160201_models.DescribeHistoryApisRequest,
    ) -> cloud_api20160201_models.DescribeHistoryApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_history_apis_with_options(request, runtime)

    async def describe_history_apis_async(
        self,
        request: cloud_api20160201_models.DescribeHistoryApisRequest,
    ) -> cloud_api20160201_models.DescribeHistoryApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_history_apis_with_options_async(request, runtime)

    def describe_models_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DescribeModelsForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeModelsForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModelsForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeModelsForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_models_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeModelsForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeModelsForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_name):
            query['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeModelsForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeModelsForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_models_for_inner(
        self,
        request: cloud_api20160201_models.DescribeModelsForInnerRequest,
    ) -> cloud_api20160201_models.DescribeModelsForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_models_for_inner_with_options(request, runtime)

    async def describe_models_for_inner_async(
        self,
        request: cloud_api20160201_models.DescribeModelsForInnerRequest,
    ) -> cloud_api20160201_models.DescribeModelsForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_models_for_inner_with_options_async(request, runtime)

    def describe_purchased_api_with_options(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_with_options_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_with_options(request, runtime)

    async def describe_purchased_api_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_with_options_async(request, runtime)

    def describe_purchased_api_group_detail_with_options(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroupDetail',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApiGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_group_detail_with_options_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroupDetail',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApiGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_group_detail(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupDetailRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_group_detail_with_options(request, runtime)

    async def describe_purchased_api_group_detail_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupDetailRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_group_detail_with_options_async(request, runtime)

    def describe_purchased_api_groups_with_options(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_api_groups_with_options_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApiGroups',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_api_groups(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupsRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_api_groups_with_options(request, runtime)

    async def describe_purchased_api_groups_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApiGroupsRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApiGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_api_groups_with_options_async(request, runtime)

    def describe_purchased_apis_with_options(
        self,
        request: cloud_api20160201_models.DescribePurchasedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_apis_with_options_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribePurchasedApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribePurchasedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_apis(
        self,
        request: cloud_api20160201_models.DescribePurchasedApisRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_apis_with_options(request, runtime)

    async def describe_purchased_apis_async(
        self,
        request: cloud_api20160201_models.DescribePurchasedApisRequest,
    ) -> cloud_api20160201_models.DescribePurchasedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_apis_with_options_async(request, runtime)

    def describe_race_work_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DescribeRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRaceWorkForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRaceWorkForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_race_work_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeRaceWorkForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRaceWorkForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRaceWorkForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRaceWorkForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_race_work_for_inner(
        self,
        request: cloud_api20160201_models.DescribeRaceWorkForInnerRequest,
    ) -> cloud_api20160201_models.DescribeRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_race_work_for_inner_with_options(request, runtime)

    async def describe_race_work_for_inner_async(
        self,
        request: cloud_api20160201_models.DescribeRaceWorkForInnerRequest,
    ) -> cloud_api20160201_models.DescribeRaceWorkForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_race_work_for_inner_with_options_async(request, runtime)

    def describe_race_works_for_inner_with_options(
        self,
        request: cloud_api20160201_models.DescribeRaceWorksForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRaceWorksForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRaceWorksForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRaceWorksForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_race_works_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeRaceWorksForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRaceWorksForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRaceWorksForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRaceWorksForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_race_works_for_inner(
        self,
        request: cloud_api20160201_models.DescribeRaceWorksForInnerRequest,
    ) -> cloud_api20160201_models.DescribeRaceWorksForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_race_works_for_inner_with_options(request, runtime)

    async def describe_race_works_for_inner_async(
        self,
        request: cloud_api20160201_models.DescribeRaceWorksForInnerRequest,
    ) -> cloud_api20160201_models.DescribeRaceWorksForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_race_works_for_inner_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cloud_api20160201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: cloud_api20160201_models.DescribeRegionsRequest,
    ) -> cloud_api20160201_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cloud_api20160201_models.DescribeRegionsRequest,
    ) -> cloud_api20160201_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_rules_by_api_with_options(
        self,
        request: cloud_api20160201_models.DescribeRulesByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRulesByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRulesByApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRulesByApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_by_api_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeRulesByApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeRulesByApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRulesByApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeRulesByApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rules_by_api(
        self,
        request: cloud_api20160201_models.DescribeRulesByApiRequest,
    ) -> cloud_api20160201_models.DescribeRulesByApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_by_api_with_options(request, runtime)

    async def describe_rules_by_api_async(
        self,
        request: cloud_api20160201_models.DescribeRulesByApiRequest,
    ) -> cloud_api20160201_models.DescribeRulesByApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rules_by_api_with_options_async(request, runtime)

    def describe_secret_keys_with_options(
        self,
        request: cloud_api20160201_models.DescribeSecretKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeSecretKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecretKeys',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeSecretKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_secret_keys_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeSecretKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeSecretKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecretKeys',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeSecretKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_secret_keys(
        self,
        request: cloud_api20160201_models.DescribeSecretKeysRequest,
    ) -> cloud_api20160201_models.DescribeSecretKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_secret_keys_with_options(request, runtime)

    async def describe_secret_keys_async(
        self,
        request: cloud_api20160201_models.DescribeSecretKeysRequest,
    ) -> cloud_api20160201_models.DescribeSecretKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_secret_keys_with_options_async(request, runtime)

    def describe_system_parameters_with_options(
        self,
        request: cloud_api20160201_models.DescribeSystemParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeSystemParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeSystemParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_parameters_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeSystemParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeSystemParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParameters',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeSystemParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_parameters(
        self,
        request: cloud_api20160201_models.DescribeSystemParametersRequest,
    ) -> cloud_api20160201_models.DescribeSystemParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_parameters_with_options(request, runtime)

    async def describe_system_parameters_async(
        self,
        request: cloud_api20160201_models.DescribeSystemParametersRequest,
    ) -> cloud_api20160201_models.DescribeSystemParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_parameters_with_options_async(request, runtime)

    def describe_system_params_with_options(
        self,
        request: cloud_api20160201_models.DescribeSystemParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeSystemParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParams',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeSystemParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_params_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeSystemParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeSystemParamsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSystemParams',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeSystemParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_params(
        self,
        request: cloud_api20160201_models.DescribeSystemParamsRequest,
    ) -> cloud_api20160201_models.DescribeSystemParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_params_with_options(request, runtime)

    async def describe_system_params_async(
        self,
        request: cloud_api20160201_models.DescribeSystemParamsRequest,
    ) -> cloud_api20160201_models.DescribeSystemParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_params_with_options_async(request, runtime)

    def describe_traffic_controls_with_options(
        self,
        request: cloud_api20160201_models.DescribeTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeTrafficControlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_traffic_controls_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeTrafficControlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeTrafficControlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_uid):
            query['ApiUid'] = request.api_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrafficControls',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeTrafficControlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_traffic_controls(
        self,
        request: cloud_api20160201_models.DescribeTrafficControlsRequest,
    ) -> cloud_api20160201_models.DescribeTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_traffic_controls_with_options(request, runtime)

    async def describe_traffic_controls_async(
        self,
        request: cloud_api20160201_models.DescribeTrafficControlsRequest,
    ) -> cloud_api20160201_models.DescribeTrafficControlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_traffic_controls_with_options_async(request, runtime)

    def describe_user_white_lists_with_options(
        self,
        request: cloud_api20160201_models.DescribeUserWhiteListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeUserWhiteListsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserWhiteLists',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeUserWhiteListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_white_lists_with_options_async(
        self,
        request: cloud_api20160201_models.DescribeUserWhiteListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.DescribeUserWhiteListsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserWhiteLists',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.DescribeUserWhiteListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_white_lists(
        self,
        request: cloud_api20160201_models.DescribeUserWhiteListsRequest,
    ) -> cloud_api20160201_models.DescribeUserWhiteListsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_white_lists_with_options(request, runtime)

    async def describe_user_white_lists_async(
        self,
        request: cloud_api20160201_models.DescribeUserWhiteListsRequest,
    ) -> cloud_api20160201_models.DescribeUserWhiteListsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_white_lists_with_options_async(request, runtime)

    def is_included_by_user_whitelist_with_options(
        self,
        request: cloud_api20160201_models.IsIncludedByUserWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.IsIncludedByUserWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IsIncludedByUserWhitelist',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.IsIncludedByUserWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def is_included_by_user_whitelist_with_options_async(
        self,
        request: cloud_api20160201_models.IsIncludedByUserWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.IsIncludedByUserWhitelistResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IsIncludedByUserWhitelist',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.IsIncludedByUserWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def is_included_by_user_whitelist(
        self,
        request: cloud_api20160201_models.IsIncludedByUserWhitelistRequest,
    ) -> cloud_api20160201_models.IsIncludedByUserWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.is_included_by_user_whitelist_with_options(request, runtime)

    async def is_included_by_user_whitelist_async(
        self,
        request: cloud_api20160201_models.IsIncludedByUserWhitelistRequest,
    ) -> cloud_api20160201_models.IsIncludedByUserWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.is_included_by_user_whitelist_with_options_async(request, runtime)

    def modify_api_with_options(
        self,
        request: cloud_api20160201_models.ModifyApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.body_format):
            query['BodyFormat'] = request.body_format
        if not UtilClient.is_unset(request.constant_parameters):
            query['ConstantParameters'] = request.constant_parameters
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.http_method):
            query['HttpMethod'] = request.http_method
        if not UtilClient.is_unset(request.http_protocol):
            query['HttpProtocol'] = request.http_protocol
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.path_parameters):
            query['PathParameters'] = request.path_parameters
        if not UtilClient.is_unset(request.post_body_description):
            query['PostBodyDescription'] = request.post_body_description
        if not UtilClient.is_unset(request.post_body_type):
            query['PostBodyType'] = request.post_body_type
        if not UtilClient.is_unset(request.request_body):
            query['RequestBody'] = request.request_body
        if not UtilClient.is_unset(request.request_headers):
            query['RequestHeaders'] = request.request_headers
        if not UtilClient.is_unset(request.request_queries):
            query['RequestQueries'] = request.request_queries
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_address):
            query['ServiceAddress'] = request.service_address
        if not UtilClient.is_unset(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not UtilClient.is_unset(request.service_timeout):
            query['ServiceTimeout'] = request.service_timeout
        if not UtilClient.is_unset(request.system_parameters):
            query['SystemParameters'] = request.system_parameters
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.body_format):
            query['BodyFormat'] = request.body_format
        if not UtilClient.is_unset(request.constant_parameters):
            query['ConstantParameters'] = request.constant_parameters
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.http_method):
            query['HttpMethod'] = request.http_method
        if not UtilClient.is_unset(request.http_protocol):
            query['HttpProtocol'] = request.http_protocol
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.path_parameters):
            query['PathParameters'] = request.path_parameters
        if not UtilClient.is_unset(request.post_body_description):
            query['PostBodyDescription'] = request.post_body_description
        if not UtilClient.is_unset(request.post_body_type):
            query['PostBodyType'] = request.post_body_type
        if not UtilClient.is_unset(request.request_body):
            query['RequestBody'] = request.request_body
        if not UtilClient.is_unset(request.request_headers):
            query['RequestHeaders'] = request.request_headers
        if not UtilClient.is_unset(request.request_queries):
            query['RequestQueries'] = request.request_queries
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_address):
            query['ServiceAddress'] = request.service_address
        if not UtilClient.is_unset(request.service_protocol):
            query['ServiceProtocol'] = request.service_protocol
        if not UtilClient.is_unset(request.service_timeout):
            query['ServiceTimeout'] = request.service_timeout
        if not UtilClient.is_unset(request.system_parameters):
            query['SystemParameters'] = request.system_parameters
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api(
        self,
        request: cloud_api20160201_models.ModifyApiRequest,
    ) -> cloud_api20160201_models.ModifyApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_with_options(request, runtime)

    async def modify_api_async(
        self,
        request: cloud_api20160201_models.ModifyApiRequest,
    ) -> cloud_api20160201_models.ModifyApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_with_options_async(request, runtime)

    def modify_api_for_inner_with_options(
        self,
        request: cloud_api20160201_models.ModifyApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.request_config):
            query['RequestConfig'] = request.request_config
        if not UtilClient.is_unset(request.request_paramters):
            query['RequestParamters'] = request.request_paramters
        if not UtilClient.is_unset(request.result_sample):
            query['ResultSample'] = request.result_sample
        if not UtilClient.is_unset(request.result_type):
            query['ResultType'] = request.result_type
        if not UtilClient.is_unset(request.service_config):
            query['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.service_parameters):
            query['ServiceParameters'] = request.service_parameters
        if not UtilClient.is_unset(request.service_parameters_map):
            query['ServiceParametersMap'] = request.service_parameters_map
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_for_inner(
        self,
        request: cloud_api20160201_models.ModifyApiForInnerRequest,
    ) -> cloud_api20160201_models.ModifyApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_for_inner_with_options(request, runtime)

    async def modify_api_for_inner_async(
        self,
        request: cloud_api20160201_models.ModifyApiForInnerRequest,
    ) -> cloud_api20160201_models.ModifyApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_for_inner_with_options_async(request, runtime)

    def modify_api_group_with_options(
        self,
        request: cloud_api20160201_models.ModifyApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_group_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyApiGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiGroup',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_group(
        self,
        request: cloud_api20160201_models.ModifyApiGroupRequest,
    ) -> cloud_api20160201_models.ModifyApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_group_with_options(request, runtime)

    async def modify_api_group_async(
        self,
        request: cloud_api20160201_models.ModifyApiGroupRequest,
    ) -> cloud_api20160201_models.ModifyApiGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_group_with_options_async(request, runtime)

    def modify_api_market_instance_attribute_with_options(
        self,
        request: cloud_api20160201_models.ModifyApiMarketInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiMarketInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_attributes):
            query['InstanceAttributes'] = request.instance_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiMarketInstanceAttribute',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiMarketInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_market_instance_attribute_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyApiMarketInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyApiMarketInstanceAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_attributes):
            query['InstanceAttributes'] = request.instance_attributes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApiMarketInstanceAttribute',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyApiMarketInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_market_instance_attribute(
        self,
        request: cloud_api20160201_models.ModifyApiMarketInstanceAttributeRequest,
    ) -> cloud_api20160201_models.ModifyApiMarketInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_api_market_instance_attribute_with_options(request, runtime)

    async def modify_api_market_instance_attribute_async(
        self,
        request: cloud_api20160201_models.ModifyApiMarketInstanceAttributeRequest,
    ) -> cloud_api20160201_models.ModifyApiMarketInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_market_instance_attribute_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: cloud_api20160201_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: cloud_api20160201_models.ModifyAppRequest,
    ) -> cloud_api20160201_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: cloud_api20160201_models.ModifyAppRequest,
    ) -> cloud_api20160201_models.ModifyAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_app_for_inner_with_options(
        self,
        request: cloud_api20160201_models.ModifyAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyAppForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyAppForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_for_inner(
        self,
        request: cloud_api20160201_models.ModifyAppForInnerRequest,
    ) -> cloud_api20160201_models.ModifyAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_app_for_inner_with_options(request, runtime)

    async def modify_app_for_inner_async(
        self,
        request: cloud_api20160201_models.ModifyAppForInnerRequest,
    ) -> cloud_api20160201_models.ModifyAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_for_inner_with_options_async(request, runtime)

    def modify_group_auth_app_code_for_backend_with_options(
        self,
        request: cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.auth_app_code):
            query['AuthAppCode'] = request.auth_app_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupAuthAppCodeForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_group_auth_app_code_for_backend_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.auth_app_code):
            query['AuthAppCode'] = request.auth_app_code
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroupAuthAppCodeForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_group_auth_app_code_for_backend(
        self,
        request: cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendRequest,
    ) -> cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_group_auth_app_code_for_backend_with_options(request, runtime)

    async def modify_group_auth_app_code_for_backend_async(
        self,
        request: cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendRequest,
    ) -> cloud_api20160201_models.ModifyGroupAuthAppCodeForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_group_auth_app_code_for_backend_with_options_async(request, runtime)

    def modify_secret_key_with_options(
        self,
        request: cloud_api20160201_models.ModifySecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifySecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecretKey',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifySecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_secret_key_with_options_async(
        self,
        request: cloud_api20160201_models.ModifySecretKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifySecretKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.secret_key_id):
            query['SecretKeyId'] = request.secret_key_id
        if not UtilClient.is_unset(request.secret_key_name):
            query['SecretKeyName'] = request.secret_key_name
        if not UtilClient.is_unset(request.secret_value):
            query['SecretValue'] = request.secret_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecretKey',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifySecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_secret_key(
        self,
        request: cloud_api20160201_models.ModifySecretKeyRequest,
    ) -> cloud_api20160201_models.ModifySecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_secret_key_with_options(request, runtime)

    async def modify_secret_key_async(
        self,
        request: cloud_api20160201_models.ModifySecretKeyRequest,
    ) -> cloud_api20160201_models.ModifySecretKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_secret_key_with_options_async(request, runtime)

    def modify_traffic_control_with_options(
        self,
        request: cloud_api20160201_models.ModifyTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyTrafficControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_traffic_control_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyTrafficControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyTrafficControlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_default):
            query['ApiDefault'] = request.api_default
        if not UtilClient.is_unset(request.app_default):
            query['AppDefault'] = request.app_default
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.traffic_control_id):
            query['TrafficControlId'] = request.traffic_control_id
        if not UtilClient.is_unset(request.traffic_control_name):
            query['TrafficControlName'] = request.traffic_control_name
        if not UtilClient.is_unset(request.traffic_control_unit):
            query['TrafficControlUnit'] = request.traffic_control_unit
        if not UtilClient.is_unset(request.user_default):
            query['UserDefault'] = request.user_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTrafficControl',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyTrafficControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_traffic_control(
        self,
        request: cloud_api20160201_models.ModifyTrafficControlRequest,
    ) -> cloud_api20160201_models.ModifyTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_traffic_control_with_options(request, runtime)

    async def modify_traffic_control_async(
        self,
        request: cloud_api20160201_models.ModifyTrafficControlRequest,
    ) -> cloud_api20160201_models.ModifyTrafficControlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_traffic_control_with_options_async(request, runtime)

    def modify_user_white_list_value_by_type_with_options(
        self,
        request: cloud_api20160201_models.ModifyUserWhiteListValueByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyUserWhiteListValueByTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserWhiteListValueByType',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyUserWhiteListValueByTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_white_list_value_by_type_with_options_async(
        self,
        request: cloud_api20160201_models.ModifyUserWhiteListValueByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ModifyUserWhiteListValueByTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.value):
            query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserWhiteListValueByType',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ModifyUserWhiteListValueByTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_white_list_value_by_type(
        self,
        request: cloud_api20160201_models.ModifyUserWhiteListValueByTypeRequest,
    ) -> cloud_api20160201_models.ModifyUserWhiteListValueByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_white_list_value_by_type_with_options(request, runtime)

    async def modify_user_white_list_value_by_type_async(
        self,
        request: cloud_api20160201_models.ModifyUserWhiteListValueByTypeRequest,
    ) -> cloud_api20160201_models.ModifyUserWhiteListValueByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_white_list_value_by_type_with_options_async(request, runtime)

    def reactivate_domain_for_backend_with_options(
        self,
        request: cloud_api20160201_models.ReactivateDomainForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ReactivateDomainForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReactivateDomainForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ReactivateDomainForBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def reactivate_domain_for_backend_with_options_async(
        self,
        request: cloud_api20160201_models.ReactivateDomainForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ReactivateDomainForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliuid):
            query['Aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReactivateDomainForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ReactivateDomainForBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reactivate_domain_for_backend(
        self,
        request: cloud_api20160201_models.ReactivateDomainForBackendRequest,
    ) -> cloud_api20160201_models.ReactivateDomainForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return self.reactivate_domain_for_backend_with_options(request, runtime)

    async def reactivate_domain_for_backend_async(
        self,
        request: cloud_api20160201_models.ReactivateDomainForBackendRequest,
    ) -> cloud_api20160201_models.ReactivateDomainForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reactivate_domain_for_backend_with_options_async(request, runtime)

    def recover_api_from_historical_with_options(
        self,
        request: cloud_api20160201_models.RecoverApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RecoverApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverApiFromHistorical',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RecoverApiFromHistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_api_from_historical_with_options_async(
        self,
        request: cloud_api20160201_models.RecoverApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RecoverApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverApiFromHistorical',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RecoverApiFromHistoricalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_api_from_historical(
        self,
        request: cloud_api20160201_models.RecoverApiFromHistoricalRequest,
    ) -> cloud_api20160201_models.RecoverApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_api_from_historical_with_options(request, runtime)

    async def recover_api_from_historical_async(
        self,
        request: cloud_api20160201_models.RecoverApiFromHistoricalRequest,
    ) -> cloud_api20160201_models.RecoverApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_api_from_historical_with_options_async(request, runtime)

    def recovery_api_define_from_historical_with_options(
        self,
        request: cloud_api20160201_models.RecoveryApiDefineFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RecoveryApiDefineFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiDefineFromHistorical',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RecoveryApiDefineFromHistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_api_define_from_historical_with_options_async(
        self,
        request: cloud_api20160201_models.RecoveryApiDefineFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RecoveryApiDefineFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiDefineFromHistorical',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RecoveryApiDefineFromHistoricalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_api_define_from_historical(
        self,
        request: cloud_api20160201_models.RecoveryApiDefineFromHistoricalRequest,
    ) -> cloud_api20160201_models.RecoveryApiDefineFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return self.recovery_api_define_from_historical_with_options(request, runtime)

    async def recovery_api_define_from_historical_async(
        self,
        request: cloud_api20160201_models.RecoveryApiDefineFromHistoricalRequest,
    ) -> cloud_api20160201_models.RecoveryApiDefineFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recovery_api_define_from_historical_with_options_async(request, runtime)

    def recovery_api_from_historical_with_options(
        self,
        request: cloud_api20160201_models.RecoveryApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RecoveryApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiFromHistorical',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RecoveryApiFromHistoricalResponse(),
            self.call_api(params, req, runtime)
        )

    async def recovery_api_from_historical_with_options_async(
        self,
        request: cloud_api20160201_models.RecoveryApiFromHistoricalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RecoveryApiFromHistoricalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoveryApiFromHistorical',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RecoveryApiFromHistoricalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recovery_api_from_historical(
        self,
        request: cloud_api20160201_models.RecoveryApiFromHistoricalRequest,
    ) -> cloud_api20160201_models.RecoveryApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return self.recovery_api_from_historical_with_options(request, runtime)

    async def recovery_api_from_historical_async(
        self,
        request: cloud_api20160201_models.RecoveryApiFromHistoricalRequest,
    ) -> cloud_api20160201_models.RecoveryApiFromHistoricalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recovery_api_from_historical_with_options_async(request, runtime)

    def refresh_domain_with_options(
        self,
        request: cloud_api20160201_models.RefreshDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RefreshDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RefreshDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_domain_with_options_async(
        self,
        request: cloud_api20160201_models.RefreshDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RefreshDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RefreshDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_domain(
        self,
        request: cloud_api20160201_models.RefreshDomainRequest,
    ) -> cloud_api20160201_models.RefreshDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_domain_with_options(request, runtime)

    async def refresh_domain_async(
        self,
        request: cloud_api20160201_models.RefreshDomainRequest,
    ) -> cloud_api20160201_models.RefreshDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_domain_with_options_async(request, runtime)

    def remove_access_permission_by_apis_with_options(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAccessPermissionByApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_permission_by_apis_with_options_async(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAccessPermissionByApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_access_permission_by_apis(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByApisRequest,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_access_permission_by_apis_with_options(request, runtime)

    async def remove_access_permission_by_apis_async(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByApisRequest,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_access_permission_by_apis_with_options_async(request, runtime)

    def remove_access_permission_by_apps_with_options(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApps',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAccessPermissionByAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_permission_by_apps_with_options_async(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByApps',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAccessPermissionByAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_access_permission_by_apps(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsRequest,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_access_permission_by_apps_with_options(request, runtime)

    async def remove_access_permission_by_apps_async(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsRequest,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_access_permission_by_apps_with_options_async(request, runtime)

    def remove_access_permission_by_apps_for_inner_with_options(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByAppsForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_access_permission_by_apps_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessPermissionByAppsForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_access_permission_by_apps_for_inner(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerRequest,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_access_permission_by_apps_for_inner_with_options(request, runtime)

    async def remove_access_permission_by_apps_for_inner_async(
        self,
        request: cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerRequest,
    ) -> cloud_api20160201_models.RemoveAccessPermissionByAppsForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_access_permission_by_apps_for_inner_with_options_async(request, runtime)

    def remove_all_black_list_with_options(
        self,
        request: cloud_api20160201_models.RemoveAllBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAllBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAllBlackList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAllBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_all_black_list_with_options_async(
        self,
        request: cloud_api20160201_models.RemoveAllBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAllBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAllBlackList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAllBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_all_black_list(
        self,
        request: cloud_api20160201_models.RemoveAllBlackListRequest,
    ) -> cloud_api20160201_models.RemoveAllBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_all_black_list_with_options(request, runtime)

    async def remove_all_black_list_async(
        self,
        request: cloud_api20160201_models.RemoveAllBlackListRequest,
    ) -> cloud_api20160201_models.RemoveAllBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_all_black_list_with_options_async(request, runtime)

    def remove_api_rule_with_options(
        self,
        request: cloud_api20160201_models.RemoveApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApiRule',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveApiRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_api_rule_with_options_async(
        self,
        request: cloud_api20160201_models.RemoveApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApiRule',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveApiRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_api_rule(
        self,
        request: cloud_api20160201_models.RemoveApiRuleRequest,
    ) -> cloud_api20160201_models.RemoveApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_api_rule_with_options(request, runtime)

    async def remove_api_rule_async(
        self,
        request: cloud_api20160201_models.RemoveApiRuleRequest,
    ) -> cloud_api20160201_models.RemoveApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_api_rule_with_options_async(request, runtime)

    def remove_apps_from_api_with_options(
        self,
        request: cloud_api20160201_models.RemoveAppsFromApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAppsFromApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAppsFromApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAppsFromApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_apps_from_api_with_options_async(
        self,
        request: cloud_api20160201_models.RemoveAppsFromApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveAppsFromApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAppsFromApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveAppsFromApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_apps_from_api(
        self,
        request: cloud_api20160201_models.RemoveAppsFromApiRequest,
    ) -> cloud_api20160201_models.RemoveAppsFromApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_apps_from_api_with_options(request, runtime)

    async def remove_apps_from_api_async(
        self,
        request: cloud_api20160201_models.RemoveAppsFromApiRequest,
    ) -> cloud_api20160201_models.RemoveAppsFromApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_apps_from_api_with_options_async(request, runtime)

    def remove_black_list_with_options(
        self,
        request: cloud_api20160201_models.RemoveBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBlackList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_black_list_with_options_async(
        self,
        request: cloud_api20160201_models.RemoveBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.RemoveBlackListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.black_content):
            query['BlackContent'] = request.black_content
        if not UtilClient.is_unset(request.black_type):
            query['BlackType'] = request.black_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBlackList',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.RemoveBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_black_list(
        self,
        request: cloud_api20160201_models.RemoveBlackListRequest,
    ) -> cloud_api20160201_models.RemoveBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_black_list_with_options(request, runtime)

    async def remove_black_list_async(
        self,
        request: cloud_api20160201_models.RemoveBlackListRequest,
    ) -> cloud_api20160201_models.RemoveBlackListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_black_list_with_options_async(request, runtime)

    def reset_app_code_with_options(
        self,
        request: cloud_api20160201_models.ResetAppCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetAppCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppCode',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetAppCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_code_with_options_async(
        self,
        request: cloud_api20160201_models.ResetAppCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetAppCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppCode',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetAppCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_code(
        self,
        request: cloud_api20160201_models.ResetAppCodeRequest,
    ) -> cloud_api20160201_models.ResetAppCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_app_code_with_options(request, runtime)

    async def reset_app_code_async(
        self,
        request: cloud_api20160201_models.ResetAppCodeRequest,
    ) -> cloud_api20160201_models.ResetAppCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_code_with_options_async(request, runtime)

    def reset_app_code_for_inner_with_options(
        self,
        request: cloud_api20160201_models.ResetAppCodeForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetAppCodeForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.new_app_code):
            query['NewAppCode'] = request.new_app_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppCodeForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetAppCodeForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_code_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.ResetAppCodeForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetAppCodeForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_code):
            query['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.new_app_code):
            query['NewAppCode'] = request.new_app_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppCodeForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetAppCodeForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_code_for_inner(
        self,
        request: cloud_api20160201_models.ResetAppCodeForInnerRequest,
    ) -> cloud_api20160201_models.ResetAppCodeForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_app_code_for_inner_with_options(request, runtime)

    async def reset_app_code_for_inner_async(
        self,
        request: cloud_api20160201_models.ResetAppCodeForInnerRequest,
    ) -> cloud_api20160201_models.ResetAppCodeForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_code_for_inner_with_options_async(request, runtime)

    def reset_app_key_secret_with_options(
        self,
        request: cloud_api20160201_models.ResetAppKeySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetAppKeySecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppKeySecret',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetAppKeySecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_app_key_secret_with_options_async(
        self,
        request: cloud_api20160201_models.ResetAppKeySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetAppKeySecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAppKeySecret',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetAppKeySecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_app_key_secret(
        self,
        request: cloud_api20160201_models.ResetAppKeySecretRequest,
    ) -> cloud_api20160201_models.ResetAppKeySecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_app_key_secret_with_options(request, runtime)

    async def reset_app_key_secret_async(
        self,
        request: cloud_api20160201_models.ResetAppKeySecretRequest,
    ) -> cloud_api20160201_models.ResetAppKeySecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_key_secret_with_options_async(request, runtime)

    def reset_secret_by_app_key_for_inner_with_options(
        self,
        request: cloud_api20160201_models.ResetSecretByAppKeyForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetSecretByAppKeyForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.new_app_key):
            query['NewAppKey'] = request.new_app_key
        if not UtilClient.is_unset(request.new_app_secret):
            query['NewAppSecret'] = request.new_app_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSecretByAppKeyForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetSecretByAppKeyForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_secret_by_app_key_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.ResetSecretByAppKeyForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.ResetSecretByAppKeyForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.new_app_key):
            query['NewAppKey'] = request.new_app_key
        if not UtilClient.is_unset(request.new_app_secret):
            query['NewAppSecret'] = request.new_app_secret
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSecretByAppKeyForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.ResetSecretByAppKeyForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_secret_by_app_key_for_inner(
        self,
        request: cloud_api20160201_models.ResetSecretByAppKeyForInnerRequest,
    ) -> cloud_api20160201_models.ResetSecretByAppKeyForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_secret_by_app_key_for_inner_with_options(request, runtime)

    async def reset_secret_by_app_key_for_inner_async(
        self,
        request: cloud_api20160201_models.ResetSecretByAppKeyForInnerRequest,
    ) -> cloud_api20160201_models.ResetSecretByAppKeyForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_secret_by_app_key_for_inner_with_options_async(request, runtime)

    def set_access_permission_by_apis_with_options(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionByApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionByApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_permission_by_apis_with_options_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionByApisResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionByApis',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionByApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_permission_by_apis(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByApisRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_access_permission_by_apis_with_options(request, runtime)

    async def set_access_permission_by_apis_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByApisRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionByApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_access_permission_by_apis_with_options_async(request, runtime)

    def set_access_permission_by_group_for_backend_with_options(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByGroupForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionByGroupForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionByGroupForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionByGroupForBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_permission_by_group_for_backend_with_options_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByGroupForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionByGroupForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionByGroupForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionByGroupForBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_permission_by_group_for_backend(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByGroupForBackendRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionByGroupForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_access_permission_by_group_for_backend_with_options(request, runtime)

    async def set_access_permission_by_group_for_backend_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionByGroupForBackendRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionByGroupForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_access_permission_by_group_for_backend_with_options_async(request, runtime)

    def set_access_permissions_with_options(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissions',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_permissions_with_options_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissions',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_permissions(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_access_permissions_with_options(request, runtime)

    async def set_access_permissions_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_access_permissions_with_options_async(request, runtime)

    def set_access_permissions_for_inner_with_options(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionsForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionsForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionsForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_access_permissions_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetAccessPermissionsForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessPermissionsForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetAccessPermissionsForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_access_permissions_for_inner(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsForInnerRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionsForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_access_permissions_for_inner_with_options(request, runtime)

    async def set_access_permissions_for_inner_async(
        self,
        request: cloud_api20160201_models.SetAccessPermissionsForInnerRequest,
    ) -> cloud_api20160201_models.SetAccessPermissionsForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_access_permissions_for_inner_with_options_async(request, runtime)

    def set_api_rule_with_options(
        self,
        request: cloud_api20160201_models.SetApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApiRule',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetApiRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_api_rule_with_options_async(
        self,
        request: cloud_api20160201_models.SetApiRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetApiRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_ids):
            query['ApiIds'] = request.api_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApiRule',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetApiRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_api_rule(
        self,
        request: cloud_api20160201_models.SetApiRuleRequest,
    ) -> cloud_api20160201_models.SetApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_api_rule_with_options(request, runtime)

    async def set_api_rule_async(
        self,
        request: cloud_api20160201_models.SetApiRuleRequest,
    ) -> cloud_api20160201_models.SetApiRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_api_rule_with_options_async(request, runtime)

    def set_domain_with_options(
        self,
        request: cloud_api20160201_models.SetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_with_options_async(
        self,
        request: cloud_api20160201_models.SetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomain',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain(
        self,
        request: cloud_api20160201_models.SetDomainRequest,
    ) -> cloud_api20160201_models.SetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_with_options(request, runtime)

    async def set_domain_async(
        self,
        request: cloud_api20160201_models.SetDomainRequest,
    ) -> cloud_api20160201_models.SetDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_with_options_async(request, runtime)

    def set_domain_certificate_with_options(
        self,
        request: cloud_api20160201_models.SetDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_certificate_with_options_async(
        self,
        request: cloud_api20160201_models.SetDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetDomainCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainCertificate',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_certificate(
        self,
        request: cloud_api20160201_models.SetDomainCertificateRequest,
    ) -> cloud_api20160201_models.SetDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_certificate_with_options(request, runtime)

    async def set_domain_certificate_async(
        self,
        request: cloud_api20160201_models.SetDomainCertificateRequest,
    ) -> cloud_api20160201_models.SetDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_certificate_with_options_async(request, runtime)

    def set_domain_for_backend_with_options(
        self,
        request: cloud_api20160201_models.SetDomainForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetDomainForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_private_key):
            query['CertificatePrivateKey'] = request.certificate_private_key
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetDomainForBackendResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_for_backend_with_options_async(
        self,
        request: cloud_api20160201_models.SetDomainForBackendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetDomainForBackendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_body):
            query['CertificateBody'] = request.certificate_body
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_private_key):
            query['CertificatePrivateKey'] = request.certificate_private_key
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainForBackend',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetDomainForBackendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_for_backend(
        self,
        request: cloud_api20160201_models.SetDomainForBackendRequest,
    ) -> cloud_api20160201_models.SetDomainForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_domain_for_backend_with_options(request, runtime)

    async def set_domain_for_backend_async(
        self,
        request: cloud_api20160201_models.SetDomainForBackendRequest,
    ) -> cloud_api20160201_models.SetDomainForBackendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_for_backend_with_options_async(request, runtime)

    def set_mock_integration_with_options(
        self,
        request: cloud_api20160201_models.SetMockIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetMockIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.mock):
            query['Mock'] = request.mock
        if not UtilClient.is_unset(request.mock_result):
            query['MockResult'] = request.mock_result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMockIntegration',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetMockIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_mock_integration_with_options_async(
        self,
        request: cloud_api20160201_models.SetMockIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetMockIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.mock):
            query['Mock'] = request.mock
        if not UtilClient.is_unset(request.mock_result):
            query['MockResult'] = request.mock_result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMockIntegration',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetMockIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_mock_integration(
        self,
        request: cloud_api20160201_models.SetMockIntegrationRequest,
    ) -> cloud_api20160201_models.SetMockIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_mock_integration_with_options(request, runtime)

    async def set_mock_integration_async(
        self,
        request: cloud_api20160201_models.SetMockIntegrationRequest,
    ) -> cloud_api20160201_models.SetMockIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_mock_integration_with_options_async(request, runtime)

    def set_purchased_api_group_status_with_options(
        self,
        request: cloud_api20160201_models.SetPurchasedApiGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetPurchasedApiGroupStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.billing_status):
            query['BillingStatus'] = request.billing_status
        if not UtilClient.is_unset(request.close_order):
            query['CloseOrder'] = request.close_order
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPurchasedApiGroupStatus',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetPurchasedApiGroupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_purchased_api_group_status_with_options_async(
        self,
        request: cloud_api20160201_models.SetPurchasedApiGroupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SetPurchasedApiGroupStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.billing_status):
            query['BillingStatus'] = request.billing_status
        if not UtilClient.is_unset(request.close_order):
            query['CloseOrder'] = request.close_order
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPurchasedApiGroupStatus',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SetPurchasedApiGroupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_purchased_api_group_status(
        self,
        request: cloud_api20160201_models.SetPurchasedApiGroupStatusRequest,
    ) -> cloud_api20160201_models.SetPurchasedApiGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_purchased_api_group_status_with_options(request, runtime)

    async def set_purchased_api_group_status_async(
        self,
        request: cloud_api20160201_models.SetPurchasedApiGroupStatusRequest,
    ) -> cloud_api20160201_models.SetPurchasedApiGroupStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_purchased_api_group_status_with_options_async(request, runtime)

    def switch_api_with_options(
        self,
        request: cloud_api20160201_models.SwitchApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SwitchApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SwitchApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_api_with_options_async(
        self,
        request: cloud_api20160201_models.SwitchApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SwitchApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchApi',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SwitchApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_api(
        self,
        request: cloud_api20160201_models.SwitchApiRequest,
    ) -> cloud_api20160201_models.SwitchApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_api_with_options(request, runtime)

    async def switch_api_async(
        self,
        request: cloud_api20160201_models.SwitchApiRequest,
    ) -> cloud_api20160201_models.SwitchApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_api_with_options_async(request, runtime)

    def switch_api_for_inner_with_options(
        self,
        request: cloud_api20160201_models.SwitchApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SwitchApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SwitchApiForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_api_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.SwitchApiForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SwitchApiForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        if not UtilClient.is_unset(request.stage_name):
            query['StageName'] = request.stage_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchApiForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SwitchApiForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_api_for_inner(
        self,
        request: cloud_api20160201_models.SwitchApiForInnerRequest,
    ) -> cloud_api20160201_models.SwitchApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_api_for_inner_with_options(request, runtime)

    async def switch_api_for_inner_async(
        self,
        request: cloud_api20160201_models.SwitchApiForInnerRequest,
    ) -> cloud_api20160201_models.SwitchApiForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_api_for_inner_with_options_async(request, runtime)

    def syn_create_app_for_inner_with_options(
        self,
        request: cloud_api20160201_models.SynCreateAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SynCreateAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_secret):
            query['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynCreateAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SynCreateAppForInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def syn_create_app_for_inner_with_options_async(
        self,
        request: cloud_api20160201_models.SynCreateAppForInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.SynCreateAppForInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_secret):
            query['AppSecret'] = request.app_secret
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynCreateAppForInner',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.SynCreateAppForInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def syn_create_app_for_inner(
        self,
        request: cloud_api20160201_models.SynCreateAppForInnerRequest,
    ) -> cloud_api20160201_models.SynCreateAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.syn_create_app_for_inner_with_options(request, runtime)

    async def syn_create_app_for_inner_async(
        self,
        request: cloud_api20160201_models.SynCreateAppForInnerRequest,
    ) -> cloud_api20160201_models.SynCreateAppForInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.syn_create_app_for_inner_with_options_async(request, runtime)

    def tag_resources_system_tags_with_options(
        self,
        request: cloud_api20160201_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.TagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResourcesSystemTags',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.TagResourcesSystemTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_system_tags_with_options_async(
        self,
        request: cloud_api20160201_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.TagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResourcesSystemTags',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.TagResourcesSystemTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources_system_tags(
        self,
        request: cloud_api20160201_models.TagResourcesSystemTagsRequest,
    ) -> cloud_api20160201_models.TagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_system_tags_with_options(request, runtime)

    async def tag_resources_system_tags_async(
        self,
        request: cloud_api20160201_models.TagResourcesSystemTagsRequest,
    ) -> cloud_api20160201_models.TagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_system_tags_with_options_async(request, runtime)

    def untag_resources_system_tags_with_options(
        self,
        request: cloud_api20160201_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.UntagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResourcesSystemTags',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.UntagResourcesSystemTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_system_tags_with_options_async(
        self,
        request: cloud_api20160201_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.UntagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tag_owner_bid):
            query['TagOwnerBid'] = request.tag_owner_bid
        if not UtilClient.is_unset(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResourcesSystemTags',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.UntagResourcesSystemTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources_system_tags(
        self,
        request: cloud_api20160201_models.UntagResourcesSystemTagsRequest,
    ) -> cloud_api20160201_models.UntagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_system_tags_with_options(request, runtime)

    async def untag_resources_system_tags_async(
        self,
        request: cloud_api20160201_models.UntagResourcesSystemTagsRequest,
    ) -> cloud_api20160201_models.UntagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_system_tags_with_options_async(request, runtime)

    def vip_migration_with_options(
        self,
        request: cloud_api20160201_models.VipMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VipMigrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_vip):
            query['NewVip'] = request.new_vip
        if not UtilClient.is_unset(request.original_vip):
            query['OriginalVip'] = request.original_vip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VipMigration',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VipMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def vip_migration_with_options_async(
        self,
        request: cloud_api20160201_models.VipMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VipMigrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_vip):
            query['NewVip'] = request.new_vip
        if not UtilClient.is_unset(request.original_vip):
            query['OriginalVip'] = request.original_vip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VipMigration',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VipMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vip_migration(
        self,
        request: cloud_api20160201_models.VipMigrationRequest,
    ) -> cloud_api20160201_models.VipMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.vip_migration_with_options(request, runtime)

    async def vip_migration_async(
        self,
        request: cloud_api20160201_models.VipMigrationRequest,
    ) -> cloud_api20160201_models.VipMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vip_migration_with_options_async(request, runtime)

    def vip_migration_by_uid_with_options(
        self,
        request: cloud_api20160201_models.VipMigrationByUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VipMigrationByUidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_vip):
            query['NewVip'] = request.new_vip
        if not UtilClient.is_unset(request.original_vip):
            query['OriginalVip'] = request.original_vip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VipMigrationByUid',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VipMigrationByUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def vip_migration_by_uid_with_options_async(
        self,
        request: cloud_api20160201_models.VipMigrationByUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VipMigrationByUidResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_vip):
            query['NewVip'] = request.new_vip
        if not UtilClient.is_unset(request.original_vip):
            query['OriginalVip'] = request.original_vip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VipMigrationByUid',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VipMigrationByUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vip_migration_by_uid(
        self,
        request: cloud_api20160201_models.VipMigrationByUidRequest,
    ) -> cloud_api20160201_models.VipMigrationByUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.vip_migration_by_uid_with_options(request, runtime)

    async def vip_migration_by_uid_async(
        self,
        request: cloud_api20160201_models.VipMigrationByUidRequest,
    ) -> cloud_api20160201_models.VipMigrationByUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vip_migration_by_uid_with_options_async(request, runtime)

    def vpc_add_app_server_with_options(
        self,
        request: cloud_api20160201_models.VpcAddAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcAddAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcAddAppServer',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcAddAppServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_add_app_server_with_options_async(
        self,
        request: cloud_api20160201_models.VpcAddAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcAddAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcAddAppServer',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcAddAppServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_add_app_server(
        self,
        request: cloud_api20160201_models.VpcAddAppServerRequest,
    ) -> cloud_api20160201_models.VpcAddAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_add_app_server_with_options(request, runtime)

    async def vpc_add_app_server_async(
        self,
        request: cloud_api20160201_models.VpcAddAppServerRequest,
    ) -> cloud_api20160201_models.VpcAddAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_add_app_server_with_options_async(request, runtime)

    def vpc_create_address_pool_with_options(
        self,
        request: cloud_api20160201_models.VpcCreateAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcCreateAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcCreateAddressPool',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcCreateAddressPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_create_address_pool_with_options_async(
        self,
        request: cloud_api20160201_models.VpcCreateAddressPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcCreateAddressPoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcCreateAddressPool',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcCreateAddressPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_create_address_pool(
        self,
        request: cloud_api20160201_models.VpcCreateAddressPoolRequest,
    ) -> cloud_api20160201_models.VpcCreateAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_create_address_pool_with_options(request, runtime)

    async def vpc_create_address_pool_async(
        self,
        request: cloud_api20160201_models.VpcCreateAddressPoolRequest,
    ) -> cloud_api20160201_models.VpcCreateAddressPoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_create_address_pool_with_options_async(request, runtime)

    def vpc_query_app_servers_with_options(
        self,
        request: cloud_api20160201_models.VpcQueryAppServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcQueryAppServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcQueryAppServers',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcQueryAppServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_query_app_servers_with_options_async(
        self,
        request: cloud_api20160201_models.VpcQueryAppServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcQueryAppServersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_pool_id):
            query['AddressPoolId'] = request.address_pool_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcQueryAppServers',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcQueryAppServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_query_app_servers(
        self,
        request: cloud_api20160201_models.VpcQueryAppServersRequest,
    ) -> cloud_api20160201_models.VpcQueryAppServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_query_app_servers_with_options(request, runtime)

    async def vpc_query_app_servers_async(
        self,
        request: cloud_api20160201_models.VpcQueryAppServersRequest,
    ) -> cloud_api20160201_models.VpcQueryAppServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_query_app_servers_with_options_async(request, runtime)

    def vpc_register_app_with_options(
        self,
        request: cloud_api20160201_models.VpcRegisterAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcRegisterAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcRegisterApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcRegisterAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_register_app_with_options_async(
        self,
        request: cloud_api20160201_models.VpcRegisterAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcRegisterAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcRegisterApp',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcRegisterAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_register_app(
        self,
        request: cloud_api20160201_models.VpcRegisterAppRequest,
    ) -> cloud_api20160201_models.VpcRegisterAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_register_app_with_options(request, runtime)

    async def vpc_register_app_async(
        self,
        request: cloud_api20160201_models.VpcRegisterAppRequest,
    ) -> cloud_api20160201_models.VpcRegisterAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_register_app_with_options_async(request, runtime)

    def vpc_remove_app_server_with_options(
        self,
        request: cloud_api20160201_models.VpcRemoveAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcRemoveAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcRemoveAppServer',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcRemoveAppServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def vpc_remove_app_server_with_options_async(
        self,
        request: cloud_api20160201_models.VpcRemoveAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_api20160201_models.VpcRemoveAppServerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.server_ip):
            query['ServerIp'] = request.server_ip
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VpcRemoveAppServer',
            version='2016-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloud_api20160201_models.VpcRemoveAppServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vpc_remove_app_server(
        self,
        request: cloud_api20160201_models.VpcRemoveAppServerRequest,
    ) -> cloud_api20160201_models.VpcRemoveAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.vpc_remove_app_server_with_options(request, runtime)

    async def vpc_remove_app_server_async(
        self,
        request: cloud_api20160201_models.VpcRemoveAppServerRequest,
    ) -> cloud_api20160201_models.VpcRemoveAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.vpc_remove_app_server_with_options_async(request, runtime)
