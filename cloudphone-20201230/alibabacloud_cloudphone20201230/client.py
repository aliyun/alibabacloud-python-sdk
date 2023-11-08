# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudphone20201230 import models as cloudphone_20201230_models
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
        self._endpoint = self.get_endpoint('cloudphone', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_task_with_options(
        self,
        request: cloudphone_20201230_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.CancelTaskResponse:
        """
        When you call this operation, take note of the following item:
        *   If the task is executed, you fail to call the operation and an error is returned.
        
        @param request: CancelTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: cloudphone_20201230_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.CancelTaskResponse:
        """
        When you call this operation, take note of the following item:
        *   If the task is executed, you fail to call the operation and an error is returned.
        
        @param request: CancelTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        request: cloudphone_20201230_models.CancelTaskRequest,
    ) -> cloudphone_20201230_models.CancelTaskResponse:
        """
        When you call this operation, take note of the following item:
        *   If the task is executed, you fail to call the operation and an error is returned.
        
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: cloudphone_20201230_models.CancelTaskRequest,
    ) -> cloudphone_20201230_models.CancelTaskResponse:
        """
        When you call this operation, take note of the following item:
        *   If the task is executed, you fail to call the operation and an error is returned.
        
        @param request: CancelTaskRequest
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def copy_image_with_options(
        self,
        request: cloudphone_20201230_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.CopyImageResponse:
        """
        When you call this operation, take note of the following items:
        *   The custom image that you want to copy must be in the Available state.
        *   You can only copy images within your own Alibaba Cloud account. Images cannot be copied from one account to another.
        *   A single region can have only one image copy task running at a time. Other image copy tasks queue up for the current task to complete before they run in sequence.
        
        @param request: CopyImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyImage',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.CopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_image_with_options_async(
        self,
        request: cloudphone_20201230_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.CopyImageResponse:
        """
        When you call this operation, take note of the following items:
        *   The custom image that you want to copy must be in the Available state.
        *   You can only copy images within your own Alibaba Cloud account. Images cannot be copied from one account to another.
        *   A single region can have only one image copy task running at a time. Other image copy tasks queue up for the current task to complete before they run in sequence.
        
        @param request: CopyImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyImage',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.CopyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_image(
        self,
        request: cloudphone_20201230_models.CopyImageRequest,
    ) -> cloudphone_20201230_models.CopyImageResponse:
        """
        When you call this operation, take note of the following items:
        *   The custom image that you want to copy must be in the Available state.
        *   You can only copy images within your own Alibaba Cloud account. Images cannot be copied from one account to another.
        *   A single region can have only one image copy task running at a time. Other image copy tasks queue up for the current task to complete before they run in sequence.
        
        @param request: CopyImageRequest
        @return: CopyImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_image_with_options(request, runtime)

    async def copy_image_async(
        self,
        request: cloudphone_20201230_models.CopyImageRequest,
    ) -> cloudphone_20201230_models.CopyImageResponse:
        """
        When you call this operation, take note of the following items:
        *   The custom image that you want to copy must be in the Available state.
        *   You can only copy images within your own Alibaba Cloud account. Images cannot be copied from one account to another.
        *   A single region can have only one image copy task running at a time. Other image copy tasks queue up for the current task to complete before they run in sequence.
        
        @param request: CopyImageRequest
        @return: CopyImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_image_with_options_async(request, runtime)

    def create_image_with_options(
        self,
        request: cloudphone_20201230_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.CreateImageResponse:
        """
        When you call this operation, take note of the following items:
        *   You need to only specify the ID (InstanceId) of an ECP instance. The instance is used as a template. The instance must be in the Running or Stopped state.
        *   You can use the created custom image only if the image is in the Available state.
        
        @param request: CreateImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.CreateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: cloudphone_20201230_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.CreateImageResponse:
        """
        When you call this operation, take note of the following items:
        *   You need to only specify the ID (InstanceId) of an ECP instance. The instance is used as a template. The instance must be in the Running or Stopped state.
        *   You can use the created custom image only if the image is in the Available state.
        
        @param request: CreateImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.CreateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image(
        self,
        request: cloudphone_20201230_models.CreateImageRequest,
    ) -> cloudphone_20201230_models.CreateImageResponse:
        """
        When you call this operation, take note of the following items:
        *   You need to only specify the ID (InstanceId) of an ECP instance. The instance is used as a template. The instance must be in the Running or Stopped state.
        *   You can use the created custom image only if the image is in the Available state.
        
        @param request: CreateImageRequest
        @return: CreateImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    async def create_image_async(
        self,
        request: cloudphone_20201230_models.CreateImageRequest,
    ) -> cloudphone_20201230_models.CreateImageResponse:
        """
        When you call this operation, take note of the following items:
        *   You need to only specify the ID (InstanceId) of an ECP instance. The instance is used as a template. The instance must be in the Running or Stopped state.
        *   You can use the created custom image only if the image is in the Available state.
        
        @param request: CreateImageRequest
        @return: CreateImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_with_options_async(request, runtime)

    def delete_images_with_options(
        self,
        request: cloudphone_20201230_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.DeleteImagesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   Images that are shared with recipient users can be deleted only after you unshare the images.
        *   Images that are used by other Elastic Cloud Phone (ECP) instances can only be forcefully deleted.
        
        @param request: DeleteImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImages',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.DeleteImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_images_with_options_async(
        self,
        request: cloudphone_20201230_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.DeleteImagesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   Images that are shared with recipient users can be deleted only after you unshare the images.
        *   Images that are used by other Elastic Cloud Phone (ECP) instances can only be forcefully deleted.
        
        @param request: DeleteImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImages',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.DeleteImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_images(
        self,
        request: cloudphone_20201230_models.DeleteImagesRequest,
    ) -> cloudphone_20201230_models.DeleteImagesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   Images that are shared with recipient users can be deleted only after you unshare the images.
        *   Images that are used by other Elastic Cloud Phone (ECP) instances can only be forcefully deleted.
        
        @param request: DeleteImagesRequest
        @return: DeleteImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    async def delete_images_async(
        self,
        request: cloudphone_20201230_models.DeleteImagesRequest,
    ) -> cloudphone_20201230_models.DeleteImagesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   Images that are shared with recipient users can be deleted only after you unshare the images.
        *   Images that are used by other Elastic Cloud Phone (ECP) instances can only be forcefully deleted.
        
        @param request: DeleteImagesRequest
        @return: DeleteImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_images_with_options_async(request, runtime)

    def delete_instances_with_options(
        self,
        request: cloudphone_20201230_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.DeleteInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.DeleteInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.DeleteInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.DeleteInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instances(
        self,
        request: cloudphone_20201230_models.DeleteInstancesRequest,
    ) -> cloudphone_20201230_models.DeleteInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instances_with_options(request, runtime)

    async def delete_instances_async(
        self,
        request: cloudphone_20201230_models.DeleteInstancesRequest,
    ) -> cloudphone_20201230_models.DeleteInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instances_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: cloudphone_20201230_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.DeleteKeyPairsResponse:
        """
        Before you call the operation, take note of the following items:
        *   If you delete a key pair of a cloud phone, you cannot query the key pair of the cloud phone by calling the ListKeyPairs operation.
        *   If you delete a key pair that is bound to an existing Elastic Cloud Phone (ECP) instance, Alibaba Cloud no longer saves the key pair for you, but the ECP instance can use the key pair as expected.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.DeleteKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: cloudphone_20201230_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.DeleteKeyPairsResponse:
        """
        Before you call the operation, take note of the following items:
        *   If you delete a key pair of a cloud phone, you cannot query the key pair of the cloud phone by calling the ListKeyPairs operation.
        *   If you delete a key pair that is bound to an existing Elastic Cloud Phone (ECP) instance, Alibaba Cloud no longer saves the key pair for you, but the ECP instance can use the key pair as expected.
        
        @param request: DeleteKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKeyPairs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.DeleteKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_key_pairs(
        self,
        request: cloudphone_20201230_models.DeleteKeyPairsRequest,
    ) -> cloudphone_20201230_models.DeleteKeyPairsResponse:
        """
        Before you call the operation, take note of the following items:
        *   If you delete a key pair of a cloud phone, you cannot query the key pair of the cloud phone by calling the ListKeyPairs operation.
        *   If you delete a key pair that is bound to an existing Elastic Cloud Phone (ECP) instance, Alibaba Cloud no longer saves the key pair for you, but the ECP instance can use the key pair as expected.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: cloudphone_20201230_models.DeleteKeyPairsRequest,
    ) -> cloudphone_20201230_models.DeleteKeyPairsResponse:
        """
        Before you call the operation, take note of the following items:
        *   If you delete a key pair of a cloud phone, you cannot query the key pair of the cloud phone by calling the ListKeyPairs operation.
        *   If you delete a key pair that is bound to an existing Elastic Cloud Phone (ECP) instance, Alibaba Cloud no longer saves the key pair for you, but the ECP instance can use the key pair as expected.
        
        @param request: DeleteKeyPairsRequest
        @return: DeleteKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def fetch_file_with_options(
        self,
        request: cloudphone_20201230_models.FetchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.FetchFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchFile',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.FetchFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_file_with_options_async(
        self,
        request: cloudphone_20201230_models.FetchFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.FetchFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchFile',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.FetchFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_file(
        self,
        request: cloudphone_20201230_models.FetchFileRequest,
    ) -> cloudphone_20201230_models.FetchFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_file_with_options(request, runtime)

    async def fetch_file_async(
        self,
        request: cloudphone_20201230_models.FetchFileRequest,
    ) -> cloudphone_20201230_models.FetchFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_file_with_options_async(request, runtime)

    def import_image_with_options(
        self,
        request: cloudphone_20201230_models.ImportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ImportImageResponse:
        """
        When you call this operation, take note of the following items:
        *   Before you import the image, you must upload the image to an Object Storage Service (OSS) bucket. For more information, see [Upload objects](~~31886~~).
        *   When you import an image for the first time, you must use Resource Access Management (RAM) to grant permissions on the access to OSS buckets in advance to obtain [Cloud Resource Access Authorization](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CloudPhone%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCloudPhoneDefaultRole%22%2C%22TemplateId%22%3A%22AliyunCloudPhoneDefaultRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcloudphone.console.aliyun.com%2F%23%2Finstances%22%7D) with one click.
        *   You can import an image only to a region that is the same as that of the OSS bucket to which the image file was imported.
        
        @param request: ImportImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportImage',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ImportImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_image_with_options_async(
        self,
        request: cloudphone_20201230_models.ImportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ImportImageResponse:
        """
        When you call this operation, take note of the following items:
        *   Before you import the image, you must upload the image to an Object Storage Service (OSS) bucket. For more information, see [Upload objects](~~31886~~).
        *   When you import an image for the first time, you must use Resource Access Management (RAM) to grant permissions on the access to OSS buckets in advance to obtain [Cloud Resource Access Authorization](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CloudPhone%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCloudPhoneDefaultRole%22%2C%22TemplateId%22%3A%22AliyunCloudPhoneDefaultRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcloudphone.console.aliyun.com%2F%23%2Finstances%22%7D) with one click.
        *   You can import an image only to a region that is the same as that of the OSS bucket to which the image file was imported.
        
        @param request: ImportImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportImage',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ImportImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_image(
        self,
        request: cloudphone_20201230_models.ImportImageRequest,
    ) -> cloudphone_20201230_models.ImportImageResponse:
        """
        When you call this operation, take note of the following items:
        *   Before you import the image, you must upload the image to an Object Storage Service (OSS) bucket. For more information, see [Upload objects](~~31886~~).
        *   When you import an image for the first time, you must use Resource Access Management (RAM) to grant permissions on the access to OSS buckets in advance to obtain [Cloud Resource Access Authorization](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CloudPhone%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCloudPhoneDefaultRole%22%2C%22TemplateId%22%3A%22AliyunCloudPhoneDefaultRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcloudphone.console.aliyun.com%2F%23%2Finstances%22%7D) with one click.
        *   You can import an image only to a region that is the same as that of the OSS bucket to which the image file was imported.
        
        @param request: ImportImageRequest
        @return: ImportImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_image_with_options(request, runtime)

    async def import_image_async(
        self,
        request: cloudphone_20201230_models.ImportImageRequest,
    ) -> cloudphone_20201230_models.ImportImageResponse:
        """
        When you call this operation, take note of the following items:
        *   Before you import the image, you must upload the image to an Object Storage Service (OSS) bucket. For more information, see [Upload objects](~~31886~~).
        *   When you import an image for the first time, you must use Resource Access Management (RAM) to grant permissions on the access to OSS buckets in advance to obtain [Cloud Resource Access Authorization](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22CloudPhone%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunCloudPhoneDefaultRole%22%2C%22TemplateId%22%3A%22AliyunCloudPhoneDefaultRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fcloudphone.console.aliyun.com%2F%23%2Finstances%22%7D) with one click.
        *   You can import an image only to a region that is the same as that of the OSS bucket to which the image file was imported.
        
        @param request: ImportImageRequest
        @return: ImportImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_image_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: cloudphone_20201230_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ImportKeyPairResponse:
        """
        Usage notes Before you call this operation, take note of the following items:
        *   You can create up to 500 key pairs in each region.
        *   The imported public key pair must generate the public key of a key pair for Android Debug Bridge (ADB).
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ImportKeyPairResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: cloudphone_20201230_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ImportKeyPairResponse:
        """
        Usage notes Before you call this operation, take note of the following items:
        *   You can create up to 500 key pairs in each region.
        *   The imported public key pair must generate the public key of a key pair for Android Debug Bridge (ADB).
        
        @param request: ImportKeyPairRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportKeyPairResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.public_key_body):
            query['PublicKeyBody'] = request.public_key_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportKeyPair',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ImportKeyPairResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_key_pair(
        self,
        request: cloudphone_20201230_models.ImportKeyPairRequest,
    ) -> cloudphone_20201230_models.ImportKeyPairResponse:
        """
        Usage notes Before you call this operation, take note of the following items:
        *   You can create up to 500 key pairs in each region.
        *   The imported public key pair must generate the public key of a key pair for Android Debug Bridge (ADB).
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: cloudphone_20201230_models.ImportKeyPairRequest,
    ) -> cloudphone_20201230_models.ImportKeyPairResponse:
        """
        Usage notes Before you call this operation, take note of the following items:
        *   You can create up to 500 key pairs in each region.
        *   The imported public key pair must generate the public key of a key pair for Android Debug Bridge (ADB).
        
        @param request: ImportKeyPairRequest
        @return: ImportKeyPairResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def install_application_with_options(
        self,
        request: cloudphone_20201230_models.InstallApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.InstallApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallApplication',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.InstallApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_application_with_options_async(
        self,
        request: cloudphone_20201230_models.InstallApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.InstallApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallApplication',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.InstallApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_application(
        self,
        request: cloudphone_20201230_models.InstallApplicationRequest,
    ) -> cloudphone_20201230_models.InstallApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_application_with_options(request, runtime)

    async def install_application_async(
        self,
        request: cloudphone_20201230_models.InstallApplicationRequest,
    ) -> cloudphone_20201230_models.InstallApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_application_with_options_async(request, runtime)

    def list_image_share_permission_with_options(
        self,
        request: cloudphone_20201230_models.ListImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListImageSharePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageSharePermission',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListImageSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_share_permission_with_options_async(
        self,
        request: cloudphone_20201230_models.ListImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListImageSharePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageSharePermission',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListImageSharePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_share_permission(
        self,
        request: cloudphone_20201230_models.ListImageSharePermissionRequest,
    ) -> cloudphone_20201230_models.ListImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_image_share_permission_with_options(request, runtime)

    async def list_image_share_permission_async(
        self,
        request: cloudphone_20201230_models.ListImageSharePermissionRequest,
    ) -> cloudphone_20201230_models.ListImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_image_share_permission_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: cloudphone_20201230_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: cloudphone_20201230_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: cloudphone_20201230_models.ListImagesRequest,
    ) -> cloudphone_20201230_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: cloudphone_20201230_models.ListImagesRequest,
    ) -> cloudphone_20201230_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_instance_types_with_options(
        self,
        request: cloudphone_20201230_models.ListInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceTypes',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_types_with_options_async(
        self,
        request: cloudphone_20201230_models.ListInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListInstanceTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceTypes',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListInstanceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_types(
        self,
        request: cloudphone_20201230_models.ListInstanceTypesRequest,
    ) -> cloudphone_20201230_models.ListInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_types_with_options(request, runtime)

    async def list_instance_types_async(
        self,
        request: cloudphone_20201230_models.ListInstanceTypesRequest,
    ) -> cloudphone_20201230_models.ListInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_types_with_options_async(request, runtime)

    def list_instance_vnc_url_with_options(
        self,
        request: cloudphone_20201230_models.ListInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListInstanceVncUrlResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   The URL returned is valid only for 15 seconds. If no connection is established within 15 seconds after a successful query, the URL expires. You must query the URL again if you still want to use the URL.
        *   The keep-alive duration of a single URL of a management terminal is 60 seconds. If no interaction is detected within the 60 seconds, the management terminal is automatically disconnected.
        *   After the management terminal is disconnected, you can only reconnect to the terminal up to 30 times per minute.
        *   You need to add vncUrl=\\*\\*\\*\\*, instanceId= ****and password=**** to the end of the link https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html? and use ampersands (&) between the parameters. Parameter description:
        *   vncUrl: the value that is returned after the operation is called.
        *   instanceId: the instance ID.
        *   (Optional) password: the password for remote connection of the instance, which can contain six characters in length. The password can be digits or letters. If you specify this parameter, you do not need to enter your password again when the management terminal is being connected.
        Example:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\
        Or:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\\&password=\\*\\*\\*\\*\
        
        @param request: ListInstanceVncUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceVncUrlResponse
        """
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceVncUrl',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListInstanceVncUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_vnc_url_with_options_async(
        self,
        request: cloudphone_20201230_models.ListInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListInstanceVncUrlResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   The URL returned is valid only for 15 seconds. If no connection is established within 15 seconds after a successful query, the URL expires. You must query the URL again if you still want to use the URL.
        *   The keep-alive duration of a single URL of a management terminal is 60 seconds. If no interaction is detected within the 60 seconds, the management terminal is automatically disconnected.
        *   After the management terminal is disconnected, you can only reconnect to the terminal up to 30 times per minute.
        *   You need to add vncUrl=\\*\\*\\*\\*, instanceId= ****and password=**** to the end of the link https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html? and use ampersands (&) between the parameters. Parameter description:
        *   vncUrl: the value that is returned after the operation is called.
        *   instanceId: the instance ID.
        *   (Optional) password: the password for remote connection of the instance, which can contain six characters in length. The password can be digits or letters. If you specify this parameter, you do not need to enter your password again when the management terminal is being connected.
        Example:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\
        Or:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\\&password=\\*\\*\\*\\*\
        
        @param request: ListInstanceVncUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceVncUrlResponse
        """
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceVncUrl',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListInstanceVncUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_vnc_url(
        self,
        request: cloudphone_20201230_models.ListInstanceVncUrlRequest,
    ) -> cloudphone_20201230_models.ListInstanceVncUrlResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   The URL returned is valid only for 15 seconds. If no connection is established within 15 seconds after a successful query, the URL expires. You must query the URL again if you still want to use the URL.
        *   The keep-alive duration of a single URL of a management terminal is 60 seconds. If no interaction is detected within the 60 seconds, the management terminal is automatically disconnected.
        *   After the management terminal is disconnected, you can only reconnect to the terminal up to 30 times per minute.
        *   You need to add vncUrl=\\*\\*\\*\\*, instanceId= ****and password=**** to the end of the link https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html? and use ampersands (&) between the parameters. Parameter description:
        *   vncUrl: the value that is returned after the operation is called.
        *   instanceId: the instance ID.
        *   (Optional) password: the password for remote connection of the instance, which can contain six characters in length. The password can be digits or letters. If you specify this parameter, you do not need to enter your password again when the management terminal is being connected.
        Example:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\
        Or:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\\&password=\\*\\*\\*\\*\
        
        @param request: ListInstanceVncUrlRequest
        @return: ListInstanceVncUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_vnc_url_with_options(request, runtime)

    async def list_instance_vnc_url_async(
        self,
        request: cloudphone_20201230_models.ListInstanceVncUrlRequest,
    ) -> cloudphone_20201230_models.ListInstanceVncUrlResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   The URL returned is valid only for 15 seconds. If no connection is established within 15 seconds after a successful query, the URL expires. You must query the URL again if you still want to use the URL.
        *   The keep-alive duration of a single URL of a management terminal is 60 seconds. If no interaction is detected within the 60 seconds, the management terminal is automatically disconnected.
        *   After the management terminal is disconnected, you can only reconnect to the terminal up to 30 times per minute.
        *   You need to add vncUrl=\\*\\*\\*\\*, instanceId= ****and password=**** to the end of the link https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html? and use ampersands (&) between the parameters. Parameter description:
        *   vncUrl: the value that is returned after the operation is called.
        *   instanceId: the instance ID.
        *   (Optional) password: the password for remote connection of the instance, which can contain six characters in length. The password can be digits or letters. If you specify this parameter, you do not need to enter your password again when the management terminal is being connected.
        Example:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\
        Or:
        https://g.alicdn.com/aliyun/ecs-console-vnc2/0.0.8/index.html?vncUrl=ws%3A%2F%****\\&instanceId=cp-wz9hhwq5a6tm****\\&password=\\*\\*\\*\\*\
        
        @param request: ListInstanceVncUrlRequest
        @return: ListInstanceVncUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_vnc_url_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: cloudphone_20201230_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListInstancesResponse:
        """
        This operation only supports the NextToken query method.
        *   Results are returned in descending order based on the time when ECP instances were created.
        *   When you use NextToken to specify a query token, set the value to the NextToken value that is returned in the last call to the ListInstances operation. Then, use MaxResults to specify the maximum number of entries to return on each page.
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.show_web_rtc_token):
            query['ShowWebRtcToken'] = request.show_web_rtc_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListInstancesResponse:
        """
        This operation only supports the NextToken query method.
        *   Results are returned in descending order based on the time when ECP instances were created.
        *   When you use NextToken to specify a query token, set the value to the NextToken value that is returned in the last call to the ListInstances operation. Then, use MaxResults to specify the maximum number of entries to return on each page.
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.show_web_rtc_token):
            query['ShowWebRtcToken'] = request.show_web_rtc_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: cloudphone_20201230_models.ListInstancesRequest,
    ) -> cloudphone_20201230_models.ListInstancesResponse:
        """
        This operation only supports the NextToken query method.
        *   Results are returned in descending order based on the time when ECP instances were created.
        *   When you use NextToken to specify a query token, set the value to the NextToken value that is returned in the last call to the ListInstances operation. Then, use MaxResults to specify the maximum number of entries to return on each page.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: cloudphone_20201230_models.ListInstancesRequest,
    ) -> cloudphone_20201230_models.ListInstancesResponse:
        """
        This operation only supports the NextToken query method.
        *   Results are returned in descending order based on the time when ECP instances were created.
        *   When you use NextToken to specify a query token, set the value to the NextToken value that is returned in the last call to the ListInstances operation. Then, use MaxResults to specify the maximum number of entries to return on each page.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_key_pairs_with_options(
        self,
        request: cloudphone_20201230_models.ListKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListKeyPairsResponse:
        """
        You can call this operation to query one or more key pairs of cloud phones.
        
        @param request: ListKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_finger_print):
            query['KeyPairFingerPrint'] = request.key_pair_finger_print
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeyPairs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListKeyPairsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_key_pairs_with_options_async(
        self,
        request: cloudphone_20201230_models.ListKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListKeyPairsResponse:
        """
        You can call this operation to query one or more key pairs of cloud phones.
        
        @param request: ListKeyPairsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeyPairsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_pair_finger_print):
            query['KeyPairFingerPrint'] = request.key_pair_finger_print
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeyPairs',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListKeyPairsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_key_pairs(
        self,
        request: cloudphone_20201230_models.ListKeyPairsRequest,
    ) -> cloudphone_20201230_models.ListKeyPairsResponse:
        """
        You can call this operation to query one or more key pairs of cloud phones.
        
        @param request: ListKeyPairsRequest
        @return: ListKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_key_pairs_with_options(request, runtime)

    async def list_key_pairs_async(
        self,
        request: cloudphone_20201230_models.ListKeyPairsRequest,
    ) -> cloudphone_20201230_models.ListKeyPairsResponse:
        """
        You can call this operation to query one or more key pairs of cloud phones.
        
        @param request: ListKeyPairsRequest
        @return: ListKeyPairsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_key_pairs_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: cloudphone_20201230_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListRegionsResponse:
        """
        You can call this operation to query regions where ECP is available.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: cloudphone_20201230_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListRegionsResponse:
        """
        You can call this operation to query regions where ECP is available.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: cloudphone_20201230_models.ListRegionsRequest,
    ) -> cloudphone_20201230_models.ListRegionsResponse:
        """
        You can call this operation to query regions where ECP is available.
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: cloudphone_20201230_models.ListRegionsRequest,
    ) -> cloudphone_20201230_models.ListRegionsResponse:
        """
        You can call this operation to query regions where ECP is available.
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: cloudphone_20201230_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTagKeysResponse:
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: cloudphone_20201230_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTagKeysResponse:
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
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: cloudphone_20201230_models.ListTagKeysRequest,
    ) -> cloudphone_20201230_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: cloudphone_20201230_models.ListTagKeysRequest,
    ) -> cloudphone_20201230_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: cloudphone_20201230_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTagResourcesResponse:
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: cloudphone_20201230_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTagResourcesResponse:
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: cloudphone_20201230_models.ListTagResourcesRequest,
    ) -> cloudphone_20201230_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: cloudphone_20201230_models.ListTagResourcesRequest,
    ) -> cloudphone_20201230_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: cloudphone_20201230_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: cloudphone_20201230_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: cloudphone_20201230_models.ListTagValuesRequest,
    ) -> cloudphone_20201230_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: cloudphone_20201230_models.ListTagValuesRequest,
    ) -> cloudphone_20201230_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: cloudphone_20201230_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: cloudphone_20201230_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: cloudphone_20201230_models.ListTasksRequest,
    ) -> cloudphone_20201230_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: cloudphone_20201230_models.ListTasksRequest,
    ) -> cloudphone_20201230_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_zones_with_options(
        self,
        request: cloudphone_20201230_models.ListZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListZonesResponse:
        """
        ## [](#)Usage notes
        *   You can call the operation to query zones available in a specified region.
        
        @param request: ListZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_zones_with_options_async(
        self,
        request: cloudphone_20201230_models.ListZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ListZonesResponse:
        """
        ## [](#)Usage notes
        *   You can call the operation to query zones available in a specified region.
        
        @param request: ListZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ListZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_zones(
        self,
        request: cloudphone_20201230_models.ListZonesRequest,
    ) -> cloudphone_20201230_models.ListZonesResponse:
        """
        ## [](#)Usage notes
        *   You can call the operation to query zones available in a specified region.
        
        @param request: ListZonesRequest
        @return: ListZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_zones_with_options(request, runtime)

    async def list_zones_async(
        self,
        request: cloudphone_20201230_models.ListZonesRequest,
    ) -> cloudphone_20201230_models.ListZonesResponse:
        """
        ## [](#)Usage notes
        *   You can call the operation to query zones available in a specified region.
        
        @param request: ListZonesRequest
        @return: ListZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_zones_with_options_async(request, runtime)

    def reboot_instances_with_options(
        self,
        request: cloudphone_20201230_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RebootInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RebootInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_instances(
        self,
        request: cloudphone_20201230_models.RebootInstancesRequest,
    ) -> cloudphone_20201230_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    async def reboot_instances_async(
        self,
        request: cloudphone_20201230_models.RebootInstancesRequest,
    ) -> cloudphone_20201230_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instances_with_options_async(request, runtime)

    def renew_instances_with_options(
        self,
        request: cloudphone_20201230_models.RenewInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RenewInstancesResponse:
        """
        You can call the operation to renew multiple ECP instances at a time.
        
        @param request: RenewInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RenewInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.RenewInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RenewInstancesResponse:
        """
        You can call the operation to renew multiple ECP instances at a time.
        
        @param request: RenewInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RenewInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instances(
        self,
        request: cloudphone_20201230_models.RenewInstancesRequest,
    ) -> cloudphone_20201230_models.RenewInstancesResponse:
        """
        You can call the operation to renew multiple ECP instances at a time.
        
        @param request: RenewInstancesRequest
        @return: RenewInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_instances_with_options(request, runtime)

    async def renew_instances_async(
        self,
        request: cloudphone_20201230_models.RenewInstancesRequest,
    ) -> cloudphone_20201230_models.RenewInstancesResponse:
        """
        You can call the operation to renew multiple ECP instances at a time.
        
        @param request: RenewInstancesRequest
        @return: RenewInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_instances_with_options_async(request, runtime)

    def reset_instances_with_options(
        self,
        request: cloudphone_20201230_models.ResetInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ResetInstancesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   This operation is valid only for ECP instances that are in the Stopped state.
        *   If the images based on which the instances are created are deleted, the instances cannot be reset.
        
        @param request: ResetInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ResetInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.ResetInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.ResetInstancesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   This operation is valid only for ECP instances that are in the Stopped state.
        *   If the images based on which the instances are created are deleted, the instances cannot be reset.
        
        @param request: ResetInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.ResetInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_instances(
        self,
        request: cloudphone_20201230_models.ResetInstancesRequest,
    ) -> cloudphone_20201230_models.ResetInstancesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   This operation is valid only for ECP instances that are in the Stopped state.
        *   If the images based on which the instances are created are deleted, the instances cannot be reset.
        
        @param request: ResetInstancesRequest
        @return: ResetInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_instances_with_options(request, runtime)

    async def reset_instances_async(
        self,
        request: cloudphone_20201230_models.ResetInstancesRequest,
    ) -> cloudphone_20201230_models.ResetInstancesResponse:
        """
        ## [](#)Usage notes
        When you call this operation, take note of the following items:
        *   This operation is valid only for ECP instances that are in the Stopped state.
        *   If the images based on which the instances are created are deleted, the instances cannot be reset.
        
        @param request: ResetInstancesRequest
        @return: ResetInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_instances_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        request: cloudphone_20201230_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RunCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        request: cloudphone_20201230_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RunCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: cloudphone_20201230_models.RunCommandRequest,
    ) -> cloudphone_20201230_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: cloudphone_20201230_models.RunCommandRequest,
    ) -> cloudphone_20201230_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def run_instances_with_options(
        self,
        request: cloudphone_20201230_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RunInstancesResponse:
        """
        Preparations:
        *   The real-name verification is complete. For more information, see [Real-name verification](~~428525~~).
        Precautions:
        *   You can create up to 100 ECP instances at a time.
        *   You can call this operation to create and start ECP instances.
        *   If an ECP instance fails to be created due to force majeure factors, such as insufficient inventory, the ECP instance is automatically rolled back and released.
        
        @param request: RunInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RunInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.RunInstancesResponse:
        """
        Preparations:
        *   The real-name verification is complete. For more information, see [Real-name verification](~~428525~~).
        Precautions:
        *   You can create up to 100 ECP instances at a time.
        *   You can call this operation to create and start ECP instances.
        *   If an ECP instance fails to be created due to force majeure factors, such as insufficient inventory, the ECP instance is automatically rolled back and released.
        
        @param request: RunInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.RunInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_instances(
        self,
        request: cloudphone_20201230_models.RunInstancesRequest,
    ) -> cloudphone_20201230_models.RunInstancesResponse:
        """
        Preparations:
        *   The real-name verification is complete. For more information, see [Real-name verification](~~428525~~).
        Precautions:
        *   You can create up to 100 ECP instances at a time.
        *   You can call this operation to create and start ECP instances.
        *   If an ECP instance fails to be created due to force majeure factors, such as insufficient inventory, the ECP instance is automatically rolled back and released.
        
        @param request: RunInstancesRequest
        @return: RunInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_instances_with_options(request, runtime)

    async def run_instances_async(
        self,
        request: cloudphone_20201230_models.RunInstancesRequest,
    ) -> cloudphone_20201230_models.RunInstancesResponse:
        """
        Preparations:
        *   The real-name verification is complete. For more information, see [Real-name verification](~~428525~~).
        Precautions:
        *   You can create up to 100 ECP instances at a time.
        *   You can call this operation to create and start ECP instances.
        *   If an ECP instance fails to be created due to force majeure factors, such as insufficient inventory, the ECP instance is automatically rolled back and released.
        
        @param request: RunInstancesRequest
        @return: RunInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_instances_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        request: cloudphone_20201230_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.SendFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendFile',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.SendFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_file_with_options_async(
        self,
        request: cloudphone_20201230_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.SendFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendFile',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.SendFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_file(
        self,
        request: cloudphone_20201230_models.SendFileRequest,
    ) -> cloudphone_20201230_models.SendFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: cloudphone_20201230_models.SendFileRequest,
    ) -> cloudphone_20201230_models.SendFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def start_instances_with_options(
        self,
        request: cloudphone_20201230_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.StartInstancesResponse:
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.StartInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.StartInstancesResponse:
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.StartInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instances(
        self,
        request: cloudphone_20201230_models.StartInstancesRequest,
    ) -> cloudphone_20201230_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    async def start_instances_async(
        self,
        request: cloudphone_20201230_models.StartInstancesRequest,
    ) -> cloudphone_20201230_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instances_with_options_async(request, runtime)

    def stop_instances_with_options(
        self,
        request: cloudphone_20201230_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.StopInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instances_with_options_async(
        self,
        request: cloudphone_20201230_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstances',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.StopInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instances(
        self,
        request: cloudphone_20201230_models.StopInstancesRequest,
    ) -> cloudphone_20201230_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    async def stop_instances_async(
        self,
        request: cloudphone_20201230_models.StopInstancesRequest,
    ) -> cloudphone_20201230_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instances_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: cloudphone_20201230_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.TagResourcesResponse:
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cloudphone_20201230_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.TagResourcesResponse:
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: cloudphone_20201230_models.TagResourcesRequest,
    ) -> cloudphone_20201230_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: cloudphone_20201230_models.TagResourcesRequest,
    ) -> cloudphone_20201230_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def uninstall_application_with_options(
        self,
        request: cloudphone_20201230_models.UninstallApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UninstallApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallApplication',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UninstallApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_application_with_options_async(
        self,
        request: cloudphone_20201230_models.UninstallApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UninstallApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_name):
            query['PackageName'] = request.package_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallApplication',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UninstallApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_application(
        self,
        request: cloudphone_20201230_models.UninstallApplicationRequest,
    ) -> cloudphone_20201230_models.UninstallApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_application_with_options(request, runtime)

    async def uninstall_application_async(
        self,
        request: cloudphone_20201230_models.UninstallApplicationRequest,
    ) -> cloudphone_20201230_models.UninstallApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_application_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: cloudphone_20201230_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: cloudphone_20201230_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: cloudphone_20201230_models.UntagResourcesRequest,
    ) -> cloudphone_20201230_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: cloudphone_20201230_models.UntagResourcesRequest,
    ) -> cloudphone_20201230_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_image_attribute_with_options(
        self,
        request: cloudphone_20201230_models.UpdateImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UpdateImageAttributeResponse:
        """
        When you call this operation, take note of the following items:
        *   You can share only your own custom images with other Alibaba Cloud accounts.
        *   You can share a custom image with up to 10 Alibaba Cloud accounts at a time.
        
        @param request: UpdateImageAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_account):
            query['AddAccount'] = request.add_account
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_account):
            query['RemoveAccount'] = request.remove_account
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImageAttribute',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UpdateImageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_attribute_with_options_async(
        self,
        request: cloudphone_20201230_models.UpdateImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UpdateImageAttributeResponse:
        """
        When you call this operation, take note of the following items:
        *   You can share only your own custom images with other Alibaba Cloud accounts.
        *   You can share a custom image with up to 10 Alibaba Cloud accounts at a time.
        
        @param request: UpdateImageAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_account):
            query['AddAccount'] = request.add_account
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_account):
            query['RemoveAccount'] = request.remove_account
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImageAttribute',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UpdateImageAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image_attribute(
        self,
        request: cloudphone_20201230_models.UpdateImageAttributeRequest,
    ) -> cloudphone_20201230_models.UpdateImageAttributeResponse:
        """
        When you call this operation, take note of the following items:
        *   You can share only your own custom images with other Alibaba Cloud accounts.
        *   You can share a custom image with up to 10 Alibaba Cloud accounts at a time.
        
        @param request: UpdateImageAttributeRequest
        @return: UpdateImageAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_image_attribute_with_options(request, runtime)

    async def update_image_attribute_async(
        self,
        request: cloudphone_20201230_models.UpdateImageAttributeRequest,
    ) -> cloudphone_20201230_models.UpdateImageAttributeResponse:
        """
        When you call this operation, take note of the following items:
        *   You can share only your own custom images with other Alibaba Cloud accounts.
        *   You can share a custom image with up to 10 Alibaba Cloud accounts at a time.
        
        @param request: UpdateImageAttributeRequest
        @return: UpdateImageAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_image_attribute_with_options_async(request, runtime)

    def update_instance_attribute_with_options(
        self,
        request: cloudphone_20201230_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UpdateInstanceAttributeResponse:
        """
        You can call this operation to modify the name, key pair, Virtual Network Computing (VNC) password, and resolution of an ECP instance. Take note that the modified key pair and resolution takes effect the next time you restart the instance.
        
        @param request: UpdateInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vnc_password):
            query['VncPassword'] = request.vnc_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAttribute',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UpdateInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_attribute_with_options_async(
        self,
        request: cloudphone_20201230_models.UpdateInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudphone_20201230_models.UpdateInstanceAttributeResponse:
        """
        You can call this operation to modify the name, key pair, Virtual Network Computing (VNC) password, and resolution of an ECP instance. Take note that the modified key pair and resolution takes effect the next time you restart the instance.
        
        @param request: UpdateInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resolution):
            query['Resolution'] = request.resolution
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vnc_password):
            query['VncPassword'] = request.vnc_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceAttribute',
            version='2020-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudphone_20201230_models.UpdateInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_attribute(
        self,
        request: cloudphone_20201230_models.UpdateInstanceAttributeRequest,
    ) -> cloudphone_20201230_models.UpdateInstanceAttributeResponse:
        """
        You can call this operation to modify the name, key pair, Virtual Network Computing (VNC) password, and resolution of an ECP instance. Take note that the modified key pair and resolution takes effect the next time you restart the instance.
        
        @param request: UpdateInstanceAttributeRequest
        @return: UpdateInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_attribute_with_options(request, runtime)

    async def update_instance_attribute_async(
        self,
        request: cloudphone_20201230_models.UpdateInstanceAttributeRequest,
    ) -> cloudphone_20201230_models.UpdateInstanceAttributeResponse:
        """
        You can call this operation to modify the name, key pair, Virtual Network Computing (VNC) password, and resolution of an ECP instance. Take note that the modified key pair and resolution takes effect the next time you restart the instance.
        
        @param request: UpdateInstanceAttributeRequest
        @return: UpdateInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_attribute_with_options_async(request, runtime)
