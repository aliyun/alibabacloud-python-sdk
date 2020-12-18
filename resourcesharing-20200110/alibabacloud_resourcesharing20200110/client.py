# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_resourcesharing20200110 import models as resource_sharing_20200110_models
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
        self._endpoint = self.get_endpoint('resourcesharing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_regions_with_options(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.DescribeRegionsResponse().from_map(
            self.do_request('DescribeRegions', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.DescribeRegionsResponse().from_map(
            await self.do_request_async('DescribeRegions', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_regions(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: resource_sharing_20200110_models.DescribeRegionsRequest,
    ) -> resource_sharing_20200110_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def list_resource_shares_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListResourceSharesResponse().from_map(
            self.do_request('ListResourceShares', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_resource_shares_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListResourceSharesResponse().from_map(
            await self.do_request_async('ListResourceShares', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_resource_shares(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_shares_with_options(request, runtime)

    async def list_resource_shares_async(
        self,
        request: resource_sharing_20200110_models.ListResourceSharesRequest,
    ) -> resource_sharing_20200110_models.ListResourceSharesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_shares_with_options_async(request, runtime)

    def list_shared_resources_with_options(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListSharedResourcesResponse().from_map(
            self.do_request('ListSharedResources', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_shared_resources_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListSharedResourcesResponse().from_map(
            await self.do_request_async('ListSharedResources', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_shared_resources(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_shared_resources_with_options(request, runtime)

    async def list_shared_resources_async(
        self,
        request: resource_sharing_20200110_models.ListSharedResourcesRequest,
    ) -> resource_sharing_20200110_models.ListSharedResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_resources_with_options_async(request, runtime)

    def list_shared_targets_with_options(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListSharedTargetsResponse().from_map(
            self.do_request('ListSharedTargets', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_shared_targets_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListSharedTargetsResponse().from_map(
            await self.do_request_async('ListSharedTargets', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_shared_targets(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_shared_targets_with_options(request, runtime)

    async def list_shared_targets_async(
        self,
        request: resource_sharing_20200110_models.ListSharedTargetsRequest,
    ) -> resource_sharing_20200110_models.ListSharedTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_shared_targets_with_options_async(request, runtime)

    def associate_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.AssociateResourceShareResponse().from_map(
            self.do_request('AssociateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def associate_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.AssociateResourceShareResponse().from_map(
            await self.do_request_async('AssociateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def associate_resource_share(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_resource_share_with_options(request, runtime)

    async def associate_resource_share_async(
        self,
        request: resource_sharing_20200110_models.AssociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.AssociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_resource_share_with_options_async(request, runtime)

    def update_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.UpdateResourceShareResponse().from_map(
            self.do_request('UpdateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.UpdateResourceShareResponse().from_map(
            await self.do_request_async('UpdateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_resource_share(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_share_with_options(request, runtime)

    async def update_resource_share_async(
        self,
        request: resource_sharing_20200110_models.UpdateResourceShareRequest,
    ) -> resource_sharing_20200110_models.UpdateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_share_with_options_async(request, runtime)

    def delete_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.DeleteResourceShareResponse().from_map(
            self.do_request('DeleteResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.DeleteResourceShareResponse().from_map(
            await self.do_request_async('DeleteResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_resource_share(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_share_with_options(request, runtime)

    async def delete_resource_share_async(
        self,
        request: resource_sharing_20200110_models.DeleteResourceShareRequest,
    ) -> resource_sharing_20200110_models.DeleteResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_share_with_options_async(request, runtime)

    def disassociate_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.DisassociateResourceShareResponse().from_map(
            self.do_request('DisassociateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def disassociate_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.DisassociateResourceShareResponse().from_map(
            await self.do_request_async('DisassociateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disassociate_resource_share(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.disassociate_resource_share_with_options(request, runtime)

    async def disassociate_resource_share_async(
        self,
        request: resource_sharing_20200110_models.DisassociateResourceShareRequest,
    ) -> resource_sharing_20200110_models.DisassociateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_resource_share_with_options_async(request, runtime)

    def list_resource_share_associations_with_options(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListResourceShareAssociationsResponse().from_map(
            self.do_request('ListResourceShareAssociations', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_resource_share_associations_with_options_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.ListResourceShareAssociationsResponse().from_map(
            await self.do_request_async('ListResourceShareAssociations', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_resource_share_associations(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_associations_with_options(request, runtime)

    async def list_resource_share_associations_async(
        self,
        request: resource_sharing_20200110_models.ListResourceShareAssociationsRequest,
    ) -> resource_sharing_20200110_models.ListResourceShareAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_share_associations_with_options_async(request, runtime)

    def create_resource_share_with_options(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.CreateResourceShareResponse().from_map(
            self.do_request('CreateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_resource_share_with_options_async(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        UtilClient.validate_model(request)
        return resource_sharing_20200110_models.CreateResourceShareResponse().from_map(
            await self.do_request_async('CreateResourceShare', 'HTTPS', 'POST', '2020-01-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_resource_share(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_share_with_options(request, runtime)

    async def create_resource_share_async(
        self,
        request: resource_sharing_20200110_models.CreateResourceShareRequest,
    ) -> resource_sharing_20200110_models.CreateResourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_share_with_options_async(request, runtime)

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
