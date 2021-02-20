# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_avds20171129 import models as avds_20171129_models
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
        self._endpoint = self.get_endpoint('avds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_assets_with_options(
        self,
        request: avds_20171129_models.AddAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddAssetsResponse().from_map(
            self.do_rpcrequest('AddAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_assets_with_options_async(
        self,
        request: avds_20171129_models.AddAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddAssetsResponse().from_map(
            await self.do_rpcrequest_async('AddAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_assets(
        self,
        request: avds_20171129_models.AddAssetsRequest,
    ) -> avds_20171129_models.AddAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_assets_with_options(request, runtime)

    async def add_assets_async(
        self,
        request: avds_20171129_models.AddAssetsRequest,
    ) -> avds_20171129_models.AddAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_assets_with_options_async(request, runtime)

    def add_asset_tags_with_options(
        self,
        request: avds_20171129_models.AddAssetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddAssetTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddAssetTagsResponse().from_map(
            self.do_rpcrequest('AddAssetTags', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_asset_tags_with_options_async(
        self,
        request: avds_20171129_models.AddAssetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddAssetTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddAssetTagsResponse().from_map(
            await self.do_rpcrequest_async('AddAssetTags', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_asset_tags(
        self,
        request: avds_20171129_models.AddAssetTagsRequest,
    ) -> avds_20171129_models.AddAssetTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_asset_tags_with_options(request, runtime)

    async def add_asset_tags_async(
        self,
        request: avds_20171129_models.AddAssetTagsRequest,
    ) -> avds_20171129_models.AddAssetTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_asset_tags_with_options_async(request, runtime)

    def add_org_domains_with_options(
        self,
        request: avds_20171129_models.AddOrgDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgDomainsResponse().from_map(
            self.do_rpcrequest('AddOrgDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_org_domains_with_options_async(
        self,
        request: avds_20171129_models.AddOrgDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgDomainsResponse().from_map(
            await self.do_rpcrequest_async('AddOrgDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_org_domains(
        self,
        request: avds_20171129_models.AddOrgDomainsRequest,
    ) -> avds_20171129_models.AddOrgDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_org_domains_with_options(request, runtime)

    async def add_org_domains_async(
        self,
        request: avds_20171129_models.AddOrgDomainsRequest,
    ) -> avds_20171129_models.AddOrgDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_org_domains_with_options_async(request, runtime)

    def add_org_hosts_with_options(
        self,
        request: avds_20171129_models.AddOrgHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgHostsResponse().from_map(
            self.do_rpcrequest('AddOrgHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_org_hosts_with_options_async(
        self,
        request: avds_20171129_models.AddOrgHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgHostsResponse().from_map(
            await self.do_rpcrequest_async('AddOrgHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_org_hosts(
        self,
        request: avds_20171129_models.AddOrgHostsRequest,
    ) -> avds_20171129_models.AddOrgHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_org_hosts_with_options(request, runtime)

    async def add_org_hosts_async(
        self,
        request: avds_20171129_models.AddOrgHostsRequest,
    ) -> avds_20171129_models.AddOrgHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_org_hosts_with_options_async(request, runtime)

    def add_org_subdomains_with_options(
        self,
        request: avds_20171129_models.AddOrgSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgSubdomainsResponse().from_map(
            self.do_rpcrequest('AddOrgSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_org_subdomains_with_options_async(
        self,
        request: avds_20171129_models.AddOrgSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgSubdomainsResponse().from_map(
            await self.do_rpcrequest_async('AddOrgSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_org_subdomains(
        self,
        request: avds_20171129_models.AddOrgSubdomainsRequest,
    ) -> avds_20171129_models.AddOrgSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_org_subdomains_with_options(request, runtime)

    async def add_org_subdomains_async(
        self,
        request: avds_20171129_models.AddOrgSubdomainsRequest,
    ) -> avds_20171129_models.AddOrgSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_org_subdomains_with_options_async(request, runtime)

    def add_org_web_paths_with_options(
        self,
        request: avds_20171129_models.AddOrgWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgWebPathsResponse().from_map(
            self.do_rpcrequest('AddOrgWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_org_web_paths_with_options_async(
        self,
        request: avds_20171129_models.AddOrgWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.AddOrgWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.AddOrgWebPathsResponse().from_map(
            await self.do_rpcrequest_async('AddOrgWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_org_web_paths(
        self,
        request: avds_20171129_models.AddOrgWebPathsRequest,
    ) -> avds_20171129_models.AddOrgWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_org_web_paths_with_options(request, runtime)

    async def add_org_web_paths_async(
        self,
        request: avds_20171129_models.AddOrgWebPathsRequest,
    ) -> avds_20171129_models.AddOrgWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_org_web_paths_with_options_async(request, runtime)

    def create_avds_bag_order_with_options(
        self,
        request: avds_20171129_models.CreateAvdsBagOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateAvdsBagOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateAvdsBagOrderResponse().from_map(
            self.do_rpcrequest('CreateAvdsBagOrder', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_avds_bag_order_with_options_async(
        self,
        request: avds_20171129_models.CreateAvdsBagOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateAvdsBagOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateAvdsBagOrderResponse().from_map(
            await self.do_rpcrequest_async('CreateAvdsBagOrder', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_avds_bag_order(
        self,
        request: avds_20171129_models.CreateAvdsBagOrderRequest,
    ) -> avds_20171129_models.CreateAvdsBagOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_avds_bag_order_with_options(request, runtime)

    async def create_avds_bag_order_async(
        self,
        request: avds_20171129_models.CreateAvdsBagOrderRequest,
    ) -> avds_20171129_models.CreateAvdsBagOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_avds_bag_order_with_options_async(request, runtime)

    def create_avds_order_with_options(
        self,
        request: avds_20171129_models.CreateAvdsOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateAvdsOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateAvdsOrderResponse().from_map(
            self.do_rpcrequest('CreateAvdsOrder', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_avds_order_with_options_async(
        self,
        request: avds_20171129_models.CreateAvdsOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateAvdsOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateAvdsOrderResponse().from_map(
            await self.do_rpcrequest_async('CreateAvdsOrder', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_avds_order(
        self,
        request: avds_20171129_models.CreateAvdsOrderRequest,
    ) -> avds_20171129_models.CreateAvdsOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_avds_order_with_options(request, runtime)

    async def create_avds_order_async(
        self,
        request: avds_20171129_models.CreateAvdsOrderRequest,
    ) -> avds_20171129_models.CreateAvdsOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_avds_order_with_options_async(request, runtime)

    def create_avds_public_order_with_options(
        self,
        request: avds_20171129_models.CreateAvdsPublicOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateAvdsPublicOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateAvdsPublicOrderResponse().from_map(
            self.do_rpcrequest('CreateAvdsPublicOrder', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_avds_public_order_with_options_async(
        self,
        request: avds_20171129_models.CreateAvdsPublicOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateAvdsPublicOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateAvdsPublicOrderResponse().from_map(
            await self.do_rpcrequest_async('CreateAvdsPublicOrder', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_avds_public_order(
        self,
        request: avds_20171129_models.CreateAvdsPublicOrderRequest,
    ) -> avds_20171129_models.CreateAvdsPublicOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_avds_public_order_with_options(request, runtime)

    async def create_avds_public_order_async(
        self,
        request: avds_20171129_models.CreateAvdsPublicOrderRequest,
    ) -> avds_20171129_models.CreateAvdsPublicOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_avds_public_order_with_options_async(request, runtime)

    def create_organization_with_options(
        self,
        request: avds_20171129_models.CreateOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateOrganizationResponse().from_map(
            self.do_rpcrequest('CreateOrganization', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_organization_with_options_async(
        self,
        request: avds_20171129_models.CreateOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateOrganizationResponse().from_map(
            await self.do_rpcrequest_async('CreateOrganization', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_organization(
        self,
        request: avds_20171129_models.CreateOrganizationRequest,
    ) -> avds_20171129_models.CreateOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_organization_with_options(request, runtime)

    async def create_organization_async(
        self,
        request: avds_20171129_models.CreateOrganizationRequest,
    ) -> avds_20171129_models.CreateOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_organization_with_options_async(request, runtime)

    def create_session_with_options(
        self,
        request: avds_20171129_models.CreateSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateSessionResponse().from_map(
            self.do_rpcrequest('CreateSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_session_with_options_async(
        self,
        request: avds_20171129_models.CreateSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.CreateSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.CreateSessionResponse().from_map(
            await self.do_rpcrequest_async('CreateSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_session(
        self,
        request: avds_20171129_models.CreateSessionRequest,
    ) -> avds_20171129_models.CreateSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_session_with_options(request, runtime)

    async def create_session_async(
        self,
        request: avds_20171129_models.CreateSessionRequest,
    ) -> avds_20171129_models.CreateSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_session_with_options_async(request, runtime)

    def delete_assets_with_options(
        self,
        request: avds_20171129_models.DeleteAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteAssetsResponse().from_map(
            self.do_rpcrequest('DeleteAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_assets_with_options_async(
        self,
        request: avds_20171129_models.DeleteAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteAssetsResponse().from_map(
            await self.do_rpcrequest_async('DeleteAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_assets(
        self,
        request: avds_20171129_models.DeleteAssetsRequest,
    ) -> avds_20171129_models.DeleteAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_assets_with_options(request, runtime)

    async def delete_assets_async(
        self,
        request: avds_20171129_models.DeleteAssetsRequest,
    ) -> avds_20171129_models.DeleteAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_assets_with_options_async(request, runtime)

    def delete_organizations_with_options(
        self,
        request: avds_20171129_models.DeleteOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteOrganizationsResponse().from_map(
            self.do_rpcrequest('DeleteOrganizations', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_organizations_with_options_async(
        self,
        request: avds_20171129_models.DeleteOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteOrganizationsResponse().from_map(
            await self.do_rpcrequest_async('DeleteOrganizations', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_organizations(
        self,
        request: avds_20171129_models.DeleteOrganizationsRequest,
    ) -> avds_20171129_models.DeleteOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_organizations_with_options(request, runtime)

    async def delete_organizations_async(
        self,
        request: avds_20171129_models.DeleteOrganizationsRequest,
    ) -> avds_20171129_models.DeleteOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_organizations_with_options_async(request, runtime)

    def delete_org_attack_surface_records_with_options(
        self,
        request: avds_20171129_models.DeleteOrgAttackSurfaceRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteOrgAttackSurfaceRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteOrgAttackSurfaceRecordsResponse().from_map(
            self.do_rpcrequest('DeleteOrgAttackSurfaceRecords', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_org_attack_surface_records_with_options_async(
        self,
        request: avds_20171129_models.DeleteOrgAttackSurfaceRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteOrgAttackSurfaceRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteOrgAttackSurfaceRecordsResponse().from_map(
            await self.do_rpcrequest_async('DeleteOrgAttackSurfaceRecords', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_org_attack_surface_records(
        self,
        request: avds_20171129_models.DeleteOrgAttackSurfaceRecordsRequest,
    ) -> avds_20171129_models.DeleteOrgAttackSurfaceRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_org_attack_surface_records_with_options(request, runtime)

    async def delete_org_attack_surface_records_async(
        self,
        request: avds_20171129_models.DeleteOrgAttackSurfaceRecordsRequest,
    ) -> avds_20171129_models.DeleteOrgAttackSurfaceRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_org_attack_surface_records_with_options_async(request, runtime)

    def delete_session_with_options(
        self,
        request: avds_20171129_models.DeleteSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteSessionResponse().from_map(
            self.do_rpcrequest('DeleteSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_session_with_options_async(
        self,
        request: avds_20171129_models.DeleteSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteSessionResponse().from_map(
            await self.do_rpcrequest_async('DeleteSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_session(
        self,
        request: avds_20171129_models.DeleteSessionRequest,
    ) -> avds_20171129_models.DeleteSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_session_with_options(request, runtime)

    async def delete_session_async(
        self,
        request: avds_20171129_models.DeleteSessionRequest,
    ) -> avds_20171129_models.DeleteSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_session_with_options_async(request, runtime)

    def delete_user_attack_surface_records_with_options(
        self,
        request: avds_20171129_models.DeleteUserAttackSurfaceRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteUserAttackSurfaceRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteUserAttackSurfaceRecordsResponse().from_map(
            self.do_rpcrequest('DeleteUserAttackSurfaceRecords', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_attack_surface_records_with_options_async(
        self,
        request: avds_20171129_models.DeleteUserAttackSurfaceRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DeleteUserAttackSurfaceRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DeleteUserAttackSurfaceRecordsResponse().from_map(
            await self.do_rpcrequest_async('DeleteUserAttackSurfaceRecords', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_attack_surface_records(
        self,
        request: avds_20171129_models.DeleteUserAttackSurfaceRecordsRequest,
    ) -> avds_20171129_models.DeleteUserAttackSurfaceRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_attack_surface_records_with_options(request, runtime)

    async def delete_user_attack_surface_records_async(
        self,
        request: avds_20171129_models.DeleteUserAttackSurfaceRecordsRequest,
    ) -> avds_20171129_models.DeleteUserAttackSurfaceRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_attack_surface_records_with_options_async(request, runtime)

    def describe_all_vulnerabilities_with_options(
        self,
        request: avds_20171129_models.DescribeAllVulnerabilitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeAllVulnerabilitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeAllVulnerabilitiesResponse().from_map(
            self.do_rpcrequest('DescribeAllVulnerabilities', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_all_vulnerabilities_with_options_async(
        self,
        request: avds_20171129_models.DescribeAllVulnerabilitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeAllVulnerabilitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeAllVulnerabilitiesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAllVulnerabilities', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_all_vulnerabilities(
        self,
        request: avds_20171129_models.DescribeAllVulnerabilitiesRequest,
    ) -> avds_20171129_models.DescribeAllVulnerabilitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_vulnerabilities_with_options(request, runtime)

    async def describe_all_vulnerabilities_async(
        self,
        request: avds_20171129_models.DescribeAllVulnerabilitiesRequest,
    ) -> avds_20171129_models.DescribeAllVulnerabilitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_vulnerabilities_with_options_async(request, runtime)

    def describe_assets_with_options(
        self,
        request: avds_20171129_models.DescribeAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeAssetsResponse().from_map(
            self.do_rpcrequest('DescribeAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_assets_with_options_async(
        self,
        request: avds_20171129_models.DescribeAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeAssetsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_assets(
        self,
        request: avds_20171129_models.DescribeAssetsRequest,
    ) -> avds_20171129_models.DescribeAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_assets_with_options(request, runtime)

    async def describe_assets_async(
        self,
        request: avds_20171129_models.DescribeAssetsRequest,
    ) -> avds_20171129_models.DescribeAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_assets_with_options_async(request, runtime)

    def describe_attack_surfaces_facets_with_options(
        self,
        request: avds_20171129_models.DescribeAttackSurfacesFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeAttackSurfacesFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeAttackSurfacesFacetsResponse().from_map(
            self.do_rpcrequest('DescribeAttackSurfacesFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_attack_surfaces_facets_with_options_async(
        self,
        request: avds_20171129_models.DescribeAttackSurfacesFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeAttackSurfacesFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeAttackSurfacesFacetsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAttackSurfacesFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_attack_surfaces_facets(
        self,
        request: avds_20171129_models.DescribeAttackSurfacesFacetsRequest,
    ) -> avds_20171129_models.DescribeAttackSurfacesFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_surfaces_facets_with_options(request, runtime)

    async def describe_attack_surfaces_facets_async(
        self,
        request: avds_20171129_models.DescribeAttackSurfacesFacetsRequest,
    ) -> avds_20171129_models.DescribeAttackSurfacesFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_attack_surfaces_facets_with_options_async(request, runtime)

    def describe_crawler_requests_with_options(
        self,
        request: avds_20171129_models.DescribeCrawlerRequestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeCrawlerRequestsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeCrawlerRequestsResponse().from_map(
            self.do_rpcrequest('DescribeCrawlerRequests', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_crawler_requests_with_options_async(
        self,
        request: avds_20171129_models.DescribeCrawlerRequestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeCrawlerRequestsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeCrawlerRequestsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCrawlerRequests', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_crawler_requests(
        self,
        request: avds_20171129_models.DescribeCrawlerRequestsRequest,
    ) -> avds_20171129_models.DescribeCrawlerRequestsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_crawler_requests_with_options(request, runtime)

    async def describe_crawler_requests_async(
        self,
        request: avds_20171129_models.DescribeCrawlerRequestsRequest,
    ) -> avds_20171129_models.DescribeCrawlerRequestsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_crawler_requests_with_options_async(request, runtime)

    def describe_dnsmap_with_options(
        self,
        request: avds_20171129_models.DescribeDNSMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeDNSMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeDNSMapResponse().from_map(
            self.do_rpcrequest('DescribeDNSMap', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dnsmap_with_options_async(
        self,
        request: avds_20171129_models.DescribeDNSMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeDNSMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeDNSMapResponse().from_map(
            await self.do_rpcrequest_async('DescribeDNSMap', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dnsmap(
        self,
        request: avds_20171129_models.DescribeDNSMapRequest,
    ) -> avds_20171129_models.DescribeDNSMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dnsmap_with_options(request, runtime)

    async def describe_dnsmap_async(
        self,
        request: avds_20171129_models.DescribeDNSMapRequest,
    ) -> avds_20171129_models.DescribeDNSMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dnsmap_with_options_async(request, runtime)

    def describe_domain_attack_surfaces_facets_with_options(
        self,
        request: avds_20171129_models.DescribeDomainAttackSurfacesFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeDomainAttackSurfacesFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeDomainAttackSurfacesFacetsResponse().from_map(
            self.do_rpcrequest('DescribeDomainAttackSurfacesFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domain_attack_surfaces_facets_with_options_async(
        self,
        request: avds_20171129_models.DescribeDomainAttackSurfacesFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeDomainAttackSurfacesFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeDomainAttackSurfacesFacetsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomainAttackSurfacesFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_attack_surfaces_facets(
        self,
        request: avds_20171129_models.DescribeDomainAttackSurfacesFacetsRequest,
    ) -> avds_20171129_models.DescribeDomainAttackSurfacesFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_attack_surfaces_facets_with_options(request, runtime)

    async def describe_domain_attack_surfaces_facets_async(
        self,
        request: avds_20171129_models.DescribeDomainAttackSurfacesFacetsRequest,
    ) -> avds_20171129_models.DescribeDomainAttackSurfacesFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_attack_surfaces_facets_with_options_async(request, runtime)

    def describe_domains_with_options(
        self,
        request: avds_20171129_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeDomainsResponse().from_map(
            self.do_rpcrequest('DescribeDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_domains_with_options_async(
        self,
        request: avds_20171129_models.DescribeDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domains(
        self,
        request: avds_20171129_models.DescribeDomainsRequest,
    ) -> avds_20171129_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_domains_with_options(request, runtime)

    async def describe_domains_async(
        self,
        request: avds_20171129_models.DescribeDomainsRequest,
    ) -> avds_20171129_models.DescribeDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_domains_with_options_async(request, runtime)

    def describe_host_attack_surfaces_facets_with_options(
        self,
        request: avds_20171129_models.DescribeHostAttackSurfacesFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeHostAttackSurfacesFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeHostAttackSurfacesFacetsResponse().from_map(
            self.do_rpcrequest('DescribeHostAttackSurfacesFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_host_attack_surfaces_facets_with_options_async(
        self,
        request: avds_20171129_models.DescribeHostAttackSurfacesFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeHostAttackSurfacesFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeHostAttackSurfacesFacetsResponse().from_map(
            await self.do_rpcrequest_async('DescribeHostAttackSurfacesFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_attack_surfaces_facets(
        self,
        request: avds_20171129_models.DescribeHostAttackSurfacesFacetsRequest,
    ) -> avds_20171129_models.DescribeHostAttackSurfacesFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_host_attack_surfaces_facets_with_options(request, runtime)

    async def describe_host_attack_surfaces_facets_async(
        self,
        request: avds_20171129_models.DescribeHostAttackSurfacesFacetsRequest,
    ) -> avds_20171129_models.DescribeHostAttackSurfacesFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_attack_surfaces_facets_with_options_async(request, runtime)

    def describe_hosts_with_options(
        self,
        request: avds_20171129_models.DescribeHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeHostsResponse().from_map(
            self.do_rpcrequest('DescribeHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hosts_with_options_async(
        self,
        request: avds_20171129_models.DescribeHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeHostsResponse().from_map(
            await self.do_rpcrequest_async('DescribeHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hosts(
        self,
        request: avds_20171129_models.DescribeHostsRequest,
    ) -> avds_20171129_models.DescribeHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hosts_with_options(request, runtime)

    async def describe_hosts_async(
        self,
        request: avds_20171129_models.DescribeHostsRequest,
    ) -> avds_20171129_models.DescribeHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hosts_with_options_async(request, runtime)

    def describe_list_sessions_with_options(
        self,
        request: avds_20171129_models.DescribeListSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeListSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeListSessionsResponse().from_map(
            self.do_rpcrequest('DescribeListSessions', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_list_sessions_with_options_async(
        self,
        request: avds_20171129_models.DescribeListSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeListSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeListSessionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeListSessions', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_list_sessions(
        self,
        request: avds_20171129_models.DescribeListSessionsRequest,
    ) -> avds_20171129_models.DescribeListSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_list_sessions_with_options(request, runtime)

    async def describe_list_sessions_async(
        self,
        request: avds_20171129_models.DescribeListSessionsRequest,
    ) -> avds_20171129_models.DescribeListSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_list_sessions_with_options_async(request, runtime)

    def describe_org_attack_surface_details_with_options(
        self,
        request: avds_20171129_models.DescribeOrgAttackSurfaceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeOrgAttackSurfaceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeOrgAttackSurfaceDetailsResponse().from_map(
            self.do_rpcrequest('DescribeOrgAttackSurfaceDetails', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_org_attack_surface_details_with_options_async(
        self,
        request: avds_20171129_models.DescribeOrgAttackSurfaceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeOrgAttackSurfaceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeOrgAttackSurfaceDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeOrgAttackSurfaceDetails', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_org_attack_surface_details(
        self,
        request: avds_20171129_models.DescribeOrgAttackSurfaceDetailsRequest,
    ) -> avds_20171129_models.DescribeOrgAttackSurfaceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_org_attack_surface_details_with_options(request, runtime)

    async def describe_org_attack_surface_details_async(
        self,
        request: avds_20171129_models.DescribeOrgAttackSurfaceDetailsRequest,
    ) -> avds_20171129_models.DescribeOrgAttackSurfaceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_org_attack_surface_details_with_options_async(request, runtime)

    def describe_org_info_with_options(
        self,
        request: avds_20171129_models.DescribeOrgInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeOrgInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeOrgInfoResponse().from_map(
            self.do_rpcrequest('DescribeOrgInfo', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_org_info_with_options_async(
        self,
        request: avds_20171129_models.DescribeOrgInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeOrgInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeOrgInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeOrgInfo', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_org_info(
        self,
        request: avds_20171129_models.DescribeOrgInfoRequest,
    ) -> avds_20171129_models.DescribeOrgInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_org_info_with_options(request, runtime)

    async def describe_org_info_async(
        self,
        request: avds_20171129_models.DescribeOrgInfoRequest,
    ) -> avds_20171129_models.DescribeOrgInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_org_info_with_options_async(request, runtime)

    def describe_ports_with_options(
        self,
        request: avds_20171129_models.DescribePortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribePortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribePortsResponse().from_map(
            self.do_rpcrequest('DescribePorts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ports_with_options_async(
        self,
        request: avds_20171129_models.DescribePortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribePortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribePortsResponse().from_map(
            await self.do_rpcrequest_async('DescribePorts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ports(
        self,
        request: avds_20171129_models.DescribePortsRequest,
    ) -> avds_20171129_models.DescribePortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ports_with_options(request, runtime)

    async def describe_ports_async(
        self,
        request: avds_20171129_models.DescribePortsRequest,
    ) -> avds_20171129_models.DescribePortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ports_with_options_async(request, runtime)

    def describe_scan_sessions_with_options(
        self,
        request: avds_20171129_models.DescribeScanSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeScanSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeScanSessionsResponse().from_map(
            self.do_rpcrequest('DescribeScanSessions', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scan_sessions_with_options_async(
        self,
        request: avds_20171129_models.DescribeScanSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeScanSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeScanSessionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeScanSessions', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scan_sessions(
        self,
        request: avds_20171129_models.DescribeScanSessionsRequest,
    ) -> avds_20171129_models.DescribeScanSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_sessions_with_options(request, runtime)

    async def describe_scan_sessions_async(
        self,
        request: avds_20171129_models.DescribeScanSessionsRequest,
    ) -> avds_20171129_models.DescribeScanSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scan_sessions_with_options_async(request, runtime)

    def describe_session_with_options(
        self,
        request: avds_20171129_models.DescribeSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeSessionResponse().from_map(
            self.do_rpcrequest('DescribeSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_session_with_options_async(
        self,
        request: avds_20171129_models.DescribeSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeSessionResponse().from_map(
            await self.do_rpcrequest_async('DescribeSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_session(
        self,
        request: avds_20171129_models.DescribeSessionRequest,
    ) -> avds_20171129_models.DescribeSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_session_with_options(request, runtime)

    async def describe_session_async(
        self,
        request: avds_20171129_models.DescribeSessionRequest,
    ) -> avds_20171129_models.DescribeSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_session_with_options_async(request, runtime)

    def describe_subdomains_with_options(
        self,
        request: avds_20171129_models.DescribeSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeSubdomainsResponse().from_map(
            self.do_rpcrequest('DescribeSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_subdomains_with_options_async(
        self,
        request: avds_20171129_models.DescribeSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeSubdomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_subdomains(
        self,
        request: avds_20171129_models.DescribeSubdomainsRequest,
    ) -> avds_20171129_models.DescribeSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subdomains_with_options(request, runtime)

    async def describe_subdomains_async(
        self,
        request: avds_20171129_models.DescribeSubdomainsRequest,
    ) -> avds_20171129_models.DescribeSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subdomains_with_options_async(request, runtime)

    def describe_task_brief_info_with_options(
        self,
        request: avds_20171129_models.DescribeTaskBriefInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeTaskBriefInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeTaskBriefInfoResponse().from_map(
            self.do_rpcrequest('DescribeTaskBriefInfo', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_task_brief_info_with_options_async(
        self,
        request: avds_20171129_models.DescribeTaskBriefInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeTaskBriefInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeTaskBriefInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeTaskBriefInfo', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_task_brief_info(
        self,
        request: avds_20171129_models.DescribeTaskBriefInfoRequest,
    ) -> avds_20171129_models.DescribeTaskBriefInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_task_brief_info_with_options(request, runtime)

    async def describe_task_brief_info_async(
        self,
        request: avds_20171129_models.DescribeTaskBriefInfoRequest,
    ) -> avds_20171129_models.DescribeTaskBriefInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_brief_info_with_options_async(request, runtime)

    def describe_user_tags_with_options(
        self,
        request: avds_20171129_models.DescribeUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeUserTagsResponse().from_map(
            self.do_rpcrequest('DescribeUserTags', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_tags_with_options_async(
        self,
        request: avds_20171129_models.DescribeUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeUserTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserTags', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_tags(
        self,
        request: avds_20171129_models.DescribeUserTagsRequest,
    ) -> avds_20171129_models.DescribeUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_tags_with_options(request, runtime)

    async def describe_user_tags_async(
        self,
        request: avds_20171129_models.DescribeUserTagsRequest,
    ) -> avds_20171129_models.DescribeUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_tags_with_options_async(request, runtime)

    def describe_vulnerability_with_options(
        self,
        request: avds_20171129_models.DescribeVulnerabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeVulnerabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeVulnerabilityResponse().from_map(
            self.do_rpcrequest('DescribeVulnerability', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vulnerability_with_options_async(
        self,
        request: avds_20171129_models.DescribeVulnerabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeVulnerabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeVulnerabilityResponse().from_map(
            await self.do_rpcrequest_async('DescribeVulnerability', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vulnerability(
        self,
        request: avds_20171129_models.DescribeVulnerabilityRequest,
    ) -> avds_20171129_models.DescribeVulnerabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vulnerability_with_options(request, runtime)

    async def describe_vulnerability_async(
        self,
        request: avds_20171129_models.DescribeVulnerabilityRequest,
    ) -> avds_20171129_models.DescribeVulnerabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vulnerability_with_options_async(request, runtime)

    def describe_web_paths_with_options(
        self,
        request: avds_20171129_models.DescribeWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeWebPathsResponse().from_map(
            self.do_rpcrequest('DescribeWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_paths_with_options_async(
        self,
        request: avds_20171129_models.DescribeWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeWebPathsResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_paths(
        self,
        request: avds_20171129_models.DescribeWebPathsRequest,
    ) -> avds_20171129_models.DescribeWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_paths_with_options(request, runtime)

    async def describe_web_paths_async(
        self,
        request: avds_20171129_models.DescribeWebPathsRequest,
    ) -> avds_20171129_models.DescribeWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_paths_with_options_async(request, runtime)

    def describe_web_servers_with_options(
        self,
        request: avds_20171129_models.DescribeWebServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeWebServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeWebServersResponse().from_map(
            self.do_rpcrequest('DescribeWebServers', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_servers_with_options_async(
        self,
        request: avds_20171129_models.DescribeWebServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeWebServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeWebServersResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebServers', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_servers(
        self,
        request: avds_20171129_models.DescribeWebServersRequest,
    ) -> avds_20171129_models.DescribeWebServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_servers_with_options(request, runtime)

    async def describe_web_servers_async(
        self,
        request: avds_20171129_models.DescribeWebServersRequest,
    ) -> avds_20171129_models.DescribeWebServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_servers_with_options_async(request, runtime)

    def describe_web_techs_with_options(
        self,
        request: avds_20171129_models.DescribeWebTechsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeWebTechsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeWebTechsResponse().from_map(
            self.do_rpcrequest('DescribeWebTechs', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_web_techs_with_options_async(
        self,
        request: avds_20171129_models.DescribeWebTechsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.DescribeWebTechsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.DescribeWebTechsResponse().from_map(
            await self.do_rpcrequest_async('DescribeWebTechs', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_web_techs(
        self,
        request: avds_20171129_models.DescribeWebTechsRequest,
    ) -> avds_20171129_models.DescribeWebTechsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_techs_with_options(request, runtime)

    async def describe_web_techs_async(
        self,
        request: avds_20171129_models.DescribeWebTechsRequest,
    ) -> avds_20171129_models.DescribeWebTechsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_techs_with_options_async(request, runtime)

    def edit_session_with_options(
        self,
        request: avds_20171129_models.EditSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.EditSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.EditSessionResponse().from_map(
            self.do_rpcrequest('EditSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_session_with_options_async(
        self,
        request: avds_20171129_models.EditSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.EditSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.EditSessionResponse().from_map(
            await self.do_rpcrequest_async('EditSession', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_session(
        self,
        request: avds_20171129_models.EditSessionRequest,
    ) -> avds_20171129_models.EditSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_session_with_options(request, runtime)

    async def edit_session_async(
        self,
        request: avds_20171129_models.EditSessionRequest,
    ) -> avds_20171129_models.EditSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_session_with_options_async(request, runtime)

    def generate_vul_report_with_options(
        self,
        request: avds_20171129_models.GenerateVulReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.GenerateVulReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.GenerateVulReportResponse().from_map(
            self.do_rpcrequest('GenerateVulReport', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_vul_report_with_options_async(
        self,
        request: avds_20171129_models.GenerateVulReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.GenerateVulReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.GenerateVulReportResponse().from_map(
            await self.do_rpcrequest_async('GenerateVulReport', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_vul_report(
        self,
        request: avds_20171129_models.GenerateVulReportRequest,
    ) -> avds_20171129_models.GenerateVulReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_vul_report_with_options(request, runtime)

    async def generate_vul_report_async(
        self,
        request: avds_20171129_models.GenerateVulReportRequest,
    ) -> avds_20171129_models.GenerateVulReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_vul_report_with_options_async(request, runtime)

    def list_org_dnsmap_with_options(
        self,
        request: avds_20171129_models.ListOrgDNSMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgDNSMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgDNSMapResponse().from_map(
            self.do_rpcrequest('ListOrgDNSMap', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_dnsmap_with_options_async(
        self,
        request: avds_20171129_models.ListOrgDNSMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgDNSMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgDNSMapResponse().from_map(
            await self.do_rpcrequest_async('ListOrgDNSMap', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_dnsmap(
        self,
        request: avds_20171129_models.ListOrgDNSMapRequest,
    ) -> avds_20171129_models.ListOrgDNSMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_dnsmap_with_options(request, runtime)

    async def list_org_dnsmap_async(
        self,
        request: avds_20171129_models.ListOrgDNSMapRequest,
    ) -> avds_20171129_models.ListOrgDNSMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_dnsmap_with_options_async(request, runtime)

    def list_org_domains_with_options(
        self,
        request: avds_20171129_models.ListOrgDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgDomainsResponse().from_map(
            self.do_rpcrequest('ListOrgDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_domains_with_options_async(
        self,
        request: avds_20171129_models.ListOrgDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgDomainsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_domains(
        self,
        request: avds_20171129_models.ListOrgDomainsRequest,
    ) -> avds_20171129_models.ListOrgDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_domains_with_options(request, runtime)

    async def list_org_domains_async(
        self,
        request: avds_20171129_models.ListOrgDomainsRequest,
    ) -> avds_20171129_models.ListOrgDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_domains_with_options_async(request, runtime)

    def list_org_hosts_with_options(
        self,
        request: avds_20171129_models.ListOrgHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgHostsResponse().from_map(
            self.do_rpcrequest('ListOrgHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_hosts_with_options_async(
        self,
        request: avds_20171129_models.ListOrgHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgHostsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_hosts(
        self,
        request: avds_20171129_models.ListOrgHostsRequest,
    ) -> avds_20171129_models.ListOrgHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_hosts_with_options(request, runtime)

    async def list_org_hosts_async(
        self,
        request: avds_20171129_models.ListOrgHostsRequest,
    ) -> avds_20171129_models.ListOrgHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_hosts_with_options_async(request, runtime)

    def list_org_ports_with_options(
        self,
        request: avds_20171129_models.ListOrgPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgPortsResponse().from_map(
            self.do_rpcrequest('ListOrgPorts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_ports_with_options_async(
        self,
        request: avds_20171129_models.ListOrgPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgPortsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgPorts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_ports(
        self,
        request: avds_20171129_models.ListOrgPortsRequest,
    ) -> avds_20171129_models.ListOrgPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_ports_with_options(request, runtime)

    async def list_org_ports_async(
        self,
        request: avds_20171129_models.ListOrgPortsRequest,
    ) -> avds_20171129_models.ListOrgPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_ports_with_options_async(request, runtime)

    def list_org_risky_assets_with_options(
        self,
        request: avds_20171129_models.ListOrgRiskyAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgRiskyAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgRiskyAssetsResponse().from_map(
            self.do_rpcrequest('ListOrgRiskyAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_risky_assets_with_options_async(
        self,
        request: avds_20171129_models.ListOrgRiskyAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgRiskyAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgRiskyAssetsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgRiskyAssets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_risky_assets(
        self,
        request: avds_20171129_models.ListOrgRiskyAssetsRequest,
    ) -> avds_20171129_models.ListOrgRiskyAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_risky_assets_with_options(request, runtime)

    async def list_org_risky_assets_async(
        self,
        request: avds_20171129_models.ListOrgRiskyAssetsRequest,
    ) -> avds_20171129_models.ListOrgRiskyAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_risky_assets_with_options_async(request, runtime)

    def list_org_subdomains_with_options(
        self,
        request: avds_20171129_models.ListOrgSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgSubdomainsResponse().from_map(
            self.do_rpcrequest('ListOrgSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_subdomains_with_options_async(
        self,
        request: avds_20171129_models.ListOrgSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgSubdomainsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_subdomains(
        self,
        request: avds_20171129_models.ListOrgSubdomainsRequest,
    ) -> avds_20171129_models.ListOrgSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_subdomains_with_options(request, runtime)

    async def list_org_subdomains_async(
        self,
        request: avds_20171129_models.ListOrgSubdomainsRequest,
    ) -> avds_20171129_models.ListOrgSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_subdomains_with_options_async(request, runtime)

    def list_org_vul_facets_with_options(
        self,
        request: avds_20171129_models.ListOrgVulFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgVulFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgVulFacetsResponse().from_map(
            self.do_rpcrequest('ListOrgVulFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_vul_facets_with_options_async(
        self,
        request: avds_20171129_models.ListOrgVulFacetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgVulFacetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgVulFacetsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgVulFacets', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_vul_facets(
        self,
        request: avds_20171129_models.ListOrgVulFacetsRequest,
    ) -> avds_20171129_models.ListOrgVulFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_vul_facets_with_options(request, runtime)

    async def list_org_vul_facets_async(
        self,
        request: avds_20171129_models.ListOrgVulFacetsRequest,
    ) -> avds_20171129_models.ListOrgVulFacetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_vul_facets_with_options_async(request, runtime)

    def list_org_web_paths_with_options(
        self,
        request: avds_20171129_models.ListOrgWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgWebPathsResponse().from_map(
            self.do_rpcrequest('ListOrgWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_web_paths_with_options_async(
        self,
        request: avds_20171129_models.ListOrgWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgWebPathsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_web_paths(
        self,
        request: avds_20171129_models.ListOrgWebPathsRequest,
    ) -> avds_20171129_models.ListOrgWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_web_paths_with_options(request, runtime)

    async def list_org_web_paths_async(
        self,
        request: avds_20171129_models.ListOrgWebPathsRequest,
    ) -> avds_20171129_models.ListOrgWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_web_paths_with_options_async(request, runtime)

    def list_org_web_techs_with_options(
        self,
        request: avds_20171129_models.ListOrgWebTechsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgWebTechsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgWebTechsResponse().from_map(
            self.do_rpcrequest('ListOrgWebTechs', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_org_web_techs_with_options_async(
        self,
        request: avds_20171129_models.ListOrgWebTechsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListOrgWebTechsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListOrgWebTechsResponse().from_map(
            await self.do_rpcrequest_async('ListOrgWebTechs', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_org_web_techs(
        self,
        request: avds_20171129_models.ListOrgWebTechsRequest,
    ) -> avds_20171129_models.ListOrgWebTechsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_org_web_techs_with_options(request, runtime)

    async def list_org_web_techs_async(
        self,
        request: avds_20171129_models.ListOrgWebTechsRequest,
    ) -> avds_20171129_models.ListOrgWebTechsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_org_web_techs_with_options_async(request, runtime)

    def list_user_dnsmap_with_options(
        self,
        request: avds_20171129_models.ListUserDNSMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserDNSMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserDNSMapResponse().from_map(
            self.do_rpcrequest('ListUserDNSMap', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_dnsmap_with_options_async(
        self,
        request: avds_20171129_models.ListUserDNSMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserDNSMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserDNSMapResponse().from_map(
            await self.do_rpcrequest_async('ListUserDNSMap', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_dnsmap(
        self,
        request: avds_20171129_models.ListUserDNSMapRequest,
    ) -> avds_20171129_models.ListUserDNSMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_dnsmap_with_options(request, runtime)

    async def list_user_dnsmap_async(
        self,
        request: avds_20171129_models.ListUserDNSMapRequest,
    ) -> avds_20171129_models.ListUserDNSMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_dnsmap_with_options_async(request, runtime)

    def list_user_dnsmap_histories_with_options(
        self,
        request: avds_20171129_models.ListUserDNSMapHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserDNSMapHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserDNSMapHistoriesResponse().from_map(
            self.do_rpcrequest('ListUserDNSMapHistories', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_dnsmap_histories_with_options_async(
        self,
        request: avds_20171129_models.ListUserDNSMapHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserDNSMapHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserDNSMapHistoriesResponse().from_map(
            await self.do_rpcrequest_async('ListUserDNSMapHistories', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_dnsmap_histories(
        self,
        request: avds_20171129_models.ListUserDNSMapHistoriesRequest,
    ) -> avds_20171129_models.ListUserDNSMapHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_dnsmap_histories_with_options(request, runtime)

    async def list_user_dnsmap_histories_async(
        self,
        request: avds_20171129_models.ListUserDNSMapHistoriesRequest,
    ) -> avds_20171129_models.ListUserDNSMapHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_dnsmap_histories_with_options_async(request, runtime)

    def list_user_domains_with_options(
        self,
        request: avds_20171129_models.ListUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserDomainsResponse().from_map(
            self.do_rpcrequest('ListUserDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_domains_with_options_async(
        self,
        request: avds_20171129_models.ListUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserDomainsResponse().from_map(
            await self.do_rpcrequest_async('ListUserDomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_domains(
        self,
        request: avds_20171129_models.ListUserDomainsRequest,
    ) -> avds_20171129_models.ListUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_domains_with_options(request, runtime)

    async def list_user_domains_async(
        self,
        request: avds_20171129_models.ListUserDomainsRequest,
    ) -> avds_20171129_models.ListUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_domains_with_options_async(request, runtime)

    def list_user_hosts_with_options(
        self,
        request: avds_20171129_models.ListUserHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserHostsResponse().from_map(
            self.do_rpcrequest('ListUserHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_hosts_with_options_async(
        self,
        request: avds_20171129_models.ListUserHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserHostsResponse().from_map(
            await self.do_rpcrequest_async('ListUserHosts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_hosts(
        self,
        request: avds_20171129_models.ListUserHostsRequest,
    ) -> avds_20171129_models.ListUserHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_hosts_with_options(request, runtime)

    async def list_user_hosts_async(
        self,
        request: avds_20171129_models.ListUserHostsRequest,
    ) -> avds_20171129_models.ListUserHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_hosts_with_options_async(request, runtime)

    def list_user_organizations_with_options(
        self,
        request: avds_20171129_models.ListUserOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserOrganizationsResponse().from_map(
            self.do_rpcrequest('ListUserOrganizations', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_organizations_with_options_async(
        self,
        request: avds_20171129_models.ListUserOrganizationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserOrganizationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserOrganizationsResponse().from_map(
            await self.do_rpcrequest_async('ListUserOrganizations', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_organizations(
        self,
        request: avds_20171129_models.ListUserOrganizationsRequest,
    ) -> avds_20171129_models.ListUserOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_organizations_with_options(request, runtime)

    async def list_user_organizations_async(
        self,
        request: avds_20171129_models.ListUserOrganizationsRequest,
    ) -> avds_20171129_models.ListUserOrganizationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_organizations_with_options_async(request, runtime)

    def list_user_ports_with_options(
        self,
        request: avds_20171129_models.ListUserPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserPortsResponse().from_map(
            self.do_rpcrequest('ListUserPorts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_ports_with_options_async(
        self,
        request: avds_20171129_models.ListUserPortsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserPortsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserPortsResponse().from_map(
            await self.do_rpcrequest_async('ListUserPorts', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_ports(
        self,
        request: avds_20171129_models.ListUserPortsRequest,
    ) -> avds_20171129_models.ListUserPortsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_ports_with_options(request, runtime)

    async def list_user_ports_async(
        self,
        request: avds_20171129_models.ListUserPortsRequest,
    ) -> avds_20171129_models.ListUserPortsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_ports_with_options_async(request, runtime)

    def list_user_subdomains_with_options(
        self,
        request: avds_20171129_models.ListUserSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserSubdomainsResponse().from_map(
            self.do_rpcrequest('ListUserSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_subdomains_with_options_async(
        self,
        request: avds_20171129_models.ListUserSubdomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserSubdomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserSubdomainsResponse().from_map(
            await self.do_rpcrequest_async('ListUserSubdomains', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_subdomains(
        self,
        request: avds_20171129_models.ListUserSubdomainsRequest,
    ) -> avds_20171129_models.ListUserSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_subdomains_with_options(request, runtime)

    async def list_user_subdomains_async(
        self,
        request: avds_20171129_models.ListUserSubdomainsRequest,
    ) -> avds_20171129_models.ListUserSubdomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_subdomains_with_options_async(request, runtime)

    def list_user_web_paths_with_options(
        self,
        request: avds_20171129_models.ListUserWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserWebPathsResponse().from_map(
            self.do_rpcrequest('ListUserWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_web_paths_with_options_async(
        self,
        request: avds_20171129_models.ListUserWebPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserWebPathsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserWebPathsResponse().from_map(
            await self.do_rpcrequest_async('ListUserWebPaths', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_web_paths(
        self,
        request: avds_20171129_models.ListUserWebPathsRequest,
    ) -> avds_20171129_models.ListUserWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_web_paths_with_options(request, runtime)

    async def list_user_web_paths_async(
        self,
        request: avds_20171129_models.ListUserWebPathsRequest,
    ) -> avds_20171129_models.ListUserWebPathsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_web_paths_with_options_async(request, runtime)

    def list_user_web_techs_with_options(
        self,
        request: avds_20171129_models.ListUserWebTechsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserWebTechsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserWebTechsResponse().from_map(
            self.do_rpcrequest('ListUserWebTechs', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_web_techs_with_options_async(
        self,
        request: avds_20171129_models.ListUserWebTechsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ListUserWebTechsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ListUserWebTechsResponse().from_map(
            await self.do_rpcrequest_async('ListUserWebTechs', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_web_techs(
        self,
        request: avds_20171129_models.ListUserWebTechsRequest,
    ) -> avds_20171129_models.ListUserWebTechsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_web_techs_with_options(request, runtime)

    async def list_user_web_techs_async(
        self,
        request: avds_20171129_models.ListUserWebTechsRequest,
    ) -> avds_20171129_models.ListUserWebTechsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_web_techs_with_options_async(request, runtime)

    def modify_organization_with_options(
        self,
        request: avds_20171129_models.ModifyOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ModifyOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ModifyOrganizationResponse().from_map(
            self.do_rpcrequest('ModifyOrganization', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_organization_with_options_async(
        self,
        request: avds_20171129_models.ModifyOrganizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.ModifyOrganizationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.ModifyOrganizationResponse().from_map(
            await self.do_rpcrequest_async('ModifyOrganization', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_organization(
        self,
        request: avds_20171129_models.ModifyOrganizationRequest,
    ) -> avds_20171129_models.ModifyOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_organization_with_options(request, runtime)

    async def modify_organization_async(
        self,
        request: avds_20171129_models.ModifyOrganizationRequest,
    ) -> avds_20171129_models.ModifyOrganizationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_organization_with_options_async(request, runtime)

    def tag_assets_by_records_with_options(
        self,
        request: avds_20171129_models.TagAssetsByRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.TagAssetsByRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.TagAssetsByRecordsResponse().from_map(
            self.do_rpcrequest('TagAssetsByRecords', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_assets_by_records_with_options_async(
        self,
        request: avds_20171129_models.TagAssetsByRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.TagAssetsByRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.TagAssetsByRecordsResponse().from_map(
            await self.do_rpcrequest_async('TagAssetsByRecords', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_assets_by_records(
        self,
        request: avds_20171129_models.TagAssetsByRecordsRequest,
    ) -> avds_20171129_models.TagAssetsByRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_assets_by_records_with_options(request, runtime)

    async def tag_assets_by_records_async(
        self,
        request: avds_20171129_models.TagAssetsByRecordsRequest,
    ) -> avds_20171129_models.TagAssetsByRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_assets_by_records_with_options_async(request, runtime)

    def tag_assets_by_search_with_options(
        self,
        request: avds_20171129_models.TagAssetsBySearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.TagAssetsBySearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.TagAssetsBySearchResponse().from_map(
            self.do_rpcrequest('TagAssetsBySearch', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_assets_by_search_with_options_async(
        self,
        request: avds_20171129_models.TagAssetsBySearchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avds_20171129_models.TagAssetsBySearchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return avds_20171129_models.TagAssetsBySearchResponse().from_map(
            await self.do_rpcrequest_async('TagAssetsBySearch', '2017-11-29', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_assets_by_search(
        self,
        request: avds_20171129_models.TagAssetsBySearchRequest,
    ) -> avds_20171129_models.TagAssetsBySearchResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_assets_by_search_with_options(request, runtime)

    async def tag_assets_by_search_async(
        self,
        request: avds_20171129_models.TagAssetsBySearchRequest,
    ) -> avds_20171129_models.TagAssetsBySearchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_assets_by_search_with_options_async(request, runtime)
