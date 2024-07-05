# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mts20140618 import models as mts_20140618_models
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
            'ap-northeast-2-pop': 'mts.aliyuncs.com',
            'ap-southeast-2': 'mts.aliyuncs.com',
            'ap-southeast-3': 'mts.aliyuncs.com',
            'cn-beijing-finance-1': 'mts.aliyuncs.com',
            'cn-beijing-finance-pop': 'mts.aliyuncs.com',
            'cn-beijing-gov-1': 'mts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mts.aliyuncs.com',
            'cn-chengdu': 'mts.aliyuncs.com',
            'cn-edge-1': 'mts.aliyuncs.com',
            'cn-fujian': 'mts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mts.aliyuncs.com',
            'cn-hangzhou-finance': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mts.aliyuncs.com',
            'cn-hangzhou-test-306': 'mts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'mts.aliyuncs.com',
            'cn-north-2-gov-1': 'mts.aliyuncs.com',
            'cn-qingdao-nebula': 'mts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mts.aliyuncs.com',
            'cn-shanghai-finance-1': 'mts.aliyuncs.com',
            'cn-shanghai-inner': 'mts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mts.aliyuncs.com',
            'cn-shenzhen-inner': 'mts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mts.aliyuncs.com',
            'cn-wuhan': 'mts.aliyuncs.com',
            'cn-wulanchabu': 'mts.aliyuncs.com',
            'cn-yushanfang': 'mts.aliyuncs.com',
            'cn-zhangbei': 'mts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mts.aliyuncs.com',
            'eu-west-1-oxs': 'mts.aliyuncs.com',
            'me-east-1': 'mts.aliyuncs.com',
            'rus-west-1-pop': 'mts.aliyuncs.com',
            'us-east-1': 'mts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_media_workflow_with_options(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        """
        @summary Activates a media workflow.
        
        @description You can call this operation to activate a media workflow that has been deactivated. After you activate a media workflow, you cannot modify the workflow information, such as the name, topology, or trigger mode. A media workflow is activated by default after it is created.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ActivateMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ActivateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        """
        @summary Activates a media workflow.
        
        @description You can call this operation to activate a media workflow that has been deactivated. After you activate a media workflow, you cannot modify the workflow information, such as the name, topology, or trigger mode. A media workflow is activated by default after it is created.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ActivateMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ActivateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_media_workflow(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        """
        @summary Activates a media workflow.
        
        @description You can call this operation to activate a media workflow that has been deactivated. After you activate a media workflow, you cannot modify the workflow information, such as the name, topology, or trigger mode. A media workflow is activated by default after it is created.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ActivateMediaWorkflowRequest
        @return: ActivateMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_media_workflow_with_options(request, runtime)

    async def activate_media_workflow_async(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        """
        @summary Activates a media workflow.
        
        @description You can call this operation to activate a media workflow that has been deactivated. After you activate a media workflow, you cannot modify the workflow information, such as the name, topology, or trigger mode. A media workflow is activated by default after it is created.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ActivateMediaWorkflowRequest
        @return: ActivateMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_media_workflow_with_options_async(request, runtime)

    def add_media_with_options(
        self,
        request: mts_20140618_models.AddMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaResponse:
        """
        @summary Adds a media file.
        
        @description    You can call this operation to process videos that are uploaded to Object Storage Service (OSS) but not processed. This way, you do not need to upload the videos to OSS again. If you have configured media workflows, OSS automatically notifies ApsaraVideo Media Processing (MPS) when a media file is uploaded to OSS. MPS automatically finds the corresponding workflow in the Active state based on the specified OSS bucket and object. Therefore, in most cases, you do not need to manually call the AddMedia operation to process the media file.
        Media information is automatically obtained only when the specified media workflow is in the Active state. If no media workflow is specified or the specified media workflow is not in the Active state, media information is not obtained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_url):
            query['FileURL'] = request.file_url
        if not UtilClient.is_unset(request.input_unbind):
            query['InputUnbind'] = request.input_unbind
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_user_data):
            query['MediaWorkflowUserData'] = request.media_workflow_user_data
        if not UtilClient.is_unset(request.override_params):
            query['OverrideParams'] = request.override_params
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_with_options_async(
        self,
        request: mts_20140618_models.AddMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaResponse:
        """
        @summary Adds a media file.
        
        @description    You can call this operation to process videos that are uploaded to Object Storage Service (OSS) but not processed. This way, you do not need to upload the videos to OSS again. If you have configured media workflows, OSS automatically notifies ApsaraVideo Media Processing (MPS) when a media file is uploaded to OSS. MPS automatically finds the corresponding workflow in the Active state based on the specified OSS bucket and object. Therefore, in most cases, you do not need to manually call the AddMedia operation to process the media file.
        Media information is automatically obtained only when the specified media workflow is in the Active state. If no media workflow is specified or the specified media workflow is not in the Active state, media information is not obtained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_url):
            query['FileURL'] = request.file_url
        if not UtilClient.is_unset(request.input_unbind):
            query['InputUnbind'] = request.input_unbind
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_user_data):
            query['MediaWorkflowUserData'] = request.media_workflow_user_data
        if not UtilClient.is_unset(request.override_params):
            query['OverrideParams'] = request.override_params
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_media(
        self,
        request: mts_20140618_models.AddMediaRequest,
    ) -> mts_20140618_models.AddMediaResponse:
        """
        @summary Adds a media file.
        
        @description    You can call this operation to process videos that are uploaded to Object Storage Service (OSS) but not processed. This way, you do not need to upload the videos to OSS again. If you have configured media workflows, OSS automatically notifies ApsaraVideo Media Processing (MPS) when a media file is uploaded to OSS. MPS automatically finds the corresponding workflow in the Active state based on the specified OSS bucket and object. Therefore, in most cases, you do not need to manually call the AddMedia operation to process the media file.
        Media information is automatically obtained only when the specified media workflow is in the Active state. If no media workflow is specified or the specified media workflow is not in the Active state, media information is not obtained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaRequest
        @return: AddMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_media_with_options(request, runtime)

    async def add_media_async(
        self,
        request: mts_20140618_models.AddMediaRequest,
    ) -> mts_20140618_models.AddMediaResponse:
        """
        @summary Adds a media file.
        
        @description    You can call this operation to process videos that are uploaded to Object Storage Service (OSS) but not processed. This way, you do not need to upload the videos to OSS again. If you have configured media workflows, OSS automatically notifies ApsaraVideo Media Processing (MPS) when a media file is uploaded to OSS. MPS automatically finds the corresponding workflow in the Active state based on the specified OSS bucket and object. Therefore, in most cases, you do not need to manually call the AddMedia operation to process the media file.
        Media information is automatically obtained only when the specified media workflow is in the Active state. If no media workflow is specified or the specified media workflow is not in the Active state, media information is not obtained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaRequest
        @return: AddMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_media_with_options_async(request, runtime)

    def add_media_tag_with_options(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaTagResponse:
        """
        @summary Adds a tag to a media file.
        
        @description You can call this operation to add only one tag. To add multiple tags at a time, you can call the [UpdateMedia](https://help.aliyun.com/document_detail/44464.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMediaTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_tag_with_options_async(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaTagResponse:
        """
        @summary Adds a tag to a media file.
        
        @description You can call this operation to add only one tag. To add multiple tags at a time, you can call the [UpdateMedia](https://help.aliyun.com/document_detail/44464.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMediaTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_media_tag(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
    ) -> mts_20140618_models.AddMediaTagResponse:
        """
        @summary Adds a tag to a media file.
        
        @description You can call this operation to add only one tag. To add multiple tags at a time, you can call the [UpdateMedia](https://help.aliyun.com/document_detail/44464.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaTagRequest
        @return: AddMediaTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_media_tag_with_options(request, runtime)

    async def add_media_tag_async(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
    ) -> mts_20140618_models.AddMediaTagResponse:
        """
        @summary Adds a tag to a media file.
        
        @description You can call this operation to add only one tag. To add multiple tags at a time, you can call the [UpdateMedia](https://help.aliyun.com/document_detail/44464.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaTagRequest
        @return: AddMediaTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_media_tag_with_options_async(request, runtime)

    def add_media_workflow_with_options(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        """
        @summary Creates a media workflow.
        
        @description    You can call this operation to define the topology, activities, and dependencies of a media workflow. The topology is represented by a directed acyclic graph (DAG) in the console. For more information, see [Workflow activities](https://help.aliyun.com/document_detail/68494.html). You can view and run the workflows that are created by calling this operation in the ApsaraVideo Media Processing (MPS) console.
        MPS media workflows can be automatically triggered only by using the prefix of the file path. Automatic triggering by using the suffix is not supported. For more information about the trigger rules, see [Workflow triggering rules for files](https://help.aliyun.com/document_detail/68574.html).
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        """
        @summary Creates a media workflow.
        
        @description    You can call this operation to define the topology, activities, and dependencies of a media workflow. The topology is represented by a directed acyclic graph (DAG) in the console. For more information, see [Workflow activities](https://help.aliyun.com/document_detail/68494.html). You can view and run the workflows that are created by calling this operation in the ApsaraVideo Media Processing (MPS) console.
        MPS media workflows can be automatically triggered only by using the prefix of the file path. Automatic triggering by using the suffix is not supported. For more information about the trigger rules, see [Workflow triggering rules for files](https://help.aliyun.com/document_detail/68574.html).
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_media_workflow(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        """
        @summary Creates a media workflow.
        
        @description    You can call this operation to define the topology, activities, and dependencies of a media workflow. The topology is represented by a directed acyclic graph (DAG) in the console. For more information, see [Workflow activities](https://help.aliyun.com/document_detail/68494.html). You can view and run the workflows that are created by calling this operation in the ApsaraVideo Media Processing (MPS) console.
        MPS media workflows can be automatically triggered only by using the prefix of the file path. Automatic triggering by using the suffix is not supported. For more information about the trigger rules, see [Workflow triggering rules for files](https://help.aliyun.com/document_detail/68574.html).
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaWorkflowRequest
        @return: AddMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_media_workflow_with_options(request, runtime)

    async def add_media_workflow_async(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        """
        @summary Creates a media workflow.
        
        @description    You can call this operation to define the topology, activities, and dependencies of a media workflow. The topology is represented by a directed acyclic graph (DAG) in the console. For more information, see [Workflow activities](https://help.aliyun.com/document_detail/68494.html). You can view and run the workflows that are created by calling this operation in the ApsaraVideo Media Processing (MPS) console.
        MPS media workflows can be automatically triggered only by using the prefix of the file path. Automatic triggering by using the suffix is not supported. For more information about the trigger rules, see [Workflow triggering rules for files](https://help.aliyun.com/document_detail/68574.html).
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddMediaWorkflowRequest
        @return: AddMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_media_workflow_with_options_async(request, runtime)

    def add_pipeline_with_options(
        self,
        request: mts_20140618_models.AddPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPipelineResponse:
        """
        @summary Adds an ApsaraVideo Media Processing (MPS) queue.
        
        @param request: AddPipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.speed_level):
            query['SpeedLevel'] = request.speed_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPipelineResponse:
        """
        @summary Adds an ApsaraVideo Media Processing (MPS) queue.
        
        @param request: AddPipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.speed_level):
            query['SpeedLevel'] = request.speed_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_pipeline(
        self,
        request: mts_20140618_models.AddPipelineRequest,
    ) -> mts_20140618_models.AddPipelineResponse:
        """
        @summary Adds an ApsaraVideo Media Processing (MPS) queue.
        
        @param request: AddPipelineRequest
        @return: AddPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_pipeline_with_options(request, runtime)

    async def add_pipeline_async(
        self,
        request: mts_20140618_models.AddPipelineRequest,
    ) -> mts_20140618_models.AddPipelineResponse:
        """
        @summary Adds an ApsaraVideo Media Processing (MPS) queue.
        
        @param request: AddPipelineRequest
        @return: AddPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_pipeline_with_options_async(request, runtime)

    def add_smarttag_template_with_options(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        """
        @summary 添加labelVersion、knowledgeConfig配置
        
        @param request: AddSmarttagTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSmarttagTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not UtilClient.is_unset(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        """
        @summary 添加labelVersion、knowledgeConfig配置
        
        @param request: AddSmarttagTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSmarttagTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not UtilClient.is_unset(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_smarttag_template(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        """
        @summary 添加labelVersion、knowledgeConfig配置
        
        @param request: AddSmarttagTemplateRequest
        @return: AddSmarttagTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_smarttag_template_with_options(request, runtime)

    async def add_smarttag_template_async(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        """
        @summary 添加labelVersion、knowledgeConfig配置
        
        @param request: AddSmarttagTemplateRequest
        @return: AddSmarttagTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_smarttag_template_with_options_async(request, runtime)

    def add_template_with_options(
        self,
        request: mts_20140618_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTemplateResponse:
        """
        @summary Creates a custom transcoding template. You need to configure the information such as the container format, video stream settings, and audio stream settings.
        
        @description When you call this operation, you need to set transcoding parameters such as those related to the container format, video stream, and audio stream. If you do not specify some parameters, streams that are generated by using the template do not contain the information specified by those parameters.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_template_with_options_async(
        self,
        request: mts_20140618_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTemplateResponse:
        """
        @summary Creates a custom transcoding template. You need to configure the information such as the container format, video stream settings, and audio stream settings.
        
        @description When you call this operation, you need to set transcoding parameters such as those related to the container format, video stream, and audio stream. If you do not specify some parameters, streams that are generated by using the template do not contain the information specified by those parameters.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_template(
        self,
        request: mts_20140618_models.AddTemplateRequest,
    ) -> mts_20140618_models.AddTemplateResponse:
        """
        @summary Creates a custom transcoding template. You need to configure the information such as the container format, video stream settings, and audio stream settings.
        
        @description When you call this operation, you need to set transcoding parameters such as those related to the container format, video stream, and audio stream. If you do not specify some parameters, streams that are generated by using the template do not contain the information specified by those parameters.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddTemplateRequest
        @return: AddTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_template_with_options(request, runtime)

    async def add_template_async(
        self,
        request: mts_20140618_models.AddTemplateRequest,
    ) -> mts_20140618_models.AddTemplateResponse:
        """
        @summary Creates a custom transcoding template. You need to configure the information such as the container format, video stream settings, and audio stream settings.
        
        @description When you call this operation, you need to set transcoding parameters such as those related to the container format, video stream, and audio stream. If you do not specify some parameters, streams that are generated by using the template do not contain the information specified by those parameters.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddTemplateRequest
        @return: AddTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_template_with_options_async(request, runtime)

    def add_water_mark_template_with_options(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        """
        @summary Creates a watermark template.
        
        @description After you create a watermark template by calling this operation, you can specify the watermark template and watermark asset when you [submit a transcoding job](https://help.aliyun.com/document_detail/29226.html). This allows you to add watermark information to the output video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddWaterMarkTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        """
        @summary Creates a watermark template.
        
        @description After you create a watermark template by calling this operation, you can specify the watermark template and watermark asset when you [submit a transcoding job](https://help.aliyun.com/document_detail/29226.html). This allows you to add watermark information to the output video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddWaterMarkTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_water_mark_template(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        """
        @summary Creates a watermark template.
        
        @description After you create a watermark template by calling this operation, you can specify the watermark template and watermark asset when you [submit a transcoding job](https://help.aliyun.com/document_detail/29226.html). This allows you to add watermark information to the output video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddWaterMarkTemplateRequest
        @return: AddWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_water_mark_template_with_options(request, runtime)

    async def add_water_mark_template_async(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        """
        @summary Creates a watermark template.
        
        @description After you create a watermark template by calling this operation, you can specify the watermark template and watermark asset when you [submit a transcoding job](https://help.aliyun.com/document_detail/29226.html). This allows you to add watermark information to the output video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: AddWaterMarkTemplateRequest
        @return: AddWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_water_mark_template_with_options_async(request, runtime)

    def bind_input_bucket_with_options(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindInputBucketResponse:
        """
        @summary Binds an input media bucket.
        
        @description Before you call this operation to bind an input media bucket, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindInputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindInputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_input_bucket_with_options_async(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindInputBucketResponse:
        """
        @summary Binds an input media bucket.
        
        @description Before you call this operation to bind an input media bucket, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindInputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindInputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindInputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_input_bucket(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
    ) -> mts_20140618_models.BindInputBucketResponse:
        """
        @summary Binds an input media bucket.
        
        @description Before you call this operation to bind an input media bucket, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindInputBucketRequest
        @return: BindInputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_input_bucket_with_options(request, runtime)

    async def bind_input_bucket_async(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
    ) -> mts_20140618_models.BindInputBucketResponse:
        """
        @summary Binds an input media bucket.
        
        @description Before you call this operation to bind an input media bucket, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindInputBucketRequest
        @return: BindInputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_input_bucket_with_options_async(request, runtime)

    def bind_output_bucket_with_options(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        """
        @summary Binds an output media bucket to the media library.
        
        @description Before you call this operation to bind an output media bucket to the media library, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindOutputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindOutputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindOutputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_output_bucket_with_options_async(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        """
        @summary Binds an output media bucket to the media library.
        
        @description Before you call this operation to bind an output media bucket to the media library, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindOutputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindOutputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindOutputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_output_bucket(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        """
        @summary Binds an output media bucket to the media library.
        
        @description Before you call this operation to bind an output media bucket to the media library, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindOutputBucketRequest
        @return: BindOutputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_output_bucket_with_options(request, runtime)

    async def bind_output_bucket_async(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        """
        @summary Binds an output media bucket to the media library.
        
        @description Before you call this operation to bind an output media bucket to the media library, you must create a media bucket. For more information, see [Add media buckets](https://help.aliyun.com/document_detail/42430.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: BindOutputBucketRequest
        @return: BindOutputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_output_bucket_with_options_async(request, runtime)

    def cancel_job_with_options(
        self,
        request: mts_20140618_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CancelJobResponse:
        """
        @summary Cancels a transcoding job.
        
        @description    You can cancel a transcoding job only if the job is in the Submitted state.
        We recommend that you call the **UpdatePipeline** operation to set the status of the ApsaraVideo Media Processing (MPS) queue to Paused before you cancel a job. This suspends job scheduling in the MPS queue. After the job is canceled, you must set the status of the MPS queue back to Active so that the other jobs in the MPS queue can be scheduled.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CancelJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CancelJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_job_with_options_async(
        self,
        request: mts_20140618_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CancelJobResponse:
        """
        @summary Cancels a transcoding job.
        
        @description    You can cancel a transcoding job only if the job is in the Submitted state.
        We recommend that you call the **UpdatePipeline** operation to set the status of the ApsaraVideo Media Processing (MPS) queue to Paused before you cancel a job. This suspends job scheduling in the MPS queue. After the job is canceled, you must set the status of the MPS queue back to Active so that the other jobs in the MPS queue can be scheduled.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CancelJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CancelJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_job(
        self,
        request: mts_20140618_models.CancelJobRequest,
    ) -> mts_20140618_models.CancelJobResponse:
        """
        @summary Cancels a transcoding job.
        
        @description    You can cancel a transcoding job only if the job is in the Submitted state.
        We recommend that you call the **UpdatePipeline** operation to set the status of the ApsaraVideo Media Processing (MPS) queue to Paused before you cancel a job. This suspends job scheduling in the MPS queue. After the job is canceled, you must set the status of the MPS queue back to Active so that the other jobs in the MPS queue can be scheduled.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CancelJobRequest
        @return: CancelJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    async def cancel_job_async(
        self,
        request: mts_20140618_models.CancelJobRequest,
    ) -> mts_20140618_models.CancelJobResponse:
        """
        @summary Cancels a transcoding job.
        
        @description    You can cancel a transcoding job only if the job is in the Submitted state.
        We recommend that you call the **UpdatePipeline** operation to set the status of the ApsaraVideo Media Processing (MPS) queue to Paused before you cancel a job. This suspends job scheduling in the MPS queue. After the job is canceled, you must set the status of the MPS queue back to Active so that the other jobs in the MPS queue can be scheduled.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CancelJobRequest
        @return: CancelJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_job_with_options_async(request, runtime)

    def create_custom_entity_with_options(
        self,
        request: mts_20140618_models.CreateCustomEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateCustomEntityResponse:
        """
        @param request: CreateCustomEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_info):
            query['CustomEntityInfo'] = request.custom_entity_info
        if not UtilClient.is_unset(request.custom_entity_name):
            query['CustomEntityName'] = request.custom_entity_name
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomEntity',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateCustomEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_entity_with_options_async(
        self,
        request: mts_20140618_models.CreateCustomEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateCustomEntityResponse:
        """
        @param request: CreateCustomEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_info):
            query['CustomEntityInfo'] = request.custom_entity_info
        if not UtilClient.is_unset(request.custom_entity_name):
            query['CustomEntityName'] = request.custom_entity_name
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomEntity',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateCustomEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_entity(
        self,
        request: mts_20140618_models.CreateCustomEntityRequest,
    ) -> mts_20140618_models.CreateCustomEntityResponse:
        """
        @param request: CreateCustomEntityRequest
        @return: CreateCustomEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_entity_with_options(request, runtime)

    async def create_custom_entity_async(
        self,
        request: mts_20140618_models.CreateCustomEntityRequest,
    ) -> mts_20140618_models.CreateCustomEntityResponse:
        """
        @param request: CreateCustomEntityRequest
        @return: CreateCustomEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_entity_with_options_async(request, runtime)

    def create_custom_group_with_options(
        self,
        request: mts_20140618_models.CreateCustomGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateCustomGroupResponse:
        """
        @param request: CreateCustomGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_group_description):
            query['CustomGroupDescription'] = request.custom_group_description
        if not UtilClient.is_unset(request.custom_group_name):
            query['CustomGroupName'] = request.custom_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomGroup',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateCustomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_group_with_options_async(
        self,
        request: mts_20140618_models.CreateCustomGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateCustomGroupResponse:
        """
        @param request: CreateCustomGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_group_description):
            query['CustomGroupDescription'] = request.custom_group_description
        if not UtilClient.is_unset(request.custom_group_name):
            query['CustomGroupName'] = request.custom_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomGroup',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateCustomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_group(
        self,
        request: mts_20140618_models.CreateCustomGroupRequest,
    ) -> mts_20140618_models.CreateCustomGroupResponse:
        """
        @param request: CreateCustomGroupRequest
        @return: CreateCustomGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_group_with_options(request, runtime)

    async def create_custom_group_async(
        self,
        request: mts_20140618_models.CreateCustomGroupRequest,
    ) -> mts_20140618_models.CreateCustomGroupResponse:
        """
        @param request: CreateCustomGroupRequest
        @return: CreateCustomGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_group_with_options_async(request, runtime)

    def create_fp_shot_dbwith_options(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        """
        @summary Submits a job of creating a media fingerprint library.
        
        @description    You can call this operation to submit a job to create a video or text fingerprint library. You can use a text fingerprint library to store fingerprints for text.
        You can submit a job of creating a text fingerprint library only in the China (Shanghai) region.
        By default, you can submit up to 10 jobs of creating a video fingerprint library to an ApsaraVideo Media Processing (MPS) queue at a time. If you submit more than 10 jobs at a time, the call may fail.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CreateFpShotDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFpShotDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateFpShotDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fp_shot_dbwith_options_async(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        """
        @summary Submits a job of creating a media fingerprint library.
        
        @description    You can call this operation to submit a job to create a video or text fingerprint library. You can use a text fingerprint library to store fingerprints for text.
        You can submit a job of creating a text fingerprint library only in the China (Shanghai) region.
        By default, you can submit up to 10 jobs of creating a video fingerprint library to an ApsaraVideo Media Processing (MPS) queue at a time. If you submit more than 10 jobs at a time, the call may fail.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CreateFpShotDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFpShotDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateFpShotDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fp_shot_db(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        """
        @summary Submits a job of creating a media fingerprint library.
        
        @description    You can call this operation to submit a job to create a video or text fingerprint library. You can use a text fingerprint library to store fingerprints for text.
        You can submit a job of creating a text fingerprint library only in the China (Shanghai) region.
        By default, you can submit up to 10 jobs of creating a video fingerprint library to an ApsaraVideo Media Processing (MPS) queue at a time. If you submit more than 10 jobs at a time, the call may fail.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CreateFpShotDBRequest
        @return: CreateFpShotDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_fp_shot_dbwith_options(request, runtime)

    async def create_fp_shot_db_async(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        """
        @summary Submits a job of creating a media fingerprint library.
        
        @description    You can call this operation to submit a job to create a video or text fingerprint library. You can use a text fingerprint library to store fingerprints for text.
        You can submit a job of creating a text fingerprint library only in the China (Shanghai) region.
        By default, you can submit up to 10 jobs of creating a video fingerprint library to an ApsaraVideo Media Processing (MPS) queue at a time. If you submit more than 10 jobs at a time, the call may fail.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: CreateFpShotDBRequest
        @return: CreateFpShotDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_fp_shot_dbwith_options_async(request, runtime)

    def deactivate_media_workflow_with_options(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        """
        @summary Disables a media workflow.
        
        @description The time when the media workflow was created.
        
        @param request: DeactivateMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactivateMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeactivateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        """
        @summary Disables a media workflow.
        
        @description The time when the media workflow was created.
        
        @param request: DeactivateMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactivateMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeactivateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactivate_media_workflow(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        """
        @summary Disables a media workflow.
        
        @description The time when the media workflow was created.
        
        @param request: DeactivateMediaWorkflowRequest
        @return: DeactivateMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deactivate_media_workflow_with_options(request, runtime)

    async def deactivate_media_workflow_async(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        """
        @summary Disables a media workflow.
        
        @description The time when the media workflow was created.
        
        @param request: DeactivateMediaWorkflowRequest
        @return: DeactivateMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deactivate_media_workflow_with_options_async(request, runtime)

    def delete_custom_entity_with_options(
        self,
        request: mts_20140618_models.DeleteCustomEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCustomEntityResponse:
        """
        @summary Deletes a custom entity from a custom library.
        
        @param request: DeleteCustomEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomEntity',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCustomEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_entity_with_options_async(
        self,
        request: mts_20140618_models.DeleteCustomEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCustomEntityResponse:
        """
        @summary Deletes a custom entity from a custom library.
        
        @param request: DeleteCustomEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomEntity',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCustomEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_entity(
        self,
        request: mts_20140618_models.DeleteCustomEntityRequest,
    ) -> mts_20140618_models.DeleteCustomEntityResponse:
        """
        @summary Deletes a custom entity from a custom library.
        
        @param request: DeleteCustomEntityRequest
        @return: DeleteCustomEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_entity_with_options(request, runtime)

    async def delete_custom_entity_async(
        self,
        request: mts_20140618_models.DeleteCustomEntityRequest,
    ) -> mts_20140618_models.DeleteCustomEntityResponse:
        """
        @summary Deletes a custom entity from a custom library.
        
        @param request: DeleteCustomEntityRequest
        @return: DeleteCustomEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_entity_with_options_async(request, runtime)

    def delete_custom_group_with_options(
        self,
        request: mts_20140618_models.DeleteCustomGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCustomGroupResponse:
        """
        @summary Delete a custom image library.
        
        @description You can call this operation only in the China (Beijing), China (Shanghai), and China (Hangzhou) regions.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteCustomGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomGroup',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCustomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_group_with_options_async(
        self,
        request: mts_20140618_models.DeleteCustomGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCustomGroupResponse:
        """
        @summary Delete a custom image library.
        
        @description You can call this operation only in the China (Beijing), China (Shanghai), and China (Hangzhou) regions.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteCustomGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomGroup',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCustomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_group(
        self,
        request: mts_20140618_models.DeleteCustomGroupRequest,
    ) -> mts_20140618_models.DeleteCustomGroupResponse:
        """
        @summary Delete a custom image library.
        
        @description You can call this operation only in the China (Beijing), China (Shanghai), and China (Hangzhou) regions.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteCustomGroupRequest
        @return: DeleteCustomGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_group_with_options(request, runtime)

    async def delete_custom_group_async(
        self,
        request: mts_20140618_models.DeleteCustomGroupRequest,
    ) -> mts_20140618_models.DeleteCustomGroupResponse:
        """
        @summary Delete a custom image library.
        
        @description You can call this operation only in the China (Beijing), China (Shanghai), and China (Hangzhou) regions.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteCustomGroupRequest
        @return: DeleteCustomGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_group_with_options_async(request, runtime)

    def delete_custom_view_with_options(
        self,
        request: mts_20140618_models.DeleteCustomViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCustomViewResponse:
        """
        @param request: DeleteCustomViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.custom_view_id):
            query['CustomViewId'] = request.custom_view_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomView',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCustomViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_view_with_options_async(
        self,
        request: mts_20140618_models.DeleteCustomViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCustomViewResponse:
        """
        @param request: DeleteCustomViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.custom_view_id):
            query['CustomViewId'] = request.custom_view_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomView',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCustomViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_view(
        self,
        request: mts_20140618_models.DeleteCustomViewRequest,
    ) -> mts_20140618_models.DeleteCustomViewResponse:
        """
        @param request: DeleteCustomViewRequest
        @return: DeleteCustomViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_view_with_options(request, runtime)

    async def delete_custom_view_async(
        self,
        request: mts_20140618_models.DeleteCustomViewRequest,
    ) -> mts_20140618_models.DeleteCustomViewResponse:
        """
        @param request: DeleteCustomViewRequest
        @return: DeleteCustomViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_view_with_options_async(request, runtime)

    def delete_media_with_options(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaResponse:
        """
        @summary Deletes media files from ApsaraVideo Media Processing (MPS).
        
        @description This operation allows you to logically delete a media file. The media file can no longer be processed, but the corresponding objects in the input and output Object Storage Service (OSS) buckets are retained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaResponse:
        """
        @summary Deletes media files from ApsaraVideo Media Processing (MPS).
        
        @description This operation allows you to logically delete a media file. The media file can no longer be processed, but the corresponding objects in the input and output Object Storage Service (OSS) buckets are retained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_media(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
    ) -> mts_20140618_models.DeleteMediaResponse:
        """
        @summary Deletes media files from ApsaraVideo Media Processing (MPS).
        
        @description This operation allows you to logically delete a media file. The media file can no longer be processed, but the corresponding objects in the input and output Object Storage Service (OSS) buckets are retained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaRequest
        @return: DeleteMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_media_with_options(request, runtime)

    async def delete_media_async(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
    ) -> mts_20140618_models.DeleteMediaResponse:
        """
        @summary Deletes media files from ApsaraVideo Media Processing (MPS).
        
        @description This operation allows you to logically delete a media file. The media file can no longer be processed, but the corresponding objects in the input and output Object Storage Service (OSS) buckets are retained.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaRequest
        @return: DeleteMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_with_options_async(request, runtime)

    def delete_media_tag_with_options(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        """
        @summary Removes a tag for a media file.
        
        @description You can call this operation to remove only one tag at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMediaTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_tag_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        """
        @summary Removes a tag for a media file.
        
        @description You can call this operation to remove only one tag at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMediaTagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_media_tag(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        """
        @summary Removes a tag for a media file.
        
        @description You can call this operation to remove only one tag at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaTagRequest
        @return: DeleteMediaTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_media_tag_with_options(request, runtime)

    async def delete_media_tag_async(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        """
        @summary Removes a tag for a media file.
        
        @description You can call this operation to remove only one tag at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaTagRequest
        @return: DeleteMediaTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_tag_with_options_async(request, runtime)

    def delete_media_workflow_with_options(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        """
        @summary Deletes a media workflow. This does not affect workflow instances that are running.
        
        @description After you delete or disable a workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        """
        @summary Deletes a media workflow. This does not affect workflow instances that are running.
        
        @description After you delete or disable a workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_media_workflow(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        """
        @summary Deletes a media workflow. This does not affect workflow instances that are running.
        
        @description After you delete or disable a workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaWorkflowRequest
        @return: DeleteMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_media_workflow_with_options(request, runtime)

    async def delete_media_workflow_async(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        """
        @summary Deletes a media workflow. This does not affect workflow instances that are running.
        
        @description After you delete or disable a workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteMediaWorkflowRequest
        @return: DeleteMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_workflow_with_options_async(request, runtime)

    def delete_pipeline_with_options(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeletePipelineResponse:
        """
        @summary Deletes an ApsaraVideo Media Processing (MPS) queue.
        
        @description You can call this operation to delete only one MPS queue at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeletePipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeletePipelineResponse:
        """
        @summary Deletes an ApsaraVideo Media Processing (MPS) queue.
        
        @description You can call this operation to delete only one MPS queue at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeletePipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
    ) -> mts_20140618_models.DeletePipelineResponse:
        """
        @summary Deletes an ApsaraVideo Media Processing (MPS) queue.
        
        @description You can call this operation to delete only one MPS queue at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeletePipelineRequest
        @return: DeletePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_pipeline_with_options(request, runtime)

    async def delete_pipeline_async(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
    ) -> mts_20140618_models.DeletePipelineResponse:
        """
        @summary Deletes an ApsaraVideo Media Processing (MPS) queue.
        
        @description You can call this operation to delete only one MPS queue at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeletePipelineRequest
        @return: DeletePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_pipeline_with_options_async(request, runtime)

    def delete_smarttag_template_with_options(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        """
        @summary Deletes a template.
        
        @description You can call this operation to delete only one template at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteSmarttagTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmarttagTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        """
        @summary Deletes a template.
        
        @description You can call this operation to delete only one template at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteSmarttagTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSmarttagTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_smarttag_template(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        """
        @summary Deletes a template.
        
        @description You can call this operation to delete only one template at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteSmarttagTemplateRequest
        @return: DeleteSmarttagTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_smarttag_template_with_options(request, runtime)

    async def delete_smarttag_template_async(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        """
        @summary Deletes a template.
        
        @description You can call this operation to delete only one template at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteSmarttagTemplateRequest
        @return: DeleteSmarttagTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_smarttag_template_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        """
        @summary Deletes a custom transcoding template.
        
        @description A custom transcoding template cannot be deleted if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        """
        @summary Deletes a custom transcoding template.
        
        @description A custom transcoding template cannot be deleted if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        """
        @summary Deletes a custom transcoding template.
        
        @description A custom transcoding template cannot be deleted if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        """
        @summary Deletes a custom transcoding template.
        
        @description A custom transcoding template cannot be deleted if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_water_mark_template_with_options(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        """
        @summary Deletes a watermark template.
        
        @description A watermark template cannot be deleted if it is being used by a submitted job.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaterMarkTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        """
        @summary Deletes a watermark template.
        
        @description A watermark template cannot be deleted if it is being used by a submitted job.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaterMarkTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_water_mark_template(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        """
        @summary Deletes a watermark template.
        
        @description A watermark template cannot be deleted if it is being used by a submitted job.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteWaterMarkTemplateRequest
        @return: DeleteWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_water_mark_template_with_options(request, runtime)

    async def delete_water_mark_template_async(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        """
        @summary Deletes a watermark template.
        
        @description A watermark template cannot be deleted if it is being used by a submitted job.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: DeleteWaterMarkTemplateRequest
        @return: DeleteWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_water_mark_template_with_options_async(request, runtime)

    def im_audit_with_options(
        self,
        request: mts_20140618_models.ImAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImAuditResponse:
        """
        @summary Reviews images and text and returns the review results.
        
        @description    The moderation results are synchronously returned after the moderation is complete.
        You can use the image and text moderation feature only in the China (Beijing), China (Shanghai), and Singapore regions.
        ### QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.contents):
            query['Contents'] = request.contents
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scenes):
            query['Scenes'] = request.scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImAudit',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def im_audit_with_options_async(
        self,
        request: mts_20140618_models.ImAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImAuditResponse:
        """
        @summary Reviews images and text and returns the review results.
        
        @description    The moderation results are synchronously returned after the moderation is complete.
        You can use the image and text moderation feature only in the China (Beijing), China (Shanghai), and Singapore regions.
        ### QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImAuditResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.contents):
            query['Contents'] = request.contents
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scenes):
            query['Scenes'] = request.scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImAudit',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def im_audit(
        self,
        request: mts_20140618_models.ImAuditRequest,
    ) -> mts_20140618_models.ImAuditResponse:
        """
        @summary Reviews images and text and returns the review results.
        
        @description    The moderation results are synchronously returned after the moderation is complete.
        You can use the image and text moderation feature only in the China (Beijing), China (Shanghai), and Singapore regions.
        ### QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImAuditRequest
        @return: ImAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.im_audit_with_options(request, runtime)

    async def im_audit_async(
        self,
        request: mts_20140618_models.ImAuditRequest,
    ) -> mts_20140618_models.ImAuditResponse:
        """
        @summary Reviews images and text and returns the review results.
        
        @description    The moderation results are synchronously returned after the moderation is complete.
        You can use the image and text moderation feature only in the China (Beijing), China (Shanghai), and Singapore regions.
        ### QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImAuditRequest
        @return: ImAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.im_audit_with_options_async(request, runtime)

    def import_fp_shot_job_with_options(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        """
        @summary Submits a job of importing text files to a text fingerprint library.
        
        @description    You can call this operation to import multiple text files to a text fingerprint library at a time. The system extracts fingerprints from the text files and saves the fingerprints to the text fingerprint library.
        You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImportFpShotJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportFpShotJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.fp_import_config):
            query['FpImportConfig'] = request.fp_import_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImportFpShotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_fp_shot_job_with_options_async(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        """
        @summary Submits a job of importing text files to a text fingerprint library.
        
        @description    You can call this operation to import multiple text files to a text fingerprint library at a time. The system extracts fingerprints from the text files and saves the fingerprints to the text fingerprint library.
        You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImportFpShotJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportFpShotJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.fp_import_config):
            query['FpImportConfig'] = request.fp_import_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImportFpShotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_fp_shot_job(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        """
        @summary Submits a job of importing text files to a text fingerprint library.
        
        @description    You can call this operation to import multiple text files to a text fingerprint library at a time. The system extracts fingerprints from the text files and saves the fingerprints to the text fingerprint library.
        You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImportFpShotJobRequest
        @return: ImportFpShotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_fp_shot_job_with_options(request, runtime)

    async def import_fp_shot_job_async(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        """
        @summary Submits a job of importing text files to a text fingerprint library.
        
        @description    You can call this operation to import multiple text files to a text fingerprint library at a time. The system extracts fingerprints from the text files and saves the fingerprints to the text fingerprint library.
        You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ImportFpShotJobRequest
        @return: ImportFpShotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_fp_shot_job_with_options_async(request, runtime)

    def list_all_media_bucket_with_options(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        """
        @summary Queries all media buckets bound to the media library.
        
        @description A maximum of 100 media buckets can be returned.
        ### QPS limit
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListAllMediaBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllMediaBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllMediaBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAllMediaBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_media_bucket_with_options_async(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        """
        @summary Queries all media buckets bound to the media library.
        
        @description A maximum of 100 media buckets can be returned.
        ### QPS limit
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListAllMediaBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAllMediaBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllMediaBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAllMediaBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_media_bucket(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        """
        @summary Queries all media buckets bound to the media library.
        
        @description A maximum of 100 media buckets can be returned.
        ### QPS limit
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListAllMediaBucketRequest
        @return: ListAllMediaBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_all_media_bucket_with_options(request, runtime)

    async def list_all_media_bucket_async(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        """
        @summary Queries all media buckets bound to the media library.
        
        @description A maximum of 100 media buckets can be returned.
        ### QPS limit
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListAllMediaBucketRequest
        @return: ListAllMediaBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_all_media_bucket_with_options_async(request, runtime)

    def list_custom_entities_with_options(
        self,
        request: mts_20140618_models.ListCustomEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomEntitiesResponse:
        """
        @summary Queries a list of entities in a custom library.
        
        @param request: ListCustomEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomEntities',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_entities_with_options_async(
        self,
        request: mts_20140618_models.ListCustomEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomEntitiesResponse:
        """
        @summary Queries a list of entities in a custom library.
        
        @param request: ListCustomEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomEntitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomEntities',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_entities(
        self,
        request: mts_20140618_models.ListCustomEntitiesRequest,
    ) -> mts_20140618_models.ListCustomEntitiesResponse:
        """
        @summary Queries a list of entities in a custom library.
        
        @param request: ListCustomEntitiesRequest
        @return: ListCustomEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_entities_with_options(request, runtime)

    async def list_custom_entities_async(
        self,
        request: mts_20140618_models.ListCustomEntitiesRequest,
    ) -> mts_20140618_models.ListCustomEntitiesResponse:
        """
        @summary Queries a list of entities in a custom library.
        
        @param request: ListCustomEntitiesRequest
        @return: ListCustomEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_entities_with_options_async(request, runtime)

    def list_custom_groups_with_options(
        self,
        request: mts_20140618_models.ListCustomGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomGroupsResponse:
        """
        @param request: ListCustomGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomGroups',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_groups_with_options_async(
        self,
        request: mts_20140618_models.ListCustomGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomGroupsResponse:
        """
        @param request: ListCustomGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomGroups',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_groups(
        self,
        request: mts_20140618_models.ListCustomGroupsRequest,
    ) -> mts_20140618_models.ListCustomGroupsResponse:
        """
        @param request: ListCustomGroupsRequest
        @return: ListCustomGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_groups_with_options(request, runtime)

    async def list_custom_groups_async(
        self,
        request: mts_20140618_models.ListCustomGroupsRequest,
    ) -> mts_20140618_models.ListCustomGroupsResponse:
        """
        @param request: ListCustomGroupsRequest
        @return: ListCustomGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_groups_with_options_async(request, runtime)

    def list_custom_persons_with_options(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        """
        @summary Queries the information about all figures and faces in a specific figure library.
        
        @description You can specify the ID of a figure or a figure library to query the corresponding information. If neither the figure ID nor figure library ID is specified, the operation returns the information about all figures and faces in all figure libraries within the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListCustomPersonsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomPersonsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPersons',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomPersonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_persons_with_options_async(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        """
        @summary Queries the information about all figures and faces in a specific figure library.
        
        @description You can specify the ID of a figure or a figure library to query the corresponding information. If neither the figure ID nor figure library ID is specified, the operation returns the information about all figures and faces in all figure libraries within the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListCustomPersonsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomPersonsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPersons',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomPersonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_persons(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        """
        @summary Queries the information about all figures and faces in a specific figure library.
        
        @description You can specify the ID of a figure or a figure library to query the corresponding information. If neither the figure ID nor figure library ID is specified, the operation returns the information about all figures and faces in all figure libraries within the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListCustomPersonsRequest
        @return: ListCustomPersonsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_persons_with_options(request, runtime)

    async def list_custom_persons_async(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        """
        @summary Queries the information about all figures and faces in a specific figure library.
        
        @description You can specify the ID of a figure or a figure library to query the corresponding information. If neither the figure ID nor figure library ID is specified, the operation returns the information about all figures and faces in all figure libraries within the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListCustomPersonsRequest
        @return: ListCustomPersonsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_persons_with_options_async(request, runtime)

    def list_custom_views_with_options(
        self,
        request: mts_20140618_models.ListCustomViewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomViewsResponse:
        """
        @param request: ListCustomViewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomViewsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomViews',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_views_with_options_async(
        self,
        request: mts_20140618_models.ListCustomViewsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomViewsResponse:
        """
        @param request: ListCustomViewsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomViewsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomViews',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_views(
        self,
        request: mts_20140618_models.ListCustomViewsRequest,
    ) -> mts_20140618_models.ListCustomViewsResponse:
        """
        @param request: ListCustomViewsRequest
        @return: ListCustomViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_views_with_options(request, runtime)

    async def list_custom_views_async(
        self,
        request: mts_20140618_models.ListCustomViewsRequest,
    ) -> mts_20140618_models.ListCustomViewsResponse:
        """
        @param request: ListCustomViewsRequest
        @return: ListCustomViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_views_with_options_async(request, runtime)

    def list_fp_shot_dbwith_options(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        """
        @summary Queries media fingerprint libraries.
        
        @description    You can call this operation to query the status and information about the media fingerprint libraries based on the specified IDs.
        You can query text fingerprint libraries only in the China (Shanghai) region.
        You can call this operation to query up to 10 media fingerprint libraries.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFpShotDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fp_dbids):
            query['FpDBIds'] = request.fp_dbids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_dbwith_options_async(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        """
        @summary Queries media fingerprint libraries.
        
        @description    You can call this operation to query the status and information about the media fingerprint libraries based on the specified IDs.
        You can query text fingerprint libraries only in the China (Shanghai) region.
        You can call this operation to query up to 10 media fingerprint libraries.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFpShotDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fp_dbids):
            query['FpDBIds'] = request.fp_dbids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fp_shot_db(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        """
        @summary Queries media fingerprint libraries.
        
        @description    You can call this operation to query the status and information about the media fingerprint libraries based on the specified IDs.
        You can query text fingerprint libraries only in the China (Shanghai) region.
        You can call this operation to query up to 10 media fingerprint libraries.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotDBRequest
        @return: ListFpShotDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fp_shot_dbwith_options(request, runtime)

    async def list_fp_shot_db_async(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        """
        @summary Queries media fingerprint libraries.
        
        @description    You can call this operation to query the status and information about the media fingerprint libraries based on the specified IDs.
        You can query text fingerprint libraries only in the China (Shanghai) region.
        You can call this operation to query up to 10 media fingerprint libraries.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotDBRequest
        @return: ListFpShotDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fp_shot_dbwith_options_async(request, runtime)

    def list_fp_shot_files_with_options(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        """
        @summary Queries media files in a media fingerprint library.
        
        @description    You can call this operation to query media files in a specific media fingerprint library based on the library ID. This operation supports paged queries.
        You can call this operation only in the China (Beijing), China (Hangzhou), China (Shanghai), and Singapore regions.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFpShotFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotFiles',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_files_with_options_async(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        """
        @summary Queries media files in a media fingerprint library.
        
        @description    You can call this operation to query media files in a specific media fingerprint library based on the library ID. This operation supports paged queries.
        You can call this operation only in the China (Beijing), China (Hangzhou), China (Shanghai), and Singapore regions.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFpShotFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotFiles',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fp_shot_files(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        """
        @summary Queries media files in a media fingerprint library.
        
        @description    You can call this operation to query media files in a specific media fingerprint library based on the library ID. This operation supports paged queries.
        You can call this operation only in the China (Beijing), China (Hangzhou), China (Shanghai), and Singapore regions.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotFilesRequest
        @return: ListFpShotFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fp_shot_files_with_options(request, runtime)

    async def list_fp_shot_files_async(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        """
        @summary Queries media files in a media fingerprint library.
        
        @description    You can call this operation to query media files in a specific media fingerprint library based on the library ID. This operation supports paged queries.
        You can call this operation only in the China (Beijing), China (Hangzhou), China (Shanghai), and Singapore regions.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotFilesRequest
        @return: ListFpShotFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fp_shot_files_with_options_async(request, runtime)

    def list_fp_shot_import_job_with_options(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        """
        @summary Queries jobs of importing text files to a text fingerprint library.
        
        @description You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotImportJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFpShotImportJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotImportJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotImportJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_import_job_with_options_async(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        """
        @summary Queries jobs of importing text files to a text fingerprint library.
        
        @description You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotImportJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFpShotImportJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotImportJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotImportJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fp_shot_import_job(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        """
        @summary Queries jobs of importing text files to a text fingerprint library.
        
        @description You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotImportJobRequest
        @return: ListFpShotImportJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fp_shot_import_job_with_options(request, runtime)

    async def list_fp_shot_import_job_async(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        """
        @summary Queries jobs of importing text files to a text fingerprint library.
        
        @description You can call this operation only in the China (Shanghai) region.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListFpShotImportJobRequest
        @return: ListFpShotImportJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fp_shot_import_job_with_options_async(request, runtime)

    def list_job_with_options(
        self,
        request: mts_20140618_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListJobResponse:
        """
        @summary Traverses transcoding jobs
        
        @description    By default, the returned transcoding jobs are sorted by CreationTime in descending order.
        You can call this operation to return transcoding jobs of the last 90 days. The jobs are returned based on the specified time range.
        You can filter query results by configuring request parameters such as job status, creation time interval, and ApsaraVideo Media Processing (MPS) queue for transcoding.
        By default, MPS does not allow you to access data across regions within the same account. Before you call this operation, make sure that the region that you specify is the same as the region of the transcoding jobs to be queried. Otherwise, this operation may fail to be called, or invalid information may be returned.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_with_options_async(
        self,
        request: mts_20140618_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListJobResponse:
        """
        @summary Traverses transcoding jobs
        
        @description    By default, the returned transcoding jobs are sorted by CreationTime in descending order.
        You can call this operation to return transcoding jobs of the last 90 days. The jobs are returned based on the specified time range.
        You can filter query results by configuring request parameters such as job status, creation time interval, and ApsaraVideo Media Processing (MPS) queue for transcoding.
        By default, MPS does not allow you to access data across regions within the same account. Before you call this operation, make sure that the region that you specify is the same as the region of the transcoding jobs to be queried. Otherwise, this operation may fail to be called, or invalid information may be returned.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job(
        self,
        request: mts_20140618_models.ListJobRequest,
    ) -> mts_20140618_models.ListJobResponse:
        """
        @summary Traverses transcoding jobs
        
        @description    By default, the returned transcoding jobs are sorted by CreationTime in descending order.
        You can call this operation to return transcoding jobs of the last 90 days. The jobs are returned based on the specified time range.
        You can filter query results by configuring request parameters such as job status, creation time interval, and ApsaraVideo Media Processing (MPS) queue for transcoding.
        By default, MPS does not allow you to access data across regions within the same account. Before you call this operation, make sure that the region that you specify is the same as the region of the transcoding jobs to be queried. Otherwise, this operation may fail to be called, or invalid information may be returned.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListJobRequest
        @return: ListJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_job_with_options(request, runtime)

    async def list_job_async(
        self,
        request: mts_20140618_models.ListJobRequest,
    ) -> mts_20140618_models.ListJobResponse:
        """
        @summary Traverses transcoding jobs
        
        @description    By default, the returned transcoding jobs are sorted by CreationTime in descending order.
        You can call this operation to return transcoding jobs of the last 90 days. The jobs are returned based on the specified time range.
        You can filter query results by configuring request parameters such as job status, creation time interval, and ApsaraVideo Media Processing (MPS) queue for transcoding.
        By default, MPS does not allow you to access data across regions within the same account. Before you call this operation, make sure that the region that you specify is the same as the region of the transcoding jobs to be queried. Otherwise, this operation may fail to be called, or invalid information may be returned.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListJobRequest
        @return: ListJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_job_with_options_async(request, runtime)

    def list_media_workflow_executions_with_options(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        """
        @summary Queries the execution instances of a media workflow.
        
        @description This operation returns execution instances only in the recent 90 days.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListMediaWorkflowExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMediaWorkflowExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_file_url):
            query['InputFileURL'] = request.input_file_url
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_name):
            query['MediaWorkflowName'] = request.media_workflow_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaWorkflowExecutions',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListMediaWorkflowExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_media_workflow_executions_with_options_async(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        """
        @summary Queries the execution instances of a media workflow.
        
        @description This operation returns execution instances only in the recent 90 days.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListMediaWorkflowExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMediaWorkflowExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_file_url):
            query['InputFileURL'] = request.input_file_url
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_name):
            query['MediaWorkflowName'] = request.media_workflow_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaWorkflowExecutions',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListMediaWorkflowExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_media_workflow_executions(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        """
        @summary Queries the execution instances of a media workflow.
        
        @description This operation returns execution instances only in the recent 90 days.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListMediaWorkflowExecutionsRequest
        @return: ListMediaWorkflowExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_media_workflow_executions_with_options(request, runtime)

    async def list_media_workflow_executions_async(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        """
        @summary Queries the execution instances of a media workflow.
        
        @description This operation returns execution instances only in the recent 90 days.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: ListMediaWorkflowExecutionsRequest
        @return: ListMediaWorkflowExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_media_workflow_executions_with_options_async(request, runtime)

    def query_analysis_job_list_with_options(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        """
        @summary Queries the template analysis job and returns a list of available preset templates when the template analysis job is complete.
        
        @description The time when the job was created.
        
        @param request: QueryAnalysisJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAnalysisJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_job_ids):
            query['AnalysisJobIds'] = request.analysis_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnalysisJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAnalysisJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_analysis_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        """
        @summary Queries the template analysis job and returns a list of available preset templates when the template analysis job is complete.
        
        @description The time when the job was created.
        
        @param request: QueryAnalysisJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAnalysisJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_job_ids):
            query['AnalysisJobIds'] = request.analysis_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnalysisJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAnalysisJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_analysis_job_list(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        """
        @summary Queries the template analysis job and returns a list of available preset templates when the template analysis job is complete.
        
        @description The time when the job was created.
        
        @param request: QueryAnalysisJobListRequest
        @return: QueryAnalysisJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_analysis_job_list_with_options(request, runtime)

    async def query_analysis_job_list_async(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        """
        @summary Queries the template analysis job and returns a list of available preset templates when the template analysis job is complete.
        
        @description The time when the job was created.
        
        @param request: QueryAnalysisJobListRequest
        @return: QueryAnalysisJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_analysis_job_list_with_options_async(request, runtime)

    def query_fp_dbdelete_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        """
        @summary Queries the jobs of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of clearing or deleting a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpDBDeleteJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFpDBDeleteJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpDBDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpDBDeleteJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_dbdelete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        """
        @summary Queries the jobs of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of clearing or deleting a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpDBDeleteJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFpDBDeleteJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpDBDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpDBDeleteJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fp_dbdelete_job_list(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        """
        @summary Queries the jobs of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of clearing or deleting a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpDBDeleteJobListRequest
        @return: QueryFpDBDeleteJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fp_dbdelete_job_list_with_options(request, runtime)

    async def query_fp_dbdelete_job_list_async(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        """
        @summary Queries the jobs of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of clearing or deleting a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpDBDeleteJobListRequest
        @return: QueryFpDBDeleteJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_dbdelete_job_list_with_options_async(request, runtime)

    def query_fp_file_delete_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        """
        @summary Queries the jobs of deleting media files from a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of deleting media files from a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpFileDeleteJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFpFileDeleteJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpFileDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpFileDeleteJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_file_delete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        """
        @summary Queries the jobs of deleting media files from a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of deleting media files from a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpFileDeleteJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFpFileDeleteJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpFileDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpFileDeleteJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fp_file_delete_job_list(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        """
        @summary Queries the jobs of deleting media files from a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of deleting media files from a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpFileDeleteJobListRequest
        @return: QueryFpFileDeleteJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fp_file_delete_job_list_with_options(request, runtime)

    async def query_fp_file_delete_job_list_async(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        """
        @summary Queries the jobs of deleting media files from a media fingerprint library.
        
        @description You can call this operation to query the specified jobs of deleting media files from a media fingerprint library based on the job IDs. If you do not specify job IDs, the system returns the latest 20 jobs that are submitted.
        ### QPS limit
        You can call this operation up to 500 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpFileDeleteJobListRequest
        @return: QueryFpFileDeleteJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_file_delete_job_list_with_options_async(request, runtime)

    def query_fp_shot_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        """
        @summary Queries media fingerprint analysis jobs. You can call this operation to query video fingerprint analysis jobs and text fingerprint analysis jobs.
        
        @description    After a media fingerprint analysis job is submitted, the media fingerprinting service compares the fingerprints of the job input with those of the media files in the media fingerprint library. You can call this operation to query the job results.
        You can query the results of a text fingerprint analysis job only in the China (Shanghai) region.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpShotJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFpShotJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpShotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpShotJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_shot_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        """
        @summary Queries media fingerprint analysis jobs. You can call this operation to query video fingerprint analysis jobs and text fingerprint analysis jobs.
        
        @description    After a media fingerprint analysis job is submitted, the media fingerprinting service compares the fingerprints of the job input with those of the media files in the media fingerprint library. You can call this operation to query the job results.
        You can query the results of a text fingerprint analysis job only in the China (Shanghai) region.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpShotJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFpShotJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpShotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpShotJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fp_shot_job_list(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        """
        @summary Queries media fingerprint analysis jobs. You can call this operation to query video fingerprint analysis jobs and text fingerprint analysis jobs.
        
        @description    After a media fingerprint analysis job is submitted, the media fingerprinting service compares the fingerprints of the job input with those of the media files in the media fingerprint library. You can call this operation to query the job results.
        You can query the results of a text fingerprint analysis job only in the China (Shanghai) region.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpShotJobListRequest
        @return: QueryFpShotJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_fp_shot_job_list_with_options(request, runtime)

    async def query_fp_shot_job_list_async(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        """
        @summary Queries media fingerprint analysis jobs. You can call this operation to query video fingerprint analysis jobs and text fingerprint analysis jobs.
        
        @description    After a media fingerprint analysis job is submitted, the media fingerprinting service compares the fingerprints of the job input with those of the media files in the media fingerprint library. You can call this operation to query the job results.
        You can query the results of a text fingerprint analysis job only in the China (Shanghai) region.
        ### [](#qps)QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryFpShotJobListRequest
        @return: QueryFpShotJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_shot_job_list_with_options_async(request, runtime)

    def query_iproduction_job_with_options(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        """
        @param request: QueryIProductionJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIProductionJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        """
        @param request: QueryIProductionJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryIProductionJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_iproduction_job(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        """
        @param request: QueryIProductionJobRequest
        @return: QueryIProductionJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_iproduction_job_with_options(request, runtime)

    async def query_iproduction_job_async(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        """
        @param request: QueryIProductionJobRequest
        @return: QueryIProductionJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_iproduction_job_with_options_async(request, runtime)

    def query_job_list_with_options(
        self,
        request: mts_20140618_models.QueryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryJobListResponse:
        """
        @summary Queries transcoding jobs at a time by job ID.
        
        @description    By default, returned jobs are sorted in descending order by CreationTime.
        You can call this operation to query up to 10 transcoding jobs at a time.
        If you do not set the JobIds parameter, the `InvalidParameter` error code is returned.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryJobListResponse:
        """
        @summary Queries transcoding jobs at a time by job ID.
        
        @description    By default, returned jobs are sorted in descending order by CreationTime.
        You can call this operation to query up to 10 transcoding jobs at a time.
        If you do not set the JobIds parameter, the `InvalidParameter` error code is returned.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_job_list(
        self,
        request: mts_20140618_models.QueryJobListRequest,
    ) -> mts_20140618_models.QueryJobListResponse:
        """
        @summary Queries transcoding jobs at a time by job ID.
        
        @description    By default, returned jobs are sorted in descending order by CreationTime.
        You can call this operation to query up to 10 transcoding jobs at a time.
        If you do not set the JobIds parameter, the `InvalidParameter` error code is returned.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryJobListRequest
        @return: QueryJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_job_list_with_options(request, runtime)

    async def query_job_list_async(
        self,
        request: mts_20140618_models.QueryJobListRequest,
    ) -> mts_20140618_models.QueryJobListResponse:
        """
        @summary Queries transcoding jobs at a time by job ID.
        
        @description    By default, returned jobs are sorted in descending order by CreationTime.
        You can call this operation to query up to 10 transcoding jobs at a time.
        If you do not set the JobIds parameter, the `InvalidParameter` error code is returned.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryJobListRequest
        @return: QueryJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_job_list_with_options_async(request, runtime)

    def query_media_censor_job_detail_with_options(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        """
        @summary Queries the information about a content moderation job.
        
        @description In the content moderation results, the moderation results of the video are sorted in ascending order by time into a timeline. If the video is long, the content moderation results are paginated, and the first page is returned. You can call this operation again to query the remaining moderation results of the video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaCensorJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_detail_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        """
        @summary Queries the information about a content moderation job.
        
        @description In the content moderation results, the moderation results of the video are sorted in ascending order by time into a timeline. If the video is long, the content moderation results are paginated, and the first page is returned. You can call this operation again to query the remaining moderation results of the video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaCensorJobDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_censor_job_detail(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        """
        @summary Queries the information about a content moderation job.
        
        @description In the content moderation results, the moderation results of the video are sorted in ascending order by time into a timeline. If the video is long, the content moderation results are paginated, and the first page is returned. You can call this operation again to query the remaining moderation results of the video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobDetailRequest
        @return: QueryMediaCensorJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_detail_with_options(request, runtime)

    async def query_media_censor_job_detail_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        """
        @summary Queries the information about a content moderation job.
        
        @description In the content moderation results, the moderation results of the video are sorted in ascending order by time into a timeline. If the video is long, the content moderation results are paginated, and the first page is returned. You can call this operation again to query the remaining moderation results of the video.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobDetailRequest
        @return: QueryMediaCensorJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_media_censor_job_detail_with_options_async(request, runtime)

    def query_media_censor_job_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        """
        @summary Queries content moderation jobs.
        
        @description You can call this operation to query only the content moderation jobs within three months.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaCensorJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        """
        @summary Queries content moderation jobs.
        
        @description You can call this operation to query only the content moderation jobs within three months.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaCensorJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_censor_job_list(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        """
        @summary Queries content moderation jobs.
        
        @description You can call this operation to query only the content moderation jobs within three months.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobListRequest
        @return: QueryMediaCensorJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_list_with_options(request, runtime)

    async def query_media_censor_job_list_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        """
        @summary Queries content moderation jobs.
        
        @description You can call this operation to query only the content moderation jobs within three months.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaCensorJobListRequest
        @return: QueryMediaCensorJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_media_censor_job_list_with_options_async(request, runtime)

    def query_media_info_job_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        """
        @summary Queries the results of media information analysis jobs.
        
        @description    In asynchronous mode, the media information can be retrieved only after the Message Service (MNS) callback of **submitting a media information job** is returned. If you have not retrieved the media information for a long period, the job may have failed.
        You can call this operation to query up to 10 media information analysis jobs at a time.
        By default, returned jobs are sorted in descending order by CreationTime.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaInfoJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaInfoJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_info_job_ids):
            query['MediaInfoJobIds'] = request.media_info_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaInfoJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaInfoJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_info_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        """
        @summary Queries the results of media information analysis jobs.
        
        @description    In asynchronous mode, the media information can be retrieved only after the Message Service (MNS) callback of **submitting a media information job** is returned. If you have not retrieved the media information for a long period, the job may have failed.
        You can call this operation to query up to 10 media information analysis jobs at a time.
        By default, returned jobs are sorted in descending order by CreationTime.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaInfoJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaInfoJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_info_job_ids):
            query['MediaInfoJobIds'] = request.media_info_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaInfoJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaInfoJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_info_job_list(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        """
        @summary Queries the results of media information analysis jobs.
        
        @description    In asynchronous mode, the media information can be retrieved only after the Message Service (MNS) callback of **submitting a media information job** is returned. If you have not retrieved the media information for a long period, the job may have failed.
        You can call this operation to query up to 10 media information analysis jobs at a time.
        By default, returned jobs are sorted in descending order by CreationTime.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaInfoJobListRequest
        @return: QueryMediaInfoJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_media_info_job_list_with_options(request, runtime)

    async def query_media_info_job_list_async(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        """
        @summary Queries the results of media information analysis jobs.
        
        @description    In asynchronous mode, the media information can be retrieved only after the Message Service (MNS) callback of **submitting a media information job** is returned. If you have not retrieved the media information for a long period, the job may have failed.
        You can call this operation to query up to 10 media information analysis jobs at a time.
        By default, returned jobs are sorted in descending order by CreationTime.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaInfoJobListRequest
        @return: QueryMediaInfoJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_media_info_job_list_with_options_async(request, runtime)

    def query_media_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListResponse:
        """
        @summary Queries media files based on media file IDs.
        
        @description You can call this operation to query up to 10 media files at a time.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListResponse:
        """
        @summary Queries media files based on media file IDs.
        
        @description You can call this operation to query up to 10 media files at a time.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_list(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
    ) -> mts_20140618_models.QueryMediaListResponse:
        """
        @summary Queries media files based on media file IDs.
        
        @description You can call this operation to query up to 10 media files at a time.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListRequest
        @return: QueryMediaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_media_list_with_options(request, runtime)

    async def query_media_list_async(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
    ) -> mts_20140618_models.QueryMediaListResponse:
        """
        @summary Queries media files based on media file IDs.
        
        @description You can call this operation to query up to 10 media files at a time.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListRequest
        @return: QueryMediaListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_media_list_with_options_async(request, runtime)

    def query_media_list_by_urlwith_options(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        """
        @summary Queries media files based on their Object Storage Service (OSS) URLs.
        
        @description    You can call this operation to query up to 10 media files at a time.
        Before you call this operation, you must call the [AddMedia](https://help.aliyun.com/document_detail/44458.html) operation to add media files.
        You can call this operation to query only media files that are processed in a workflow. To obtain comprehensive information about a media file that is newly uploaded to OSS, you can call this operation after the corresponding workflow is complete. To query media files that are not processed in a workflow, you must call the [SubmitMediaInfoJob](https://help.aliyun.com/document_detail/29220.html) operation to submit a media information analysis job. After the job is complete, you can query the information about the media files.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListByURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaListByURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaListByURL',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_list_by_urlwith_options_async(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        """
        @summary Queries media files based on their Object Storage Service (OSS) URLs.
        
        @description    You can call this operation to query up to 10 media files at a time.
        Before you call this operation, you must call the [AddMedia](https://help.aliyun.com/document_detail/44458.html) operation to add media files.
        You can call this operation to query only media files that are processed in a workflow. To obtain comprehensive information about a media file that is newly uploaded to OSS, you can call this operation after the corresponding workflow is complete. To query media files that are not processed in a workflow, you must call the [SubmitMediaInfoJob](https://help.aliyun.com/document_detail/29220.html) operation to submit a media information analysis job. After the job is complete, you can query the information about the media files.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListByURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaListByURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaListByURL',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListByURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_list_by_url(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        """
        @summary Queries media files based on their Object Storage Service (OSS) URLs.
        
        @description    You can call this operation to query up to 10 media files at a time.
        Before you call this operation, you must call the [AddMedia](https://help.aliyun.com/document_detail/44458.html) operation to add media files.
        You can call this operation to query only media files that are processed in a workflow. To obtain comprehensive information about a media file that is newly uploaded to OSS, you can call this operation after the corresponding workflow is complete. To query media files that are not processed in a workflow, you must call the [SubmitMediaInfoJob](https://help.aliyun.com/document_detail/29220.html) operation to submit a media information analysis job. After the job is complete, you can query the information about the media files.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListByURLRequest
        @return: QueryMediaListByURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_media_list_by_urlwith_options(request, runtime)

    async def query_media_list_by_url_async(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        """
        @summary Queries media files based on their Object Storage Service (OSS) URLs.
        
        @description    You can call this operation to query up to 10 media files at a time.
        Before you call this operation, you must call the [AddMedia](https://help.aliyun.com/document_detail/44458.html) operation to add media files.
        You can call this operation to query only media files that are processed in a workflow. To obtain comprehensive information about a media file that is newly uploaded to OSS, you can call this operation after the corresponding workflow is complete. To query media files that are not processed in a workflow, you must call the [SubmitMediaInfoJob](https://help.aliyun.com/document_detail/29220.html) operation to submit a media information analysis job. After the job is complete, you can query the information about the media files.
        ## QPS limit
        You can call this API operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: QueryMediaListByURLRequest
        @return: QueryMediaListByURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_media_list_by_urlwith_options_async(request, runtime)

    def query_media_workflow_execution_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        """
        @summary Queries media workflow execution instances.
        
        @description    You can call this operation to query a maximum of 10 media workflow execution instances at a time.
        Before you call this operation, make sure that the workflow pipeline is enabled. Otherwise, the workflow may not run as expected. For example, the following exceptions may occur: the workflow node is invalid and jobs created in the workflow cannot be executed.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowExecutionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaWorkflowExecutionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.run_ids):
            query['RunIds'] = request.run_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowExecutionList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowExecutionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_workflow_execution_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        """
        @summary Queries media workflow execution instances.
        
        @description    You can call this operation to query a maximum of 10 media workflow execution instances at a time.
        Before you call this operation, make sure that the workflow pipeline is enabled. Otherwise, the workflow may not run as expected. For example, the following exceptions may occur: the workflow node is invalid and jobs created in the workflow cannot be executed.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowExecutionListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaWorkflowExecutionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.run_ids):
            query['RunIds'] = request.run_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowExecutionList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowExecutionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_workflow_execution_list(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        """
        @summary Queries media workflow execution instances.
        
        @description    You can call this operation to query a maximum of 10 media workflow execution instances at a time.
        Before you call this operation, make sure that the workflow pipeline is enabled. Otherwise, the workflow may not run as expected. For example, the following exceptions may occur: the workflow node is invalid and jobs created in the workflow cannot be executed.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowExecutionListRequest
        @return: QueryMediaWorkflowExecutionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_media_workflow_execution_list_with_options(request, runtime)

    async def query_media_workflow_execution_list_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        """
        @summary Queries media workflow execution instances.
        
        @description    You can call this operation to query a maximum of 10 media workflow execution instances at a time.
        Before you call this operation, make sure that the workflow pipeline is enabled. Otherwise, the workflow may not run as expected. For example, the following exceptions may occur: the workflow node is invalid and jobs created in the workflow cannot be executed.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowExecutionListRequest
        @return: QueryMediaWorkflowExecutionListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_media_workflow_execution_list_with_options_async(request, runtime)

    def query_media_workflow_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        """
        @summary Queries registered media workflows.
        
        @description You can call this operation to query up to 10 media workflows at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaWorkflowListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_ids):
            query['MediaWorkflowIds'] = request.media_workflow_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_workflow_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        """
        @summary Queries registered media workflows.
        
        @description You can call this operation to query up to 10 media workflows at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMediaWorkflowListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_ids):
            query['MediaWorkflowIds'] = request.media_workflow_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_workflow_list(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        """
        @summary Queries registered media workflows.
        
        @description You can call this operation to query up to 10 media workflows at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowListRequest
        @return: QueryMediaWorkflowListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_media_workflow_list_with_options(request, runtime)

    async def query_media_workflow_list_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        """
        @summary Queries registered media workflows.
        
        @description You can call this operation to query up to 10 media workflows at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryMediaWorkflowListRequest
        @return: QueryMediaWorkflowListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_media_workflow_list_with_options_async(request, runtime)

    def query_pipeline_list_with_options(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        """
        @summary Queries an ApsaraVideo Media Processing (MPS) queue by using the ID of the queue.
        
        @description    You can call this operation to query up to 10 MPS queues at a time.
        If `"Code": "InvalidIdentity.ServiceDisabled","Message": "The request identity was not allowed operated.","Recommend"` is returned after you call this operation, check whether the RAM user that you use is assigned the AliyunMTSDefaultRole role to obtain the permissions on MPS and whether your Alibaba Cloud account has overdue payments.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryPipelineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPipelineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        """
        @summary Queries an ApsaraVideo Media Processing (MPS) queue by using the ID of the queue.
        
        @description    You can call this operation to query up to 10 MPS queues at a time.
        If `"Code": "InvalidIdentity.ServiceDisabled","Message": "The request identity was not allowed operated.","Recommend"` is returned after you call this operation, check whether the RAM user that you use is assigned the AliyunMTSDefaultRole role to obtain the permissions on MPS and whether your Alibaba Cloud account has overdue payments.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryPipelineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPipelineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pipeline_list(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        """
        @summary Queries an ApsaraVideo Media Processing (MPS) queue by using the ID of the queue.
        
        @description    You can call this operation to query up to 10 MPS queues at a time.
        If `"Code": "InvalidIdentity.ServiceDisabled","Message": "The request identity was not allowed operated.","Recommend"` is returned after you call this operation, check whether the RAM user that you use is assigned the AliyunMTSDefaultRole role to obtain the permissions on MPS and whether your Alibaba Cloud account has overdue payments.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryPipelineListRequest
        @return: QueryPipelineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_pipeline_list_with_options(request, runtime)

    async def query_pipeline_list_async(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        """
        @summary Queries an ApsaraVideo Media Processing (MPS) queue by using the ID of the queue.
        
        @description    You can call this operation to query up to 10 MPS queues at a time.
        If `"Code": "InvalidIdentity.ServiceDisabled","Message": "The request identity was not allowed operated.","Recommend"` is returned after you call this operation, check whether the RAM user that you use is assigned the AliyunMTSDefaultRole role to obtain the permissions on MPS and whether your Alibaba Cloud account has overdue payments.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryPipelineListRequest
        @return: QueryPipelineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_pipeline_list_with_options_async(request, runtime)

    def query_smarttag_job_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        """
        @param request: QuerySmarttagJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmarttagJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_job_with_options_async(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        """
        @param request: QuerySmarttagJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmarttagJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_smarttag_job(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        """
        @param request: QuerySmarttagJobRequest
        @return: QuerySmarttagJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_smarttag_job_with_options(request, runtime)

    async def query_smarttag_job_async(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        """
        @param request: QuerySmarttagJobRequest
        @return: QuerySmarttagJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_smarttag_job_with_options_async(request, runtime)

    def query_smarttag_template_list_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        """
        @summary Queries the analysis template of a smart tagging job.
        
        @description If you call this operation to query the information about a smart tagging template, you must specify the template ID. Otherwise, the operation returns the information about all the templates that are created by the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QuerySmarttagTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmarttagTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_template_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        """
        @summary Queries the analysis template of a smart tagging job.
        
        @description If you call this operation to query the information about a smart tagging template, you must specify the template ID. Otherwise, the operation returns the information about all the templates that are created by the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QuerySmarttagTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmarttagTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_smarttag_template_list(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        """
        @summary Queries the analysis template of a smart tagging job.
        
        @description If you call this operation to query the information about a smart tagging template, you must specify the template ID. Otherwise, the operation returns the information about all the templates that are created by the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QuerySmarttagTemplateListRequest
        @return: QuerySmarttagTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_smarttag_template_list_with_options(request, runtime)

    async def query_smarttag_template_list_async(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        """
        @summary Queries the analysis template of a smart tagging job.
        
        @description If you call this operation to query the information about a smart tagging template, you must specify the template ID. Otherwise, the operation returns the information about all the templates that are created by the current RAM user.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QuerySmarttagTemplateListRequest
        @return: QuerySmarttagTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_smarttag_template_list_with_options_async(request, runtime)

    def query_snapshot_job_list_with_options(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        """
        @summary Queries snapshot jobs.
        
        @description The status of the snapshot jobs that you want to query.
        **Submitted**: The job was submitted.
        **Snapshoting**: The job is being processed.
        **Success**: The job was successfully processed.
        **Fail**: The job failed.
        
        @param request: QuerySnapshotJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySnapshotJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_job_ids):
            query['SnapshotJobIds'] = request.snapshot_job_ids
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySnapshotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySnapshotJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_snapshot_job_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        """
        @summary Queries snapshot jobs.
        
        @description The status of the snapshot jobs that you want to query.
        **Submitted**: The job was submitted.
        **Snapshoting**: The job is being processed.
        **Success**: The job was successfully processed.
        **Fail**: The job failed.
        
        @param request: QuerySnapshotJobListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySnapshotJobListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_job_ids):
            query['SnapshotJobIds'] = request.snapshot_job_ids
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySnapshotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySnapshotJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_snapshot_job_list(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        """
        @summary Queries snapshot jobs.
        
        @description The status of the snapshot jobs that you want to query.
        **Submitted**: The job was submitted.
        **Snapshoting**: The job is being processed.
        **Success**: The job was successfully processed.
        **Fail**: The job failed.
        
        @param request: QuerySnapshotJobListRequest
        @return: QuerySnapshotJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_snapshot_job_list_with_options(request, runtime)

    async def query_snapshot_job_list_async(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        """
        @summary Queries snapshot jobs.
        
        @description The status of the snapshot jobs that you want to query.
        **Submitted**: The job was submitted.
        **Snapshoting**: The job is being processed.
        **Success**: The job was successfully processed.
        **Fail**: The job failed.
        
        @param request: QuerySnapshotJobListRequest
        @return: QuerySnapshotJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_snapshot_job_list_with_options_async(request, runtime)

    def query_template_list_with_options(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        """
        @summary You can call this operation to query up to 10 transcoding templates at a time.
        
        @description The IDs of the transcoding templates that you want to query. You can query up to 10 transcoding templates at a time. Separate multiple IDs of custom transcoding templates with commas (,).
        
        @param request: QueryTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_template_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        """
        @summary You can call this operation to query up to 10 transcoding templates at a time.
        
        @description The IDs of the transcoding templates that you want to query. You can query up to 10 transcoding templates at a time. Separate multiple IDs of custom transcoding templates with commas (,).
        
        @param request: QueryTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_template_list(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        """
        @summary You can call this operation to query up to 10 transcoding templates at a time.
        
        @description The IDs of the transcoding templates that you want to query. You can query up to 10 transcoding templates at a time. Separate multiple IDs of custom transcoding templates with commas (,).
        
        @param request: QueryTemplateListRequest
        @return: QueryTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_template_list_with_options(request, runtime)

    async def query_template_list_async(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        """
        @summary You can call this operation to query up to 10 transcoding templates at a time.
        
        @description The IDs of the transcoding templates that you want to query. You can query up to 10 transcoding templates at a time. Separate multiple IDs of custom transcoding templates with commas (,).
        
        @param request: QueryTemplateListRequest
        @return: QueryTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_template_list_with_options_async(request, runtime)

    def query_water_mark_template_list_with_options(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        """
        @summary Queries watermark templates.
        
        @description You can call this operation to query up to 10 watermark templates at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryWaterMarkTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWaterMarkTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_ids):
            query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaterMarkTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryWaterMarkTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_water_mark_template_list_with_options_async(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        """
        @summary Queries watermark templates.
        
        @description You can call this operation to query up to 10 watermark templates at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryWaterMarkTemplateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryWaterMarkTemplateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_ids):
            query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaterMarkTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryWaterMarkTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_water_mark_template_list(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        """
        @summary Queries watermark templates.
        
        @description You can call this operation to query up to 10 watermark templates at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryWaterMarkTemplateListRequest
        @return: QueryWaterMarkTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_water_mark_template_list_with_options(request, runtime)

    async def query_water_mark_template_list_async(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        """
        @summary Queries watermark templates.
        
        @description You can call this operation to query up to 10 watermark templates at a time.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: QueryWaterMarkTemplateListRequest
        @return: QueryWaterMarkTemplateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_water_mark_template_list_with_options_async(request, runtime)

    def register_custom_face_with_options(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        """
        @summary Registers a custom face.
        
        @description    You can call this operation to register only one custom face at a time.
        A maximum of 10 images can be registered for a custom face.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: RegisterCustomFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCustomFaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterCustomFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_custom_face_with_options_async(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        """
        @summary Registers a custom face.
        
        @description    You can call this operation to register only one custom face at a time.
        A maximum of 10 images can be registered for a custom face.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: RegisterCustomFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCustomFaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterCustomFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_custom_face(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        """
        @summary Registers a custom face.
        
        @description    You can call this operation to register only one custom face at a time.
        A maximum of 10 images can be registered for a custom face.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: RegisterCustomFaceRequest
        @return: RegisterCustomFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_custom_face_with_options(request, runtime)

    async def register_custom_face_async(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        """
        @summary Registers a custom face.
        
        @description    You can call this operation to register only one custom face at a time.
        A maximum of 10 images can be registered for a custom face.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: RegisterCustomFaceRequest
        @return: RegisterCustomFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_custom_face_with_options_async(request, runtime)

    def register_custom_view_with_options(
        self,
        request: mts_20140618_models.RegisterCustomViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomViewResponse:
        """
        @param request: RegisterCustomViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCustomViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomView',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterCustomViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_custom_view_with_options_async(
        self,
        request: mts_20140618_models.RegisterCustomViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomViewResponse:
        """
        @param request: RegisterCustomViewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterCustomViewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not UtilClient.is_unset(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomView',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterCustomViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_custom_view(
        self,
        request: mts_20140618_models.RegisterCustomViewRequest,
    ) -> mts_20140618_models.RegisterCustomViewResponse:
        """
        @param request: RegisterCustomViewRequest
        @return: RegisterCustomViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_custom_view_with_options(request, runtime)

    async def register_custom_view_async(
        self,
        request: mts_20140618_models.RegisterCustomViewRequest,
    ) -> mts_20140618_models.RegisterCustomViewResponse:
        """
        @param request: RegisterCustomViewRequest
        @return: RegisterCustomViewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_custom_view_with_options_async(request, runtime)

    def search_media_workflow_with_options(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        """
        @summary Queries media workflows in the specified state.
        
        @description You can call this operation to query media workflows in the specified state. If you do not specify the state, all media workflows are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchMediaWorkflowResponse
        """
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state_list):
            query['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        """
        @summary Queries media workflows in the specified state.
        
        @description You can call this operation to query media workflows in the specified state. If you do not specify the state, all media workflows are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchMediaWorkflowResponse
        """
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state_list):
            query['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_media_workflow(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        """
        @summary Queries media workflows in the specified state.
        
        @description You can call this operation to query media workflows in the specified state. If you do not specify the state, all media workflows are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchMediaWorkflowRequest
        @return: SearchMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_media_workflow_with_options(request, runtime)

    async def search_media_workflow_async(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        """
        @summary Queries media workflows in the specified state.
        
        @description You can call this operation to query media workflows in the specified state. If you do not specify the state, all media workflows are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchMediaWorkflowRequest
        @return: SearchMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_media_workflow_with_options_async(request, runtime)

    def search_pipeline_with_options(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchPipelineResponse:
        """
        @summary Searches for ApsaraVideo Media Processing (MPS) queues in the specified state.
        
        @description You can call this operation to query MPS queues in the specified state. If you do not specify the state, all MPS queues are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchPipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPipelineResponse
        """
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_pipeline_with_options_async(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchPipelineResponse:
        """
        @summary Searches for ApsaraVideo Media Processing (MPS) queues in the specified state.
        
        @description You can call this operation to query MPS queues in the specified state. If you do not specify the state, all MPS queues are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchPipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchPipelineResponse
        """
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_pipeline(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
    ) -> mts_20140618_models.SearchPipelineResponse:
        """
        @summary Searches for ApsaraVideo Media Processing (MPS) queues in the specified state.
        
        @description You can call this operation to query MPS queues in the specified state. If you do not specify the state, all MPS queues are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchPipelineRequest
        @return: SearchPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_pipeline_with_options(request, runtime)

    async def search_pipeline_async(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
    ) -> mts_20140618_models.SearchPipelineResponse:
        """
        @summary Searches for ApsaraVideo Media Processing (MPS) queues in the specified state.
        
        @description You can call this operation to query MPS queues in the specified state. If you do not specify the state, all MPS queues are queried by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchPipelineRequest
        @return: SearchPipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_pipeline_with_options_async(request, runtime)

    def search_template_with_options(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchTemplateResponse:
        """
        @summary You can call this operation to query custom transcoding templates in the specified state.
        
        @description You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_template_with_options_async(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchTemplateResponse:
        """
        @summary You can call this operation to query custom transcoding templates in the specified state.
        
        @description You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_template(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
    ) -> mts_20140618_models.SearchTemplateResponse:
        """
        @summary You can call this operation to query custom transcoding templates in the specified state.
        
        @description You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchTemplateRequest
        @return: SearchTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_template_with_options(request, runtime)

    async def search_template_async(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
    ) -> mts_20140618_models.SearchTemplateResponse:
        """
        @summary You can call this operation to query custom transcoding templates in the specified state.
        
        @description You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SearchTemplateRequest
        @return: SearchTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_template_with_options_async(request, runtime)

    def search_water_mark_template_with_options(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        """
        @summary Searches for watermark templates.
        
        @description The total number of returned entries.
        
        @param request: SearchWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchWaterMarkTemplateResponse
        """
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        """
        @summary Searches for watermark templates.
        
        @description The total number of returned entries.
        
        @param request: SearchWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchWaterMarkTemplateResponse
        """
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_water_mark_template(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        """
        @summary Searches for watermark templates.
        
        @description The total number of returned entries.
        
        @param request: SearchWaterMarkTemplateRequest
        @return: SearchWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_water_mark_template_with_options(request, runtime)

    async def search_water_mark_template_async(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        """
        @summary Searches for watermark templates.
        
        @description The total number of returned entries.
        
        @param request: SearchWaterMarkTemplateRequest
        @return: SearchWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_water_mark_template_with_options_async(request, runtime)

    def submit_analysis_job_with_options(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        """
        @summary Submits a preset template analysis job.
        
        @description    After you call the SubmitAnalysisJob operation to submit a preset template analysis job, ApsaraVideo Media Processing (MPS) intelligently analyzes the input file of the job and recommends a suitable preset template. You can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html) operation to query the analysis result or enable asynchronous notifications to receive the analysis result.
        The analysis result is retained only for two weeks after it is generated. The analysis result is deleted after two weeks. If you use the recommended preset template in a transcoding job after two weeks, the job fails, and the `AnalysisResultNotFound` error code is returned.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitAnalysisJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAnalysisJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_config):
            query['AnalysisConfig'] = request.analysis_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_analysis_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        """
        @summary Submits a preset template analysis job.
        
        @description    After you call the SubmitAnalysisJob operation to submit a preset template analysis job, ApsaraVideo Media Processing (MPS) intelligently analyzes the input file of the job and recommends a suitable preset template. You can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html) operation to query the analysis result or enable asynchronous notifications to receive the analysis result.
        The analysis result is retained only for two weeks after it is generated. The analysis result is deleted after two weeks. If you use the recommended preset template in a transcoding job after two weeks, the job fails, and the `AnalysisResultNotFound` error code is returned.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitAnalysisJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAnalysisJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_config):
            query['AnalysisConfig'] = request.analysis_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAnalysisJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_analysis_job(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        """
        @summary Submits a preset template analysis job.
        
        @description    After you call the SubmitAnalysisJob operation to submit a preset template analysis job, ApsaraVideo Media Processing (MPS) intelligently analyzes the input file of the job and recommends a suitable preset template. You can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html) operation to query the analysis result or enable asynchronous notifications to receive the analysis result.
        The analysis result is retained only for two weeks after it is generated. The analysis result is deleted after two weeks. If you use the recommended preset template in a transcoding job after two weeks, the job fails, and the `AnalysisResultNotFound` error code is returned.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitAnalysisJobRequest
        @return: SubmitAnalysisJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_analysis_job_with_options(request, runtime)

    async def submit_analysis_job_async(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        """
        @summary Submits a preset template analysis job.
        
        @description    After you call the SubmitAnalysisJob operation to submit a preset template analysis job, ApsaraVideo Media Processing (MPS) intelligently analyzes the input file of the job and recommends a suitable preset template. You can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html) operation to query the analysis result or enable asynchronous notifications to receive the analysis result.
        The analysis result is retained only for two weeks after it is generated. The analysis result is deleted after two weeks. If you use the recommended preset template in a transcoding job after two weeks, the job fails, and the `AnalysisResultNotFound` error code is returned.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitAnalysisJobRequest
        @return: SubmitAnalysisJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_analysis_job_with_options_async(request, runtime)

    def submit_fp_dbdelete_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        """
        @summary Submits a job of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to clear or delete the specified media fingerprint library based on the library ID. If you clear a media fingerprint library, the content in the library is deleted, but the library is not deleted. If you delete a media fingerprint library, both the library and the content in the library are deleted. If you do not specify the operation type, the system clears the media fingerprint library by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpDBDeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitFpDBDeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.del_type):
            query['DelType'] = request.del_type
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpDBDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpDBDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_dbdelete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        """
        @summary Submits a job of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to clear or delete the specified media fingerprint library based on the library ID. If you clear a media fingerprint library, the content in the library is deleted, but the library is not deleted. If you delete a media fingerprint library, both the library and the content in the library are deleted. If you do not specify the operation type, the system clears the media fingerprint library by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpDBDeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitFpDBDeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.del_type):
            query['DelType'] = request.del_type
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpDBDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpDBDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fp_dbdelete_job(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        """
        @summary Submits a job of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to clear or delete the specified media fingerprint library based on the library ID. If you clear a media fingerprint library, the content in the library is deleted, but the library is not deleted. If you delete a media fingerprint library, both the library and the content in the library are deleted. If you do not specify the operation type, the system clears the media fingerprint library by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpDBDeleteJobRequest
        @return: SubmitFpDBDeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_fp_dbdelete_job_with_options(request, runtime)

    async def submit_fp_dbdelete_job_async(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        """
        @summary Submits a job of clearing or deleting a media fingerprint library.
        
        @description You can call this operation to clear or delete the specified media fingerprint library based on the library ID. If you clear a media fingerprint library, the content in the library is deleted, but the library is not deleted. If you delete a media fingerprint library, both the library and the content in the library are deleted. If you do not specify the operation type, the system clears the media fingerprint library by default.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpDBDeleteJobRequest
        @return: SubmitFpDBDeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_fp_dbdelete_job_with_options_async(request, runtime)

    def submit_fp_file_delete_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        """
        @summary Submits a job of deleting media files from a media fingerprint library.
        
        @description ## [](#)Limits
        You can call this operation to delete up to 200 media files from a media fingerprint library at a time.
        This operation is available in the following regions: China (Beijing), China (Hangzhou), China (Shanghai), and Singapore.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpFileDeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitFpFileDeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.primary_keys):
            query['PrimaryKeys'] = request.primary_keys
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpFileDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpFileDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_file_delete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        """
        @summary Submits a job of deleting media files from a media fingerprint library.
        
        @description ## [](#)Limits
        You can call this operation to delete up to 200 media files from a media fingerprint library at a time.
        This operation is available in the following regions: China (Beijing), China (Hangzhou), China (Shanghai), and Singapore.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpFileDeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitFpFileDeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.primary_keys):
            query['PrimaryKeys'] = request.primary_keys
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpFileDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpFileDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fp_file_delete_job(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        """
        @summary Submits a job of deleting media files from a media fingerprint library.
        
        @description ## [](#)Limits
        You can call this operation to delete up to 200 media files from a media fingerprint library at a time.
        This operation is available in the following regions: China (Beijing), China (Hangzhou), China (Shanghai), and Singapore.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpFileDeleteJobRequest
        @return: SubmitFpFileDeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_fp_file_delete_job_with_options(request, runtime)

    async def submit_fp_file_delete_job_async(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        """
        @summary Submits a job of deleting media files from a media fingerprint library.
        
        @description ## [](#)Limits
        You can call this operation to delete up to 200 media files from a media fingerprint library at a time.
        This operation is available in the following regions: China (Beijing), China (Hangzhou), China (Shanghai), and Singapore.
        ## [](#qps-)QPS limits
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpFileDeleteJobRequest
        @return: SubmitFpFileDeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_fp_file_delete_job_with_options_async(request, runtime)

    def submit_fp_shot_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        """
        @summary Submits a media fingerprint analysis job to query the media fingerprint repository for a media file with the identical or similar fingerprint as the input file.
        
        @description    You can call this operation to submit a video, audio, image, or text fingerprint analysis job.
        This operation asynchronously submits a job. The query results may not have been generated when the response is returned. After the results are generated, an asynchronous message is returned.
        You can submit a text fingerprint analysis job only in the China (Shanghai) region.
        The input file of the job must be in one of the following formats:
        Image formats: JPEG, PNG, and BMP.
        Video formats: MP4, AVI, MKV, MPG, TS, MOV, FLV, MXF.
        Video encoding formats: MPEG2, MPEG4, H264, HEVC, and WMV.
        ### QPS limit
        You can call this operation up to 150 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpShotJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitFpShotJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fp_shot_config):
            query['FpShotConfig'] = request.fp_shot_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpShotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_shot_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        """
        @summary Submits a media fingerprint analysis job to query the media fingerprint repository for a media file with the identical or similar fingerprint as the input file.
        
        @description    You can call this operation to submit a video, audio, image, or text fingerprint analysis job.
        This operation asynchronously submits a job. The query results may not have been generated when the response is returned. After the results are generated, an asynchronous message is returned.
        You can submit a text fingerprint analysis job only in the China (Shanghai) region.
        The input file of the job must be in one of the following formats:
        Image formats: JPEG, PNG, and BMP.
        Video formats: MP4, AVI, MKV, MPG, TS, MOV, FLV, MXF.
        Video encoding formats: MPEG2, MPEG4, H264, HEVC, and WMV.
        ### QPS limit
        You can call this operation up to 150 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpShotJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitFpShotJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fp_shot_config):
            query['FpShotConfig'] = request.fp_shot_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpShotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fp_shot_job(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        """
        @summary Submits a media fingerprint analysis job to query the media fingerprint repository for a media file with the identical or similar fingerprint as the input file.
        
        @description    You can call this operation to submit a video, audio, image, or text fingerprint analysis job.
        This operation asynchronously submits a job. The query results may not have been generated when the response is returned. After the results are generated, an asynchronous message is returned.
        You can submit a text fingerprint analysis job only in the China (Shanghai) region.
        The input file of the job must be in one of the following formats:
        Image formats: JPEG, PNG, and BMP.
        Video formats: MP4, AVI, MKV, MPG, TS, MOV, FLV, MXF.
        Video encoding formats: MPEG2, MPEG4, H264, HEVC, and WMV.
        ### QPS limit
        You can call this operation up to 150 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpShotJobRequest
        @return: SubmitFpShotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_fp_shot_job_with_options(request, runtime)

    async def submit_fp_shot_job_async(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        """
        @summary Submits a media fingerprint analysis job to query the media fingerprint repository for a media file with the identical or similar fingerprint as the input file.
        
        @description    You can call this operation to submit a video, audio, image, or text fingerprint analysis job.
        This operation asynchronously submits a job. The query results may not have been generated when the response is returned. After the results are generated, an asynchronous message is returned.
        You can submit a text fingerprint analysis job only in the China (Shanghai) region.
        The input file of the job must be in one of the following formats:
        Image formats: JPEG, PNG, and BMP.
        Video formats: MP4, AVI, MKV, MPG, TS, MOV, FLV, MXF.
        Video encoding formats: MPEG2, MPEG4, H264, HEVC, and WMV.
        ### QPS limit
        You can call this operation up to 150 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitFpShotJobRequest
        @return: SubmitFpShotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_fp_shot_job_with_options_async(request, runtime)

    def submit_iproduction_job_with_options(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        """
        @description    Jobs that are submitted by calling this operation run in an asynchronous manner. After a job is added to the ApsaraVideo Media Processing (MPS) queue, the job is scheduled to run. You can call the [QueryIProductionJob](https://help.aliyun.com/document_detail/170217.html) operation or configure a callback to query the job result.
        Capabilities provided by the intelligent production feature vary based on the region. Before you call this operation to submit an intelligent production job, check whether the job is supported in the region in which your service is activated. For more information, see [Regions and endpoints](https://help.aliyun.com/document_detail/43248.html).
        ### [](#qps)QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitIProductionJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIProductionJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        """
        @description    Jobs that are submitted by calling this operation run in an asynchronous manner. After a job is added to the ApsaraVideo Media Processing (MPS) queue, the job is scheduled to run. You can call the [QueryIProductionJob](https://help.aliyun.com/document_detail/170217.html) operation or configure a callback to query the job result.
        Capabilities provided by the intelligent production feature vary based on the region. Before you call this operation to submit an intelligent production job, check whether the job is supported in the region in which your service is activated. For more information, see [Regions and endpoints](https://help.aliyun.com/document_detail/43248.html).
        ### [](#qps)QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitIProductionJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitIProductionJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_iproduction_job(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        """
        @description    Jobs that are submitted by calling this operation run in an asynchronous manner. After a job is added to the ApsaraVideo Media Processing (MPS) queue, the job is scheduled to run. You can call the [QueryIProductionJob](https://help.aliyun.com/document_detail/170217.html) operation or configure a callback to query the job result.
        Capabilities provided by the intelligent production feature vary based on the region. Before you call this operation to submit an intelligent production job, check whether the job is supported in the region in which your service is activated. For more information, see [Regions and endpoints](https://help.aliyun.com/document_detail/43248.html).
        ### [](#qps)QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitIProductionJobRequest
        @return: SubmitIProductionJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_iproduction_job_with_options(request, runtime)

    async def submit_iproduction_job_async(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        """
        @description    Jobs that are submitted by calling this operation run in an asynchronous manner. After a job is added to the ApsaraVideo Media Processing (MPS) queue, the job is scheduled to run. You can call the [QueryIProductionJob](https://help.aliyun.com/document_detail/170217.html) operation or configure a callback to query the job result.
        Capabilities provided by the intelligent production feature vary based on the region. Before you call this operation to submit an intelligent production job, check whether the job is supported in the region in which your service is activated. For more information, see [Regions and endpoints](https://help.aliyun.com/document_detail/43248.html).
        ### [](#qps)QPS limit
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitIProductionJobRequest
        @return: SubmitIProductionJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_iproduction_job_with_options_async(request, runtime)

    def submit_jobs_with_options(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitJobsResponse:
        """
        @summary Submits transcoding jobs. If the transcoding jobs and workflows created in the ApsaraVideo Media Processing (MPS) console cannot meet your business requirements, you can call the SubmitJobs operation to submit transcoding jobs. Specify transcoding parameters as required when you call the SubmitJobs operation.
        
        @description    SubmitJobs is an asynchronous operation. After you submit transcoding jobs, the jobs are added to an MPS queue to be scheduled and run. The transcoding jobs may not have been complete when the response is returned. After you call this operation, you can call the [QueryJobList](https://help.aliyun.com/document_detail/602836.html) operation to query the job results. You can also associate a Message Service (MNS) queue or topic with the MPS queue to receive notifications on the jobs. For more information, see [Receive notifications](https://www.alibabacloud.com/help/zh/apsaravideo-for-media-processing/latest/receive-message-notifications).
        An input file can be up to 100 GB in size. If the size of the input file exceeds this limit, the job may fail.
        If you use an **intelligent preset template** to transcode an input file, you must first call the [SubmitAnalysisJob](https://help.aliyun.com/document_detail/29223.html) operation to submit a preset template analysis job. After the analysis job is complete, you can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html)operation to obtain the available preset templates for the input file. When you submit a transcoding job, set TemplateId to the ID of an available preset template. If you specify a preset template that is not in the available preset templates, the transcoding job fails.
        If you use a **static preset template** to transcode an input file, you do not need to submit a preset template analysis job.
        If you want to use multiple accounts in MPS, you can create Resource Access Management (RAM) users by using your Alibaba Cloud account. For more information, see [Create a RAM user and grant permissions to the RAM user](https://help.aliyun.com/document_detail/42841.html). If the Alibaba Cloud account that is used to query transcoding jobs is not the one that is used to submit the transcoding jobs, no data is returned.
        For information about transcoding FAQ, see [FAQ about MPS](https://help.aliyun.com/document_detail/38986.html).
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not UtilClient.is_unset(request.output_location):
            query['OutputLocation'] = request.output_location
        if not UtilClient.is_unset(request.outputs):
            query['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_jobs_with_options_async(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitJobsResponse:
        """
        @summary Submits transcoding jobs. If the transcoding jobs and workflows created in the ApsaraVideo Media Processing (MPS) console cannot meet your business requirements, you can call the SubmitJobs operation to submit transcoding jobs. Specify transcoding parameters as required when you call the SubmitJobs operation.
        
        @description    SubmitJobs is an asynchronous operation. After you submit transcoding jobs, the jobs are added to an MPS queue to be scheduled and run. The transcoding jobs may not have been complete when the response is returned. After you call this operation, you can call the [QueryJobList](https://help.aliyun.com/document_detail/602836.html) operation to query the job results. You can also associate a Message Service (MNS) queue or topic with the MPS queue to receive notifications on the jobs. For more information, see [Receive notifications](https://www.alibabacloud.com/help/zh/apsaravideo-for-media-processing/latest/receive-message-notifications).
        An input file can be up to 100 GB in size. If the size of the input file exceeds this limit, the job may fail.
        If you use an **intelligent preset template** to transcode an input file, you must first call the [SubmitAnalysisJob](https://help.aliyun.com/document_detail/29223.html) operation to submit a preset template analysis job. After the analysis job is complete, you can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html)operation to obtain the available preset templates for the input file. When you submit a transcoding job, set TemplateId to the ID of an available preset template. If you specify a preset template that is not in the available preset templates, the transcoding job fails.
        If you use a **static preset template** to transcode an input file, you do not need to submit a preset template analysis job.
        If you want to use multiple accounts in MPS, you can create Resource Access Management (RAM) users by using your Alibaba Cloud account. For more information, see [Create a RAM user and grant permissions to the RAM user](https://help.aliyun.com/document_detail/42841.html). If the Alibaba Cloud account that is used to query transcoding jobs is not the one that is used to submit the transcoding jobs, no data is returned.
        For information about transcoding FAQ, see [FAQ about MPS](https://help.aliyun.com/document_detail/38986.html).
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not UtilClient.is_unset(request.output_location):
            query['OutputLocation'] = request.output_location
        if not UtilClient.is_unset(request.outputs):
            query['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_jobs(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
    ) -> mts_20140618_models.SubmitJobsResponse:
        """
        @summary Submits transcoding jobs. If the transcoding jobs and workflows created in the ApsaraVideo Media Processing (MPS) console cannot meet your business requirements, you can call the SubmitJobs operation to submit transcoding jobs. Specify transcoding parameters as required when you call the SubmitJobs operation.
        
        @description    SubmitJobs is an asynchronous operation. After you submit transcoding jobs, the jobs are added to an MPS queue to be scheduled and run. The transcoding jobs may not have been complete when the response is returned. After you call this operation, you can call the [QueryJobList](https://help.aliyun.com/document_detail/602836.html) operation to query the job results. You can also associate a Message Service (MNS) queue or topic with the MPS queue to receive notifications on the jobs. For more information, see [Receive notifications](https://www.alibabacloud.com/help/zh/apsaravideo-for-media-processing/latest/receive-message-notifications).
        An input file can be up to 100 GB in size. If the size of the input file exceeds this limit, the job may fail.
        If you use an **intelligent preset template** to transcode an input file, you must first call the [SubmitAnalysisJob](https://help.aliyun.com/document_detail/29223.html) operation to submit a preset template analysis job. After the analysis job is complete, you can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html)operation to obtain the available preset templates for the input file. When you submit a transcoding job, set TemplateId to the ID of an available preset template. If you specify a preset template that is not in the available preset templates, the transcoding job fails.
        If you use a **static preset template** to transcode an input file, you do not need to submit a preset template analysis job.
        If you want to use multiple accounts in MPS, you can create Resource Access Management (RAM) users by using your Alibaba Cloud account. For more information, see [Create a RAM user and grant permissions to the RAM user](https://help.aliyun.com/document_detail/42841.html). If the Alibaba Cloud account that is used to query transcoding jobs is not the one that is used to submit the transcoding jobs, no data is returned.
        For information about transcoding FAQ, see [FAQ about MPS](https://help.aliyun.com/document_detail/38986.html).
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitJobsRequest
        @return: SubmitJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_jobs_with_options(request, runtime)

    async def submit_jobs_async(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
    ) -> mts_20140618_models.SubmitJobsResponse:
        """
        @summary Submits transcoding jobs. If the transcoding jobs and workflows created in the ApsaraVideo Media Processing (MPS) console cannot meet your business requirements, you can call the SubmitJobs operation to submit transcoding jobs. Specify transcoding parameters as required when you call the SubmitJobs operation.
        
        @description    SubmitJobs is an asynchronous operation. After you submit transcoding jobs, the jobs are added to an MPS queue to be scheduled and run. The transcoding jobs may not have been complete when the response is returned. After you call this operation, you can call the [QueryJobList](https://help.aliyun.com/document_detail/602836.html) operation to query the job results. You can also associate a Message Service (MNS) queue or topic with the MPS queue to receive notifications on the jobs. For more information, see [Receive notifications](https://www.alibabacloud.com/help/zh/apsaravideo-for-media-processing/latest/receive-message-notifications).
        An input file can be up to 100 GB in size. If the size of the input file exceeds this limit, the job may fail.
        If you use an **intelligent preset template** to transcode an input file, you must first call the [SubmitAnalysisJob](https://help.aliyun.com/document_detail/29223.html) operation to submit a preset template analysis job. After the analysis job is complete, you can call the [QueryAnalysisJobList](https://help.aliyun.com/document_detail/29224.html)operation to obtain the available preset templates for the input file. When you submit a transcoding job, set TemplateId to the ID of an available preset template. If you specify a preset template that is not in the available preset templates, the transcoding job fails.
        If you use a **static preset template** to transcode an input file, you do not need to submit a preset template analysis job.
        If you want to use multiple accounts in MPS, you can create Resource Access Management (RAM) users by using your Alibaba Cloud account. For more information, see [Create a RAM user and grant permissions to the RAM user](https://help.aliyun.com/document_detail/42841.html). If the Alibaba Cloud account that is used to query transcoding jobs is not the one that is used to submit the transcoding jobs, no data is returned.
        For information about transcoding FAQ, see [FAQ about MPS](https://help.aliyun.com/document_detail/38986.html).
        ### [](#qps)QPS limits
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limits](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitJobsRequest
        @return: SubmitJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_jobs_with_options_async(request, runtime)

    def submit_media_censor_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        """
        @summary Submits a content moderation job.
        
        @description The job that you submit by calling this operation is run in asynchronous mode. The job is added to an ApsaraVideo Media Processing (MPS) queue and then scheduled, queued, and run. You can call the [QueryMediaCensorJobDetail](https://help.aliyun.com/document_detail/91779.html) operation or configure an asynchronous notification to obtain the job result.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaCensorJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitMediaCensorJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.barrages):
            query['Barrages'] = request.barrages
        if not UtilClient.is_unset(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.external_url):
            query['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.video_censor_config):
            query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaCensorJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_censor_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        """
        @summary Submits a content moderation job.
        
        @description The job that you submit by calling this operation is run in asynchronous mode. The job is added to an ApsaraVideo Media Processing (MPS) queue and then scheduled, queued, and run. You can call the [QueryMediaCensorJobDetail](https://help.aliyun.com/document_detail/91779.html) operation or configure an asynchronous notification to obtain the job result.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaCensorJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitMediaCensorJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.barrages):
            query['Barrages'] = request.barrages
        if not UtilClient.is_unset(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.external_url):
            query['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.video_censor_config):
            query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaCensorJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_censor_job(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        """
        @summary Submits a content moderation job.
        
        @description The job that you submit by calling this operation is run in asynchronous mode. The job is added to an ApsaraVideo Media Processing (MPS) queue and then scheduled, queued, and run. You can call the [QueryMediaCensorJobDetail](https://help.aliyun.com/document_detail/91779.html) operation or configure an asynchronous notification to obtain the job result.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaCensorJobRequest
        @return: SubmitMediaCensorJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_media_censor_job_with_options(request, runtime)

    async def submit_media_censor_job_async(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        """
        @summary Submits a content moderation job.
        
        @description The job that you submit by calling this operation is run in asynchronous mode. The job is added to an ApsaraVideo Media Processing (MPS) queue and then scheduled, queued, and run. You can call the [QueryMediaCensorJobDetail](https://help.aliyun.com/document_detail/91779.html) operation or configure an asynchronous notification to obtain the job result.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaCensorJobRequest
        @return: SubmitMediaCensorJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_censor_job_with_options_async(request, runtime)

    def submit_media_info_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        """
        @summary Submits a media information analysis job.
        
        @description After you call the SubmitMediaInfoJob operation, ApsaraVideo Media Processing (MPS) analyzes the input media file and generates the analysis results. You can call the [QueryMediaInfoJobList](https://help.aliyun.com/document_detail/29221.html) operation to query the analysis results.
        > We recommend that you submit a media information analysis job after you confirm that the media file is uploaded to Object Storage Service (OSS). You can configure upload callbacks to be notified of the upload status of files.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaInfoJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitMediaInfoJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_info_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        """
        @summary Submits a media information analysis job.
        
        @description After you call the SubmitMediaInfoJob operation, ApsaraVideo Media Processing (MPS) analyzes the input media file and generates the analysis results. You can call the [QueryMediaInfoJobList](https://help.aliyun.com/document_detail/29221.html) operation to query the analysis results.
        > We recommend that you submit a media information analysis job after you confirm that the media file is uploaded to Object Storage Service (OSS). You can configure upload callbacks to be notified of the upload status of files.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaInfoJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitMediaInfoJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaInfoJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_info_job(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        """
        @summary Submits a media information analysis job.
        
        @description After you call the SubmitMediaInfoJob operation, ApsaraVideo Media Processing (MPS) analyzes the input media file and generates the analysis results. You can call the [QueryMediaInfoJobList](https://help.aliyun.com/document_detail/29221.html) operation to query the analysis results.
        > We recommend that you submit a media information analysis job after you confirm that the media file is uploaded to Object Storage Service (OSS). You can configure upload callbacks to be notified of the upload status of files.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaInfoJobRequest
        @return: SubmitMediaInfoJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_media_info_job_with_options(request, runtime)

    async def submit_media_info_job_async(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        """
        @summary Submits a media information analysis job.
        
        @description After you call the SubmitMediaInfoJob operation, ApsaraVideo Media Processing (MPS) analyzes the input media file and generates the analysis results. You can call the [QueryMediaInfoJobList](https://help.aliyun.com/document_detail/29221.html) operation to query the analysis results.
        > We recommend that you submit a media information analysis job after you confirm that the media file is uploaded to Object Storage Service (OSS). You can configure upload callbacks to be notified of the upload status of files.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitMediaInfoJobRequest
        @return: SubmitMediaInfoJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_info_job_with_options_async(request, runtime)

    def submit_smarttag_job_with_options(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        """
        @param request: SubmitSmarttagJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSmarttagJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smarttag_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        """
        @param request: SubmitSmarttagJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSmarttagJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smarttag_job(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        """
        @param request: SubmitSmarttagJobRequest
        @return: SubmitSmarttagJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_smarttag_job_with_options(request, runtime)

    async def submit_smarttag_job_async(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        """
        @param request: SubmitSmarttagJobRequest
        @return: SubmitSmarttagJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_smarttag_job_with_options_async(request, runtime)

    def submit_snapshot_job_with_options(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        """
        @summary Submits a snapshot job.
        
        @description    Only JPG images can be generated by calling this operation.
        Asynchronous mode: This operation may return a response before snapshots are captured. Snapshot jobs are queued in the background and asynchronously processed by ApsaraVideo Media Processing (MPS). If the **Interval** or **Num** parameter is set, the snapshot job is processed in asynchronous mode. For more information about FAQ about capturing snapshots, see [FAQ about taking snapshots](https://help.aliyun.com/document_detail/60805.html).
        Notifications: When you submit a snapshot job, the **PipelineId** parameter is required. An asynchronous message is sent only after the notification feature is enabled for the MPS queue.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitSnapshotJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSnapshotJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        """
        @summary Submits a snapshot job.
        
        @description    Only JPG images can be generated by calling this operation.
        Asynchronous mode: This operation may return a response before snapshots are captured. Snapshot jobs are queued in the background and asynchronously processed by ApsaraVideo Media Processing (MPS). If the **Interval** or **Num** parameter is set, the snapshot job is processed in asynchronous mode. For more information about FAQ about capturing snapshots, see [FAQ about taking snapshots](https://help.aliyun.com/document_detail/60805.html).
        Notifications: When you submit a snapshot job, the **PipelineId** parameter is required. An asynchronous message is sent only after the notification feature is enabled for the MPS queue.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitSnapshotJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSnapshotJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_snapshot_job(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        """
        @summary Submits a snapshot job.
        
        @description    Only JPG images can be generated by calling this operation.
        Asynchronous mode: This operation may return a response before snapshots are captured. Snapshot jobs are queued in the background and asynchronously processed by ApsaraVideo Media Processing (MPS). If the **Interval** or **Num** parameter is set, the snapshot job is processed in asynchronous mode. For more information about FAQ about capturing snapshots, see [FAQ about taking snapshots](https://help.aliyun.com/document_detail/60805.html).
        Notifications: When you submit a snapshot job, the **PipelineId** parameter is required. An asynchronous message is sent only after the notification feature is enabled for the MPS queue.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitSnapshotJobRequest
        @return: SubmitSnapshotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    async def submit_snapshot_job_async(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        """
        @summary Submits a snapshot job.
        
        @description    Only JPG images can be generated by calling this operation.
        Asynchronous mode: This operation may return a response before snapshots are captured. Snapshot jobs are queued in the background and asynchronously processed by ApsaraVideo Media Processing (MPS). If the **Interval** or **Num** parameter is set, the snapshot job is processed in asynchronous mode. For more information about FAQ about capturing snapshots, see [FAQ about taking snapshots](https://help.aliyun.com/document_detail/60805.html).
        Notifications: When you submit a snapshot job, the **PipelineId** parameter is required. An asynchronous message is sent only after the notification feature is enabled for the MPS queue.
        ### QPS limit
        You can call this operation up to 50 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: SubmitSnapshotJobRequest
        @return: SubmitSnapshotJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_snapshot_job_with_options_async(request, runtime)

    def tag_custom_person_with_options(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        """
        @summary The description of the figure. The description can be up to 512 characters in length.
        
        @description The response parameters.
        
        @param request: TagCustomPersonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagCustomPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_description):
            query['CategoryDescription'] = request.category_description
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_description):
            query['PersonDescription'] = request.person_description
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.person_name):
            query['PersonName'] = request.person_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagCustomPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.TagCustomPersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_custom_person_with_options_async(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        """
        @summary The description of the figure. The description can be up to 512 characters in length.
        
        @description The response parameters.
        
        @param request: TagCustomPersonRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagCustomPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_description):
            query['CategoryDescription'] = request.category_description
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_description):
            query['PersonDescription'] = request.person_description
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.person_name):
            query['PersonName'] = request.person_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagCustomPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.TagCustomPersonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_custom_person(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        """
        @summary The description of the figure. The description can be up to 512 characters in length.
        
        @description The response parameters.
        
        @param request: TagCustomPersonRequest
        @return: TagCustomPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_custom_person_with_options(request, runtime)

    async def tag_custom_person_async(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        """
        @summary The description of the figure. The description can be up to 512 characters in length.
        
        @description The response parameters.
        
        @param request: TagCustomPersonRequest
        @return: TagCustomPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_custom_person_with_options_async(request, runtime)

    def unbind_input_bucket_with_options(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        """
        @summary Unbinds an input media bucket from the media library.
        
        @description # Usage notes
        You can call this operation to unbind an input media bucket from the media library based on the name of the output media bucket.
        # QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnbindInputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindInputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindInputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_input_bucket_with_options_async(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        """
        @summary Unbinds an input media bucket from the media library.
        
        @description # Usage notes
        You can call this operation to unbind an input media bucket from the media library based on the name of the output media bucket.
        # QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnbindInputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindInputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindInputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_input_bucket(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        """
        @summary Unbinds an input media bucket from the media library.
        
        @description # Usage notes
        You can call this operation to unbind an input media bucket from the media library based on the name of the output media bucket.
        # QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnbindInputBucketRequest
        @return: UnbindInputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_input_bucket_with_options(request, runtime)

    async def unbind_input_bucket_async(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        """
        @summary Unbinds an input media bucket from the media library.
        
        @description # Usage notes
        You can call this operation to unbind an input media bucket from the media library based on the name of the output media bucket.
        # QPS limits
        You can call this API operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnbindInputBucketRequest
        @return: UnbindInputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_input_bucket_with_options_async(request, runtime)

    def unbind_output_bucket_with_options(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        """
        @summary You can call this operation to unbind an output media bucket from the media library based on the name of the output media bucket.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @description The name of the output media bucket to be unbound. To obtain the media bucket name, you can log on to the *ApsaraVideo Media Processing (MPS)** console and choose **Workflows** > **Media Buckets** in the left-side navigation pane. Alternatively, you can log on to the **Object Storage Service (OSS) console** and click **My OSS Paths**.
        
        @param request: UnbindOutputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindOutputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindOutputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_output_bucket_with_options_async(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        """
        @summary You can call this operation to unbind an output media bucket from the media library based on the name of the output media bucket.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @description The name of the output media bucket to be unbound. To obtain the media bucket name, you can log on to the *ApsaraVideo Media Processing (MPS)** console and choose **Workflows** > **Media Buckets** in the left-side navigation pane. Alternatively, you can log on to the **Object Storage Service (OSS) console** and click **My OSS Paths**.
        
        @param request: UnbindOutputBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindOutputBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindOutputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_output_bucket(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        """
        @summary You can call this operation to unbind an output media bucket from the media library based on the name of the output media bucket.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @description The name of the output media bucket to be unbound. To obtain the media bucket name, you can log on to the *ApsaraVideo Media Processing (MPS)** console and choose **Workflows** > **Media Buckets** in the left-side navigation pane. Alternatively, you can log on to the **Object Storage Service (OSS) console** and click **My OSS Paths**.
        
        @param request: UnbindOutputBucketRequest
        @return: UnbindOutputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_output_bucket_with_options(request, runtime)

    async def unbind_output_bucket_async(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        """
        @summary You can call this operation to unbind an output media bucket from the media library based on the name of the output media bucket.
        ## QPS limit
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @description The name of the output media bucket to be unbound. To obtain the media bucket name, you can log on to the *ApsaraVideo Media Processing (MPS)** console and choose **Workflows** > **Media Buckets** in the left-side navigation pane. Alternatively, you can log on to the **Object Storage Service (OSS) console** and click **My OSS Paths**.
        
        @param request: UnbindOutputBucketRequest
        @return: UnbindOutputBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_output_bucket_with_options_async(request, runtime)

    def unregister_custom_face_with_options(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        """
        @summary Deletes a custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        
        @description You can call this operation to delete a specific custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnregisterCustomFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnregisterCustomFaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.face_id):
            query['FaceId'] = request.face_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnregisterCustomFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unregister_custom_face_with_options_async(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        """
        @summary Deletes a custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        
        @description You can call this operation to delete a specific custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnregisterCustomFaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnregisterCustomFaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.face_id):
            query['FaceId'] = request.face_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnregisterCustomFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unregister_custom_face(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        """
        @summary Deletes a custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        
        @description You can call this operation to delete a specific custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnregisterCustomFaceRequest
        @return: UnregisterCustomFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unregister_custom_face_with_options(request, runtime)

    async def unregister_custom_face_async(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        """
        @summary Deletes a custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        
        @description You can call this operation to delete a specific custom face, all the custom faces that are registered in a custom figure library, or a custom figure library.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped, and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UnregisterCustomFaceRequest
        @return: UnregisterCustomFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unregister_custom_face_with_options_async(request, runtime)

    def update_media_with_options(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaResponse:
        """
        @summary Updates the basic information about a media file.
        
        @description The basic information that you can update by calling this operation includes the title, description, and category of a media file. This operation applies to a full update. You must set all the parameters unless you want to replace the value of a specific parameter with a NULL value.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaResponse:
        """
        @summary Updates the basic information about a media file.
        
        @description The basic information that you can update by calling this operation includes the title, description, and category of a media file. This operation applies to a full update. You must set all the parameters unless you want to replace the value of a specific parameter with a NULL value.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
    ) -> mts_20140618_models.UpdateMediaResponse:
        """
        @summary Updates the basic information about a media file.
        
        @description The basic information that you can update by calling this operation includes the title, description, and category of a media file. This operation applies to a full update. You must set all the parameters unless you want to replace the value of a specific parameter with a NULL value.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaRequest
        @return: UpdateMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_media_with_options(request, runtime)

    async def update_media_async(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
    ) -> mts_20140618_models.UpdateMediaResponse:
        """
        @summary Updates the basic information about a media file.
        
        @description The basic information that you can update by calling this operation includes the title, description, and category of a media file. This operation applies to a full update. You must set all the parameters unless you want to replace the value of a specific parameter with a NULL value.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaRequest
        @return: UpdateMediaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_media_with_options_async(request, runtime)

    def update_media_category_with_options(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        """
        @summary Updates the category to which a media file belongs.
        
        @description You can call this operation to update only the category of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_category_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        """
        @summary Updates the category to which a media file belongs.
        
        @description You can call this operation to update only the category of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_category(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        """
        @summary Updates the category to which a media file belongs.
        
        @description You can call this operation to update only the category of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaCategoryRequest
        @return: UpdateMediaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_media_category_with_options(request, runtime)

    async def update_media_category_async(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        """
        @summary Updates the category to which a media file belongs.
        
        @description You can call this operation to update only the category of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaCategoryRequest
        @return: UpdateMediaCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_media_category_with_options_async(request, runtime)

    def update_media_cover_with_options(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        """
        @summary Updates the thumbnail of a media file.
        
        @description You can call this operation to update only the thumbnail of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ## Limits on QPS
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: UpdateMediaCoverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaCoverResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCover',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCoverResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_cover_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        """
        @summary Updates the thumbnail of a media file.
        
        @description You can call this operation to update only the thumbnail of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ## Limits on QPS
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: UpdateMediaCoverRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaCoverResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCover',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCoverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_cover(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        """
        @summary Updates the thumbnail of a media file.
        
        @description You can call this operation to update only the thumbnail of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ## Limits on QPS
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: UpdateMediaCoverRequest
        @return: UpdateMediaCoverResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_media_cover_with_options(request, runtime)

    async def update_media_cover_async(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        """
        @summary Updates the thumbnail of a media file.
        
        @description You can call this operation to update only the thumbnail of a media file. For more information about how to update all the information about a media file, see [UpdateMedia](https://help.aliyun.com/document_detail/44464.html).
        ## Limits on QPS
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limits](https://www.alibabacloud.com/help/en/apsaravideo-for-media-processing/latest/qps-limit).
        
        @param request: UpdateMediaCoverRequest
        @return: UpdateMediaCoverResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_media_cover_with_options_async(request, runtime)

    def update_media_publish_state_with_options(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        """
        @summary Updates the publishing status of a media file.
        
        @description The published state indicates that the access control list (ACL) of media playback resources and snapshot files is set to inherit the ACL of the bucket to which they belong. The unpublished state indicates that the ACL of media playback resources and snapshot files is set to private.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaPublishStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaPublishStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish):
            query['Publish'] = request.publish
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaPublishState',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaPublishStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_publish_state_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        """
        @summary Updates the publishing status of a media file.
        
        @description The published state indicates that the access control list (ACL) of media playback resources and snapshot files is set to inherit the ACL of the bucket to which they belong. The unpublished state indicates that the ACL of media playback resources and snapshot files is set to private.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaPublishStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaPublishStateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish):
            query['Publish'] = request.publish
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaPublishState',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaPublishStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_publish_state(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        """
        @summary Updates the publishing status of a media file.
        
        @description The published state indicates that the access control list (ACL) of media playback resources and snapshot files is set to inherit the ACL of the bucket to which they belong. The unpublished state indicates that the ACL of media playback resources and snapshot files is set to private.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaPublishStateRequest
        @return: UpdateMediaPublishStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_media_publish_state_with_options(request, runtime)

    async def update_media_publish_state_async(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        """
        @summary Updates the publishing status of a media file.
        
        @description The published state indicates that the access control list (ACL) of media playback resources and snapshot files is set to inherit the ACL of the bucket to which they belong. The unpublished state indicates that the ACL of media playback resources and snapshot files is set to private.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaPublishStateRequest
        @return: UpdateMediaPublishStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_media_publish_state_with_options_async(request, runtime)

    def update_media_workflow_with_options(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        """
        @summary Updates the topology of a media workflow.
        
        @description    You can call this operation to update the topology of a media workflow. To update the trigger mode of a media workflow, call the [UpdateMediaWorkflowTriggerMode](https://help.aliyun.com/document_detail/70372.html) operation.
        After you delete or deactivate a media workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        <warning>Deleting or deactivating a workflow will not affect tasks that have already been submitted. If a workflow is deleted or deactivated after a task has been submitted, tasks that are already in the processing queue will not be canceled and will be executed normally and charged the corresponding fees.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).>
        
        @param request: UpdateMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        """
        @summary Updates the topology of a media workflow.
        
        @description    You can call this operation to update the topology of a media workflow. To update the trigger mode of a media workflow, call the [UpdateMediaWorkflowTriggerMode](https://help.aliyun.com/document_detail/70372.html) operation.
        After you delete or deactivate a media workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        <warning>Deleting or deactivating a workflow will not affect tasks that have already been submitted. If a workflow is deleted or deactivated after a task has been submitted, tasks that are already in the processing queue will not be canceled and will be executed normally and charged the corresponding fees.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).>
        
        @param request: UpdateMediaWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_workflow(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        """
        @summary Updates the topology of a media workflow.
        
        @description    You can call this operation to update the topology of a media workflow. To update the trigger mode of a media workflow, call the [UpdateMediaWorkflowTriggerMode](https://help.aliyun.com/document_detail/70372.html) operation.
        After you delete or deactivate a media workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        <warning>Deleting or deactivating a workflow will not affect tasks that have already been submitted. If a workflow is deleted or deactivated after a task has been submitted, tasks that are already in the processing queue will not be canceled and will be executed normally and charged the corresponding fees.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).>
        
        @param request: UpdateMediaWorkflowRequest
        @return: UpdateMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_media_workflow_with_options(request, runtime)

    async def update_media_workflow_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        """
        @summary Updates the topology of a media workflow.
        
        @description    You can call this operation to update the topology of a media workflow. To update the trigger mode of a media workflow, call the [UpdateMediaWorkflowTriggerMode](https://help.aliyun.com/document_detail/70372.html) operation.
        After you delete or deactivate a media workflow, the workflow cannot be used. In this case, the workflow is not automatically triggered when you upload a file to the bucket specified by the workflow.
        <warning>Deleting or deactivating a workflow will not affect tasks that have already been submitted. If a workflow is deleted or deactivated after a task has been submitted, tasks that are already in the processing queue will not be canceled and will be executed normally and charged the corresponding fees.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).>
        
        @param request: UpdateMediaWorkflowRequest
        @return: UpdateMediaWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_media_workflow_with_options_async(request, runtime)

    def update_media_workflow_trigger_mode_with_options(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        """
        @summary Updates the trigger mode of a media workflow.
        
        @description You can call this operation only to modify the trigger mode of a media workflow. To modify other information about the workflow, call the [UpdateMediaWorkflow](https://help.aliyun.com/document_detail/44438.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaWorkflowTriggerModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaWorkflowTriggerModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflowTriggerMode',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_workflow_trigger_mode_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        """
        @summary Updates the trigger mode of a media workflow.
        
        @description You can call this operation only to modify the trigger mode of a media workflow. To modify other information about the workflow, call the [UpdateMediaWorkflow](https://help.aliyun.com/document_detail/44438.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaWorkflowTriggerModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMediaWorkflowTriggerModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflowTriggerMode',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_workflow_trigger_mode(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        """
        @summary Updates the trigger mode of a media workflow.
        
        @description You can call this operation only to modify the trigger mode of a media workflow. To modify other information about the workflow, call the [UpdateMediaWorkflow](https://help.aliyun.com/document_detail/44438.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaWorkflowTriggerModeRequest
        @return: UpdateMediaWorkflowTriggerModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_media_workflow_trigger_mode_with_options(request, runtime)

    async def update_media_workflow_trigger_mode_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        """
        @summary Updates the trigger mode of a media workflow.
        
        @description You can call this operation only to modify the trigger mode of a media workflow. To modify other information about the workflow, call the [UpdateMediaWorkflow](https://help.aliyun.com/document_detail/44438.html) operation.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateMediaWorkflowTriggerModeRequest
        @return: UpdateMediaWorkflowTriggerModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_media_workflow_trigger_mode_with_options_async(request, runtime)

    def update_pipeline_with_options(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        """
        @summary Updates an ApsaraVideo Media Processing (MPS) queue.
        
        @description    You can call this operation to modify the name, status, and notification settings of the specified MPS queue.
        If a paused MPS queue is selected in a workflow or a job, such as a video review or media fingerprint job, the workflow or job fails.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdatePipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        """
        @summary Updates an ApsaraVideo Media Processing (MPS) queue.
        
        @description    You can call this operation to modify the name, status, and notification settings of the specified MPS queue.
        If a paused MPS queue is selected in a workflow or a job, such as a video review or media fingerprint job, the workflow or job fails.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdatePipelineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        """
        @summary Updates an ApsaraVideo Media Processing (MPS) queue.
        
        @description    You can call this operation to modify the name, status, and notification settings of the specified MPS queue.
        If a paused MPS queue is selected in a workflow or a job, such as a video review or media fingerprint job, the workflow or job fails.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdatePipelineRequest
        @return: UpdatePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_pipeline_with_options(request, runtime)

    async def update_pipeline_async(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        """
        @summary Updates an ApsaraVideo Media Processing (MPS) queue.
        
        @description    You can call this operation to modify the name, status, and notification settings of the specified MPS queue.
        If a paused MPS queue is selected in a workflow or a job, such as a video review or media fingerprint job, the workflow or job fails.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdatePipelineRequest
        @return: UpdatePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_pipeline_with_options_async(request, runtime)

    def update_smarttag_template_with_options(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        """
        @summary 更新智能标签模板接口支持cpv
        
        @param request: UpdateSmarttagTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmarttagTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not UtilClient.is_unset(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        """
        @summary 更新智能标签模板接口支持cpv
        
        @param request: UpdateSmarttagTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSmarttagTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not UtilClient.is_unset(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smarttag_template(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        """
        @summary 更新智能标签模板接口支持cpv
        
        @param request: UpdateSmarttagTemplateRequest
        @return: UpdateSmarttagTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_smarttag_template_with_options(request, runtime)

    async def update_smarttag_template_async(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        """
        @summary 更新智能标签模板接口支持cpv
        
        @param request: UpdateSmarttagTemplateRequest
        @return: UpdateSmarttagTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_smarttag_template_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        """
        @description A custom transcoding template cannot be updated if it is being used by a job that has been submitted.The ID of the template. You can obtain the template ID from the response of the [AddTemplate](https://help.aliyun.com/document_detail/213306.html) operation.
        ### QPS limits
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        """
        @description A custom transcoding template cannot be updated if it is being used by a job that has been submitted.The ID of the template. You can obtain the template ID from the response of the [AddTemplate](https://help.aliyun.com/document_detail/213306.html) operation.
        ### QPS limits
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        """
        @description A custom transcoding template cannot be updated if it is being used by a job that has been submitted.The ID of the template. You can obtain the template ID from the response of the [AddTemplate](https://help.aliyun.com/document_detail/213306.html) operation.
        ### QPS limits
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        """
        @description A custom transcoding template cannot be updated if it is being used by a job that has been submitted.The ID of the template. You can obtain the template ID from the response of the [AddTemplate](https://help.aliyun.com/document_detail/213306.html) operation.
        ### QPS limits
        You can call this operation up to 100 times per second. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def update_water_mark_template_with_options(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        """
        @summary Updates the name and configurations of the specified watermark template.
        
        @description    You can call this operation to update the information about a watermark template based on the ID of the watermark template. For example, you can update the name and configurations of a watermark template.
        A watermark template cannot be updated if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaterMarkTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        """
        @summary Updates the name and configurations of the specified watermark template.
        
        @description    You can call this operation to update the information about a watermark template based on the ID of the watermark template. For example, you can update the name and configurations of a watermark template.
        A watermark template cannot be updated if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateWaterMarkTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaterMarkTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_water_mark_template(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        """
        @summary Updates the name and configurations of the specified watermark template.
        
        @description    You can call this operation to update the information about a watermark template based on the ID of the watermark template. For example, you can update the name and configurations of a watermark template.
        A watermark template cannot be updated if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateWaterMarkTemplateRequest
        @return: UpdateWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_water_mark_template_with_options(request, runtime)

    async def update_water_mark_template_async(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        """
        @summary Updates the name and configurations of the specified watermark template.
        
        @description    You can call this operation to update the information about a watermark template based on the ID of the watermark template. For example, you can update the name and configurations of a watermark template.
        A watermark template cannot be updated if it is being used by a job that has been submitted.
        ### QPS limit
        You can call this operation up to 100 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation. For more information, see [QPS limit](https://help.aliyun.com/document_detail/342832.html).
        
        @param request: UpdateWaterMarkTemplateRequest
        @return: UpdateWaterMarkTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_water_mark_template_with_options_async(request, runtime)
