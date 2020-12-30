# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudphoto20170711 import models as cloud_photo_20170711_models
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
        self._endpoint = self.get_endpoint('cloudphoto', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ActivatePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ActivatePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ActivatePhotosResponse().from_map(
            self.do_rpcrequest('ActivatePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def activate_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ActivatePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ActivatePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ActivatePhotosResponse().from_map(
            await self.do_rpcrequest_async('ActivatePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_photos(
        self,
        request: cloud_photo_20170711_models.ActivatePhotosRequest,
    ) -> cloud_photo_20170711_models.ActivatePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_photos_with_options(request, runtime)

    async def activate_photos_async(
        self,
        request: cloud_photo_20170711_models.ActivatePhotosRequest,
    ) -> cloud_photo_20170711_models.ActivatePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_photos_with_options_async(request, runtime)

    def add_album_photos_with_options(
        self,
        request: cloud_photo_20170711_models.AddAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.AddAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.AddAlbumPhotosResponse().from_map(
            self.do_rpcrequest('AddAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_album_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.AddAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.AddAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.AddAlbumPhotosResponse().from_map(
            await self.do_rpcrequest_async('AddAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_album_photos(
        self,
        request: cloud_photo_20170711_models.AddAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.AddAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_album_photos_with_options(request, runtime)

    async def add_album_photos_async(
        self,
        request: cloud_photo_20170711_models.AddAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.AddAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_album_photos_with_options_async(request, runtime)

    def create_album_with_options(
        self,
        request: cloud_photo_20170711_models.CreateAlbumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreateAlbumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreateAlbumResponse().from_map(
            self.do_rpcrequest('CreateAlbum', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_album_with_options_async(
        self,
        request: cloud_photo_20170711_models.CreateAlbumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreateAlbumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreateAlbumResponse().from_map(
            await self.do_rpcrequest_async('CreateAlbum', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_album(
        self,
        request: cloud_photo_20170711_models.CreateAlbumRequest,
    ) -> cloud_photo_20170711_models.CreateAlbumResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_album_with_options(request, runtime)

    async def create_album_async(
        self,
        request: cloud_photo_20170711_models.CreateAlbumRequest,
    ) -> cloud_photo_20170711_models.CreateAlbumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_album_with_options_async(request, runtime)

    def create_photo_with_options(
        self,
        request: cloud_photo_20170711_models.CreatePhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreatePhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreatePhotoResponse().from_map(
            self.do_rpcrequest('CreatePhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_photo_with_options_async(
        self,
        request: cloud_photo_20170711_models.CreatePhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreatePhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreatePhotoResponse().from_map(
            await self.do_rpcrequest_async('CreatePhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_photo(
        self,
        request: cloud_photo_20170711_models.CreatePhotoRequest,
    ) -> cloud_photo_20170711_models.CreatePhotoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_photo_with_options(request, runtime)

    async def create_photo_async(
        self,
        request: cloud_photo_20170711_models.CreatePhotoRequest,
    ) -> cloud_photo_20170711_models.CreatePhotoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_photo_with_options_async(request, runtime)

    def create_photo_store_with_options(
        self,
        request: cloud_photo_20170711_models.CreatePhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreatePhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreatePhotoStoreResponse().from_map(
            self.do_rpcrequest('CreatePhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_photo_store_with_options_async(
        self,
        request: cloud_photo_20170711_models.CreatePhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreatePhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreatePhotoStoreResponse().from_map(
            await self.do_rpcrequest_async('CreatePhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_photo_store(
        self,
        request: cloud_photo_20170711_models.CreatePhotoStoreRequest,
    ) -> cloud_photo_20170711_models.CreatePhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_photo_store_with_options(request, runtime)

    async def create_photo_store_async(
        self,
        request: cloud_photo_20170711_models.CreatePhotoStoreRequest,
    ) -> cloud_photo_20170711_models.CreatePhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_photo_store_with_options_async(request, runtime)

    def create_transaction_with_options(
        self,
        request: cloud_photo_20170711_models.CreateTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreateTransactionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreateTransactionResponse().from_map(
            self.do_rpcrequest('CreateTransaction', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_transaction_with_options_async(
        self,
        request: cloud_photo_20170711_models.CreateTransactionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.CreateTransactionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.CreateTransactionResponse().from_map(
            await self.do_rpcrequest_async('CreateTransaction', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_transaction(
        self,
        request: cloud_photo_20170711_models.CreateTransactionRequest,
    ) -> cloud_photo_20170711_models.CreateTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_transaction_with_options(request, runtime)

    async def create_transaction_async(
        self,
        request: cloud_photo_20170711_models.CreateTransactionRequest,
    ) -> cloud_photo_20170711_models.CreateTransactionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_transaction_with_options_async(request, runtime)

    def delete_albums_with_options(
        self,
        request: cloud_photo_20170711_models.DeleteAlbumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeleteAlbumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeleteAlbumsResponse().from_map(
            self.do_rpcrequest('DeleteAlbums', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_albums_with_options_async(
        self,
        request: cloud_photo_20170711_models.DeleteAlbumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeleteAlbumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeleteAlbumsResponse().from_map(
            await self.do_rpcrequest_async('DeleteAlbums', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_albums(
        self,
        request: cloud_photo_20170711_models.DeleteAlbumsRequest,
    ) -> cloud_photo_20170711_models.DeleteAlbumsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_albums_with_options(request, runtime)

    async def delete_albums_async(
        self,
        request: cloud_photo_20170711_models.DeleteAlbumsRequest,
    ) -> cloud_photo_20170711_models.DeleteAlbumsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_albums_with_options_async(request, runtime)

    def delete_event_with_options(
        self,
        request: cloud_photo_20170711_models.DeleteEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeleteEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeleteEventResponse().from_map(
            self.do_rpcrequest('DeleteEvent', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_event_with_options_async(
        self,
        request: cloud_photo_20170711_models.DeleteEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeleteEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeleteEventResponse().from_map(
            await self.do_rpcrequest_async('DeleteEvent', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_event(
        self,
        request: cloud_photo_20170711_models.DeleteEventRequest,
    ) -> cloud_photo_20170711_models.DeleteEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_with_options(request, runtime)

    async def delete_event_async(
        self,
        request: cloud_photo_20170711_models.DeleteEventRequest,
    ) -> cloud_photo_20170711_models.DeleteEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_with_options_async(request, runtime)

    def delete_faces_with_options(
        self,
        request: cloud_photo_20170711_models.DeleteFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeleteFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeleteFacesResponse().from_map(
            self.do_rpcrequest('DeleteFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_faces_with_options_async(
        self,
        request: cloud_photo_20170711_models.DeleteFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeleteFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeleteFacesResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_faces(
        self,
        request: cloud_photo_20170711_models.DeleteFacesRequest,
    ) -> cloud_photo_20170711_models.DeleteFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_faces_with_options(request, runtime)

    async def delete_faces_async(
        self,
        request: cloud_photo_20170711_models.DeleteFacesRequest,
    ) -> cloud_photo_20170711_models.DeleteFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_faces_with_options_async(request, runtime)

    def delete_photos_with_options(
        self,
        request: cloud_photo_20170711_models.DeletePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeletePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeletePhotosResponse().from_map(
            self.do_rpcrequest('DeletePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.DeletePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeletePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeletePhotosResponse().from_map(
            await self.do_rpcrequest_async('DeletePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_photos(
        self,
        request: cloud_photo_20170711_models.DeletePhotosRequest,
    ) -> cloud_photo_20170711_models.DeletePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_photos_with_options(request, runtime)

    async def delete_photos_async(
        self,
        request: cloud_photo_20170711_models.DeletePhotosRequest,
    ) -> cloud_photo_20170711_models.DeletePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_photos_with_options_async(request, runtime)

    def delete_photo_store_with_options(
        self,
        request: cloud_photo_20170711_models.DeletePhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeletePhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeletePhotoStoreResponse().from_map(
            self.do_rpcrequest('DeletePhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_photo_store_with_options_async(
        self,
        request: cloud_photo_20170711_models.DeletePhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.DeletePhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.DeletePhotoStoreResponse().from_map(
            await self.do_rpcrequest_async('DeletePhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_photo_store(
        self,
        request: cloud_photo_20170711_models.DeletePhotoStoreRequest,
    ) -> cloud_photo_20170711_models.DeletePhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_photo_store_with_options(request, runtime)

    async def delete_photo_store_async(
        self,
        request: cloud_photo_20170711_models.DeletePhotoStoreRequest,
    ) -> cloud_photo_20170711_models.DeletePhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_photo_store_with_options_async(request, runtime)

    def edit_photos_with_options(
        self,
        request: cloud_photo_20170711_models.EditPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.EditPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.EditPhotosResponse().from_map(
            self.do_rpcrequest('EditPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.EditPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.EditPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.EditPhotosResponse().from_map(
            await self.do_rpcrequest_async('EditPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_photos(
        self,
        request: cloud_photo_20170711_models.EditPhotosRequest,
    ) -> cloud_photo_20170711_models.EditPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_photos_with_options(request, runtime)

    async def edit_photos_async(
        self,
        request: cloud_photo_20170711_models.EditPhotosRequest,
    ) -> cloud_photo_20170711_models.EditPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_photos_with_options_async(request, runtime)

    def edit_photo_store_with_options(
        self,
        request: cloud_photo_20170711_models.EditPhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.EditPhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.EditPhotoStoreResponse().from_map(
            self.do_rpcrequest('EditPhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_photo_store_with_options_async(
        self,
        request: cloud_photo_20170711_models.EditPhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.EditPhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.EditPhotoStoreResponse().from_map(
            await self.do_rpcrequest_async('EditPhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def edit_photo_store(
        self,
        request: cloud_photo_20170711_models.EditPhotoStoreRequest,
    ) -> cloud_photo_20170711_models.EditPhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_photo_store_with_options(request, runtime)

    async def edit_photo_store_async(
        self,
        request: cloud_photo_20170711_models.EditPhotoStoreRequest,
    ) -> cloud_photo_20170711_models.EditPhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_photo_store_with_options_async(request, runtime)

    def fetch_album_tag_photos_with_options(
        self,
        request: cloud_photo_20170711_models.FetchAlbumTagPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchAlbumTagPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchAlbumTagPhotosResponse().from_map(
            self.do_rpcrequest('FetchAlbumTagPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fetch_album_tag_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.FetchAlbumTagPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchAlbumTagPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchAlbumTagPhotosResponse().from_map(
            await self.do_rpcrequest_async('FetchAlbumTagPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_album_tag_photos(
        self,
        request: cloud_photo_20170711_models.FetchAlbumTagPhotosRequest,
    ) -> cloud_photo_20170711_models.FetchAlbumTagPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_album_tag_photos_with_options(request, runtime)

    async def fetch_album_tag_photos_async(
        self,
        request: cloud_photo_20170711_models.FetchAlbumTagPhotosRequest,
    ) -> cloud_photo_20170711_models.FetchAlbumTagPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_album_tag_photos_with_options_async(request, runtime)

    def fetch_libraries_with_options(
        self,
        request: cloud_photo_20170711_models.FetchLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchLibrariesResponse().from_map(
            self.do_rpcrequest('FetchLibraries', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fetch_libraries_with_options_async(
        self,
        request: cloud_photo_20170711_models.FetchLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchLibrariesResponse().from_map(
            await self.do_rpcrequest_async('FetchLibraries', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_libraries(
        self,
        request: cloud_photo_20170711_models.FetchLibrariesRequest,
    ) -> cloud_photo_20170711_models.FetchLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_libraries_with_options(request, runtime)

    async def fetch_libraries_async(
        self,
        request: cloud_photo_20170711_models.FetchLibrariesRequest,
    ) -> cloud_photo_20170711_models.FetchLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_libraries_with_options_async(request, runtime)

    def fetch_moment_photos_with_options(
        self,
        request: cloud_photo_20170711_models.FetchMomentPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchMomentPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchMomentPhotosResponse().from_map(
            self.do_rpcrequest('FetchMomentPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fetch_moment_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.FetchMomentPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchMomentPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchMomentPhotosResponse().from_map(
            await self.do_rpcrequest_async('FetchMomentPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_moment_photos(
        self,
        request: cloud_photo_20170711_models.FetchMomentPhotosRequest,
    ) -> cloud_photo_20170711_models.FetchMomentPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_moment_photos_with_options(request, runtime)

    async def fetch_moment_photos_async(
        self,
        request: cloud_photo_20170711_models.FetchMomentPhotosRequest,
    ) -> cloud_photo_20170711_models.FetchMomentPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_moment_photos_with_options_async(request, runtime)

    def fetch_photos_with_options(
        self,
        request: cloud_photo_20170711_models.FetchPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchPhotosResponse().from_map(
            self.do_rpcrequest('FetchPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fetch_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.FetchPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.FetchPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.FetchPhotosResponse().from_map(
            await self.do_rpcrequest_async('FetchPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_photos(
        self,
        request: cloud_photo_20170711_models.FetchPhotosRequest,
    ) -> cloud_photo_20170711_models.FetchPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_photos_with_options(request, runtime)

    async def fetch_photos_async(
        self,
        request: cloud_photo_20170711_models.FetchPhotosRequest,
    ) -> cloud_photo_20170711_models.FetchPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_photos_with_options_async(request, runtime)

    def get_albums_by_names_with_options(
        self,
        request: cloud_photo_20170711_models.GetAlbumsByNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetAlbumsByNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetAlbumsByNamesResponse().from_map(
            self.do_rpcrequest('GetAlbumsByNames', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_albums_by_names_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetAlbumsByNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetAlbumsByNamesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetAlbumsByNamesResponse().from_map(
            await self.do_rpcrequest_async('GetAlbumsByNames', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_albums_by_names(
        self,
        request: cloud_photo_20170711_models.GetAlbumsByNamesRequest,
    ) -> cloud_photo_20170711_models.GetAlbumsByNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_albums_by_names_with_options(request, runtime)

    async def get_albums_by_names_async(
        self,
        request: cloud_photo_20170711_models.GetAlbumsByNamesRequest,
    ) -> cloud_photo_20170711_models.GetAlbumsByNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_albums_by_names_with_options_async(request, runtime)

    def get_download_url_with_options(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetDownloadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetDownloadUrlResponse().from_map(
            self.do_rpcrequest('GetDownloadUrl', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_download_url_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetDownloadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetDownloadUrlResponse().from_map(
            await self.do_rpcrequest_async('GetDownloadUrl', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_download_url(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlRequest,
    ) -> cloud_photo_20170711_models.GetDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_download_url_with_options(request, runtime)

    async def get_download_url_async(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlRequest,
    ) -> cloud_photo_20170711_models.GetDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_download_url_with_options_async(request, runtime)

    def get_download_urls_with_options(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetDownloadUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetDownloadUrlsResponse().from_map(
            self.do_rpcrequest('GetDownloadUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_download_urls_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetDownloadUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetDownloadUrlsResponse().from_map(
            await self.do_rpcrequest_async('GetDownloadUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_download_urls(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlsRequest,
    ) -> cloud_photo_20170711_models.GetDownloadUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_download_urls_with_options(request, runtime)

    async def get_download_urls_async(
        self,
        request: cloud_photo_20170711_models.GetDownloadUrlsRequest,
    ) -> cloud_photo_20170711_models.GetDownloadUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_download_urls_with_options_async(request, runtime)

    def get_framed_photo_urls_with_options(
        self,
        request: cloud_photo_20170711_models.GetFramedPhotoUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetFramedPhotoUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetFramedPhotoUrlsResponse().from_map(
            self.do_rpcrequest('GetFramedPhotoUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_framed_photo_urls_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetFramedPhotoUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetFramedPhotoUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetFramedPhotoUrlsResponse().from_map(
            await self.do_rpcrequest_async('GetFramedPhotoUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_framed_photo_urls(
        self,
        request: cloud_photo_20170711_models.GetFramedPhotoUrlsRequest,
    ) -> cloud_photo_20170711_models.GetFramedPhotoUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_framed_photo_urls_with_options(request, runtime)

    async def get_framed_photo_urls_async(
        self,
        request: cloud_photo_20170711_models.GetFramedPhotoUrlsRequest,
    ) -> cloud_photo_20170711_models.GetFramedPhotoUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_framed_photo_urls_with_options_async(request, runtime)

    def get_library_with_options(
        self,
        request: cloud_photo_20170711_models.GetLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetLibraryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetLibraryResponse().from_map(
            self.do_rpcrequest('GetLibrary', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_library_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetLibraryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetLibraryResponse().from_map(
            await self.do_rpcrequest_async('GetLibrary', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_library(
        self,
        request: cloud_photo_20170711_models.GetLibraryRequest,
    ) -> cloud_photo_20170711_models.GetLibraryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_library_with_options(request, runtime)

    async def get_library_async(
        self,
        request: cloud_photo_20170711_models.GetLibraryRequest,
    ) -> cloud_photo_20170711_models.GetLibraryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_library_with_options_async(request, runtime)

    def get_photos_with_options(
        self,
        request: cloud_photo_20170711_models.GetPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPhotosResponse().from_map(
            self.do_rpcrequest('GetPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPhotosResponse().from_map(
            await self.do_rpcrequest_async('GetPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_photos(
        self,
        request: cloud_photo_20170711_models.GetPhotosRequest,
    ) -> cloud_photo_20170711_models.GetPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_photos_with_options(request, runtime)

    async def get_photos_async(
        self,
        request: cloud_photo_20170711_models.GetPhotosRequest,
    ) -> cloud_photo_20170711_models.GetPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_photos_with_options_async(request, runtime)

    def get_photos_by_md_5s_with_options(
        self,
        request: cloud_photo_20170711_models.GetPhotosByMd5sRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPhotosByMd5sResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPhotosByMd5sResponse().from_map(
            self.do_rpcrequest('GetPhotosByMd5s', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_photos_by_md_5s_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetPhotosByMd5sRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPhotosByMd5sResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPhotosByMd5sResponse().from_map(
            await self.do_rpcrequest_async('GetPhotosByMd5s', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_photos_by_md_5s(
        self,
        request: cloud_photo_20170711_models.GetPhotosByMd5sRequest,
    ) -> cloud_photo_20170711_models.GetPhotosByMd5sResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_photos_by_md_5s_with_options(request, runtime)

    async def get_photos_by_md_5s_async(
        self,
        request: cloud_photo_20170711_models.GetPhotosByMd5sRequest,
    ) -> cloud_photo_20170711_models.GetPhotosByMd5sResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_photos_by_md_5s_with_options_async(request, runtime)

    def get_photo_store_with_options(
        self,
        request: cloud_photo_20170711_models.GetPhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPhotoStoreResponse().from_map(
            self.do_rpcrequest('GetPhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_photo_store_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetPhotoStoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPhotoStoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPhotoStoreResponse().from_map(
            await self.do_rpcrequest_async('GetPhotoStore', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_photo_store(
        self,
        request: cloud_photo_20170711_models.GetPhotoStoreRequest,
    ) -> cloud_photo_20170711_models.GetPhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_photo_store_with_options(request, runtime)

    async def get_photo_store_async(
        self,
        request: cloud_photo_20170711_models.GetPhotoStoreRequest,
    ) -> cloud_photo_20170711_models.GetPhotoStoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_photo_store_with_options_async(request, runtime)

    def get_private_access_urls_with_options(
        self,
        request: cloud_photo_20170711_models.GetPrivateAccessUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPrivateAccessUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPrivateAccessUrlsResponse().from_map(
            self.do_rpcrequest('GetPrivateAccessUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_private_access_urls_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetPrivateAccessUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPrivateAccessUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPrivateAccessUrlsResponse().from_map(
            await self.do_rpcrequest_async('GetPrivateAccessUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_private_access_urls(
        self,
        request: cloud_photo_20170711_models.GetPrivateAccessUrlsRequest,
    ) -> cloud_photo_20170711_models.GetPrivateAccessUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_private_access_urls_with_options(request, runtime)

    async def get_private_access_urls_async(
        self,
        request: cloud_photo_20170711_models.GetPrivateAccessUrlsRequest,
    ) -> cloud_photo_20170711_models.GetPrivateAccessUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_private_access_urls_with_options_async(request, runtime)

    def get_public_access_urls_with_options(
        self,
        request: cloud_photo_20170711_models.GetPublicAccessUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPublicAccessUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPublicAccessUrlsResponse().from_map(
            self.do_rpcrequest('GetPublicAccessUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_public_access_urls_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetPublicAccessUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetPublicAccessUrlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetPublicAccessUrlsResponse().from_map(
            await self.do_rpcrequest_async('GetPublicAccessUrls', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_public_access_urls(
        self,
        request: cloud_photo_20170711_models.GetPublicAccessUrlsRequest,
    ) -> cloud_photo_20170711_models.GetPublicAccessUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_public_access_urls_with_options(request, runtime)

    async def get_public_access_urls_async(
        self,
        request: cloud_photo_20170711_models.GetPublicAccessUrlsRequest,
    ) -> cloud_photo_20170711_models.GetPublicAccessUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_public_access_urls_with_options_async(request, runtime)

    def get_quota_with_options(
        self,
        request: cloud_photo_20170711_models.GetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetQuotaResponse().from_map(
            self.do_rpcrequest('GetQuota', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetQuotaResponse().from_map(
            await self.do_rpcrequest_async('GetQuota', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quota(
        self,
        request: cloud_photo_20170711_models.GetQuotaRequest,
    ) -> cloud_photo_20170711_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quota_with_options(request, runtime)

    async def get_quota_async(
        self,
        request: cloud_photo_20170711_models.GetQuotaRequest,
    ) -> cloud_photo_20170711_models.GetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quota_with_options_async(request, runtime)

    def get_similar_photos_with_options(
        self,
        request: cloud_photo_20170711_models.GetSimilarPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetSimilarPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetSimilarPhotosResponse().from_map(
            self.do_rpcrequest('GetSimilarPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_similar_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetSimilarPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetSimilarPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetSimilarPhotosResponse().from_map(
            await self.do_rpcrequest_async('GetSimilarPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_similar_photos(
        self,
        request: cloud_photo_20170711_models.GetSimilarPhotosRequest,
    ) -> cloud_photo_20170711_models.GetSimilarPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_similar_photos_with_options(request, runtime)

    async def get_similar_photos_async(
        self,
        request: cloud_photo_20170711_models.GetSimilarPhotosRequest,
    ) -> cloud_photo_20170711_models.GetSimilarPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_similar_photos_with_options_async(request, runtime)

    def get_thumbnail_with_options(
        self,
        request: cloud_photo_20170711_models.GetThumbnailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetThumbnailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetThumbnailResponse().from_map(
            self.do_rpcrequest('GetThumbnail', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thumbnail_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetThumbnailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetThumbnailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetThumbnailResponse().from_map(
            await self.do_rpcrequest_async('GetThumbnail', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_thumbnail(
        self,
        request: cloud_photo_20170711_models.GetThumbnailRequest,
    ) -> cloud_photo_20170711_models.GetThumbnailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thumbnail_with_options(request, runtime)

    async def get_thumbnail_async(
        self,
        request: cloud_photo_20170711_models.GetThumbnailRequest,
    ) -> cloud_photo_20170711_models.GetThumbnailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thumbnail_with_options_async(request, runtime)

    def get_thumbnails_with_options(
        self,
        request: cloud_photo_20170711_models.GetThumbnailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetThumbnailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetThumbnailsResponse().from_map(
            self.do_rpcrequest('GetThumbnails', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thumbnails_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetThumbnailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetThumbnailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetThumbnailsResponse().from_map(
            await self.do_rpcrequest_async('GetThumbnails', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_thumbnails(
        self,
        request: cloud_photo_20170711_models.GetThumbnailsRequest,
    ) -> cloud_photo_20170711_models.GetThumbnailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thumbnails_with_options(request, runtime)

    async def get_thumbnails_async(
        self,
        request: cloud_photo_20170711_models.GetThumbnailsRequest,
    ) -> cloud_photo_20170711_models.GetThumbnailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thumbnails_with_options_async(request, runtime)

    def get_video_cover_with_options(
        self,
        request: cloud_photo_20170711_models.GetVideoCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetVideoCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetVideoCoverResponse().from_map(
            self.do_rpcrequest('GetVideoCover', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_cover_with_options_async(
        self,
        request: cloud_photo_20170711_models.GetVideoCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.GetVideoCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.GetVideoCoverResponse().from_map(
            await self.do_rpcrequest_async('GetVideoCover', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_cover(
        self,
        request: cloud_photo_20170711_models.GetVideoCoverRequest,
    ) -> cloud_photo_20170711_models.GetVideoCoverResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_cover_with_options(request, runtime)

    async def get_video_cover_async(
        self,
        request: cloud_photo_20170711_models.GetVideoCoverRequest,
    ) -> cloud_photo_20170711_models.GetVideoCoverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_cover_with_options_async(request, runtime)

    def inactivate_photos_with_options(
        self,
        request: cloud_photo_20170711_models.InactivatePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.InactivatePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.InactivatePhotosResponse().from_map(
            self.do_rpcrequest('InactivatePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def inactivate_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.InactivatePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.InactivatePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.InactivatePhotosResponse().from_map(
            await self.do_rpcrequest_async('InactivatePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def inactivate_photos(
        self,
        request: cloud_photo_20170711_models.InactivatePhotosRequest,
    ) -> cloud_photo_20170711_models.InactivatePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.inactivate_photos_with_options(request, runtime)

    async def inactivate_photos_async(
        self,
        request: cloud_photo_20170711_models.InactivatePhotosRequest,
    ) -> cloud_photo_20170711_models.InactivatePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inactivate_photos_with_options_async(request, runtime)

    def like_photo_with_options(
        self,
        request: cloud_photo_20170711_models.LikePhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.LikePhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.LikePhotoResponse().from_map(
            self.do_rpcrequest('LikePhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def like_photo_with_options_async(
        self,
        request: cloud_photo_20170711_models.LikePhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.LikePhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.LikePhotoResponse().from_map(
            await self.do_rpcrequest_async('LikePhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def like_photo(
        self,
        request: cloud_photo_20170711_models.LikePhotoRequest,
    ) -> cloud_photo_20170711_models.LikePhotoResponse:
        runtime = util_models.RuntimeOptions()
        return self.like_photo_with_options(request, runtime)

    async def like_photo_async(
        self,
        request: cloud_photo_20170711_models.LikePhotoRequest,
    ) -> cloud_photo_20170711_models.LikePhotoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.like_photo_with_options_async(request, runtime)

    def list_album_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ListAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListAlbumPhotosResponse().from_map(
            self.do_rpcrequest('ListAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_album_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListAlbumPhotosResponse().from_map(
            await self.do_rpcrequest_async('ListAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_album_photos(
        self,
        request: cloud_photo_20170711_models.ListAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.ListAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_album_photos_with_options(request, runtime)

    async def list_album_photos_async(
        self,
        request: cloud_photo_20170711_models.ListAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.ListAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_album_photos_with_options_async(request, runtime)

    def list_albums_with_options(
        self,
        request: cloud_photo_20170711_models.ListAlbumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListAlbumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListAlbumsResponse().from_map(
            self.do_rpcrequest('ListAlbums', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_albums_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListAlbumsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListAlbumsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListAlbumsResponse().from_map(
            await self.do_rpcrequest_async('ListAlbums', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_albums(
        self,
        request: cloud_photo_20170711_models.ListAlbumsRequest,
    ) -> cloud_photo_20170711_models.ListAlbumsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_albums_with_options(request, runtime)

    async def list_albums_async(
        self,
        request: cloud_photo_20170711_models.ListAlbumsRequest,
    ) -> cloud_photo_20170711_models.ListAlbumsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_albums_with_options_async(request, runtime)

    def list_face_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ListFacePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListFacePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListFacePhotosResponse().from_map(
            self.do_rpcrequest('ListFacePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListFacePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListFacePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListFacePhotosResponse().from_map(
            await self.do_rpcrequest_async('ListFacePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_photos(
        self,
        request: cloud_photo_20170711_models.ListFacePhotosRequest,
    ) -> cloud_photo_20170711_models.ListFacePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_photos_with_options(request, runtime)

    async def list_face_photos_async(
        self,
        request: cloud_photo_20170711_models.ListFacePhotosRequest,
    ) -> cloud_photo_20170711_models.ListFacePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_photos_with_options_async(request, runtime)

    def list_faces_with_options(
        self,
        request: cloud_photo_20170711_models.ListFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListFacesResponse().from_map(
            self.do_rpcrequest('ListFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_faces_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListFacesResponse().from_map(
            await self.do_rpcrequest_async('ListFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_faces(
        self,
        request: cloud_photo_20170711_models.ListFacesRequest,
    ) -> cloud_photo_20170711_models.ListFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_faces_with_options(request, runtime)

    async def list_faces_async(
        self,
        request: cloud_photo_20170711_models.ListFacesRequest,
    ) -> cloud_photo_20170711_models.ListFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_faces_with_options_async(request, runtime)

    def list_moment_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ListMomentPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListMomentPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListMomentPhotosResponse().from_map(
            self.do_rpcrequest('ListMomentPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_moment_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListMomentPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListMomentPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListMomentPhotosResponse().from_map(
            await self.do_rpcrequest_async('ListMomentPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_moment_photos(
        self,
        request: cloud_photo_20170711_models.ListMomentPhotosRequest,
    ) -> cloud_photo_20170711_models.ListMomentPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_moment_photos_with_options(request, runtime)

    async def list_moment_photos_async(
        self,
        request: cloud_photo_20170711_models.ListMomentPhotosRequest,
    ) -> cloud_photo_20170711_models.ListMomentPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_moment_photos_with_options_async(request, runtime)

    def list_moments_with_options(
        self,
        request: cloud_photo_20170711_models.ListMomentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListMomentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListMomentsResponse().from_map(
            self.do_rpcrequest('ListMoments', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_moments_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListMomentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListMomentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListMomentsResponse().from_map(
            await self.do_rpcrequest_async('ListMoments', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_moments(
        self,
        request: cloud_photo_20170711_models.ListMomentsRequest,
    ) -> cloud_photo_20170711_models.ListMomentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_moments_with_options(request, runtime)

    async def list_moments_async(
        self,
        request: cloud_photo_20170711_models.ListMomentsRequest,
    ) -> cloud_photo_20170711_models.ListMomentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_moments_with_options_async(request, runtime)

    def list_photo_faces_with_options(
        self,
        request: cloud_photo_20170711_models.ListPhotoFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotoFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListPhotoFacesResponse().from_map(
            self.do_rpcrequest('ListPhotoFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_photo_faces_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListPhotoFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotoFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListPhotoFacesResponse().from_map(
            await self.do_rpcrequest_async('ListPhotoFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_photo_faces(
        self,
        request: cloud_photo_20170711_models.ListPhotoFacesRequest,
    ) -> cloud_photo_20170711_models.ListPhotoFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_photo_faces_with_options(request, runtime)

    async def list_photo_faces_async(
        self,
        request: cloud_photo_20170711_models.ListPhotoFacesRequest,
    ) -> cloud_photo_20170711_models.ListPhotoFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_photo_faces_with_options_async(request, runtime)

    def list_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ListPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListPhotosResponse().from_map(
            self.do_rpcrequest('ListPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListPhotosResponse().from_map(
            await self.do_rpcrequest_async('ListPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_photos(
        self,
        request: cloud_photo_20170711_models.ListPhotosRequest,
    ) -> cloud_photo_20170711_models.ListPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_photos_with_options(request, runtime)

    async def list_photos_async(
        self,
        request: cloud_photo_20170711_models.ListPhotosRequest,
    ) -> cloud_photo_20170711_models.ListPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_photos_with_options_async(request, runtime)

    def list_photo_stores_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotoStoresResponse:
        req = open_api_models.OpenApiRequest()
        return cloud_photo_20170711_models.ListPhotoStoresResponse().from_map(
            self.do_rpcrequest('ListPhotoStores', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_photo_stores_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotoStoresResponse:
        req = open_api_models.OpenApiRequest()
        return cloud_photo_20170711_models.ListPhotoStoresResponse().from_map(
            await self.do_rpcrequest_async('ListPhotoStores', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_photo_stores(self) -> cloud_photo_20170711_models.ListPhotoStoresResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_photo_stores_with_options(runtime)

    async def list_photo_stores_async(self) -> cloud_photo_20170711_models.ListPhotoStoresResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_photo_stores_with_options_async(runtime)

    def list_photo_tags_with_options(
        self,
        request: cloud_photo_20170711_models.ListPhotoTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotoTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListPhotoTagsResponse().from_map(
            self.do_rpcrequest('ListPhotoTags', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_photo_tags_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListPhotoTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListPhotoTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListPhotoTagsResponse().from_map(
            await self.do_rpcrequest_async('ListPhotoTags', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_photo_tags(
        self,
        request: cloud_photo_20170711_models.ListPhotoTagsRequest,
    ) -> cloud_photo_20170711_models.ListPhotoTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_photo_tags_with_options(request, runtime)

    async def list_photo_tags_async(
        self,
        request: cloud_photo_20170711_models.ListPhotoTagsRequest,
    ) -> cloud_photo_20170711_models.ListPhotoTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_photo_tags_with_options_async(request, runtime)

    def list_registered_tags_with_options(
        self,
        request: cloud_photo_20170711_models.ListRegisteredTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListRegisteredTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListRegisteredTagsResponse().from_map(
            self.do_rpcrequest('ListRegisteredTags', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_registered_tags_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListRegisteredTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListRegisteredTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListRegisteredTagsResponse().from_map(
            await self.do_rpcrequest_async('ListRegisteredTags', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_registered_tags(
        self,
        request: cloud_photo_20170711_models.ListRegisteredTagsRequest,
    ) -> cloud_photo_20170711_models.ListRegisteredTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_registered_tags_with_options(request, runtime)

    async def list_registered_tags_async(
        self,
        request: cloud_photo_20170711_models.ListRegisteredTagsRequest,
    ) -> cloud_photo_20170711_models.ListRegisteredTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_registered_tags_with_options_async(request, runtime)

    def list_tag_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ListTagPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTagPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTagPhotosResponse().from_map(
            self.do_rpcrequest('ListTagPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListTagPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTagPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTagPhotosResponse().from_map(
            await self.do_rpcrequest_async('ListTagPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_photos(
        self,
        request: cloud_photo_20170711_models.ListTagPhotosRequest,
    ) -> cloud_photo_20170711_models.ListTagPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_photos_with_options(request, runtime)

    async def list_tag_photos_async(
        self,
        request: cloud_photo_20170711_models.ListTagPhotosRequest,
    ) -> cloud_photo_20170711_models.ListTagPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_photos_with_options_async(request, runtime)

    def list_tags_with_options(
        self,
        request: cloud_photo_20170711_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTagsResponse().from_map(
            self.do_rpcrequest('ListTags', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTagsResponse().from_map(
            await self.do_rpcrequest_async('ListTags', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tags(
        self,
        request: cloud_photo_20170711_models.ListTagsRequest,
    ) -> cloud_photo_20170711_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: cloud_photo_20170711_models.ListTagsRequest,
    ) -> cloud_photo_20170711_models.ListTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def list_time_line_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ListTimeLinePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTimeLinePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTimeLinePhotosResponse().from_map(
            self.do_rpcrequest('ListTimeLinePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_time_line_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListTimeLinePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTimeLinePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTimeLinePhotosResponse().from_map(
            await self.do_rpcrequest_async('ListTimeLinePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_time_line_photos(
        self,
        request: cloud_photo_20170711_models.ListTimeLinePhotosRequest,
    ) -> cloud_photo_20170711_models.ListTimeLinePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_time_line_photos_with_options(request, runtime)

    async def list_time_line_photos_async(
        self,
        request: cloud_photo_20170711_models.ListTimeLinePhotosRequest,
    ) -> cloud_photo_20170711_models.ListTimeLinePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_time_line_photos_with_options_async(request, runtime)

    def list_time_lines_with_options(
        self,
        request: cloud_photo_20170711_models.ListTimeLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTimeLinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTimeLinesResponse().from_map(
            self.do_rpcrequest('ListTimeLines', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_time_lines_with_options_async(
        self,
        request: cloud_photo_20170711_models.ListTimeLinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ListTimeLinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ListTimeLinesResponse().from_map(
            await self.do_rpcrequest_async('ListTimeLines', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_time_lines(
        self,
        request: cloud_photo_20170711_models.ListTimeLinesRequest,
    ) -> cloud_photo_20170711_models.ListTimeLinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_time_lines_with_options(request, runtime)

    async def list_time_lines_async(
        self,
        request: cloud_photo_20170711_models.ListTimeLinesRequest,
    ) -> cloud_photo_20170711_models.ListTimeLinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_time_lines_with_options_async(request, runtime)

    def merge_faces_with_options(
        self,
        request: cloud_photo_20170711_models.MergeFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.MergeFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.MergeFacesResponse().from_map(
            self.do_rpcrequest('MergeFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def merge_faces_with_options_async(
        self,
        request: cloud_photo_20170711_models.MergeFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.MergeFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.MergeFacesResponse().from_map(
            await self.do_rpcrequest_async('MergeFaces', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def merge_faces(
        self,
        request: cloud_photo_20170711_models.MergeFacesRequest,
    ) -> cloud_photo_20170711_models.MergeFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.merge_faces_with_options(request, runtime)

    async def merge_faces_async(
        self,
        request: cloud_photo_20170711_models.MergeFacesRequest,
    ) -> cloud_photo_20170711_models.MergeFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.merge_faces_with_options_async(request, runtime)

    def move_album_photos_with_options(
        self,
        request: cloud_photo_20170711_models.MoveAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.MoveAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.MoveAlbumPhotosResponse().from_map(
            self.do_rpcrequest('MoveAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_album_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.MoveAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.MoveAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.MoveAlbumPhotosResponse().from_map(
            await self.do_rpcrequest_async('MoveAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_album_photos(
        self,
        request: cloud_photo_20170711_models.MoveAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.MoveAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_album_photos_with_options(request, runtime)

    async def move_album_photos_async(
        self,
        request: cloud_photo_20170711_models.MoveAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.MoveAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_album_photos_with_options_async(request, runtime)

    def move_face_photos_with_options(
        self,
        request: cloud_photo_20170711_models.MoveFacePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.MoveFacePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.MoveFacePhotosResponse().from_map(
            self.do_rpcrequest('MoveFacePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_face_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.MoveFacePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.MoveFacePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.MoveFacePhotosResponse().from_map(
            await self.do_rpcrequest_async('MoveFacePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_face_photos(
        self,
        request: cloud_photo_20170711_models.MoveFacePhotosRequest,
    ) -> cloud_photo_20170711_models.MoveFacePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_face_photos_with_options(request, runtime)

    async def move_face_photos_async(
        self,
        request: cloud_photo_20170711_models.MoveFacePhotosRequest,
    ) -> cloud_photo_20170711_models.MoveFacePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_face_photos_with_options_async(request, runtime)

    def reactivate_photos_with_options(
        self,
        request: cloud_photo_20170711_models.ReactivatePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ReactivatePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ReactivatePhotosResponse().from_map(
            self.do_rpcrequest('ReactivatePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reactivate_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.ReactivatePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ReactivatePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ReactivatePhotosResponse().from_map(
            await self.do_rpcrequest_async('ReactivatePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reactivate_photos(
        self,
        request: cloud_photo_20170711_models.ReactivatePhotosRequest,
    ) -> cloud_photo_20170711_models.ReactivatePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.reactivate_photos_with_options(request, runtime)

    async def reactivate_photos_async(
        self,
        request: cloud_photo_20170711_models.ReactivatePhotosRequest,
    ) -> cloud_photo_20170711_models.ReactivatePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reactivate_photos_with_options_async(request, runtime)

    def register_photo_with_options(
        self,
        request: cloud_photo_20170711_models.RegisterPhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RegisterPhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RegisterPhotoResponse().from_map(
            self.do_rpcrequest('RegisterPhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_photo_with_options_async(
        self,
        request: cloud_photo_20170711_models.RegisterPhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RegisterPhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RegisterPhotoResponse().from_map(
            await self.do_rpcrequest_async('RegisterPhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_photo(
        self,
        request: cloud_photo_20170711_models.RegisterPhotoRequest,
    ) -> cloud_photo_20170711_models.RegisterPhotoResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_photo_with_options(request, runtime)

    async def register_photo_async(
        self,
        request: cloud_photo_20170711_models.RegisterPhotoRequest,
    ) -> cloud_photo_20170711_models.RegisterPhotoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_photo_with_options_async(request, runtime)

    def register_tag_with_options(
        self,
        request: cloud_photo_20170711_models.RegisterTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RegisterTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RegisterTagResponse().from_map(
            self.do_rpcrequest('RegisterTag', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_tag_with_options_async(
        self,
        request: cloud_photo_20170711_models.RegisterTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RegisterTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RegisterTagResponse().from_map(
            await self.do_rpcrequest_async('RegisterTag', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_tag(
        self,
        request: cloud_photo_20170711_models.RegisterTagRequest,
    ) -> cloud_photo_20170711_models.RegisterTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_tag_with_options(request, runtime)

    async def register_tag_async(
        self,
        request: cloud_photo_20170711_models.RegisterTagRequest,
    ) -> cloud_photo_20170711_models.RegisterTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_tag_with_options_async(request, runtime)

    def remove_album_photos_with_options(
        self,
        request: cloud_photo_20170711_models.RemoveAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RemoveAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RemoveAlbumPhotosResponse().from_map(
            self.do_rpcrequest('RemoveAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_album_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.RemoveAlbumPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RemoveAlbumPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RemoveAlbumPhotosResponse().from_map(
            await self.do_rpcrequest_async('RemoveAlbumPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_album_photos(
        self,
        request: cloud_photo_20170711_models.RemoveAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.RemoveAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_album_photos_with_options(request, runtime)

    async def remove_album_photos_async(
        self,
        request: cloud_photo_20170711_models.RemoveAlbumPhotosRequest,
    ) -> cloud_photo_20170711_models.RemoveAlbumPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_album_photos_with_options_async(request, runtime)

    def remove_face_photos_with_options(
        self,
        request: cloud_photo_20170711_models.RemoveFacePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RemoveFacePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RemoveFacePhotosResponse().from_map(
            self.do_rpcrequest('RemoveFacePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_face_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.RemoveFacePhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RemoveFacePhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RemoveFacePhotosResponse().from_map(
            await self.do_rpcrequest_async('RemoveFacePhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_face_photos(
        self,
        request: cloud_photo_20170711_models.RemoveFacePhotosRequest,
    ) -> cloud_photo_20170711_models.RemoveFacePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_face_photos_with_options(request, runtime)

    async def remove_face_photos_async(
        self,
        request: cloud_photo_20170711_models.RemoveFacePhotosRequest,
    ) -> cloud_photo_20170711_models.RemoveFacePhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_face_photos_with_options_async(request, runtime)

    def rename_album_with_options(
        self,
        request: cloud_photo_20170711_models.RenameAlbumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RenameAlbumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RenameAlbumResponse().from_map(
            self.do_rpcrequest('RenameAlbum', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rename_album_with_options_async(
        self,
        request: cloud_photo_20170711_models.RenameAlbumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RenameAlbumResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RenameAlbumResponse().from_map(
            await self.do_rpcrequest_async('RenameAlbum', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rename_album(
        self,
        request: cloud_photo_20170711_models.RenameAlbumRequest,
    ) -> cloud_photo_20170711_models.RenameAlbumResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_album_with_options(request, runtime)

    async def rename_album_async(
        self,
        request: cloud_photo_20170711_models.RenameAlbumRequest,
    ) -> cloud_photo_20170711_models.RenameAlbumResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_album_with_options_async(request, runtime)

    def rename_face_with_options(
        self,
        request: cloud_photo_20170711_models.RenameFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RenameFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RenameFaceResponse().from_map(
            self.do_rpcrequest('RenameFace', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rename_face_with_options_async(
        self,
        request: cloud_photo_20170711_models.RenameFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.RenameFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.RenameFaceResponse().from_map(
            await self.do_rpcrequest_async('RenameFace', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rename_face(
        self,
        request: cloud_photo_20170711_models.RenameFaceRequest,
    ) -> cloud_photo_20170711_models.RenameFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rename_face_with_options(request, runtime)

    async def rename_face_async(
        self,
        request: cloud_photo_20170711_models.RenameFaceRequest,
    ) -> cloud_photo_20170711_models.RenameFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rename_face_with_options_async(request, runtime)

    def search_photos_with_options(
        self,
        request: cloud_photo_20170711_models.SearchPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SearchPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SearchPhotosResponse().from_map(
            self.do_rpcrequest('SearchPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_photos_with_options_async(
        self,
        request: cloud_photo_20170711_models.SearchPhotosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SearchPhotosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SearchPhotosResponse().from_map(
            await self.do_rpcrequest_async('SearchPhotos', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_photos(
        self,
        request: cloud_photo_20170711_models.SearchPhotosRequest,
    ) -> cloud_photo_20170711_models.SearchPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_photos_with_options(request, runtime)

    async def search_photos_async(
        self,
        request: cloud_photo_20170711_models.SearchPhotosRequest,
    ) -> cloud_photo_20170711_models.SearchPhotosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_photos_with_options_async(request, runtime)

    def set_album_cover_with_options(
        self,
        request: cloud_photo_20170711_models.SetAlbumCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetAlbumCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetAlbumCoverResponse().from_map(
            self.do_rpcrequest('SetAlbumCover', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_album_cover_with_options_async(
        self,
        request: cloud_photo_20170711_models.SetAlbumCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetAlbumCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetAlbumCoverResponse().from_map(
            await self.do_rpcrequest_async('SetAlbumCover', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_album_cover(
        self,
        request: cloud_photo_20170711_models.SetAlbumCoverRequest,
    ) -> cloud_photo_20170711_models.SetAlbumCoverResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_album_cover_with_options(request, runtime)

    async def set_album_cover_async(
        self,
        request: cloud_photo_20170711_models.SetAlbumCoverRequest,
    ) -> cloud_photo_20170711_models.SetAlbumCoverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_album_cover_with_options_async(request, runtime)

    def set_face_cover_with_options(
        self,
        request: cloud_photo_20170711_models.SetFaceCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetFaceCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetFaceCoverResponse().from_map(
            self.do_rpcrequest('SetFaceCover', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_face_cover_with_options_async(
        self,
        request: cloud_photo_20170711_models.SetFaceCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetFaceCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetFaceCoverResponse().from_map(
            await self.do_rpcrequest_async('SetFaceCover', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_face_cover(
        self,
        request: cloud_photo_20170711_models.SetFaceCoverRequest,
    ) -> cloud_photo_20170711_models.SetFaceCoverResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_face_cover_with_options(request, runtime)

    async def set_face_cover_async(
        self,
        request: cloud_photo_20170711_models.SetFaceCoverRequest,
    ) -> cloud_photo_20170711_models.SetFaceCoverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_face_cover_with_options_async(request, runtime)

    def set_me_with_options(
        self,
        request: cloud_photo_20170711_models.SetMeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetMeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetMeResponse().from_map(
            self.do_rpcrequest('SetMe', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_me_with_options_async(
        self,
        request: cloud_photo_20170711_models.SetMeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetMeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetMeResponse().from_map(
            await self.do_rpcrequest_async('SetMe', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_me(
        self,
        request: cloud_photo_20170711_models.SetMeRequest,
    ) -> cloud_photo_20170711_models.SetMeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_me_with_options(request, runtime)

    async def set_me_async(
        self,
        request: cloud_photo_20170711_models.SetMeRequest,
    ) -> cloud_photo_20170711_models.SetMeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_me_with_options_async(request, runtime)

    def set_quota_with_options(
        self,
        request: cloud_photo_20170711_models.SetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetQuotaResponse().from_map(
            self.do_rpcrequest('SetQuota', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_quota_with_options_async(
        self,
        request: cloud_photo_20170711_models.SetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.SetQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.SetQuotaResponse().from_map(
            await self.do_rpcrequest_async('SetQuota', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_quota(
        self,
        request: cloud_photo_20170711_models.SetQuotaRequest,
    ) -> cloud_photo_20170711_models.SetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_quota_with_options(request, runtime)

    async def set_quota_async(
        self,
        request: cloud_photo_20170711_models.SetQuotaRequest,
    ) -> cloud_photo_20170711_models.SetQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_quota_with_options_async(request, runtime)

    def tag_photo_with_options(
        self,
        request: cloud_photo_20170711_models.TagPhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.TagPhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.TagPhotoResponse().from_map(
            self.do_rpcrequest('TagPhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_photo_with_options_async(
        self,
        request: cloud_photo_20170711_models.TagPhotoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.TagPhotoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.TagPhotoResponse().from_map(
            await self.do_rpcrequest_async('TagPhoto', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_photo(
        self,
        request: cloud_photo_20170711_models.TagPhotoRequest,
    ) -> cloud_photo_20170711_models.TagPhotoResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_photo_with_options(request, runtime)

    async def tag_photo_async(
        self,
        request: cloud_photo_20170711_models.TagPhotoRequest,
    ) -> cloud_photo_20170711_models.TagPhotoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_photo_with_options_async(request, runtime)

    def toggle_features_with_options(
        self,
        request: cloud_photo_20170711_models.ToggleFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ToggleFeaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ToggleFeaturesResponse().from_map(
            self.do_rpcrequest('ToggleFeatures', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def toggle_features_with_options_async(
        self,
        request: cloud_photo_20170711_models.ToggleFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloud_photo_20170711_models.ToggleFeaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cloud_photo_20170711_models.ToggleFeaturesResponse().from_map(
            await self.do_rpcrequest_async('ToggleFeatures', '2017-07-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def toggle_features(
        self,
        request: cloud_photo_20170711_models.ToggleFeaturesRequest,
    ) -> cloud_photo_20170711_models.ToggleFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.toggle_features_with_options(request, runtime)

    async def toggle_features_async(
        self,
        request: cloud_photo_20170711_models.ToggleFeaturesRequest,
    ) -> cloud_photo_20170711_models.ToggleFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.toggle_features_with_options_async(request, runtime)
