# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cbn20170912 import models as cbn_20170912_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cbn', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_flow_log_with_options(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ActiveFlowLogResponse(),
            self.do_rpcrequest('ActiveFlowLog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def active_flow_log_with_options_async(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ActiveFlowLogResponse(),
            await self.do_rpcrequest_async('ActiveFlowLog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def active_flow_log(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    async def active_flow_log_async(
        self,
        request: cbn_20170912_models.ActiveFlowLogRequest,
    ) -> cbn_20170912_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_flow_log_with_options_async(request, runtime)

    def associate_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateCenBandwidthPackageResponse(),
            self.do_rpcrequest('AssociateCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.AssociateCenBandwidthPackageResponse(),
            await self.do_rpcrequest_async('AssociateCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_cen_bandwidth_package_with_options(request, runtime)

    async def associate_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.AssociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.AssociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_cen_bandwidth_package_with_options_async(request, runtime)

    def attach_cen_child_instance_with_options(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.AttachCenChildInstanceResponse(),
            self.do_rpcrequest('AttachCenChildInstance', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_cen_child_instance_with_options_async(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.AttachCenChildInstanceResponse(),
            await self.do_rpcrequest_async('AttachCenChildInstance', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_cen_child_instance(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_child_instance_with_options(request, runtime)

    async def attach_cen_child_instance_async(
        self,
        request: cbn_20170912_models.AttachCenChildInstanceRequest,
    ) -> cbn_20170912_models.AttachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_cen_child_instance_with_options_async(request, runtime)

    def create_cen_with_options(
        self,
        request: cbn_20170912_models.CreateCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenResponse(),
            self.do_rpcrequest('CreateCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cen_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenResponse(),
            await self.do_rpcrequest_async('CreateCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cen(
        self,
        request: cbn_20170912_models.CreateCenRequest,
    ) -> cbn_20170912_models.CreateCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_with_options(request, runtime)

    async def create_cen_async(
        self,
        request: cbn_20170912_models.CreateCenRequest,
    ) -> cbn_20170912_models.CreateCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_with_options_async(request, runtime)

    def create_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenBandwidthPackageResponse(),
            self.do_rpcrequest('CreateCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenBandwidthPackageResponse(),
            await self.do_rpcrequest_async('CreateCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_bandwidth_package_with_options(request, runtime)

    async def create_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.CreateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.CreateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_bandwidth_package_with_options_async(request, runtime)

    def create_cen_child_instance_route_entry_to_cen_with_options(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse(),
            self.do_rpcrequest('CreateCenChildInstanceRouteEntryToCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cen_child_instance_route_entry_to_cen_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse(),
            await self.do_rpcrequest_async('CreateCenChildInstanceRouteEntryToCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cen_child_instance_route_entry_to_cen(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    async def create_cen_child_instance_route_entry_to_cen_async(
        self,
        request: cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.CreateCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_child_instance_route_entry_to_cen_with_options_async(request, runtime)

    def create_cen_route_map_with_options(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenRouteMapResponse(),
            self.do_rpcrequest('CreateCenRouteMap', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cen_route_map_with_options_async(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateCenRouteMapResponse(),
            await self.do_rpcrequest_async('CreateCenRouteMap', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cen_route_map(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cen_route_map_with_options(request, runtime)

    async def create_cen_route_map_async(
        self,
        request: cbn_20170912_models.CreateCenRouteMapRequest,
    ) -> cbn_20170912_models.CreateCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cen_route_map_with_options_async(request, runtime)

    def create_flowlog_with_options(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateFlowlogResponse(),
            self.do_rpcrequest('CreateFlowlog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flowlog_with_options_async(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.CreateFlowlogResponse(),
            await self.do_rpcrequest_async('CreateFlowlog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flowlog(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flowlog_with_options(request, runtime)

    async def create_flowlog_async(
        self,
        request: cbn_20170912_models.CreateFlowlogRequest,
    ) -> cbn_20170912_models.CreateFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flowlog_with_options_async(request, runtime)

    def deactive_flow_log_with_options(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeactiveFlowLogResponse(),
            self.do_rpcrequest('DeactiveFlowLog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactive_flow_log_with_options_async(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeactiveFlowLogResponse(),
            await self.do_rpcrequest_async('DeactiveFlowLog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactive_flow_log(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    async def deactive_flow_log_async(
        self,
        request: cbn_20170912_models.DeactiveFlowLogRequest,
    ) -> cbn_20170912_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactive_flow_log_with_options_async(request, runtime)

    def delete_cen_with_options(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenResponse(),
            self.do_rpcrequest('DeleteCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cen_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenResponse(),
            await self.do_rpcrequest_async('DeleteCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cen(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
    ) -> cbn_20170912_models.DeleteCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_with_options(request, runtime)

    async def delete_cen_async(
        self,
        request: cbn_20170912_models.DeleteCenRequest,
    ) -> cbn_20170912_models.DeleteCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_with_options_async(request, runtime)

    def delete_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenBandwidthPackageResponse(),
            self.do_rpcrequest('DeleteCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenBandwidthPackageResponse(),
            await self.do_rpcrequest_async('DeleteCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_bandwidth_package_with_options(request, runtime)

    async def delete_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.DeleteCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.DeleteCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_bandwidth_package_with_options_async(request, runtime)

    def delete_cen_child_instance_route_entry_to_cen_with_options(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse(),
            self.do_rpcrequest('DeleteCenChildInstanceRouteEntryToCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cen_child_instance_route_entry_to_cen_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse(),
            await self.do_rpcrequest_async('DeleteCenChildInstanceRouteEntryToCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cen_child_instance_route_entry_to_cen(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_child_instance_route_entry_to_cen_with_options(request, runtime)

    async def delete_cen_child_instance_route_entry_to_cen_async(
        self,
        request: cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenRequest,
    ) -> cbn_20170912_models.DeleteCenChildInstanceRouteEntryToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_child_instance_route_entry_to_cen_with_options_async(request, runtime)

    def delete_cen_route_map_with_options(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenRouteMapResponse(),
            self.do_rpcrequest('DeleteCenRouteMap', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cen_route_map_with_options_async(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteCenRouteMapResponse(),
            await self.do_rpcrequest_async('DeleteCenRouteMap', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cen_route_map(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cen_route_map_with_options(request, runtime)

    async def delete_cen_route_map_async(
        self,
        request: cbn_20170912_models.DeleteCenRouteMapRequest,
    ) -> cbn_20170912_models.DeleteCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cen_route_map_with_options_async(request, runtime)

    def delete_flowlog_with_options(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteFlowlogResponse(),
            self.do_rpcrequest('DeleteFlowlog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flowlog_with_options_async(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteFlowlogResponse(),
            await self.do_rpcrequest_async('DeleteFlowlog', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flowlog(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flowlog_with_options(request, runtime)

    async def delete_flowlog_async(
        self,
        request: cbn_20170912_models.DeleteFlowlogRequest,
    ) -> cbn_20170912_models.DeleteFlowlogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flowlog_with_options_async(request, runtime)

    def delete_route_service_in_cen_with_options(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteRouteServiceInCenResponse(),
            self.do_rpcrequest('DeleteRouteServiceInCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_route_service_in_cen_with_options_async(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DeleteRouteServiceInCenResponse(),
            await self.do_rpcrequest_async('DeleteRouteServiceInCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_route_service_in_cen(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_route_service_in_cen_with_options(request, runtime)

    async def delete_route_service_in_cen_async(
        self,
        request: cbn_20170912_models.DeleteRouteServiceInCenRequest,
    ) -> cbn_20170912_models.DeleteRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_service_in_cen_with_options_async(request, runtime)

    def describe_cen_attached_child_instance_attribute_with_options(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeCenAttachedChildInstanceAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_attached_child_instance_attribute_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeCenAttachedChildInstanceAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_attached_child_instance_attribute(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_attached_child_instance_attribute_with_options(request, runtime)

    async def describe_cen_attached_child_instance_attribute_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_attached_child_instance_attribute_with_options_async(request, runtime)

    def describe_cen_attached_child_instances_with_options(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstancesResponse(),
            self.do_rpcrequest('DescribeCenAttachedChildInstances', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_attached_child_instances_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenAttachedChildInstancesResponse(),
            await self.do_rpcrequest_async('DescribeCenAttachedChildInstances', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_attached_child_instances(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_attached_child_instances_with_options(request, runtime)

    async def describe_cen_attached_child_instances_async(
        self,
        request: cbn_20170912_models.DescribeCenAttachedChildInstancesRequest,
    ) -> cbn_20170912_models.DescribeCenAttachedChildInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_attached_child_instances_with_options_async(request, runtime)

    def describe_cen_bandwidth_packages_with_options(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenBandwidthPackagesResponse(),
            self.do_rpcrequest('DescribeCenBandwidthPackages', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_bandwidth_packages_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenBandwidthPackagesResponse(),
            await self.do_rpcrequest_async('DescribeCenBandwidthPackages', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_bandwidth_packages(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_bandwidth_packages_with_options(request, runtime)

    async def describe_cen_bandwidth_packages_async(
        self,
        request: cbn_20170912_models.DescribeCenBandwidthPackagesRequest,
    ) -> cbn_20170912_models.DescribeCenBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_bandwidth_packages_with_options_async(request, runtime)

    def describe_cen_child_instance_route_entries_with_options(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse(),
            self.do_rpcrequest('DescribeCenChildInstanceRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_child_instance_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse(),
            await self.do_rpcrequest_async('DescribeCenChildInstanceRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_child_instance_route_entries(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_child_instance_route_entries_with_options(request, runtime)

    async def describe_cen_child_instance_route_entries_async(
        self,
        request: cbn_20170912_models.DescribeCenChildInstanceRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenChildInstanceRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_child_instance_route_entries_with_options_async(request, runtime)

    def describe_cen_geographic_span_remaining_bandwidth_with_options(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse(),
            self.do_rpcrequest('DescribeCenGeographicSpanRemainingBandwidth', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_geographic_span_remaining_bandwidth_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse(),
            await self.do_rpcrequest_async('DescribeCenGeographicSpanRemainingBandwidth', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_geographic_span_remaining_bandwidth(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_geographic_span_remaining_bandwidth_with_options(request, runtime)

    async def describe_cen_geographic_span_remaining_bandwidth_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpanRemainingBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_geographic_span_remaining_bandwidth_with_options_async(request, runtime)

    def describe_cen_geographic_spans_with_options(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpansResponse(),
            self.do_rpcrequest('DescribeCenGeographicSpans', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_geographic_spans_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenGeographicSpansResponse(),
            await self.do_rpcrequest_async('DescribeCenGeographicSpans', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_geographic_spans(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_geographic_spans_with_options(request, runtime)

    async def describe_cen_geographic_spans_async(
        self,
        request: cbn_20170912_models.DescribeCenGeographicSpansRequest,
    ) -> cbn_20170912_models.DescribeCenGeographicSpansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_geographic_spans_with_options_async(request, runtime)

    def describe_cen_inter_region_bandwidth_limits_with_options(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse(),
            self.do_rpcrequest('DescribeCenInterRegionBandwidthLimits', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_inter_region_bandwidth_limits_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse(),
            await self.do_rpcrequest_async('DescribeCenInterRegionBandwidthLimits', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_inter_region_bandwidth_limits(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_inter_region_bandwidth_limits_with_options(request, runtime)

    async def describe_cen_inter_region_bandwidth_limits_async(
        self,
        request: cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsRequest,
    ) -> cbn_20170912_models.DescribeCenInterRegionBandwidthLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_inter_region_bandwidth_limits_with_options_async(request, runtime)

    def describe_cen_private_zone_routes_with_options(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse(),
            self.do_rpcrequest('DescribeCenPrivateZoneRoutes', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_private_zone_routes_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse(),
            await self.do_rpcrequest_async('DescribeCenPrivateZoneRoutes', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_private_zone_routes(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_private_zone_routes_with_options(request, runtime)

    async def describe_cen_private_zone_routes_async(
        self,
        request: cbn_20170912_models.DescribeCenPrivateZoneRoutesRequest,
    ) -> cbn_20170912_models.DescribeCenPrivateZoneRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_private_zone_routes_with_options_async(request, runtime)

    def describe_cen_region_domain_route_entries_with_options(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse(),
            self.do_rpcrequest('DescribeCenRegionDomainRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_region_domain_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse(),
            await self.do_rpcrequest_async('DescribeCenRegionDomainRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_region_domain_route_entries(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_region_domain_route_entries_with_options(request, runtime)

    async def describe_cen_region_domain_route_entries_async(
        self,
        request: cbn_20170912_models.DescribeCenRegionDomainRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribeCenRegionDomainRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_region_domain_route_entries_with_options_async(request, runtime)

    def describe_cen_route_maps_with_options(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRouteMapsResponse(),
            self.do_rpcrequest('DescribeCenRouteMaps', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_route_maps_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenRouteMapsResponse(),
            await self.do_rpcrequest_async('DescribeCenRouteMaps', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_route_maps(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_route_maps_with_options(request, runtime)

    async def describe_cen_route_maps_async(
        self,
        request: cbn_20170912_models.DescribeCenRouteMapsRequest,
    ) -> cbn_20170912_models.DescribeCenRouteMapsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_route_maps_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCensResponse(),
            self.do_rpcrequest('DescribeCens', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCensResponse(),
            await self.do_rpcrequest_async('DescribeCens', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cens(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
    ) -> cbn_20170912_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: cbn_20170912_models.DescribeCensRequest,
    ) -> cbn_20170912_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_cen_vbr_health_check_with_options(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenVbrHealthCheckResponse(),
            self.do_rpcrequest('DescribeCenVbrHealthCheck', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cen_vbr_health_check_with_options_async(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeCenVbrHealthCheckResponse(),
            await self.do_rpcrequest_async('DescribeCenVbrHealthCheck', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cen_vbr_health_check(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cen_vbr_health_check_with_options(request, runtime)

    async def describe_cen_vbr_health_check_async(
        self,
        request: cbn_20170912_models.DescribeCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DescribeCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cen_vbr_health_check_with_options_async(request, runtime)

    def describe_child_instance_regions_with_options(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeChildInstanceRegionsResponse(),
            self.do_rpcrequest('DescribeChildInstanceRegions', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_child_instance_regions_with_options_async(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeChildInstanceRegionsResponse(),
            await self.do_rpcrequest_async('DescribeChildInstanceRegions', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_child_instance_regions(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_child_instance_regions_with_options(request, runtime)

    async def describe_child_instance_regions_async(
        self,
        request: cbn_20170912_models.DescribeChildInstanceRegionsRequest,
    ) -> cbn_20170912_models.DescribeChildInstanceRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_child_instance_regions_with_options_async(request, runtime)

    def describe_flowlogs_with_options(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeFlowlogsResponse(),
            self.do_rpcrequest('DescribeFlowlogs', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flowlogs_with_options_async(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeFlowlogsResponse(),
            await self.do_rpcrequest_async('DescribeFlowlogs', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flowlogs(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flowlogs_with_options(request, runtime)

    async def describe_flowlogs_async(
        self,
        request: cbn_20170912_models.DescribeFlowlogsRequest,
    ) -> cbn_20170912_models.DescribeFlowlogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flowlogs_with_options_async(request, runtime)

    def describe_geographic_region_membership_with_options(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGeographicRegionMembershipResponse(),
            self.do_rpcrequest('DescribeGeographicRegionMembership', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_geographic_region_membership_with_options_async(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGeographicRegionMembershipResponse(),
            await self.do_rpcrequest_async('DescribeGeographicRegionMembership', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_geographic_region_membership(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_geographic_region_membership_with_options(request, runtime)

    async def describe_geographic_region_membership_async(
        self,
        request: cbn_20170912_models.DescribeGeographicRegionMembershipRequest,
    ) -> cbn_20170912_models.DescribeGeographicRegionMembershipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_geographic_region_membership_with_options_async(request, runtime)

    def describe_grant_rules_to_cen_with_options(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToCenResponse(),
            self.do_rpcrequest('DescribeGrantRulesToCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grant_rules_to_cen_with_options_async(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeGrantRulesToCenResponse(),
            await self.do_rpcrequest_async('DescribeGrantRulesToCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grant_rules_to_cen(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_rules_to_cen_with_options(request, runtime)

    async def describe_grant_rules_to_cen_async(
        self,
        request: cbn_20170912_models.DescribeGrantRulesToCenRequest,
    ) -> cbn_20170912_models.DescribeGrantRulesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grant_rules_to_cen_with_options_async(request, runtime)

    def describe_published_route_entries_with_options(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribePublishedRouteEntriesResponse(),
            self.do_rpcrequest('DescribePublishedRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_published_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribePublishedRouteEntriesResponse(),
            await self.do_rpcrequest_async('DescribePublishedRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_published_route_entries(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_published_route_entries_with_options(request, runtime)

    async def describe_published_route_entries_async(
        self,
        request: cbn_20170912_models.DescribePublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.DescribePublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_published_route_entries_with_options_async(request, runtime)

    def describe_route_conflict_with_options(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteConflictResponse(),
            self.do_rpcrequest('DescribeRouteConflict', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_route_conflict_with_options_async(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteConflictResponse(),
            await self.do_rpcrequest_async('DescribeRouteConflict', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_conflict(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_conflict_with_options(request, runtime)

    async def describe_route_conflict_async(
        self,
        request: cbn_20170912_models.DescribeRouteConflictRequest,
    ) -> cbn_20170912_models.DescribeRouteConflictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_conflict_with_options_async(request, runtime)

    def describe_route_services_in_cen_with_options(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteServicesInCenResponse(),
            self.do_rpcrequest('DescribeRouteServicesInCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_route_services_in_cen_with_options_async(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DescribeRouteServicesInCenResponse(),
            await self.do_rpcrequest_async('DescribeRouteServicesInCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_services_in_cen(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_services_in_cen_with_options(request, runtime)

    async def describe_route_services_in_cen_async(
        self,
        request: cbn_20170912_models.DescribeRouteServicesInCenRequest,
    ) -> cbn_20170912_models.DescribeRouteServicesInCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_services_in_cen_with_options_async(request, runtime)

    def detach_cen_child_instance_with_options(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DetachCenChildInstanceResponse(),
            self.do_rpcrequest('DetachCenChildInstance', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_cen_child_instance_with_options_async(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DetachCenChildInstanceResponse(),
            await self.do_rpcrequest_async('DetachCenChildInstance', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_cen_child_instance(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_cen_child_instance_with_options(request, runtime)

    async def detach_cen_child_instance_async(
        self,
        request: cbn_20170912_models.DetachCenChildInstanceRequest,
    ) -> cbn_20170912_models.DetachCenChildInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_cen_child_instance_with_options_async(request, runtime)

    def disable_cen_vbr_health_check_with_options(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableCenVbrHealthCheckResponse(),
            self.do_rpcrequest('DisableCenVbrHealthCheck', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_cen_vbr_health_check_with_options_async(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.DisableCenVbrHealthCheckResponse(),
            await self.do_rpcrequest_async('DisableCenVbrHealthCheck', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_cen_vbr_health_check(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_cen_vbr_health_check_with_options(request, runtime)

    async def disable_cen_vbr_health_check_async(
        self,
        request: cbn_20170912_models.DisableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.DisableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_cen_vbr_health_check_with_options_async(request, runtime)

    def enable_cen_vbr_health_check_with_options(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableCenVbrHealthCheckResponse(),
            self.do_rpcrequest('EnableCenVbrHealthCheck', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_cen_vbr_health_check_with_options_async(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.EnableCenVbrHealthCheckResponse(),
            await self.do_rpcrequest_async('EnableCenVbrHealthCheck', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_cen_vbr_health_check(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_cen_vbr_health_check_with_options(request, runtime)

    async def enable_cen_vbr_health_check_async(
        self,
        request: cbn_20170912_models.EnableCenVbrHealthCheckRequest,
    ) -> cbn_20170912_models.EnableCenVbrHealthCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_cen_vbr_health_check_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cbn_20170912_models.ListTagResourcesRequest,
    ) -> cbn_20170912_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_cen_attribute_with_options(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenAttributeResponse(),
            self.do_rpcrequest('ModifyCenAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cen_attribute_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenAttributeResponse(),
            await self.do_rpcrequest_async('ModifyCenAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cen_attribute(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_attribute_with_options(request, runtime)

    async def modify_cen_attribute_async(
        self,
        request: cbn_20170912_models.ModifyCenAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_attribute_with_options_async(request, runtime)

    def modify_cen_bandwidth_package_attribute_with_options(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse(),
            self.do_rpcrequest('ModifyCenBandwidthPackageAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cen_bandwidth_package_attribute_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse(),
            await self.do_rpcrequest_async('ModifyCenBandwidthPackageAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cen_bandwidth_package_attribute(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_bandwidth_package_attribute_with_options(request, runtime)

    async def modify_cen_bandwidth_package_attribute_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageAttributeRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_bandwidth_package_attribute_with_options_async(request, runtime)

    def modify_cen_bandwidth_package_spec_with_options(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse(),
            self.do_rpcrequest('ModifyCenBandwidthPackageSpec', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cen_bandwidth_package_spec_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse(),
            await self.do_rpcrequest_async('ModifyCenBandwidthPackageSpec', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cen_bandwidth_package_spec(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_bandwidth_package_spec_with_options(request, runtime)

    async def modify_cen_bandwidth_package_spec_async(
        self,
        request: cbn_20170912_models.ModifyCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.ModifyCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_bandwidth_package_spec_with_options_async(request, runtime)

    def modify_cen_route_map_with_options(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenRouteMapResponse(),
            self.do_rpcrequest('ModifyCenRouteMap', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cen_route_map_with_options_async(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyCenRouteMapResponse(),
            await self.do_rpcrequest_async('ModifyCenRouteMap', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cen_route_map(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cen_route_map_with_options(request, runtime)

    async def modify_cen_route_map_async(
        self,
        request: cbn_20170912_models.ModifyCenRouteMapRequest,
    ) -> cbn_20170912_models.ModifyCenRouteMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cen_route_map_with_options_async(request, runtime)

    def modify_flow_log_attribute_with_options(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyFlowLogAttributeResponse(),
            self.do_rpcrequest('ModifyFlowLogAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ModifyFlowLogAttributeResponse(),
            await self.do_rpcrequest_async('ModifyFlowLogAttribute', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_log_attribute(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    async def modify_flow_log_attribute_async(
        self,
        request: cbn_20170912_models.ModifyFlowLogAttributeRequest,
    ) -> cbn_20170912_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_log_attribute_with_options_async(request, runtime)

    def publish_route_entries_with_options(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.PublishRouteEntriesResponse(),
            self.do_rpcrequest('PublishRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.PublishRouteEntriesResponse(),
            await self.do_rpcrequest_async('PublishRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_route_entries(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_route_entries_with_options(request, runtime)

    async def publish_route_entries_async(
        self,
        request: cbn_20170912_models.PublishRouteEntriesRequest,
    ) -> cbn_20170912_models.PublishRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_route_entries_with_options_async(request, runtime)

    def resolve_and_route_service_in_cen_with_options(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ResolveAndRouteServiceInCenResponse(),
            self.do_rpcrequest('ResolveAndRouteServiceInCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resolve_and_route_service_in_cen_with_options_async(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.ResolveAndRouteServiceInCenResponse(),
            await self.do_rpcrequest_async('ResolveAndRouteServiceInCen', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resolve_and_route_service_in_cen(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.resolve_and_route_service_in_cen_with_options(request, runtime)

    async def resolve_and_route_service_in_cen_async(
        self,
        request: cbn_20170912_models.ResolveAndRouteServiceInCenRequest,
    ) -> cbn_20170912_models.ResolveAndRouteServiceInCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resolve_and_route_service_in_cen_with_options_async(request, runtime)

    def route_private_zone_in_cen_to_vpc_with_options(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse(),
            self.do_rpcrequest('RoutePrivateZoneInCenToVpc', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def route_private_zone_in_cen_to_vpc_with_options_async(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse(),
            await self.do_rpcrequest_async('RoutePrivateZoneInCenToVpc', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def route_private_zone_in_cen_to_vpc(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.route_private_zone_in_cen_to_vpc_with_options(request, runtime)

    async def route_private_zone_in_cen_to_vpc_async(
        self,
        request: cbn_20170912_models.RoutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.RoutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.route_private_zone_in_cen_to_vpc_with_options_async(request, runtime)

    def set_cen_inter_region_bandwidth_limit_with_options(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse(),
            self.do_rpcrequest('SetCenInterRegionBandwidthLimit', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_cen_inter_region_bandwidth_limit_with_options_async(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse(),
            await self.do_rpcrequest_async('SetCenInterRegionBandwidthLimit', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_cen_inter_region_bandwidth_limit(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_cen_inter_region_bandwidth_limit_with_options(request, runtime)

    async def set_cen_inter_region_bandwidth_limit_async(
        self,
        request: cbn_20170912_models.SetCenInterRegionBandwidthLimitRequest,
    ) -> cbn_20170912_models.SetCenInterRegionBandwidthLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_cen_inter_region_bandwidth_limit_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
    ) -> cbn_20170912_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cbn_20170912_models.TagResourcesRequest,
    ) -> cbn_20170912_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def temp_upgrade_cen_bandwidth_package_spec_with_options(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse(),
            self.do_rpcrequest('TempUpgradeCenBandwidthPackageSpec', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def temp_upgrade_cen_bandwidth_package_spec_with_options_async(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse(),
            await self.do_rpcrequest_async('TempUpgradeCenBandwidthPackageSpec', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def temp_upgrade_cen_bandwidth_package_spec(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.temp_upgrade_cen_bandwidth_package_spec_with_options(request, runtime)

    async def temp_upgrade_cen_bandwidth_package_spec_async(
        self,
        request: cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecRequest,
    ) -> cbn_20170912_models.TempUpgradeCenBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.temp_upgrade_cen_bandwidth_package_spec_with_options_async(request, runtime)

    def unassociate_cen_bandwidth_package_with_options(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnassociateCenBandwidthPackageResponse(),
            self.do_rpcrequest('UnassociateCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_cen_bandwidth_package_with_options_async(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnassociateCenBandwidthPackageResponse(),
            await self.do_rpcrequest_async('UnassociateCenBandwidthPackage', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_cen_bandwidth_package(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_cen_bandwidth_package_with_options(request, runtime)

    async def unassociate_cen_bandwidth_package_async(
        self,
        request: cbn_20170912_models.UnassociateCenBandwidthPackageRequest,
    ) -> cbn_20170912_models.UnassociateCenBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_cen_bandwidth_package_with_options_async(request, runtime)

    def unroute_private_zone_in_cen_to_vpc_with_options(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse(),
            self.do_rpcrequest('UnroutePrivateZoneInCenToVpc', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unroute_private_zone_in_cen_to_vpc_with_options_async(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse(),
            await self.do_rpcrequest_async('UnroutePrivateZoneInCenToVpc', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unroute_private_zone_in_cen_to_vpc(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.unroute_private_zone_in_cen_to_vpc_with_options(request, runtime)

    async def unroute_private_zone_in_cen_to_vpc_async(
        self,
        request: cbn_20170912_models.UnroutePrivateZoneInCenToVpcRequest,
    ) -> cbn_20170912_models.UnroutePrivateZoneInCenToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unroute_private_zone_in_cen_to_vpc_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cbn_20170912_models.UntagResourcesRequest,
    ) -> cbn_20170912_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def withdraw_published_route_entries_with_options(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.WithdrawPublishedRouteEntriesResponse(),
            self.do_rpcrequest('WithdrawPublishedRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def withdraw_published_route_entries_with_options_async(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cbn_20170912_models.WithdrawPublishedRouteEntriesResponse(),
            await self.do_rpcrequest_async('WithdrawPublishedRouteEntries', '2017-09-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def withdraw_published_route_entries(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.withdraw_published_route_entries_with_options(request, runtime)

    async def withdraw_published_route_entries_async(
        self,
        request: cbn_20170912_models.WithdrawPublishedRouteEntriesRequest,
    ) -> cbn_20170912_models.WithdrawPublishedRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_published_route_entries_with_options_async(request, runtime)
