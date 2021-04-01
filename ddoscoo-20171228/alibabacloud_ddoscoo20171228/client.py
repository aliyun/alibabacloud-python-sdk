# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_ddoscoo20171228 import models as ddoscoo_20171228_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddoscoo', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def modify_full_log_ttl_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ModifyFullLogTtlResponse(),
            self.do_request('ModifyFullLogTtl', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_full_log_ttl_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ModifyFullLogTtlResponse(),
            await self.do_request_async('ModifyFullLogTtl', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_full_log_ttl(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_full_log_ttl_with_options(request, runtime)

    async def modify_full_log_ttl_async(
        self,
        request: ddoscoo_20171228_models.ModifyFullLogTtlRequest,
    ) -> ddoscoo_20171228_models.ModifyFullLogTtlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_full_log_ttl_with_options_async(request, runtime)

    def release_value_added_with_options(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ReleaseValueAddedResponse(),
            self.do_request('ReleaseValueAdded', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def release_value_added_with_options_async(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ReleaseValueAddedResponse(),
            await self.do_request_async('ReleaseValueAdded', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def release_value_added(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_value_added_with_options(request, runtime)

    async def release_value_added_async(
        self,
        request: ddoscoo_20171228_models.ReleaseValueAddedRequest,
    ) -> ddoscoo_20171228_models.ReleaseValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_value_added_with_options_async(request, runtime)

    def list_value_added_with_options(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListValueAddedResponse(),
            self.do_request('ListValueAdded', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_value_added_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListValueAddedResponse(),
            await self.do_request_async('ListValueAdded', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_value_added(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_value_added_with_options(request, runtime)

    async def list_value_added_async(
        self,
        request: ddoscoo_20171228_models.ListValueAddedRequest,
    ) -> ddoscoo_20171228_models.ListValueAddedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_value_added_with_options_async(request, runtime)

    def list_layer_7custom_ports_with_options(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListLayer7CustomPortsResponse(),
            self.do_request('ListLayer7CustomPorts', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_layer_7custom_ports_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListLayer7CustomPortsResponse(),
            await self.do_request_async('ListLayer7CustomPorts', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_layer_7custom_ports(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_layer_7custom_ports_with_options(request, runtime)

    async def list_layer_7custom_ports_async(
        self,
        request: ddoscoo_20171228_models.ListLayer7CustomPortsRequest,
    ) -> ddoscoo_20171228_models.ListLayer7CustomPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_layer_7custom_ports_with_options_async(request, runtime)

    def describe_simple_domains_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSimpleDomainsResponse(),
            self.do_request('DescribeSimpleDomains', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_simple_domains_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSimpleDomainsResponse(),
            await self.do_request_async('DescribeSimpleDomains', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_simple_domains(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_simple_domains_with_options(request, runtime)

    async def describe_simple_domains_async(
        self,
        request: ddoscoo_20171228_models.DescribeSimpleDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeSimpleDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_simple_domains_with_options_async(request, runtime)

    def describe_defense_count_statistics_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse(),
            self.do_request('DescribeDefenseCountStatistics', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_defense_count_statistics_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse(),
            await self.do_request_async('DescribeDefenseCountStatistics', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_defense_count_statistics(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_defense_count_statistics_with_options(request, runtime)

    async def describe_defense_count_statistics_async(
        self,
        request: ddoscoo_20171228_models.DescribeDefenseCountStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeDefenseCountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_defense_count_statistics_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.UntagResourcesResponse(),
            self.do_request('UntagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.UntagResourcesResponse(),
            await self.do_request_async('UntagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def untag_resources(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ddoscoo_20171228_models.UntagResourcesRequest,
    ) -> ddoscoo_20171228_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.TagResourcesResponse(),
            self.do_request('TagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.TagResourcesResponse(),
            await self.do_request_async('TagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def tag_resources(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ddoscoo_20171228_models.TagResourcesRequest,
    ) -> ddoscoo_20171228_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListTagResourcesResponse(),
            self.do_request('ListTagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListTagResourcesResponse(),
            await self.do_request_async('ListTagResources', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_resources(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ddoscoo_20171228_models.ListTagResourcesRequest,
    ) -> ddoscoo_20171228_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListTagKeysResponse(),
            self.do_request('ListTagKeys', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListTagKeysResponse(),
            await self.do_request_async('ListTagKeys', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_keys(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ddoscoo_20171228_models.ListTagKeysRequest,
    ) -> ddoscoo_20171228_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def describe_domain_qps_with_cache_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse(),
            self.do_request('DescribeDomainQpsWithCache', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_domain_qps_with_cache_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse(),
            await self.do_request_async('DescribeDomainQpsWithCache', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_domain_qps_with_cache(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_cache_with_options(request, runtime)

    async def describe_domain_qps_with_cache_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsWithCacheRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_with_cache_with_options_async(request, runtime)

    def describe_log_store_exist_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse(),
            self.do_request('DescribeLogStoreExistStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_log_store_exist_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse(),
            await self.do_request_async('DescribeLogStoreExistStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_log_store_exist_status(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_exist_status_with_options(request, runtime)

    async def describe_log_store_exist_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeLogStoreExistStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeLogStoreExistStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_exist_status_with_options_async(request, runtime)

    def describe_batch_sls_dispatch_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse(),
            self.do_request('DescribeBatchSlsDispatchStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_batch_sls_dispatch_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse(),
            await self.do_request_async('DescribeBatchSlsDispatchStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_batch_sls_dispatch_status(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_sls_dispatch_status_with_options(request, runtime)

    async def describe_batch_sls_dispatch_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeBatchSlsDispatchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_sls_dispatch_status_with_options_async(request, runtime)

    def describe_sls_empty_count_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsEmptyCountResponse(),
            self.do_request('DescribeSlsEmptyCount', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_sls_empty_count_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsEmptyCountResponse(),
            await self.do_request_async('DescribeSlsEmptyCount', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_sls_empty_count(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_empty_count_with_options(request, runtime)

    async def describe_sls_empty_count_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsEmptyCountRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsEmptyCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_empty_count_with_options_async(request, runtime)

    def empty_sls_logstore_with_options(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.EmptySlsLogstoreResponse(),
            self.do_request('EmptySlsLogstore', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def empty_sls_logstore_with_options_async(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.EmptySlsLogstoreResponse(),
            await self.do_request_async('EmptySlsLogstore', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def empty_sls_logstore(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.empty_sls_logstore_with_options(request, runtime)

    async def empty_sls_logstore_async(
        self,
        request: ddoscoo_20171228_models.EmptySlsLogstoreRequest,
    ) -> ddoscoo_20171228_models.EmptySlsLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.empty_sls_logstore_with_options_async(request, runtime)

    def close_domain_sls_config_with_options(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CloseDomainSlsConfigResponse(),
            self.do_request('CloseDomainSlsConfig', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def close_domain_sls_config_with_options_async(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CloseDomainSlsConfigResponse(),
            await self.do_request_async('CloseDomainSlsConfig', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def close_domain_sls_config(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_domain_sls_config_with_options(request, runtime)

    async def close_domain_sls_config_async(
        self,
        request: ddoscoo_20171228_models.CloseDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.CloseDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_domain_sls_config_with_options_async(request, runtime)

    def open_domain_sls_config_with_options(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.OpenDomainSlsConfigResponse(),
            self.do_request('OpenDomainSlsConfig', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def open_domain_sls_config_with_options_async(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.OpenDomainSlsConfigResponse(),
            await self.do_request_async('OpenDomainSlsConfig', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def open_domain_sls_config(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_domain_sls_config_with_options(request, runtime)

    async def open_domain_sls_config_async(
        self,
        request: ddoscoo_20171228_models.OpenDomainSlsConfigRequest,
    ) -> ddoscoo_20171228_models.OpenDomainSlsConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_domain_sls_config_with_options_async(request, runtime)

    def describe_sls_logstore_info_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse(),
            self.do_request('DescribeSlsLogstoreInfo', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_sls_logstore_info_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse(),
            await self.do_request_async('DescribeSlsLogstoreInfo', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_sls_logstore_info(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_logstore_info_with_options(request, runtime)

    async def describe_sls_logstore_info_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsLogstoreInfoRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsLogstoreInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_logstore_info_with_options_async(request, runtime)

    def describe_sls_auth_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsAuthStatusResponse(),
            self.do_request('DescribeSlsAuthStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_sls_auth_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsAuthStatusResponse(),
            await self.do_request_async('DescribeSlsAuthStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_sls_auth_status(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_auth_status_with_options(request, runtime)

    async def describe_sls_auth_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsAuthStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_auth_status_with_options_async(request, runtime)

    def describe_sls_open_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsOpenStatusResponse(),
            self.do_request('DescribeSlsOpenStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_sls_open_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeSlsOpenStatusResponse(),
            await self.do_request_async('DescribeSlsOpenStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_sls_open_status(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sls_open_status_with_options(request, runtime)

    async def describe_sls_open_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeSlsOpenStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeSlsOpenStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sls_open_status_with_options_async(request, runtime)

    def describe_domain_sls_status_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainSlsStatusResponse(),
            self.do_request('DescribeDomainSlsStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_domain_sls_status_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainSlsStatusResponse(),
            await self.do_request_async('DescribeDomainSlsStatus', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_domain_sls_status(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_sls_status_with_options(request, runtime)

    async def describe_domain_sls_status_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainSlsStatusRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainSlsStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_sls_status_with_options_async(request, runtime)

    def config_domain_access_mode_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigDomainAccessModeResponse(),
            self.do_request('ConfigDomainAccessMode', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_domain_access_mode_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigDomainAccessModeResponse(),
            await self.do_request_async('ConfigDomainAccessMode', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_domain_access_mode(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_domain_access_mode_with_options(request, runtime)

    async def config_domain_access_mode_async(
        self,
        request: ddoscoo_20171228_models.ConfigDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.ConfigDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_domain_access_mode_with_options_async(request, runtime)

    def describe_domain_access_mode_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainAccessModeResponse(),
            self.do_request('DescribeDomainAccessMode', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_domain_access_mode_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainAccessModeResponse(),
            await self.do_request_async('DescribeDomainAccessMode', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_domain_access_mode(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_access_mode_with_options(request, runtime)

    async def describe_domain_access_mode_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAccessModeRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAccessModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_access_mode_with_options_async(request, runtime)

    def delete_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteAsyncTaskResponse(),
            self.do_request('DeleteAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteAsyncTaskResponse(),
            await self.do_request_async('DeleteAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_async_task(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_async_task_with_options(request, runtime)

    async def delete_async_task_async(
        self,
        request: ddoscoo_20171228_models.DeleteAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.DeleteAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_async_task_with_options_async(request, runtime)

    def create_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CreateAsyncTaskResponse(),
            self.do_request('CreateAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CreateAsyncTaskResponse(),
            await self.do_request_async('CreateAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_async_task(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_async_task_with_options(request, runtime)

    async def create_async_task_async(
        self,
        request: ddoscoo_20171228_models.CreateAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.CreateAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_async_task_with_options_async(request, runtime)

    def list_async_task_with_options(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListAsyncTaskResponse(),
            self.do_request('ListAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_async_task_with_options_async(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ListAsyncTaskResponse(),
            await self.do_request_async('ListAsyncTask', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_async_task(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_async_task_with_options(request, runtime)

    async def list_async_task_async(
        self,
        request: ddoscoo_20171228_models.ListAsyncTaskRequest,
    ) -> ddoscoo_20171228_models.ListAsyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_async_task_with_options_async(request, runtime)

    def enable_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.EnableLayer7CCRuleResponse(),
            self.do_request('EnableLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def enable_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.EnableLayer7CCRuleResponse(),
            await self.do_request_async('EnableLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccrule_with_options(request, runtime)

    async def enable_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_layer_7ccrule_with_options_async(request, runtime)

    def enable_layer_7ccwith_options(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.EnableLayer7CCResponse(),
            self.do_request('EnableLayer7CC', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def enable_layer_7ccwith_options_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.EnableLayer7CCResponse(),
            await self.do_request_async('EnableLayer7CC', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_layer_7cc(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_layer_7ccwith_options(request, runtime)

    async def enable_layer_7cc_async(
        self,
        request: ddoscoo_20171228_models.EnableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.EnableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_layer_7ccwith_options_async(request, runtime)

    def disable_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DisableLayer7CCRuleResponse(),
            self.do_request('DisableLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disable_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DisableLayer7CCRuleResponse(),
            await self.do_request_async('DisableLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccrule_with_options(request, runtime)

    async def disable_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_layer_7ccrule_with_options_async(request, runtime)

    def disable_layer_7ccwith_options(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DisableLayer7CCResponse(),
            self.do_request('DisableLayer7CC', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disable_layer_7ccwith_options_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DisableLayer7CCResponse(),
            await self.do_request_async('DisableLayer7CC', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_layer_7cc(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_layer_7ccwith_options(request, runtime)

    async def disable_layer_7cc_async(
        self,
        request: ddoscoo_20171228_models.DisableLayer7CCRequest,
    ) -> ddoscoo_20171228_models.DisableLayer7CCResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_layer_7ccwith_options_async(request, runtime)

    def describle_layer_7instance_relations_with_options(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse(),
            self.do_request('DescribleLayer7InstanceRelations', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describle_layer_7instance_relations_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse(),
            await self.do_request_async('DescribleLayer7InstanceRelations', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describle_layer_7instance_relations(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describle_layer_7instance_relations_with_options(request, runtime)

    async def describle_layer_7instance_relations_async(
        self,
        request: ddoscoo_20171228_models.DescribleLayer7InstanceRelationsRequest,
    ) -> ddoscoo_20171228_models.DescribleLayer7InstanceRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describle_layer_7instance_relations_with_options_async(request, runtime)

    def describle_cert_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribleCertListResponse(),
            self.do_request('DescribleCertList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describle_cert_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribleCertListResponse(),
            await self.do_request_async('DescribleCertList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describle_cert_list(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describle_cert_list_with_options(request, runtime)

    async def describle_cert_list_async(
        self,
        request: ddoscoo_20171228_models.DescribleCertListRequest,
    ) -> ddoscoo_20171228_models.DescribleCertListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describle_cert_list_with_options_async(request, runtime)

    def describe_layer_7ccrules_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLayer7CCRulesResponse(),
            self.do_request('DescribeLayer7CCRules', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_layer_7ccrules_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLayer7CCRulesResponse(),
            await self.do_request_async('DescribeLayer7CCRules', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_layer_7ccrules(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_7ccrules_with_options(request, runtime)

    async def describe_layer_7ccrules_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer7CCRulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer7CCRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_7ccrules_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainsResponse(),
            self.do_request('DescribeDomains', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainsResponse(),
            await self.do_request_async('DescribeDomains', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_domains(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_domain_qps_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainQpsResponse(),
            self.do_request('DescribeDomainQps', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_domain_qps_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainQpsResponse(),
            await self.do_request_async('DescribeDomainQps', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_domain_qps(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_qps_with_options(request, runtime)

    async def describe_domain_qps_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainQpsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainQpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_qps_with_options_async(request, runtime)

    def describe_domain_attack_events_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainAttackEventsResponse(),
            self.do_request('DescribeDomainAttackEvents', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_domain_attack_events_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDomainAttackEventsResponse(),
            await self.do_request_async('DescribeDomainAttackEvents', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_domain_attack_events(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_events_with_options(request, runtime)

    async def describe_domain_attack_events_async(
        self,
        request: ddoscoo_20171228_models.DescribeDomainAttackEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDomainAttackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_attack_events_with_options_async(request, runtime)

    def describe_back_source_cidr_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeBackSourceCidrResponse(),
            self.do_request('DescribeBackSourceCidr', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_back_source_cidr_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeBackSourceCidrResponse(),
            await self.do_request_async('DescribeBackSourceCidr', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_back_source_cidr(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_back_source_cidr_with_options(request, runtime)

    async def describe_back_source_cidr_async(
        self,
        request: ddoscoo_20171228_models.DescribeBackSourceCidrRequest,
    ) -> ddoscoo_20171228_models.DescribeBackSourceCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_source_cidr_with_options_async(request, runtime)

    def delete_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteLayer7RuleResponse(),
            self.do_request('DeleteLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteLayer7RuleResponse(),
            await self.do_request_async('DeleteLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_layer_7rule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7rule_with_options(request, runtime)

    async def delete_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_7rule_with_options_async(request, runtime)

    def delete_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteLayer7CCRuleResponse(),
            self.do_request('DeleteLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteLayer7CCRuleResponse(),
            await self.do_request_async('DeleteLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_7ccrule_with_options(request, runtime)

    async def delete_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_7ccrule_with_options_async(request, runtime)

    def create_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CreateLayer7RuleResponse(),
            self.do_request('CreateLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CreateLayer7RuleResponse(),
            await self.do_request_async('CreateLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_layer_7rule(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_layer_7rule_with_options(request, runtime)

    async def create_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_7rule_with_options_async(request, runtime)

    def config_layer_7rule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7RuleResponse(),
            self.do_request('ConfigLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_layer_7rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7RuleResponse(),
            await self.do_request_async('ConfigLayer7Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_layer_7rule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7rule_with_options(request, runtime)

    async def config_layer_7rule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7rule_with_options_async(request, runtime)

    def config_layer_7cert_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7CertResponse(),
            self.do_request('ConfigLayer7Cert', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_layer_7cert_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7CertResponse(),
            await self.do_request_async('ConfigLayer7Cert', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_layer_7cert(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cert_with_options(request, runtime)

    async def config_layer_7cert_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CertRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7cert_with_options_async(request, runtime)

    def config_layer_7cctemplate_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse(),
            self.do_request('ConfigLayer7CCTemplate', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_layer_7cctemplate_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse(),
            await self.do_request_async('ConfigLayer7CCTemplate', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_layer_7cctemplate(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7cctemplate_with_options(request, runtime)

    async def config_layer_7cctemplate_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCTemplateRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7cctemplate_with_options_async(request, runtime)

    def config_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7CCRuleResponse(),
            self.do_request('ConfigLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7CCRuleResponse(),
            await self.do_request_async('ConfigLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7ccrule_with_options(request, runtime)

    async def config_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7ccrule_with_options_async(request, runtime)

    def config_layer_7black_white_list_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse(),
            self.do_request('ConfigLayer7BlackWhiteList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_layer_7black_white_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse(),
            await self.do_request_async('ConfigLayer7BlackWhiteList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_layer_7black_white_list(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_7black_white_list_with_options(request, runtime)

    async def config_layer_7black_white_list_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer7BlackWhiteListRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer7BlackWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_7black_white_list_with_options_async(request, runtime)

    def add_layer_7ccrule_with_options(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.AddLayer7CCRuleResponse(),
            self.do_request('AddLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def add_layer_7ccrule_with_options_async(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.AddLayer7CCRuleResponse(),
            await self.do_request_async('AddLayer7CCRule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_layer_7ccrule(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_layer_7ccrule_with_options(request, runtime)

    async def add_layer_7ccrule_async(
        self,
        request: ddoscoo_20171228_models.AddLayer7CCRuleRequest,
    ) -> ddoscoo_20171228_models.AddLayer7CCRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_layer_7ccrule_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ReleaseInstanceResponse(),
            self.do_request('ReleaseInstance', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ReleaseInstanceResponse(),
            await self.do_request_async('ReleaseInstance', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def release_instance(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: ddoscoo_20171228_models.ReleaseInstanceRequest,
    ) -> ddoscoo_20171228_models.ReleaseInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def modify_instance_remark_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ModifyInstanceRemarkResponse(),
            self.do_request('ModifyInstanceRemark', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_instance_remark_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ModifyInstanceRemarkResponse(),
            await self.do_request_async('ModifyInstanceRemark', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_instance_remark(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_remark_with_options(request, runtime)

    async def modify_instance_remark_async(
        self,
        request: ddoscoo_20171228_models.ModifyInstanceRemarkRequest,
    ) -> ddoscoo_20171228_models.ModifyInstanceRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_remark_with_options_async(request, runtime)

    def modify_elastic_band_width_with_options(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ModifyElasticBandWidthResponse(),
            self.do_request('ModifyElasticBandWidth', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_elastic_band_width_with_options_async(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ModifyElasticBandWidthResponse(),
            await self.do_request_async('ModifyElasticBandWidth', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_elastic_band_width(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_elastic_band_width_with_options(request, runtime)

    async def modify_elastic_band_width_async(
        self,
        request: ddoscoo_20171228_models.ModifyElasticBandWidthRequest,
    ) -> ddoscoo_20171228_models.ModifyElasticBandWidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_elastic_band_width_with_options_async(request, runtime)

    def describe_op_entities_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeOpEntitiesResponse(),
            self.do_request('DescribeOpEntities', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_op_entities_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeOpEntitiesResponse(),
            await self.do_request_async('DescribeOpEntities', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_op_entities(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_op_entities_with_options(request, runtime)

    async def describe_op_entities_async(
        self,
        request: ddoscoo_20171228_models.DescribeOpEntitiesRequest,
    ) -> ddoscoo_20171228_models.DescribeOpEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_op_entities_with_options_async(request, runtime)

    def describe_layer_4rules_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLayer4RulesResponse(),
            self.do_request('DescribeLayer4Rules', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_layer_4rules_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLayer4RulesResponse(),
            await self.do_request_async('DescribeLayer4Rules', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_layer_4rules(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rules_with_options(request, runtime)

    async def describe_layer_4rules_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RulesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rules_with_options_async(request, runtime)

    def describe_layer_4rule_attributes_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse(),
            self.do_request('DescribeLayer4RuleAttributes', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_layer_4rule_attributes_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse(),
            await self.do_request_async('DescribeLayer4RuleAttributes', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_layer_4rule_attributes(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_layer_4rule_attributes_with_options(request, runtime)

    async def describe_layer_4rule_attributes_async(
        self,
        request: ddoscoo_20171228_models.DescribeLayer4RuleAttributesRequest,
    ) -> ddoscoo_20171228_models.DescribeLayer4RuleAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_layer_4rule_attributes_with_options_async(request, runtime)

    def describe_ip_traffic_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeIpTrafficResponse(),
            self.do_request('DescribeIpTraffic', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_ip_traffic_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeIpTrafficResponse(),
            await self.do_request_async('DescribeIpTraffic', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_ip_traffic(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ip_traffic_with_options(request, runtime)

    async def describe_ip_traffic_async(
        self,
        request: ddoscoo_20171228_models.DescribeIpTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeIpTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ip_traffic_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstanceStatisticsResponse(),
            self.do_request('DescribeInstanceStatistics', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstanceStatisticsResponse(),
            await self.do_request_async('DescribeInstanceStatistics', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instance_statistics(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceStatisticsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_instance_specs_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstanceSpecsResponse(),
            self.do_request('DescribeInstanceSpecs', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instance_specs_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstanceSpecsResponse(),
            await self.do_request_async('DescribeInstanceSpecs', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instance_specs(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_specs_with_options(request, runtime)

    async def describe_instance_specs_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceSpecsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceSpecsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_specs_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstancesResponse(),
            self.do_request('DescribeInstances', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstancesResponse(),
            await self.do_request_async('DescribeInstances', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instances(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstancesRequest,
    ) -> ddoscoo_20171228_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instance_details_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstanceDetailsResponse(),
            self.do_request('DescribeInstanceDetails', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_instance_details_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeInstanceDetailsResponse(),
            await self.do_request_async('DescribeInstanceDetails', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_instance_details(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_details_with_options(request, runtime)

    async def describe_instance_details_async(
        self,
        request: ddoscoo_20171228_models.DescribeInstanceDetailsRequest,
    ) -> ddoscoo_20171228_models.DescribeInstanceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_details_with_options_async(request, runtime)

    def describe_health_check_status_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse(),
            self.do_request('DescribeHealthCheckStatusList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_health_check_status_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse(),
            await self.do_request_async('DescribeHealthCheckStatusList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_health_check_status_list(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_status_list_with_options(request, runtime)

    async def describe_health_check_status_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckStatusListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_status_list_with_options_async(request, runtime)

    def describe_health_check_list_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeHealthCheckListResponse(),
            self.do_request('DescribeHealthCheckList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_health_check_list_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeHealthCheckListResponse(),
            await self.do_request_async('DescribeHealthCheckList', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_health_check_list(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_health_check_list_with_options(request, runtime)

    async def describe_health_check_list_async(
        self,
        request: ddoscoo_20171228_models.DescribeHealthCheckListRequest,
    ) -> ddoscoo_20171228_models.DescribeHealthCheckListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_health_check_list_with_options_async(request, runtime)

    def describe_elastic_bandwidth_spec_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse(),
            self.do_request('DescribeElasticBandwidthSpec', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_elastic_bandwidth_spec_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse(),
            await self.do_request_async('DescribeElasticBandwidthSpec', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_elastic_bandwidth_spec(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_elastic_bandwidth_spec_with_options(request, runtime)

    async def describe_elastic_bandwidth_spec_async(
        self,
        request: ddoscoo_20171228_models.DescribeElasticBandwidthSpecRequest,
    ) -> ddoscoo_20171228_models.DescribeElasticBandwidthSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_elastic_bandwidth_spec_with_options_async(request, runtime)

    def describe_ddo_straffic_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDDoSTrafficResponse(),
            self.do_request('DescribeDDoSTraffic', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_ddo_straffic_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDDoSTrafficResponse(),
            await self.do_request_async('DescribeDDoSTraffic', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_ddo_straffic(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_straffic_with_options(request, runtime)

    async def describe_ddo_straffic_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSTrafficRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSTrafficResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_straffic_with_options_async(request, runtime)

    def describe_ddo_sevents_with_options(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDDoSEventsResponse(),
            self.do_request('DescribeDDoSEvents', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_ddo_sevents_with_options_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DescribeDDoSEventsResponse(),
            await self.do_request_async('DescribeDDoSEvents', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_ddo_sevents(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sevents_with_options(request, runtime)

    async def describe_ddo_sevents_async(
        self,
        request: ddoscoo_20171228_models.DescribeDDoSEventsRequest,
    ) -> ddoscoo_20171228_models.DescribeDDoSEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_sevents_with_options_async(request, runtime)

    def delete_layer_4rule_with_options(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteLayer4RuleResponse(),
            self.do_request('DeleteLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_layer_4rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.DeleteLayer4RuleResponse(),
            await self.do_request_async('DeleteLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_layer_4rule(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_layer_4rule_with_options(request, runtime)

    async def delete_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.DeleteLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.DeleteLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_layer_4rule_with_options_async(request, runtime)

    def create_layer_4rule_with_options(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CreateLayer4RuleResponse(),
            self.do_request('CreateLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_layer_4rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.CreateLayer4RuleResponse(),
            await self.do_request_async('CreateLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_layer_4rule(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_layer_4rule_with_options(request, runtime)

    async def create_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.CreateLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.CreateLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_layer_4rule_with_options_async(request, runtime)

    def config_layer_4rule_attribute_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse(),
            self.do_request('ConfigLayer4RuleAttribute', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_layer_4rule_attribute_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse(),
            await self.do_request_async('ConfigLayer4RuleAttribute', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_layer_4rule_attribute(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_attribute_with_options(request, runtime)

    async def config_layer_4rule_attribute_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleAttributeRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_attribute_with_options_async(request, runtime)

    def config_layer_4rule_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer4RuleResponse(),
            self.do_request('ConfigLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_layer_4rule_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigLayer4RuleResponse(),
            await self.do_request_async('ConfigLayer4Rule', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_layer_4rule(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_layer_4rule_with_options(request, runtime)

    async def config_layer_4rule_async(
        self,
        request: ddoscoo_20171228_models.ConfigLayer4RuleRequest,
    ) -> ddoscoo_20171228_models.ConfigLayer4RuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_layer_4rule_with_options_async(request, runtime)

    def config_health_check_with_options(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigHealthCheckResponse(),
            self.do_request('ConfigHealthCheck', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def config_health_check_with_options_async(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            ddoscoo_20171228_models.ConfigHealthCheckResponse(),
            await self.do_request_async('ConfigHealthCheck', 'HTTPS', 'POST', '2017-12-28', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def config_health_check(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_health_check_with_options(request, runtime)

    async def config_health_check_async(
        self,
        request: ddoscoo_20171228_models.ConfigHealthCheckRequest,
    ) -> ddoscoo_20171228_models.ConfigHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_health_check_with_options_async(request, runtime)

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
