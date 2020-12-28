# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rds20140815 import models as rds_20140815_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'rds.aliyuncs.com',
            'cn-beijing': 'rds.aliyuncs.com',
            'cn-hangzhou': 'rds.aliyuncs.com',
            'cn-shanghai': 'rds.aliyuncs.com',
            'cn-shenzhen': 'rds.aliyuncs.com',
            'cn-hongkong': 'rds.aliyuncs.com',
            'ap-southeast-1': 'rds.aliyuncs.com',
            'us-west-1': 'rds.aliyuncs.com',
            'us-east-1': 'rds.aliyuncs.com',
            'cn-shanghai-finance-1': 'rds.aliyuncs.com',
            'cn-shenzhen-finance-1': 'rds.aliyuncs.com',
            'cn-north-2-gov-1': 'rds.aliyuncs.com',
            'ap-northeast-2-pop': 'rds.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'rds.aliyuncs.com',
            'cn-beijing-finance-pop': 'rds.aliyuncs.com',
            'cn-beijing-gov-1': 'rds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'rds.aliyuncs.com',
            'cn-edge-1': 'rds.aliyuncs.com',
            'cn-fujian': 'rds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'rds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'rds.aliyuncs.com',
            'cn-hangzhou-finance': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'rds.aliyuncs.com',
            'cn-hangzhou-test-306': 'rds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'rds.aliyuncs.com',
            'cn-qingdao-nebula': 'rds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'rds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'rds.aliyuncs.com',
            'cn-shanghai-inner': 'rds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'rds.aliyuncs.com',
            'cn-shenzhen-inner': 'rds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'rds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'rds.aliyuncs.com',
            'cn-wuhan': 'rds.aliyuncs.com',
            'cn-yushanfang': 'rds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'rds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'rds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'rds.aliyuncs.com',
            'eu-west-1-oxs': 'rds.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'rds.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('rds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_diagnostic_report_with_options(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDiagnosticReportResponse().from_map(
            self.do_rpcrequest('CreateDiagnosticReport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDiagnosticReportResponse().from_map(
            await self.do_rpcrequest_async('CreateDiagnosticReport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_diagnostic_report(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def describe_diagnostic_report_list_with_options(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDiagnosticReportListResponse().from_map(
            self.do_rpcrequest('DescribeDiagnosticReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDiagnosticReportListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDiagnosticReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnostic_report_list(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    async def describe_diagnostic_report_list_async(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_report_list_with_options_async(request, runtime)

    def get_dbinstance_topology_with_options(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GetDBInstanceTopologyResponse().from_map(
            self.do_rpcrequest('GetDBInstanceTopology', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dbinstance_topology_with_options_async(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GetDBInstanceTopologyResponse().from_map(
            await self.do_rpcrequest_async('GetDBInstanceTopology', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dbinstance_topology(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dbinstance_topology_with_options(request, runtime)

    async def get_dbinstance_topology_async(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dbinstance_topology_with_options_async(request, runtime)

    def migrate_connection_to_other_zone_with_options(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateConnectionToOtherZoneResponse().from_map(
            self.do_rpcrequest('MigrateConnectionToOtherZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_connection_to_other_zone_with_options_async(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateConnectionToOtherZoneResponse().from_map(
            await self.do_rpcrequest_async('MigrateConnectionToOtherZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_connection_to_other_zone(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_connection_to_other_zone_with_options(request, runtime)

    async def migrate_connection_to_other_zone_async(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_connection_to_other_zone_with_options_async(request, runtime)

    def modify_dbinstance_monitor_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceMonitorResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_monitor_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceMonitorResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_monitor(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    async def modify_dbinstance_monitor_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_monitor_with_options_async(request, runtime)
