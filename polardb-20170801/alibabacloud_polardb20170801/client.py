# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_polardb20170801 import models as polardb_20170801_models
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
            'cn-qingdao': 'polardb.aliyuncs.com',
            'cn-beijing': 'polardb.aliyuncs.com',
            'cn-hangzhou': 'polardb.aliyuncs.com',
            'cn-shanghai': 'polardb.aliyuncs.com',
            'cn-shenzhen': 'polardb.aliyuncs.com',
            'cn-hongkong': 'polardb.aliyuncs.com',
            'ap-southeast-1': 'polardb.aliyuncs.com',
            'us-west-1': 'polardb.aliyuncs.com',
            'us-east-1': 'polardb.aliyuncs.com',
            'cn-hangzhou-finance': 'polardb.aliyuncs.com',
            'cn-shanghai-finance-1': 'polardb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'polardb.aliyuncs.com',
            'ap-northeast-2-pop': 'polardb.aliyuncs.com',
            'cn-beijing-finance-1': 'polardb.aliyuncs.com',
            'cn-beijing-finance-pop': 'polardb.aliyuncs.com',
            'cn-beijing-gov-1': 'polardb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'polardb.aliyuncs.com',
            'cn-edge-1': 'polardb.aliyuncs.com',
            'cn-fujian': 'polardb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'polardb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'polardb.aliyuncs.com',
            'cn-hangzhou-test-306': 'polardb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'polardb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'polardb.aliyuncs.com',
            'cn-north-2-gov-1': 'polardb.aliyuncs.com',
            'cn-qingdao-nebula': 'polardb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'polardb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'polardb.aliyuncs.com',
            'cn-shanghai-inner': 'polardb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'polardb.aliyuncs.com',
            'cn-shenzhen-inner': 'polardb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'polardb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'polardb.aliyuncs.com',
            'cn-wuhan': 'polardb.aliyuncs.com',
            'cn-wulanchabu': 'polardb.aliyuncs.com',
            'cn-yushanfang': 'polardb.aliyuncs.com',
            'cn-zhangbei': 'polardb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'polardb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'polardb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'polardb.aliyuncs.com',
            'eu-west-1-oxs': 'polardb.aliyuncs.com',
            'rus-west-1-pop': 'polardb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('polardb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def modify_dbcluster_monitor_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMonitorResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterMonitor', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_monitor_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMonitorResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterMonitor', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_monitor(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_monitor_with_options(request, runtime)

    async def modify_dbcluster_monitor_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_monitor_with_options_async(request, runtime)
