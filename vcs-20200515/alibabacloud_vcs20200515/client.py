# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vcs20200515 import models as vcs_20200515_models
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
        self._endpoint = self.get_endpoint('vcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def unbind_person_with_options(
        self,
        request: vcs_20200515_models.UnbindPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UnbindPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UnbindPersonResponse().from_map(
            self.do_rpcrequest('UnbindPerson', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_person_with_options_async(
        self,
        request: vcs_20200515_models.UnbindPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UnbindPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UnbindPersonResponse().from_map(
            await self.do_rpcrequest_async('UnbindPerson', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_person(
        self,
        request: vcs_20200515_models.UnbindPersonRequest,
    ) -> vcs_20200515_models.UnbindPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_person_with_options(request, runtime)

    async def unbind_person_async(
        self,
        request: vcs_20200515_models.UnbindPersonRequest,
    ) -> vcs_20200515_models.UnbindPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_person_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        tmp_req: vcs_20200515_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.ListUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.person_list):
            request.person_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_list, 'PersonList', 'json')
        if not UtilClient.is_unset(tmp_req.user_list):
            request.user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        tmp_req: vcs_20200515_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.ListUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.person_list):
            request.person_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_list, 'PersonList', 'json')
        if not UtilClient.is_unset(tmp_req.user_list):
            request.user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListUsersResponse().from_map(
            await self.do_rpcrequest_async('ListUsers', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: vcs_20200515_models.ListUsersRequest,
    ) -> vcs_20200515_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: vcs_20200515_models.ListUsersRequest,
    ) -> vcs_20200515_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def search_object_with_options(
        self,
        tmp_req: vcs_20200515_models.SearchObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SearchObjectResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchObjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_list):
            request.device_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_list, 'DeviceList', 'json')
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not UtilClient.is_unset(tmp_req.image_path):
            request.image_path_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_path, 'ImagePath', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SearchObjectResponse().from_map(
            self.do_rpcrequest('SearchObject', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_object_with_options_async(
        self,
        tmp_req: vcs_20200515_models.SearchObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SearchObjectResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchObjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device_list):
            request.device_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_list, 'DeviceList', 'json')
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not UtilClient.is_unset(tmp_req.image_path):
            request.image_path_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_path, 'ImagePath', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SearchObjectResponse().from_map(
            await self.do_rpcrequest_async('SearchObject', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_object(
        self,
        request: vcs_20200515_models.SearchObjectRequest,
    ) -> vcs_20200515_models.SearchObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_object_with_options(request, runtime)

    async def search_object_async(
        self,
        request: vcs_20200515_models.SearchObjectRequest,
    ) -> vcs_20200515_models.SearchObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_object_with_options_async(request, runtime)

    def delete_records_with_options(
        self,
        request: vcs_20200515_models.DeleteRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteRecordsResponse().from_map(
            self.do_rpcrequest('DeleteRecords', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_records_with_options_async(
        self,
        request: vcs_20200515_models.DeleteRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteRecordsResponse().from_map(
            await self.do_rpcrequest_async('DeleteRecords', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_records(
        self,
        request: vcs_20200515_models.DeleteRecordsRequest,
    ) -> vcs_20200515_models.DeleteRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_records_with_options(request, runtime)

    async def delete_records_async(
        self,
        request: vcs_20200515_models.DeleteRecordsRequest,
    ) -> vcs_20200515_models.DeleteRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_records_with_options_async(request, runtime)

    def start_deploy_with_options(
        self,
        request: vcs_20200515_models.StartDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StartDeployResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StartDeployResponse().from_map(
            self.do_rpcrequest('StartDeploy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_deploy_with_options_async(
        self,
        request: vcs_20200515_models.StartDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StartDeployResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StartDeployResponse().from_map(
            await self.do_rpcrequest_async('StartDeploy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_deploy(
        self,
        request: vcs_20200515_models.StartDeployRequest,
    ) -> vcs_20200515_models.StartDeployResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_deploy_with_options(request, runtime)

    async def start_deploy_async(
        self,
        request: vcs_20200515_models.StartDeployRequest,
    ) -> vcs_20200515_models.StartDeployResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_deploy_with_options_async(request, runtime)

    def get_inventory_with_options(
        self,
        request: vcs_20200515_models.GetInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetInventoryResponse().from_map(
            self.do_rpcrequest('GetInventory', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_inventory_with_options_async(
        self,
        request: vcs_20200515_models.GetInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetInventoryResponse().from_map(
            await self.do_rpcrequest_async('GetInventory', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_inventory(
        self,
        request: vcs_20200515_models.GetInventoryRequest,
    ) -> vcs_20200515_models.GetInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inventory_with_options(request, runtime)

    async def get_inventory_async(
        self,
        request: vcs_20200515_models.GetInventoryRequest,
    ) -> vcs_20200515_models.GetInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inventory_with_options_async(request, runtime)

    def upload_image_with_options(
        self,
        request: vcs_20200515_models.UploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UploadImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UploadImageResponse().from_map(
            self.do_rpcrequest('UploadImage', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_image_with_options_async(
        self,
        request: vcs_20200515_models.UploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UploadImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UploadImageResponse().from_map(
            await self.do_rpcrequest_async('UploadImage', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_image(
        self,
        request: vcs_20200515_models.UploadImageRequest,
    ) -> vcs_20200515_models.UploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_image_with_options(request, runtime)

    async def upload_image_async(
        self,
        request: vcs_20200515_models.UploadImageRequest,
    ) -> vcs_20200515_models.UploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_image_with_options_async(request, runtime)

    def bind_user_with_options(
        self,
        request: vcs_20200515_models.BindUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.BindUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.BindUserResponse().from_map(
            self.do_rpcrequest('BindUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_user_with_options_async(
        self,
        request: vcs_20200515_models.BindUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.BindUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.BindUserResponse().from_map(
            await self.do_rpcrequest_async('BindUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_user(
        self,
        request: vcs_20200515_models.BindUserRequest,
    ) -> vcs_20200515_models.BindUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_user_with_options(request, runtime)

    async def bind_user_async(
        self,
        request: vcs_20200515_models.BindUserRequest,
    ) -> vcs_20200515_models.BindUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_user_with_options_async(request, runtime)

    def delete_device_with_options(
        self,
        request: vcs_20200515_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteDeviceResponse().from_map(
            self.do_rpcrequest('DeleteDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: vcs_20200515_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteDeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device(
        self,
        request: vcs_20200515_models.DeleteDeviceRequest,
    ) -> vcs_20200515_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    async def delete_device_async(
        self,
        request: vcs_20200515_models.DeleteDeviceRequest,
    ) -> vcs_20200515_models.DeleteDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_with_options_async(request, runtime)

    def verify_train_label_with_options(
        self,
        request: vcs_20200515_models.VerifyTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.VerifyTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.VerifyTrainLabelResponse().from_map(
            self.do_rpcrequest('VerifyTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_train_label_with_options_async(
        self,
        request: vcs_20200515_models.VerifyTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.VerifyTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.VerifyTrainLabelResponse().from_map(
            await self.do_rpcrequest_async('VerifyTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_train_label(
        self,
        request: vcs_20200515_models.VerifyTrainLabelRequest,
    ) -> vcs_20200515_models.VerifyTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_train_label_with_options(request, runtime)

    async def verify_train_label_async(
        self,
        request: vcs_20200515_models.VerifyTrainLabelRequest,
    ) -> vcs_20200515_models.VerifyTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_train_label_with_options_async(request, runtime)

    def update_monitor_with_options(
        self,
        request: vcs_20200515_models.UpdateMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateMonitorResponse().from_map(
            self.do_rpcrequest('UpdateMonitor', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_monitor_with_options_async(
        self,
        request: vcs_20200515_models.UpdateMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateMonitorResponse().from_map(
            await self.do_rpcrequest_async('UpdateMonitor', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_monitor(
        self,
        request: vcs_20200515_models.UpdateMonitorRequest,
    ) -> vcs_20200515_models.UpdateMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_monitor_with_options(request, runtime)

    async def update_monitor_async(
        self,
        request: vcs_20200515_models.UpdateMonitorRequest,
    ) -> vcs_20200515_models.UpdateMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_monitor_with_options_async(request, runtime)

    def get_person_detail_with_options(
        self,
        request: vcs_20200515_models.GetPersonDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetPersonDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetPersonDetailResponse().from_map(
            self.do_rpcrequest('GetPersonDetail', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_person_detail_with_options_async(
        self,
        request: vcs_20200515_models.GetPersonDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetPersonDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetPersonDetailResponse().from_map(
            await self.do_rpcrequest_async('GetPersonDetail', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_person_detail(
        self,
        request: vcs_20200515_models.GetPersonDetailRequest,
    ) -> vcs_20200515_models.GetPersonDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_person_detail_with_options(request, runtime)

    async def get_person_detail_async(
        self,
        request: vcs_20200515_models.GetPersonDetailRequest,
    ) -> vcs_20200515_models.GetPersonDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_person_detail_with_options_async(request, runtime)

    def delete_sample_with_options(
        self,
        request: vcs_20200515_models.DeleteSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteSampleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteSampleResponse().from_map(
            self.do_rpcrequest('DeleteSample', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sample_with_options_async(
        self,
        request: vcs_20200515_models.DeleteSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteSampleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteSampleResponse().from_map(
            await self.do_rpcrequest_async('DeleteSample', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sample(
        self,
        request: vcs_20200515_models.DeleteSampleRequest,
    ) -> vcs_20200515_models.DeleteSampleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sample_with_options(request, runtime)

    async def delete_sample_async(
        self,
        request: vcs_20200515_models.DeleteSampleRequest,
    ) -> vcs_20200515_models.DeleteSampleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sample_with_options_async(request, runtime)

    def list_corp_group_metrics_with_options(
        self,
        request: vcs_20200515_models.ListCorpGroupMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpGroupMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpGroupMetricsResponse().from_map(
            self.do_rpcrequest('ListCorpGroupMetrics', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_corp_group_metrics_with_options_async(
        self,
        request: vcs_20200515_models.ListCorpGroupMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpGroupMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpGroupMetricsResponse().from_map(
            await self.do_rpcrequest_async('ListCorpGroupMetrics', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corp_group_metrics(
        self,
        request: vcs_20200515_models.ListCorpGroupMetricsRequest,
    ) -> vcs_20200515_models.ListCorpGroupMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_corp_group_metrics_with_options(request, runtime)

    async def list_corp_group_metrics_async(
        self,
        request: vcs_20200515_models.ListCorpGroupMetricsRequest,
    ) -> vcs_20200515_models.ListCorpGroupMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_corp_group_metrics_with_options_async(request, runtime)

    def save_video_summary_task_video_with_options(
        self,
        request: vcs_20200515_models.SaveVideoSummaryTaskVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SaveVideoSummaryTaskVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SaveVideoSummaryTaskVideoResponse().from_map(
            self.do_rpcrequest('SaveVideoSummaryTaskVideo', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_video_summary_task_video_with_options_async(
        self,
        request: vcs_20200515_models.SaveVideoSummaryTaskVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SaveVideoSummaryTaskVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SaveVideoSummaryTaskVideoResponse().from_map(
            await self.do_rpcrequest_async('SaveVideoSummaryTaskVideo', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_video_summary_task_video(
        self,
        request: vcs_20200515_models.SaveVideoSummaryTaskVideoRequest,
    ) -> vcs_20200515_models.SaveVideoSummaryTaskVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_video_summary_task_video_with_options(request, runtime)

    async def save_video_summary_task_video_async(
        self,
        request: vcs_20200515_models.SaveVideoSummaryTaskVideoRequest,
    ) -> vcs_20200515_models.SaveVideoSummaryTaskVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_video_summary_task_video_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: vcs_20200515_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteProjectResponse().from_map(
            self.do_rpcrequest('DeleteProject', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: vcs_20200515_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteProject', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(
        self,
        request: vcs_20200515_models.DeleteProjectRequest,
    ) -> vcs_20200515_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: vcs_20200515_models.DeleteProjectRequest,
    ) -> vcs_20200515_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def search_face_with_options(
        self,
        tmp_req: vcs_20200515_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SearchFaceResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchFaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.option_list):
            request.option_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option_list, 'OptionList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SearchFaceResponse().from_map(
            self.do_rpcrequest('SearchFace', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_face_with_options_async(
        self,
        tmp_req: vcs_20200515_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SearchFaceResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchFaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.option_list):
            request.option_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option_list, 'OptionList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SearchFaceResponse().from_map(
            await self.do_rpcrequest_async('SearchFace', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_face(
        self,
        request: vcs_20200515_models.SearchFaceRequest,
    ) -> vcs_20200515_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    async def search_face_async(
        self,
        request: vcs_20200515_models.SearchFaceRequest,
    ) -> vcs_20200515_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_face_with_options_async(request, runtime)

    def list_access_number_with_options(
        self,
        request: vcs_20200515_models.ListAccessNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListAccessNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListAccessNumberResponse().from_map(
            self.do_rpcrequest('ListAccessNumber', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_access_number_with_options_async(
        self,
        request: vcs_20200515_models.ListAccessNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListAccessNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListAccessNumberResponse().from_map(
            await self.do_rpcrequest_async('ListAccessNumber', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_access_number(
        self,
        request: vcs_20200515_models.ListAccessNumberRequest,
    ) -> vcs_20200515_models.ListAccessNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_number_with_options(request, runtime)

    async def list_access_number_async(
        self,
        request: vcs_20200515_models.ListAccessNumberRequest,
    ) -> vcs_20200515_models.ListAccessNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_number_with_options_async(request, runtime)

    def get_device_picture_with_options(
        self,
        request: vcs_20200515_models.GetDevicePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDevicePictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDevicePictureResponse().from_map(
            self.do_rpcrequest('GetDevicePicture', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_picture_with_options_async(
        self,
        request: vcs_20200515_models.GetDevicePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDevicePictureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDevicePictureResponse().from_map(
            await self.do_rpcrequest_async('GetDevicePicture', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_picture(
        self,
        request: vcs_20200515_models.GetDevicePictureRequest,
    ) -> vcs_20200515_models.GetDevicePictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_picture_with_options(request, runtime)

    async def get_device_picture_async(
        self,
        request: vcs_20200515_models.GetDevicePictureRequest,
    ) -> vcs_20200515_models.GetDevicePictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_picture_with_options_async(request, runtime)

    def get_monitor_list_with_options(
        self,
        request: vcs_20200515_models.GetMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetMonitorListResponse().from_map(
            self.do_rpcrequest('GetMonitorList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_monitor_list_with_options_async(
        self,
        request: vcs_20200515_models.GetMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetMonitorListResponse().from_map(
            await self.do_rpcrequest_async('GetMonitorList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_monitor_list(
        self,
        request: vcs_20200515_models.GetMonitorListRequest,
    ) -> vcs_20200515_models.GetMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_list_with_options(request, runtime)

    async def get_monitor_list_async(
        self,
        request: vcs_20200515_models.GetMonitorListRequest,
    ) -> vcs_20200515_models.GetMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_monitor_list_with_options_async(request, runtime)

    def list_train_label_with_options(
        self,
        request: vcs_20200515_models.ListTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListTrainLabelResponse().from_map(
            self.do_rpcrequest('ListTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_train_label_with_options_async(
        self,
        request: vcs_20200515_models.ListTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListTrainLabelResponse().from_map(
            await self.do_rpcrequest_async('ListTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_train_label(
        self,
        request: vcs_20200515_models.ListTrainLabelRequest,
    ) -> vcs_20200515_models.ListTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_train_label_with_options(request, runtime)

    async def list_train_label_async(
        self,
        request: vcs_20200515_models.ListTrainLabelRequest,
    ) -> vcs_20200515_models.ListTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_train_label_with_options_async(request, runtime)

    def update_train_label_with_options(
        self,
        request: vcs_20200515_models.UpdateTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateTrainLabelResponse().from_map(
            self.do_rpcrequest('UpdateTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_train_label_with_options_async(
        self,
        request: vcs_20200515_models.UpdateTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateTrainLabelResponse().from_map(
            await self.do_rpcrequest_async('UpdateTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_train_label(
        self,
        request: vcs_20200515_models.UpdateTrainLabelRequest,
    ) -> vcs_20200515_models.UpdateTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_train_label_with_options(request, runtime)

    async def update_train_label_async(
        self,
        request: vcs_20200515_models.UpdateTrainLabelRequest,
    ) -> vcs_20200515_models.UpdateTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_train_label_with_options_async(request, runtime)

    def delete_train_label_with_options(
        self,
        request: vcs_20200515_models.DeleteTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteTrainLabelResponse().from_map(
            self.do_rpcrequest('DeleteTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_train_label_with_options_async(
        self,
        request: vcs_20200515_models.DeleteTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteTrainLabelResponse().from_map(
            await self.do_rpcrequest_async('DeleteTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_train_label(
        self,
        request: vcs_20200515_models.DeleteTrainLabelRequest,
    ) -> vcs_20200515_models.DeleteTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_train_label_with_options(request, runtime)

    async def delete_train_label_async(
        self,
        request: vcs_20200515_models.DeleteTrainLabelRequest,
    ) -> vcs_20200515_models.DeleteTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_train_label_with_options_async(request, runtime)

    def stop_deploy_with_options(
        self,
        request: vcs_20200515_models.StopDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StopDeployResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StopDeployResponse().from_map(
            self.do_rpcrequest('StopDeploy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_deploy_with_options_async(
        self,
        request: vcs_20200515_models.StopDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StopDeployResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StopDeployResponse().from_map(
            await self.do_rpcrequest_async('StopDeploy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_deploy(
        self,
        request: vcs_20200515_models.StopDeployRequest,
    ) -> vcs_20200515_models.StopDeployResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_deploy_with_options(request, runtime)

    async def stop_deploy_async(
        self,
        request: vcs_20200515_models.StopDeployRequest,
    ) -> vcs_20200515_models.StopDeployResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_deploy_with_options_async(request, runtime)

    def stop_monitor_with_options(
        self,
        request: vcs_20200515_models.StopMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StopMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StopMonitorResponse().from_map(
            self.do_rpcrequest('StopMonitor', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_monitor_with_options_async(
        self,
        request: vcs_20200515_models.StopMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StopMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StopMonitorResponse().from_map(
            await self.do_rpcrequest_async('StopMonitor', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_monitor(
        self,
        request: vcs_20200515_models.StopMonitorRequest,
    ) -> vcs_20200515_models.StopMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_monitor_with_options(request, runtime)

    async def stop_monitor_async(
        self,
        request: vcs_20200515_models.StopMonitorRequest,
    ) -> vcs_20200515_models.StopMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_monitor_with_options_async(request, runtime)

    def get_profile_list_with_options(
        self,
        tmp_req: vcs_20200515_models.GetProfileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetProfileListResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.GetProfileListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.person_id_list):
            request.person_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id_list, 'PersonIdList', 'json')
        if not UtilClient.is_unset(tmp_req.profile_id_list):
            request.profile_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.profile_id_list, 'ProfileIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetProfileListResponse().from_map(
            self.do_rpcrequest('GetProfileList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_profile_list_with_options_async(
        self,
        tmp_req: vcs_20200515_models.GetProfileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetProfileListResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.GetProfileListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.person_id_list):
            request.person_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id_list, 'PersonIdList', 'json')
        if not UtilClient.is_unset(tmp_req.profile_id_list):
            request.profile_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.profile_id_list, 'ProfileIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetProfileListResponse().from_map(
            await self.do_rpcrequest_async('GetProfileList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_profile_list(
        self,
        request: vcs_20200515_models.GetProfileListRequest,
    ) -> vcs_20200515_models.GetProfileListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_profile_list_with_options(request, runtime)

    async def get_profile_list_async(
        self,
        request: vcs_20200515_models.GetProfileListRequest,
    ) -> vcs_20200515_models.GetProfileListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_profile_list_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: vcs_20200515_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteDataSourceResponse().from_map(
            self.do_rpcrequest('DeleteDataSource', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: vcs_20200515_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteDataSourceResponse().from_map(
            await self.do_rpcrequest_async('DeleteDataSource', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_source(
        self,
        request: vcs_20200515_models.DeleteDataSourceRequest,
    ) -> vcs_20200515_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: vcs_20200515_models.DeleteDataSourceRequest,
    ) -> vcs_20200515_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def get_video_compose_result_with_options(
        self,
        request: vcs_20200515_models.GetVideoComposeResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetVideoComposeResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetVideoComposeResultResponse().from_map(
            self.do_rpcrequest('GetVideoComposeResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_compose_result_with_options_async(
        self,
        request: vcs_20200515_models.GetVideoComposeResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetVideoComposeResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetVideoComposeResultResponse().from_map(
            await self.do_rpcrequest_async('GetVideoComposeResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_compose_result(
        self,
        request: vcs_20200515_models.GetVideoComposeResultRequest,
    ) -> vcs_20200515_models.GetVideoComposeResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_compose_result_with_options(request, runtime)

    async def get_video_compose_result_async(
        self,
        request: vcs_20200515_models.GetVideoComposeResultRequest,
    ) -> vcs_20200515_models.GetVideoComposeResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_compose_result_with_options_async(request, runtime)

    def list_face_algorithm_results_with_options(
        self,
        request: vcs_20200515_models.ListFaceAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListFaceAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListFaceAlgorithmResultsResponse().from_map(
            self.do_rpcrequest('ListFaceAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_algorithm_results_with_options_async(
        self,
        request: vcs_20200515_models.ListFaceAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListFaceAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListFaceAlgorithmResultsResponse().from_map(
            await self.do_rpcrequest_async('ListFaceAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_algorithm_results(
        self,
        request: vcs_20200515_models.ListFaceAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListFaceAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_algorithm_results_with_options(request, runtime)

    async def list_face_algorithm_results_async(
        self,
        request: vcs_20200515_models.ListFaceAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListFaceAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_algorithm_results_with_options_async(request, runtime)

    def get_face_options_with_options(
        self,
        request: vcs_20200515_models.GetFaceOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetFaceOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetFaceOptionsResponse().from_map(
            self.do_rpcrequest('GetFaceOptions', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_face_options_with_options_async(
        self,
        request: vcs_20200515_models.GetFaceOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetFaceOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetFaceOptionsResponse().from_map(
            await self.do_rpcrequest_async('GetFaceOptions', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_face_options(
        self,
        request: vcs_20200515_models.GetFaceOptionsRequest,
    ) -> vcs_20200515_models.GetFaceOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_face_options_with_options(request, runtime)

    async def get_face_options_async(
        self,
        request: vcs_20200515_models.GetFaceOptionsRequest,
    ) -> vcs_20200515_models.GetFaceOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_face_options_with_options_async(request, runtime)

    def get_profile_detail_with_options(
        self,
        request: vcs_20200515_models.GetProfileDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetProfileDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetProfileDetailResponse().from_map(
            self.do_rpcrequest('GetProfileDetail', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_profile_detail_with_options_async(
        self,
        request: vcs_20200515_models.GetProfileDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetProfileDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetProfileDetailResponse().from_map(
            await self.do_rpcrequest_async('GetProfileDetail', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_profile_detail(
        self,
        request: vcs_20200515_models.GetProfileDetailRequest,
    ) -> vcs_20200515_models.GetProfileDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_profile_detail_with_options(request, runtime)

    async def get_profile_detail_async(
        self,
        request: vcs_20200515_models.GetProfileDetailRequest,
    ) -> vcs_20200515_models.GetProfileDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_profile_detail_with_options_async(request, runtime)

    def create_device_with_options(
        self,
        request: vcs_20200515_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateDeviceResponse().from_map(
            self.do_rpcrequest('CreateDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_device_with_options_async(
        self,
        request: vcs_20200515_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateDeviceResponse().from_map(
            await self.do_rpcrequest_async('CreateDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device(
        self,
        request: vcs_20200515_models.CreateDeviceRequest,
    ) -> vcs_20200515_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    async def create_device_async(
        self,
        request: vcs_20200515_models.CreateDeviceRequest,
    ) -> vcs_20200515_models.CreateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_device_with_options_async(request, runtime)

    def create_marker_with_options(
        self,
        request: vcs_20200515_models.CreateMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateMarkerResponse().from_map(
            self.do_rpcrequest('CreateMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_marker_with_options_async(
        self,
        request: vcs_20200515_models.CreateMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateMarkerResponse().from_map(
            await self.do_rpcrequest_async('CreateMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_marker(
        self,
        request: vcs_20200515_models.CreateMarkerRequest,
    ) -> vcs_20200515_models.CreateMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_marker_with_options(request, runtime)

    async def create_marker_async(
        self,
        request: vcs_20200515_models.CreateMarkerRequest,
    ) -> vcs_20200515_models.CreateMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_marker_with_options_async(request, runtime)

    def create_corp_with_options(
        self,
        request: vcs_20200515_models.CreateCorpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateCorpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateCorpResponse().from_map(
            self.do_rpcrequest('CreateCorp', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_corp_with_options_async(
        self,
        request: vcs_20200515_models.CreateCorpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateCorpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateCorpResponse().from_map(
            await self.do_rpcrequest_async('CreateCorp', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_corp(
        self,
        request: vcs_20200515_models.CreateCorpRequest,
    ) -> vcs_20200515_models.CreateCorpResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_corp_with_options(request, runtime)

    async def create_corp_async(
        self,
        request: vcs_20200515_models.CreateCorpRequest,
    ) -> vcs_20200515_models.CreateCorpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_corp_with_options_async(request, runtime)

    def update_profile_with_options(
        self,
        request: vcs_20200515_models.UpdateProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateProfileResponse().from_map(
            self.do_rpcrequest('UpdateProfile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_profile_with_options_async(
        self,
        request: vcs_20200515_models.UpdateProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateProfileResponse().from_map(
            await self.do_rpcrequest_async('UpdateProfile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_profile(
        self,
        request: vcs_20200515_models.UpdateProfileRequest,
    ) -> vcs_20200515_models.UpdateProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_profile_with_options(request, runtime)

    async def update_profile_async(
        self,
        request: vcs_20200515_models.UpdateProfileRequest,
    ) -> vcs_20200515_models.UpdateProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_profile_with_options_async(request, runtime)

    def get_device_capture_strategy_with_options(
        self,
        request: vcs_20200515_models.GetDeviceCaptureStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceCaptureStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceCaptureStrategyResponse().from_map(
            self.do_rpcrequest('GetDeviceCaptureStrategy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_capture_strategy_with_options_async(
        self,
        request: vcs_20200515_models.GetDeviceCaptureStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceCaptureStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceCaptureStrategyResponse().from_map(
            await self.do_rpcrequest_async('GetDeviceCaptureStrategy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_capture_strategy(
        self,
        request: vcs_20200515_models.GetDeviceCaptureStrategyRequest,
    ) -> vcs_20200515_models.GetDeviceCaptureStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_capture_strategy_with_options(request, runtime)

    async def get_device_capture_strategy_async(
        self,
        request: vcs_20200515_models.GetDeviceCaptureStrategyRequest,
    ) -> vcs_20200515_models.GetDeviceCaptureStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_capture_strategy_with_options_async(request, runtime)

    def start_train_with_options(
        self,
        request: vcs_20200515_models.StartTrainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StartTrainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StartTrainResponse().from_map(
            self.do_rpcrequest('StartTrain', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_train_with_options_async(
        self,
        request: vcs_20200515_models.StartTrainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StartTrainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StartTrainResponse().from_map(
            await self.do_rpcrequest_async('StartTrain', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_train(
        self,
        request: vcs_20200515_models.StartTrainRequest,
    ) -> vcs_20200515_models.StartTrainResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_train_with_options(request, runtime)

    async def start_train_async(
        self,
        request: vcs_20200515_models.StartTrainRequest,
    ) -> vcs_20200515_models.StartTrainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_train_with_options_async(request, runtime)

    def delete_video_summary_task_with_options(
        self,
        request: vcs_20200515_models.DeleteVideoSummaryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteVideoSummaryTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteVideoSummaryTaskResponse().from_map(
            self.do_rpcrequest('DeleteVideoSummaryTask', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_video_summary_task_with_options_async(
        self,
        request: vcs_20200515_models.DeleteVideoSummaryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteVideoSummaryTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteVideoSummaryTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteVideoSummaryTask', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_video_summary_task(
        self,
        request: vcs_20200515_models.DeleteVideoSummaryTaskRequest,
    ) -> vcs_20200515_models.DeleteVideoSummaryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_video_summary_task_with_options(request, runtime)

    async def delete_video_summary_task_async(
        self,
        request: vcs_20200515_models.DeleteVideoSummaryTaskRequest,
    ) -> vcs_20200515_models.DeleteVideoSummaryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_video_summary_task_with_options_async(request, runtime)

    def unbind_user_with_options(
        self,
        request: vcs_20200515_models.UnbindUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UnbindUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UnbindUserResponse().from_map(
            self.do_rpcrequest('UnbindUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_user_with_options_async(
        self,
        request: vcs_20200515_models.UnbindUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UnbindUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UnbindUserResponse().from_map(
            await self.do_rpcrequest_async('UnbindUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_user(
        self,
        request: vcs_20200515_models.UnbindUserRequest,
    ) -> vcs_20200515_models.UnbindUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_user_with_options(request, runtime)

    async def unbind_user_async(
        self,
        request: vcs_20200515_models.UnbindUserRequest,
    ) -> vcs_20200515_models.UnbindUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_user_with_options_async(request, runtime)

    def list_persons_with_options(
        self,
        request: vcs_20200515_models.ListPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonsResponse().from_map(
            self.do_rpcrequest('ListPersons', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_persons_with_options_async(
        self,
        request: vcs_20200515_models.ListPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonsResponse().from_map(
            await self.do_rpcrequest_async('ListPersons', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_persons(
        self,
        request: vcs_20200515_models.ListPersonsRequest,
    ) -> vcs_20200515_models.ListPersonsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_persons_with_options(request, runtime)

    async def list_persons_async(
        self,
        request: vcs_20200515_models.ListPersonsRequest,
    ) -> vcs_20200515_models.ListPersonsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_persons_with_options_async(request, runtime)

    def list_motor_algorithm_results_with_options(
        self,
        request: vcs_20200515_models.ListMotorAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListMotorAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListMotorAlgorithmResultsResponse().from_map(
            self.do_rpcrequest('ListMotorAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_motor_algorithm_results_with_options_async(
        self,
        request: vcs_20200515_models.ListMotorAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListMotorAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListMotorAlgorithmResultsResponse().from_map(
            await self.do_rpcrequest_async('ListMotorAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_motor_algorithm_results(
        self,
        request: vcs_20200515_models.ListMotorAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListMotorAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_motor_algorithm_results_with_options(request, runtime)

    async def list_motor_algorithm_results_async(
        self,
        request: vcs_20200515_models.ListMotorAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListMotorAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_motor_algorithm_results_with_options_async(request, runtime)

    def list_person_trace_with_options(
        self,
        request: vcs_20200515_models.ListPersonTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonTraceResponse().from_map(
            self.do_rpcrequest('ListPersonTrace', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_trace_with_options_async(
        self,
        request: vcs_20200515_models.ListPersonTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonTraceResponse().from_map(
            await self.do_rpcrequest_async('ListPersonTrace', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_trace(
        self,
        request: vcs_20200515_models.ListPersonTraceRequest,
    ) -> vcs_20200515_models.ListPersonTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_trace_with_options(request, runtime)

    async def list_person_trace_async(
        self,
        request: vcs_20200515_models.ListPersonTraceRequest,
    ) -> vcs_20200515_models.ListPersonTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_trace_with_options_async(request, runtime)

    def list_devices_with_options(
        self,
        request: vcs_20200515_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListDevicesResponse().from_map(
            self.do_rpcrequest('ListDevices', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_devices_with_options_async(
        self,
        request: vcs_20200515_models.ListDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListDevicesResponse().from_map(
            await self.do_rpcrequest_async('ListDevices', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_devices(
        self,
        request: vcs_20200515_models.ListDevicesRequest,
    ) -> vcs_20200515_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    async def list_devices_async(
        self,
        request: vcs_20200515_models.ListDevicesRequest,
    ) -> vcs_20200515_models.ListDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_devices_with_options_async(request, runtime)

    def report_device_capacity_with_options(
        self,
        request: vcs_20200515_models.ReportDeviceCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ReportDeviceCapacityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ReportDeviceCapacityResponse().from_map(
            self.do_rpcrequest('ReportDeviceCapacity', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_device_capacity_with_options_async(
        self,
        request: vcs_20200515_models.ReportDeviceCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ReportDeviceCapacityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ReportDeviceCapacityResponse().from_map(
            await self.do_rpcrequest_async('ReportDeviceCapacity', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_device_capacity(
        self,
        request: vcs_20200515_models.ReportDeviceCapacityRequest,
    ) -> vcs_20200515_models.ReportDeviceCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_device_capacity_with_options(request, runtime)

    async def report_device_capacity_async(
        self,
        request: vcs_20200515_models.ReportDeviceCapacityRequest,
    ) -> vcs_20200515_models.ReportDeviceCapacityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_device_capacity_with_options_async(request, runtime)

    def delete_marker_with_options(
        self,
        request: vcs_20200515_models.DeleteMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteMarkerResponse().from_map(
            self.do_rpcrequest('DeleteMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_marker_with_options_async(
        self,
        request: vcs_20200515_models.DeleteMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteMarkerResponse().from_map(
            await self.do_rpcrequest_async('DeleteMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_marker(
        self,
        request: vcs_20200515_models.DeleteMarkerRequest,
    ) -> vcs_20200515_models.DeleteMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_marker_with_options(request, runtime)

    async def delete_marker_async(
        self,
        request: vcs_20200515_models.DeleteMarkerRequest,
    ) -> vcs_20200515_models.DeleteMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_marker_with_options_async(request, runtime)

    def list_person_trace_details_with_options(
        self,
        request: vcs_20200515_models.ListPersonTraceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonTraceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonTraceDetailsResponse().from_map(
            self.do_rpcrequest('ListPersonTraceDetails', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_trace_details_with_options_async(
        self,
        request: vcs_20200515_models.ListPersonTraceDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonTraceDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonTraceDetailsResponse().from_map(
            await self.do_rpcrequest_async('ListPersonTraceDetails', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_trace_details(
        self,
        request: vcs_20200515_models.ListPersonTraceDetailsRequest,
    ) -> vcs_20200515_models.ListPersonTraceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_trace_details_with_options(request, runtime)

    async def list_person_trace_details_async(
        self,
        request: vcs_20200515_models.ListPersonTraceDetailsRequest,
    ) -> vcs_20200515_models.ListPersonTraceDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_trace_details_with_options_async(request, runtime)

    def list_metrics_with_options(
        self,
        request: vcs_20200515_models.ListMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListMetricsResponse().from_map(
            self.do_rpcrequest('ListMetrics', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_metrics_with_options_async(
        self,
        request: vcs_20200515_models.ListMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListMetricsResponse().from_map(
            await self.do_rpcrequest_async('ListMetrics', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_metrics(
        self,
        request: vcs_20200515_models.ListMetricsRequest,
    ) -> vcs_20200515_models.ListMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_metrics_with_options(request, runtime)

    async def list_metrics_async(
        self,
        request: vcs_20200515_models.ListMetricsRequest,
    ) -> vcs_20200515_models.ListMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_metrics_with_options_async(request, runtime)

    def delete_nvrdevice_with_options(
        self,
        request: vcs_20200515_models.DeleteNVRDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteNVRDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteNVRDeviceResponse().from_map(
            self.do_rpcrequest('DeleteNVRDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nvrdevice_with_options_async(
        self,
        request: vcs_20200515_models.DeleteNVRDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteNVRDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteNVRDeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteNVRDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nvrdevice(
        self,
        request: vcs_20200515_models.DeleteNVRDeviceRequest,
    ) -> vcs_20200515_models.DeleteNVRDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nvrdevice_with_options(request, runtime)

    async def delete_nvrdevice_async(
        self,
        request: vcs_20200515_models.DeleteNVRDeviceRequest,
    ) -> vcs_20200515_models.DeleteNVRDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nvrdevice_with_options_async(request, runtime)

    def add_profile_catalog_with_options(
        self,
        request: vcs_20200515_models.AddProfileCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddProfileCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddProfileCatalogResponse().from_map(
            self.do_rpcrequest('AddProfileCatalog', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_profile_catalog_with_options_async(
        self,
        request: vcs_20200515_models.AddProfileCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddProfileCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddProfileCatalogResponse().from_map(
            await self.do_rpcrequest_async('AddProfileCatalog', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_profile_catalog(
        self,
        request: vcs_20200515_models.AddProfileCatalogRequest,
    ) -> vcs_20200515_models.AddProfileCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_profile_catalog_with_options(request, runtime)

    async def add_profile_catalog_async(
        self,
        request: vcs_20200515_models.AddProfileCatalogRequest,
    ) -> vcs_20200515_models.AddProfileCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_profile_catalog_with_options_async(request, runtime)

    def sample_list_with_options(
        self,
        request: vcs_20200515_models.SampleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SampleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SampleListResponse().from_map(
            self.do_rpcrequest('SampleList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sample_list_with_options_async(
        self,
        request: vcs_20200515_models.SampleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SampleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SampleListResponse().from_map(
            await self.do_rpcrequest_async('SampleList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sample_list(
        self,
        request: vcs_20200515_models.SampleListRequest,
    ) -> vcs_20200515_models.SampleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.sample_list_with_options(request, runtime)

    async def sample_list_async(
        self,
        request: vcs_20200515_models.SampleListRequest,
    ) -> vcs_20200515_models.SampleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sample_list_with_options_async(request, runtime)

    def recognize_face_quality_with_options(
        self,
        request: vcs_20200515_models.RecognizeFaceQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RecognizeFaceQualityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RecognizeFaceQualityResponse().from_map(
            self.do_rpcrequest('RecognizeFaceQuality', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_face_quality_with_options_async(
        self,
        request: vcs_20200515_models.RecognizeFaceQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RecognizeFaceQualityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RecognizeFaceQualityResponse().from_map(
            await self.do_rpcrequest_async('RecognizeFaceQuality', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_face_quality(
        self,
        request: vcs_20200515_models.RecognizeFaceQualityRequest,
    ) -> vcs_20200515_models.RecognizeFaceQualityResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_face_quality_with_options(request, runtime)

    async def recognize_face_quality_async(
        self,
        request: vcs_20200515_models.RecognizeFaceQualityRequest,
    ) -> vcs_20200515_models.RecognizeFaceQualityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_face_quality_with_options_async(request, runtime)

    def get_train_algorithm_with_options(
        self,
        request: vcs_20200515_models.GetTrainAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetTrainAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetTrainAlgorithmResponse().from_map(
            self.do_rpcrequest('GetTrainAlgorithm', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_train_algorithm_with_options_async(
        self,
        request: vcs_20200515_models.GetTrainAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetTrainAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetTrainAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('GetTrainAlgorithm', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_train_algorithm(
        self,
        request: vcs_20200515_models.GetTrainAlgorithmRequest,
    ) -> vcs_20200515_models.GetTrainAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_train_algorithm_with_options(request, runtime)

    async def get_train_algorithm_async(
        self,
        request: vcs_20200515_models.GetTrainAlgorithmRequest,
    ) -> vcs_20200515_models.GetTrainAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_train_algorithm_with_options_async(request, runtime)

    def delete_train_algorithm_with_options(
        self,
        request: vcs_20200515_models.DeleteTrainAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteTrainAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteTrainAlgorithmResponse().from_map(
            self.do_rpcrequest('DeleteTrainAlgorithm', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_train_algorithm_with_options_async(
        self,
        request: vcs_20200515_models.DeleteTrainAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteTrainAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteTrainAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('DeleteTrainAlgorithm', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_train_algorithm(
        self,
        request: vcs_20200515_models.DeleteTrainAlgorithmRequest,
    ) -> vcs_20200515_models.DeleteTrainAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_train_algorithm_with_options(request, runtime)

    async def delete_train_algorithm_async(
        self,
        request: vcs_20200515_models.DeleteTrainAlgorithmRequest,
    ) -> vcs_20200515_models.DeleteTrainAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_train_algorithm_with_options_async(request, runtime)

    def update_marker_with_options(
        self,
        request: vcs_20200515_models.UpdateMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateMarkerResponse().from_map(
            self.do_rpcrequest('UpdateMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_marker_with_options_async(
        self,
        request: vcs_20200515_models.UpdateMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateMarkerResponse().from_map(
            await self.do_rpcrequest_async('UpdateMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_marker(
        self,
        request: vcs_20200515_models.UpdateMarkerRequest,
    ) -> vcs_20200515_models.UpdateMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_marker_with_options(request, runtime)

    async def update_marker_async(
        self,
        request: vcs_20200515_models.UpdateMarkerRequest,
    ) -> vcs_20200515_models.UpdateMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_marker_with_options_async(request, runtime)

    def list_corp_groups_with_options(
        self,
        request: vcs_20200515_models.ListCorpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpGroupsResponse().from_map(
            self.do_rpcrequest('ListCorpGroups', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_corp_groups_with_options_async(
        self,
        request: vcs_20200515_models.ListCorpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListCorpGroups', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corp_groups(
        self,
        request: vcs_20200515_models.ListCorpGroupsRequest,
    ) -> vcs_20200515_models.ListCorpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_corp_groups_with_options(request, runtime)

    async def list_corp_groups_async(
        self,
        request: vcs_20200515_models.ListCorpGroupsRequest,
    ) -> vcs_20200515_models.ListCorpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_corp_groups_with_options_async(request, runtime)

    def stop_train_with_options(
        self,
        request: vcs_20200515_models.StopTrainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StopTrainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StopTrainResponse().from_map(
            self.do_rpcrequest('StopTrain', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_train_with_options_async(
        self,
        request: vcs_20200515_models.StopTrainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.StopTrainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.StopTrainResponse().from_map(
            await self.do_rpcrequest_async('StopTrain', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_train(
        self,
        request: vcs_20200515_models.StopTrainRequest,
    ) -> vcs_20200515_models.StopTrainResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_train_with_options(request, runtime)

    async def stop_train_async(
        self,
        request: vcs_20200515_models.StopTrainRequest,
    ) -> vcs_20200515_models.StopTrainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_train_with_options_async(request, runtime)

    def describe_devices_with_options(
        self,
        request: vcs_20200515_models.DescribeDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DescribeDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DescribeDevicesResponse().from_map(
            self.do_rpcrequest('DescribeDevices', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_devices_with_options_async(
        self,
        request: vcs_20200515_models.DescribeDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DescribeDevicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DescribeDevicesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDevices', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_devices(
        self,
        request: vcs_20200515_models.DescribeDevicesRequest,
    ) -> vcs_20200515_models.DescribeDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    async def describe_devices_async(
        self,
        request: vcs_20200515_models.DescribeDevicesRequest,
    ) -> vcs_20200515_models.DescribeDevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_devices_with_options_async(request, runtime)

    def get_device_video_url_with_options(
        self,
        request: vcs_20200515_models.GetDeviceVideoUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceVideoUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceVideoUrlResponse().from_map(
            self.do_rpcrequest('GetDeviceVideoUrl', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_video_url_with_options_async(
        self,
        request: vcs_20200515_models.GetDeviceVideoUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceVideoUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceVideoUrlResponse().from_map(
            await self.do_rpcrequest_async('GetDeviceVideoUrl', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_video_url(
        self,
        request: vcs_20200515_models.GetDeviceVideoUrlRequest,
    ) -> vcs_20200515_models.GetDeviceVideoUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_video_url_with_options(request, runtime)

    async def get_device_video_url_async(
        self,
        request: vcs_20200515_models.GetDeviceVideoUrlRequest,
    ) -> vcs_20200515_models.GetDeviceVideoUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_video_url_with_options_async(request, runtime)

    def list_corps_with_options(
        self,
        request: vcs_20200515_models.ListCorpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpsResponse().from_map(
            self.do_rpcrequest('ListCorps', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_corps_with_options_async(
        self,
        request: vcs_20200515_models.ListCorpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpsResponse().from_map(
            await self.do_rpcrequest_async('ListCorps', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corps(
        self,
        request: vcs_20200515_models.ListCorpsRequest,
    ) -> vcs_20200515_models.ListCorpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_corps_with_options(request, runtime)

    async def list_corps_async(
        self,
        request: vcs_20200515_models.ListCorpsRequest,
    ) -> vcs_20200515_models.ListCorpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_corps_with_options_async(request, runtime)

    def list_body_algorithm_results_with_options(
        self,
        request: vcs_20200515_models.ListBodyAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListBodyAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListBodyAlgorithmResultsResponse().from_map(
            self.do_rpcrequest('ListBodyAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_body_algorithm_results_with_options_async(
        self,
        request: vcs_20200515_models.ListBodyAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListBodyAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListBodyAlgorithmResultsResponse().from_map(
            await self.do_rpcrequest_async('ListBodyAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_body_algorithm_results(
        self,
        request: vcs_20200515_models.ListBodyAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListBodyAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_body_algorithm_results_with_options(request, runtime)

    async def list_body_algorithm_results_async(
        self,
        request: vcs_20200515_models.ListBodyAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListBodyAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_body_algorithm_results_with_options_async(request, runtime)

    def get_device_config_with_options(
        self,
        request: vcs_20200515_models.GetDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceConfigResponse().from_map(
            self.do_rpcrequest('GetDeviceConfig', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_config_with_options_async(
        self,
        request: vcs_20200515_models.GetDeviceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceConfigResponse().from_map(
            await self.do_rpcrequest_async('GetDeviceConfig', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_config(
        self,
        request: vcs_20200515_models.GetDeviceConfigRequest,
    ) -> vcs_20200515_models.GetDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_with_options(request, runtime)

    async def get_device_config_async(
        self,
        request: vcs_20200515_models.GetDeviceConfigRequest,
    ) -> vcs_20200515_models.GetDeviceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_config_with_options_async(request, runtime)

    def update_corp_with_options(
        self,
        request: vcs_20200515_models.UpdateCorpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateCorpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateCorpResponse().from_map(
            self.do_rpcrequest('UpdateCorp', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_corp_with_options_async(
        self,
        request: vcs_20200515_models.UpdateCorpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateCorpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateCorpResponse().from_map(
            await self.do_rpcrequest_async('UpdateCorp', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_corp(
        self,
        request: vcs_20200515_models.UpdateCorpRequest,
    ) -> vcs_20200515_models.UpdateCorpResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_corp_with_options(request, runtime)

    async def update_corp_async(
        self,
        request: vcs_20200515_models.UpdateCorpRequest,
    ) -> vcs_20200515_models.UpdateCorpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_corp_with_options_async(request, runtime)

    def create_corp_group_with_options(
        self,
        request: vcs_20200515_models.CreateCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateCorpGroupResponse().from_map(
            self.do_rpcrequest('CreateCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_corp_group_with_options_async(
        self,
        request: vcs_20200515_models.CreateCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateCorpGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_corp_group(
        self,
        request: vcs_20200515_models.CreateCorpGroupRequest,
    ) -> vcs_20200515_models.CreateCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_corp_group_with_options(request, runtime)

    async def create_corp_group_async(
        self,
        request: vcs_20200515_models.CreateCorpGroupRequest,
    ) -> vcs_20200515_models.CreateCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_corp_group_with_options_async(request, runtime)

    def add_device_with_options(
        self,
        request: vcs_20200515_models.AddDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddDeviceResponse().from_map(
            self.do_rpcrequest('AddDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_device_with_options_async(
        self,
        request: vcs_20200515_models.AddDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddDeviceResponse().from_map(
            await self.do_rpcrequest_async('AddDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_device(
        self,
        request: vcs_20200515_models.AddDeviceRequest,
    ) -> vcs_20200515_models.AddDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_device_with_options(request, runtime)

    async def add_device_async(
        self,
        request: vcs_20200515_models.AddDeviceRequest,
    ) -> vcs_20200515_models.AddDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_device_with_options_async(request, runtime)

    def get_person_list_with_options(
        self,
        tmp_req: vcs_20200515_models.GetPersonListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetPersonListResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.GetPersonListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id_list):
            request.corp_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id_list, 'CorpIdList', 'json')
        if not UtilClient.is_unset(tmp_req.person_id_list):
            request.person_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id_list, 'PersonIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetPersonListResponse().from_map(
            self.do_rpcrequest('GetPersonList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_person_list_with_options_async(
        self,
        tmp_req: vcs_20200515_models.GetPersonListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetPersonListResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.GetPersonListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id_list):
            request.corp_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id_list, 'CorpIdList', 'json')
        if not UtilClient.is_unset(tmp_req.person_id_list):
            request.person_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id_list, 'PersonIdList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetPersonListResponse().from_map(
            await self.do_rpcrequest_async('GetPersonList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_person_list(
        self,
        request: vcs_20200515_models.GetPersonListRequest,
    ) -> vcs_20200515_models.GetPersonListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_person_list_with_options(request, runtime)

    async def get_person_list_async(
        self,
        request: vcs_20200515_models.GetPersonListRequest,
    ) -> vcs_20200515_models.GetPersonListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_person_list_with_options_async(request, runtime)

    def create_train_label_with_options(
        self,
        request: vcs_20200515_models.CreateTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateTrainLabelResponse().from_map(
            self.do_rpcrequest('CreateTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_train_label_with_options_async(
        self,
        request: vcs_20200515_models.CreateTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateTrainLabelResponse().from_map(
            await self.do_rpcrequest_async('CreateTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_train_label(
        self,
        request: vcs_20200515_models.CreateTrainLabelRequest,
    ) -> vcs_20200515_models.CreateTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_train_label_with_options(request, runtime)

    async def create_train_label_async(
        self,
        request: vcs_20200515_models.CreateTrainLabelRequest,
    ) -> vcs_20200515_models.CreateTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_train_label_with_options_async(request, runtime)

    def update_profile_catalog_with_options(
        self,
        request: vcs_20200515_models.UpdateProfileCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateProfileCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateProfileCatalogResponse().from_map(
            self.do_rpcrequest('UpdateProfileCatalog', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_profile_catalog_with_options_async(
        self,
        request: vcs_20200515_models.UpdateProfileCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateProfileCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateProfileCatalogResponse().from_map(
            await self.do_rpcrequest_async('UpdateProfileCatalog', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_profile_catalog(
        self,
        request: vcs_20200515_models.UpdateProfileCatalogRequest,
    ) -> vcs_20200515_models.UpdateProfileCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_profile_catalog_with_options(request, runtime)

    async def update_profile_catalog_async(
        self,
        request: vcs_20200515_models.UpdateProfileCatalogRequest,
    ) -> vcs_20200515_models.UpdateProfileCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_profile_catalog_with_options_async(request, runtime)

    def list_person_visit_count_with_options(
        self,
        request: vcs_20200515_models.ListPersonVisitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonVisitCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonVisitCountResponse().from_map(
            self.do_rpcrequest('ListPersonVisitCount', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_person_visit_count_with_options_async(
        self,
        request: vcs_20200515_models.ListPersonVisitCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListPersonVisitCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListPersonVisitCountResponse().from_map(
            await self.do_rpcrequest_async('ListPersonVisitCount', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_person_visit_count(
        self,
        request: vcs_20200515_models.ListPersonVisitCountRequest,
    ) -> vcs_20200515_models.ListPersonVisitCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_person_visit_count_with_options(request, runtime)

    async def list_person_visit_count_async(
        self,
        request: vcs_20200515_models.ListPersonVisitCountRequest,
    ) -> vcs_20200515_models.ListPersonVisitCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_person_visit_count_with_options_async(request, runtime)

    def update_sample_with_options(
        self,
        request: vcs_20200515_models.UpdateSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateSampleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateSampleResponse().from_map(
            self.do_rpcrequest('UpdateSample', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_sample_with_options_async(
        self,
        request: vcs_20200515_models.UpdateSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateSampleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateSampleResponse().from_map(
            await self.do_rpcrequest_async('UpdateSample', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_sample(
        self,
        request: vcs_20200515_models.UpdateSampleRequest,
    ) -> vcs_20200515_models.UpdateSampleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sample_with_options(request, runtime)

    async def update_sample_async(
        self,
        request: vcs_20200515_models.UpdateSampleRequest,
    ) -> vcs_20200515_models.UpdateSampleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sample_with_options_async(request, runtime)

    def create_video_summary_task_with_options(
        self,
        request: vcs_20200515_models.CreateVideoSummaryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateVideoSummaryTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateVideoSummaryTaskResponse().from_map(
            self.do_rpcrequest('CreateVideoSummaryTask', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_video_summary_task_with_options_async(
        self,
        request: vcs_20200515_models.CreateVideoSummaryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateVideoSummaryTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateVideoSummaryTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateVideoSummaryTask', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_video_summary_task(
        self,
        request: vcs_20200515_models.CreateVideoSummaryTaskRequest,
    ) -> vcs_20200515_models.CreateVideoSummaryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_video_summary_task_with_options(request, runtime)

    async def create_video_summary_task_async(
        self,
        request: vcs_20200515_models.CreateVideoSummaryTaskRequest,
    ) -> vcs_20200515_models.CreateVideoSummaryTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_summary_task_with_options_async(request, runtime)

    def list_corp_metrics_with_options(
        self,
        request: vcs_20200515_models.ListCorpMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpMetricsResponse().from_map(
            self.do_rpcrequest('ListCorpMetrics', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_corp_metrics_with_options_async(
        self,
        request: vcs_20200515_models.ListCorpMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListCorpMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListCorpMetricsResponse().from_map(
            await self.do_rpcrequest_async('ListCorpMetrics', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_corp_metrics(
        self,
        request: vcs_20200515_models.ListCorpMetricsRequest,
    ) -> vcs_20200515_models.ListCorpMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_corp_metrics_with_options(request, runtime)

    async def list_corp_metrics_async(
        self,
        request: vcs_20200515_models.ListCorpMetricsRequest,
    ) -> vcs_20200515_models.ListCorpMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_corp_metrics_with_options_async(request, runtime)

    def list_event_algorithm_details_with_options(
        self,
        request: vcs_20200515_models.ListEventAlgorithmDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListEventAlgorithmDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListEventAlgorithmDetailsResponse().from_map(
            self.do_rpcrequest('ListEventAlgorithmDetails', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_event_algorithm_details_with_options_async(
        self,
        request: vcs_20200515_models.ListEventAlgorithmDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListEventAlgorithmDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListEventAlgorithmDetailsResponse().from_map(
            await self.do_rpcrequest_async('ListEventAlgorithmDetails', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_event_algorithm_details(
        self,
        request: vcs_20200515_models.ListEventAlgorithmDetailsRequest,
    ) -> vcs_20200515_models.ListEventAlgorithmDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_algorithm_details_with_options(request, runtime)

    async def list_event_algorithm_details_async(
        self,
        request: vcs_20200515_models.ListEventAlgorithmDetailsRequest,
    ) -> vcs_20200515_models.ListEventAlgorithmDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_algorithm_details_with_options_async(request, runtime)

    def get_catalog_list_with_options(
        self,
        request: vcs_20200515_models.GetCatalogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetCatalogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetCatalogListResponse().from_map(
            self.do_rpcrequest('GetCatalogList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_catalog_list_with_options_async(
        self,
        request: vcs_20200515_models.GetCatalogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetCatalogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetCatalogListResponse().from_map(
            await self.do_rpcrequest_async('GetCatalogList', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_catalog_list(
        self,
        request: vcs_20200515_models.GetCatalogListRequest,
    ) -> vcs_20200515_models.GetCatalogListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_catalog_list_with_options(request, runtime)

    async def get_catalog_list_async(
        self,
        request: vcs_20200515_models.GetCatalogListRequest,
    ) -> vcs_20200515_models.GetCatalogListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_catalog_list_with_options_async(request, runtime)

    def list_nvrdevice_with_options(
        self,
        request: vcs_20200515_models.ListNVRDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListNVRDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListNVRDeviceResponse().from_map(
            self.do_rpcrequest('ListNVRDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nvrdevice_with_options_async(
        self,
        request: vcs_20200515_models.ListNVRDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListNVRDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListNVRDeviceResponse().from_map(
            await self.do_rpcrequest_async('ListNVRDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nvrdevice(
        self,
        request: vcs_20200515_models.ListNVRDeviceRequest,
    ) -> vcs_20200515_models.ListNVRDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nvrdevice_with_options(request, runtime)

    async def list_nvrdevice_async(
        self,
        request: vcs_20200515_models.ListNVRDeviceRequest,
    ) -> vcs_20200515_models.ListNVRDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nvrdevice_with_options_async(request, runtime)

    def get_device_live_url_with_options(
        self,
        request: vcs_20200515_models.GetDeviceLiveUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceLiveUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceLiveUrlResponse().from_map(
            self.do_rpcrequest('GetDeviceLiveUrl', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_live_url_with_options_async(
        self,
        request: vcs_20200515_models.GetDeviceLiveUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetDeviceLiveUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetDeviceLiveUrlResponse().from_map(
            await self.do_rpcrequest_async('GetDeviceLiveUrl', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_live_url(
        self,
        request: vcs_20200515_models.GetDeviceLiveUrlRequest,
    ) -> vcs_20200515_models.GetDeviceLiveUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_live_url_with_options(request, runtime)

    async def get_device_live_url_async(
        self,
        request: vcs_20200515_models.GetDeviceLiveUrlRequest,
    ) -> vcs_20200515_models.GetDeviceLiveUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_live_url_with_options_async(request, runtime)

    def delete_corp_group_with_options(
        self,
        request: vcs_20200515_models.DeleteCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteCorpGroupResponse().from_map(
            self.do_rpcrequest('DeleteCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_corp_group_with_options_async(
        self,
        request: vcs_20200515_models.DeleteCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteCorpGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_corp_group(
        self,
        request: vcs_20200515_models.DeleteCorpGroupRequest,
    ) -> vcs_20200515_models.DeleteCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_corp_group_with_options(request, runtime)

    async def delete_corp_group_async(
        self,
        request: vcs_20200515_models.DeleteCorpGroupRequest,
    ) -> vcs_20200515_models.DeleteCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_corp_group_with_options_async(request, runtime)

    def update_train_algorithm_with_options(
        self,
        request: vcs_20200515_models.UpdateTrainAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateTrainAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateTrainAlgorithmResponse().from_map(
            self.do_rpcrequest('UpdateTrainAlgorithm', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_train_algorithm_with_options_async(
        self,
        request: vcs_20200515_models.UpdateTrainAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateTrainAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateTrainAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('UpdateTrainAlgorithm', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_train_algorithm(
        self,
        request: vcs_20200515_models.UpdateTrainAlgorithmRequest,
    ) -> vcs_20200515_models.UpdateTrainAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_train_algorithm_with_options(request, runtime)

    async def update_train_algorithm_async(
        self,
        request: vcs_20200515_models.UpdateTrainAlgorithmRequest,
    ) -> vcs_20200515_models.UpdateTrainAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_train_algorithm_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: vcs_20200515_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: vcs_20200515_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateUserResponse().from_map(
            await self.do_rpcrequest_async('CreateUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(
        self,
        request: vcs_20200515_models.CreateUserRequest,
    ) -> vcs_20200515_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: vcs_20200515_models.CreateUserRequest,
    ) -> vcs_20200515_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def list_algorithm_names_by_device_ids_with_options(
        self,
        request: vcs_20200515_models.ListAlgorithmNamesByDeviceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListAlgorithmNamesByDeviceIdsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return vcs_20200515_models.ListAlgorithmNamesByDeviceIdsResponse().from_map(
            self.do_rpcrequest('ListAlgorithmNamesByDeviceIds', '2020-05-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_algorithm_names_by_device_ids_with_options_async(
        self,
        request: vcs_20200515_models.ListAlgorithmNamesByDeviceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListAlgorithmNamesByDeviceIdsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return vcs_20200515_models.ListAlgorithmNamesByDeviceIdsResponse().from_map(
            await self.do_rpcrequest_async('ListAlgorithmNamesByDeviceIds', '2020-05-15', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_algorithm_names_by_device_ids(
        self,
        request: vcs_20200515_models.ListAlgorithmNamesByDeviceIdsRequest,
    ) -> vcs_20200515_models.ListAlgorithmNamesByDeviceIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_algorithm_names_by_device_ids_with_options(request, runtime)

    async def list_algorithm_names_by_device_ids_async(
        self,
        request: vcs_20200515_models.ListAlgorithmNamesByDeviceIdsRequest,
    ) -> vcs_20200515_models.ListAlgorithmNamesByDeviceIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_algorithm_names_by_device_ids_with_options_async(request, runtime)

    def add_data_source_with_options(
        self,
        request: vcs_20200515_models.AddDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddDataSourceResponse().from_map(
            self.do_rpcrequest('AddDataSource', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_data_source_with_options_async(
        self,
        request: vcs_20200515_models.AddDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddDataSourceResponse().from_map(
            await self.do_rpcrequest_async('AddDataSource', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_data_source(
        self,
        request: vcs_20200515_models.AddDataSourceRequest,
    ) -> vcs_20200515_models.AddDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_data_source_with_options(request, runtime)

    async def add_data_source_async(
        self,
        request: vcs_20200515_models.AddDataSourceRequest,
    ) -> vcs_20200515_models.AddDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_data_source_with_options_async(request, runtime)

    def unbind_corp_group_with_options(
        self,
        request: vcs_20200515_models.UnbindCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UnbindCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UnbindCorpGroupResponse().from_map(
            self.do_rpcrequest('UnbindCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_corp_group_with_options_async(
        self,
        request: vcs_20200515_models.UnbindCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UnbindCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UnbindCorpGroupResponse().from_map(
            await self.do_rpcrequest_async('UnbindCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_corp_group(
        self,
        request: vcs_20200515_models.UnbindCorpGroupRequest,
    ) -> vcs_20200515_models.UnbindCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_corp_group_with_options(request, runtime)

    async def unbind_corp_group_async(
        self,
        request: vcs_20200515_models.UnbindCorpGroupRequest,
    ) -> vcs_20200515_models.UnbindCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_corp_group_with_options_async(request, runtime)

    def upload_file_with_options(
        self,
        request: vcs_20200515_models.UploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UploadFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UploadFileResponse().from_map(
            self.do_rpcrequest('UploadFile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_file_with_options_async(
        self,
        request: vcs_20200515_models.UploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UploadFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UploadFileResponse().from_map(
            await self.do_rpcrequest_async('UploadFile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_file(
        self,
        request: vcs_20200515_models.UploadFileRequest,
    ) -> vcs_20200515_models.UploadFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_file_with_options(request, runtime)

    async def upload_file_async(
        self,
        request: vcs_20200515_models.UploadFileRequest,
    ) -> vcs_20200515_models.UploadFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_file_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: vcs_20200515_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: vcs_20200515_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateUserResponse().from_map(
            await self.do_rpcrequest_async('UpdateUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(
        self,
        request: vcs_20200515_models.UpdateUserRequest,
    ) -> vcs_20200515_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: vcs_20200515_models.UpdateUserRequest,
    ) -> vcs_20200515_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def get_train_algorith_with_options(
        self,
        request: vcs_20200515_models.GetTrainAlgorithRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetTrainAlgorithResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetTrainAlgorithResponse().from_map(
            self.do_rpcrequest('GetTrainAlgorith', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_train_algorith_with_options_async(
        self,
        request: vcs_20200515_models.GetTrainAlgorithRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetTrainAlgorithResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetTrainAlgorithResponse().from_map(
            await self.do_rpcrequest_async('GetTrainAlgorith', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_train_algorith(
        self,
        request: vcs_20200515_models.GetTrainAlgorithRequest,
    ) -> vcs_20200515_models.GetTrainAlgorithResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_train_algorith_with_options(request, runtime)

    async def get_train_algorith_async(
        self,
        request: vcs_20200515_models.GetTrainAlgorithRequest,
    ) -> vcs_20200515_models.GetTrainAlgorithResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_train_algorith_with_options_async(request, runtime)

    def get_video_summary_task_result_with_options(
        self,
        request: vcs_20200515_models.GetVideoSummaryTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetVideoSummaryTaskResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetVideoSummaryTaskResultResponse().from_map(
            self.do_rpcrequest('GetVideoSummaryTaskResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_summary_task_result_with_options_async(
        self,
        request: vcs_20200515_models.GetVideoSummaryTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetVideoSummaryTaskResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetVideoSummaryTaskResultResponse().from_map(
            await self.do_rpcrequest_async('GetVideoSummaryTaskResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_summary_task_result(
        self,
        request: vcs_20200515_models.GetVideoSummaryTaskResultRequest,
    ) -> vcs_20200515_models.GetVideoSummaryTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_summary_task_result_with_options(request, runtime)

    async def get_video_summary_task_result_async(
        self,
        request: vcs_20200515_models.GetVideoSummaryTaskResultRequest,
    ) -> vcs_20200515_models.GetVideoSummaryTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_summary_task_result_with_options_async(request, runtime)

    def list_device_groups_with_options(
        self,
        request: vcs_20200515_models.ListDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListDeviceGroupsResponse().from_map(
            self.do_rpcrequest('ListDeviceGroups', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_device_groups_with_options_async(
        self,
        request: vcs_20200515_models.ListDeviceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListDeviceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListDeviceGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListDeviceGroups', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_groups(
        self,
        request: vcs_20200515_models.ListDeviceGroupsRequest,
    ) -> vcs_20200515_models.ListDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_device_groups_with_options(request, runtime)

    async def list_device_groups_async(
        self,
        request: vcs_20200515_models.ListDeviceGroupsRequest,
    ) -> vcs_20200515_models.ListDeviceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_device_groups_with_options_async(request, runtime)

    def get_user_detail_with_options(
        self,
        request: vcs_20200515_models.GetUserDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetUserDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetUserDetailResponse().from_map(
            self.do_rpcrequest('GetUserDetail', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_detail_with_options_async(
        self,
        request: vcs_20200515_models.GetUserDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetUserDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetUserDetailResponse().from_map(
            await self.do_rpcrequest_async('GetUserDetail', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_detail(
        self,
        request: vcs_20200515_models.GetUserDetailRequest,
    ) -> vcs_20200515_models.GetUserDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_detail_with_options(request, runtime)

    async def get_user_detail_async(
        self,
        request: vcs_20200515_models.GetUserDetailRequest,
    ) -> vcs_20200515_models.GetUserDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_detail_with_options_async(request, runtime)

    def update_device_capture_strategy_with_options(
        self,
        request: vcs_20200515_models.UpdateDeviceCaptureStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateDeviceCaptureStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateDeviceCaptureStrategyResponse().from_map(
            self.do_rpcrequest('UpdateDeviceCaptureStrategy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_capture_strategy_with_options_async(
        self,
        request: vcs_20200515_models.UpdateDeviceCaptureStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateDeviceCaptureStrategyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateDeviceCaptureStrategyResponse().from_map(
            await self.do_rpcrequest_async('UpdateDeviceCaptureStrategy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_capture_strategy(
        self,
        request: vcs_20200515_models.UpdateDeviceCaptureStrategyRequest,
    ) -> vcs_20200515_models.UpdateDeviceCaptureStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_capture_strategy_with_options(request, runtime)

    async def update_device_capture_strategy_async(
        self,
        request: vcs_20200515_models.UpdateDeviceCaptureStrategyRequest,
    ) -> vcs_20200515_models.UpdateDeviceCaptureStrategyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_capture_strategy_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: vcs_20200515_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateUserGroupResponse().from_map(
            self.do_rpcrequest('CreateUserGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: vcs_20200515_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateUserGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateUserGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user_group(
        self,
        request: vcs_20200515_models.CreateUserGroupRequest,
    ) -> vcs_20200515_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: vcs_20200515_models.CreateUserGroupRequest,
    ) -> vcs_20200515_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def invoke_motor_model_with_options(
        self,
        request: vcs_20200515_models.InvokeMotorModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.InvokeMotorModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.InvokeMotorModelResponse().from_map(
            self.do_rpcrequest('InvokeMotorModel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_motor_model_with_options_async(
        self,
        request: vcs_20200515_models.InvokeMotorModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.InvokeMotorModelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.InvokeMotorModelResponse().from_map(
            await self.do_rpcrequest_async('InvokeMotorModel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_motor_model(
        self,
        request: vcs_20200515_models.InvokeMotorModelRequest,
    ) -> vcs_20200515_models.InvokeMotorModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_motor_model_with_options(request, runtime)

    async def invoke_motor_model_async(
        self,
        request: vcs_20200515_models.InvokeMotorModelRequest,
    ) -> vcs_20200515_models.InvokeMotorModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_motor_model_with_options_async(request, runtime)

    def list_event_algorithm_results_with_options(
        self,
        request: vcs_20200515_models.ListEventAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListEventAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListEventAlgorithmResultsResponse().from_map(
            self.do_rpcrequest('ListEventAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_event_algorithm_results_with_options_async(
        self,
        request: vcs_20200515_models.ListEventAlgorithmResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListEventAlgorithmResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListEventAlgorithmResultsResponse().from_map(
            await self.do_rpcrequest_async('ListEventAlgorithmResults', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_event_algorithm_results(
        self,
        request: vcs_20200515_models.ListEventAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListEventAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_algorithm_results_with_options(request, runtime)

    async def list_event_algorithm_results_async(
        self,
        request: vcs_20200515_models.ListEventAlgorithmResultsRequest,
    ) -> vcs_20200515_models.ListEventAlgorithmResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_algorithm_results_with_options_async(request, runtime)

    def get_face_model_result_with_options(
        self,
        request: vcs_20200515_models.GetFaceModelResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetFaceModelResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetFaceModelResultResponse().from_map(
            self.do_rpcrequest('GetFaceModelResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_face_model_result_with_options_async(
        self,
        request: vcs_20200515_models.GetFaceModelResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetFaceModelResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetFaceModelResultResponse().from_map(
            await self.do_rpcrequest_async('GetFaceModelResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_face_model_result(
        self,
        request: vcs_20200515_models.GetFaceModelResultRequest,
    ) -> vcs_20200515_models.GetFaceModelResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_face_model_result_with_options(request, runtime)

    async def get_face_model_result_async(
        self,
        request: vcs_20200515_models.GetFaceModelResultRequest,
    ) -> vcs_20200515_models.GetFaceModelResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_face_model_result_with_options_async(request, runtime)

    def retry_start_deploy_with_options(
        self,
        request: vcs_20200515_models.RetryStartDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RetryStartDeployResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RetryStartDeployResponse().from_map(
            self.do_rpcrequest('RetryStartDeploy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retry_start_deploy_with_options_async(
        self,
        request: vcs_20200515_models.RetryStartDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RetryStartDeployResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RetryStartDeployResponse().from_map(
            await self.do_rpcrequest_async('RetryStartDeploy', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retry_start_deploy(
        self,
        request: vcs_20200515_models.RetryStartDeployRequest,
    ) -> vcs_20200515_models.RetryStartDeployResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_start_deploy_with_options(request, runtime)

    async def retry_start_deploy_async(
        self,
        request: vcs_20200515_models.RetryStartDeployRequest,
    ) -> vcs_20200515_models.RetryStartDeployResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_start_deploy_with_options_async(request, runtime)

    def sync_device_time_with_options(
        self,
        request: vcs_20200515_models.SyncDeviceTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SyncDeviceTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SyncDeviceTimeResponse().from_map(
            self.do_rpcrequest('SyncDeviceTime', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_device_time_with_options_async(
        self,
        request: vcs_20200515_models.SyncDeviceTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SyncDeviceTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SyncDeviceTimeResponse().from_map(
            await self.do_rpcrequest_async('SyncDeviceTime', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_device_time(
        self,
        request: vcs_20200515_models.SyncDeviceTimeRequest,
    ) -> vcs_20200515_models.SyncDeviceTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_device_time_with_options(request, runtime)

    async def sync_device_time_async(
        self,
        request: vcs_20200515_models.SyncDeviceTimeRequest,
    ) -> vcs_20200515_models.SyncDeviceTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_device_time_with_options_async(request, runtime)

    def create_sample_with_options(
        self,
        request: vcs_20200515_models.CreateSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateSampleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateSampleResponse().from_map(
            self.do_rpcrequest('CreateSample', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sample_with_options_async(
        self,
        request: vcs_20200515_models.CreateSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateSampleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateSampleResponse().from_map(
            await self.do_rpcrequest_async('CreateSample', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sample(
        self,
        request: vcs_20200515_models.CreateSampleRequest,
    ) -> vcs_20200515_models.CreateSampleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sample_with_options(request, runtime)

    async def create_sample_async(
        self,
        request: vcs_20200515_models.CreateSampleRequest,
    ) -> vcs_20200515_models.CreateSampleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sample_with_options_async(request, runtime)

    def add_monitor_with_options(
        self,
        request: vcs_20200515_models.AddMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddMonitorResponse().from_map(
            self.do_rpcrequest('AddMonitor', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_monitor_with_options_async(
        self,
        request: vcs_20200515_models.AddMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddMonitorResponse().from_map(
            await self.do_rpcrequest_async('AddMonitor', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_monitor(
        self,
        request: vcs_20200515_models.AddMonitorRequest,
    ) -> vcs_20200515_models.AddMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_monitor_with_options(request, runtime)

    async def add_monitor_async(
        self,
        request: vcs_20200515_models.AddMonitorRequest,
    ) -> vcs_20200515_models.AddMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_monitor_with_options_async(request, runtime)

    def delete_profile_with_options(
        self,
        request: vcs_20200515_models.DeleteProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteProfileResponse().from_map(
            self.do_rpcrequest('DeleteProfile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_profile_with_options_async(
        self,
        request: vcs_20200515_models.DeleteProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteProfileResponse().from_map(
            await self.do_rpcrequest_async('DeleteProfile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_profile(
        self,
        request: vcs_20200515_models.DeleteProfileRequest,
    ) -> vcs_20200515_models.DeleteProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_profile_with_options(request, runtime)

    async def delete_profile_async(
        self,
        request: vcs_20200515_models.DeleteProfileRequest,
    ) -> vcs_20200515_models.DeleteProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_profile_with_options_async(request, runtime)

    def delete_profile_catalog_with_options(
        self,
        request: vcs_20200515_models.DeleteProfileCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteProfileCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteProfileCatalogResponse().from_map(
            self.do_rpcrequest('DeleteProfileCatalog', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_profile_catalog_with_options_async(
        self,
        request: vcs_20200515_models.DeleteProfileCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteProfileCatalogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteProfileCatalogResponse().from_map(
            await self.do_rpcrequest_async('DeleteProfileCatalog', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_profile_catalog(
        self,
        request: vcs_20200515_models.DeleteProfileCatalogRequest,
    ) -> vcs_20200515_models.DeleteProfileCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_profile_catalog_with_options(request, runtime)

    async def delete_profile_catalog_async(
        self,
        request: vcs_20200515_models.DeleteProfileCatalogRequest,
    ) -> vcs_20200515_models.DeleteProfileCatalogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_profile_catalog_with_options_async(request, runtime)

    def delete_ipcdevice_with_options(
        self,
        request: vcs_20200515_models.DeleteIPCDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteIPCDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteIPCDeviceResponse().from_map(
            self.do_rpcrequest('DeleteIPCDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipcdevice_with_options_async(
        self,
        request: vcs_20200515_models.DeleteIPCDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteIPCDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteIPCDeviceResponse().from_map(
            await self.do_rpcrequest_async('DeleteIPCDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipcdevice(
        self,
        request: vcs_20200515_models.DeleteIPCDeviceRequest,
    ) -> vcs_20200515_models.DeleteIPCDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipcdevice_with_options(request, runtime)

    async def delete_ipcdevice_async(
        self,
        request: vcs_20200515_models.DeleteIPCDeviceRequest,
    ) -> vcs_20200515_models.DeleteIPCDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipcdevice_with_options_async(request, runtime)

    def get_monitor_result_with_options(
        self,
        request: vcs_20200515_models.GetMonitorResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetMonitorResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetMonitorResultResponse().from_map(
            self.do_rpcrequest('GetMonitorResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_monitor_result_with_options_async(
        self,
        request: vcs_20200515_models.GetMonitorResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetMonitorResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetMonitorResultResponse().from_map(
            await self.do_rpcrequest_async('GetMonitorResult', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_monitor_result(
        self,
        request: vcs_20200515_models.GetMonitorResultRequest,
    ) -> vcs_20200515_models.GetMonitorResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_result_with_options(request, runtime)

    async def get_monitor_result_async(
        self,
        request: vcs_20200515_models.GetMonitorResultRequest,
    ) -> vcs_20200515_models.GetMonitorResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_monitor_result_with_options_async(request, runtime)

    def recognize_image_with_options(
        self,
        request: vcs_20200515_models.RecognizeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RecognizeImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RecognizeImageResponse().from_map(
            self.do_rpcrequest('RecognizeImage', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_image_with_options_async(
        self,
        request: vcs_20200515_models.RecognizeImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RecognizeImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RecognizeImageResponse().from_map(
            await self.do_rpcrequest_async('RecognizeImage', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_image(
        self,
        request: vcs_20200515_models.RecognizeImageRequest,
    ) -> vcs_20200515_models.RecognizeImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_with_options(request, runtime)

    async def recognize_image_async(
        self,
        request: vcs_20200515_models.RecognizeImageRequest,
    ) -> vcs_20200515_models.RecognizeImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_image_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: vcs_20200515_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: vcs_20200515_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteUser', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(
        self,
        request: vcs_20200515_models.DeleteUserRequest,
    ) -> vcs_20200515_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: vcs_20200515_models.DeleteUserRequest,
    ) -> vcs_20200515_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def update_device_with_options(
        self,
        request: vcs_20200515_models.UpdateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateDeviceResponse().from_map(
            self.do_rpcrequest('UpdateDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_device_with_options_async(
        self,
        request: vcs_20200515_models.UpdateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateDeviceResponse().from_map(
            await self.do_rpcrequest_async('UpdateDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device(
        self,
        request: vcs_20200515_models.UpdateDeviceRequest,
    ) -> vcs_20200515_models.UpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_device_with_options(request, runtime)

    async def update_device_async(
        self,
        request: vcs_20200515_models.UpdateDeviceRequest,
    ) -> vcs_20200515_models.UpdateDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_device_with_options_async(request, runtime)

    def register_device_with_options(
        self,
        request: vcs_20200515_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RegisterDeviceResponse().from_map(
            self.do_rpcrequest('RegisterDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_device_with_options_async(
        self,
        request: vcs_20200515_models.RegisterDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.RegisterDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.RegisterDeviceResponse().from_map(
            await self.do_rpcrequest_async('RegisterDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_device(
        self,
        request: vcs_20200515_models.RegisterDeviceRequest,
    ) -> vcs_20200515_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    async def register_device_async(
        self,
        request: vcs_20200515_models.RegisterDeviceRequest,
    ) -> vcs_20200515_models.RegisterDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_device_with_options_async(request, runtime)

    def delete_channel_with_options(
        self,
        request: vcs_20200515_models.DeleteChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteChannelResponse().from_map(
            self.do_rpcrequest('DeleteChannel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_channel_with_options_async(
        self,
        request: vcs_20200515_models.DeleteChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteChannelResponse().from_map(
            await self.do_rpcrequest_async('DeleteChannel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_channel(
        self,
        request: vcs_20200515_models.DeleteChannelRequest,
    ) -> vcs_20200515_models.DeleteChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_channel_with_options(request, runtime)

    async def delete_channel_async(
        self,
        request: vcs_20200515_models.DeleteChannelRequest,
    ) -> vcs_20200515_models.DeleteChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_channel_with_options_async(request, runtime)

    def get_train_label_with_options(
        self,
        request: vcs_20200515_models.GetTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetTrainLabelResponse().from_map(
            self.do_rpcrequest('GetTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_train_label_with_options_async(
        self,
        request: vcs_20200515_models.GetTrainLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetTrainLabelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetTrainLabelResponse().from_map(
            await self.do_rpcrequest_async('GetTrainLabel', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_train_label(
        self,
        request: vcs_20200515_models.GetTrainLabelRequest,
    ) -> vcs_20200515_models.GetTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_train_label_with_options(request, runtime)

    async def get_train_label_async(
        self,
        request: vcs_20200515_models.GetTrainLabelRequest,
    ) -> vcs_20200515_models.GetTrainLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_train_label_with_options_async(request, runtime)

    def list_marker_with_options(
        self,
        request: vcs_20200515_models.ListMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListMarkerResponse().from_map(
            self.do_rpcrequest('ListMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_marker_with_options_async(
        self,
        request: vcs_20200515_models.ListMarkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListMarkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListMarkerResponse().from_map(
            await self.do_rpcrequest_async('ListMarker', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_marker(
        self,
        request: vcs_20200515_models.ListMarkerRequest,
    ) -> vcs_20200515_models.ListMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_marker_with_options(request, runtime)

    async def list_marker_async(
        self,
        request: vcs_20200515_models.ListMarkerRequest,
    ) -> vcs_20200515_models.ListMarkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_marker_with_options_async(request, runtime)

    def create_video_compose_task_with_options(
        self,
        request: vcs_20200515_models.CreateVideoComposeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateVideoComposeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateVideoComposeTaskResponse().from_map(
            self.do_rpcrequest('CreateVideoComposeTask', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_video_compose_task_with_options_async(
        self,
        request: vcs_20200515_models.CreateVideoComposeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.CreateVideoComposeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.CreateVideoComposeTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateVideoComposeTask', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_video_compose_task(
        self,
        request: vcs_20200515_models.CreateVideoComposeTaskRequest,
    ) -> vcs_20200515_models.CreateVideoComposeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_video_compose_task_with_options(request, runtime)

    async def create_video_compose_task_async(
        self,
        request: vcs_20200515_models.CreateVideoComposeTaskRequest,
    ) -> vcs_20200515_models.CreateVideoComposeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_compose_task_with_options_async(request, runtime)

    def delete_device_for_instance_with_options(
        self,
        tmp_req: vcs_20200515_models.DeleteDeviceForInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteDeviceForInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.DeleteDeviceForInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.devices):
            request.devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.devices, 'Devices', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteDeviceForInstanceResponse().from_map(
            self.do_rpcrequest('DeleteDeviceForInstance', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_device_for_instance_with_options_async(
        self,
        tmp_req: vcs_20200515_models.DeleteDeviceForInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteDeviceForInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.DeleteDeviceForInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.devices):
            request.devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.devices, 'Devices', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteDeviceForInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteDeviceForInstance', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device_for_instance(
        self,
        request: vcs_20200515_models.DeleteDeviceForInstanceRequest,
    ) -> vcs_20200515_models.DeleteDeviceForInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_device_for_instance_with_options(request, runtime)

    async def delete_device_for_instance_async(
        self,
        request: vcs_20200515_models.DeleteDeviceForInstanceRequest,
    ) -> vcs_20200515_models.DeleteDeviceForInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_for_instance_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: vcs_20200515_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateUserGroupResponse().from_map(
            self.do_rpcrequest('UpdateUserGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        request: vcs_20200515_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.UpdateUserGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateUserGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user_group(
        self,
        request: vcs_20200515_models.UpdateUserGroupRequest,
    ) -> vcs_20200515_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: vcs_20200515_models.UpdateUserGroupRequest,
    ) -> vcs_20200515_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def bind_person_with_options(
        self,
        request: vcs_20200515_models.BindPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.BindPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.BindPersonResponse().from_map(
            self.do_rpcrequest('BindPerson', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_person_with_options_async(
        self,
        request: vcs_20200515_models.BindPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.BindPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.BindPersonResponse().from_map(
            await self.do_rpcrequest_async('BindPerson', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_person(
        self,
        request: vcs_20200515_models.BindPersonRequest,
    ) -> vcs_20200515_models.BindPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_person_with_options(request, runtime)

    async def bind_person_async(
        self,
        request: vcs_20200515_models.BindPersonRequest,
    ) -> vcs_20200515_models.BindPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_person_with_options_async(request, runtime)

    def get_body_options_with_options(
        self,
        request: vcs_20200515_models.GetBodyOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetBodyOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetBodyOptionsResponse().from_map(
            self.do_rpcrequest('GetBodyOptions', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_body_options_with_options_async(
        self,
        request: vcs_20200515_models.GetBodyOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.GetBodyOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.GetBodyOptionsResponse().from_map(
            await self.do_rpcrequest_async('GetBodyOptions', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_body_options(
        self,
        request: vcs_20200515_models.GetBodyOptionsRequest,
    ) -> vcs_20200515_models.GetBodyOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_body_options_with_options(request, runtime)

    async def get_body_options_async(
        self,
        request: vcs_20200515_models.GetBodyOptionsRequest,
    ) -> vcs_20200515_models.GetBodyOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_body_options_with_options_async(request, runtime)

    def bind_corp_group_with_options(
        self,
        request: vcs_20200515_models.BindCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.BindCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.BindCorpGroupResponse().from_map(
            self.do_rpcrequest('BindCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_corp_group_with_options_async(
        self,
        request: vcs_20200515_models.BindCorpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.BindCorpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.BindCorpGroupResponse().from_map(
            await self.do_rpcrequest_async('BindCorpGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_corp_group(
        self,
        request: vcs_20200515_models.BindCorpGroupRequest,
    ) -> vcs_20200515_models.BindCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_corp_group_with_options(request, runtime)

    async def bind_corp_group_async(
        self,
        request: vcs_20200515_models.BindCorpGroupRequest,
    ) -> vcs_20200515_models.BindCorpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_corp_group_with_options_async(request, runtime)

    def list_nvrchannel_device_with_options(
        self,
        request: vcs_20200515_models.ListNVRChannelDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListNVRChannelDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListNVRChannelDeviceResponse().from_map(
            self.do_rpcrequest('ListNVRChannelDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nvrchannel_device_with_options_async(
        self,
        request: vcs_20200515_models.ListNVRChannelDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListNVRChannelDeviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListNVRChannelDeviceResponse().from_map(
            await self.do_rpcrequest_async('ListNVRChannelDevice', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nvrchannel_device(
        self,
        request: vcs_20200515_models.ListNVRChannelDeviceRequest,
    ) -> vcs_20200515_models.ListNVRChannelDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nvrchannel_device_with_options(request, runtime)

    async def list_nvrchannel_device_async(
        self,
        request: vcs_20200515_models.ListNVRChannelDeviceRequest,
    ) -> vcs_20200515_models.ListNVRChannelDeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nvrchannel_device_with_options_async(request, runtime)

    def add_profile_with_options(
        self,
        request: vcs_20200515_models.AddProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddProfileResponse().from_map(
            self.do_rpcrequest('AddProfile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_profile_with_options_async(
        self,
        request: vcs_20200515_models.AddProfileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.AddProfileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.AddProfileResponse().from_map(
            await self.do_rpcrequest_async('AddProfile', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_profile(
        self,
        request: vcs_20200515_models.AddProfileRequest,
    ) -> vcs_20200515_models.AddProfileResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_profile_with_options(request, runtime)

    async def add_profile_async(
        self,
        request: vcs_20200515_models.AddProfileRequest,
    ) -> vcs_20200515_models.AddProfileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_profile_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: vcs_20200515_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteUserGroupResponse().from_map(
            self.do_rpcrequest('DeleteUserGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: vcs_20200515_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.DeleteUserGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteUserGroup', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_group(
        self,
        request: vcs_20200515_models.DeleteUserGroupRequest,
    ) -> vcs_20200515_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: vcs_20200515_models.DeleteUserGroupRequest,
    ) -> vcs_20200515_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        request: vcs_20200515_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListUserGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListUserGroupsResponse().from_map(
            self.do_rpcrequest('ListUserGroups', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        request: vcs_20200515_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.ListUserGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.ListUserGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListUserGroups', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_groups(
        self,
        request: vcs_20200515_models.ListUserGroupsRequest,
    ) -> vcs_20200515_models.ListUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: vcs_20200515_models.ListUserGroupsRequest,
    ) -> vcs_20200515_models.ListUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def search_body_with_options(
        self,
        tmp_req: vcs_20200515_models.SearchBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SearchBodyResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchBodyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.option_list):
            request.option_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option_list, 'OptionList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SearchBodyResponse().from_map(
            self.do_rpcrequest('SearchBody', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_body_with_options_async(
        self,
        tmp_req: vcs_20200515_models.SearchBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vcs_20200515_models.SearchBodyResponse:
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchBodyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.option_list):
            request.option_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option_list, 'OptionList', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vcs_20200515_models.SearchBodyResponse().from_map(
            await self.do_rpcrequest_async('SearchBody', '2020-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_body(
        self,
        request: vcs_20200515_models.SearchBodyRequest,
    ) -> vcs_20200515_models.SearchBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_body_with_options(request, runtime)

    async def search_body_async(
        self,
        request: vcs_20200515_models.SearchBodyRequest,
    ) -> vcs_20200515_models.SearchBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_body_with_options_async(request, runtime)
