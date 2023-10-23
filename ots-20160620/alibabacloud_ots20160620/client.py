# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ots20160620 import models as ots_20160620_models
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
        self._endpoint = self.get_endpoint('ots', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_instance_2vpc_with_options(
        self,
        request: ots_20160620_models.BindInstance2VpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.BindInstance2VpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_vpc_name):
            query['InstanceVpcName'] = request.instance_vpc_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.virtual_switch_id):
            query['VirtualSwitchId'] = request.virtual_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInstance2Vpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.BindInstance2VpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_instance_2vpc_with_options_async(
        self,
        request: ots_20160620_models.BindInstance2VpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.BindInstance2VpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_vpc_name):
            query['InstanceVpcName'] = request.instance_vpc_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.virtual_switch_id):
            query['VirtualSwitchId'] = request.virtual_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInstance2Vpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.BindInstance2VpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_instance_2vpc(
        self,
        request: ots_20160620_models.BindInstance2VpcRequest,
    ) -> ots_20160620_models.BindInstance2VpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_instance_2vpc_with_options(request, runtime)

    async def bind_instance_2vpc_async(
        self,
        request: ots_20160620_models.BindInstance2VpcRequest,
    ) -> ots_20160620_models.BindInstance2VpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_instance_2vpc_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: ots_20160620_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: ots_20160620_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: ots_20160620_models.DeleteInstanceRequest,
    ) -> ots_20160620_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: ots_20160620_models.DeleteInstanceRequest,
    ) -> ots_20160620_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_tags_with_options(
        self,
        request: ots_20160620_models.DeleteTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.DeleteTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.DeleteTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tags_with_options_async(
        self,
        request: ots_20160620_models.DeleteTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.DeleteTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.DeleteTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tags(
        self,
        request: ots_20160620_models.DeleteTagsRequest,
    ) -> ots_20160620_models.DeleteTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tags_with_options(request, runtime)

    async def delete_tags_async(
        self,
        request: ots_20160620_models.DeleteTagsRequest,
    ) -> ots_20160620_models.DeleteTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tags_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: ots_20160620_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: ots_20160620_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: ots_20160620_models.GetInstanceRequest,
    ) -> ots_20160620_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: ots_20160620_models.GetInstanceRequest,
    ) -> ots_20160620_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_ots_service_status_with_options(
        self,
        request: ots_20160620_models.GetOtsServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.GetOtsServiceStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOtsServiceStatus',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.GetOtsServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ots_service_status_with_options_async(
        self,
        request: ots_20160620_models.GetOtsServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.GetOtsServiceStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOtsServiceStatus',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.GetOtsServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ots_service_status(
        self,
        request: ots_20160620_models.GetOtsServiceStatusRequest,
    ) -> ots_20160620_models.GetOtsServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ots_service_status_with_options(request, runtime)

    async def get_ots_service_status_async(
        self,
        request: ots_20160620_models.GetOtsServiceStatusRequest,
    ) -> ots_20160620_models.GetOtsServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ots_service_status_with_options_async(request, runtime)

    def insert_instance_with_options(
        self,
        request: ots_20160620_models.InsertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.InsertInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.InsertInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_instance_with_options_async(
        self,
        request: ots_20160620_models.InsertInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.InsertInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.InsertInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_instance(
        self,
        request: ots_20160620_models.InsertInstanceRequest,
    ) -> ots_20160620_models.InsertInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_instance_with_options(request, runtime)

    async def insert_instance_async(
        self,
        request: ots_20160620_models.InsertInstanceRequest,
    ) -> ots_20160620_models.InsertInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_instance_with_options_async(request, runtime)

    def insert_tags_with_options(
        self,
        request: ots_20160620_models.InsertTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.InsertTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.InsertTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_tags_with_options_async(
        self,
        request: ots_20160620_models.InsertTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.InsertTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.InsertTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_tags(
        self,
        request: ots_20160620_models.InsertTagsRequest,
    ) -> ots_20160620_models.InsertTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_tags_with_options(request, runtime)

    async def insert_tags_async(
        self,
        request: ots_20160620_models.InsertTagsRequest,
    ) -> ots_20160620_models.InsertTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_tags_with_options_async(request, runtime)

    def list_cluster_type_with_options(
        self,
        request: ots_20160620_models.ListClusterTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListClusterTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterType',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListClusterTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_type_with_options_async(
        self,
        request: ots_20160620_models.ListClusterTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListClusterTypeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterType',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListClusterTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_type(
        self,
        request: ots_20160620_models.ListClusterTypeRequest,
    ) -> ots_20160620_models.ListClusterTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_type_with_options(request, runtime)

    async def list_cluster_type_async(
        self,
        request: ots_20160620_models.ListClusterTypeRequest,
    ) -> ots_20160620_models.ListClusterTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_type_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: ots_20160620_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: ots_20160620_models.ListInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: ots_20160620_models.ListInstanceRequest,
    ) -> ots_20160620_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: ots_20160620_models.ListInstanceRequest,
    ) -> ots_20160620_models.ListInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_tags_with_options(
        self,
        request: ots_20160620_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: ots_20160620_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag_info):
            query['TagInfo'] = request.tag_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: ots_20160620_models.ListTagsRequest,
    ) -> ots_20160620_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: ots_20160620_models.ListTagsRequest,
    ) -> ots_20160620_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def list_vpc_info_by_instance_with_options(
        self,
        request: ots_20160620_models.ListVpcInfoByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListVpcInfoByInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcInfoByInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListVpcInfoByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_info_by_instance_with_options_async(
        self,
        request: ots_20160620_models.ListVpcInfoByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListVpcInfoByInstanceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcInfoByInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListVpcInfoByInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_info_by_instance(
        self,
        request: ots_20160620_models.ListVpcInfoByInstanceRequest,
    ) -> ots_20160620_models.ListVpcInfoByInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_info_by_instance_with_options(request, runtime)

    async def list_vpc_info_by_instance_async(
        self,
        request: ots_20160620_models.ListVpcInfoByInstanceRequest,
    ) -> ots_20160620_models.ListVpcInfoByInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_info_by_instance_with_options_async(request, runtime)

    def list_vpc_info_by_vpc_with_options(
        self,
        request: ots_20160620_models.ListVpcInfoByVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListVpcInfoByVpcResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcInfoByVpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListVpcInfoByVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_info_by_vpc_with_options_async(
        self,
        request: ots_20160620_models.ListVpcInfoByVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.ListVpcInfoByVpcResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVpcInfoByVpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.ListVpcInfoByVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc_info_by_vpc(
        self,
        request: ots_20160620_models.ListVpcInfoByVpcRequest,
    ) -> ots_20160620_models.ListVpcInfoByVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_info_by_vpc_with_options(request, runtime)

    async def list_vpc_info_by_vpc_async(
        self,
        request: ots_20160620_models.ListVpcInfoByVpcRequest,
    ) -> ots_20160620_models.ListVpcInfoByVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_info_by_vpc_with_options_async(request, runtime)

    def open_ots_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.OpenOtsServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenOtsService',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.OpenOtsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_ots_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.OpenOtsServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenOtsService',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.OpenOtsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_ots_service(self) -> ots_20160620_models.OpenOtsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_ots_service_with_options(runtime)

    async def open_ots_service_async(self) -> ots_20160620_models.OpenOtsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_ots_service_with_options_async(runtime)

    def unbind_instance_2vpc_with_options(
        self,
        request: ots_20160620_models.UnbindInstance2VpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.UnbindInstance2VpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_vpc_name):
            query['InstanceVpcName'] = request.instance_vpc_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInstance2Vpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.UnbindInstance2VpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_instance_2vpc_with_options_async(
        self,
        request: ots_20160620_models.UnbindInstance2VpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.UnbindInstance2VpcResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_vpc_name):
            query['InstanceVpcName'] = request.instance_vpc_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInstance2Vpc',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.UnbindInstance2VpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_instance_2vpc(
        self,
        request: ots_20160620_models.UnbindInstance2VpcRequest,
    ) -> ots_20160620_models.UnbindInstance2VpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_instance_2vpc_with_options(request, runtime)

    async def unbind_instance_2vpc_async(
        self,
        request: ots_20160620_models.UnbindInstance2VpcRequest,
    ) -> ots_20160620_models.UnbindInstance2VpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_instance_2vpc_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: ots_20160620_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: ots_20160620_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ots_20160620_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2016-06-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ots_20160620_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: ots_20160620_models.UpdateInstanceRequest,
    ) -> ots_20160620_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: ots_20160620_models.UpdateInstanceRequest,
    ) -> ots_20160620_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)
