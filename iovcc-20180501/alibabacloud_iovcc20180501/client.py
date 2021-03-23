# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iovcc20180501 import models as iovcc_20180501_models
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
        self._endpoint = self.get_endpoint('iovcc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_uploaded_function_file_info_with_options(
        self,
        request: iovcc_20180501_models.AddUploadedFunctionFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddUploadedFunctionFileInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddUploadedFunctionFileInfoResponse().from_map(
            self.do_rpcrequest('AddUploadedFunctionFileInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_uploaded_function_file_info_with_options_async(
        self,
        request: iovcc_20180501_models.AddUploadedFunctionFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddUploadedFunctionFileInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddUploadedFunctionFileInfoResponse().from_map(
            await self.do_rpcrequest_async('AddUploadedFunctionFileInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_uploaded_function_file_info(
        self,
        request: iovcc_20180501_models.AddUploadedFunctionFileInfoRequest,
    ) -> iovcc_20180501_models.AddUploadedFunctionFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_uploaded_function_file_info_with_options(request, runtime)

    async def add_uploaded_function_file_info_async(
        self,
        request: iovcc_20180501_models.AddUploadedFunctionFileInfoRequest,
    ) -> iovcc_20180501_models.AddUploadedFunctionFileInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_uploaded_function_file_info_with_options_async(request, runtime)

    def add_version_black_devices_with_options(
        self,
        request: iovcc_20180501_models.AddVersionBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionBlackDevicesResponse().from_map(
            self.do_rpcrequest('AddVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_version_black_devices_with_options_async(
        self,
        request: iovcc_20180501_models.AddVersionBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionBlackDevicesResponse().from_map(
            await self.do_rpcrequest_async('AddVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_black_devices(
        self,
        request: iovcc_20180501_models.AddVersionBlackDevicesRequest,
    ) -> iovcc_20180501_models.AddVersionBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_version_black_devices_with_options(request, runtime)

    async def add_version_black_devices_async(
        self,
        request: iovcc_20180501_models.AddVersionBlackDevicesRequest,
    ) -> iovcc_20180501_models.AddVersionBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_version_black_devices_with_options_async(request, runtime)

    def add_version_group_devices_with_options(
        self,
        request: iovcc_20180501_models.AddVersionGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionGroupDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionGroupDevicesResponse().from_map(
            self.do_rpcrequest('AddVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_version_group_devices_with_options_async(
        self,
        request: iovcc_20180501_models.AddVersionGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionGroupDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionGroupDevicesResponse().from_map(
            await self.do_rpcrequest_async('AddVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_group_devices(
        self,
        request: iovcc_20180501_models.AddVersionGroupDevicesRequest,
    ) -> iovcc_20180501_models.AddVersionGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_version_group_devices_with_options(request, runtime)

    async def add_version_group_devices_async(
        self,
        request: iovcc_20180501_models.AddVersionGroupDevicesRequest,
    ) -> iovcc_20180501_models.AddVersionGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_version_group_devices_with_options_async(request, runtime)

    def add_version_white_devices_with_options(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionWhiteDevicesResponse().from_map(
            self.do_rpcrequest('AddVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_version_white_devices_with_options_async(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionWhiteDevicesResponse().from_map(
            await self.do_rpcrequest_async('AddVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_white_devices(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesRequest,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_version_white_devices_with_options(request, runtime)

    async def add_version_white_devices_async(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesRequest,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_version_white_devices_with_options_async(request, runtime)

    def add_version_white_devices_by_device_groups_with_options(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsResponse().from_map(
            self.do_rpcrequest('AddVersionWhiteDevicesByDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_version_white_devices_by_device_groups_with_options_async(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsResponse().from_map(
            await self.do_rpcrequest_async('AddVersionWhiteDevicesByDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_white_devices_by_device_groups(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsRequest,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_version_white_devices_by_device_groups_with_options(request, runtime)

    async def add_version_white_devices_by_device_groups_async(
        self,
        request: iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsRequest,
    ) -> iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_version_white_devices_by_device_groups_with_options_async(request, runtime)

    def connect_assist_device_with_options(
        self,
        request: iovcc_20180501_models.ConnectAssistDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ConnectAssistDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ConnectAssistDeviceResponse().from_map(
            self.do_rpcrequest('ConnectAssistDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def connect_assist_device_with_options_async(
        self,
        request: iovcc_20180501_models.ConnectAssistDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ConnectAssistDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ConnectAssistDeviceResponse().from_map(
            await self.do_rpcrequest_async('ConnectAssistDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def connect_assist_device(
        self,
        request: iovcc_20180501_models.ConnectAssistDeviceRequest,
    ) -> iovcc_20180501_models.ConnectAssistDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.connect_assist_device_with_options(request, runtime)

    async def connect_assist_device_async(
        self,
        request: iovcc_20180501_models.ConnectAssistDeviceRequest,
    ) -> iovcc_20180501_models.ConnectAssistDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.connect_assist_device_with_options_async(request, runtime)

    def count_activated_or_new_registration_device_with_options(
        self,
        request: iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceResponse().from_map(
            self.do_rpcrequest('CountActivatedOrNewRegistrationDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def count_activated_or_new_registration_device_with_options_async(
        self,
        request: iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceResponse().from_map(
            await self.do_rpcrequest_async('CountActivatedOrNewRegistrationDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def count_activated_or_new_registration_device(
        self,
        request: iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceRequest,
    ) -> iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_activated_or_new_registration_device_with_options(request, runtime)

    async def count_activated_or_new_registration_device_async(
        self,
        request: iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceRequest,
    ) -> iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_activated_or_new_registration_device_with_options_async(request, runtime)

    def count_device_brands_with_options(
        self,
        request: iovcc_20180501_models.CountDeviceBrandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountDeviceBrandsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.CountDeviceBrandsResponse().from_map(
            self.do_rpcrequest('CountDeviceBrands', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def count_device_brands_with_options_async(
        self,
        request: iovcc_20180501_models.CountDeviceBrandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountDeviceBrandsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.CountDeviceBrandsResponse().from_map(
            await self.do_rpcrequest_async('CountDeviceBrands', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def count_device_brands(
        self,
        request: iovcc_20180501_models.CountDeviceBrandsRequest,
    ) -> iovcc_20180501_models.CountDeviceBrandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_device_brands_with_options(request, runtime)

    async def count_device_brands_async(
        self,
        request: iovcc_20180501_models.CountDeviceBrandsRequest,
    ) -> iovcc_20180501_models.CountDeviceBrandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_device_brands_with_options_async(request, runtime)

    def count_device_models_with_options(
        self,
        request: iovcc_20180501_models.CountDeviceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountDeviceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.CountDeviceModelsResponse().from_map(
            self.do_rpcrequest('CountDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def count_device_models_with_options_async(
        self,
        request: iovcc_20180501_models.CountDeviceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountDeviceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.CountDeviceModelsResponse().from_map(
            await self.do_rpcrequest_async('CountDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def count_device_models(
        self,
        request: iovcc_20180501_models.CountDeviceModelsRequest,
    ) -> iovcc_20180501_models.CountDeviceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_device_models_with_options(request, runtime)

    async def count_device_models_async(
        self,
        request: iovcc_20180501_models.CountDeviceModelsRequest,
    ) -> iovcc_20180501_models.CountDeviceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_device_models_with_options_async(request, runtime)

    def count_devices_with_options(
        self,
        request: iovcc_20180501_models.CountDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountDevicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.CountDevicesResponse().from_map(
            self.do_rpcrequest('CountDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def count_devices_with_options_async(
        self,
        request: iovcc_20180501_models.CountDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountDevicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.CountDevicesResponse().from_map(
            await self.do_rpcrequest_async('CountDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def count_devices(
        self,
        request: iovcc_20180501_models.CountDevicesRequest,
    ) -> iovcc_20180501_models.CountDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_devices_with_options(request, runtime)

    async def count_devices_async(
        self,
        request: iovcc_20180501_models.CountDevicesRequest,
    ) -> iovcc_20180501_models.CountDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_devices_with_options_async(request, runtime)

    def count_projects_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountProjectsResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.CountProjectsResponse().from_map(
            self.do_rpcrequest('CountProjects', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def count_projects_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountProjectsResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.CountProjectsResponse().from_map(
            await self.do_rpcrequest_async('CountProjects', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def count_projects(self) -> iovcc_20180501_models.CountProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_projects_with_options(runtime)

    async def count_projects_async(self) -> iovcc_20180501_models.CountProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_projects_with_options_async(runtime)

    def count_yun_id_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountYunIdInfoResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.CountYunIdInfoResponse().from_map(
            self.do_rpcrequest('CountYunIdInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def count_yun_id_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CountYunIdInfoResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.CountYunIdInfoResponse().from_map(
            await self.do_rpcrequest_async('CountYunIdInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def count_yun_id_info(self) -> iovcc_20180501_models.CountYunIdInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_yun_id_info_with_options(runtime)

    async def count_yun_id_info_async(self) -> iovcc_20180501_models.CountYunIdInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_yun_id_info_with_options_async(runtime)

    def create_app_version_with_options(
        self,
        request: iovcc_20180501_models.CreateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateAppVersionResponse().from_map(
            self.do_rpcrequest('CreateAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_version_with_options_async(
        self,
        request: iovcc_20180501_models.CreateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateAppVersionResponse().from_map(
            await self.do_rpcrequest_async('CreateAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_version(
        self,
        request: iovcc_20180501_models.CreateAppVersionRequest,
    ) -> iovcc_20180501_models.CreateAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_version_with_options(request, runtime)

    async def create_app_version_async(
        self,
        request: iovcc_20180501_models.CreateAppVersionRequest,
    ) -> iovcc_20180501_models.CreateAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_version_with_options_async(request, runtime)

    def create_customized_filter_with_options(
        self,
        request: iovcc_20180501_models.CreateCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateCustomizedFilterResponse().from_map(
            self.do_rpcrequest('CreateCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_customized_filter_with_options_async(
        self,
        request: iovcc_20180501_models.CreateCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateCustomizedFilterResponse().from_map(
            await self.do_rpcrequest_async('CreateCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_customized_filter(
        self,
        request: iovcc_20180501_models.CreateCustomizedFilterRequest,
    ) -> iovcc_20180501_models.CreateCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_customized_filter_with_options(request, runtime)

    async def create_customized_filter_async(
        self,
        request: iovcc_20180501_models.CreateCustomizedFilterRequest,
    ) -> iovcc_20180501_models.CreateCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_customized_filter_with_options_async(request, runtime)

    def create_customized_property_with_options(
        self,
        request: iovcc_20180501_models.CreateCustomizedPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateCustomizedPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateCustomizedPropertyResponse().from_map(
            self.do_rpcrequest('CreateCustomizedProperty', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_customized_property_with_options_async(
        self,
        request: iovcc_20180501_models.CreateCustomizedPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateCustomizedPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateCustomizedPropertyResponse().from_map(
            await self.do_rpcrequest_async('CreateCustomizedProperty', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_customized_property(
        self,
        request: iovcc_20180501_models.CreateCustomizedPropertyRequest,
    ) -> iovcc_20180501_models.CreateCustomizedPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_customized_property_with_options(request, runtime)

    async def create_customized_property_async(
        self,
        request: iovcc_20180501_models.CreateCustomizedPropertyRequest,
    ) -> iovcc_20180501_models.CreateCustomizedPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_customized_property_with_options_async(request, runtime)

    def create_device_with_options(
        self,
        request: iovcc_20180501_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateDeviceResponse().from_map(
            self.do_rpcrequest('CreateDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_with_options_async(
        self,
        request: iovcc_20180501_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateDeviceResponse().from_map(
            await self.do_rpcrequest_async('CreateDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device(
        self,
        request: iovcc_20180501_models.CreateDeviceRequest,
    ) -> iovcc_20180501_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    async def create_device_async(
        self,
        request: iovcc_20180501_models.CreateDeviceRequest,
    ) -> iovcc_20180501_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_with_options_async(request, runtime)

    def create_device_brand_with_options(
        self,
        request: iovcc_20180501_models.CreateDeviceBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateDeviceBrandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateDeviceBrandResponse().from_map(
            self.do_rpcrequest('CreateDeviceBrand', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_brand_with_options_async(
        self,
        request: iovcc_20180501_models.CreateDeviceBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateDeviceBrandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateDeviceBrandResponse().from_map(
            await self.do_rpcrequest_async('CreateDeviceBrand', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_brand(
        self,
        request: iovcc_20180501_models.CreateDeviceBrandRequest,
    ) -> iovcc_20180501_models.CreateDeviceBrandResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_brand_with_options(request, runtime)

    async def create_device_brand_async(
        self,
        request: iovcc_20180501_models.CreateDeviceBrandRequest,
    ) -> iovcc_20180501_models.CreateDeviceBrandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_brand_with_options_async(request, runtime)

    def create_device_model_with_options(
        self,
        request: iovcc_20180501_models.CreateDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateDeviceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateDeviceModelResponse().from_map(
            self.do_rpcrequest('CreateDeviceModel', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_model_with_options_async(
        self,
        request: iovcc_20180501_models.CreateDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateDeviceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateDeviceModelResponse().from_map(
            await self.do_rpcrequest_async('CreateDeviceModel', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_model(
        self,
        request: iovcc_20180501_models.CreateDeviceModelRequest,
    ) -> iovcc_20180501_models.CreateDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_model_with_options(request, runtime)

    async def create_device_model_async(
        self,
        request: iovcc_20180501_models.CreateDeviceModelRequest,
    ) -> iovcc_20180501_models.CreateDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_model_with_options_async(request, runtime)

    def create_mqtt_root_topic_with_options(
        self,
        request: iovcc_20180501_models.CreateMqttRootTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateMqttRootTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateMqttRootTopicResponse().from_map(
            self.do_rpcrequest('CreateMqttRootTopic', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mqtt_root_topic_with_options_async(
        self,
        request: iovcc_20180501_models.CreateMqttRootTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateMqttRootTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateMqttRootTopicResponse().from_map(
            await self.do_rpcrequest_async('CreateMqttRootTopic', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mqtt_root_topic(
        self,
        request: iovcc_20180501_models.CreateMqttRootTopicRequest,
    ) -> iovcc_20180501_models.CreateMqttRootTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mqtt_root_topic_with_options(request, runtime)

    async def create_mqtt_root_topic_async(
        self,
        request: iovcc_20180501_models.CreateMqttRootTopicRequest,
    ) -> iovcc_20180501_models.CreateMqttRootTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mqtt_root_topic_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: iovcc_20180501_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateNamespaceResponse().from_map(
            self.do_rpcrequest('CreateNamespace', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: iovcc_20180501_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateNamespaceResponse().from_map(
            await self.do_rpcrequest_async('CreateNamespace', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_namespace(
        self,
        request: iovcc_20180501_models.CreateNamespaceRequest,
    ) -> iovcc_20180501_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: iovcc_20180501_models.CreateNamespaceRequest,
    ) -> iovcc_20180501_models.CreateNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_os_version_with_options(
        self,
        request: iovcc_20180501_models.CreateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateOsVersionResponse().from_map(
            self.do_rpcrequest('CreateOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_os_version_with_options_async(
        self,
        request: iovcc_20180501_models.CreateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateOsVersionResponse().from_map(
            await self.do_rpcrequest_async('CreateOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_os_version(
        self,
        request: iovcc_20180501_models.CreateOsVersionRequest,
    ) -> iovcc_20180501_models.CreateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_os_version_with_options(request, runtime)

    async def create_os_version_async(
        self,
        request: iovcc_20180501_models.CreateOsVersionRequest,
    ) -> iovcc_20180501_models.CreateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_os_version_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        request: iovcc_20180501_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateProjectResponse().from_map(
            self.do_rpcrequest('CreateProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: iovcc_20180501_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: iovcc_20180501_models.CreateProjectRequest,
    ) -> iovcc_20180501_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: iovcc_20180501_models.CreateProjectRequest,
    ) -> iovcc_20180501_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_project_app_with_options(
        self,
        request: iovcc_20180501_models.CreateProjectAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateProjectAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateProjectAppResponse().from_map(
            self.do_rpcrequest('CreateProjectApp', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_app_with_options_async(
        self,
        request: iovcc_20180501_models.CreateProjectAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateProjectAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateProjectAppResponse().from_map(
            await self.do_rpcrequest_async('CreateProjectApp', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project_app(
        self,
        request: iovcc_20180501_models.CreateProjectAppRequest,
    ) -> iovcc_20180501_models.CreateProjectAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_app_with_options(request, runtime)

    async def create_project_app_async(
        self,
        request: iovcc_20180501_models.CreateProjectAppRequest,
    ) -> iovcc_20180501_models.CreateProjectAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_app_with_options_async(request, runtime)

    def create_rpc_service_with_options(
        self,
        request: iovcc_20180501_models.CreateRpcServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateRpcServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateRpcServiceResponse().from_map(
            self.do_rpcrequest('CreateRpcService', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rpc_service_with_options_async(
        self,
        request: iovcc_20180501_models.CreateRpcServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateRpcServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateRpcServiceResponse().from_map(
            await self.do_rpcrequest_async('CreateRpcService', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rpc_service(
        self,
        request: iovcc_20180501_models.CreateRpcServiceRequest,
    ) -> iovcc_20180501_models.CreateRpcServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rpc_service_with_options(request, runtime)

    async def create_rpc_service_async(
        self,
        request: iovcc_20180501_models.CreateRpcServiceRequest,
    ) -> iovcc_20180501_models.CreateRpcServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rpc_service_with_options_async(request, runtime)

    def create_schema_subscribe_with_options(
        self,
        request: iovcc_20180501_models.CreateSchemaSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateSchemaSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateSchemaSubscribeResponse().from_map(
            self.do_rpcrequest('CreateSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_schema_subscribe_with_options_async(
        self,
        request: iovcc_20180501_models.CreateSchemaSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateSchemaSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateSchemaSubscribeResponse().from_map(
            await self.do_rpcrequest_async('CreateSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_schema_subscribe(
        self,
        request: iovcc_20180501_models.CreateSchemaSubscribeRequest,
    ) -> iovcc_20180501_models.CreateSchemaSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_schema_subscribe_with_options(request, runtime)

    async def create_schema_subscribe_async(
        self,
        request: iovcc_20180501_models.CreateSchemaSubscribeRequest,
    ) -> iovcc_20180501_models.CreateSchemaSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_schema_subscribe_with_options_async(request, runtime)

    def create_shadow_schema_with_options(
        self,
        request: iovcc_20180501_models.CreateShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateShadowSchemaResponse().from_map(
            self.do_rpcrequest('CreateShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_shadow_schema_with_options_async(
        self,
        request: iovcc_20180501_models.CreateShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateShadowSchemaResponse().from_map(
            await self.do_rpcrequest_async('CreateShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_shadow_schema(
        self,
        request: iovcc_20180501_models.CreateShadowSchemaRequest,
    ) -> iovcc_20180501_models.CreateShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_shadow_schema_with_options(request, runtime)

    async def create_shadow_schema_async(
        self,
        request: iovcc_20180501_models.CreateShadowSchemaRequest,
    ) -> iovcc_20180501_models.CreateShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_shadow_schema_with_options_async(request, runtime)

    def create_trigger_with_options(
        self,
        request: iovcc_20180501_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateTriggerResponse().from_map(
            self.do_rpcrequest('CreateTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        request: iovcc_20180501_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateTriggerResponse().from_map(
            await self.do_rpcrequest_async('CreateTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_trigger(
        self,
        request: iovcc_20180501_models.CreateTriggerRequest,
    ) -> iovcc_20180501_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_trigger_with_options(request, runtime)

    async def create_trigger_async(
        self,
        request: iovcc_20180501_models.CreateTriggerRequest,
    ) -> iovcc_20180501_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_trigger_with_options_async(request, runtime)

    def create_upstream_app_key_relation_with_options(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateUpstreamAppKeyRelationResponse().from_map(
            self.do_rpcrequest('CreateUpstreamAppKeyRelation', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upstream_app_key_relation_with_options_async(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateUpstreamAppKeyRelationResponse().from_map(
            await self.do_rpcrequest_async('CreateUpstreamAppKeyRelation', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upstream_app_key_relation(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationRequest,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upstream_app_key_relation_with_options(request, runtime)

    async def create_upstream_app_key_relation_async(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationRequest,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upstream_app_key_relation_with_options_async(request, runtime)

    def create_upstream_app_key_relations_with_options(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateUpstreamAppKeyRelationsResponse().from_map(
            self.do_rpcrequest('CreateUpstreamAppKeyRelations', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upstream_app_key_relations_with_options_async(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateUpstreamAppKeyRelationsResponse().from_map(
            await self.do_rpcrequest_async('CreateUpstreamAppKeyRelations', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upstream_app_key_relations(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationsRequest,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upstream_app_key_relations_with_options(request, runtime)

    async def create_upstream_app_key_relations_async(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppKeyRelationsRequest,
    ) -> iovcc_20180501_models.CreateUpstreamAppKeyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upstream_app_key_relations_with_options_async(request, runtime)

    def create_upstream_app_server_with_options(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateUpstreamAppServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateUpstreamAppServerResponse().from_map(
            self.do_rpcrequest('CreateUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upstream_app_server_with_options_async(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateUpstreamAppServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateUpstreamAppServerResponse().from_map(
            await self.do_rpcrequest_async('CreateUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upstream_app_server(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppServerRequest,
    ) -> iovcc_20180501_models.CreateUpstreamAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upstream_app_server_with_options(request, runtime)

    async def create_upstream_app_server_async(
        self,
        request: iovcc_20180501_models.CreateUpstreamAppServerRequest,
    ) -> iovcc_20180501_models.CreateUpstreamAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upstream_app_server_with_options_async(request, runtime)

    def create_version_device_group_with_options(
        self,
        request: iovcc_20180501_models.CreateVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateVersionDeviceGroupResponse().from_map(
            self.do_rpcrequest('CreateVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_version_device_group_with_options_async(
        self,
        request: iovcc_20180501_models.CreateVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateVersionDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_version_device_group(
        self,
        request: iovcc_20180501_models.CreateVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.CreateVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_version_device_group_with_options(request, runtime)

    async def create_version_device_group_async(
        self,
        request: iovcc_20180501_models.CreateVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.CreateVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_version_device_group_with_options_async(request, runtime)

    def create_version_prepublish_with_options(
        self,
        request: iovcc_20180501_models.CreateVersionPrepublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateVersionPrepublishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateVersionPrepublishResponse().from_map(
            self.do_rpcrequest('CreateVersionPrepublish', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_version_prepublish_with_options_async(
        self,
        request: iovcc_20180501_models.CreateVersionPrepublishRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateVersionPrepublishResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateVersionPrepublishResponse().from_map(
            await self.do_rpcrequest_async('CreateVersionPrepublish', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_version_prepublish(
        self,
        request: iovcc_20180501_models.CreateVersionPrepublishRequest,
    ) -> iovcc_20180501_models.CreateVersionPrepublishResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_version_prepublish_with_options(request, runtime)

    async def create_version_prepublish_async(
        self,
        request: iovcc_20180501_models.CreateVersionPrepublishRequest,
    ) -> iovcc_20180501_models.CreateVersionPrepublishResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_version_prepublish_with_options_async(request, runtime)

    def create_version_test_with_options(
        self,
        request: iovcc_20180501_models.CreateVersionTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateVersionTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateVersionTestResponse().from_map(
            self.do_rpcrequest('CreateVersionTest', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_version_test_with_options_async(
        self,
        request: iovcc_20180501_models.CreateVersionTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.CreateVersionTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.CreateVersionTestResponse().from_map(
            await self.do_rpcrequest_async('CreateVersionTest', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_version_test(
        self,
        request: iovcc_20180501_models.CreateVersionTestRequest,
    ) -> iovcc_20180501_models.CreateVersionTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_version_test_with_options(request, runtime)

    async def create_version_test_async(
        self,
        request: iovcc_20180501_models.CreateVersionTestRequest,
    ) -> iovcc_20180501_models.CreateVersionTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_version_test_with_options_async(request, runtime)

    def delay_publish_os_version_with_options(
        self,
        request: iovcc_20180501_models.DelayPublishOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DelayPublishOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DelayPublishOsVersionResponse().from_map(
            self.do_rpcrequest('DelayPublishOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delay_publish_os_version_with_options_async(
        self,
        request: iovcc_20180501_models.DelayPublishOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DelayPublishOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DelayPublishOsVersionResponse().from_map(
            await self.do_rpcrequest_async('DelayPublishOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delay_publish_os_version(
        self,
        request: iovcc_20180501_models.DelayPublishOsVersionRequest,
    ) -> iovcc_20180501_models.DelayPublishOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delay_publish_os_version_with_options(request, runtime)

    async def delay_publish_os_version_async(
        self,
        request: iovcc_20180501_models.DelayPublishOsVersionRequest,
    ) -> iovcc_20180501_models.DelayPublishOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delay_publish_os_version_with_options_async(request, runtime)

    def delete_all_customized_filters_with_options(
        self,
        request: iovcc_20180501_models.DeleteAllCustomizedFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteAllCustomizedFiltersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteAllCustomizedFiltersResponse().from_map(
            self.do_rpcrequest('DeleteAllCustomizedFilters', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_all_customized_filters_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteAllCustomizedFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteAllCustomizedFiltersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteAllCustomizedFiltersResponse().from_map(
            await self.do_rpcrequest_async('DeleteAllCustomizedFilters', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_all_customized_filters(
        self,
        request: iovcc_20180501_models.DeleteAllCustomizedFiltersRequest,
    ) -> iovcc_20180501_models.DeleteAllCustomizedFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_all_customized_filters_with_options(request, runtime)

    async def delete_all_customized_filters_async(
        self,
        request: iovcc_20180501_models.DeleteAllCustomizedFiltersRequest,
    ) -> iovcc_20180501_models.DeleteAllCustomizedFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_all_customized_filters_with_options_async(request, runtime)

    def delete_all_version_group_devices_with_options(
        self,
        request: iovcc_20180501_models.DeleteAllVersionGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteAllVersionGroupDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteAllVersionGroupDevicesResponse().from_map(
            self.do_rpcrequest('DeleteAllVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_all_version_group_devices_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteAllVersionGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteAllVersionGroupDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteAllVersionGroupDevicesResponse().from_map(
            await self.do_rpcrequest_async('DeleteAllVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_all_version_group_devices(
        self,
        request: iovcc_20180501_models.DeleteAllVersionGroupDevicesRequest,
    ) -> iovcc_20180501_models.DeleteAllVersionGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_all_version_group_devices_with_options(request, runtime)

    async def delete_all_version_group_devices_async(
        self,
        request: iovcc_20180501_models.DeleteAllVersionGroupDevicesRequest,
    ) -> iovcc_20180501_models.DeleteAllVersionGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_all_version_group_devices_with_options_async(request, runtime)

    def delete_customized_filter_with_options(
        self,
        request: iovcc_20180501_models.DeleteCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteCustomizedFilterResponse().from_map(
            self.do_rpcrequest('DeleteCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_customized_filter_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteCustomizedFilterResponse().from_map(
            await self.do_rpcrequest_async('DeleteCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_customized_filter(
        self,
        request: iovcc_20180501_models.DeleteCustomizedFilterRequest,
    ) -> iovcc_20180501_models.DeleteCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_customized_filter_with_options(request, runtime)

    async def delete_customized_filter_async(
        self,
        request: iovcc_20180501_models.DeleteCustomizedFilterRequest,
    ) -> iovcc_20180501_models.DeleteCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_customized_filter_with_options_async(request, runtime)

    def delete_customized_property_with_options(
        self,
        request: iovcc_20180501_models.DeleteCustomizedPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteCustomizedPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteCustomizedPropertyResponse().from_map(
            self.do_rpcrequest('DeleteCustomizedProperty', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_customized_property_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteCustomizedPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteCustomizedPropertyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteCustomizedPropertyResponse().from_map(
            await self.do_rpcrequest_async('DeleteCustomizedProperty', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_customized_property(
        self,
        request: iovcc_20180501_models.DeleteCustomizedPropertyRequest,
    ) -> iovcc_20180501_models.DeleteCustomizedPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_customized_property_with_options(request, runtime)

    async def delete_customized_property_async(
        self,
        request: iovcc_20180501_models.DeleteCustomizedPropertyRequest,
    ) -> iovcc_20180501_models.DeleteCustomizedPropertyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_customized_property_with_options_async(request, runtime)

    def delete_device_with_options(
        self,
        request: iovcc_20180501_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteDeviceResponse().from_map(
            self.do_rpcrequest('DeleteDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteDeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device(
        self,
        request: iovcc_20180501_models.DeleteDeviceRequest,
    ) -> iovcc_20180501_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    async def delete_device_async(
        self,
        request: iovcc_20180501_models.DeleteDeviceRequest,
    ) -> iovcc_20180501_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_with_options_async(request, runtime)

    def delete_function_file_with_options(
        self,
        request: iovcc_20180501_models.DeleteFunctionFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteFunctionFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteFunctionFileResponse().from_map(
            self.do_rpcrequest('DeleteFunctionFile', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_function_file_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteFunctionFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteFunctionFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteFunctionFileResponse().from_map(
            await self.do_rpcrequest_async('DeleteFunctionFile', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_function_file(
        self,
        request: iovcc_20180501_models.DeleteFunctionFileRequest,
    ) -> iovcc_20180501_models.DeleteFunctionFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_function_file_with_options(request, runtime)

    async def delete_function_file_async(
        self,
        request: iovcc_20180501_models.DeleteFunctionFileRequest,
    ) -> iovcc_20180501_models.DeleteFunctionFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_function_file_with_options_async(request, runtime)

    def delete_mqtt_root_topic_with_options(
        self,
        request: iovcc_20180501_models.DeleteMqttRootTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteMqttRootTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteMqttRootTopicResponse().from_map(
            self.do_rpcrequest('DeleteMqttRootTopic', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mqtt_root_topic_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteMqttRootTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteMqttRootTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteMqttRootTopicResponse().from_map(
            await self.do_rpcrequest_async('DeleteMqttRootTopic', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mqtt_root_topic(
        self,
        request: iovcc_20180501_models.DeleteMqttRootTopicRequest,
    ) -> iovcc_20180501_models.DeleteMqttRootTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mqtt_root_topic_with_options(request, runtime)

    async def delete_mqtt_root_topic_async(
        self,
        request: iovcc_20180501_models.DeleteMqttRootTopicRequest,
    ) -> iovcc_20180501_models.DeleteMqttRootTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mqtt_root_topic_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: iovcc_20180501_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteNamespaceResponse().from_map(
            self.do_rpcrequest('DeleteNamespace', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteNamespaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteNamespace', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_namespace(
        self,
        request: iovcc_20180501_models.DeleteNamespaceRequest,
    ) -> iovcc_20180501_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: iovcc_20180501_models.DeleteNamespaceRequest,
    ) -> iovcc_20180501_models.DeleteNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_open_account_with_options(
        self,
        request: iovcc_20180501_models.DeleteOpenAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteOpenAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DeleteOpenAccountResponse().from_map(
            self.do_rpcrequest('DeleteOpenAccount', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_open_account_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteOpenAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteOpenAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DeleteOpenAccountResponse().from_map(
            await self.do_rpcrequest_async('DeleteOpenAccount', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_open_account(
        self,
        request: iovcc_20180501_models.DeleteOpenAccountRequest,
    ) -> iovcc_20180501_models.DeleteOpenAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_open_account_with_options(request, runtime)

    async def delete_open_account_async(
        self,
        request: iovcc_20180501_models.DeleteOpenAccountRequest,
    ) -> iovcc_20180501_models.DeleteOpenAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_open_account_with_options_async(request, runtime)

    def delete_project_app_with_options(
        self,
        request: iovcc_20180501_models.DeleteProjectAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteProjectAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteProjectAppResponse().from_map(
            self.do_rpcrequest('DeleteProjectApp', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_app_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteProjectAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteProjectAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteProjectAppResponse().from_map(
            await self.do_rpcrequest_async('DeleteProjectApp', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project_app(
        self,
        request: iovcc_20180501_models.DeleteProjectAppRequest,
    ) -> iovcc_20180501_models.DeleteProjectAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_app_with_options(request, runtime)

    async def delete_project_app_async(
        self,
        request: iovcc_20180501_models.DeleteProjectAppRequest,
    ) -> iovcc_20180501_models.DeleteProjectAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_app_with_options_async(request, runtime)

    def delete_rpc_service_with_options(
        self,
        request: iovcc_20180501_models.DeleteRpcServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteRpcServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteRpcServiceResponse().from_map(
            self.do_rpcrequest('DeleteRpcService', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rpc_service_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteRpcServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteRpcServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteRpcServiceResponse().from_map(
            await self.do_rpcrequest_async('DeleteRpcService', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rpc_service(
        self,
        request: iovcc_20180501_models.DeleteRpcServiceRequest,
    ) -> iovcc_20180501_models.DeleteRpcServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rpc_service_with_options(request, runtime)

    async def delete_rpc_service_async(
        self,
        request: iovcc_20180501_models.DeleteRpcServiceRequest,
    ) -> iovcc_20180501_models.DeleteRpcServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rpc_service_with_options_async(request, runtime)

    def delete_schema_subscribe_with_options(
        self,
        request: iovcc_20180501_models.DeleteSchemaSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteSchemaSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteSchemaSubscribeResponse().from_map(
            self.do_rpcrequest('DeleteSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_schema_subscribe_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteSchemaSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteSchemaSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteSchemaSubscribeResponse().from_map(
            await self.do_rpcrequest_async('DeleteSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_schema_subscribe(
        self,
        request: iovcc_20180501_models.DeleteSchemaSubscribeRequest,
    ) -> iovcc_20180501_models.DeleteSchemaSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_schema_subscribe_with_options(request, runtime)

    async def delete_schema_subscribe_async(
        self,
        request: iovcc_20180501_models.DeleteSchemaSubscribeRequest,
    ) -> iovcc_20180501_models.DeleteSchemaSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_schema_subscribe_with_options_async(request, runtime)

    def delete_shadow_schema_with_options(
        self,
        request: iovcc_20180501_models.DeleteShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteShadowSchemaResponse().from_map(
            self.do_rpcrequest('DeleteShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_shadow_schema_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteShadowSchemaResponse().from_map(
            await self.do_rpcrequest_async('DeleteShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_shadow_schema(
        self,
        request: iovcc_20180501_models.DeleteShadowSchemaRequest,
    ) -> iovcc_20180501_models.DeleteShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_shadow_schema_with_options(request, runtime)

    async def delete_shadow_schema_async(
        self,
        request: iovcc_20180501_models.DeleteShadowSchemaRequest,
    ) -> iovcc_20180501_models.DeleteShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_shadow_schema_with_options_async(request, runtime)

    def delete_trigger_with_options(
        self,
        request: iovcc_20180501_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteTriggerResponse().from_map(
            self.do_rpcrequest('DeleteTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteTriggerResponse().from_map(
            await self.do_rpcrequest_async('DeleteTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_trigger(
        self,
        request: iovcc_20180501_models.DeleteTriggerRequest,
    ) -> iovcc_20180501_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trigger_with_options(request, runtime)

    async def delete_trigger_async(
        self,
        request: iovcc_20180501_models.DeleteTriggerRequest,
    ) -> iovcc_20180501_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trigger_with_options_async(request, runtime)

    def delete_upstream_app_key_relation_with_options(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppKeyRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteUpstreamAppKeyRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteUpstreamAppKeyRelationResponse().from_map(
            self.do_rpcrequest('DeleteUpstreamAppKeyRelation', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_upstream_app_key_relation_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppKeyRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteUpstreamAppKeyRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteUpstreamAppKeyRelationResponse().from_map(
            await self.do_rpcrequest_async('DeleteUpstreamAppKeyRelation', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_upstream_app_key_relation(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppKeyRelationRequest,
    ) -> iovcc_20180501_models.DeleteUpstreamAppKeyRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_upstream_app_key_relation_with_options(request, runtime)

    async def delete_upstream_app_key_relation_async(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppKeyRelationRequest,
    ) -> iovcc_20180501_models.DeleteUpstreamAppKeyRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_upstream_app_key_relation_with_options_async(request, runtime)

    def delete_upstream_app_server_with_options(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteUpstreamAppServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteUpstreamAppServerResponse().from_map(
            self.do_rpcrequest('DeleteUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_upstream_app_server_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteUpstreamAppServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteUpstreamAppServerResponse().from_map(
            await self.do_rpcrequest_async('DeleteUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_upstream_app_server(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppServerRequest,
    ) -> iovcc_20180501_models.DeleteUpstreamAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_upstream_app_server_with_options(request, runtime)

    async def delete_upstream_app_server_async(
        self,
        request: iovcc_20180501_models.DeleteUpstreamAppServerRequest,
    ) -> iovcc_20180501_models.DeleteUpstreamAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_upstream_app_server_with_options_async(request, runtime)

    def delete_version_all_black_devices_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionAllBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionAllBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionAllBlackDevicesResponse().from_map(
            self.do_rpcrequest('DeleteVersionAllBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_all_black_devices_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionAllBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionAllBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionAllBlackDevicesResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionAllBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_all_black_devices(
        self,
        request: iovcc_20180501_models.DeleteVersionAllBlackDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionAllBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_all_black_devices_with_options(request, runtime)

    async def delete_version_all_black_devices_async(
        self,
        request: iovcc_20180501_models.DeleteVersionAllBlackDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionAllBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_all_black_devices_with_options_async(request, runtime)

    def delete_version_all_white_devices_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionAllWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionAllWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionAllWhiteDevicesResponse().from_map(
            self.do_rpcrequest('DeleteVersionAllWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_all_white_devices_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionAllWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionAllWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionAllWhiteDevicesResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionAllWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_all_white_devices(
        self,
        request: iovcc_20180501_models.DeleteVersionAllWhiteDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionAllWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_all_white_devices_with_options(request, runtime)

    async def delete_version_all_white_devices_async(
        self,
        request: iovcc_20180501_models.DeleteVersionAllWhiteDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionAllWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_all_white_devices_with_options_async(request, runtime)

    def delete_version_black_devices_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionBlackDevicesResponse().from_map(
            self.do_rpcrequest('DeleteVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_black_devices_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionBlackDevicesResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_black_devices(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_black_devices_with_options(request, runtime)

    async def delete_version_black_devices_async(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_black_devices_with_options_async(request, runtime)

    def delete_version_black_devices_by_id_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionBlackDevicesByIdResponse().from_map(
            self.do_rpcrequest('DeleteVersionBlackDevicesById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_black_devices_by_id_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionBlackDevicesByIdResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionBlackDevicesById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_black_devices_by_id(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesByIdRequest,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_black_devices_by_id_with_options(request, runtime)

    async def delete_version_black_devices_by_id_async(
        self,
        request: iovcc_20180501_models.DeleteVersionBlackDevicesByIdRequest,
    ) -> iovcc_20180501_models.DeleteVersionBlackDevicesByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_black_devices_by_id_with_options_async(request, runtime)

    def delete_version_device_group_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionDeviceGroupResponse().from_map(
            self.do_rpcrequest('DeleteVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_device_group_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_device_group(
        self,
        request: iovcc_20180501_models.DeleteVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.DeleteVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_device_group_with_options(request, runtime)

    async def delete_version_device_group_async(
        self,
        request: iovcc_20180501_models.DeleteVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.DeleteVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_device_group_with_options_async(request, runtime)

    def delete_version_group_device_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionGroupDeviceResponse().from_map(
            self.do_rpcrequest('DeleteVersionGroupDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_group_device_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionGroupDeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionGroupDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_group_device(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceRequest,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_group_device_with_options(request, runtime)

    async def delete_version_group_device_async(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceRequest,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_group_device_with_options_async(request, runtime)

    def delete_version_group_device_by_id_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionGroupDeviceByIdResponse().from_map(
            self.do_rpcrequest('DeleteVersionGroupDeviceById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_group_device_by_id_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionGroupDeviceByIdResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionGroupDeviceById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_group_device_by_id(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceByIdRequest,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_group_device_by_id_with_options(request, runtime)

    async def delete_version_group_device_by_id_async(
        self,
        request: iovcc_20180501_models.DeleteVersionGroupDeviceByIdRequest,
    ) -> iovcc_20180501_models.DeleteVersionGroupDeviceByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_group_device_by_id_with_options_async(request, runtime)

    def delete_version_test_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionTestResponse().from_map(
            self.do_rpcrequest('DeleteVersionTest', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_test_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionTestResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionTest', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_test(
        self,
        request: iovcc_20180501_models.DeleteVersionTestRequest,
    ) -> iovcc_20180501_models.DeleteVersionTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_test_with_options(request, runtime)

    async def delete_version_test_async(
        self,
        request: iovcc_20180501_models.DeleteVersionTestRequest,
    ) -> iovcc_20180501_models.DeleteVersionTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_test_with_options_async(request, runtime)

    def delete_version_white_devices_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionWhiteDevicesResponse().from_map(
            self.do_rpcrequest('DeleteVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_white_devices_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionWhiteDevicesResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_white_devices(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_white_devices_with_options(request, runtime)

    async def delete_version_white_devices_async(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesRequest,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_white_devices_with_options_async(request, runtime)

    def delete_version_white_devices_by_id_with_options(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionWhiteDevicesByIdResponse().from_map(
            self.do_rpcrequest('DeleteVersionWhiteDevicesById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_version_white_devices_by_id_with_options_async(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeleteVersionWhiteDevicesByIdResponse().from_map(
            await self.do_rpcrequest_async('DeleteVersionWhiteDevicesById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_white_devices_by_id(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesByIdRequest,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_version_white_devices_by_id_with_options(request, runtime)

    async def delete_version_white_devices_by_id_async(
        self,
        request: iovcc_20180501_models.DeleteVersionWhiteDevicesByIdRequest,
    ) -> iovcc_20180501_models.DeleteVersionWhiteDevicesByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_version_white_devices_by_id_with_options_async(request, runtime)

    def deploy_function_file_with_options(
        self,
        request: iovcc_20180501_models.DeployFunctionFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeployFunctionFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeployFunctionFileResponse().from_map(
            self.do_rpcrequest('DeployFunctionFile', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_function_file_with_options_async(
        self,
        request: iovcc_20180501_models.DeployFunctionFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DeployFunctionFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DeployFunctionFileResponse().from_map(
            await self.do_rpcrequest_async('DeployFunctionFile', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_function_file(
        self,
        request: iovcc_20180501_models.DeployFunctionFileRequest,
    ) -> iovcc_20180501_models.DeployFunctionFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_function_file_with_options(request, runtime)

    async def deploy_function_file_async(
        self,
        request: iovcc_20180501_models.DeployFunctionFileRequest,
    ) -> iovcc_20180501_models.DeployFunctionFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_function_file_with_options_async(request, runtime)

    def describe_api_gateway_app_security_with_options(
        self,
        request: iovcc_20180501_models.DescribeApiGatewayAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeApiGatewayAppSecurityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeApiGatewayAppSecurityResponse().from_map(
            self.do_rpcrequest('DescribeApiGatewayAppSecurity', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_api_gateway_app_security_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeApiGatewayAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeApiGatewayAppSecurityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeApiGatewayAppSecurityResponse().from_map(
            await self.do_rpcrequest_async('DescribeApiGatewayAppSecurity', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_gateway_app_security(
        self,
        request: iovcc_20180501_models.DescribeApiGatewayAppSecurityRequest,
    ) -> iovcc_20180501_models.DescribeApiGatewayAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_api_gateway_app_security_with_options(request, runtime)

    async def describe_api_gateway_app_security_async(
        self,
        request: iovcc_20180501_models.DescribeApiGatewayAppSecurityRequest,
    ) -> iovcc_20180501_models.DescribeApiGatewayAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_api_gateway_app_security_with_options_async(request, runtime)

    def describe_app_version_with_options(
        self,
        request: iovcc_20180501_models.DescribeAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeAppVersionResponse().from_map(
            self.do_rpcrequest('DescribeAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_app_version_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeAppVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_version(
        self,
        request: iovcc_20180501_models.DescribeAppVersionRequest,
    ) -> iovcc_20180501_models.DescribeAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_version_with_options(request, runtime)

    async def describe_app_version_async(
        self,
        request: iovcc_20180501_models.DescribeAppVersionRequest,
    ) -> iovcc_20180501_models.DescribeAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_version_with_options_async(request, runtime)

    def describe_assist_report_with_options(
        self,
        request: iovcc_20180501_models.DescribeAssistReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAssistReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeAssistReportResponse().from_map(
            self.do_rpcrequest('DescribeAssistReport', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_assist_report_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeAssistReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAssistReportResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeAssistReportResponse().from_map(
            await self.do_rpcrequest_async('DescribeAssistReport', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_assist_report(
        self,
        request: iovcc_20180501_models.DescribeAssistReportRequest,
    ) -> iovcc_20180501_models.DescribeAssistReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_assist_report_with_options(request, runtime)

    async def describe_assist_report_async(
        self,
        request: iovcc_20180501_models.DescribeAssistReportRequest,
    ) -> iovcc_20180501_models.DescribeAssistReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_assist_report_with_options_async(request, runtime)

    def describe_assist_rtmpserver_address_with_options(
        self,
        request: iovcc_20180501_models.DescribeAssistRTMPServerAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAssistRTMPServerAddressResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeAssistRTMPServerAddressResponse().from_map(
            self.do_rpcrequest('DescribeAssistRTMPServerAddress', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_assist_rtmpserver_address_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeAssistRTMPServerAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAssistRTMPServerAddressResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeAssistRTMPServerAddressResponse().from_map(
            await self.do_rpcrequest_async('DescribeAssistRTMPServerAddress', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_assist_rtmpserver_address(
        self,
        request: iovcc_20180501_models.DescribeAssistRTMPServerAddressRequest,
    ) -> iovcc_20180501_models.DescribeAssistRTMPServerAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_assist_rtmpserver_address_with_options(request, runtime)

    async def describe_assist_rtmpserver_address_async(
        self,
        request: iovcc_20180501_models.DescribeAssistRTMPServerAddressRequest,
    ) -> iovcc_20180501_models.DescribeAssistRTMPServerAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_assist_rtmpserver_address_with_options_async(request, runtime)

    def describe_assist_wsserver_address_with_options(
        self,
        request: iovcc_20180501_models.DescribeAssistWSServerAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAssistWSServerAddressResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeAssistWSServerAddressResponse().from_map(
            self.do_rpcrequest('DescribeAssistWSServerAddress', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_assist_wsserver_address_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeAssistWSServerAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeAssistWSServerAddressResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeAssistWSServerAddressResponse().from_map(
            await self.do_rpcrequest_async('DescribeAssistWSServerAddress', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_assist_wsserver_address(
        self,
        request: iovcc_20180501_models.DescribeAssistWSServerAddressRequest,
    ) -> iovcc_20180501_models.DescribeAssistWSServerAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_assist_wsserver_address_with_options(request, runtime)

    async def describe_assist_wsserver_address_async(
        self,
        request: iovcc_20180501_models.DescribeAssistWSServerAddressRequest,
    ) -> iovcc_20180501_models.DescribeAssistWSServerAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_assist_wsserver_address_with_options_async(request, runtime)

    def describe_customized_filter_with_options(
        self,
        request: iovcc_20180501_models.DescribeCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeCustomizedFilterResponse().from_map(
            self.do_rpcrequest('DescribeCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_customized_filter_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeCustomizedFilterResponse().from_map(
            await self.do_rpcrequest_async('DescribeCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_customized_filter(
        self,
        request: iovcc_20180501_models.DescribeCustomizedFilterRequest,
    ) -> iovcc_20180501_models.DescribeCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customized_filter_with_options(request, runtime)

    async def describe_customized_filter_async(
        self,
        request: iovcc_20180501_models.DescribeCustomizedFilterRequest,
    ) -> iovcc_20180501_models.DescribeCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customized_filter_with_options_async(request, runtime)

    def describe_default_schema_with_options(
        self,
        request: iovcc_20180501_models.DescribeDefaultSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDefaultSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDefaultSchemaResponse().from_map(
            self.do_rpcrequest('DescribeDefaultSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_default_schema_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDefaultSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDefaultSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDefaultSchemaResponse().from_map(
            await self.do_rpcrequest_async('DescribeDefaultSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_default_schema(
        self,
        request: iovcc_20180501_models.DescribeDefaultSchemaRequest,
    ) -> iovcc_20180501_models.DescribeDefaultSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_default_schema_with_options(request, runtime)

    async def describe_default_schema_async(
        self,
        request: iovcc_20180501_models.DescribeDefaultSchemaRequest,
    ) -> iovcc_20180501_models.DescribeDefaultSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_default_schema_with_options_async(request, runtime)

    def describe_device_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceResponse().from_map(
            self.do_rpcrequest('DescribeDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_device_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device(
        self,
        request: iovcc_20180501_models.DescribeDeviceRequest,
    ) -> iovcc_20180501_models.DescribeDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_with_options(request, runtime)

    async def describe_device_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceRequest,
    ) -> iovcc_20180501_models.DescribeDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_with_options_async(request, runtime)

    def describe_device_brand_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceBrandResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceBrandResponse().from_map(
            self.do_rpcrequest('DescribeDeviceBrand', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_device_brand_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceBrandResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceBrandResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceBrand', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_brand(
        self,
        request: iovcc_20180501_models.DescribeDeviceBrandRequest,
    ) -> iovcc_20180501_models.DescribeDeviceBrandResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_brand_with_options(request, runtime)

    async def describe_device_brand_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceBrandRequest,
    ) -> iovcc_20180501_models.DescribeDeviceBrandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_brand_with_options_async(request, runtime)

    def describe_device_id_by_outer_info_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceIdByOuterInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceIdByOuterInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceIdByOuterInfoResponse().from_map(
            self.do_rpcrequest('DescribeDeviceIdByOuterInfo', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_device_id_by_outer_info_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceIdByOuterInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceIdByOuterInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceIdByOuterInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceIdByOuterInfo', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_id_by_outer_info(
        self,
        request: iovcc_20180501_models.DescribeDeviceIdByOuterInfoRequest,
    ) -> iovcc_20180501_models.DescribeDeviceIdByOuterInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_id_by_outer_info_with_options(request, runtime)

    async def describe_device_id_by_outer_info_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceIdByOuterInfoRequest,
    ) -> iovcc_20180501_models.DescribeDeviceIdByOuterInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_id_by_outer_info_with_options_async(request, runtime)

    def describe_device_info_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceInfoResponse().from_map(
            self.do_rpcrequest('DescribeDeviceInfo', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_device_info_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceInfo', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_info(
        self,
        request: iovcc_20180501_models.DescribeDeviceInfoRequest,
    ) -> iovcc_20180501_models.DescribeDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    async def describe_device_info_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceInfoRequest,
    ) -> iovcc_20180501_models.DescribeDeviceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_info_with_options_async(request, runtime)

    def describe_device_model_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceModelResponse().from_map(
            self.do_rpcrequest('DescribeDeviceModel', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_device_model_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeDeviceModelResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceModel', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_model(
        self,
        request: iovcc_20180501_models.DescribeDeviceModelRequest,
    ) -> iovcc_20180501_models.DescribeDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_model_with_options(request, runtime)

    async def describe_device_model_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceModelRequest,
    ) -> iovcc_20180501_models.DescribeDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_model_with_options_async(request, runtime)

    def describe_device_online_info_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceOnlineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceOnlineInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceOnlineInfoResponse().from_map(
            self.do_rpcrequest('DescribeDeviceOnlineInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_device_online_info_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceOnlineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceOnlineInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceOnlineInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceOnlineInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_online_info(
        self,
        request: iovcc_20180501_models.DescribeDeviceOnlineInfoRequest,
    ) -> iovcc_20180501_models.DescribeDeviceOnlineInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_online_info_with_options(request, runtime)

    async def describe_device_online_info_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceOnlineInfoRequest,
    ) -> iovcc_20180501_models.DescribeDeviceOnlineInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_online_info_with_options_async(request, runtime)

    def describe_device_shadow_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceShadowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceShadowResponse().from_map(
            self.do_rpcrequest('DescribeDeviceShadow', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_device_shadow_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceShadowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceShadowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceShadowResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceShadow', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_shadow(
        self,
        request: iovcc_20180501_models.DescribeDeviceShadowRequest,
    ) -> iovcc_20180501_models.DescribeDeviceShadowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_shadow_with_options(request, runtime)

    async def describe_device_shadow_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceShadowRequest,
    ) -> iovcc_20180501_models.DescribeDeviceShadowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_shadow_with_options_async(request, runtime)

    def describe_device_validity_schema_with_options(
        self,
        request: iovcc_20180501_models.DescribeDeviceValiditySchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceValiditySchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceValiditySchemaResponse().from_map(
            self.do_rpcrequest('DescribeDeviceValiditySchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_device_validity_schema_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceValiditySchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeDeviceValiditySchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeDeviceValiditySchemaResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeviceValiditySchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_validity_schema(
        self,
        request: iovcc_20180501_models.DescribeDeviceValiditySchemaRequest,
    ) -> iovcc_20180501_models.DescribeDeviceValiditySchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_device_validity_schema_with_options(request, runtime)

    async def describe_device_validity_schema_async(
        self,
        request: iovcc_20180501_models.DescribeDeviceValiditySchemaRequest,
    ) -> iovcc_20180501_models.DescribeDeviceValiditySchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_validity_schema_with_options_async(request, runtime)

    def describe_message_with_options(
        self,
        request: iovcc_20180501_models.DescribeMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMessageResponse().from_map(
            self.do_rpcrequest('DescribeMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_message_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMessageResponse().from_map(
            await self.do_rpcrequest_async('DescribeMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_message(
        self,
        request: iovcc_20180501_models.DescribeMessageRequest,
    ) -> iovcc_20180501_models.DescribeMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_message_with_options(request, runtime)

    async def describe_message_async(
        self,
        request: iovcc_20180501_models.DescribeMessageRequest,
    ) -> iovcc_20180501_models.DescribeMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_message_with_options_async(request, runtime)

    def describe_mqtt_client_status_with_options(
        self,
        request: iovcc_20180501_models.DescribeMqttClientStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMqttClientStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMqttClientStatusResponse().from_map(
            self.do_rpcrequest('DescribeMqttClientStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mqtt_client_status_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeMqttClientStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMqttClientStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMqttClientStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeMqttClientStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mqtt_client_status(
        self,
        request: iovcc_20180501_models.DescribeMqttClientStatusRequest,
    ) -> iovcc_20180501_models.DescribeMqttClientStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mqtt_client_status_with_options(request, runtime)

    async def describe_mqtt_client_status_async(
        self,
        request: iovcc_20180501_models.DescribeMqttClientStatusRequest,
    ) -> iovcc_20180501_models.DescribeMqttClientStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mqtt_client_status_with_options_async(request, runtime)

    def describe_mqtt_message_with_options(
        self,
        request: iovcc_20180501_models.DescribeMqttMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMqttMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMqttMessageResponse().from_map(
            self.do_rpcrequest('DescribeMqttMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mqtt_message_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeMqttMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMqttMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMqttMessageResponse().from_map(
            await self.do_rpcrequest_async('DescribeMqttMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mqtt_message(
        self,
        request: iovcc_20180501_models.DescribeMqttMessageRequest,
    ) -> iovcc_20180501_models.DescribeMqttMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mqtt_message_with_options(request, runtime)

    async def describe_mqtt_message_async(
        self,
        request: iovcc_20180501_models.DescribeMqttMessageRequest,
    ) -> iovcc_20180501_models.DescribeMqttMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mqtt_message_with_options_async(request, runtime)

    def describe_mqtt_topic_subscription_with_options(
        self,
        request: iovcc_20180501_models.DescribeMqttTopicSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMqttTopicSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMqttTopicSubscriptionResponse().from_map(
            self.do_rpcrequest('DescribeMqttTopicSubscription', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mqtt_topic_subscription_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeMqttTopicSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeMqttTopicSubscriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeMqttTopicSubscriptionResponse().from_map(
            await self.do_rpcrequest_async('DescribeMqttTopicSubscription', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mqtt_topic_subscription(
        self,
        request: iovcc_20180501_models.DescribeMqttTopicSubscriptionRequest,
    ) -> iovcc_20180501_models.DescribeMqttTopicSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mqtt_topic_subscription_with_options(request, runtime)

    async def describe_mqtt_topic_subscription_async(
        self,
        request: iovcc_20180501_models.DescribeMqttTopicSubscriptionRequest,
    ) -> iovcc_20180501_models.DescribeMqttTopicSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mqtt_topic_subscription_with_options_async(request, runtime)

    def describe_open_account_with_options(
        self,
        request: iovcc_20180501_models.DescribeOpenAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeOpenAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeOpenAccountResponse().from_map(
            self.do_rpcrequest('DescribeOpenAccount', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_open_account_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeOpenAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeOpenAccountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.DescribeOpenAccountResponse().from_map(
            await self.do_rpcrequest_async('DescribeOpenAccount', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_open_account(
        self,
        request: iovcc_20180501_models.DescribeOpenAccountRequest,
    ) -> iovcc_20180501_models.DescribeOpenAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_open_account_with_options(request, runtime)

    async def describe_open_account_async(
        self,
        request: iovcc_20180501_models.DescribeOpenAccountRequest,
    ) -> iovcc_20180501_models.DescribeOpenAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_account_with_options_async(request, runtime)

    def describe_os_version_with_options(
        self,
        request: iovcc_20180501_models.DescribeOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeOsVersionResponse().from_map(
            self.do_rpcrequest('DescribeOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_os_version_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeOsVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_os_version(
        self,
        request: iovcc_20180501_models.DescribeOsVersionRequest,
    ) -> iovcc_20180501_models.DescribeOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_os_version_with_options(request, runtime)

    async def describe_os_version_async(
        self,
        request: iovcc_20180501_models.DescribeOsVersionRequest,
    ) -> iovcc_20180501_models.DescribeOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_os_version_with_options_async(request, runtime)

    def describe_project_with_options(
        self,
        request: iovcc_20180501_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeProjectResponse().from_map(
            self.do_rpcrequest('DescribeProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_project_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeProjectResponse().from_map(
            await self.do_rpcrequest_async('DescribeProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_project(
        self,
        request: iovcc_20180501_models.DescribeProjectRequest,
    ) -> iovcc_20180501_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_with_options(request, runtime)

    async def describe_project_async(
        self,
        request: iovcc_20180501_models.DescribeProjectRequest,
    ) -> iovcc_20180501_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_with_options_async(request, runtime)

    def describe_project_app_security_with_options(
        self,
        request: iovcc_20180501_models.DescribeProjectAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeProjectAppSecurityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeProjectAppSecurityResponse().from_map(
            self.do_rpcrequest('DescribeProjectAppSecurity', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_project_app_security_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeProjectAppSecurityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeProjectAppSecurityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeProjectAppSecurityResponse().from_map(
            await self.do_rpcrequest_async('DescribeProjectAppSecurity', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_project_app_security(
        self,
        request: iovcc_20180501_models.DescribeProjectAppSecurityRequest,
    ) -> iovcc_20180501_models.DescribeProjectAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_app_security_with_options(request, runtime)

    async def describe_project_app_security_async(
        self,
        request: iovcc_20180501_models.DescribeProjectAppSecurityRequest,
    ) -> iovcc_20180501_models.DescribeProjectAppSecurityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_app_security_with_options_async(request, runtime)

    def describe_shadow_schema_with_options(
        self,
        request: iovcc_20180501_models.DescribeShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeShadowSchemaResponse().from_map(
            self.do_rpcrequest('DescribeShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_shadow_schema_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeShadowSchemaResponse().from_map(
            await self.do_rpcrequest_async('DescribeShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_shadow_schema(
        self,
        request: iovcc_20180501_models.DescribeShadowSchemaRequest,
    ) -> iovcc_20180501_models.DescribeShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shadow_schema_with_options(request, runtime)

    async def describe_shadow_schema_async(
        self,
        request: iovcc_20180501_models.DescribeShadowSchemaRequest,
    ) -> iovcc_20180501_models.DescribeShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shadow_schema_with_options_async(request, runtime)

    def describe_version_device_group_with_options(
        self,
        request: iovcc_20180501_models.DescribeVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeVersionDeviceGroupResponse().from_map(
            self.do_rpcrequest('DescribeVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_version_device_group_with_options_async(
        self,
        request: iovcc_20180501_models.DescribeVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DescribeVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DescribeVersionDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_version_device_group(
        self,
        request: iovcc_20180501_models.DescribeVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.DescribeVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_version_device_group_with_options(request, runtime)

    async def describe_version_device_group_async(
        self,
        request: iovcc_20180501_models.DescribeVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.DescribeVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_version_device_group_with_options_async(request, runtime)

    def diagnosis_version_with_options(
        self,
        request: iovcc_20180501_models.DiagnosisVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DiagnosisVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DiagnosisVersionResponse().from_map(
            self.do_rpcrequest('DiagnosisVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def diagnosis_version_with_options_async(
        self,
        request: iovcc_20180501_models.DiagnosisVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.DiagnosisVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.DiagnosisVersionResponse().from_map(
            await self.do_rpcrequest_async('DiagnosisVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def diagnosis_version(
        self,
        request: iovcc_20180501_models.DiagnosisVersionRequest,
    ) -> iovcc_20180501_models.DiagnosisVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.diagnosis_version_with_options(request, runtime)

    async def diagnosis_version_async(
        self,
        request: iovcc_20180501_models.DiagnosisVersionRequest,
    ) -> iovcc_20180501_models.DiagnosisVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.diagnosis_version_with_options_async(request, runtime)

    def find_app_versions_with_options(
        self,
        request: iovcc_20180501_models.FindAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindAppVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindAppVersionsResponse().from_map(
            self.do_rpcrequest('FindAppVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_app_versions_with_options_async(
        self,
        request: iovcc_20180501_models.FindAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindAppVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindAppVersionsResponse().from_map(
            await self.do_rpcrequest_async('FindAppVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_app_versions(
        self,
        request: iovcc_20180501_models.FindAppVersionsRequest,
    ) -> iovcc_20180501_models.FindAppVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_app_versions_with_options(request, runtime)

    async def find_app_versions_async(
        self,
        request: iovcc_20180501_models.FindAppVersionsRequest,
    ) -> iovcc_20180501_models.FindAppVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_app_versions_with_options_async(request, runtime)

    def find_customized_filters_with_options(
        self,
        request: iovcc_20180501_models.FindCustomizedFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindCustomizedFiltersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindCustomizedFiltersResponse().from_map(
            self.do_rpcrequest('FindCustomizedFilters', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_customized_filters_with_options_async(
        self,
        request: iovcc_20180501_models.FindCustomizedFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindCustomizedFiltersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindCustomizedFiltersResponse().from_map(
            await self.do_rpcrequest_async('FindCustomizedFilters', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_customized_filters(
        self,
        request: iovcc_20180501_models.FindCustomizedFiltersRequest,
    ) -> iovcc_20180501_models.FindCustomizedFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_customized_filters_with_options(request, runtime)

    async def find_customized_filters_async(
        self,
        request: iovcc_20180501_models.FindCustomizedFiltersRequest,
    ) -> iovcc_20180501_models.FindCustomizedFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_customized_filters_with_options_async(request, runtime)

    def find_customized_properties_with_options(
        self,
        request: iovcc_20180501_models.FindCustomizedPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindCustomizedPropertiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindCustomizedPropertiesResponse().from_map(
            self.do_rpcrequest('FindCustomizedProperties', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_customized_properties_with_options_async(
        self,
        request: iovcc_20180501_models.FindCustomizedPropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindCustomizedPropertiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindCustomizedPropertiesResponse().from_map(
            await self.do_rpcrequest_async('FindCustomizedProperties', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_customized_properties(
        self,
        request: iovcc_20180501_models.FindCustomizedPropertiesRequest,
    ) -> iovcc_20180501_models.FindCustomizedPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_customized_properties_with_options(request, runtime)

    async def find_customized_properties_async(
        self,
        request: iovcc_20180501_models.FindCustomizedPropertiesRequest,
    ) -> iovcc_20180501_models.FindCustomizedPropertiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_customized_properties_with_options_async(request, runtime)

    def find_os_versions_with_options(
        self,
        request: iovcc_20180501_models.FindOsVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindOsVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindOsVersionsResponse().from_map(
            self.do_rpcrequest('FindOsVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_os_versions_with_options_async(
        self,
        request: iovcc_20180501_models.FindOsVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindOsVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindOsVersionsResponse().from_map(
            await self.do_rpcrequest_async('FindOsVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_os_versions(
        self,
        request: iovcc_20180501_models.FindOsVersionsRequest,
    ) -> iovcc_20180501_models.FindOsVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_os_versions_with_options(request, runtime)

    async def find_os_versions_async(
        self,
        request: iovcc_20180501_models.FindOsVersionsRequest,
    ) -> iovcc_20180501_models.FindOsVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_os_versions_with_options_async(request, runtime)

    def find_prepublishes_by_parent_id_with_options(
        self,
        request: iovcc_20180501_models.FindPrepublishesByParentIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindPrepublishesByParentIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindPrepublishesByParentIdResponse().from_map(
            self.do_rpcrequest('FindPrepublishesByParentId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_prepublishes_by_parent_id_with_options_async(
        self,
        request: iovcc_20180501_models.FindPrepublishesByParentIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindPrepublishesByParentIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindPrepublishesByParentIdResponse().from_map(
            await self.do_rpcrequest_async('FindPrepublishesByParentId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_prepublishes_by_parent_id(
        self,
        request: iovcc_20180501_models.FindPrepublishesByParentIdRequest,
    ) -> iovcc_20180501_models.FindPrepublishesByParentIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_prepublishes_by_parent_id_with_options(request, runtime)

    async def find_prepublishes_by_parent_id_async(
        self,
        request: iovcc_20180501_models.FindPrepublishesByParentIdRequest,
    ) -> iovcc_20180501_models.FindPrepublishesByParentIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_prepublishes_by_parent_id_with_options_async(request, runtime)

    def find_prepublishes_by_version_id_with_options(
        self,
        request: iovcc_20180501_models.FindPrepublishesByVersionIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindPrepublishesByVersionIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindPrepublishesByVersionIdResponse().from_map(
            self.do_rpcrequest('FindPrepublishesByVersionId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_prepublishes_by_version_id_with_options_async(
        self,
        request: iovcc_20180501_models.FindPrepublishesByVersionIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindPrepublishesByVersionIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindPrepublishesByVersionIdResponse().from_map(
            await self.do_rpcrequest_async('FindPrepublishesByVersionId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_prepublishes_by_version_id(
        self,
        request: iovcc_20180501_models.FindPrepublishesByVersionIdRequest,
    ) -> iovcc_20180501_models.FindPrepublishesByVersionIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_prepublishes_by_version_id_with_options(request, runtime)

    async def find_prepublishes_by_version_id_async(
        self,
        request: iovcc_20180501_models.FindPrepublishesByVersionIdRequest,
    ) -> iovcc_20180501_models.FindPrepublishesByVersionIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_prepublishes_by_version_id_with_options_async(request, runtime)

    def find_prepublish_passed_devices_with_options(
        self,
        request: iovcc_20180501_models.FindPrepublishPassedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindPrepublishPassedDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindPrepublishPassedDevicesResponse().from_map(
            self.do_rpcrequest('FindPrepublishPassedDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_prepublish_passed_devices_with_options_async(
        self,
        request: iovcc_20180501_models.FindPrepublishPassedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindPrepublishPassedDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindPrepublishPassedDevicesResponse().from_map(
            await self.do_rpcrequest_async('FindPrepublishPassedDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_prepublish_passed_devices(
        self,
        request: iovcc_20180501_models.FindPrepublishPassedDevicesRequest,
    ) -> iovcc_20180501_models.FindPrepublishPassedDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_prepublish_passed_devices_with_options(request, runtime)

    async def find_prepublish_passed_devices_async(
        self,
        request: iovcc_20180501_models.FindPrepublishPassedDevicesRequest,
    ) -> iovcc_20180501_models.FindPrepublishPassedDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_prepublish_passed_devices_with_options_async(request, runtime)

    def find_version_black_devices_with_options(
        self,
        request: iovcc_20180501_models.FindVersionBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionBlackDevicesResponse().from_map(
            self.do_rpcrequest('FindVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_version_black_devices_with_options_async(
        self,
        request: iovcc_20180501_models.FindVersionBlackDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionBlackDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionBlackDevicesResponse().from_map(
            await self.do_rpcrequest_async('FindVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_black_devices(
        self,
        request: iovcc_20180501_models.FindVersionBlackDevicesRequest,
    ) -> iovcc_20180501_models.FindVersionBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_version_black_devices_with_options(request, runtime)

    async def find_version_black_devices_async(
        self,
        request: iovcc_20180501_models.FindVersionBlackDevicesRequest,
    ) -> iovcc_20180501_models.FindVersionBlackDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_version_black_devices_with_options_async(request, runtime)

    def find_version_device_groups_with_options(
        self,
        request: iovcc_20180501_models.FindVersionDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionDeviceGroupsResponse().from_map(
            self.do_rpcrequest('FindVersionDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_version_device_groups_with_options_async(
        self,
        request: iovcc_20180501_models.FindVersionDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionDeviceGroupsResponse().from_map(
            await self.do_rpcrequest_async('FindVersionDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_device_groups(
        self,
        request: iovcc_20180501_models.FindVersionDeviceGroupsRequest,
    ) -> iovcc_20180501_models.FindVersionDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_version_device_groups_with_options(request, runtime)

    async def find_version_device_groups_async(
        self,
        request: iovcc_20180501_models.FindVersionDeviceGroupsRequest,
    ) -> iovcc_20180501_models.FindVersionDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_version_device_groups_with_options_async(request, runtime)

    def find_version_group_devices_with_options(
        self,
        request: iovcc_20180501_models.FindVersionGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionGroupDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionGroupDevicesResponse().from_map(
            self.do_rpcrequest('FindVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_version_group_devices_with_options_async(
        self,
        request: iovcc_20180501_models.FindVersionGroupDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionGroupDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionGroupDevicesResponse().from_map(
            await self.do_rpcrequest_async('FindVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_group_devices(
        self,
        request: iovcc_20180501_models.FindVersionGroupDevicesRequest,
    ) -> iovcc_20180501_models.FindVersionGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_version_group_devices_with_options(request, runtime)

    async def find_version_group_devices_async(
        self,
        request: iovcc_20180501_models.FindVersionGroupDevicesRequest,
    ) -> iovcc_20180501_models.FindVersionGroupDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_version_group_devices_with_options_async(request, runtime)

    def find_version_messages_with_options(
        self,
        request: iovcc_20180501_models.FindVersionMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionMessagesResponse().from_map(
            self.do_rpcrequest('FindVersionMessages', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_version_messages_with_options_async(
        self,
        request: iovcc_20180501_models.FindVersionMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionMessagesResponse().from_map(
            await self.do_rpcrequest_async('FindVersionMessages', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_messages(
        self,
        request: iovcc_20180501_models.FindVersionMessagesRequest,
    ) -> iovcc_20180501_models.FindVersionMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_version_messages_with_options(request, runtime)

    async def find_version_messages_async(
        self,
        request: iovcc_20180501_models.FindVersionMessagesRequest,
    ) -> iovcc_20180501_models.FindVersionMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_version_messages_with_options_async(request, runtime)

    def find_version_message_send_records_with_options(
        self,
        request: iovcc_20180501_models.FindVersionMessageSendRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionMessageSendRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionMessageSendRecordsResponse().from_map(
            self.do_rpcrequest('FindVersionMessageSendRecords', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_version_message_send_records_with_options_async(
        self,
        request: iovcc_20180501_models.FindVersionMessageSendRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionMessageSendRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionMessageSendRecordsResponse().from_map(
            await self.do_rpcrequest_async('FindVersionMessageSendRecords', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_message_send_records(
        self,
        request: iovcc_20180501_models.FindVersionMessageSendRecordsRequest,
    ) -> iovcc_20180501_models.FindVersionMessageSendRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_version_message_send_records_with_options(request, runtime)

    async def find_version_message_send_records_async(
        self,
        request: iovcc_20180501_models.FindVersionMessageSendRecordsRequest,
    ) -> iovcc_20180501_models.FindVersionMessageSendRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_version_message_send_records_with_options_async(request, runtime)

    def find_version_tests_with_options(
        self,
        request: iovcc_20180501_models.FindVersionTestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionTestsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionTestsResponse().from_map(
            self.do_rpcrequest('FindVersionTests', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_version_tests_with_options_async(
        self,
        request: iovcc_20180501_models.FindVersionTestsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionTestsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionTestsResponse().from_map(
            await self.do_rpcrequest_async('FindVersionTests', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_tests(
        self,
        request: iovcc_20180501_models.FindVersionTestsRequest,
    ) -> iovcc_20180501_models.FindVersionTestsResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_version_tests_with_options(request, runtime)

    async def find_version_tests_async(
        self,
        request: iovcc_20180501_models.FindVersionTestsRequest,
    ) -> iovcc_20180501_models.FindVersionTestsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_version_tests_with_options_async(request, runtime)

    def find_version_white_devices_with_options(
        self,
        request: iovcc_20180501_models.FindVersionWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionWhiteDevicesResponse().from_map(
            self.do_rpcrequest('FindVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_version_white_devices_with_options_async(
        self,
        request: iovcc_20180501_models.FindVersionWhiteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.FindVersionWhiteDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.FindVersionWhiteDevicesResponse().from_map(
            await self.do_rpcrequest_async('FindVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_white_devices(
        self,
        request: iovcc_20180501_models.FindVersionWhiteDevicesRequest,
    ) -> iovcc_20180501_models.FindVersionWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_version_white_devices_with_options(request, runtime)

    async def find_version_white_devices_async(
        self,
        request: iovcc_20180501_models.FindVersionWhiteDevicesRequest,
    ) -> iovcc_20180501_models.FindVersionWhiteDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_version_white_devices_with_options_async(request, runtime)

    def generate_assist_file_upload_url_with_options(
        self,
        request: iovcc_20180501_models.GenerateAssistFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateAssistFileUploadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateAssistFileUploadUrlResponse().from_map(
            self.do_rpcrequest('GenerateAssistFileUploadUrl', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_assist_file_upload_url_with_options_async(
        self,
        request: iovcc_20180501_models.GenerateAssistFileUploadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateAssistFileUploadUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateAssistFileUploadUrlResponse().from_map(
            await self.do_rpcrequest_async('GenerateAssistFileUploadUrl', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_assist_file_upload_url(
        self,
        request: iovcc_20180501_models.GenerateAssistFileUploadUrlRequest,
    ) -> iovcc_20180501_models.GenerateAssistFileUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_assist_file_upload_url_with_options(request, runtime)

    async def generate_assist_file_upload_url_async(
        self,
        request: iovcc_20180501_models.GenerateAssistFileUploadUrlRequest,
    ) -> iovcc_20180501_models.GenerateAssistFileUploadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_assist_file_upload_url_with_options_async(request, runtime)

    def generate_function_file_upload_meta_with_options(
        self,
        request: iovcc_20180501_models.GenerateFunctionFileUploadMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateFunctionFileUploadMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateFunctionFileUploadMetaResponse().from_map(
            self.do_rpcrequest('GenerateFunctionFileUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_function_file_upload_meta_with_options_async(
        self,
        request: iovcc_20180501_models.GenerateFunctionFileUploadMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateFunctionFileUploadMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateFunctionFileUploadMetaResponse().from_map(
            await self.do_rpcrequest_async('GenerateFunctionFileUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_function_file_upload_meta(
        self,
        request: iovcc_20180501_models.GenerateFunctionFileUploadMetaRequest,
    ) -> iovcc_20180501_models.GenerateFunctionFileUploadMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_function_file_upload_meta_with_options(request, runtime)

    async def generate_function_file_upload_meta_async(
        self,
        request: iovcc_20180501_models.GenerateFunctionFileUploadMetaRequest,
    ) -> iovcc_20180501_models.GenerateFunctionFileUploadMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_function_file_upload_meta_with_options_async(request, runtime)

    def generate_oss_post_policy_with_options(
        self,
        request: iovcc_20180501_models.GenerateOssPostPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateOssPostPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateOssPostPolicyResponse().from_map(
            self.do_rpcrequest('GenerateOssPostPolicy', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_oss_post_policy_with_options_async(
        self,
        request: iovcc_20180501_models.GenerateOssPostPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateOssPostPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateOssPostPolicyResponse().from_map(
            await self.do_rpcrequest_async('GenerateOssPostPolicy', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_oss_post_policy(
        self,
        request: iovcc_20180501_models.GenerateOssPostPolicyRequest,
    ) -> iovcc_20180501_models.GenerateOssPostPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_oss_post_policy_with_options(request, runtime)

    async def generate_oss_post_policy_async(
        self,
        request: iovcc_20180501_models.GenerateOssPostPolicyRequest,
    ) -> iovcc_20180501_models.GenerateOssPostPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_oss_post_policy_with_options_async(request, runtime)

    def generate_oss_upload_meta_with_options(
        self,
        request: iovcc_20180501_models.GenerateOssUploadMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateOssUploadMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateOssUploadMetaResponse().from_map(
            self.do_rpcrequest('GenerateOssUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_oss_upload_meta_with_options_async(
        self,
        request: iovcc_20180501_models.GenerateOssUploadMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateOssUploadMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateOssUploadMetaResponse().from_map(
            await self.do_rpcrequest_async('GenerateOssUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_oss_upload_meta(
        self,
        request: iovcc_20180501_models.GenerateOssUploadMetaRequest,
    ) -> iovcc_20180501_models.GenerateOssUploadMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_oss_upload_meta_with_options(request, runtime)

    async def generate_oss_upload_meta_async(
        self,
        request: iovcc_20180501_models.GenerateOssUploadMetaRequest,
    ) -> iovcc_20180501_models.GenerateOssUploadMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_oss_upload_meta_with_options_async(request, runtime)

    def generate_sdk_download_info_with_options(
        self,
        request: iovcc_20180501_models.GenerateSdkDownloadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateSdkDownloadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateSdkDownloadInfoResponse().from_map(
            self.do_rpcrequest('GenerateSdkDownloadInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_sdk_download_info_with_options_async(
        self,
        request: iovcc_20180501_models.GenerateSdkDownloadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateSdkDownloadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateSdkDownloadInfoResponse().from_map(
            await self.do_rpcrequest_async('GenerateSdkDownloadInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_sdk_download_info(
        self,
        request: iovcc_20180501_models.GenerateSdkDownloadInfoRequest,
    ) -> iovcc_20180501_models.GenerateSdkDownloadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_sdk_download_info_with_options(request, runtime)

    async def generate_sdk_download_info_async(
        self,
        request: iovcc_20180501_models.GenerateSdkDownloadInfoRequest,
    ) -> iovcc_20180501_models.GenerateSdkDownloadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_sdk_download_info_with_options_async(request, runtime)

    def generate_sys_app_download_info_with_options(
        self,
        request: iovcc_20180501_models.GenerateSysAppDownloadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateSysAppDownloadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateSysAppDownloadInfoResponse().from_map(
            self.do_rpcrequest('GenerateSysAppDownloadInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_sys_app_download_info_with_options_async(
        self,
        request: iovcc_20180501_models.GenerateSysAppDownloadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GenerateSysAppDownloadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GenerateSysAppDownloadInfoResponse().from_map(
            await self.do_rpcrequest_async('GenerateSysAppDownloadInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_sys_app_download_info(
        self,
        request: iovcc_20180501_models.GenerateSysAppDownloadInfoRequest,
    ) -> iovcc_20180501_models.GenerateSysAppDownloadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_sys_app_download_info_with_options(request, runtime)

    async def generate_sys_app_download_info_async(
        self,
        request: iovcc_20180501_models.GenerateSysAppDownloadInfoRequest,
    ) -> iovcc_20180501_models.GenerateSysAppDownloadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_sys_app_download_info_with_options_async(request, runtime)

    def get_device_app_update_funnel_events_with_options(
        self,
        request: iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsResponse().from_map(
            self.do_rpcrequest('GetDeviceAppUpdateFunnelEvents', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_app_update_funnel_events_with_options_async(
        self,
        request: iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsResponse().from_map(
            await self.do_rpcrequest_async('GetDeviceAppUpdateFunnelEvents', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_app_update_funnel_events(
        self,
        request: iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsRequest,
    ) -> iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_app_update_funnel_events_with_options(request, runtime)

    async def get_device_app_update_funnel_events_async(
        self,
        request: iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsRequest,
    ) -> iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_app_update_funnel_events_with_options_async(request, runtime)

    def get_device_system_update_funnel_events_with_options(
        self,
        request: iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsResponse().from_map(
            self.do_rpcrequest('GetDeviceSystemUpdateFunnelEvents', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_system_update_funnel_events_with_options_async(
        self,
        request: iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsResponse().from_map(
            await self.do_rpcrequest_async('GetDeviceSystemUpdateFunnelEvents', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_system_update_funnel_events(
        self,
        request: iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsRequest,
    ) -> iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_system_update_funnel_events_with_options(request, runtime)

    async def get_device_system_update_funnel_events_async(
        self,
        request: iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsRequest,
    ) -> iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_system_update_funnel_events_with_options_async(request, runtime)

    def get_namespace_data_with_options(
        self,
        request: iovcc_20180501_models.GetNamespaceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetNamespaceDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetNamespaceDataResponse().from_map(
            self.do_rpcrequest('GetNamespaceData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_namespace_data_with_options_async(
        self,
        request: iovcc_20180501_models.GetNamespaceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetNamespaceDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetNamespaceDataResponse().from_map(
            await self.do_rpcrequest_async('GetNamespaceData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_namespace_data(
        self,
        request: iovcc_20180501_models.GetNamespaceDataRequest,
    ) -> iovcc_20180501_models.GetNamespaceDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_namespace_data_with_options(request, runtime)

    async def get_namespace_data_async(
        self,
        request: iovcc_20180501_models.GetNamespaceDataRequest,
    ) -> iovcc_20180501_models.GetNamespaceDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_namespace_data_with_options_async(request, runtime)

    def get_namespace_statistics_data_with_options(
        self,
        request: iovcc_20180501_models.GetNamespaceStatisticsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetNamespaceStatisticsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetNamespaceStatisticsDataResponse().from_map(
            self.do_rpcrequest('GetNamespaceStatisticsData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_namespace_statistics_data_with_options_async(
        self,
        request: iovcc_20180501_models.GetNamespaceStatisticsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetNamespaceStatisticsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetNamespaceStatisticsDataResponse().from_map(
            await self.do_rpcrequest_async('GetNamespaceStatisticsData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_namespace_statistics_data(
        self,
        request: iovcc_20180501_models.GetNamespaceStatisticsDataRequest,
    ) -> iovcc_20180501_models.GetNamespaceStatisticsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_namespace_statistics_data_with_options(request, runtime)

    async def get_namespace_statistics_data_async(
        self,
        request: iovcc_20180501_models.GetNamespaceStatisticsDataRequest,
    ) -> iovcc_20180501_models.GetNamespaceStatisticsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_namespace_statistics_data_with_options_async(request, runtime)

    def get_oss_upload_meta_with_options(
        self,
        request: iovcc_20180501_models.GetOssUploadMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetOssUploadMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetOssUploadMetaResponse().from_map(
            self.do_rpcrequest('GetOssUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_oss_upload_meta_with_options_async(
        self,
        request: iovcc_20180501_models.GetOssUploadMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.GetOssUploadMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.GetOssUploadMetaResponse().from_map(
            await self.do_rpcrequest_async('GetOssUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_oss_upload_meta(
        self,
        request: iovcc_20180501_models.GetOssUploadMetaRequest,
    ) -> iovcc_20180501_models.GetOssUploadMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_oss_upload_meta_with_options(request, runtime)

    async def get_oss_upload_meta_async(
        self,
        request: iovcc_20180501_models.GetOssUploadMetaRequest,
    ) -> iovcc_20180501_models.GetOssUploadMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_upload_meta_with_options_async(request, runtime)

    def invoke_function_with_options(
        self,
        request: iovcc_20180501_models.InvokeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.InvokeFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.InvokeFunctionResponse().from_map(
            self.do_rpcrequest('InvokeFunction', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_function_with_options_async(
        self,
        request: iovcc_20180501_models.InvokeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.InvokeFunctionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.InvokeFunctionResponse().from_map(
            await self.do_rpcrequest_async('InvokeFunction', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_function(
        self,
        request: iovcc_20180501_models.InvokeFunctionRequest,
    ) -> iovcc_20180501_models.InvokeFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_function_with_options(request, runtime)

    async def invoke_function_async(
        self,
        request: iovcc_20180501_models.InvokeFunctionRequest,
    ) -> iovcc_20180501_models.InvokeFunctionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_function_with_options_async(request, runtime)

    def list_api_gateway_apps_with_options(
        self,
        request: iovcc_20180501_models.ListApiGatewayAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListApiGatewayAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListApiGatewayAppsResponse().from_map(
            self.do_rpcrequest('ListApiGatewayApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_api_gateway_apps_with_options_async(
        self,
        request: iovcc_20180501_models.ListApiGatewayAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListApiGatewayAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListApiGatewayAppsResponse().from_map(
            await self.do_rpcrequest_async('ListApiGatewayApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_api_gateway_apps(
        self,
        request: iovcc_20180501_models.ListApiGatewayAppsRequest,
    ) -> iovcc_20180501_models.ListApiGatewayAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_api_gateway_apps_with_options(request, runtime)

    async def list_api_gateway_apps_async(
        self,
        request: iovcc_20180501_models.ListApiGatewayAppsRequest,
    ) -> iovcc_20180501_models.ListApiGatewayAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_api_gateway_apps_with_options_async(request, runtime)

    def list_apps_with_options(
        self,
        request: iovcc_20180501_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListAppsResponse().from_map(
            self.do_rpcrequest('ListApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: iovcc_20180501_models.ListAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListAppsResponse().from_map(
            await self.do_rpcrequest_async('ListApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apps(
        self,
        request: iovcc_20180501_models.ListAppsRequest,
    ) -> iovcc_20180501_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    async def list_apps_async(
        self,
        request: iovcc_20180501_models.ListAppsRequest,
    ) -> iovcc_20180501_models.ListAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apps_with_options_async(request, runtime)

    def list_assist_action_details_with_options(
        self,
        request: iovcc_20180501_models.ListAssistActionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistActionDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistActionDetailsResponse().from_map(
            self.do_rpcrequest('ListAssistActionDetails', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_assist_action_details_with_options_async(
        self,
        request: iovcc_20180501_models.ListAssistActionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistActionDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistActionDetailsResponse().from_map(
            await self.do_rpcrequest_async('ListAssistActionDetails', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_action_details(
        self,
        request: iovcc_20180501_models.ListAssistActionDetailsRequest,
    ) -> iovcc_20180501_models.ListAssistActionDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_assist_action_details_with_options(request, runtime)

    async def list_assist_action_details_async(
        self,
        request: iovcc_20180501_models.ListAssistActionDetailsRequest,
    ) -> iovcc_20180501_models.ListAssistActionDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_assist_action_details_with_options_async(request, runtime)

    def list_assist_devices_with_options(
        self,
        request: iovcc_20180501_models.ListAssistDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistDevicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistDevicesResponse().from_map(
            self.do_rpcrequest('ListAssistDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_assist_devices_with_options_async(
        self,
        request: iovcc_20180501_models.ListAssistDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistDevicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistDevicesResponse().from_map(
            await self.do_rpcrequest_async('ListAssistDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_devices(
        self,
        request: iovcc_20180501_models.ListAssistDevicesRequest,
    ) -> iovcc_20180501_models.ListAssistDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_assist_devices_with_options(request, runtime)

    async def list_assist_devices_async(
        self,
        request: iovcc_20180501_models.ListAssistDevicesRequest,
    ) -> iovcc_20180501_models.ListAssistDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_assist_devices_with_options_async(request, runtime)

    def list_assist_histories_with_options(
        self,
        request: iovcc_20180501_models.ListAssistHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistHistoriesResponse().from_map(
            self.do_rpcrequest('ListAssistHistories', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_assist_histories_with_options_async(
        self,
        request: iovcc_20180501_models.ListAssistHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistHistoriesResponse().from_map(
            await self.do_rpcrequest_async('ListAssistHistories', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_histories(
        self,
        request: iovcc_20180501_models.ListAssistHistoriesRequest,
    ) -> iovcc_20180501_models.ListAssistHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_assist_histories_with_options(request, runtime)

    async def list_assist_histories_async(
        self,
        request: iovcc_20180501_models.ListAssistHistoriesRequest,
    ) -> iovcc_20180501_models.ListAssistHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_assist_histories_with_options_async(request, runtime)

    def list_assist_history_details_with_options(
        self,
        request: iovcc_20180501_models.ListAssistHistoryDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistHistoryDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistHistoryDetailsResponse().from_map(
            self.do_rpcrequest('ListAssistHistoryDetails', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_assist_history_details_with_options_async(
        self,
        request: iovcc_20180501_models.ListAssistHistoryDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListAssistHistoryDetailsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListAssistHistoryDetailsResponse().from_map(
            await self.do_rpcrequest_async('ListAssistHistoryDetails', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_history_details(
        self,
        request: iovcc_20180501_models.ListAssistHistoryDetailsRequest,
    ) -> iovcc_20180501_models.ListAssistHistoryDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_assist_history_details_with_options(request, runtime)

    async def list_assist_history_details_async(
        self,
        request: iovcc_20180501_models.ListAssistHistoryDetailsRequest,
    ) -> iovcc_20180501_models.ListAssistHistoryDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_assist_history_details_with_options_async(request, runtime)

    def list_client_plugins_with_options(
        self,
        request: iovcc_20180501_models.ListClientPluginsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListClientPluginsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListClientPluginsResponse().from_map(
            self.do_rpcrequest('ListClientPlugins', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_client_plugins_with_options_async(
        self,
        request: iovcc_20180501_models.ListClientPluginsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListClientPluginsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListClientPluginsResponse().from_map(
            await self.do_rpcrequest_async('ListClientPlugins', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_client_plugins(
        self,
        request: iovcc_20180501_models.ListClientPluginsRequest,
    ) -> iovcc_20180501_models.ListClientPluginsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_client_plugins_with_options(request, runtime)

    async def list_client_plugins_async(
        self,
        request: iovcc_20180501_models.ListClientPluginsRequest,
    ) -> iovcc_20180501_models.ListClientPluginsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_client_plugins_with_options_async(request, runtime)

    def list_client_plugin_versions_with_options(
        self,
        request: iovcc_20180501_models.ListClientPluginVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListClientPluginVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListClientPluginVersionsResponse().from_map(
            self.do_rpcrequest('ListClientPluginVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_client_plugin_versions_with_options_async(
        self,
        request: iovcc_20180501_models.ListClientPluginVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListClientPluginVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListClientPluginVersionsResponse().from_map(
            await self.do_rpcrequest_async('ListClientPluginVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_client_plugin_versions(
        self,
        request: iovcc_20180501_models.ListClientPluginVersionsRequest,
    ) -> iovcc_20180501_models.ListClientPluginVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_client_plugin_versions_with_options(request, runtime)

    async def list_client_plugin_versions_async(
        self,
        request: iovcc_20180501_models.ListClientPluginVersionsRequest,
    ) -> iovcc_20180501_models.ListClientPluginVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_client_plugin_versions_with_options_async(request, runtime)

    def list_client_sdks_with_options(
        self,
        request: iovcc_20180501_models.ListClientSdksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListClientSdksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListClientSdksResponse().from_map(
            self.do_rpcrequest('ListClientSdks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_client_sdks_with_options_async(
        self,
        request: iovcc_20180501_models.ListClientSdksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListClientSdksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListClientSdksResponse().from_map(
            await self.do_rpcrequest_async('ListClientSdks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_client_sdks(
        self,
        request: iovcc_20180501_models.ListClientSdksRequest,
    ) -> iovcc_20180501_models.ListClientSdksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_client_sdks_with_options(request, runtime)

    async def list_client_sdks_async(
        self,
        request: iovcc_20180501_models.ListClientSdksRequest,
    ) -> iovcc_20180501_models.ListClientSdksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_client_sdks_with_options_async(request, runtime)

    def list_connect_logs_with_options(
        self,
        request: iovcc_20180501_models.ListConnectLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListConnectLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListConnectLogsResponse().from_map(
            self.do_rpcrequest('ListConnectLogs', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_connect_logs_with_options_async(
        self,
        request: iovcc_20180501_models.ListConnectLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListConnectLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListConnectLogsResponse().from_map(
            await self.do_rpcrequest_async('ListConnectLogs', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_connect_logs(
        self,
        request: iovcc_20180501_models.ListConnectLogsRequest,
    ) -> iovcc_20180501_models.ListConnectLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connect_logs_with_options(request, runtime)

    async def list_connect_logs_async(
        self,
        request: iovcc_20180501_models.ListConnectLogsRequest,
    ) -> iovcc_20180501_models.ListConnectLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connect_logs_with_options_async(request, runtime)

    def list_deployed_functions_with_options(
        self,
        request: iovcc_20180501_models.ListDeployedFunctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeployedFunctionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListDeployedFunctionsResponse().from_map(
            self.do_rpcrequest('ListDeployedFunctions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_deployed_functions_with_options_async(
        self,
        request: iovcc_20180501_models.ListDeployedFunctionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeployedFunctionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListDeployedFunctionsResponse().from_map(
            await self.do_rpcrequest_async('ListDeployedFunctions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_deployed_functions(
        self,
        request: iovcc_20180501_models.ListDeployedFunctionsRequest,
    ) -> iovcc_20180501_models.ListDeployedFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_deployed_functions_with_options(request, runtime)

    async def list_deployed_functions_async(
        self,
        request: iovcc_20180501_models.ListDeployedFunctionsRequest,
    ) -> iovcc_20180501_models.ListDeployedFunctionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_deployed_functions_with_options_async(request, runtime)

    def list_device_brands_with_options(
        self,
        request: iovcc_20180501_models.ListDeviceBrandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceBrandsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceBrandsResponse().from_map(
            self.do_rpcrequest('ListDeviceBrands', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_brands_with_options_async(
        self,
        request: iovcc_20180501_models.ListDeviceBrandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceBrandsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceBrandsResponse().from_map(
            await self.do_rpcrequest_async('ListDeviceBrands', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_brands(
        self,
        request: iovcc_20180501_models.ListDeviceBrandsRequest,
    ) -> iovcc_20180501_models.ListDeviceBrandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_brands_with_options(request, runtime)

    async def list_device_brands_async(
        self,
        request: iovcc_20180501_models.ListDeviceBrandsRequest,
    ) -> iovcc_20180501_models.ListDeviceBrandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_brands_with_options_async(request, runtime)

    def list_device_model_with_options(
        self,
        request: iovcc_20180501_models.ListDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceModelResponse().from_map(
            self.do_rpcrequest('ListDeviceModel', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_model_with_options_async(
        self,
        request: iovcc_20180501_models.ListDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceModelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceModelResponse().from_map(
            await self.do_rpcrequest_async('ListDeviceModel', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_model(
        self,
        request: iovcc_20180501_models.ListDeviceModelRequest,
    ) -> iovcc_20180501_models.ListDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_model_with_options(request, runtime)

    async def list_device_model_async(
        self,
        request: iovcc_20180501_models.ListDeviceModelRequest,
    ) -> iovcc_20180501_models.ListDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_model_with_options_async(request, runtime)

    def list_device_models_with_options(
        self,
        request: iovcc_20180501_models.ListDeviceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceModelsResponse().from_map(
            self.do_rpcrequest('ListDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_models_with_options_async(
        self,
        request: iovcc_20180501_models.ListDeviceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceModelsResponse().from_map(
            await self.do_rpcrequest_async('ListDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_models(
        self,
        request: iovcc_20180501_models.ListDeviceModelsRequest,
    ) -> iovcc_20180501_models.ListDeviceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_models_with_options(request, runtime)

    async def list_device_models_async(
        self,
        request: iovcc_20180501_models.ListDeviceModelsRequest,
    ) -> iovcc_20180501_models.ListDeviceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_models_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: iovcc_20180501_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDevicesResponse().from_map(
            self.do_rpcrequest('ListDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: iovcc_20180501_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDevicesResponse().from_map(
            await self.do_rpcrequest_async('ListDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_devices(
        self,
        request: iovcc_20180501_models.ListDevicesRequest,
    ) -> iovcc_20180501_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: iovcc_20180501_models.ListDevicesRequest,
    ) -> iovcc_20180501_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def list_device_types_with_options(
        self,
        request: iovcc_20180501_models.ListDeviceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceTypesResponse().from_map(
            self.do_rpcrequest('ListDeviceTypes', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_device_types_with_options_async(
        self,
        request: iovcc_20180501_models.ListDeviceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListDeviceTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListDeviceTypesResponse().from_map(
            await self.do_rpcrequest_async('ListDeviceTypes', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_types(
        self,
        request: iovcc_20180501_models.ListDeviceTypesRequest,
    ) -> iovcc_20180501_models.ListDeviceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_types_with_options(request, runtime)

    async def list_device_types_async(
        self,
        request: iovcc_20180501_models.ListDeviceTypesRequest,
    ) -> iovcc_20180501_models.ListDeviceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_types_with_options_async(request, runtime)

    def list_function_execute_log_with_options(
        self,
        request: iovcc_20180501_models.ListFunctionExecuteLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListFunctionExecuteLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListFunctionExecuteLogResponse().from_map(
            self.do_rpcrequest('ListFunctionExecuteLog', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_function_execute_log_with_options_async(
        self,
        request: iovcc_20180501_models.ListFunctionExecuteLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListFunctionExecuteLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListFunctionExecuteLogResponse().from_map(
            await self.do_rpcrequest_async('ListFunctionExecuteLog', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_execute_log(
        self,
        request: iovcc_20180501_models.ListFunctionExecuteLogRequest,
    ) -> iovcc_20180501_models.ListFunctionExecuteLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_function_execute_log_with_options(request, runtime)

    async def list_function_execute_log_async(
        self,
        request: iovcc_20180501_models.ListFunctionExecuteLogRequest,
    ) -> iovcc_20180501_models.ListFunctionExecuteLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_function_execute_log_with_options_async(request, runtime)

    def list_function_files_with_options(
        self,
        request: iovcc_20180501_models.ListFunctionFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListFunctionFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListFunctionFilesResponse().from_map(
            self.do_rpcrequest('ListFunctionFiles', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_function_files_with_options_async(
        self,
        request: iovcc_20180501_models.ListFunctionFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListFunctionFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListFunctionFilesResponse().from_map(
            await self.do_rpcrequest_async('ListFunctionFiles', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_files(
        self,
        request: iovcc_20180501_models.ListFunctionFilesRequest,
    ) -> iovcc_20180501_models.ListFunctionFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_function_files_with_options(request, runtime)

    async def list_function_files_async(
        self,
        request: iovcc_20180501_models.ListFunctionFilesRequest,
    ) -> iovcc_20180501_models.ListFunctionFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_function_files_with_options_async(request, runtime)

    def list_function_files_by_project_id_with_options(
        self,
        request: iovcc_20180501_models.ListFunctionFilesByProjectIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListFunctionFilesByProjectIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListFunctionFilesByProjectIdResponse().from_map(
            self.do_rpcrequest('ListFunctionFilesByProjectId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_function_files_by_project_id_with_options_async(
        self,
        request: iovcc_20180501_models.ListFunctionFilesByProjectIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListFunctionFilesByProjectIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListFunctionFilesByProjectIdResponse().from_map(
            await self.do_rpcrequest_async('ListFunctionFilesByProjectId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_files_by_project_id(
        self,
        request: iovcc_20180501_models.ListFunctionFilesByProjectIdRequest,
    ) -> iovcc_20180501_models.ListFunctionFilesByProjectIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_function_files_by_project_id_with_options(request, runtime)

    async def list_function_files_by_project_id_async(
        self,
        request: iovcc_20180501_models.ListFunctionFilesByProjectIdRequest,
    ) -> iovcc_20180501_models.ListFunctionFilesByProjectIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_function_files_by_project_id_with_options_async(request, runtime)

    def list_message_acks_with_options(
        self,
        request: iovcc_20180501_models.ListMessageAcksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMessageAcksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMessageAcksResponse().from_map(
            self.do_rpcrequest('ListMessageAcks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_message_acks_with_options_async(
        self,
        request: iovcc_20180501_models.ListMessageAcksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMessageAcksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMessageAcksResponse().from_map(
            await self.do_rpcrequest_async('ListMessageAcks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_message_acks(
        self,
        request: iovcc_20180501_models.ListMessageAcksRequest,
    ) -> iovcc_20180501_models.ListMessageAcksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_message_acks_with_options(request, runtime)

    async def list_message_acks_async(
        self,
        request: iovcc_20180501_models.ListMessageAcksRequest,
    ) -> iovcc_20180501_models.ListMessageAcksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_message_acks_with_options_async(request, runtime)

    def list_message_receivers_with_options(
        self,
        request: iovcc_20180501_models.ListMessageReceiversRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMessageReceiversResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMessageReceiversResponse().from_map(
            self.do_rpcrequest('ListMessageReceivers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_message_receivers_with_options_async(
        self,
        request: iovcc_20180501_models.ListMessageReceiversRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMessageReceiversResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMessageReceiversResponse().from_map(
            await self.do_rpcrequest_async('ListMessageReceivers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_message_receivers(
        self,
        request: iovcc_20180501_models.ListMessageReceiversRequest,
    ) -> iovcc_20180501_models.ListMessageReceiversResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_message_receivers_with_options(request, runtime)

    async def list_message_receivers_async(
        self,
        request: iovcc_20180501_models.ListMessageReceiversRequest,
    ) -> iovcc_20180501_models.ListMessageReceiversResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_message_receivers_with_options_async(request, runtime)

    def list_mqtt_client_subscriptions_with_options(
        self,
        request: iovcc_20180501_models.ListMqttClientSubscriptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMqttClientSubscriptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMqttClientSubscriptionsResponse().from_map(
            self.do_rpcrequest('ListMqttClientSubscriptions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_mqtt_client_subscriptions_with_options_async(
        self,
        request: iovcc_20180501_models.ListMqttClientSubscriptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMqttClientSubscriptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMqttClientSubscriptionsResponse().from_map(
            await self.do_rpcrequest_async('ListMqttClientSubscriptions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_mqtt_client_subscriptions(
        self,
        request: iovcc_20180501_models.ListMqttClientSubscriptionsRequest,
    ) -> iovcc_20180501_models.ListMqttClientSubscriptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_mqtt_client_subscriptions_with_options(request, runtime)

    async def list_mqtt_client_subscriptions_async(
        self,
        request: iovcc_20180501_models.ListMqttClientSubscriptionsRequest,
    ) -> iovcc_20180501_models.ListMqttClientSubscriptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_mqtt_client_subscriptions_with_options_async(request, runtime)

    def list_mqtt_message_logs_with_options(
        self,
        request: iovcc_20180501_models.ListMqttMessageLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMqttMessageLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMqttMessageLogsResponse().from_map(
            self.do_rpcrequest('ListMqttMessageLogs', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_mqtt_message_logs_with_options_async(
        self,
        request: iovcc_20180501_models.ListMqttMessageLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMqttMessageLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMqttMessageLogsResponse().from_map(
            await self.do_rpcrequest_async('ListMqttMessageLogs', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_mqtt_message_logs(
        self,
        request: iovcc_20180501_models.ListMqttMessageLogsRequest,
    ) -> iovcc_20180501_models.ListMqttMessageLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_mqtt_message_logs_with_options(request, runtime)

    async def list_mqtt_message_logs_async(
        self,
        request: iovcc_20180501_models.ListMqttMessageLogsRequest,
    ) -> iovcc_20180501_models.ListMqttMessageLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_mqtt_message_logs_with_options_async(request, runtime)

    def list_mqtt_root_topics_with_options(
        self,
        request: iovcc_20180501_models.ListMqttRootTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMqttRootTopicsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMqttRootTopicsResponse().from_map(
            self.do_rpcrequest('ListMqttRootTopics', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_mqtt_root_topics_with_options_async(
        self,
        request: iovcc_20180501_models.ListMqttRootTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListMqttRootTopicsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListMqttRootTopicsResponse().from_map(
            await self.do_rpcrequest_async('ListMqttRootTopics', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_mqtt_root_topics(
        self,
        request: iovcc_20180501_models.ListMqttRootTopicsRequest,
    ) -> iovcc_20180501_models.ListMqttRootTopicsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_mqtt_root_topics_with_options(request, runtime)

    async def list_mqtt_root_topics_async(
        self,
        request: iovcc_20180501_models.ListMqttRootTopicsRequest,
    ) -> iovcc_20180501_models.ListMqttRootTopicsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_mqtt_root_topics_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: iovcc_20180501_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListNamespacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListNamespacesResponse().from_map(
            self.do_rpcrequest('ListNamespaces', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: iovcc_20180501_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListNamespacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListNamespacesResponse().from_map(
            await self.do_rpcrequest_async('ListNamespaces', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_namespaces(
        self,
        request: iovcc_20180501_models.ListNamespacesRequest,
    ) -> iovcc_20180501_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: iovcc_20180501_models.ListNamespacesRequest,
    ) -> iovcc_20180501_models.ListNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_offline_messages_with_options(
        self,
        request: iovcc_20180501_models.ListOfflineMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListOfflineMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListOfflineMessagesResponse().from_map(
            self.do_rpcrequest('ListOfflineMessages', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_offline_messages_with_options_async(
        self,
        request: iovcc_20180501_models.ListOfflineMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListOfflineMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListOfflineMessagesResponse().from_map(
            await self.do_rpcrequest_async('ListOfflineMessages', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_offline_messages(
        self,
        request: iovcc_20180501_models.ListOfflineMessagesRequest,
    ) -> iovcc_20180501_models.ListOfflineMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_offline_messages_with_options(request, runtime)

    async def list_offline_messages_async(
        self,
        request: iovcc_20180501_models.ListOfflineMessagesRequest,
    ) -> iovcc_20180501_models.ListOfflineMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_offline_messages_with_options_async(request, runtime)

    def list_open_account_links_with_options(
        self,
        request: iovcc_20180501_models.ListOpenAccountLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListOpenAccountLinksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListOpenAccountLinksResponse().from_map(
            self.do_rpcrequest('ListOpenAccountLinks', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_open_account_links_with_options_async(
        self,
        request: iovcc_20180501_models.ListOpenAccountLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListOpenAccountLinksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListOpenAccountLinksResponse().from_map(
            await self.do_rpcrequest_async('ListOpenAccountLinks', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_open_account_links(
        self,
        request: iovcc_20180501_models.ListOpenAccountLinksRequest,
    ) -> iovcc_20180501_models.ListOpenAccountLinksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_open_account_links_with_options(request, runtime)

    async def list_open_account_links_async(
        self,
        request: iovcc_20180501_models.ListOpenAccountLinksRequest,
    ) -> iovcc_20180501_models.ListOpenAccountLinksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_open_account_links_with_options_async(request, runtime)

    def list_open_accounts_with_options(
        self,
        request: iovcc_20180501_models.ListOpenAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListOpenAccountsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListOpenAccountsResponse().from_map(
            self.do_rpcrequest('ListOpenAccounts', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_open_accounts_with_options_async(
        self,
        request: iovcc_20180501_models.ListOpenAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListOpenAccountsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListOpenAccountsResponse().from_map(
            await self.do_rpcrequest_async('ListOpenAccounts', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_open_accounts(
        self,
        request: iovcc_20180501_models.ListOpenAccountsRequest,
    ) -> iovcc_20180501_models.ListOpenAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_open_accounts_with_options(request, runtime)

    async def list_open_accounts_async(
        self,
        request: iovcc_20180501_models.ListOpenAccountsRequest,
    ) -> iovcc_20180501_models.ListOpenAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_open_accounts_with_options_async(request, runtime)

    def list_pre_checks_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListPreChecksResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListPreChecksResponse().from_map(
            self.do_rpcrequest('ListPreChecks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_pre_checks_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListPreChecksResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListPreChecksResponse().from_map(
            await self.do_rpcrequest_async('ListPreChecks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pre_checks(self) -> iovcc_20180501_models.ListPreChecksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_pre_checks_with_options(runtime)

    async def list_pre_checks_async(self) -> iovcc_20180501_models.ListPreChecksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_pre_checks_with_options_async(runtime)

    def list_project_apps_with_options(
        self,
        request: iovcc_20180501_models.ListProjectAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListProjectAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListProjectAppsResponse().from_map(
            self.do_rpcrequest('ListProjectApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_apps_with_options_async(
        self,
        request: iovcc_20180501_models.ListProjectAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListProjectAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListProjectAppsResponse().from_map(
            await self.do_rpcrequest_async('ListProjectApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_apps(
        self,
        request: iovcc_20180501_models.ListProjectAppsRequest,
    ) -> iovcc_20180501_models.ListProjectAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_apps_with_options(request, runtime)

    async def list_project_apps_async(
        self,
        request: iovcc_20180501_models.ListProjectAppsRequest,
    ) -> iovcc_20180501_models.ListProjectAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_apps_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListProjectsResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListProjectsResponse().from_map(
            self.do_rpcrequest('ListProjects', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListProjectsResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListProjectsResponse().from_map(
            await self.do_rpcrequest_async('ListProjects', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(self) -> iovcc_20180501_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(runtime)

    async def list_projects_async(self) -> iovcc_20180501_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(runtime)

    def list_rpc_services_with_options(
        self,
        request: iovcc_20180501_models.ListRpcServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListRpcServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListRpcServicesResponse().from_map(
            self.do_rpcrequest('ListRpcServices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rpc_services_with_options_async(
        self,
        request: iovcc_20180501_models.ListRpcServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListRpcServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListRpcServicesResponse().from_map(
            await self.do_rpcrequest_async('ListRpcServices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rpc_services(
        self,
        request: iovcc_20180501_models.ListRpcServicesRequest,
    ) -> iovcc_20180501_models.ListRpcServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_rpc_services_with_options(request, runtime)

    async def list_rpc_services_async(
        self,
        request: iovcc_20180501_models.ListRpcServicesRequest,
    ) -> iovcc_20180501_models.ListRpcServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rpc_services_with_options_async(request, runtime)

    def list_schema_subscribes_with_options(
        self,
        request: iovcc_20180501_models.ListSchemaSubscribesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListSchemaSubscribesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListSchemaSubscribesResponse().from_map(
            self.do_rpcrequest('ListSchemaSubscribes', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_schema_subscribes_with_options_async(
        self,
        request: iovcc_20180501_models.ListSchemaSubscribesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListSchemaSubscribesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListSchemaSubscribesResponse().from_map(
            await self.do_rpcrequest_async('ListSchemaSubscribes', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_schema_subscribes(
        self,
        request: iovcc_20180501_models.ListSchemaSubscribesRequest,
    ) -> iovcc_20180501_models.ListSchemaSubscribesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_schema_subscribes_with_options(request, runtime)

    async def list_schema_subscribes_async(
        self,
        request: iovcc_20180501_models.ListSchemaSubscribesRequest,
    ) -> iovcc_20180501_models.ListSchemaSubscribesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_schema_subscribes_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListServicesResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListServicesResponse().from_map(
            self.do_rpcrequest('ListServices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_services_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListServicesResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListServicesResponse().from_map(
            await self.do_rpcrequest_async('ListServices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_services(self) -> iovcc_20180501_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(runtime)

    async def list_services_async(self) -> iovcc_20180501_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(runtime)

    def list_shadow_schema_device_models_with_options(
        self,
        request: iovcc_20180501_models.ListShadowSchemaDeviceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListShadowSchemaDeviceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListShadowSchemaDeviceModelsResponse().from_map(
            self.do_rpcrequest('ListShadowSchemaDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_shadow_schema_device_models_with_options_async(
        self,
        request: iovcc_20180501_models.ListShadowSchemaDeviceModelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListShadowSchemaDeviceModelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return iovcc_20180501_models.ListShadowSchemaDeviceModelsResponse().from_map(
            await self.do_rpcrequest_async('ListShadowSchemaDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_shadow_schema_device_models(
        self,
        request: iovcc_20180501_models.ListShadowSchemaDeviceModelsRequest,
    ) -> iovcc_20180501_models.ListShadowSchemaDeviceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_shadow_schema_device_models_with_options(request, runtime)

    async def list_shadow_schema_device_models_async(
        self,
        request: iovcc_20180501_models.ListShadowSchemaDeviceModelsRequest,
    ) -> iovcc_20180501_models.ListShadowSchemaDeviceModelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_shadow_schema_device_models_with_options_async(request, runtime)

    def list_shadow_schemas_with_options(
        self,
        request: iovcc_20180501_models.ListShadowSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListShadowSchemasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListShadowSchemasResponse().from_map(
            self.do_rpcrequest('ListShadowSchemas', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_shadow_schemas_with_options_async(
        self,
        request: iovcc_20180501_models.ListShadowSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListShadowSchemasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListShadowSchemasResponse().from_map(
            await self.do_rpcrequest_async('ListShadowSchemas', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_shadow_schemas(
        self,
        request: iovcc_20180501_models.ListShadowSchemasRequest,
    ) -> iovcc_20180501_models.ListShadowSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_shadow_schemas_with_options(request, runtime)

    async def list_shadow_schemas_async(
        self,
        request: iovcc_20180501_models.ListShadowSchemasRequest,
    ) -> iovcc_20180501_models.ListShadowSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_shadow_schemas_with_options_async(request, runtime)

    def list_support_features_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListSupportFeaturesResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListSupportFeaturesResponse().from_map(
            self.do_rpcrequest('ListSupportFeatures', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_support_features_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListSupportFeaturesResponse:
        req = open_api_models.OpenApiRequest()
        return iovcc_20180501_models.ListSupportFeaturesResponse().from_map(
            await self.do_rpcrequest_async('ListSupportFeatures', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_support_features(self) -> iovcc_20180501_models.ListSupportFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_support_features_with_options(runtime)

    async def list_support_features_async(self) -> iovcc_20180501_models.ListSupportFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_support_features_with_options_async(runtime)

    def list_triggers_with_options(
        self,
        request: iovcc_20180501_models.ListTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListTriggersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListTriggersResponse().from_map(
            self.do_rpcrequest('ListTriggers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_triggers_with_options_async(
        self,
        request: iovcc_20180501_models.ListTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListTriggersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListTriggersResponse().from_map(
            await self.do_rpcrequest_async('ListTriggers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_triggers(
        self,
        request: iovcc_20180501_models.ListTriggersRequest,
    ) -> iovcc_20180501_models.ListTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_triggers_with_options(request, runtime)

    async def list_triggers_async(
        self,
        request: iovcc_20180501_models.ListTriggersRequest,
    ) -> iovcc_20180501_models.ListTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_triggers_with_options_async(request, runtime)

    def list_upstream_app_key_relations_with_options(
        self,
        request: iovcc_20180501_models.ListUpstreamAppKeyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListUpstreamAppKeyRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListUpstreamAppKeyRelationsResponse().from_map(
            self.do_rpcrequest('ListUpstreamAppKeyRelations', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_upstream_app_key_relations_with_options_async(
        self,
        request: iovcc_20180501_models.ListUpstreamAppKeyRelationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListUpstreamAppKeyRelationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListUpstreamAppKeyRelationsResponse().from_map(
            await self.do_rpcrequest_async('ListUpstreamAppKeyRelations', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_upstream_app_key_relations(
        self,
        request: iovcc_20180501_models.ListUpstreamAppKeyRelationsRequest,
    ) -> iovcc_20180501_models.ListUpstreamAppKeyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_upstream_app_key_relations_with_options(request, runtime)

    async def list_upstream_app_key_relations_async(
        self,
        request: iovcc_20180501_models.ListUpstreamAppKeyRelationsRequest,
    ) -> iovcc_20180501_models.ListUpstreamAppKeyRelationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_upstream_app_key_relations_with_options_async(request, runtime)

    def list_upstream_app_servers_with_options(
        self,
        request: iovcc_20180501_models.ListUpstreamAppServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListUpstreamAppServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListUpstreamAppServersResponse().from_map(
            self.do_rpcrequest('ListUpstreamAppServers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_upstream_app_servers_with_options_async(
        self,
        request: iovcc_20180501_models.ListUpstreamAppServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListUpstreamAppServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListUpstreamAppServersResponse().from_map(
            await self.do_rpcrequest_async('ListUpstreamAppServers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_upstream_app_servers(
        self,
        request: iovcc_20180501_models.ListUpstreamAppServersRequest,
    ) -> iovcc_20180501_models.ListUpstreamAppServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_upstream_app_servers_with_options(request, runtime)

    async def list_upstream_app_servers_async(
        self,
        request: iovcc_20180501_models.ListUpstreamAppServersRequest,
    ) -> iovcc_20180501_models.ListUpstreamAppServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_upstream_app_servers_with_options_async(request, runtime)

    def list_version_device_groups_with_options(
        self,
        request: iovcc_20180501_models.ListVersionDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListVersionDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListVersionDeviceGroupsResponse().from_map(
            self.do_rpcrequest('ListVersionDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_version_device_groups_with_options_async(
        self,
        request: iovcc_20180501_models.ListVersionDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.ListVersionDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.ListVersionDeviceGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListVersionDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_version_device_groups(
        self,
        request: iovcc_20180501_models.ListVersionDeviceGroupsRequest,
    ) -> iovcc_20180501_models.ListVersionDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_version_device_groups_with_options(request, runtime)

    async def list_version_device_groups_async(
        self,
        request: iovcc_20180501_models.ListVersionDeviceGroupsRequest,
    ) -> iovcc_20180501_models.ListVersionDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_version_device_groups_with_options_async(request, runtime)

    def publish_app_version_with_options(
        self,
        request: iovcc_20180501_models.PublishAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PublishAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PublishAppVersionResponse().from_map(
            self.do_rpcrequest('PublishAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_app_version_with_options_async(
        self,
        request: iovcc_20180501_models.PublishAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PublishAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PublishAppVersionResponse().from_map(
            await self.do_rpcrequest_async('PublishAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_app_version(
        self,
        request: iovcc_20180501_models.PublishAppVersionRequest,
    ) -> iovcc_20180501_models.PublishAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_app_version_with_options(request, runtime)

    async def publish_app_version_async(
        self,
        request: iovcc_20180501_models.PublishAppVersionRequest,
    ) -> iovcc_20180501_models.PublishAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_app_version_with_options_async(request, runtime)

    def publish_mqtt_message_with_options(
        self,
        request: iovcc_20180501_models.PublishMqttMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PublishMqttMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PublishMqttMessageResponse().from_map(
            self.do_rpcrequest('PublishMqttMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_mqtt_message_with_options_async(
        self,
        request: iovcc_20180501_models.PublishMqttMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PublishMqttMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PublishMqttMessageResponse().from_map(
            await self.do_rpcrequest_async('PublishMqttMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_mqtt_message(
        self,
        request: iovcc_20180501_models.PublishMqttMessageRequest,
    ) -> iovcc_20180501_models.PublishMqttMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_mqtt_message_with_options(request, runtime)

    async def publish_mqtt_message_async(
        self,
        request: iovcc_20180501_models.PublishMqttMessageRequest,
    ) -> iovcc_20180501_models.PublishMqttMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_mqtt_message_with_options_async(request, runtime)

    def publish_os_version_with_options(
        self,
        request: iovcc_20180501_models.PublishOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PublishOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PublishOsVersionResponse().from_map(
            self.do_rpcrequest('PublishOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_os_version_with_options_async(
        self,
        request: iovcc_20180501_models.PublishOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PublishOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PublishOsVersionResponse().from_map(
            await self.do_rpcrequest_async('PublishOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_os_version(
        self,
        request: iovcc_20180501_models.PublishOsVersionRequest,
    ) -> iovcc_20180501_models.PublishOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_os_version_with_options(request, runtime)

    async def publish_os_version_async(
        self,
        request: iovcc_20180501_models.PublishOsVersionRequest,
    ) -> iovcc_20180501_models.PublishOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_os_version_with_options_async(request, runtime)

    def push_message_with_options(
        self,
        request: iovcc_20180501_models.PushMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PushMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PushMessageResponse().from_map(
            self.do_rpcrequest('PushMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_message_with_options_async(
        self,
        request: iovcc_20180501_models.PushMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PushMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PushMessageResponse().from_map(
            await self.do_rpcrequest_async('PushMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_message(
        self,
        request: iovcc_20180501_models.PushMessageRequest,
    ) -> iovcc_20180501_models.PushMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_message_with_options(request, runtime)

    async def push_message_async(
        self,
        request: iovcc_20180501_models.PushMessageRequest,
    ) -> iovcc_20180501_models.PushMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_message_with_options_async(request, runtime)

    def push_version_message_with_options(
        self,
        request: iovcc_20180501_models.PushVersionMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PushVersionMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PushVersionMessageResponse().from_map(
            self.do_rpcrequest('PushVersionMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def push_version_message_with_options_async(
        self,
        request: iovcc_20180501_models.PushVersionMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.PushVersionMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.PushVersionMessageResponse().from_map(
            await self.do_rpcrequest_async('PushVersionMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_version_message(
        self,
        request: iovcc_20180501_models.PushVersionMessageRequest,
    ) -> iovcc_20180501_models.PushVersionMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_version_message_with_options(request, runtime)

    async def push_version_message_async(
        self,
        request: iovcc_20180501_models.PushVersionMessageRequest,
    ) -> iovcc_20180501_models.PushVersionMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_version_message_with_options_async(request, runtime)

    def query_prepublish_passed_device_count_with_options(
        self,
        request: iovcc_20180501_models.QueryPrepublishPassedDeviceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.QueryPrepublishPassedDeviceCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.QueryPrepublishPassedDeviceCountResponse().from_map(
            self.do_rpcrequest('QueryPrepublishPassedDeviceCount', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_prepublish_passed_device_count_with_options_async(
        self,
        request: iovcc_20180501_models.QueryPrepublishPassedDeviceCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.QueryPrepublishPassedDeviceCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.QueryPrepublishPassedDeviceCountResponse().from_map(
            await self.do_rpcrequest_async('QueryPrepublishPassedDeviceCount', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_prepublish_passed_device_count(
        self,
        request: iovcc_20180501_models.QueryPrepublishPassedDeviceCountRequest,
    ) -> iovcc_20180501_models.QueryPrepublishPassedDeviceCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_prepublish_passed_device_count_with_options(request, runtime)

    async def query_prepublish_passed_device_count_async(
        self,
        request: iovcc_20180501_models.QueryPrepublishPassedDeviceCountRequest,
    ) -> iovcc_20180501_models.QueryPrepublishPassedDeviceCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_prepublish_passed_device_count_with_options_async(request, runtime)

    def submit_assist_report_with_options(
        self,
        request: iovcc_20180501_models.SubmitAssistReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.SubmitAssistReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.SubmitAssistReportResponse().from_map(
            self.do_rpcrequest('SubmitAssistReport', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_assist_report_with_options_async(
        self,
        request: iovcc_20180501_models.SubmitAssistReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.SubmitAssistReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.SubmitAssistReportResponse().from_map(
            await self.do_rpcrequest_async('SubmitAssistReport', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_assist_report(
        self,
        request: iovcc_20180501_models.SubmitAssistReportRequest,
    ) -> iovcc_20180501_models.SubmitAssistReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_assist_report_with_options(request, runtime)

    async def submit_assist_report_async(
        self,
        request: iovcc_20180501_models.SubmitAssistReportRequest,
    ) -> iovcc_20180501_models.SubmitAssistReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_assist_report_with_options_async(request, runtime)

    def update_api_gateway_app_status_with_options(
        self,
        request: iovcc_20180501_models.UpdateApiGatewayAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateApiGatewayAppStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateApiGatewayAppStatusResponse().from_map(
            self.do_rpcrequest('UpdateApiGatewayAppStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_api_gateway_app_status_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateApiGatewayAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateApiGatewayAppStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateApiGatewayAppStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateApiGatewayAppStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_api_gateway_app_status(
        self,
        request: iovcc_20180501_models.UpdateApiGatewayAppStatusRequest,
    ) -> iovcc_20180501_models.UpdateApiGatewayAppStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_api_gateway_app_status_with_options(request, runtime)

    async def update_api_gateway_app_status_async(
        self,
        request: iovcc_20180501_models.UpdateApiGatewayAppStatusRequest,
    ) -> iovcc_20180501_models.UpdateApiGatewayAppStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_api_gateway_app_status_with_options_async(request, runtime)

    def update_app_black_white_versions_with_options(
        self,
        request: iovcc_20180501_models.UpdateAppBlackWhiteVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppBlackWhiteVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppBlackWhiteVersionsResponse().from_map(
            self.do_rpcrequest('UpdateAppBlackWhiteVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_black_white_versions_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateAppBlackWhiteVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppBlackWhiteVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppBlackWhiteVersionsResponse().from_map(
            await self.do_rpcrequest_async('UpdateAppBlackWhiteVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_black_white_versions(
        self,
        request: iovcc_20180501_models.UpdateAppBlackWhiteVersionsRequest,
    ) -> iovcc_20180501_models.UpdateAppBlackWhiteVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_black_white_versions_with_options(request, runtime)

    async def update_app_black_white_versions_async(
        self,
        request: iovcc_20180501_models.UpdateAppBlackWhiteVersionsRequest,
    ) -> iovcc_20180501_models.UpdateAppBlackWhiteVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_black_white_versions_with_options_async(request, runtime)

    def update_app_version_with_options(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionResponse().from_map(
            self.do_rpcrequest('UpdateAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_version_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionResponse().from_map(
            await self.do_rpcrequest_async('UpdateAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_with_options(request, runtime)

    async def update_app_version_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_version_with_options_async(request, runtime)

    def update_app_version_release_note_with_options(
        self,
        request: iovcc_20180501_models.UpdateAppVersionReleaseNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionReleaseNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionReleaseNoteResponse().from_map(
            self.do_rpcrequest('UpdateAppVersionReleaseNote', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_version_release_note_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionReleaseNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionReleaseNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionReleaseNoteResponse().from_map(
            await self.do_rpcrequest_async('UpdateAppVersionReleaseNote', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version_release_note(
        self,
        request: iovcc_20180501_models.UpdateAppVersionReleaseNoteRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionReleaseNoteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_release_note_with_options(request, runtime)

    async def update_app_version_release_note_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionReleaseNoteRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionReleaseNoteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_version_release_note_with_options_async(request, runtime)

    def update_app_version_remark_with_options(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionRemarkResponse().from_map(
            self.do_rpcrequest('UpdateAppVersionRemark', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_version_remark_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionRemarkResponse().from_map(
            await self.do_rpcrequest_async('UpdateAppVersionRemark', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version_remark(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRemarkRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_remark_with_options(request, runtime)

    async def update_app_version_remark_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionRemarkRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_version_remark_with_options_async(request, runtime)

    def update_app_version_status_with_options(
        self,
        request: iovcc_20180501_models.UpdateAppVersionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionStatusResponse().from_map(
            self.do_rpcrequest('UpdateAppVersionStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_version_status_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateAppVersionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateAppVersionStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateAppVersionStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version_status(
        self,
        request: iovcc_20180501_models.UpdateAppVersionStatusRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_status_with_options(request, runtime)

    async def update_app_version_status_async(
        self,
        request: iovcc_20180501_models.UpdateAppVersionStatusRequest,
    ) -> iovcc_20180501_models.UpdateAppVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_version_status_with_options_async(request, runtime)

    def update_customized_filter_with_options(
        self,
        request: iovcc_20180501_models.UpdateCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateCustomizedFilterResponse().from_map(
            self.do_rpcrequest('UpdateCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_customized_filter_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateCustomizedFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateCustomizedFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateCustomizedFilterResponse().from_map(
            await self.do_rpcrequest_async('UpdateCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_customized_filter(
        self,
        request: iovcc_20180501_models.UpdateCustomizedFilterRequest,
    ) -> iovcc_20180501_models.UpdateCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_customized_filter_with_options(request, runtime)

    async def update_customized_filter_async(
        self,
        request: iovcc_20180501_models.UpdateCustomizedFilterRequest,
    ) -> iovcc_20180501_models.UpdateCustomizedFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_customized_filter_with_options_async(request, runtime)

    def update_device_model_with_options(
        self,
        request: iovcc_20180501_models.UpdateDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateDeviceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateDeviceModelResponse().from_map(
            self.do_rpcrequest('UpdateDeviceModel', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_model_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateDeviceModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateDeviceModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateDeviceModelResponse().from_map(
            await self.do_rpcrequest_async('UpdateDeviceModel', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_model(
        self,
        request: iovcc_20180501_models.UpdateDeviceModelRequest,
    ) -> iovcc_20180501_models.UpdateDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_model_with_options(request, runtime)

    async def update_device_model_async(
        self,
        request: iovcc_20180501_models.UpdateDeviceModelRequest,
    ) -> iovcc_20180501_models.UpdateDeviceModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_model_with_options_async(request, runtime)

    def update_namespace_data_with_options(
        self,
        request: iovcc_20180501_models.UpdateNamespaceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateNamespaceDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateNamespaceDataResponse().from_map(
            self.do_rpcrequest('UpdateNamespaceData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_namespace_data_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateNamespaceDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateNamespaceDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateNamespaceDataResponse().from_map(
            await self.do_rpcrequest_async('UpdateNamespaceData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_namespace_data(
        self,
        request: iovcc_20180501_models.UpdateNamespaceDataRequest,
    ) -> iovcc_20180501_models.UpdateNamespaceDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_namespace_data_with_options(request, runtime)

    async def update_namespace_data_async(
        self,
        request: iovcc_20180501_models.UpdateNamespaceDataRequest,
    ) -> iovcc_20180501_models.UpdateNamespaceDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_namespace_data_with_options_async(request, runtime)

    def update_os_black_white_versions_with_options(
        self,
        request: iovcc_20180501_models.UpdateOsBlackWhiteVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsBlackWhiteVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsBlackWhiteVersionsResponse().from_map(
            self.do_rpcrequest('UpdateOsBlackWhiteVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_os_black_white_versions_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateOsBlackWhiteVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsBlackWhiteVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsBlackWhiteVersionsResponse().from_map(
            await self.do_rpcrequest_async('UpdateOsBlackWhiteVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_black_white_versions(
        self,
        request: iovcc_20180501_models.UpdateOsBlackWhiteVersionsRequest,
    ) -> iovcc_20180501_models.UpdateOsBlackWhiteVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_os_black_white_versions_with_options(request, runtime)

    async def update_os_black_white_versions_async(
        self,
        request: iovcc_20180501_models.UpdateOsBlackWhiteVersionsRequest,
    ) -> iovcc_20180501_models.UpdateOsBlackWhiteVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_os_black_white_versions_with_options_async(request, runtime)

    def update_os_version_with_options(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionResponse().from_map(
            self.do_rpcrequest('UpdateOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_os_version_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionResponse().from_map(
            await self.do_rpcrequest_async('UpdateOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_with_options(request, runtime)

    async def update_os_version_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_os_version_with_options_async(request, runtime)

    def update_os_version_release_note_with_options(
        self,
        request: iovcc_20180501_models.UpdateOsVersionReleaseNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionReleaseNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionReleaseNoteResponse().from_map(
            self.do_rpcrequest('UpdateOsVersionReleaseNote', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_os_version_release_note_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionReleaseNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionReleaseNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionReleaseNoteResponse().from_map(
            await self.do_rpcrequest_async('UpdateOsVersionReleaseNote', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version_release_note(
        self,
        request: iovcc_20180501_models.UpdateOsVersionReleaseNoteRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionReleaseNoteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_release_note_with_options(request, runtime)

    async def update_os_version_release_note_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionReleaseNoteRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionReleaseNoteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_os_version_release_note_with_options_async(request, runtime)

    def update_os_version_remark_with_options(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionRemarkResponse().from_map(
            self.do_rpcrequest('UpdateOsVersionRemark', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_os_version_remark_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRemarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionRemarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionRemarkResponse().from_map(
            await self.do_rpcrequest_async('UpdateOsVersionRemark', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version_remark(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRemarkRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_remark_with_options(request, runtime)

    async def update_os_version_remark_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionRemarkRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionRemarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_os_version_remark_with_options_async(request, runtime)

    def update_os_version_status_with_options(
        self,
        request: iovcc_20180501_models.UpdateOsVersionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionStatusResponse().from_map(
            self.do_rpcrequest('UpdateOsVersionStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_os_version_status_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateOsVersionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateOsVersionStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateOsVersionStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version_status(
        self,
        request: iovcc_20180501_models.UpdateOsVersionStatusRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_status_with_options(request, runtime)

    async def update_os_version_status_async(
        self,
        request: iovcc_20180501_models.UpdateOsVersionStatusRequest,
    ) -> iovcc_20180501_models.UpdateOsVersionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_os_version_status_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: iovcc_20180501_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateProjectResponse().from_map(
            self.do_rpcrequest('UpdateProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateProjectResponse().from_map(
            await self.do_rpcrequest_async('UpdateProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(
        self,
        request: iovcc_20180501_models.UpdateProjectRequest,
    ) -> iovcc_20180501_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: iovcc_20180501_models.UpdateProjectRequest,
    ) -> iovcc_20180501_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_schema_subscribe_with_options(
        self,
        request: iovcc_20180501_models.UpdateSchemaSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateSchemaSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateSchemaSubscribeResponse().from_map(
            self.do_rpcrequest('UpdateSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_schema_subscribe_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateSchemaSubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateSchemaSubscribeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateSchemaSubscribeResponse().from_map(
            await self.do_rpcrequest_async('UpdateSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_schema_subscribe(
        self,
        request: iovcc_20180501_models.UpdateSchemaSubscribeRequest,
    ) -> iovcc_20180501_models.UpdateSchemaSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_schema_subscribe_with_options(request, runtime)

    async def update_schema_subscribe_async(
        self,
        request: iovcc_20180501_models.UpdateSchemaSubscribeRequest,
    ) -> iovcc_20180501_models.UpdateSchemaSubscribeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_schema_subscribe_with_options_async(request, runtime)

    def update_shadow_schema_with_options(
        self,
        request: iovcc_20180501_models.UpdateShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateShadowSchemaResponse().from_map(
            self.do_rpcrequest('UpdateShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_shadow_schema_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateShadowSchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateShadowSchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateShadowSchemaResponse().from_map(
            await self.do_rpcrequest_async('UpdateShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_shadow_schema(
        self,
        request: iovcc_20180501_models.UpdateShadowSchemaRequest,
    ) -> iovcc_20180501_models.UpdateShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_shadow_schema_with_options(request, runtime)

    async def update_shadow_schema_async(
        self,
        request: iovcc_20180501_models.UpdateShadowSchemaRequest,
    ) -> iovcc_20180501_models.UpdateShadowSchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_shadow_schema_with_options_async(request, runtime)

    def update_trigger_with_options(
        self,
        request: iovcc_20180501_models.UpdateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateTriggerResponse().from_map(
            self.do_rpcrequest('UpdateTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateTriggerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateTriggerResponse().from_map(
            await self.do_rpcrequest_async('UpdateTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_trigger(
        self,
        request: iovcc_20180501_models.UpdateTriggerRequest,
    ) -> iovcc_20180501_models.UpdateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_trigger_with_options(request, runtime)

    async def update_trigger_async(
        self,
        request: iovcc_20180501_models.UpdateTriggerRequest,
    ) -> iovcc_20180501_models.UpdateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_trigger_with_options_async(request, runtime)

    def update_upstream_app_server_with_options(
        self,
        request: iovcc_20180501_models.UpdateUpstreamAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateUpstreamAppServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateUpstreamAppServerResponse().from_map(
            self.do_rpcrequest('UpdateUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_upstream_app_server_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateUpstreamAppServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateUpstreamAppServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateUpstreamAppServerResponse().from_map(
            await self.do_rpcrequest_async('UpdateUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_upstream_app_server(
        self,
        request: iovcc_20180501_models.UpdateUpstreamAppServerRequest,
    ) -> iovcc_20180501_models.UpdateUpstreamAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_upstream_app_server_with_options(request, runtime)

    async def update_upstream_app_server_async(
        self,
        request: iovcc_20180501_models.UpdateUpstreamAppServerRequest,
    ) -> iovcc_20180501_models.UpdateUpstreamAppServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_upstream_app_server_with_options_async(request, runtime)

    def update_version_device_group_with_options(
        self,
        request: iovcc_20180501_models.UpdateVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateVersionDeviceGroupResponse().from_map(
            self.do_rpcrequest('UpdateVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_version_device_group_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateVersionDeviceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateVersionDeviceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateVersionDeviceGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_version_device_group(
        self,
        request: iovcc_20180501_models.UpdateVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.UpdateVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_version_device_group_with_options(request, runtime)

    async def update_version_device_group_async(
        self,
        request: iovcc_20180501_models.UpdateVersionDeviceGroupRequest,
    ) -> iovcc_20180501_models.UpdateVersionDeviceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_version_device_group_with_options_async(request, runtime)

    def update_version_prepublish_active_status_with_options(
        self,
        request: iovcc_20180501_models.UpdateVersionPrepublishActiveStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateVersionPrepublishActiveStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateVersionPrepublishActiveStatusResponse().from_map(
            self.do_rpcrequest('UpdateVersionPrepublishActiveStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_version_prepublish_active_status_with_options_async(
        self,
        request: iovcc_20180501_models.UpdateVersionPrepublishActiveStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iovcc_20180501_models.UpdateVersionPrepublishActiveStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iovcc_20180501_models.UpdateVersionPrepublishActiveStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateVersionPrepublishActiveStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_version_prepublish_active_status(
        self,
        request: iovcc_20180501_models.UpdateVersionPrepublishActiveStatusRequest,
    ) -> iovcc_20180501_models.UpdateVersionPrepublishActiveStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_version_prepublish_active_status_with_options(request, runtime)

    async def update_version_prepublish_active_status_async(
        self,
        request: iovcc_20180501_models.UpdateVersionPrepublishActiveStatusRequest,
    ) -> iovcc_20180501_models.UpdateVersionPrepublishActiveStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_version_prepublish_active_status_with_options_async(request, runtime)
