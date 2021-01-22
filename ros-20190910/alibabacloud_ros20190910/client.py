# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_ros20190910 import models as ros20190910_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ros', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def generate_template_policy_with_options(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GenerateTemplatePolicyResponse().from_map(
            self.do_request('GenerateTemplatePolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def generate_template_policy_with_options_async(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GenerateTemplatePolicyResponse().from_map(
            await self.do_request_async('GenerateTemplatePolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_template_policy(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_template_policy_with_options(request, runtime)

    async def generate_template_policy_async(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_template_policy_with_options_async(request, runtime)

    def list_template_versions_with_options(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTemplateVersionsResponse().from_map(
            self.do_request('ListTemplateVersions', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_template_versions_with_options_async(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTemplateVersionsResponse().from_map(
            await self.do_request_async('ListTemplateVersions', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_template_versions(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    async def list_template_versions_async(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_template_versions_with_options_async(request, runtime)

    def set_template_permission_with_options(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SetTemplatePermissionResponse().from_map(
            self.do_request('SetTemplatePermission', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_template_permission_with_options_async(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SetTemplatePermissionResponse().from_map(
            await self.do_request_async('SetTemplatePermission', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_template_permission(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_template_permission_with_options(request, runtime)

    async def set_template_permission_async(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_template_permission_with_options_async(request, runtime)

    def list_stack_operation_risks_with_options(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackOperationRisksResponse().from_map(
            self.do_request('ListStackOperationRisks', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_operation_risks_with_options_async(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackOperationRisksResponse().from_map(
            await self.do_request_async('ListStackOperationRisks', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_operation_risks(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_operation_risks_with_options(request, runtime)

    async def list_stack_operation_risks_async(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_operation_risks_with_options_async(request, runtime)

    def get_template_summary_with_options(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateSummaryResponse().from_map(
            self.do_request('GetTemplateSummary', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_template_summary_with_options_async(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateSummaryResponse().from_map(
            await self.do_request_async('GetTemplateSummary', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_template_summary(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_summary_with_options(request, runtime)

    async def get_template_summary_async(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_summary_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: ros20190910_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagValuesResponse().from_map(
            self.do_request('ListTagValues', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: ros20190910_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagValuesResponse().from_map(
            await self.do_request_async('ListTagValues', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_values(
        self,
        request: ros20190910_models.ListTagValuesRequest,
    ) -> ros20190910_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: ros20190910_models.ListTagValuesRequest,
    ) -> ros20190910_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ros20190910_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagKeysResponse().from_map(
            self.do_request('ListTagKeys', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ros20190910_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagKeysResponse().from_map(
            await self.do_request_async('ListTagKeys', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_keys(
        self,
        request: ros20190910_models.ListTagKeysRequest,
    ) -> ros20190910_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ros20190910_models.ListTagKeysRequest,
    ) -> ros20190910_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def set_deletion_protection_with_options(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SetDeletionProtectionResponse().from_map(
            self.do_request('SetDeletionProtection', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_deletion_protection_with_options_async(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SetDeletionProtectionResponse().from_map(
            await self.do_request_async('SetDeletionProtection', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_deletion_protection(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    async def set_deletion_protection_async(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_deletion_protection_with_options_async(request, runtime)

    def update_stack_template_by_resources_with_options(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateStackTemplateByResourcesResponse().from_map(
            self.do_request('UpdateStackTemplateByResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_stack_template_by_resources_with_options_async(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateStackTemplateByResourcesResponse().from_map(
            await self.do_request_async('UpdateStackTemplateByResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_stack_template_by_resources(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_template_by_resources_with_options(request, runtime)

    async def update_stack_template_by_resources_async(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_template_by_resources_with_options_async(request, runtime)

    def get_stack_drift_detection_status_with_options(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackDriftDetectionStatusResponse().from_map(
            self.do_request('GetStackDriftDetectionStatus', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_stack_drift_detection_status_with_options_async(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackDriftDetectionStatusResponse().from_map(
            await self.do_request_async('GetStackDriftDetectionStatus', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_stack_drift_detection_status(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_drift_detection_status_with_options(request, runtime)

    async def get_stack_drift_detection_status_async(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_drift_detection_status_with_options_async(request, runtime)

    def detect_stack_group_drift_with_options(
        self,
        tmp: ros20190910_models.DetectStackGroupDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.DetectStackGroupDriftResponse().from_map(
            self.do_request('DetectStackGroupDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def detect_stack_group_drift_with_options_async(
        self,
        tmp: ros20190910_models.DetectStackGroupDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.DetectStackGroupDriftResponse().from_map(
            await self.do_request_async('DetectStackGroupDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detect_stack_group_drift(
        self,
        request: ros20190910_models.DetectStackGroupDriftRequest,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_group_drift_with_options(request, runtime)

    async def detect_stack_group_drift_async(
        self,
        request: ros20190910_models.DetectStackGroupDriftRequest,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_group_drift_with_options_async(request, runtime)

    def list_stack_resource_drifts_with_options(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackResourceDriftsResponse().from_map(
            self.do_request('ListStackResourceDrifts', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_resource_drifts_with_options_async(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackResourceDriftsResponse().from_map(
            await self.do_request_async('ListStackResourceDrifts', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_resource_drifts(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resource_drifts_with_options(request, runtime)

    async def list_stack_resource_drifts_async(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_resource_drifts_with_options_async(request, runtime)

    def detect_stack_resource_drift_with_options(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DetectStackResourceDriftResponse().from_map(
            self.do_request('DetectStackResourceDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def detect_stack_resource_drift_with_options_async(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DetectStackResourceDriftResponse().from_map(
            await self.do_request_async('DetectStackResourceDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detect_stack_resource_drift(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_resource_drift_with_options(request, runtime)

    async def detect_stack_resource_drift_async(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_resource_drift_with_options_async(request, runtime)

    def detect_stack_drift_with_options(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackDriftResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DetectStackDriftResponse().from_map(
            self.do_request('DetectStackDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def detect_stack_drift_with_options_async(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackDriftResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DetectStackDriftResponse().from_map(
            await self.do_request_async('DetectStackDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detect_stack_drift(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
    ) -> ros20190910_models.DetectStackDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_drift_with_options(request, runtime)

    async def detect_stack_drift_async(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
    ) -> ros20190910_models.DetectStackDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_drift_with_options_async(request, runtime)

    def update_stack_instances_with_options(
        self,
        tmp: ros20190910_models.UpdateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.UpdateStackInstancesResponse().from_map(
            self.do_request('UpdateStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_stack_instances_with_options_async(
        self,
        tmp: ros20190910_models.UpdateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.UpdateStackInstancesResponse().from_map(
            await self.do_request_async('UpdateStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_stack_instances(
        self,
        request: ros20190910_models.UpdateStackInstancesRequest,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_instances_with_options(request, runtime)

    async def update_stack_instances_async(
        self,
        request: ros20190910_models.UpdateStackInstancesRequest,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_instances_with_options_async(request, runtime)

    def list_stack_group_operations_with_options(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupOperationsResponse().from_map(
            self.do_request('ListStackGroupOperations', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_group_operations_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupOperationsResponse().from_map(
            await self.do_request_async('ListStackGroupOperations', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_group_operations(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operations_with_options(request, runtime)

    async def list_stack_group_operations_async(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_group_operations_with_options_async(request, runtime)

    def get_stack_group_with_options(
        self,
        request: ros20190910_models.GetStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackGroupResponse().from_map(
            self.do_request('GetStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_stack_group_with_options_async(
        self,
        request: ros20190910_models.GetStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackGroupResponse().from_map(
            await self.do_request_async('GetStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_stack_group(
        self,
        request: ros20190910_models.GetStackGroupRequest,
    ) -> ros20190910_models.GetStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_with_options(request, runtime)

    async def get_stack_group_async(
        self,
        request: ros20190910_models.GetStackGroupRequest,
    ) -> ros20190910_models.GetStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_group_with_options_async(request, runtime)

    def get_stack_group_operation_with_options(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackGroupOperationResponse().from_map(
            self.do_request('GetStackGroupOperation', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_stack_group_operation_with_options_async(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackGroupOperationResponse().from_map(
            await self.do_request_async('GetStackGroupOperation', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_stack_group_operation(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_operation_with_options(request, runtime)

    async def get_stack_group_operation_async(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_group_operation_with_options_async(request, runtime)

    def list_stack_groups_with_options(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupsResponse().from_map(
            self.do_request('ListStackGroups', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_groups_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupsResponse().from_map(
            await self.do_request_async('ListStackGroups', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_groups(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
    ) -> ros20190910_models.ListStackGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_groups_with_options(request, runtime)

    async def list_stack_groups_async(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
    ) -> ros20190910_models.ListStackGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_groups_with_options_async(request, runtime)

    def create_stack_instances_with_options(
        self,
        tmp: ros20190910_models.CreateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.CreateStackInstancesResponse().from_map(
            self.do_request('CreateStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_stack_instances_with_options_async(
        self,
        tmp: ros20190910_models.CreateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.CreateStackInstancesResponse().from_map(
            await self.do_request_async('CreateStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_stack_instances(
        self,
        request: ros20190910_models.CreateStackInstancesRequest,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stack_instances_with_options(request, runtime)

    async def create_stack_instances_async(
        self,
        request: ros20190910_models.CreateStackInstancesRequest,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_instances_with_options_async(request, runtime)

    def create_stack_group_with_options(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackGroupResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateStackGroupResponse().from_map(
            self.do_request('CreateStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_stack_group_with_options_async(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackGroupResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateStackGroupResponse().from_map(
            await self.do_request_async('CreateStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_stack_group(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
    ) -> ros20190910_models.CreateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stack_group_with_options(request, runtime)

    async def create_stack_group_async(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
    ) -> ros20190910_models.CreateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_group_with_options_async(request, runtime)

    def get_stack_instance_with_options(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackInstanceResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackInstanceResponse().from_map(
            self.do_request('GetStackInstance', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_stack_instance_with_options_async(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackInstanceResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackInstanceResponse().from_map(
            await self.do_request_async('GetStackInstance', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_stack_instance(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
    ) -> ros20190910_models.GetStackInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_instance_with_options(request, runtime)

    async def get_stack_instance_async(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
    ) -> ros20190910_models.GetStackInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_instance_with_options_async(request, runtime)

    def update_stack_group_with_options(
        self,
        tmp: ros20190910_models.UpdateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.UpdateStackGroupResponse().from_map(
            self.do_request('UpdateStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_stack_group_with_options_async(
        self,
        tmp: ros20190910_models.UpdateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.UpdateStackGroupResponse().from_map(
            await self.do_request_async('UpdateStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_stack_group(
        self,
        request: ros20190910_models.UpdateStackGroupRequest,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_group_with_options(request, runtime)

    async def update_stack_group_async(
        self,
        request: ros20190910_models.UpdateStackGroupRequest,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_group_with_options_async(request, runtime)

    def list_stack_instances_with_options(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackInstancesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackInstancesResponse().from_map(
            self.do_request('ListStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_instances_with_options_async(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackInstancesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackInstancesResponse().from_map(
            await self.do_request_async('ListStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_instances(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
    ) -> ros20190910_models.ListStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_instances_with_options(request, runtime)

    async def list_stack_instances_async(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
    ) -> ros20190910_models.ListStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_instances_with_options_async(request, runtime)

    def list_stack_group_operation_results_with_options(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupOperationResultsResponse().from_map(
            self.do_request('ListStackGroupOperationResults', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_group_operation_results_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupOperationResultsResponse().from_map(
            await self.do_request_async('ListStackGroupOperationResults', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_group_operation_results(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operation_results_with_options(request, runtime)

    async def list_stack_group_operation_results_async(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_group_operation_results_with_options_async(request, runtime)

    def stop_stack_group_operation_with_options(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.StopStackGroupOperationResponse().from_map(
            self.do_request('StopStackGroupOperation', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def stop_stack_group_operation_with_options_async(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.StopStackGroupOperationResponse().from_map(
            await self.do_request_async('StopStackGroupOperation', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_stack_group_operation(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_stack_group_operation_with_options(request, runtime)

    async def stop_stack_group_operation_async(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_stack_group_operation_with_options_async(request, runtime)

    def delete_stack_group_with_options(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteStackGroupResponse().from_map(
            self.do_request('DeleteStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_stack_group_with_options_async(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteStackGroupResponse().from_map(
            await self.do_request_async('DeleteStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_stack_group(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_group_with_options(request, runtime)

    async def delete_stack_group_async(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_group_with_options_async(request, runtime)

    def delete_stack_instances_with_options(
        self,
        tmp: ros20190910_models.DeleteStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.DeleteStackInstancesResponse().from_map(
            self.do_request('DeleteStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_stack_instances_with_options_async(
        self,
        tmp: ros20190910_models.DeleteStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        UtilClient.validate_model(tmp)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.DeleteStackInstancesResponse().from_map(
            await self.do_request_async('DeleteStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_stack_instances(
        self,
        request: ros20190910_models.DeleteStackInstancesRequest,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_instances_with_options(request, runtime)

    async def delete_stack_instances_async(
        self,
        request: ros20190910_models.DeleteStackInstancesRequest,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_instances_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagResourcesResponse().from_map(
            self.do_request('ListTagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagResourcesResponse().from_map(
            await self.do_request_async('ListTagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_tag_resources(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
    ) -> ros20190910_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
    ) -> ros20190910_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ros20190910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UntagResourcesResponse().from_map(
            self.do_request('UntagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ros20190910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UntagResourcesResponse().from_map(
            await self.do_request_async('UntagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def untag_resources(
        self,
        request: ros20190910_models.UntagResourcesRequest,
    ) -> ros20190910_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ros20190910_models.UntagResourcesRequest,
    ) -> ros20190910_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ros20190910_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.TagResourcesResponse().from_map(
            self.do_request('TagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ros20190910_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.TagResourcesResponse().from_map(
            await self.do_request_async('TagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def tag_resources(
        self,
        request: ros20190910_models.TagResourcesRequest,
    ) -> ros20190910_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ros20190910_models.TagResourcesRequest,
    ) -> ros20190910_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteTemplateResponse().from_map(
            self.do_request('DeleteTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteTemplateResponse().from_map(
            await self.do_request_async('DeleteTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_template(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
    ) -> ros20190910_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
    ) -> ros20190910_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateTemplateResponse().from_map(
            self.do_request('UpdateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_template_with_options_async(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateTemplateResponse().from_map(
            await self.do_request_async('UpdateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_template(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
    ) -> ros20190910_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
    ) -> ros20190910_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: ros20190910_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTemplatesResponse().from_map(
            self.do_request('ListTemplates', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: ros20190910_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListTemplatesResponse().from_map(
            await self.do_request_async('ListTemplates', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_templates(
        self,
        request: ros20190910_models.ListTemplatesRequest,
    ) -> ros20190910_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: ros20190910_models.ListTemplatesRequest,
    ) -> ros20190910_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: ros20190910_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateTemplateResponse().from_map(
            self.do_request('CreateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_template_with_options_async(
        self,
        request: ros20190910_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateTemplateResponse().from_map(
            await self.do_request_async('CreateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_template(
        self,
        request: ros20190910_models.CreateTemplateRequest,
    ) -> ros20190910_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: ros20190910_models.CreateTemplateRequest,
    ) -> ros20190910_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def create_stack_with_options(
        self,
        request: ros20190910_models.CreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateStackResponse().from_map(
            self.do_request('CreateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_stack_with_options_async(
        self,
        request: ros20190910_models.CreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateStackResponse().from_map(
            await self.do_request_async('CreateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_stack(
        self,
        request: ros20190910_models.CreateStackRequest,
    ) -> ros20190910_models.CreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stack_with_options(request, runtime)

    async def create_stack_async(
        self,
        request: ros20190910_models.CreateStackRequest,
    ) -> ros20190910_models.CreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: ros20190910_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackResponse().from_map(
            self.do_request('GetStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: ros20190910_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackResponse().from_map(
            await self.do_request_async('GetStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_stack(
        self,
        request: ros20190910_models.GetStackRequest,
    ) -> ros20190910_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: ros20190910_models.GetStackRequest,
    ) -> ros20190910_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def delete_stack_with_options(
        self,
        request: ros20190910_models.DeleteStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteStackResponse().from_map(
            self.do_request('DeleteStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_stack_with_options_async(
        self,
        request: ros20190910_models.DeleteStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteStackResponse().from_map(
            await self.do_request_async('DeleteStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_stack(
        self,
        request: ros20190910_models.DeleteStackRequest,
    ) -> ros20190910_models.DeleteStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_with_options(request, runtime)

    async def delete_stack_async(
        self,
        request: ros20190910_models.DeleteStackRequest,
    ) -> ros20190910_models.DeleteStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_with_options_async(request, runtime)

    def update_stack_with_options(
        self,
        request: ros20190910_models.UpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateStackResponse().from_map(
            self.do_request('UpdateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_stack_with_options_async(
        self,
        request: ros20190910_models.UpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateStackResponse().from_map(
            await self.do_request_async('UpdateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_stack(
        self,
        request: ros20190910_models.UpdateStackRequest,
    ) -> ros20190910_models.UpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_with_options(request, runtime)

    async def update_stack_async(
        self,
        request: ros20190910_models.UpdateStackRequest,
    ) -> ros20190910_models.UpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_with_options_async(request, runtime)

    def list_stacks_with_options(
        self,
        request: ros20190910_models.ListStacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStacksResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStacksResponse().from_map(
            self.do_request('ListStacks', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stacks_with_options_async(
        self,
        request: ros20190910_models.ListStacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStacksResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStacksResponse().from_map(
            await self.do_request_async('ListStacks', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stacks(
        self,
        request: ros20190910_models.ListStacksRequest,
    ) -> ros20190910_models.ListStacksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stacks_with_options(request, runtime)

    async def list_stacks_async(
        self,
        request: ros20190910_models.ListStacksRequest,
    ) -> ros20190910_models.ListStacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stacks_with_options_async(request, runtime)

    def preview_stack_with_options(
        self,
        request: ros20190910_models.PreviewStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.PreviewStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.PreviewStackResponse().from_map(
            self.do_request('PreviewStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def preview_stack_with_options_async(
        self,
        request: ros20190910_models.PreviewStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.PreviewStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.PreviewStackResponse().from_map(
            await self.do_request_async('PreviewStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def preview_stack(
        self,
        request: ros20190910_models.PreviewStackRequest,
    ) -> ros20190910_models.PreviewStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.preview_stack_with_options(request, runtime)

    async def preview_stack_async(
        self,
        request: ros20190910_models.PreviewStackRequest,
    ) -> ros20190910_models.PreviewStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preview_stack_with_options_async(request, runtime)

    def get_template_estimate_cost_with_options(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateEstimateCostResponse().from_map(
            self.do_request('GetTemplateEstimateCost', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_template_estimate_cost_with_options_async(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateEstimateCostResponse().from_map(
            await self.do_request_async('GetTemplateEstimateCost', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_template_estimate_cost(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_estimate_cost_with_options(request, runtime)

    async def get_template_estimate_cost_async(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_estimate_cost_with_options_async(request, runtime)

    def cancel_update_stack_with_options(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CancelUpdateStackResponse().from_map(
            self.do_request('CancelUpdateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_update_stack_with_options_async(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CancelUpdateStackResponse().from_map(
            await self.do_request_async('CancelUpdateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_update_stack(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_update_stack_with_options(request, runtime)

    async def cancel_update_stack_async(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_update_stack_with_options_async(request, runtime)

    def continue_create_stack_with_options(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ContinueCreateStackResponse().from_map(
            self.do_request('ContinueCreateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def continue_create_stack_with_options_async(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ContinueCreateStackResponse().from_map(
            await self.do_request_async('ContinueCreateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def continue_create_stack(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.continue_create_stack_with_options(request, runtime)

    async def continue_create_stack_async(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.continue_create_stack_with_options_async(request, runtime)

    def set_stack_policy_with_options(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetStackPolicyResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SetStackPolicyResponse().from_map(
            self.do_request('SetStackPolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_stack_policy_with_options_async(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetStackPolicyResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SetStackPolicyResponse().from_map(
            await self.do_request_async('SetStackPolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_stack_policy(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
    ) -> ros20190910_models.SetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_stack_policy_with_options(request, runtime)

    async def set_stack_policy_async(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
    ) -> ros20190910_models.SetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_stack_policy_with_options_async(request, runtime)

    def get_stack_policy_with_options(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackPolicyResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackPolicyResponse().from_map(
            self.do_request('GetStackPolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_stack_policy_with_options_async(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackPolicyResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackPolicyResponse().from_map(
            await self.do_request_async('GetStackPolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_stack_policy(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
    ) -> ros20190910_models.GetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_policy_with_options(request, runtime)

    async def get_stack_policy_async(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
    ) -> ros20190910_models.GetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_policy_with_options_async(request, runtime)

    def validate_template_with_options(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ValidateTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ValidateTemplateResponse().from_map(
            self.do_request('ValidateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def validate_template_with_options_async(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ValidateTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ValidateTemplateResponse().from_map(
            await self.do_request_async('ValidateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def validate_template(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
    ) -> ros20190910_models.ValidateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_template_with_options(request, runtime)

    async def validate_template_async(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
    ) -> ros20190910_models.ValidateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_template_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: ros20190910_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateResponse().from_map(
            self.do_request('GetTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_template_with_options_async(
        self,
        request: ros20190910_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateResponse().from_map(
            await self.do_request_async('GetTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_template(
        self,
        request: ros20190910_models.GetTemplateRequest,
    ) -> ros20190910_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: ros20190910_models.GetTemplateRequest,
    ) -> ros20190910_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_change_set_with_options(
        self,
        request: ros20190910_models.GetChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetChangeSetResponse().from_map(
            self.do_request('GetChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_change_set_with_options_async(
        self,
        request: ros20190910_models.GetChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetChangeSetResponse().from_map(
            await self.do_request_async('GetChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_change_set(
        self,
        request: ros20190910_models.GetChangeSetRequest,
    ) -> ros20190910_models.GetChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_change_set_with_options(request, runtime)

    async def get_change_set_async(
        self,
        request: ros20190910_models.GetChangeSetRequest,
    ) -> ros20190910_models.GetChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_change_set_with_options_async(request, runtime)

    def list_change_sets_with_options(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListChangeSetsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListChangeSetsResponse().from_map(
            self.do_request('ListChangeSets', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_change_sets_with_options_async(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListChangeSetsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListChangeSetsResponse().from_map(
            await self.do_request_async('ListChangeSets', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_change_sets(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
    ) -> ros20190910_models.ListChangeSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_change_sets_with_options(request, runtime)

    async def list_change_sets_async(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
    ) -> ros20190910_models.ListChangeSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_change_sets_with_options_async(request, runtime)

    def execute_change_set_with_options(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ExecuteChangeSetResponse().from_map(
            self.do_request('ExecuteChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def execute_change_set_with_options_async(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ExecuteChangeSetResponse().from_map(
            await self.do_request_async('ExecuteChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def execute_change_set(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_change_set_with_options(request, runtime)

    async def execute_change_set_async(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_change_set_with_options_async(request, runtime)

    def delete_change_set_with_options(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteChangeSetResponse().from_map(
            self.do_request('DeleteChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_change_set_with_options_async(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteChangeSetResponse().from_map(
            await self.do_request_async('DeleteChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_change_set(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_change_set_with_options(request, runtime)

    async def delete_change_set_async(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_change_set_with_options_async(request, runtime)

    def list_stack_events_with_options(
        self,
        request: ros20190910_models.ListStackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackEventsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackEventsResponse().from_map(
            self.do_request('ListStackEvents', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_events_with_options_async(
        self,
        request: ros20190910_models.ListStackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackEventsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackEventsResponse().from_map(
            await self.do_request_async('ListStackEvents', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_events(
        self,
        request: ros20190910_models.ListStackEventsRequest,
    ) -> ros20190910_models.ListStackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_events_with_options(request, runtime)

    async def list_stack_events_async(
        self,
        request: ros20190910_models.ListStackEventsRequest,
    ) -> ros20190910_models.ListStackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_events_with_options_async(request, runtime)

    def list_stack_resources_with_options(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackResourcesResponse().from_map(
            self.do_request('ListStackResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_stack_resources_with_options_async(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourcesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackResourcesResponse().from_map(
            await self.do_request_async('ListStackResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_stack_resources(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
    ) -> ros20190910_models.ListStackResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resources_with_options(request, runtime)

    async def list_stack_resources_async(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
    ) -> ros20190910_models.ListStackResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_resources_with_options_async(request, runtime)

    def get_stack_resource_with_options(
        self,
        request: ros20190910_models.GetStackResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResourceResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackResourceResponse().from_map(
            self.do_request('GetStackResource', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_stack_resource_with_options_async(
        self,
        request: ros20190910_models.GetStackResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResourceResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackResourceResponse().from_map(
            await self.do_request_async('GetStackResource', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_stack_resource(
        self,
        request: ros20190910_models.GetStackResourceRequest,
    ) -> ros20190910_models.GetStackResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_resource_with_options(request, runtime)

    async def get_stack_resource_async(
        self,
        request: ros20190910_models.GetStackResourceRequest,
    ) -> ros20190910_models.GetStackResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_resource_with_options_async(request, runtime)

    def get_resource_type_template_with_options(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetResourceTypeTemplateResponse().from_map(
            self.do_request('GetResourceTypeTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_resource_type_template_with_options_async(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetResourceTypeTemplateResponse().from_map(
            await self.do_request_async('GetResourceTypeTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_resource_type_template(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_template_with_options(request, runtime)

    async def get_resource_type_template_async(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_type_template_with_options_async(request, runtime)

    def get_resource_type_with_options(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetResourceTypeResponse().from_map(
            self.do_request('GetResourceType', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.GetResourceTypeResponse().from_map(
            await self.do_request_async('GetResourceType', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_resource_type(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
    ) -> ros20190910_models.GetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_with_options(request, runtime)

    async def get_resource_type_async(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
    ) -> ros20190910_models.GetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_type_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListResourceTypesResponse().from_map(
            self.do_request('ListResourceTypes', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypesResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.ListResourceTypesResponse().from_map(
            await self.do_request_async('ListResourceTypes', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_resource_types(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
    ) -> ros20190910_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    async def list_resource_types_async(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
    ) -> ros20190910_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_types_with_options_async(request, runtime)

    def signal_resource_with_options(
        self,
        request: ros20190910_models.SignalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SignalResourceResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SignalResourceResponse().from_map(
            self.do_request('SignalResource', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def signal_resource_with_options_async(
        self,
        request: ros20190910_models.SignalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SignalResourceResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.SignalResourceResponse().from_map(
            await self.do_request_async('SignalResource', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def signal_resource(
        self,
        request: ros20190910_models.SignalResourceRequest,
    ) -> ros20190910_models.SignalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.signal_resource_with_options(request, runtime)

    async def signal_resource_async(
        self,
        request: ros20190910_models.SignalResourceRequest,
    ) -> ros20190910_models.SignalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.signal_resource_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DescribeRegionsResponse().from_map(
            self.do_request('DescribeRegions', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.DescribeRegionsResponse().from_map(
            await self.do_request_async('DescribeRegions', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def describe_regions(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
    ) -> ros20190910_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
    ) -> ros20190910_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def create_change_set_with_options(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateChangeSetResponse().from_map(
            self.do_request('CreateChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_change_set_with_options_async(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateChangeSetResponse:
        UtilClient.validate_model(request)
        return ros20190910_models.CreateChangeSetResponse().from_map(
            await self.do_request_async('CreateChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_change_set(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
    ) -> ros20190910_models.CreateChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_change_set_with_options(request, runtime)

    async def create_change_set_async(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
    ) -> ros20190910_models.CreateChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_change_set_with_options_async(request, runtime)

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
