# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_hitsdb20170601 import models as hitsdb_20170601_models
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

    def create_hi_tsdbinstance_with_options(
        self,
        request: hitsdb_20170601_models.CreateHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.CreateHiTSDBInstanceResponse:
        """
        @param request: CreateHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHiTSDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
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
            action='CreateHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.CreateHiTSDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hi_tsdbinstance_with_options_async(
        self,
        request: hitsdb_20170601_models.CreateHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.CreateHiTSDBInstanceResponse:
        """
        @param request: CreateHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHiTSDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.disk_category):
            query['DiskCategory'] = request.disk_category
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
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
            action='CreateHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.CreateHiTSDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hi_tsdbinstance(
        self,
        request: hitsdb_20170601_models.CreateHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.CreateHiTSDBInstanceResponse:
        """
        @param request: CreateHiTSDBInstanceRequest
        @return: CreateHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hi_tsdbinstance_with_options(request, runtime)

    async def create_hi_tsdbinstance_async(
        self,
        request: hitsdb_20170601_models.CreateHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.CreateHiTSDBInstanceResponse:
        """
        @param request: CreateHiTSDBInstanceRequest
        @return: CreateHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hi_tsdbinstance_with_options_async(request, runtime)

    def delete_hi_tsdbinstance_with_options(
        self,
        request: hitsdb_20170601_models.DeleteHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DeleteHiTSDBInstanceResponse:
        """
        @summary Deletes a Time Series Database (TSDB) instance.
        
        @param request: DeleteHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHiTSDBInstanceResponse
        """
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
            action='DeleteHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DeleteHiTSDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hi_tsdbinstance_with_options_async(
        self,
        request: hitsdb_20170601_models.DeleteHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DeleteHiTSDBInstanceResponse:
        """
        @summary Deletes a Time Series Database (TSDB) instance.
        
        @param request: DeleteHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHiTSDBInstanceResponse
        """
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
            action='DeleteHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DeleteHiTSDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hi_tsdbinstance(
        self,
        request: hitsdb_20170601_models.DeleteHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.DeleteHiTSDBInstanceResponse:
        """
        @summary Deletes a Time Series Database (TSDB) instance.
        
        @param request: DeleteHiTSDBInstanceRequest
        @return: DeleteHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hi_tsdbinstance_with_options(request, runtime)

    async def delete_hi_tsdbinstance_async(
        self,
        request: hitsdb_20170601_models.DeleteHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.DeleteHiTSDBInstanceResponse:
        """
        @summary Deletes a Time Series Database (TSDB) instance.
        
        @param request: DeleteHiTSDBInstanceRequest
        @return: DeleteHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hi_tsdbinstance_with_options_async(request, runtime)

    def describe_hi_tsdbinstance_with_options(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceResponse:
        """
        @summary Queries the details about a Time Series Database (TSDB) instance.
        
        @param request: DescribeHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHiTSDBInstanceResponse
        """
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
            action='DescribeHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeHiTSDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hi_tsdbinstance_with_options_async(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceResponse:
        """
        @summary Queries the details about a Time Series Database (TSDB) instance.
        
        @param request: DescribeHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHiTSDBInstanceResponse
        """
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
            action='DescribeHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeHiTSDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hi_tsdbinstance(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceResponse:
        """
        @summary Queries the details about a Time Series Database (TSDB) instance.
        
        @param request: DescribeHiTSDBInstanceRequest
        @return: DescribeHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_tsdbinstance_with_options(request, runtime)

    async def describe_hi_tsdbinstance_async(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceResponse:
        """
        @summary Queries the details about a Time Series Database (TSDB) instance.
        
        @param request: DescribeHiTSDBInstanceRequest
        @return: DescribeHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hi_tsdbinstance_with_options_async(request, runtime)

    def describe_hi_tsdbinstance_list_with_options(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceListResponse:
        """
        @param request: DescribeHiTSDBInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHiTSDBInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHiTSDBInstanceList',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeHiTSDBInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hi_tsdbinstance_list_with_options_async(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceListResponse:
        """
        @param request: DescribeHiTSDBInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHiTSDBInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.engine_type):
            query['EngineType'] = request.engine_type
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHiTSDBInstanceList',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeHiTSDBInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hi_tsdbinstance_list(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceListRequest,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceListResponse:
        """
        @param request: DescribeHiTSDBInstanceListRequest
        @return: DescribeHiTSDBInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_tsdbinstance_list_with_options(request, runtime)

    async def describe_hi_tsdbinstance_list_async(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceListRequest,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceListResponse:
        """
        @param request: DescribeHiTSDBInstanceListRequest
        @return: DescribeHiTSDBInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hi_tsdbinstance_list_with_options_async(request, runtime)

    def describe_hi_tsdbinstance_security_ip_list_with_options(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: DescribeHiTSDBInstanceSecurityIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHiTSDBInstanceSecurityIpListResponse
        """
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
            action='DescribeHiTSDBInstanceSecurityIpList',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hi_tsdbinstance_security_ip_list_with_options_async(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: DescribeHiTSDBInstanceSecurityIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHiTSDBInstanceSecurityIpListResponse
        """
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
            action='DescribeHiTSDBInstanceSecurityIpList',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hi_tsdbinstance_security_ip_list(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListRequest,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: DescribeHiTSDBInstanceSecurityIpListRequest
        @return: DescribeHiTSDBInstanceSecurityIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_tsdbinstance_security_ip_list_with_options(request, runtime)

    async def describe_hi_tsdbinstance_security_ip_list_async(
        self,
        request: hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListRequest,
    ) -> hitsdb_20170601_models.DescribeHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: DescribeHiTSDBInstanceSecurityIpListRequest
        @return: DescribeHiTSDBInstanceSecurityIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hi_tsdbinstance_security_ip_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: hitsdb_20170601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Time Series Database (TSDB) instances can be deployed.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: hitsdb_20170601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Time Series Database (TSDB) instances can be deployed.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
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
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: hitsdb_20170601_models.DescribeRegionsRequest,
    ) -> hitsdb_20170601_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Time Series Database (TSDB) instances can be deployed.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: hitsdb_20170601_models.DescribeRegionsRequest,
    ) -> hitsdb_20170601_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which Time Series Database (TSDB) instances can be deployed.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: hitsdb_20170601_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeZonesResponse:
        """
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
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
            action='DescribeZones',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: hitsdb_20170601_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.DescribeZonesResponse:
        """
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
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
            action='DescribeZones',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: hitsdb_20170601_models.DescribeZonesRequest,
    ) -> hitsdb_20170601_models.DescribeZonesResponse:
        """
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: hitsdb_20170601_models.DescribeZonesRequest,
    ) -> hitsdb_20170601_models.DescribeZonesResponse:
        """
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def modify_hi_tsdbinstance_class_with_options(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceClassResponse:
        """
        @param request: ModifyHiTSDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHiTSDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
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
            action='ModifyHiTSDBInstanceClass',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.ModifyHiTSDBInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hi_tsdbinstance_class_with_options_async(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceClassResponse:
        """
        @param request: ModifyHiTSDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHiTSDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_storage):
            query['InstanceStorage'] = request.instance_storage
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
            action='ModifyHiTSDBInstanceClass',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.ModifyHiTSDBInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hi_tsdbinstance_class(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceClassRequest,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceClassResponse:
        """
        @param request: ModifyHiTSDBInstanceClassRequest
        @return: ModifyHiTSDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hi_tsdbinstance_class_with_options(request, runtime)

    async def modify_hi_tsdbinstance_class_async(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceClassRequest,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceClassResponse:
        """
        @param request: ModifyHiTSDBInstanceClassRequest
        @return: ModifyHiTSDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hi_tsdbinstance_class_with_options_async(request, runtime)

    def modify_hi_tsdbinstance_security_ip_list_with_options(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: ModifyHiTSDBInstanceSecurityIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHiTSDBInstanceSecurityIpListResponse
        """
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
            action='ModifyHiTSDBInstanceSecurityIpList',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hi_tsdbinstance_security_ip_list_with_options_async(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: ModifyHiTSDBInstanceSecurityIpListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyHiTSDBInstanceSecurityIpListResponse
        """
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
            action='ModifyHiTSDBInstanceSecurityIpList',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hi_tsdbinstance_security_ip_list(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListRequest,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: ModifyHiTSDBInstanceSecurityIpListRequest
        @return: ModifyHiTSDBInstanceSecurityIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_hi_tsdbinstance_security_ip_list_with_options(request, runtime)

    async def modify_hi_tsdbinstance_security_ip_list_async(
        self,
        request: hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListRequest,
    ) -> hitsdb_20170601_models.ModifyHiTSDBInstanceSecurityIpListResponse:
        """
        @param request: ModifyHiTSDBInstanceSecurityIpListRequest
        @return: ModifyHiTSDBInstanceSecurityIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_hi_tsdbinstance_security_ip_list_with_options_async(request, runtime)

    def rename_hi_tsdbinstance_alias_with_options(
        self,
        request: hitsdb_20170601_models.RenameHiTSDBInstanceAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.RenameHiTSDBInstanceAliasResponse:
        """
        @summary Invoke RenameHiTSDBInstanceAlias to modify the instance alias.
        
        @param request: RenameHiTSDBInstanceAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameHiTSDBInstanceAliasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
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
            action='RenameHiTSDBInstanceAlias',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.RenameHiTSDBInstanceAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_hi_tsdbinstance_alias_with_options_async(
        self,
        request: hitsdb_20170601_models.RenameHiTSDBInstanceAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.RenameHiTSDBInstanceAliasResponse:
        """
        @summary Invoke RenameHiTSDBInstanceAlias to modify the instance alias.
        
        @param request: RenameHiTSDBInstanceAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameHiTSDBInstanceAliasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
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
            action='RenameHiTSDBInstanceAlias',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.RenameHiTSDBInstanceAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_hi_tsdbinstance_alias(
        self,
        request: hitsdb_20170601_models.RenameHiTSDBInstanceAliasRequest,
    ) -> hitsdb_20170601_models.RenameHiTSDBInstanceAliasResponse:
        """
        @summary Invoke RenameHiTSDBInstanceAlias to modify the instance alias.
        
        @param request: RenameHiTSDBInstanceAliasRequest
        @return: RenameHiTSDBInstanceAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rename_hi_tsdbinstance_alias_with_options(request, runtime)

    async def rename_hi_tsdbinstance_alias_async(
        self,
        request: hitsdb_20170601_models.RenameHiTSDBInstanceAliasRequest,
    ) -> hitsdb_20170601_models.RenameHiTSDBInstanceAliasResponse:
        """
        @summary Invoke RenameHiTSDBInstanceAlias to modify the instance alias.
        
        @param request: RenameHiTSDBInstanceAliasRequest
        @return: RenameHiTSDBInstanceAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rename_hi_tsdbinstance_alias_with_options_async(request, runtime)

    def renew_tsdbinstance_with_options(
        self,
        request: hitsdb_20170601_models.RenewTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.RenewTSDBInstanceResponse:
        """
        @param request: RenewTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewTSDBInstanceResponse
        """
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
            action='RenewTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.RenewTSDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_tsdbinstance_with_options_async(
        self,
        request: hitsdb_20170601_models.RenewTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.RenewTSDBInstanceResponse:
        """
        @param request: RenewTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewTSDBInstanceResponse
        """
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
            action='RenewTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.RenewTSDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_tsdbinstance(
        self,
        request: hitsdb_20170601_models.RenewTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.RenewTSDBInstanceResponse:
        """
        @param request: RenewTSDBInstanceRequest
        @return: RenewTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_tsdbinstance_with_options(request, runtime)

    async def renew_tsdbinstance_async(
        self,
        request: hitsdb_20170601_models.RenewTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.RenewTSDBInstanceResponse:
        """
        @param request: RenewTSDBInstanceRequest
        @return: RenewTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_tsdbinstance_with_options_async(request, runtime)

    def restart_hi_tsdbinstance_with_options(
        self,
        request: hitsdb_20170601_models.RestartHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.RestartHiTSDBInstanceResponse:
        """
        @summary Restarts a Time Series Database (TSDB) instance.
        
        @param request: RestartHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartHiTSDBInstanceResponse
        """
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
            action='RestartHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.RestartHiTSDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_hi_tsdbinstance_with_options_async(
        self,
        request: hitsdb_20170601_models.RestartHiTSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.RestartHiTSDBInstanceResponse:
        """
        @summary Restarts a Time Series Database (TSDB) instance.
        
        @param request: RestartHiTSDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartHiTSDBInstanceResponse
        """
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
            action='RestartHiTSDBInstance',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.RestartHiTSDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_hi_tsdbinstance(
        self,
        request: hitsdb_20170601_models.RestartHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.RestartHiTSDBInstanceResponse:
        """
        @summary Restarts a Time Series Database (TSDB) instance.
        
        @param request: RestartHiTSDBInstanceRequest
        @return: RestartHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_hi_tsdbinstance_with_options(request, runtime)

    async def restart_hi_tsdbinstance_async(
        self,
        request: hitsdb_20170601_models.RestartHiTSDBInstanceRequest,
    ) -> hitsdb_20170601_models.RestartHiTSDBInstanceResponse:
        """
        @summary Restarts a Time Series Database (TSDB) instance.
        
        @param request: RestartHiTSDBInstanceRequest
        @return: RestartHiTSDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_hi_tsdbinstance_with_options_async(request, runtime)

    def switch_hi_tsdbinstance_public_net_with_options(
        self,
        request: hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetResponse:
        """
        @summary Switches the Internet connection status of a Time Series Database (TSDB) instance.
        
        @param request: SwitchHiTSDBInstancePublicNetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchHiTSDBInstancePublicNetResponse
        """
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
        if not UtilClient.is_unset(request.switch_action):
            query['SwitchAction'] = request.switch_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchHiTSDBInstancePublicNet',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_hi_tsdbinstance_public_net_with_options_async(
        self,
        request: hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetResponse:
        """
        @summary Switches the Internet connection status of a Time Series Database (TSDB) instance.
        
        @param request: SwitchHiTSDBInstancePublicNetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchHiTSDBInstancePublicNetResponse
        """
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
        if not UtilClient.is_unset(request.switch_action):
            query['SwitchAction'] = request.switch_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchHiTSDBInstancePublicNet',
            version='2017-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_hi_tsdbinstance_public_net(
        self,
        request: hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetRequest,
    ) -> hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetResponse:
        """
        @summary Switches the Internet connection status of a Time Series Database (TSDB) instance.
        
        @param request: SwitchHiTSDBInstancePublicNetRequest
        @return: SwitchHiTSDBInstancePublicNetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.switch_hi_tsdbinstance_public_net_with_options(request, runtime)

    async def switch_hi_tsdbinstance_public_net_async(
        self,
        request: hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetRequest,
    ) -> hitsdb_20170601_models.SwitchHiTSDBInstancePublicNetResponse:
        """
        @summary Switches the Internet connection status of a Time Series Database (TSDB) instance.
        
        @param request: SwitchHiTSDBInstancePublicNetRequest
        @return: SwitchHiTSDBInstancePublicNetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.switch_hi_tsdbinstance_public_net_with_options_async(request, runtime)
