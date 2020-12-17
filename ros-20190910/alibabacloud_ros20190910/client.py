# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ros20190910 import models as ros20190910_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ros', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def generate_template_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GenerateTemplatePolicyResponse().from_map(self.do_request('GenerateTemplatePolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def generate_template_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_template_policy_with_options(request, runtime)

    def list_template_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListTemplateVersionsResponse().from_map(self.do_request('ListTemplateVersions', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_template_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    def set_template_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.SetTemplatePermissionResponse().from_map(self.do_request('SetTemplatePermission', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def set_template_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_template_permission_with_options(request, runtime)

    def list_stack_operation_risks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackOperationRisksResponse().from_map(self.do_request('ListStackOperationRisks', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_operation_risks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_operation_risks_with_options(request, runtime)

    def get_template_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateSummaryResponse().from_map(self.do_request('GetTemplateSummary', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_template_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_summary_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagValuesResponse().from_map(self.do_request('ListTagValues', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_tag_values(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagKeysResponse().from_map(self.do_request('ListTagKeys', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def set_deletion_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.SetDeletionProtectionResponse().from_map(self.do_request('SetDeletionProtection', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def set_deletion_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    def update_stack_template_by_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateStackTemplateByResourcesResponse().from_map(self.do_request('UpdateStackTemplateByResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def update_stack_template_by_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_template_by_resources_with_options(request, runtime)

    def get_stack_drift_detection_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackDriftDetectionStatusResponse().from_map(self.do_request('GetStackDriftDetectionStatus', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_stack_drift_detection_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_drift_detection_status_with_options(request, runtime)

    def detect_stack_group_drift_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.DetectStackGroupDriftResponse().from_map(self.do_request('DetectStackGroupDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def detect_stack_group_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_group_drift_with_options(request, runtime)

    def list_stack_resource_drifts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackResourceDriftsResponse().from_map(self.do_request('ListStackResourceDrifts', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_resource_drifts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resource_drifts_with_options(request, runtime)

    def detect_stack_resource_drift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.DetectStackResourceDriftResponse().from_map(self.do_request('DetectStackResourceDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def detect_stack_resource_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_resource_drift_with_options(request, runtime)

    def detect_stack_drift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.DetectStackDriftResponse().from_map(self.do_request('DetectStackDrift', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def detect_stack_drift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_drift_with_options(request, runtime)

    def update_stack_instances_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.UpdateStackInstancesResponse().from_map(self.do_request('UpdateStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def update_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_instances_with_options(request, runtime)

    def list_stack_group_operations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupOperationsResponse().from_map(self.do_request('ListStackGroupOperations', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_group_operations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operations_with_options(request, runtime)

    def get_stack_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackGroupResponse().from_map(self.do_request('GetStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_with_options(request, runtime)

    def get_stack_group_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackGroupOperationResponse().from_map(self.do_request('GetStackGroupOperation', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_stack_group_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_operation_with_options(request, runtime)

    def list_stack_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupsResponse().from_map(self.do_request('ListStackGroups', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_groups_with_options(request, runtime)

    def create_stack_instances_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.CreateStackInstancesResponse().from_map(self.do_request('CreateStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def create_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_instances_with_options(request, runtime)

    def create_stack_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.CreateStackGroupResponse().from_map(self.do_request('CreateStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def create_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_group_with_options(request, runtime)

    def get_stack_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackInstanceResponse().from_map(self.do_request('GetStackInstance', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_stack_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_instance_with_options(request, runtime)

    def update_stack_group_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.UpdateStackGroupResponse().from_map(self.do_request('UpdateStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def update_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_group_with_options(request, runtime)

    def list_stack_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackInstancesResponse().from_map(self.do_request('ListStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_instances_with_options(request, runtime)

    def list_stack_group_operation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackGroupOperationResultsResponse().from_map(self.do_request('ListStackGroupOperationResults', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_group_operation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operation_results_with_options(request, runtime)

    def stop_stack_group_operation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.StopStackGroupOperationResponse().from_map(self.do_request('StopStackGroupOperation', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def stop_stack_group_operation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_stack_group_operation_with_options(request, runtime)

    def delete_stack_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteStackGroupResponse().from_map(self.do_request('DeleteStackGroup', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_stack_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_group_with_options(request, runtime)

    def delete_stack_instances_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.account_ids):
            request.account_ids_shrink = UtilClient.to_jsonstring(tmp.account_ids)
        if not UtilClient.is_unset(tmp.region_ids):
            request.region_ids_shrink = UtilClient.to_jsonstring(tmp.region_ids)
        if not UtilClient.is_unset(tmp.operation_preferences):
            request.operation_preferences_shrink = UtilClient.to_jsonstring(tmp.operation_preferences)
        return ros20190910_models.DeleteStackInstancesResponse().from_map(self.do_request('DeleteStackInstances', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_stack_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_instances_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListTagResourcesResponse().from_map(self.do_request('ListTagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.UntagResourcesResponse().from_map(self.do_request('UntagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.TagResourcesResponse().from_map(self.do_request('TagResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteTemplateResponse().from_map(self.do_request('DeleteTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def update_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateTemplateResponse().from_map(self.do_request('UpdateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def update_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    def list_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListTemplatesResponse().from_map(self.do_request('ListTemplates', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.CreateTemplateResponse().from_map(self.do_request('CreateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def create_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.CreateStackResponse().from_map(self.do_request('CreateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def create_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stack_with_options(request, runtime)

    def get_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackResponse().from_map(self.do_request('GetStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    def delete_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteStackResponse().from_map(self.do_request('DeleteStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_with_options(request, runtime)

    def update_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.UpdateStackResponse().from_map(self.do_request('UpdateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def update_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_stack_with_options(request, runtime)

    def list_stacks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStacksResponse().from_map(self.do_request('ListStacks', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stacks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stacks_with_options(request, runtime)

    def preview_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.PreviewStackResponse().from_map(self.do_request('PreviewStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def preview_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.preview_stack_with_options(request, runtime)

    def get_template_estimate_cost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateEstimateCostResponse().from_map(self.do_request('GetTemplateEstimateCost', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_template_estimate_cost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_estimate_cost_with_options(request, runtime)

    def cancel_update_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.CancelUpdateStackResponse().from_map(self.do_request('CancelUpdateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def cancel_update_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_update_stack_with_options(request, runtime)

    def continue_create_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ContinueCreateStackResponse().from_map(self.do_request('ContinueCreateStack', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def continue_create_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continue_create_stack_with_options(request, runtime)

    def set_stack_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.SetStackPolicyResponse().from_map(self.do_request('SetStackPolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def set_stack_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_stack_policy_with_options(request, runtime)

    def get_stack_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackPolicyResponse().from_map(self.do_request('GetStackPolicy', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_stack_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_policy_with_options(request, runtime)

    def validate_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ValidateTemplateResponse().from_map(self.do_request('ValidateTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def validate_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.validate_template_with_options(request, runtime)

    def get_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetTemplateResponse().from_map(self.do_request('GetTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    def get_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetChangeSetResponse().from_map(self.do_request('GetChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_change_set_with_options(request, runtime)

    def list_change_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListChangeSetsResponse().from_map(self.do_request('ListChangeSets', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_change_sets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_change_sets_with_options(request, runtime)

    def execute_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ExecuteChangeSetResponse().from_map(self.do_request('ExecuteChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def execute_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_change_set_with_options(request, runtime)

    def delete_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.DeleteChangeSetResponse().from_map(self.do_request('DeleteChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def delete_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_change_set_with_options(request, runtime)

    def list_stack_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackEventsResponse().from_map(self.do_request('ListStackEvents', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_events_with_options(request, runtime)

    def list_stack_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListStackResourcesResponse().from_map(self.do_request('ListStackResources', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_stack_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resources_with_options(request, runtime)

    def get_stack_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetStackResourceResponse().from_map(self.do_request('GetStackResource', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_stack_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_resource_with_options(request, runtime)

    def get_resource_type_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetResourceTypeTemplateResponse().from_map(self.do_request('GetResourceTypeTemplate', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_resource_type_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_template_with_options(request, runtime)

    def get_resource_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.GetResourceTypeResponse().from_map(self.do_request('GetResourceType', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def get_resource_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_with_options(request, runtime)

    def list_resource_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.ListResourceTypesResponse().from_map(self.do_request('ListResourceTypes', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def list_resource_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    def signal_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.SignalResourceResponse().from_map(self.do_request('SignalResource', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def signal_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.signal_resource_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.DescribeRegionsResponse().from_map(self.do_request('DescribeRegions', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def create_change_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ros20190910_models.CreateChangeSetResponse().from_map(self.do_request('CreateChangeSet', 'HTTPS', 'POST', '2019-09-10', 'AK', None, TeaCore.to_map(request), runtime))

    def create_change_set(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_change_set_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
