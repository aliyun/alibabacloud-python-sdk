# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdn20141111 import models as cdn_20141111_models
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
            'ap-northeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'cdn.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'cdn.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'cdn.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cdn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cdn_domain_with_options(
        self,
        request: cdn_20141111_models.AddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.AddCdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priorities):
            query['Priorities'] = request.priorities
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCdnDomain',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.AddCdnDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cdn_domain_with_options_async(
        self,
        request: cdn_20141111_models.AddCdnDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.AddCdnDomainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priorities):
            query['Priorities'] = request.priorities
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCdnDomain',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.AddCdnDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cdn_domain(
        self,
        request: cdn_20141111_models.AddCdnDomainRequest,
    ) -> cdn_20141111_models.AddCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cdn_domain_with_options(request, runtime)

    async def add_cdn_domain_async(
        self,
        request: cdn_20141111_models.AddCdnDomainRequest,
    ) -> cdn_20141111_models.AddCdnDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cdn_domain_with_options_async(request, runtime)

    def describe_cdn_domain_detail_with_options(
        self,
        request: cdn_20141111_models.DescribeCdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeCdnDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnDomainDetail',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeCdnDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_detail_with_options_async(
        self,
        request: cdn_20141111_models.DescribeCdnDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeCdnDomainDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnDomainDetail',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeCdnDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_detail(
        self,
        request: cdn_20141111_models.DescribeCdnDomainDetailRequest,
    ) -> cdn_20141111_models.DescribeCdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_detail_with_options(request, runtime)

    async def describe_cdn_domain_detail_async(
        self,
        request: cdn_20141111_models.DescribeCdnDomainDetailRequest,
    ) -> cdn_20141111_models.DescribeCdnDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_detail_with_options_async(request, runtime)

    def describe_cdn_domain_logs_with_options(
        self,
        request: cdn_20141111_models.DescribeCdnDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeCdnDomainLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.log_day):
            query['LogDay'] = request.log_day
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnDomainLogs',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeCdnDomainLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_domain_logs_with_options_async(
        self,
        request: cdn_20141111_models.DescribeCdnDomainLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeCdnDomainLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.log_day):
            query['LogDay'] = request.log_day
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnDomainLogs',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeCdnDomainLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_domain_logs(
        self,
        request: cdn_20141111_models.DescribeCdnDomainLogsRequest,
    ) -> cdn_20141111_models.DescribeCdnDomainLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_domain_logs_with_options(request, runtime)

    async def describe_cdn_domain_logs_async(
        self,
        request: cdn_20141111_models.DescribeCdnDomainLogsRequest,
    ) -> cdn_20141111_models.DescribeCdnDomainLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_domain_logs_with_options_async(request, runtime)

    def describe_cdn_service_with_options(
        self,
        request: cdn_20141111_models.DescribeCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeCdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnService',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdn_service_with_options_async(
        self,
        request: cdn_20141111_models.DescribeCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeCdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCdnService',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeCdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdn_service(
        self,
        request: cdn_20141111_models.DescribeCdnServiceRequest,
    ) -> cdn_20141111_models.DescribeCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cdn_service_with_options(request, runtime)

    async def describe_cdn_service_async(
        self,
        request: cdn_20141111_models.DescribeCdnServiceRequest,
    ) -> cdn_20141111_models.DescribeCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cdn_service_with_options_async(request, runtime)

    def describe_domain_bps_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataRequest,
    ) -> cdn_20141111_models.DescribeDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_with_options(request, runtime)

    async def describe_domain_bps_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataRequest,
    ) -> cdn_20141111_models.DescribeDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_with_options_async(request, runtime)

    def describe_domain_bps_data_by_time_stamp_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsDataByTimeStamp',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainBpsDataByTimeStampResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_bps_data_by_time_stamp_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataByTimeStampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainBpsDataByTimeStampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBpsDataByTimeStamp',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainBpsDataByTimeStampResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_bps_data_by_time_stamp(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataByTimeStampRequest,
    ) -> cdn_20141111_models.DescribeDomainBpsDataByTimeStampResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_bps_data_by_time_stamp_with_options(request, runtime)

    async def describe_domain_bps_data_by_time_stamp_async(
        self,
        request: cdn_20141111_models.DescribeDomainBpsDataByTimeStampRequest,
    ) -> cdn_20141111_models.DescribeDomainBpsDataByTimeStampResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_bps_data_by_time_stamp_with_options_async(request, runtime)

    def describe_domain_file_size_proportion_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainFileSizeProportionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainFileSizeProportionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainFileSizeProportionData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainFileSizeProportionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_file_size_proportion_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainFileSizeProportionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainFileSizeProportionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainFileSizeProportionData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainFileSizeProportionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_file_size_proportion_data(
        self,
        request: cdn_20141111_models.DescribeDomainFileSizeProportionDataRequest,
    ) -> cdn_20141111_models.DescribeDomainFileSizeProportionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_file_size_proportion_data_with_options(request, runtime)

    async def describe_domain_file_size_proportion_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainFileSizeProportionDataRequest,
    ) -> cdn_20141111_models.DescribeDomainFileSizeProportionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_file_size_proportion_data_with_options_async(request, runtime)

    def describe_domain_flow_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainFlowDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainFlowDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainFlowData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainFlowDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_flow_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainFlowDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainFlowDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainFlowData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainFlowDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_flow_data(
        self,
        request: cdn_20141111_models.DescribeDomainFlowDataRequest,
    ) -> cdn_20141111_models.DescribeDomainFlowDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_flow_data_with_options(request, runtime)

    async def describe_domain_flow_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainFlowDataRequest,
    ) -> cdn_20141111_models.DescribeDomainFlowDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_flow_data_with_options_async(request, runtime)

    def describe_domain_hit_rate_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainHitRateData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_hit_rate_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainHitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainHitRateData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_hit_rate_data(
        self,
        request: cdn_20141111_models.DescribeDomainHitRateDataRequest,
    ) -> cdn_20141111_models.DescribeDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_hit_rate_data_with_options(request, runtime)

    async def describe_domain_hit_rate_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainHitRateDataRequest,
    ) -> cdn_20141111_models.DescribeDomainHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_http_code_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainHttpCodeData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_http_code_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainHttpCodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainHttpCodeDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainHttpCodeData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainHttpCodeDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_http_code_data(
        self,
        request: cdn_20141111_models.DescribeDomainHttpCodeDataRequest,
    ) -> cdn_20141111_models.DescribeDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_http_code_data_with_options(request, runtime)

    async def describe_domain_http_code_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainHttpCodeDataRequest,
    ) -> cdn_20141111_models.DescribeDomainHttpCodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_http_code_data_with_options_async(request, runtime)

    def describe_domain_ispdata_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainISPDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainISPDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainISPData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainISPDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_ispdata_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainISPDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainISPDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainISPData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainISPDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_ispdata(
        self,
        request: cdn_20141111_models.DescribeDomainISPDataRequest,
    ) -> cdn_20141111_models.DescribeDomainISPDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_ispdata_with_options(request, runtime)

    async def describe_domain_ispdata_async(
        self,
        request: cdn_20141111_models.DescribeDomainISPDataRequest,
    ) -> cdn_20141111_models.DescribeDomainISPDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_ispdata_with_options_async(request, runtime)

    def describe_domain_qps_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainQpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainQpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_qps_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainQpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainQpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainQpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainQpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_qps_data(
        self,
        request: cdn_20141111_models.DescribeDomainQpsDataRequest,
    ) -> cdn_20141111_models.DescribeDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_data_with_options(request, runtime)

    async def describe_domain_qps_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainQpsDataRequest,
    ) -> cdn_20141111_models.DescribeDomainQpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_data_with_options_async(request, runtime)

    def describe_domain_region_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainRegionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRegionData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_region_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainRegionDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRegionData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_region_data(
        self,
        request: cdn_20141111_models.DescribeDomainRegionDataRequest,
    ) -> cdn_20141111_models.DescribeDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_region_data_with_options(request, runtime)

    async def describe_domain_region_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainRegionDataRequest,
    ) -> cdn_20141111_models.DescribeDomainRegionDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_region_data_with_options_async(request, runtime)

    def describe_domain_req_hit_rate_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainReqHitRateData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainReqHitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_req_hit_rate_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainReqHitRateDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainReqHitRateDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainReqHitRateData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainReqHitRateDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_req_hit_rate_data(
        self,
        request: cdn_20141111_models.DescribeDomainReqHitRateDataRequest,
    ) -> cdn_20141111_models.DescribeDomainReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_req_hit_rate_data_with_options(request, runtime)

    async def describe_domain_req_hit_rate_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainReqHitRateDataRequest,
    ) -> cdn_20141111_models.DescribeDomainReqHitRateDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_req_hit_rate_data_with_options_async(request, runtime)

    def describe_domain_src_bps_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainSrcBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSrcBpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainSrcBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_bps_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainSrcBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainSrcBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSrcBpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainSrcBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_bps_data(
        self,
        request: cdn_20141111_models.DescribeDomainSrcBpsDataRequest,
    ) -> cdn_20141111_models.DescribeDomainSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_bps_data_with_options(request, runtime)

    async def describe_domain_src_bps_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainSrcBpsDataRequest,
    ) -> cdn_20141111_models.DescribeDomainSrcBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_bps_data_with_options_async(request, runtime)

    def describe_domain_src_flow_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainSrcFlowDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainSrcFlowDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSrcFlowData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainSrcFlowDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_src_flow_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainSrcFlowDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainSrcFlowDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fix_time_gap):
            query['FixTimeGap'] = request.fix_time_gap
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainSrcFlowData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainSrcFlowDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_src_flow_data(
        self,
        request: cdn_20141111_models.DescribeDomainSrcFlowDataRequest,
    ) -> cdn_20141111_models.DescribeDomainSrcFlowDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_src_flow_data_with_options(request, runtime)

    async def describe_domain_src_flow_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainSrcFlowDataRequest,
    ) -> cdn_20141111_models.DescribeDomainSrcFlowDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_src_flow_data_with_options_async(request, runtime)

    def describe_domain_uv_data_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainUvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUvData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_uv_data_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainUvDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUvData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_uv_data(
        self,
        request: cdn_20141111_models.DescribeDomainUvDataRequest,
    ) -> cdn_20141111_models.DescribeDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_uv_data_with_options(request, runtime)

    async def describe_domain_uv_data_async(
        self,
        request: cdn_20141111_models.DescribeDomainUvDataRequest,
    ) -> cdn_20141111_models.DescribeDomainUvDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_uv_data_with_options_async(request, runtime)

    def describe_domains_by_source_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainsBySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainsBySourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainsBySource',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainsBySourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_by_source_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainsBySourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainsBySourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainsBySource',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainsBySourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains_by_source(
        self,
        request: cdn_20141111_models.DescribeDomainsBySourceRequest,
    ) -> cdn_20141111_models.DescribeDomainsBySourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_by_source_with_options(request, runtime)

    async def describe_domains_by_source_async(
        self,
        request: cdn_20141111_models.DescribeDomainsBySourceRequest,
    ) -> cdn_20141111_models.DescribeDomainsBySourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_by_source_with_options_async(request, runtime)

    def describe_domains_usage_by_day_with_options(
        self,
        request: cdn_20141111_models.DescribeDomainsUsageByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainsUsageByDayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainsUsageByDay',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainsUsageByDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domains_usage_by_day_with_options_async(
        self,
        request: cdn_20141111_models.DescribeDomainsUsageByDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeDomainsUsageByDayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainsUsageByDay',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeDomainsUsageByDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domains_usage_by_day(
        self,
        request: cdn_20141111_models.DescribeDomainsUsageByDayRequest,
    ) -> cdn_20141111_models.DescribeDomainsUsageByDayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_usage_by_day_with_options(request, runtime)

    async def describe_domains_usage_by_day_async(
        self,
        request: cdn_20141111_models.DescribeDomainsUsageByDayRequest,
    ) -> cdn_20141111_models.DescribeDomainsUsageByDayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_usage_by_day_with_options_async(request, runtime)

    def describe_refresh_quota_with_options(
        self,
        request: cdn_20141111_models.DescribeRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeRefreshQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRefreshQuota',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeRefreshQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_refresh_quota_with_options_async(
        self,
        request: cdn_20141111_models.DescribeRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeRefreshQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRefreshQuota',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeRefreshQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_refresh_quota(
        self,
        request: cdn_20141111_models.DescribeRefreshQuotaRequest,
    ) -> cdn_20141111_models.DescribeRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_refresh_quota_with_options(request, runtime)

    async def describe_refresh_quota_async(
        self,
        request: cdn_20141111_models.DescribeRefreshQuotaRequest,
    ) -> cdn_20141111_models.DescribeRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_refresh_quota_with_options_async(request, runtime)

    def describe_top_domains_by_flow_with_options(
        self,
        request: cdn_20141111_models.DescribeTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopDomainsByFlow',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_domains_by_flow_with_options_async(
        self,
        request: cdn_20141111_models.DescribeTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeTopDomainsByFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopDomainsByFlow',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_domains_by_flow(
        self,
        request: cdn_20141111_models.DescribeTopDomainsByFlowRequest,
    ) -> cdn_20141111_models.DescribeTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_top_domains_by_flow_with_options(request, runtime)

    async def describe_top_domains_by_flow_async(
        self,
        request: cdn_20141111_models.DescribeTopDomainsByFlowRequest,
    ) -> cdn_20141111_models.DescribeTopDomainsByFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_top_domains_by_flow_with_options_async(request, runtime)

    def describe_user_domains_with_options(
        self,
        request: cdn_20141111_models.DescribeUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDomains',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_domains_with_options_async(
        self,
        request: cdn_20141111_models.DescribeUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.DescribeUserDomainsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cdn_type):
            query['CdnType'] = request.cdn_type
        if not UtilClient.is_unset(request.check_domain_show):
            query['CheckDomainShow'] = request.check_domain_show
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sources):
            query['Sources'] = request.sources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserDomains',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.DescribeUserDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_domains(
        self,
        request: cdn_20141111_models.DescribeUserDomainsRequest,
    ) -> cdn_20141111_models.DescribeUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_domains_with_options(request, runtime)

    async def describe_user_domains_async(
        self,
        request: cdn_20141111_models.DescribeUserDomainsRequest,
    ) -> cdn_20141111_models.DescribeUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_domains_with_options_async(request, runtime)

    def open_cdn_service_with_options(
        self,
        request: cdn_20141111_models.OpenCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.OpenCdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCdnService',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.OpenCdnServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_cdn_service_with_options_async(
        self,
        request: cdn_20141111_models.OpenCdnServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.OpenCdnServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCdnService',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.OpenCdnServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_cdn_service(
        self,
        request: cdn_20141111_models.OpenCdnServiceRequest,
    ) -> cdn_20141111_models.OpenCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_cdn_service_with_options(request, runtime)

    async def open_cdn_service_async(
        self,
        request: cdn_20141111_models.OpenCdnServiceRequest,
    ) -> cdn_20141111_models.OpenCdnServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_cdn_service_with_options_async(request, runtime)

    def push_object_cache_with_options(
        self,
        request: cdn_20141111_models.PushObjectCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.PushObjectCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushObjectCache',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.PushObjectCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_object_cache_with_options_async(
        self,
        request: cdn_20141111_models.PushObjectCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.PushObjectCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushObjectCache',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.PushObjectCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_object_cache(
        self,
        request: cdn_20141111_models.PushObjectCacheRequest,
    ) -> cdn_20141111_models.PushObjectCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_object_cache_with_options(request, runtime)

    async def push_object_cache_async(
        self,
        request: cdn_20141111_models.PushObjectCacheRequest,
    ) -> cdn_20141111_models.PushObjectCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_object_cache_with_options_async(request, runtime)

    def refresh_object_caches_with_options(
        self,
        request: cdn_20141111_models.RefreshObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.RefreshObjectCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshObjectCaches',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.RefreshObjectCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_object_caches_with_options_async(
        self,
        request: cdn_20141111_models.RefreshObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.RefreshObjectCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_path):
            query['ObjectPath'] = request.object_path
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshObjectCaches',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.RefreshObjectCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_object_caches(
        self,
        request: cdn_20141111_models.RefreshObjectCachesRequest,
    ) -> cdn_20141111_models.RefreshObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_object_caches_with_options(request, runtime)

    async def refresh_object_caches_async(
        self,
        request: cdn_20141111_models.RefreshObjectCachesRequest,
    ) -> cdn_20141111_models.RefreshObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_object_caches_with_options_async(request, runtime)

    def test_describe_domain_bps_data_with_options(
        self,
        request: cdn_20141111_models.TestDescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.TestDescribeDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestDescribeDomainBpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.TestDescribeDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def test_describe_domain_bps_data_with_options_async(
        self,
        request: cdn_20141111_models.TestDescribeDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cdn_20141111_models.TestDescribeDomainBpsDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_type):
            query['DomainType'] = request.domain_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.time_merge):
            query['TimeMerge'] = request.time_merge
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestDescribeDomainBpsData',
            version='2014-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cdn_20141111_models.TestDescribeDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def test_describe_domain_bps_data(
        self,
        request: cdn_20141111_models.TestDescribeDomainBpsDataRequest,
    ) -> cdn_20141111_models.TestDescribeDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_describe_domain_bps_data_with_options(request, runtime)

    async def test_describe_domain_bps_data_async(
        self,
        request: cdn_20141111_models.TestDescribeDomainBpsDataRequest,
    ) -> cdn_20141111_models.TestDescribeDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_describe_domain_bps_data_with_options_async(request, runtime)
