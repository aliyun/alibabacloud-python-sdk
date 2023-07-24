# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sasti20200512 import models as sasti_20200512_models
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
        self._endpoint = self.get_endpoint('sasti', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_domain_report_with_options(
        self,
        request: sasti_20200512_models.DescribeDomainReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.DescribeDomainReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.service_lang):
            query['ServiceLang'] = request.service_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainReport',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.DescribeDomainReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_report_with_options_async(
        self,
        request: sasti_20200512_models.DescribeDomainReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.DescribeDomainReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.service_lang):
            query['ServiceLang'] = request.service_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainReport',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.DescribeDomainReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_report(
        self,
        request: sasti_20200512_models.DescribeDomainReportRequest,
    ) -> sasti_20200512_models.DescribeDomainReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_report_with_options(request, runtime)

    async def describe_domain_report_async(
        self,
        request: sasti_20200512_models.DescribeDomainReportRequest,
    ) -> sasti_20200512_models.DescribeDomainReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_report_with_options_async(request, runtime)

    def describe_file_report_with_options(
        self,
        request: sasti_20200512_models.DescribeFileReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.DescribeFileReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.file_hash):
            query['FileHash'] = request.file_hash
        if not UtilClient.is_unset(request.service_lang):
            query['ServiceLang'] = request.service_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileReport',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.DescribeFileReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_report_with_options_async(
        self,
        request: sasti_20200512_models.DescribeFileReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.DescribeFileReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.file_hash):
            query['FileHash'] = request.file_hash
        if not UtilClient.is_unset(request.service_lang):
            query['ServiceLang'] = request.service_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileReport',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.DescribeFileReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_report(
        self,
        request: sasti_20200512_models.DescribeFileReportRequest,
    ) -> sasti_20200512_models.DescribeFileReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_file_report_with_options(request, runtime)

    async def describe_file_report_async(
        self,
        request: sasti_20200512_models.DescribeFileReportRequest,
    ) -> sasti_20200512_models.DescribeFileReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_report_with_options_async(request, runtime)

    def describe_ip_report_with_options(
        self,
        request: sasti_20200512_models.DescribeIpReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.DescribeIpReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.service_lang):
            query['ServiceLang'] = request.service_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpReport',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.DescribeIpReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_report_with_options_async(
        self,
        request: sasti_20200512_models.DescribeIpReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.DescribeIpReportResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.service_lang):
            query['ServiceLang'] = request.service_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIpReport',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.DescribeIpReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_report(
        self,
        request: sasti_20200512_models.DescribeIpReportRequest,
    ) -> sasti_20200512_models.DescribeIpReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_report_with_options(request, runtime)

    async def describe_ip_report_async(
        self,
        request: sasti_20200512_models.DescribeIpReportRequest,
    ) -> sasti_20200512_models.DescribeIpReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_report_with_options_async(request, runtime)

    def get_graph_query_templates_with_options(
        self,
        request: sasti_20200512_models.GetGraphQueryTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.GetGraphQueryTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.service_unit):
            body['ServiceUnit'] = request.service_unit
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGraphQueryTemplates',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.GetGraphQueryTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_graph_query_templates_with_options_async(
        self,
        request: sasti_20200512_models.GetGraphQueryTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sasti_20200512_models.GetGraphQueryTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.service_unit):
            body['ServiceUnit'] = request.service_unit
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGraphQueryTemplates',
            version='2020-05-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sasti_20200512_models.GetGraphQueryTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_graph_query_templates(
        self,
        request: sasti_20200512_models.GetGraphQueryTemplatesRequest,
    ) -> sasti_20200512_models.GetGraphQueryTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_graph_query_templates_with_options(request, runtime)

    async def get_graph_query_templates_async(
        self,
        request: sasti_20200512_models.GetGraphQueryTemplatesRequest,
    ) -> sasti_20200512_models.GetGraphQueryTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_graph_query_templates_with_options_async(request, runtime)
