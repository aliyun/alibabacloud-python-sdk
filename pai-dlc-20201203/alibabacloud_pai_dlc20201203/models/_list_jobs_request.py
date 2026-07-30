# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        business_user_id: str = None,
        caller: str = None,
        description: str = None,
        display_name: str = None,
        display_name_search_mode: str = None,
        enable_assign_node: str = None,
        end_time: str = None,
        from_all_workspaces: bool = None,
        image_search: str = None,
        job_id: str = None,
        job_ids: str = None,
        job_type: str = None,
        numeric_range_field: str = None,
        numeric_range_max: int = None,
        numeric_range_min: int = None,
        order: str = None,
        oversold_info: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        pipeline_id: str = None,
        reason_search: str = None,
        resource_id: str = None,
        resource_ids: str = None,
        resource_quota_name: str = None,
        show_own: bool = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        tags: Dict[str, str] = None,
        template_id: str = None,
        time_range_field: str = None,
        user_command_search: str = None,
        user_id_for_filter: str = None,
        username: str = None,
        workspace_id: str = None,
    ):
        # The visibility of the job. Valid values:
        # - PUBLIC: Visible to all members in the workspace.
        # - PRIVATE (default): Visible only to you and administrators in the workspace.
        self.accessibility = accessibility
        # The user ID associated with the job.
        self.business_user_id = business_user_id
        # The caller.
        self.caller = caller
        self.description = description
        # The job name. Supports fuzzy match and is case-insensitive. Wildcards are not supported.
        # For example, entering test matches test-job1, job-test, job-test2, or job-Test, but does not match job-t1.
        # Default value: empty, which indicates all job names.
        self.display_name = display_name
        # The search mode for DisplayName. Default value: wildcard match.
        self.display_name_search_mode = display_name_search_mode
        # Filters jobs based on whether running on specified nodes is enabled.
        self.enable_assign_node = enable_assign_node
        # The end time of the query range. The job creation time is used for filtering. Default value: the current time.
        self.end_time = end_time
        # Specifies whether to retrieve jobs across all workspaces. This parameter must be used together with `ShowOwn=true` to query jobs recently submitted by the current user.
        self.from_all_workspaces = from_all_workspaces
        # Retrieves nodes by performing a full-text index on the images field. Supports Chinese and English tokenization.
        self.image_search = image_search
        # The job ID. Fuzzy match is not supported. Case-insensitive. Wildcards are not supported.
        # Default value: empty, which indicates all job IDs.
        self.job_id = job_id
        # A list of job IDs separated by commas. If both JobIds and JobId are specified, JobId takes precedence.
        self.job_ids = job_ids
        # The job type. Default value: empty, which indicates all types. Valid values:
        # - TFJob
        # - PyTorchJob
        # - XGBoostJob
        # - OneFlowJob
        # - ElasticBatchJob
        self.job_type = job_type
        # The field name for numeric range filtering. Must be used together with NumericRangeMin/NumericRangeMax.
        self.numeric_range_field = numeric_range_field
        # The maximum value (inclusive) for numeric range filtering. Must be used together with NumericRangeField.
        self.numeric_range_max = numeric_range_max
        # The minimum value (inclusive) for numeric range filtering. Must be used together with NumericRangeField.
        self.numeric_range_min = numeric_range_min
        # The sort order. Valid values:
        # 
        # - desc: Descending order. This is the default value.
        # - asc: Ascending order.
        self.order = order
        # The idle resource information. Valid values:
        # - ForbiddenQuotaOverSold
        # - ForceQuotaOverSold
        # - AcceptQuotaOverSold-true (true indicates the job actually used idle resources)
        # - AcceptQuotaOverSold-false (false indicates the job actually used guaranteed resources)
        self.oversold_info = oversold_info
        # The page number to return in a paged query. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of jobs to return per page.
        self.page_size = page_size
        # The resource type. Valid values:
        # - PrePaid: resource quota.
        # - Spot: preemptible resources.
        # - PostPaid: public resources.
        self.payment_type = payment_type
        # Filters jobs created by the specified workflow ID.
        self.pipeline_id = pipeline_id
        # Retrieves nodes by performing a full-text index on the node failed reason field. Supports Chinese and English tokenization.
        self.reason_search = reason_search
        # The resource group ID. For information about how to query the dedicated resource group ID, see [Manage resource quotas](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        self.resource_ids = resource_ids
        # Filters the job list by the resource quota name. Supports fuzzy match. Wildcards are not supported. Default value: empty, which indicates no filtering by resource quota.
        self.resource_quota_name = resource_quota_name
        # Specifies whether to return only jobs submitted by the current user.
        self.show_own = show_own
        # The field by which to sort results:
        # 
        # - DisplayName
        # - JobType
        # - Status
        # - GmtCreateTime
        # - GmtFinishTime
        self.sort_by = sort_by
        # The start time of the query range. The job creation time is used for filtering. Default value: the current time minus 7 days. If neither StartTime nor EndTime is specified, jobs from the last 7 days are returned by default.
        self.start_time = start_time
        # The job status. Valid values:
        # - Creating
        # - Queuing
        # - Bidding (currently only for Lingjun Spot jobs)
        # - EnvPreparing
        # - SanityChecking
        # - Running
        # - Restarting
        # - Stopping
        # - SucceededReserving
        # - FailedReserving
        # - Succeeded
        # - Failed
        # - Stopped
        self.status = status
        # The tags used for filtering.
        self.tags = tags
        # The template ID. Filters jobs created from the specified template.
        self.template_id = template_id
        # The time field used for StartTime/EndTime filtering. Default value: creation time.
        self.time_range_field = time_range_field
        # Retrieves nodes by performing a full-text index on the user_command field. Supports Chinese and English tokenization.
        self.user_command_search = user_command_search
        # Filters the job list by the user ID of the job submitter.
        self.user_id_for_filter = user_id_for_filter
        # Filters the job list by the username of the job submitter. Supports fuzzy match. Wildcards are not supported. Default value: empty, which indicates no filtering by username.
        self.username = username
        # The workspace ID. <props="china">For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_search_mode is not None:
            result['DisplayNameSearchMode'] = self.display_name_search_mode

        if self.enable_assign_node is not None:
            result['EnableAssignNode'] = self.enable_assign_node

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.from_all_workspaces is not None:
            result['FromAllWorkspaces'] = self.from_all_workspaces

        if self.image_search is not None:
            result['ImageSearch'] = self.image_search

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_ids is not None:
            result['JobIds'] = self.job_ids

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.numeric_range_field is not None:
            result['NumericRangeField'] = self.numeric_range_field

        if self.numeric_range_max is not None:
            result['NumericRangeMax'] = self.numeric_range_max

        if self.numeric_range_min is not None:
            result['NumericRangeMin'] = self.numeric_range_min

        if self.order is not None:
            result['Order'] = self.order

        if self.oversold_info is not None:
            result['OversoldInfo'] = self.oversold_info

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.reason_search is not None:
            result['ReasonSearch'] = self.reason_search

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_quota_name is not None:
            result['ResourceQuotaName'] = self.resource_quota_name

        if self.show_own is not None:
            result['ShowOwn'] = self.show_own

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.time_range_field is not None:
            result['TimeRangeField'] = self.time_range_field

        if self.user_command_search is not None:
            result['UserCommandSearch'] = self.user_command_search

        if self.user_id_for_filter is not None:
            result['UserIdForFilter'] = self.user_id_for_filter

        if self.username is not None:
            result['Username'] = self.username

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameSearchMode') is not None:
            self.display_name_search_mode = m.get('DisplayNameSearchMode')

        if m.get('EnableAssignNode') is not None:
            self.enable_assign_node = m.get('EnableAssignNode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FromAllWorkspaces') is not None:
            self.from_all_workspaces = m.get('FromAllWorkspaces')

        if m.get('ImageSearch') is not None:
            self.image_search = m.get('ImageSearch')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobIds') is not None:
            self.job_ids = m.get('JobIds')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('NumericRangeField') is not None:
            self.numeric_range_field = m.get('NumericRangeField')

        if m.get('NumericRangeMax') is not None:
            self.numeric_range_max = m.get('NumericRangeMax')

        if m.get('NumericRangeMin') is not None:
            self.numeric_range_min = m.get('NumericRangeMin')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OversoldInfo') is not None:
            self.oversold_info = m.get('OversoldInfo')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ReasonSearch') is not None:
            self.reason_search = m.get('ReasonSearch')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceQuotaName') is not None:
            self.resource_quota_name = m.get('ResourceQuotaName')

        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TimeRangeField') is not None:
            self.time_range_field = m.get('TimeRangeField')

        if m.get('UserCommandSearch') is not None:
            self.user_command_search = m.get('UserCommandSearch')

        if m.get('UserIdForFilter') is not None:
            self.user_id_for_filter = m.get('UserIdForFilter')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

