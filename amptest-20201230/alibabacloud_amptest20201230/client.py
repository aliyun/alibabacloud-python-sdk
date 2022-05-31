# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_amptest20201230 import models as amp_test_20201230_models
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
        self._endpoint = self.get_endpoint('amptest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_rules_with_options(
        self,
        tmp_req: amp_test_20201230_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.CreateRulesResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.CreateRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.CreateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rules_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.CreateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.CreateRulesResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.CreateRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.CreateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rules(
        self,
        request: amp_test_20201230_models.CreateRulesRequest,
    ) -> amp_test_20201230_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    async def create_rules_async(
        self,
        request: amp_test_20201230_models.CreateRulesRequest,
    ) -> amp_test_20201230_models.CreateRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rules_with_options_async(request, runtime)

    def huicheng_test_gray_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGray',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGray',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray(
        self,
        request: amp_test_20201230_models.HuichengTestGrayRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_with_options(request, runtime)

    async def huicheng_test_gray_async(
        self,
        request: amp_test_20201230_models.HuichengTestGrayRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_with_options_async(request, runtime)

    def huicheng_test_gray_eight_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayEightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayEightResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayEightShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayEight',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayEightResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_eight_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayEightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayEightResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayEightShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayEight',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayEightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_eight(
        self,
        request: amp_test_20201230_models.HuichengTestGrayEightRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayEightResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_eight_with_options(request, runtime)

    async def huicheng_test_gray_eight_async(
        self,
        request: amp_test_20201230_models.HuichengTestGrayEightRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayEightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_eight_with_options_async(request, runtime)

    def huicheng_test_gray_fifth_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayFifthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayFifthResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayFifthShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayFifth',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayFifthResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_fifth_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayFifthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayFifthResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayFifthShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayFifth',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayFifthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_fifth(
        self,
        request: amp_test_20201230_models.HuichengTestGrayFifthRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayFifthResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_fifth_with_options(request, runtime)

    async def huicheng_test_gray_fifth_async(
        self,
        request: amp_test_20201230_models.HuichengTestGrayFifthRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayFifthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_fifth_with_options_async(request, runtime)

    def huicheng_test_gray_fourth_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayFourthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayFourthResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayFourthShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayFourth',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayFourthResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_fourth_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayFourthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayFourthResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayFourthShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayFourth',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayFourthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_fourth(
        self,
        request: amp_test_20201230_models.HuichengTestGrayFourthRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayFourthResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_fourth_with_options(request, runtime)

    async def huicheng_test_gray_fourth_async(
        self,
        request: amp_test_20201230_models.HuichengTestGrayFourthRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayFourthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_fourth_with_options_async(request, runtime)

    def huicheng_test_gray_nine_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayNineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayNineResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayNineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayNine',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayNineResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_nine_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayNineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayNineResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayNineShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayNine',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayNineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_nine(
        self,
        request: amp_test_20201230_models.HuichengTestGrayNineRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayNineResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_nine_with_options(request, runtime)

    async def huicheng_test_gray_nine_async(
        self,
        request: amp_test_20201230_models.HuichengTestGrayNineRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayNineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_nine_with_options_async(request, runtime)

    def huicheng_test_gray_second_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGraySecondRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGraySecondResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGraySecondShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGraySecond',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGraySecondResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_second_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGraySecondRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGraySecondResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGraySecondShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGraySecond',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGraySecondResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_second(
        self,
        request: amp_test_20201230_models.HuichengTestGraySecondRequest,
    ) -> amp_test_20201230_models.HuichengTestGraySecondResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_second_with_options(request, runtime)

    async def huicheng_test_gray_second_async(
        self,
        request: amp_test_20201230_models.HuichengTestGraySecondRequest,
    ) -> amp_test_20201230_models.HuichengTestGraySecondResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_second_with_options_async(request, runtime)

    def huicheng_test_gray_seven_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGraySevenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGraySevenResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGraySevenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGraySeven',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGraySevenResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_seven_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGraySevenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGraySevenResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGraySevenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGraySeven',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGraySevenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_seven(
        self,
        request: amp_test_20201230_models.HuichengTestGraySevenRequest,
    ) -> amp_test_20201230_models.HuichengTestGraySevenResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_seven_with_options(request, runtime)

    async def huicheng_test_gray_seven_async(
        self,
        request: amp_test_20201230_models.HuichengTestGraySevenRequest,
    ) -> amp_test_20201230_models.HuichengTestGraySevenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_seven_with_options_async(request, runtime)

    def huicheng_test_gray_six_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGraySixRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGraySixResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGraySixShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGraySix',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGraySixResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_six_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGraySixRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGraySixResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGraySixShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGraySix',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGraySixResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_six(
        self,
        request: amp_test_20201230_models.HuichengTestGraySixRequest,
    ) -> amp_test_20201230_models.HuichengTestGraySixResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_six_with_options(request, runtime)

    async def huicheng_test_gray_six_async(
        self,
        request: amp_test_20201230_models.HuichengTestGraySixRequest,
    ) -> amp_test_20201230_models.HuichengTestGraySixResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_six_with_options_async(request, runtime)

    def huicheng_test_gray_ten_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayTenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayTenResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayTenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayTen',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayTenResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_ten_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayTenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayTenResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayTenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayTen',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayTenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_ten(
        self,
        request: amp_test_20201230_models.HuichengTestGrayTenRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayTenResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_ten_with_options(request, runtime)

    async def huicheng_test_gray_ten_async(
        self,
        request: amp_test_20201230_models.HuichengTestGrayTenRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayTenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_ten_with_options_async(request, runtime)

    def huicheng_test_gray_third_with_options(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayThirdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayThirdResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayThirdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayThird',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayThirdResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_gray_third_with_options_async(
        self,
        tmp_req: amp_test_20201230_models.HuichengTestGrayThirdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestGrayThirdResponse:
        UtilClient.validate_model(tmp_req)
        request = amp_test_20201230_models.HuichengTestGrayThirdShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.home):
            request.home_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.home), 'Home', 'json')
        query = {}
        if not UtilClient.is_unset(request.home_shrink):
            query['Home'] = request.home_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HuichengTestGrayThird',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestGrayThirdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_gray_third(
        self,
        request: amp_test_20201230_models.HuichengTestGrayThirdRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayThirdResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_gray_third_with_options(request, runtime)

    async def huicheng_test_gray_third_async(
        self,
        request: amp_test_20201230_models.HuichengTestGrayThirdRequest,
    ) -> amp_test_20201230_models.HuichengTestGrayThirdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_gray_third_with_options_async(request, runtime)

    def huicheng_test_resource_owner_id_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestResourceOwnerIdResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='HuichengTestResourceOwnerId',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestResourceOwnerIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def huicheng_test_resource_owner_id_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengTestResourceOwnerIdResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='HuichengTestResourceOwnerId',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengTestResourceOwnerIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huicheng_test_resource_owner_id(self) -> amp_test_20201230_models.HuichengTestResourceOwnerIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.huicheng_test_resource_owner_id_with_options(runtime)

    async def huicheng_test_resource_owner_id_async(self) -> amp_test_20201230_models.HuichengTestResourceOwnerIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huicheng_test_resource_owner_id_with_options_async(runtime)

    def huichenget_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengetResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Huichenget',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengetResponse(),
            self.call_api(params, req, runtime)
        )

    async def huichenget_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengetResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Huichenget',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huichenget(self) -> amp_test_20201230_models.HuichengetResponse:
        runtime = util_models.RuntimeOptions()
        return self.huichenget_with_options(runtime)

    async def huichenget_async(self) -> amp_test_20201230_models.HuichengetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huichenget_with_options_async(runtime)

    def huichengetest_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengetestResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Huichengetest',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengetestResponse(),
            self.call_api(params, req, runtime)
        )

    async def huichengetest_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> amp_test_20201230_models.HuichengetestResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='Huichengetest',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            amp_test_20201230_models.HuichengetestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def huichengetest(self) -> amp_test_20201230_models.HuichengetestResponse:
        runtime = util_models.RuntimeOptions()
        return self.huichengetest_with_options(runtime)

    async def huichengetest_async(self) -> amp_test_20201230_models.HuichengetestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.huichengetest_with_options_async(runtime)
