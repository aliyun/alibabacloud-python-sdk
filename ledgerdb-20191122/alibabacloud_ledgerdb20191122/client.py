# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ledgerdb20191122 import models as ledgerdb_20191122_models
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
        self._endpoint = self.get_endpoint('ledgerdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_member_with_options(
        self,
        request: ledgerdb_20191122_models.AcceptMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.AcceptMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.AcceptMemberResponse().from_map(
            self.do_rpcrequest('AcceptMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def accept_member_with_options_async(
        self,
        request: ledgerdb_20191122_models.AcceptMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.AcceptMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.AcceptMemberResponse().from_map(
            await self.do_rpcrequest_async('AcceptMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_member(
        self,
        request: ledgerdb_20191122_models.AcceptMemberRequest,
    ) -> ledgerdb_20191122_models.AcceptMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_member_with_options(request, runtime)

    async def accept_member_async(
        self,
        request: ledgerdb_20191122_models.AcceptMemberRequest,
    ) -> ledgerdb_20191122_models.AcceptMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_member_with_options_async(request, runtime)

    def create_vpc_endpoint_with_options(
        self,
        request: ledgerdb_20191122_models.CreateVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.CreateVpcEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.CreateVpcEndpointResponse().from_map(
            self.do_rpcrequest('CreateVpcEndpoint', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpc_endpoint_with_options_async(
        self,
        request: ledgerdb_20191122_models.CreateVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.CreateVpcEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.CreateVpcEndpointResponse().from_map(
            await self.do_rpcrequest_async('CreateVpcEndpoint', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpc_endpoint(
        self,
        request: ledgerdb_20191122_models.CreateVpcEndpointRequest,
    ) -> ledgerdb_20191122_models.CreateVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_endpoint_with_options(request, runtime)

    async def create_vpc_endpoint_async(
        self,
        request: ledgerdb_20191122_models.CreateVpcEndpointRequest,
    ) -> ledgerdb_20191122_models.CreateVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_endpoint_with_options_async(request, runtime)

    def delete_ledger_with_options(
        self,
        request: ledgerdb_20191122_models.DeleteLedgerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DeleteLedgerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DeleteLedgerResponse().from_map(
            self.do_rpcrequest('DeleteLedger', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ledger_with_options_async(
        self,
        request: ledgerdb_20191122_models.DeleteLedgerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DeleteLedgerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DeleteLedgerResponse().from_map(
            await self.do_rpcrequest_async('DeleteLedger', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ledger(
        self,
        request: ledgerdb_20191122_models.DeleteLedgerRequest,
    ) -> ledgerdb_20191122_models.DeleteLedgerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ledger_with_options(request, runtime)

    async def delete_ledger_async(
        self,
        request: ledgerdb_20191122_models.DeleteLedgerRequest,
    ) -> ledgerdb_20191122_models.DeleteLedgerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ledger_with_options_async(request, runtime)

    def delete_member_with_options(
        self,
        request: ledgerdb_20191122_models.DeleteMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DeleteMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DeleteMemberResponse().from_map(
            self.do_rpcrequest('DeleteMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_member_with_options_async(
        self,
        request: ledgerdb_20191122_models.DeleteMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DeleteMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DeleteMemberResponse().from_map(
            await self.do_rpcrequest_async('DeleteMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_member(
        self,
        request: ledgerdb_20191122_models.DeleteMemberRequest,
    ) -> ledgerdb_20191122_models.DeleteMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_member_with_options(request, runtime)

    async def delete_member_async(
        self,
        request: ledgerdb_20191122_models.DeleteMemberRequest,
    ) -> ledgerdb_20191122_models.DeleteMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_member_with_options_async(request, runtime)

    def delete_vpc_endpoint_with_options(
        self,
        request: ledgerdb_20191122_models.DeleteVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DeleteVpcEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DeleteVpcEndpointResponse().from_map(
            self.do_rpcrequest('DeleteVpcEndpoint', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpc_endpoint_with_options_async(
        self,
        request: ledgerdb_20191122_models.DeleteVpcEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DeleteVpcEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DeleteVpcEndpointResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpcEndpoint', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpc_endpoint(
        self,
        request: ledgerdb_20191122_models.DeleteVpcEndpointRequest,
    ) -> ledgerdb_20191122_models.DeleteVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_endpoint_with_options(request, runtime)

    async def delete_vpc_endpoint_async(
        self,
        request: ledgerdb_20191122_models.DeleteVpcEndpointRequest,
    ) -> ledgerdb_20191122_models.DeleteVpcEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_endpoint_with_options_async(request, runtime)

    def describe_ledger_with_options(
        self,
        request: ledgerdb_20191122_models.DescribeLedgerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeLedgerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.DescribeLedgerResponse().from_map(
            self.do_rpcrequest('DescribeLedger', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_ledger_with_options_async(
        self,
        request: ledgerdb_20191122_models.DescribeLedgerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeLedgerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.DescribeLedgerResponse().from_map(
            await self.do_rpcrequest_async('DescribeLedger', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_ledger(
        self,
        request: ledgerdb_20191122_models.DescribeLedgerRequest,
    ) -> ledgerdb_20191122_models.DescribeLedgerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ledger_with_options(request, runtime)

    async def describe_ledger_async(
        self,
        request: ledgerdb_20191122_models.DescribeLedgerRequest,
    ) -> ledgerdb_20191122_models.DescribeLedgerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ledger_with_options_async(request, runtime)

    def describe_ledgers_with_options(
        self,
        request: ledgerdb_20191122_models.DescribeLedgersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeLedgersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.DescribeLedgersResponse().from_map(
            self.do_rpcrequest('DescribeLedgers', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_ledgers_with_options_async(
        self,
        request: ledgerdb_20191122_models.DescribeLedgersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeLedgersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.DescribeLedgersResponse().from_map(
            await self.do_rpcrequest_async('DescribeLedgers', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_ledgers(
        self,
        request: ledgerdb_20191122_models.DescribeLedgersRequest,
    ) -> ledgerdb_20191122_models.DescribeLedgersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ledgers_with_options(request, runtime)

    async def describe_ledgers_async(
        self,
        request: ledgerdb_20191122_models.DescribeLedgersRequest,
    ) -> ledgerdb_20191122_models.DescribeLedgersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ledgers_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ledgerdb_20191122_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ledgerdb_20191122_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: ledgerdb_20191122_models.DescribeRegionsRequest,
    ) -> ledgerdb_20191122_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ledgerdb_20191122_models.DescribeRegionsRequest,
    ) -> ledgerdb_20191122_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_tsawith_options(
        self,
        request: ledgerdb_20191122_models.DescribeTSARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeTSAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DescribeTSAResponse().from_map(
            self.do_rpcrequest('DescribeTSA', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tsawith_options_async(
        self,
        request: ledgerdb_20191122_models.DescribeTSARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DescribeTSAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DescribeTSAResponse().from_map(
            await self.do_rpcrequest_async('DescribeTSA', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tsa(
        self,
        request: ledgerdb_20191122_models.DescribeTSARequest,
    ) -> ledgerdb_20191122_models.DescribeTSAResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tsawith_options(request, runtime)

    async def describe_tsa_async(
        self,
        request: ledgerdb_20191122_models.DescribeTSARequest,
    ) -> ledgerdb_20191122_models.DescribeTSAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tsawith_options_async(request, runtime)

    def disable_member_with_options(
        self,
        request: ledgerdb_20191122_models.DisableMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DisableMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DisableMemberResponse().from_map(
            self.do_rpcrequest('DisableMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_member_with_options_async(
        self,
        request: ledgerdb_20191122_models.DisableMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.DisableMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.DisableMemberResponse().from_map(
            await self.do_rpcrequest_async('DisableMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_member(
        self,
        request: ledgerdb_20191122_models.DisableMemberRequest,
    ) -> ledgerdb_20191122_models.DisableMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_member_with_options(request, runtime)

    async def disable_member_async(
        self,
        request: ledgerdb_20191122_models.DisableMemberRequest,
    ) -> ledgerdb_20191122_models.DisableMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_member_with_options_async(request, runtime)

    def enable_member_with_options(
        self,
        request: ledgerdb_20191122_models.EnableMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.EnableMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.EnableMemberResponse().from_map(
            self.do_rpcrequest('EnableMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_member_with_options_async(
        self,
        request: ledgerdb_20191122_models.EnableMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.EnableMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.EnableMemberResponse().from_map(
            await self.do_rpcrequest_async('EnableMember', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_member(
        self,
        request: ledgerdb_20191122_models.EnableMemberRequest,
    ) -> ledgerdb_20191122_models.EnableMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_member_with_options(request, runtime)

    async def enable_member_async(
        self,
        request: ledgerdb_20191122_models.EnableMemberRequest,
    ) -> ledgerdb_20191122_models.EnableMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_member_with_options_async(request, runtime)

    def get_access_attribute_with_options(
        self,
        request: ledgerdb_20191122_models.GetAccessAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetAccessAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetAccessAttributeResponse().from_map(
            self.do_rpcrequest('GetAccessAttribute', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_access_attribute_with_options_async(
        self,
        request: ledgerdb_20191122_models.GetAccessAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetAccessAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetAccessAttributeResponse().from_map(
            await self.do_rpcrequest_async('GetAccessAttribute', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_access_attribute(
        self,
        request: ledgerdb_20191122_models.GetAccessAttributeRequest,
    ) -> ledgerdb_20191122_models.GetAccessAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_attribute_with_options(request, runtime)

    async def get_access_attribute_async(
        self,
        request: ledgerdb_20191122_models.GetAccessAttributeRequest,
    ) -> ledgerdb_20191122_models.GetAccessAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_attribute_with_options_async(request, runtime)

    def get_ip_white_list_with_options(
        self,
        request: ledgerdb_20191122_models.GetIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetIpWhiteListResponse().from_map(
            self.do_rpcrequest('GetIpWhiteList', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_ip_white_list_with_options_async(
        self,
        request: ledgerdb_20191122_models.GetIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetIpWhiteListResponse().from_map(
            await self.do_rpcrequest_async('GetIpWhiteList', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ip_white_list(
        self,
        request: ledgerdb_20191122_models.GetIpWhiteListRequest,
    ) -> ledgerdb_20191122_models.GetIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ip_white_list_with_options(request, runtime)

    async def get_ip_white_list_async(
        self,
        request: ledgerdb_20191122_models.GetIpWhiteListRequest,
    ) -> ledgerdb_20191122_models.GetIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ip_white_list_with_options_async(request, runtime)

    def get_journal_with_options(
        self,
        request: ledgerdb_20191122_models.GetJournalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetJournalResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetJournalResponse().from_map(
            self.do_rpcrequest('GetJournal', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_journal_with_options_async(
        self,
        request: ledgerdb_20191122_models.GetJournalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetJournalResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetJournalResponse().from_map(
            await self.do_rpcrequest_async('GetJournal', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_journal(
        self,
        request: ledgerdb_20191122_models.GetJournalRequest,
    ) -> ledgerdb_20191122_models.GetJournalResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_journal_with_options(request, runtime)

    async def get_journal_async(
        self,
        request: ledgerdb_20191122_models.GetJournalRequest,
    ) -> ledgerdb_20191122_models.GetJournalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_journal_with_options_async(request, runtime)

    def get_member_with_options(
        self,
        request: ledgerdb_20191122_models.GetMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetMemberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetMemberResponse().from_map(
            self.do_rpcrequest('GetMember', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_member_with_options_async(
        self,
        request: ledgerdb_20191122_models.GetMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GetMemberResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.GetMemberResponse().from_map(
            await self.do_rpcrequest_async('GetMember', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_member(
        self,
        request: ledgerdb_20191122_models.GetMemberRequest,
    ) -> ledgerdb_20191122_models.GetMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_member_with_options(request, runtime)

    async def get_member_async(
        self,
        request: ledgerdb_20191122_models.GetMemberRequest,
    ) -> ledgerdb_20191122_models.GetMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_member_with_options_async(request, runtime)

    def grant_service_linked_role_with_options(
        self,
        request: ledgerdb_20191122_models.GrantServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GrantServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.GrantServiceLinkedRoleResponse().from_map(
            self.do_rpcrequest('GrantServiceLinkedRole', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_service_linked_role_with_options_async(
        self,
        request: ledgerdb_20191122_models.GrantServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.GrantServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.GrantServiceLinkedRoleResponse().from_map(
            await self.do_rpcrequest_async('GrantServiceLinkedRole', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_service_linked_role(
        self,
        request: ledgerdb_20191122_models.GrantServiceLinkedRoleRequest,
    ) -> ledgerdb_20191122_models.GrantServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_service_linked_role_with_options(request, runtime)

    async def grant_service_linked_role_async(
        self,
        request: ledgerdb_20191122_models.GrantServiceLinkedRoleRequest,
    ) -> ledgerdb_20191122_models.GrantServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_service_linked_role_with_options_async(request, runtime)

    def invite_members_with_options(
        self,
        request: ledgerdb_20191122_models.InviteMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.InviteMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.InviteMembersResponse().from_map(
            self.do_rpcrequest('InviteMembers', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invite_members_with_options_async(
        self,
        request: ledgerdb_20191122_models.InviteMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.InviteMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.InviteMembersResponse().from_map(
            await self.do_rpcrequest_async('InviteMembers', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invite_members(
        self,
        request: ledgerdb_20191122_models.InviteMembersRequest,
    ) -> ledgerdb_20191122_models.InviteMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.invite_members_with_options(request, runtime)

    async def invite_members_async(
        self,
        request: ledgerdb_20191122_models.InviteMembersRequest,
    ) -> ledgerdb_20191122_models.InviteMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invite_members_with_options_async(request, runtime)

    def list_journals_with_options(
        self,
        request: ledgerdb_20191122_models.ListJournalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListJournalsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListJournalsResponse().from_map(
            self.do_rpcrequest('ListJournals', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_journals_with_options_async(
        self,
        request: ledgerdb_20191122_models.ListJournalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListJournalsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListJournalsResponse().from_map(
            await self.do_rpcrequest_async('ListJournals', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_journals(
        self,
        request: ledgerdb_20191122_models.ListJournalsRequest,
    ) -> ledgerdb_20191122_models.ListJournalsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_journals_with_options(request, runtime)

    async def list_journals_async(
        self,
        request: ledgerdb_20191122_models.ListJournalsRequest,
    ) -> ledgerdb_20191122_models.ListJournalsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_journals_with_options_async(request, runtime)

    def list_members_with_options(
        self,
        request: ledgerdb_20191122_models.ListMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListMembersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListMembersResponse().from_map(
            self.do_rpcrequest('ListMembers', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_members_with_options_async(
        self,
        request: ledgerdb_20191122_models.ListMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListMembersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListMembersResponse().from_map(
            await self.do_rpcrequest_async('ListMembers', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_members(
        self,
        request: ledgerdb_20191122_models.ListMembersRequest,
    ) -> ledgerdb_20191122_models.ListMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_members_with_options(request, runtime)

    async def list_members_async(
        self,
        request: ledgerdb_20191122_models.ListMembersRequest,
    ) -> ledgerdb_20191122_models.ListMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_members_with_options_async(request, runtime)

    def list_time_anchors_with_options(
        self,
        request: ledgerdb_20191122_models.ListTimeAnchorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListTimeAnchorsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListTimeAnchorsResponse().from_map(
            self.do_rpcrequest('ListTimeAnchors', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_time_anchors_with_options_async(
        self,
        request: ledgerdb_20191122_models.ListTimeAnchorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListTimeAnchorsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListTimeAnchorsResponse().from_map(
            await self.do_rpcrequest_async('ListTimeAnchors', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_time_anchors(
        self,
        request: ledgerdb_20191122_models.ListTimeAnchorsRequest,
    ) -> ledgerdb_20191122_models.ListTimeAnchorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_time_anchors_with_options(request, runtime)

    async def list_time_anchors_async(
        self,
        request: ledgerdb_20191122_models.ListTimeAnchorsRequest,
    ) -> ledgerdb_20191122_models.ListTimeAnchorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_time_anchors_with_options_async(request, runtime)

    def list_vpc_endpoints_with_options(
        self,
        request: ledgerdb_20191122_models.ListVpcEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListVpcEndpointsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListVpcEndpointsResponse().from_map(
            self.do_rpcrequest('ListVpcEndpoints', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_vpc_endpoints_with_options_async(
        self,
        request: ledgerdb_20191122_models.ListVpcEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ListVpcEndpointsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return ledgerdb_20191122_models.ListVpcEndpointsResponse().from_map(
            await self.do_rpcrequest_async('ListVpcEndpoints', '2019-11-22', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_vpc_endpoints(
        self,
        request: ledgerdb_20191122_models.ListVpcEndpointsRequest,
    ) -> ledgerdb_20191122_models.ListVpcEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoints_with_options(request, runtime)

    async def list_vpc_endpoints_async(
        self,
        request: ledgerdb_20191122_models.ListVpcEndpointsRequest,
    ) -> ledgerdb_20191122_models.ListVpcEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoints_with_options_async(request, runtime)

    def modify_access_attribute_with_options(
        self,
        request: ledgerdb_20191122_models.ModifyAccessAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyAccessAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyAccessAttributeResponse().from_map(
            self.do_rpcrequest('ModifyAccessAttribute', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_access_attribute_with_options_async(
        self,
        request: ledgerdb_20191122_models.ModifyAccessAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyAccessAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyAccessAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyAccessAttribute', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_access_attribute(
        self,
        request: ledgerdb_20191122_models.ModifyAccessAttributeRequest,
    ) -> ledgerdb_20191122_models.ModifyAccessAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_access_attribute_with_options(request, runtime)

    async def modify_access_attribute_async(
        self,
        request: ledgerdb_20191122_models.ModifyAccessAttributeRequest,
    ) -> ledgerdb_20191122_models.ModifyAccessAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_attribute_with_options_async(request, runtime)

    def modify_ip_white_list_with_options(
        self,
        request: ledgerdb_20191122_models.ModifyIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyIpWhiteListResponse().from_map(
            self.do_rpcrequest('ModifyIpWhiteList', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ip_white_list_with_options_async(
        self,
        request: ledgerdb_20191122_models.ModifyIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyIpWhiteListResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpWhiteList', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ip_white_list(
        self,
        request: ledgerdb_20191122_models.ModifyIpWhiteListRequest,
    ) -> ledgerdb_20191122_models.ModifyIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ip_white_list_with_options(request, runtime)

    async def modify_ip_white_list_async(
        self,
        request: ledgerdb_20191122_models.ModifyIpWhiteListRequest,
    ) -> ledgerdb_20191122_models.ModifyIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ip_white_list_with_options_async(request, runtime)

    def modify_ledger_attribute_with_options(
        self,
        request: ledgerdb_20191122_models.ModifyLedgerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyLedgerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyLedgerAttributeResponse().from_map(
            self.do_rpcrequest('ModifyLedgerAttribute', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ledger_attribute_with_options_async(
        self,
        request: ledgerdb_20191122_models.ModifyLedgerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyLedgerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyLedgerAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyLedgerAttribute', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ledger_attribute(
        self,
        request: ledgerdb_20191122_models.ModifyLedgerAttributeRequest,
    ) -> ledgerdb_20191122_models.ModifyLedgerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ledger_attribute_with_options(request, runtime)

    async def modify_ledger_attribute_async(
        self,
        request: ledgerdb_20191122_models.ModifyLedgerAttributeRequest,
    ) -> ledgerdb_20191122_models.ModifyLedgerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ledger_attribute_with_options_async(request, runtime)

    def modify_member_acls_with_options(
        self,
        request: ledgerdb_20191122_models.ModifyMemberACLsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyMemberACLsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyMemberACLsResponse().from_map(
            self.do_rpcrequest('ModifyMemberACLs', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_member_acls_with_options_async(
        self,
        request: ledgerdb_20191122_models.ModifyMemberACLsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyMemberACLsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyMemberACLsResponse().from_map(
            await self.do_rpcrequest_async('ModifyMemberACLs', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_member_acls(
        self,
        request: ledgerdb_20191122_models.ModifyMemberACLsRequest,
    ) -> ledgerdb_20191122_models.ModifyMemberACLsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_member_acls_with_options(request, runtime)

    async def modify_member_acls_async(
        self,
        request: ledgerdb_20191122_models.ModifyMemberACLsRequest,
    ) -> ledgerdb_20191122_models.ModifyMemberACLsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_member_acls_with_options_async(request, runtime)

    def modify_member_key_with_options(
        self,
        request: ledgerdb_20191122_models.ModifyMemberKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyMemberKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyMemberKeyResponse().from_map(
            self.do_rpcrequest('ModifyMemberKey', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_member_key_with_options_async(
        self,
        request: ledgerdb_20191122_models.ModifyMemberKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.ModifyMemberKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.ModifyMemberKeyResponse().from_map(
            await self.do_rpcrequest_async('ModifyMemberKey', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_member_key(
        self,
        request: ledgerdb_20191122_models.ModifyMemberKeyRequest,
    ) -> ledgerdb_20191122_models.ModifyMemberKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_member_key_with_options(request, runtime)

    async def modify_member_key_async(
        self,
        request: ledgerdb_20191122_models.ModifyMemberKeyRequest,
    ) -> ledgerdb_20191122_models.ModifyMemberKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_member_key_with_options_async(request, runtime)

    def update_member_key_by_kmswith_options(
        self,
        request: ledgerdb_20191122_models.UpdateMemberKeyByKMSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.UpdateMemberKeyByKMSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.UpdateMemberKeyByKMSResponse().from_map(
            self.do_rpcrequest('UpdateMemberKeyByKMS', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_member_key_by_kmswith_options_async(
        self,
        request: ledgerdb_20191122_models.UpdateMemberKeyByKMSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ledgerdb_20191122_models.UpdateMemberKeyByKMSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ledgerdb_20191122_models.UpdateMemberKeyByKMSResponse().from_map(
            await self.do_rpcrequest_async('UpdateMemberKeyByKMS', '2019-11-22', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_member_key_by_kms(
        self,
        request: ledgerdb_20191122_models.UpdateMemberKeyByKMSRequest,
    ) -> ledgerdb_20191122_models.UpdateMemberKeyByKMSResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_member_key_by_kmswith_options(request, runtime)

    async def update_member_key_by_kms_async(
        self,
        request: ledgerdb_20191122_models.UpdateMemberKeyByKMSRequest,
    ) -> ledgerdb_20191122_models.UpdateMemberKeyByKMSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_member_key_by_kmswith_options_async(request, runtime)
