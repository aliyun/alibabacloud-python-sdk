# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nlp20180408 import models as nlp_20180408_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('nlp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def entity(
        self,
        domain: str,
    ) -> nlp_20180408_models.EntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.entity_with_options(domain, headers, runtime)

    async def entity_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.EntityResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.entity_with_options_async(domain, headers, runtime)

    def entity_with_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.EntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.EntityResponse().from_map(
            self.do_roarequest('Entity', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/entity/{domain}', 'none', req, runtime)
        )

    async def entity_with_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.EntityResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.EntityResponse().from_map(
            await self.do_roarequest_async('Entity', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/entity/{domain}', 'none', req, runtime)
        )

    def i_e(
        self,
        domain: str,
    ) -> nlp_20180408_models.IEResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.i_ewith_options(domain, headers, runtime)

    async def i_e_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.IEResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.i_ewith_options_async(domain, headers, runtime)

    def i_ewith_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.IEResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.IEResponse().from_map(
            self.do_roarequest('IE', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/ie/{domain}', 'none', req, runtime)
        )

    async def i_ewith_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.IEResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.IEResponse().from_map(
            await self.do_roarequest_async('IE', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/ie/{domain}', 'none', req, runtime)
        )

    def k_we(
        self,
        domain: str,
    ) -> nlp_20180408_models.KWEResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.k_wewith_options(domain, headers, runtime)

    async def k_we_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.KWEResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.k_wewith_options_async(domain, headers, runtime)

    def k_wewith_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.KWEResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.KWEResponse().from_map(
            self.do_roarequest('KWE', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/kwe/{domain}', 'none', req, runtime)
        )

    async def k_wewith_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.KWEResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.KWEResponse().from_map(
            await self.do_roarequest_async('KWE', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/kwe/{domain}', 'none', req, runtime)
        )

    def review_analysis(
        self,
        domain: str,
    ) -> nlp_20180408_models.ReviewAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.review_analysis_with_options(domain, headers, runtime)

    async def review_analysis_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.ReviewAnalysisResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.review_analysis_with_options_async(domain, headers, runtime)

    def review_analysis_with_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.ReviewAnalysisResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.ReviewAnalysisResponse().from_map(
            self.do_roarequest('ReviewAnalysis', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/reviewanalysis/{domain}', 'none', req, runtime)
        )

    async def review_analysis_with_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.ReviewAnalysisResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.ReviewAnalysisResponse().from_map(
            await self.do_roarequest_async('ReviewAnalysis', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/reviewanalysis/{domain}', 'none', req, runtime)
        )

    def sentiment(
        self,
        domain: str,
    ) -> nlp_20180408_models.SentimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sentiment_with_options(domain, headers, runtime)

    async def sentiment_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.SentimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sentiment_with_options_async(domain, headers, runtime)

    def sentiment_with_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.SentimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.SentimentResponse().from_map(
            self.do_roarequest('Sentiment', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/sentiment/{domain}', 'none', req, runtime)
        )

    async def sentiment_with_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.SentimentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.SentimentResponse().from_map(
            await self.do_roarequest_async('Sentiment', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/sentiment/{domain}', 'none', req, runtime)
        )

    def text_structure(
        self,
        domain: str,
    ) -> nlp_20180408_models.TextStructureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_structure_with_options(domain, headers, runtime)

    async def text_structure_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.TextStructureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_structure_with_options_async(domain, headers, runtime)

    def text_structure_with_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.TextStructureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.TextStructureResponse().from_map(
            self.do_roarequest('TextStructure', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/textstructure/{domain}', 'none', req, runtime)
        )

    async def text_structure_with_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.TextStructureResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.TextStructureResponse().from_map(
            await self.do_roarequest_async('TextStructure', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/textstructure/{domain}', 'none', req, runtime)
        )

    def translate(
        self,
        domain: str,
    ) -> nlp_20180408_models.TranslateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.translate_with_options(domain, headers, runtime)

    async def translate_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.TranslateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.translate_with_options_async(domain, headers, runtime)

    def translate_with_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.TranslateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.TranslateResponse().from_map(
            self.do_roarequest('Translate', '2018-04-08', 'HTTP', 'POST', 'AK', f'/nlp/api/translate/{domain}', 'none', req, runtime)
        )

    async def translate_with_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.TranslateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.TranslateResponse().from_map(
            await self.do_roarequest_async('Translate', '2018-04-08', 'HTTP', 'POST', 'AK', f'/nlp/api/translate/{domain}', 'none', req, runtime)
        )

    def word_pos(
        self,
        domain: str,
    ) -> nlp_20180408_models.WordPosResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.word_pos_with_options(domain, headers, runtime)

    async def word_pos_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.WordPosResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.word_pos_with_options_async(domain, headers, runtime)

    def word_pos_with_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.WordPosResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.WordPosResponse().from_map(
            self.do_roarequest('WordPos', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/wordpos/{domain}', 'none', req, runtime)
        )

    async def word_pos_with_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.WordPosResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.WordPosResponse().from_map(
            await self.do_roarequest_async('WordPos', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/wordpos/{domain}', 'none', req, runtime)
        )

    def word_segment(
        self,
        domain: str,
    ) -> nlp_20180408_models.WordSegmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.word_segment_with_options(domain, headers, runtime)

    async def word_segment_async(
        self,
        domain: str,
    ) -> nlp_20180408_models.WordSegmentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.word_segment_with_options_async(domain, headers, runtime)

    def word_segment_with_options(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.WordSegmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.WordSegmentResponse().from_map(
            self.do_roarequest('WordSegment', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/wordsegment/{domain}', 'none', req, runtime)
        )

    async def word_segment_with_options_async(
        self,
        domain: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_20180408_models.WordSegmentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return nlp_20180408_models.WordSegmentResponse().from_map(
            await self.do_roarequest_async('WordSegment', '2018-04-08', 'HTTPS', 'POST', 'AK', f'/nlp/api/wordsegment/{domain}', 'none', req, runtime)
        )
