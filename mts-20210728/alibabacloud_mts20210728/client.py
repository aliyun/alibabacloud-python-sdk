# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mts20210728 import models as mts_20210728_models
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
            'ap-northeast-2-pop': 'mts.aliyuncs.com',
            'ap-southeast-2': 'mts.aliyuncs.com',
            'ap-southeast-3': 'mts.aliyuncs.com',
            'cn-beijing-finance-1': 'mts.aliyuncs.com',
            'cn-beijing-finance-pop': 'mts.aliyuncs.com',
            'cn-beijing-gov-1': 'mts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mts.aliyuncs.com',
            'cn-chengdu': 'mts.aliyuncs.com',
            'cn-edge-1': 'mts.aliyuncs.com',
            'cn-fujian': 'mts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mts.aliyuncs.com',
            'cn-hangzhou-finance': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mts.aliyuncs.com',
            'cn-hangzhou-test-306': 'mts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'mts.aliyuncs.com',
            'cn-north-2-gov-1': 'mts.aliyuncs.com',
            'cn-qingdao-nebula': 'mts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mts.aliyuncs.com',
            'cn-shanghai-finance-1': 'mts.aliyuncs.com',
            'cn-shanghai-inner': 'mts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mts.aliyuncs.com',
            'cn-shenzhen-inner': 'mts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mts.aliyuncs.com',
            'cn-wuhan': 'mts.aliyuncs.com',
            'cn-wulanchabu': 'mts.aliyuncs.com',
            'cn-yushanfang': 'mts.aliyuncs.com',
            'cn-zhangbei': 'mts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mts.aliyuncs.com',
            'eu-west-1-oxs': 'mts.aliyuncs.com',
            'me-east-1': 'mts.aliyuncs.com',
            'rus-west-1-pop': 'mts.aliyuncs.com',
            'us-east-1': 'mts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def query_trace_mu(
        self,
        request: mts_20210728_models.QueryTraceMuRequest,
    ) -> mts_20210728_models.QueryTraceMuResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_trace_mu_with_options(request, headers, runtime)

    async def query_trace_mu_async(
        self,
        request: mts_20210728_models.QueryTraceMuRequest,
    ) -> mts_20210728_models.QueryTraceMuResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_trace_mu_with_options_async(request, headers, runtime)

    def query_trace_mu_with_options(
        self,
        request: mts_20210728_models.QueryTraceMuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryTraceMuResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryTraceMuResponse(),
            self.do_roarequest('QueryTraceMu', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryTraceM3u8', 'json', req, runtime)
        )

    async def query_trace_mu_with_options_async(
        self,
        request: mts_20210728_models.QueryTraceMuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryTraceMuResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryTraceMuResponse(),
            await self.do_roarequest_async('QueryTraceMu', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryTraceM3u8', 'json', req, runtime)
        )

    def submit_image_copyright(
        self,
        request: mts_20210728_models.SubmitImageCopyrightRequest,
    ) -> mts_20210728_models.SubmitImageCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_image_copyright_with_options(request, headers, runtime)

    async def submit_image_copyright_async(
        self,
        request: mts_20210728_models.SubmitImageCopyrightRequest,
    ) -> mts_20210728_models.SubmitImageCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_image_copyright_with_options_async(request, headers, runtime)

    def submit_image_copyright_with_options(
        self,
        request: mts_20210728_models.SubmitImageCopyrightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitImageCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitImageCopyrightResponse(),
            self.do_roarequest('SubmitImageCopyright', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitImageCopyright', 'json', req, runtime)
        )

    async def submit_image_copyright_with_options_async(
        self,
        request: mts_20210728_models.SubmitImageCopyrightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitImageCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitImageCopyrightResponse(),
            await self.do_roarequest_async('SubmitImageCopyright', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitImageCopyright', 'json', req, runtime)
        )

    def query_image_copyright(
        self,
        request: mts_20210728_models.QueryImageCopyrightRequest,
    ) -> mts_20210728_models.QueryImageCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_image_copyright_with_options(request, headers, runtime)

    async def query_image_copyright_async(
        self,
        request: mts_20210728_models.QueryImageCopyrightRequest,
    ) -> mts_20210728_models.QueryImageCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_image_copyright_with_options_async(request, headers, runtime)

    def query_image_copyright_with_options(
        self,
        request: mts_20210728_models.QueryImageCopyrightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryImageCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryImageCopyrightResponse(),
            self.do_roarequest('QueryImageCopyright', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryImageCopyright', 'json', req, runtime)
        )

    async def query_image_copyright_with_options_async(
        self,
        request: mts_20210728_models.QueryImageCopyrightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryImageCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryImageCopyrightResponse(),
            await self.do_roarequest_async('QueryImageCopyright', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryImageCopyright', 'json', req, runtime)
        )

    def query_copyright(
        self,
        request: mts_20210728_models.QueryCopyrightRequest,
    ) -> mts_20210728_models.QueryCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_copyright_with_options(request, headers, runtime)

    async def query_copyright_async(
        self,
        request: mts_20210728_models.QueryCopyrightRequest,
    ) -> mts_20210728_models.QueryCopyrightResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_copyright_with_options_async(request, headers, runtime)

    def query_copyright_with_options(
        self,
        request: mts_20210728_models.QueryCopyrightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryCopyrightResponse(),
            self.do_roarequest('QueryCopyright', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryCopyrightJob', 'json', req, runtime)
        )

    async def query_copyright_with_options_async(
        self,
        request: mts_20210728_models.QueryCopyrightRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryCopyrightResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.create_time_end):
            body['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            body['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryCopyrightResponse(),
            await self.do_roarequest_async('QueryCopyright', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryCopyrightJob', 'json', req, runtime)
        )

    def submit_tracemu(
        self,
        request: mts_20210728_models.SubmitTracemuRequest,
    ) -> mts_20210728_models.SubmitTracemuResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_tracemu_with_options(request, headers, runtime)

    async def submit_tracemu_async(
        self,
        request: mts_20210728_models.SubmitTracemuRequest,
    ) -> mts_20210728_models.SubmitTracemuResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_tracemu_with_options_async(request, headers, runtime)

    def submit_tracemu_with_options(
        self,
        request: mts_20210728_models.SubmitTracemuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitTracemuResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.trace):
            body['Trace'] = request.trace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitTracemuResponse(),
            self.do_roarequest('SubmitTracemu', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitTraceM3u8', 'json', req, runtime)
        )

    async def submit_tracemu_with_options_async(
        self,
        request: mts_20210728_models.SubmitTracemuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitTracemuResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.trace):
            body['Trace'] = request.trace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitTracemuResponse(),
            await self.do_roarequest_async('SubmitTracemu', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitTraceM3u8', 'json', req, runtime)
        )

    def query_trace_ab(
        self,
        request: mts_20210728_models.QueryTraceAbRequest,
    ) -> mts_20210728_models.QueryTraceAbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_trace_ab_with_options(request, headers, runtime)

    async def query_trace_ab_async(
        self,
        request: mts_20210728_models.QueryTraceAbRequest,
    ) -> mts_20210728_models.QueryTraceAbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_trace_ab_with_options_async(request, headers, runtime)

    def query_trace_ab_with_options(
        self,
        request: mts_20210728_models.QueryTraceAbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryTraceAbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryTraceAbResponse(),
            self.do_roarequest('QueryTraceAb', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryTraceAb', 'json', req, runtime)
        )

    async def query_trace_ab_with_options_async(
        self,
        request: mts_20210728_models.QueryTraceAbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.QueryTraceAbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.media_id):
            body['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.QueryTraceAbResponse(),
            await self.do_roarequest_async('QueryTraceAb', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/queryTraceAb', 'json', req, runtime)
        )

    def submit_trace_ab(
        self,
        request: mts_20210728_models.SubmitTraceAbRequest,
    ) -> mts_20210728_models.SubmitTraceAbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_trace_ab_with_options(request, headers, runtime)

    async def submit_trace_ab_async(
        self,
        request: mts_20210728_models.SubmitTraceAbRequest,
    ) -> mts_20210728_models.SubmitTraceAbResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_trace_ab_with_options_async(request, headers, runtime)

    def submit_trace_ab_with_options(
        self,
        request: mts_20210728_models.SubmitTraceAbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitTraceAbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitTraceAbResponse(),
            self.do_roarequest('SubmitTraceAb', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitTraceAb', 'json', req, runtime)
        )

    async def submit_trace_ab_with_options_async(
        self,
        request: mts_20210728_models.SubmitTraceAbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitTraceAbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitTraceAbResponse(),
            await self.do_roarequest_async('SubmitTraceAb', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitTraceAb', 'json', req, runtime)
        )

    def submit_copyright_job(
        self,
        request: mts_20210728_models.SubmitCopyrightJobRequest,
    ) -> mts_20210728_models.SubmitCopyrightJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_copyright_job_with_options(request, headers, runtime)

    async def submit_copyright_job_async(
        self,
        request: mts_20210728_models.SubmitCopyrightJobRequest,
    ) -> mts_20210728_models.SubmitCopyrightJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_copyright_job_with_options_async(request, headers, runtime)

    def submit_copyright_job_with_options(
        self,
        request: mts_20210728_models.SubmitCopyrightJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitCopyrightJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_time):
            body['TotalTime'] = request.total_time
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitCopyrightJobResponse(),
            self.do_roarequest('SubmitCopyrightJob', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitCopyrightJob', 'json', req, runtime)
        )

    async def submit_copyright_job_with_options_async(
        self,
        request: mts_20210728_models.SubmitCopyrightJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> mts_20210728_models.SubmitCopyrightJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.call_back):
            body['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.input):
            body['Input'] = request.input
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_time):
            body['TotalTime'] = request.total_time
        if not UtilClient.is_unset(request.output):
            body['Output'] = request.output
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            mts_20210728_models.SubmitCopyrightJobResponse(),
            await self.do_roarequest_async('SubmitCopyrightJob', '2021-07-28', 'HTTPS', 'POST', 'AK', f'/submitCopyrightJob', 'json', req, runtime)
        )
