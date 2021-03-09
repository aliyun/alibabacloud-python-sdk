# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_ecd20200930 import models as ecd_20200930_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_directory_sso_status_with_options(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.GetDirectorySsoStatusResponse().from_map(
            self.do_request('GetDirectorySsoStatus', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_directory_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.GetDirectorySsoStatusResponse().from_map(
            await self.do_request_async('GetDirectorySsoStatus', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_directory_sso_status(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_directory_sso_status_with_options(request, runtime)

    async def get_directory_sso_status_async(
        self,
        request: ecd_20200930_models.GetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.GetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_sso_status_with_options_async(request, runtime)

    def set_directory_sso_status_with_options(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.SetDirectorySsoStatusResponse().from_map(
            self.do_request('SetDirectorySsoStatus', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_directory_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.SetDirectorySsoStatusResponse().from_map(
            await self.do_request_async('SetDirectorySsoStatus', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_directory_sso_status(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_directory_sso_status_with_options(request, runtime)

    async def set_directory_sso_status_async(
        self,
        request: ecd_20200930_models.SetDirectorySsoStatusRequest,
    ) -> ecd_20200930_models.SetDirectorySsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_directory_sso_status_with_options_async(request, runtime)

    def get_sp_metadata_with_options(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.GetSpMetadataResponse().from_map(
            self.do_request('GetSpMetadata', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_sp_metadata_with_options_async(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.GetSpMetadataResponse().from_map(
            await self.do_request_async('GetSpMetadata', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_sp_metadata(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sp_metadata_with_options(request, runtime)

    async def get_sp_metadata_async(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sp_metadata_with_options_async(request, runtime)

    def set_idp_metadata_with_options(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.SetIdpMetadataResponse().from_map(
            self.do_request('SetIdpMetadata', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_idp_metadata_with_options_async(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.SetIdpMetadataResponse().from_map(
            await self.do_request_async('SetIdpMetadata', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_idp_metadata(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_idp_metadata_with_options(request, runtime)

    async def set_idp_metadata_async(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_idp_metadata_with_options_async(request, runtime)

    def rebuild_desktops_with_options(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RebuildDesktopsResponse().from_map(
            self.do_request('RebuildDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def rebuild_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RebuildDesktopsResponse().from_map(
            await self.do_request_async('RebuildDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def rebuild_desktops(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebuild_desktops_with_options(request, runtime)

    async def rebuild_desktops_async(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebuild_desktops_with_options_async(request, runtime)

    def modify_bundle_with_options(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyBundleResponse().from_map(
            self.do_request('ModifyBundle', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_bundle_with_options_async(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyBundleResponse().from_map(
            await self.do_request_async('ModifyBundle', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_bundle(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bundle_with_options(request, runtime)

    async def modify_bundle_async(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bundle_with_options_async(request, runtime)

    def unlock_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.UnlockVirtualMFADeviceResponse().from_map(
            self.do_request('UnlockVirtualMFADevice', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def unlock_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.UnlockVirtualMFADeviceResponse().from_map(
            await self.do_request_async('UnlockVirtualMFADevice', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unlock_virtual_mfadevice(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_virtual_mfadevice_with_options(request, runtime)

    async def unlock_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_virtual_mfadevice_with_options_async(request, runtime)

    def describe_virtual_mfadevices_with_options(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeVirtualMFADevicesResponse().from_map(
            self.do_request('DescribeVirtualMFADevices', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_virtual_mfadevices_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeVirtualMFADevicesResponse().from_map(
            await self.do_request_async('DescribeVirtualMFADevices', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_virtual_mfadevices(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_mfadevices_with_options(request, runtime)

    async def describe_virtual_mfadevices_async(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_mfadevices_with_options_async(request, runtime)

    def lock_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.LockVirtualMFADeviceResponse().from_map(
            self.do_request('LockVirtualMFADevice', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def lock_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.LockVirtualMFADeviceResponse().from_map(
            await self.do_request_async('LockVirtualMFADevice', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def lock_virtual_mfadevice(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_virtual_mfadevice_with_options(request, runtime)

    async def lock_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_virtual_mfadevice_with_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteVirtualMFADeviceResponse().from_map(
            self.do_request('DeleteVirtualMFADevice', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteVirtualMFADeviceResponse().from_map(
            await self.do_request_async('DeleteVirtualMFADevice', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def modify_adconnector_directory_with_options(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyADConnectorDirectoryResponse().from_map(
            self.do_request('ModifyADConnectorDirectory', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_adconnector_directory_with_options_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyADConnectorDirectoryResponse().from_map(
            await self.do_request_async('ModifyADConnectorDirectory', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_adconnector_directory(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_directory_with_options(request, runtime)

    async def modify_adconnector_directory_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_adconnector_directory_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ListTagResourcesResponse().from_map(
            self.do_request('ListTagResources', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ListTagResourcesResponse().from_map(
            await self.do_request_async('ListTagResources', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_resources(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.UntagResourcesResponse().from_map(
            self.do_request('UntagResources', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.UntagResourcesResponse().from_map(
            await self.do_request_async('UntagResources', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def untag_resources(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.TagResourcesResponse().from_map(
            self.do_request('TagResources', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.TagResourcesResponse().from_map(
            await self.do_request_async('TagResources', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def tag_resources(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
    ) -> ecd_20200930_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
    ) -> ecd_20200930_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def modify_desktop_name_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyDesktopNameResponse().from_map(
            self.do_request('ModifyDesktopName', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_desktop_name_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyDesktopNameResponse().from_map(
            await self.do_request_async('ModifyDesktopName', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_desktop_name(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_name_with_options(request, runtime)

    async def modify_desktop_name_async(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_name_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        request: ecd_20200930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RunCommandResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RunCommandResponse().from_map(
            self.do_request('RunCommand', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def run_command_with_options_async(
        self,
        request: ecd_20200930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RunCommandResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RunCommandResponse().from_map(
            await self.do_request_async('RunCommand', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def run_command(
        self,
        request: ecd_20200930_models.RunCommandRequest,
    ) -> ecd_20200930_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: ecd_20200930_models.RunCommandRequest,
    ) -> ecd_20200930_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.StopInvocationResponse().from_map(
            self.do_request('StopInvocation', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def stop_invocation_with_options_async(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.StopInvocationResponse().from_map(
            await self.do_request_async('StopInvocation', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_invocation(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
    ) -> ecd_20200930_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
    ) -> ecd_20200930_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeInvocationsResponse().from_map(
            self.do_request('DescribeInvocations', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeInvocationsResponse().from_map(
            await self.do_request_async('DescribeInvocations', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_invocations(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeZonesResponse().from_map(
            self.do_request('DescribeZones', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeZonesResponse().from_map(
            await self.do_request_async('DescribeZones', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_zones(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeRegionsResponse().from_map(
            self.do_request('DescribeRegions', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeRegionsResponse().from_map(
            await self.do_request_async('DescribeRegions', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_regions(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_client_events_with_options(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeClientEventsResponse().from_map(
            self.do_request('DescribeClientEvents', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_client_events_with_options_async(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeClientEventsResponse().from_map(
            await self.do_request_async('DescribeClientEvents', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_client_events(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_events_with_options(request, runtime)

    async def describe_client_events_async(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_events_with_options_async(request, runtime)

    def reset_snapshot_with_options(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ResetSnapshotResponse().from_map(
            self.do_request('ResetSnapshot', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def reset_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ResetSnapshotResponse().from_map(
            await self.do_request_async('ResetSnapshot', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reset_snapshot(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    async def reset_snapshot_async(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_snapshot_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteSnapshotResponse().from_map(
            self.do_request('DeleteSnapshot', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteSnapshotResponse().from_map(
            await self.do_request_async('DeleteSnapshot', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_snapshot(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateSnapshotResponse().from_map(
            self.do_request('CreateSnapshot', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateSnapshotResponse().from_map(
            await self.do_request_async('CreateSnapshot', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_snapshot(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeSnapshotsResponse().from_map(
            self.do_request('DescribeSnapshots', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeSnapshotsResponse().from_map(
            await self.do_request_async('DescribeSnapshots', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_snapshots(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def renew_desktops_with_options(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RenewDesktopsResponse().from_map(
            self.do_request('RenewDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def renew_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RenewDesktopsResponse().from_map(
            await self.do_request_async('RenewDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def renew_desktops(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_desktops_with_options(request, runtime)

    async def renew_desktops_async(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_desktops_with_options_async(request, runtime)

    def stop_desktops_with_options(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.StopDesktopsResponse().from_map(
            self.do_request('StopDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def stop_desktops_with_options_async(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.StopDesktopsResponse().from_map(
            await self.do_request_async('StopDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_desktops(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    async def stop_desktops_async(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_desktops_with_options_async(request, runtime)

    def start_desktops_with_options(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.StartDesktopsResponse().from_map(
            self.do_request('StartDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def start_desktops_with_options_async(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.StartDesktopsResponse().from_map(
            await self.do_request_async('StartDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def start_desktops(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    async def start_desktops_async(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_desktops_with_options_async(request, runtime)

    def modify_policy_group_with_options(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyPolicyGroupResponse().from_map(
            self.do_request('ModifyPolicyGroup', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyPolicyGroupResponse().from_map(
            await self.do_request_async('ModifyPolicyGroup', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_policy_group(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    async def modify_policy_group_async(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_group_with_options_async(request, runtime)

    def describe_desktop_types_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDesktopTypesResponse().from_map(
            self.do_request('DescribeDesktopTypes', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_desktop_types_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDesktopTypesResponse().from_map(
            await self.do_request_async('DescribeDesktopTypes', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_desktop_types(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_types_with_options(request, runtime)

    async def describe_desktop_types_async(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktop_types_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDirectoriesResponse().from_map(
            self.do_request('DescribeDirectories', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDirectoriesResponse().from_map(
            await self.do_request_async('DescribeDirectories', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_directories(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def delete_directories_with_options(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteDirectoriesResponse().from_map(
            self.do_request('DeleteDirectories', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_directories_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteDirectoriesResponse().from_map(
            await self.do_request_async('DeleteDirectories', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_directories(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    async def delete_directories_async(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_directories_with_options_async(request, runtime)

    def list_directory_users_with_options(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ListDirectoryUsersResponse().from_map(
            self.do_request('ListDirectoryUsers', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_directory_users_with_options_async(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ListDirectoryUsersResponse().from_map(
            await self.do_request_async('ListDirectoryUsers', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_directory_users(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

    async def list_directory_users_async(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_directory_users_with_options_async(request, runtime)

    def create_image_with_options(
        self,
        request: ecd_20200930_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateImageResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateImageResponse().from_map(
            self.do_request('CreateImage', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_image_with_options_async(
        self,
        request: ecd_20200930_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateImageResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateImageResponse().from_map(
            await self.do_request_async('CreateImage', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_image(
        self,
        request: ecd_20200930_models.CreateImageRequest,
    ) -> ecd_20200930_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    async def create_image_async(
        self,
        request: ecd_20200930_models.CreateImageRequest,
    ) -> ecd_20200930_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_with_options_async(request, runtime)

    def create_ramdirectory_with_options(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateRAMDirectoryResponse().from_map(
            self.do_request('CreateRAMDirectory', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_ramdirectory_with_options_async(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateRAMDirectoryResponse().from_map(
            await self.do_request_async('CreateRAMDirectory', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_ramdirectory(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ramdirectory_with_options(request, runtime)

    async def create_ramdirectory_async(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ramdirectory_with_options_async(request, runtime)

    def delete_policy_groups_with_options(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeletePolicyGroupsResponse().from_map(
            self.do_request('DeletePolicyGroups', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_policy_groups_with_options_async(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeletePolicyGroupsResponse().from_map(
            await self.do_request_async('DeletePolicyGroups', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_policy_groups(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    async def delete_policy_groups_async(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_groups_with_options_async(request, runtime)

    def describe_policy_groups_with_options(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribePolicyGroupsResponse().from_map(
            self.do_request('DescribePolicyGroups', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_policy_groups_with_options_async(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribePolicyGroupsResponse().from_map(
            await self.do_request_async('DescribePolicyGroups', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_policy_groups(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_groups_with_options(request, runtime)

    async def describe_policy_groups_async(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_groups_with_options_async(request, runtime)

    def delete_desktops_with_options(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteDesktopsResponse().from_map(
            self.do_request('DeleteDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_desktops_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteDesktopsResponse().from_map(
            await self.do_request_async('DeleteDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_desktops(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_desktops_with_options(request, runtime)

    async def delete_desktops_async(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_desktops_with_options_async(request, runtime)

    def modify_image_attribute_with_options(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyImageAttributeResponse().from_map(
            self.do_request('ModifyImageAttribute', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_image_attribute_with_options_async(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyImageAttributeResponse().from_map(
            await self.do_request_async('ModifyImageAttribute', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_image_attribute(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    async def modify_image_attribute_async(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_attribute_with_options_async(request, runtime)

    def modify_entitlement_with_options(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyEntitlementResponse().from_map(
            self.do_request('ModifyEntitlement', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_entitlement_with_options_async(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyEntitlementResponse().from_map(
            await self.do_request_async('ModifyEntitlement', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_entitlement(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_entitlement_with_options(request, runtime)

    async def modify_entitlement_async(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_entitlement_with_options_async(request, runtime)

    def delete_bundles_with_options(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteBundlesResponse().from_map(
            self.do_request('DeleteBundles', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_bundles_with_options_async(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteBundlesResponse().from_map(
            await self.do_request_async('DeleteBundles', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_bundles(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bundles_with_options(request, runtime)

    async def delete_bundles_async(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bundles_with_options_async(request, runtime)

    def describe_desktops_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDesktopsResponse().from_map(
            self.do_request('DescribeDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_desktops_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDesktopsResponse().from_map(
            await self.do_request_async('DescribeDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_desktops(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    async def describe_desktops_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktops_with_options_async(request, runtime)

    def reboot_desktops_with_options(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RebootDesktopsResponse().from_map(
            self.do_request('RebootDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def reboot_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.RebootDesktopsResponse().from_map(
            await self.do_request_async('RebootDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reboot_desktops(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    async def reboot_desktops_async(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_desktops_with_options_async(request, runtime)

    def create_bundle_with_options(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateBundleResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateBundleResponse().from_map(
            self.do_request('CreateBundle', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_bundle_with_options_async(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateBundleResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateBundleResponse().from_map(
            await self.do_request_async('CreateBundle', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_bundle(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
    ) -> ecd_20200930_models.CreateBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    async def create_bundle_async(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
    ) -> ecd_20200930_models.CreateBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_bundle_with_options_async(request, runtime)

    def modify_desktops_policy_group_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyDesktopsPolicyGroupResponse().from_map(
            self.do_request('ModifyDesktopsPolicyGroup', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def modify_desktops_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyDesktopsPolicyGroupResponse().from_map(
            await self.do_request_async('ModifyDesktopsPolicyGroup', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def modify_desktops_policy_group(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktops_policy_group_with_options(request, runtime)

    async def modify_desktops_policy_group_async(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktops_policy_group_with_options_async(request, runtime)

    def create_policy_group_with_options(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreatePolicyGroupResponse().from_map(
            self.do_request('CreatePolicyGroup', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreatePolicyGroupResponse().from_map(
            await self.do_request_async('CreatePolicyGroup', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_policy_group(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    async def create_policy_group_async(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_group_with_options_async(request, runtime)

    def create_adconnector_directory_with_options(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateADConnectorDirectoryResponse().from_map(
            self.do_request('CreateADConnectorDirectory', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_adconnector_directory_with_options_async(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateADConnectorDirectoryResponse().from_map(
            await self.do_request_async('CreateADConnectorDirectory', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_adconnector_directory(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    async def create_adconnector_directory_async(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_adconnector_directory_with_options_async(request, runtime)

    def describe_bundles_with_options(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeBundlesResponse().from_map(
            self.do_request('DescribeBundles', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_bundles_with_options_async(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeBundlesResponse().from_map(
            await self.do_request_async('DescribeBundles', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_bundles(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bundles_with_options(request, runtime)

    async def describe_bundles_async(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bundles_with_options_async(request, runtime)

    def delete_images_with_options(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteImagesResponse().from_map(
            self.do_request('DeleteImages', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_images_with_options_async(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteImagesResponse().from_map(
            await self.do_request_async('DeleteImages', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_images(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    async def delete_images_async(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_images_with_options_async(request, runtime)

    def create_desktops_with_options(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateDesktopsResponse().from_map(
            self.do_request('CreateDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_desktops_with_options_async(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateDesktopsResponse().from_map(
            await self.do_request_async('CreateDesktops', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_desktops(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_with_options(request, runtime)

    async def create_desktops_async(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_desktops_with_options_async(request, runtime)

    def describe_images_with_options(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeImagesResponse().from_map(
            self.do_request('DescribeImages', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_images_with_options_async(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeImagesResponse().from_map(
            await self.do_request_async('DescribeImages', 'HTTPS', 'POST', '2020-09-30', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_images(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    async def describe_images_async(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_images_with_options_async(request, runtime)

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
