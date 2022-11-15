# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hitsdb20200615 import models as hitsdb_20200615_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'hitsdb.aliyuncs.com',
            'cn-beijing': 'hitsdb.aliyuncs.com',
            'cn-hangzhou': 'hitsdb.aliyuncs.com',
            'cn-shanghai': 'hitsdb.aliyuncs.com',
            'cn-shenzhen': 'hitsdb.aliyuncs.com',
            'cn-hongkong': 'hitsdb.aliyuncs.com',
            'ap-southeast-1': 'hitsdb.aliyuncs.com',
            'us-west-1': 'hitsdb.aliyuncs.com',
            'us-east-1': 'hitsdb.aliyuncs.com',
            'cn-shanghai-finance-1': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'hitsdb.aliyuncs.com',
            'ap-northeast-2-pop': 'hitsdb.aliyuncs.com',
            'cn-beijing-finance-1': 'hitsdb.aliyuncs.com',
            'cn-beijing-finance-pop': 'hitsdb.aliyuncs.com',
            'cn-beijing-gov-1': 'hitsdb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hitsdb.aliyuncs.com',
            'cn-chengdu': 'hitsdb.aliyuncs.com',
            'cn-edge-1': 'hitsdb.aliyuncs.com',
            'cn-fujian': 'hitsdb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-finance': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hitsdb.aliyuncs.com',
            'cn-hangzhou-test-306': 'hitsdb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hitsdb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'hitsdb.aliyuncs.com',
            'cn-qingdao-nebula': 'hitsdb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hitsdb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hitsdb.aliyuncs.com',
            'cn-shanghai-inner': 'hitsdb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-inner': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hitsdb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hitsdb.aliyuncs.com',
            'cn-wuhan': 'hitsdb.aliyuncs.com',
            'cn-wulanchabu': 'hitsdb.aliyuncs.com',
            'cn-yushanfang': 'hitsdb.aliyuncs.com',
            'cn-zhangbei': 'hitsdb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hitsdb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hitsdb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hitsdb.aliyuncs.com',
            'eu-west-1-oxs': 'hitsdb.aliyuncs.com',
            'me-east-1': 'hitsdb.aliyuncs.com',
            'rus-west-1-pop': 'hitsdb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hitsdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.core_spec):
            query['CoreSpec'] = request.core_spec
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_disk_category):
            query['LogDiskCategory'] = request.log_disk_category
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.CreateLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not UtilClient.is_unset(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not UtilClient.is_unset(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.core_spec):
            query['CoreSpec'] = request.core_spec
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_disk_category):
            query['LogDiskCategory'] = request.log_disk_category
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not UtilClient.is_unset(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not UtilClient.is_unset(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.CreateLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lindorm_instance(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_lindorm_instance_with_options(request, runtime)

    async def create_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.CreateLindormInstanceRequest,
    ) -> hitsdb_20200615_models.CreateLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_lindorm_instance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: hitsdb_20200615_models.DescribeRegionsRequest,
    ) -> hitsdb_20200615_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def get_instance_ip_white_list_with_options(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetInstanceIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_ip_white_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetInstanceIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_ip_white_list(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_ip_white_list_with_options(request, runtime)

    async def get_instance_ip_white_list_async(
        self,
        request: hitsdb_20200615_models.GetInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.GetInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_ip_white_list_with_options_async(request, runtime)

    def get_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_instance(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_with_options(request, runtime)

    async def get_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_with_options_async(request, runtime)

    def get_lindorm_instance_engine_list_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceEngineList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetLindormInstanceEngineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_instance_engine_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceEngineList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetLindormInstanceEngineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_instance_engine_list(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_engine_list_with_options(request, runtime)

    async def get_lindorm_instance_engine_list_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceEngineListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceEngineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_engine_list_with_options_async(request, runtime)

    def get_lindorm_instance_list_with_options(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            query['QueryStr'] = request.query_str
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.support_engine):
            query['SupportEngine'] = request.support_engine
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetLindormInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lindorm_instance_list_with_options_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            query['QueryStr'] = request.query_str
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.support_engine):
            query['SupportEngine'] = request.support_engine
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLindormInstanceList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.GetLindormInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lindorm_instance_list(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lindorm_instance_list_with_options(request, runtime)

    async def get_lindorm_instance_list_async(
        self,
        request: hitsdb_20200615_models.GetLindormInstanceListRequest,
    ) -> hitsdb_20200615_models.GetLindormInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lindorm_instance_list_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: hitsdb_20200615_models.ListTagResourcesRequest,
    ) -> hitsdb_20200615_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_instance_pay_type_with_options(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstancePayType',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.ModifyInstancePayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_pay_type_with_options_async(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstancePayType',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.ModifyInstancePayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_pay_type(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_pay_type_with_options(request, runtime)

    async def modify_instance_pay_type_async(
        self,
        request: hitsdb_20200615_models.ModifyInstancePayTypeRequest,
    ) -> hitsdb_20200615_models.ModifyInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_pay_type_with_options_async(request, runtime)

    def release_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.ReleaseLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.ReleaseLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_lindorm_instance(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_lindorm_instance_with_options(request, runtime)

    async def release_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.ReleaseLindormInstanceRequest,
    ) -> hitsdb_20200615_models.ReleaseLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_lindorm_instance_with_options_async(request, runtime)

    def renew_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.RenewLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.RenewLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_lindorm_instance(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_lindorm_instance_with_options(request, runtime)

    async def renew_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.RenewLindormInstanceRequest,
    ) -> hitsdb_20200615_models.RenewLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_lindorm_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: hitsdb_20200615_models.TagResourcesRequest,
    ) -> hitsdb_20200615_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: hitsdb_20200615_models.UntagResourcesRequest,
    ) -> hitsdb_20200615_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_instance_ip_white_list_with_options(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_ip_white_list_with_options_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_ip_list):
            query['SecurityIpList'] = request.security_ip_list
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceIpWhiteList',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_ip_white_list(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_ip_white_list_with_options(request, runtime)

    async def update_instance_ip_white_list_async(
        self,
        request: hitsdb_20200615_models.UpdateInstanceIpWhiteListRequest,
    ) -> hitsdb_20200615_models.UpdateInstanceIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_ip_white_list_with_options_async(request, runtime)

    def upgrade_lindorm_instance_with_options(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_storage):
            query['ClusterStorage'] = request.cluster_storage
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.lts_core_num):
            query['LtsCoreNum'] = request.lts_core_num
        if not UtilClient.is_unset(request.lts_core_spec):
            query['LtsCoreSpec'] = request.lts_core_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phoenix_core_num):
            query['PhoenixCoreNum'] = request.phoenix_core_num
        if not UtilClient.is_unset(request.phoenix_core_spec):
            query['PhoenixCoreSpec'] = request.phoenix_core_spec
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.UpgradeLindormInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_lindorm_instance_with_options_async(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_storage):
            query['ClusterStorage'] = request.cluster_storage
        if not UtilClient.is_unset(request.cold_storage):
            query['ColdStorage'] = request.cold_storage
        if not UtilClient.is_unset(request.core_single_storage):
            query['CoreSingleStorage'] = request.core_single_storage
        if not UtilClient.is_unset(request.filestore_num):
            query['FilestoreNum'] = request.filestore_num
        if not UtilClient.is_unset(request.filestore_spec):
            query['FilestoreSpec'] = request.filestore_spec
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lindorm_num):
            query['LindormNum'] = request.lindorm_num
        if not UtilClient.is_unset(request.lindorm_spec):
            query['LindormSpec'] = request.lindorm_spec
        if not UtilClient.is_unset(request.log_num):
            query['LogNum'] = request.log_num
        if not UtilClient.is_unset(request.log_single_storage):
            query['LogSingleStorage'] = request.log_single_storage
        if not UtilClient.is_unset(request.log_spec):
            query['LogSpec'] = request.log_spec
        if not UtilClient.is_unset(request.lts_core_num):
            query['LtsCoreNum'] = request.lts_core_num
        if not UtilClient.is_unset(request.lts_core_spec):
            query['LtsCoreSpec'] = request.lts_core_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.phoenix_core_num):
            query['PhoenixCoreNum'] = request.phoenix_core_num
        if not UtilClient.is_unset(request.phoenix_core_spec):
            query['PhoenixCoreSpec'] = request.phoenix_core_spec
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.solr_num):
            query['SolrNum'] = request.solr_num
        if not UtilClient.is_unset(request.solr_spec):
            query['SolrSpec'] = request.solr_spec
        if not UtilClient.is_unset(request.tsdb_num):
            query['TsdbNum'] = request.tsdb_num
        if not UtilClient.is_unset(request.tsdb_spec):
            query['TsdbSpec'] = request.tsdb_spec
        if not UtilClient.is_unset(request.upgrade_type):
            query['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeLindormInstance',
            version='2020-06-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20200615_models.UpgradeLindormInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_lindorm_instance(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_lindorm_instance_with_options(request, runtime)

    async def upgrade_lindorm_instance_async(
        self,
        request: hitsdb_20200615_models.UpgradeLindormInstanceRequest,
    ) -> hitsdb_20200615_models.UpgradeLindormInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_lindorm_instance_with_options_async(request, runtime)
