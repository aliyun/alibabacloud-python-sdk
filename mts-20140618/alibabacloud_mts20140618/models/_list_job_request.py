# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobRequest(DaraModel):
    def __init__(
        self,
        end_of_job_created_time_range: str = None,
        maximum_page_size: int = None,
        next_page_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_of_job_created_time_range: str = None,
        state: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        self.end_of_job_created_time_range = end_of_job_created_time_range
        # The number of entries per page.
        # 
        # *   Default value: **10**.
        # *   Valid values: **1 to 100**.
        self.maximum_page_size = maximum_page_size
        # The token that is used to retrieve the next page of the query results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextPageToken.
        self.next_page_token = next_page_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the MPS queue to which the job is submitted. To obtain the ID of an MPS queue, you can log on to the [MPS console](https://mps.console.aliyun.com/overview) and choose **Global Settings** > **MPS Queue and Callback** in the left-side navigation pane.
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time must be in UTC.
        self.start_of_job_created_time_range = start_of_job_created_time_range
        # The state of the transcoding job. Default value: **All**. Valid values:
        # 
        # *   **All**
        # *   **Submitted**
        # *   **Transcoding**
        # *   **TranscodeSuccess**
        # *   **TranscodeFail**
        # *   **TranscodeCancelled**
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_of_job_created_time_range is not None:
            result['EndOfJobCreatedTimeRange'] = self.end_of_job_created_time_range

        if self.maximum_page_size is not None:
            result['MaximumPageSize'] = self.maximum_page_size

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_of_job_created_time_range is not None:
            result['StartOfJobCreatedTimeRange'] = self.start_of_job_created_time_range

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndOfJobCreatedTimeRange') is not None:
            self.end_of_job_created_time_range = m.get('EndOfJobCreatedTimeRange')

        if m.get('MaximumPageSize') is not None:
            self.maximum_page_size = m.get('MaximumPageSize')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartOfJobCreatedTimeRange') is not None:
            self.start_of_job_created_time_range = m.get('StartOfJobCreatedTimeRange')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

