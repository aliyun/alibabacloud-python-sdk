# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTensorboardsRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        display_name: str = None,
        end_time: str = None,
        job_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        quota_id: str = None,
        show_own: bool = None,
        sort_by: str = None,
        source_id: str = None,
        source_type: str = None,
        start_time: str = None,
        status: str = None,
        tensorboard_id: str = None,
        user_id: str = None,
        username: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The instance visibility.
        # 
        # *   PUBLIC: TensorBoard instances are visible to all members in the workspace.
        # *   PRIVATE: TensorBoard instances are visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The TensorBoard instance name.
        self.display_name = display_name
        # The end time of the query. Use the UTC time when the TensorBoard instance is created to filter data. If you leave this parameter empty, the default value is the current time.
        self.end_time = end_time
        # The job ID used to filter TensorBoard instances. For more information about how to obtain the ID of a job, see [ListJobs](https://help.aliyun.com/document_detail/459676.html).
        self.job_id = job_id
        # The sorting order.
        # 
        # *   desc
        # *   asc
        self.order = order
        # The page number. Minimum value: 1.
        self.page_number = page_number
        # The number of TensorBoard instances per page.
        self.page_size = page_size
        # The billing method of TensorBoard instances.
        # 
        # *   Free: the TensorBoard instance that uses free resources.
        # *   Postpaid: the TensorBoard instance that uses pay-as-you-go resources.
        self.payment_type = payment_type
        # The resource quota ID.
        # 
        # > 
        # 
        # *   Only whitelisted users can use resource quotas to create TensorBoard instances. If you want to use this feature, contact us.
        # 
        # *   This parameter takes effect only when TensorBoard instances use resource quotas.
        self.quota_id = quota_id
        # Specifies whether to return only the TensorBoard instances created by the current logon account.
        self.show_own = show_own
        # The returned field used to sort TensorBoard instances.
        # 
        # *   DisplayName: the name of the TensorBoard instance.
        # *   GmtCreateTime: the time when the TensorBoard instance is created.
        self.sort_by = sort_by
        # The data source ID. For more information about how to obtain the ID of a job, see [ListJobs](https://help.aliyun.com/document_detail/459676.html).
        self.source_id = source_id
        # The data source associated with the TensorBoard instance. This parameter is no longer used. Only Deep Learning Containers (DLC) training jobs are supported.
        self.source_type = source_type
        # The start time of the query. Use the UTC time when the TensorBoard instance is created to filter data. If you leave this parameter empty, the default value is seven days before the current time.
        self.start_time = start_time
        # The TensorBoard instance status. Valid values:
        # 
        # *   Creating
        # *   Running
        # *   Stopped
        # *   Succeeded
        # *   Failed
        self.status = status
        # The TensorBoard instance ID used to filter TensorBoard instances.
        self.tensorboard_id = tensorboard_id
        # The user ID.
        self.user_id = user_id
        # The username.
        self.username = username
        # Specifies whether to return the information about the TensorBoard instance.
        # 
        # *   true
        # *   false
        self.verbose = verbose
        # The workspace ID. Obtain a list of TensorBoard instances based on the workspace ID.
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

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.show_own is not None:
            result['ShowOwn'] = self.show_own

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

